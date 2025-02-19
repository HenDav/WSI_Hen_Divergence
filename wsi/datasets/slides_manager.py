from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple

import pandas
import numpy as np
from tqdm import tqdm

from ..core import constants
from ..core.metadata import MetadataBase
from ..core.wsi import Slide, SlideContext, Tile, TilesManager

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import QuantileTransformer, OrdinalEncoder


def default_predicate( #TODO: add as parameter list of columns_used
    df: pandas.DataFrame,
    # use_taular_data: bool, # determines if null values in the Taylor data's extra columns is used. If so, rows with inapproprite null values are bad.
    min_tiles: int,
    datasets_folds: Dict,
    target: str,
    secondary_target: str
) -> pandas.Index:
    if target == "none":
        df[target] = 1
    matching_indices = pandas.Index([])
    for ds in datasets_folds:
        fold_indices = df.index[df[constants.fold_column_name].isin(datasets_folds[ds])]
        dataset_indices = df.index[df[constants.dataset_id_column_name] == ds]
        matching_indices = matching_indices.union(dataset_indices.intersection(fold_indices))
    print(
        f"Found {len(matching_indices)} slides in datasets and folds {datasets_folds}"
    )
    min_tiles_indices = df.index[
        df[constants.legitimate_tiles_column_name] > min_tiles
    ]
    target_indices = df.index[
        df[target].notna()
    ]
    if secondary_target:
        secondary_indices = df.index[
            df[secondary_target].notna()
        ]  # TODO: review this and check possible column values
        target_indices = target_indices.intersection(secondary_indices)
        
    
    filtered_target = matching_indices.intersection(target_indices)
    filtered_min_tiles = filtered_target.intersection(min_tiles_indices)
    print(
        f"Filtering {len(matching_indices) - len(filtered_target)} slides without {'secondary_target or target' if secondary_target else 'target'} {target}, {len(filtered_target) - len(filtered_min_tiles)} that have less than {min_tiles} tiles"
    )

    

    return filtered_min_tiles


class SlidesManager(MetadataBase):
    def __init__(
        self,
        datasets_base_dir_path: Path,
        tile_size: int,
        desired_mpp: float,
        metadata_at_magnification: int,
        metadata_file_path: Path,
        target: str,
        row_predicate: Callable = default_predicate,  # [[pandas.DataFrame, ...], pandas.Index] somehow causes a bug, I have no idea why
        # use_taular_data: bool = False,
        # tabular_transform_pipeline: Callable = None,
        **predicate_args,
    ):
        self._desired_mpp = desired_mpp
        self._metadata_file_path = metadata_file_path
        self.target = target
        self._slides = []
        self._current_slides = []
        # self._tile_to_slide_dict = self._create_tile_to_slide_dict()
        MetadataBase.__init__(
            self,
            datasets_base_dir_path=datasets_base_dir_path,
            tile_size=tile_size,
            metadata_at_magnification=metadata_at_magnification,
            desired_mpp=desired_mpp,
        )
        
        self._df[self.target] = self.make_target_column()
        self._df = self._df.iloc[row_predicate(self._df, target=target, **predicate_args)].reset_index()
        self._current_slides = self._create_slides()
        self._tiles_df = self._create_tiles_df()

        # self.tabular_transform_pipeline = tabular_transform_pipeline if tabular_transform_pipeline else self._create_transform_pipeline()

    def __len__(self) -> int:
        return len(self._df)

    def _create_tiles_df(self) -> pandas.DataFrame:
        tiles_dfs = [slide._tiles_df.assign(slide_idx=idx).drop(columns=[TilesManager.tile_index,]) for idx, slide in enumerate(self._current_slides)]
        tiles_df = pandas.concat(tiles_dfs) if len(tiles_dfs)>1 else tiles_dfs[0]
        return tiles_df
    
    def _create_slides(self) -> List[Slide]:
        slides = []
        row_index = 0
        for idx in tqdm(self._df.index, desc="Loading slides"):
            slide_context = SlideContext(
                row_index=row_index,
                metadata=self._df,
                dataset_paths=self._dataset_paths,
                desired_mpp=self._desired_mpp,
                tile_size=self._tile_size,
            )
            slide = Slide(slide_context=slide_context)
            slides.append(slide)
            row_index += 1

        self._file_name_to_slide = self._create_file_name_to_slide_dict()

        return slides
    
    # def _create_transform_pipeline():


    @property
    def metadata(self) -> pandas.DataFrame:
        return self._df

    @property
    def slides_count(self) -> int:
        return self._df.shape[0]
    
    @property
    def tiles_count(self) -> int:
        n_tiles = 0
        for slide in self._current_slides:
            n_tiles += slide.tiles_count
        return n_tiles

    def binarize_dfs(self, years: int) -> pandas.Series:
        bm_ret = self._df["dfs"].copy()
        bm_ret[:] = pandas.NA
        bm_ret[(self._df["dfs"] > 365*years)] = 1
        bm_ret[(self._df["dfs"] <= 365*years) & (self._df["typefdfs"] != "death without another event reported")] = 0
        return bm_ret
    
    # def multilabel_dfs(self, thresh: List[float]):
    #     bm_ret = self._df["dfs"].copy()
    #     bm_ret[:] = pandas.NA
    #     for t in thresh:
    #         bm_ret[(self._df["dfs"] > t)] = 1
    #         bm_ret[(self._df["dfs"] <= t) & (self._df["typefdfs"] != "death without another event reported")] = 0

    def get_slide(self, slide_idx: int) -> Slide:
        return self._current_slides[slide_idx]
    
    def get_tile(self, tile_idx: int) -> Tuple[Slide, int]:
        row = self._tiles_df.iloc[[tile_idx]]
        slide_idx = row["slide_idx"].item()
        slide = self._current_slides[slide_idx]
        top_left_pixel = row[[TilesManager.pixel_x, TilesManager.pixel_y]].to_numpy()
        return Tile(slide.slide_context, top_left_pixel)

    def get_random_slide(self) -> Slide:
        index = np.random.randint(low=0, high=self._df.shape[0])
        return self.get_slide(index=index)

    def _load_metadata(self) -> pandas.DataFrame:
        return pandas.read_csv(filepath_or_buffer=self._metadata_file_path)
    
    def _create_file_name_to_slide_dict(self) -> Dict[str, Slide]:
        file_name_to_slide = {}
        for slide in self._slides:
            file_name_to_slide[slide.slide_context.image_file_name] = slide

        return file_name_to_slide

    def _create_tile_to_slide_dict(self) -> Dict[Tile, Slide]:
        tile_to_slide = {}
        for slide in self._slides:
            for tile in slide.tiles:
                tile_to_slide[tile] = slide

        return tile_to_slide

    def _get_slides(self) -> List[Slide]:
        return [
            self._file_name_to_slide[x] for x in self._df[constants.file_column_name]
        ]

    def binary_label_str_to_int(self) -> pandas.Series:
        pos_label = self._df[self.target].apply(lambda x: 1 if (x=="Positive" or x=='1' or x==1) else pandas.NA)
        neg_label = self._df[self.target].apply(lambda x: 0 if (x=="Negative" or x=='0' or x==0) else pandas.NA)
        return pos_label.combine_first(neg_label)

    def make_target_column(self):
        if (self.target=="binary_dfs"):
            return self.binarize_dfs(years=constants.dfs_binarization_threshold)
        elif (self.target=="multilabel_dfs"):
            return self.multilabel_dfs(thresh=constants.SURVIVAL_QUANTILES)
        elif (self.target=="er_or_pr"):
            return (1 - ((1 - self._df["er_status"]) * (1 - self._df["pr_status"])))
        elif (self.target=="survival"):
            return self._df.apply(lambda x: np.array([x["survtime"], x["survstat"], x["survtime"]]), axis=1)
        elif (self.target=="dfs"):
            return self._df.apply(lambda x: np.array([x["dfs"], x["dfsind"], x["dfs"]]), axis=1)
        elif (self.target=="drfi"):
            return self._df.apply(lambda x: np.array([x["drfi"], x["drfiind"], x["dfs"]]), axis=1)
        elif (self.target=="rfi"):
            return self._df.apply(lambda x: np.array([x["rfi"], x["rfiind"], x["dfs"]]), axis=1)
        elif (self.target=="none"):
            return pandas.Series([1]*len(self._df))
        else:
            return self.binary_label_str_to_int()
