import logging
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd


def get_RegModel_Features_location_dict(
    train_DataSet: str, target: str, test_fold: int
):
    test_fold = test_fold if test_fold > 0 else None
    All_Data_Dict = {
        "linux": {
            "CAT": {
                "Fold None": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_40015-ER-TestFold_-1",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50394-ER-TestFold_-1/Inference/CAT_12345/",
                        "TestSet Location": None,
                        "REG Model Location": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40015-ER-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_40019-Her2-TestFold_-1",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50395-Her2-TestFold_-1/Inference/CAT_12345/",
                        "TestSet Location": None,
                        "REG Model Location": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40019-Her2-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50396-PR-TestFold_-1/Inference/CAT_12345/",
                        "TestSet Location": None,
                        "REG Model Location": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40046-PR-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1",
                        "TrainSet Location": [
                            "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40015-ER-TestFold_-1/Inference/CAT_ER_features_for_OR/",
                            "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40046-PR-TestFold_-1/Inference/CAT_PR_features_for_OR/",
                        ],
                        "TestSet Location": [None, None],
                        "REG Model Location": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40046-PR-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                },
                "Fold 1": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_355-ER-TestFold_1 With Locations",
                        "TrainSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/train_w_features_w_locs",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/test_w_features_locs",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "hl0": {
                        "DataSet Name": r"FEATURES: Exp_355-ER-TestFold_1 With Locations",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50379-ER-TestFold_1/Inference/cat2345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50379-ER-TestFold_1/Inference/cat1/",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "hl5_40": {
                        "DataSet Name": r"FEATURES: Exp_355-ER-TestFold_1 With Locations",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50381-ER-TestFold_1/Inference/cat2345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50381-ER-TestFold_1/Inference/cat1/",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "hl50": {
                        "DataSet Name": r"FEATURES: Exp_355-ER-TestFold_1 With Locations",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50380-ER-TestFold_1/Inference/cat2345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50380-ER-TestFold_1/Inference/cat1/",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_355-ER-TestFold_-1+Exp_20010-PR-TestFold_-1",
                        "TrainSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/CAT_Fold2345_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/CAT_Fold2345_PR_features_for_OR/",
                        ],
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/CAT_Fold1_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/CAT_Fold1_PR_features_for_OR/",
                        ],
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "Her2_with_cancer": {
                        "DataSet Name": r"FEATURES: Exp_355-ER-TestFold_-1+Exp_20010-PR-TestFold_-1",
                        "TrainSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_392-Her2-TestFold_1/Inference/train_w_features/",
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_627-is_cancer-TestFold_1/Inference/CAT_Her2_train_fold2345_patches_inference_w_features/",
                        ],
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_392-Her2-TestFold_1/Inference/test_w_features/",
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_627-is_cancer-TestFold_1/Inference/CAT_Her2_fold1_patches_inference_w_features/",
                        ],
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_392-Her2-TestFold_1 With Locations",
                        "TrainSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_392-Her2-TestFold_1/Inference/train_w_features",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_392-Her2-TestFold_1/Inference/test_w_locs_w_features",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_392-Her2-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_10-PR-TestFold_1  With Locations",
                        "TrainSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/train_w_features_new",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/test_w_locs_w_features",
                        "REG Model Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                },
                "Fold 2": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_393-ER-TestFold_2 With Locations",
                        "TrainSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/train_w_features_new",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/test_w_features",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_412-Her2-TestFold_2 With Locations",
                        "TrainSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_412-Her2-TestFold_2/Inference/train_w_features",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_412-Her2-TestFold_2/Inference/test_w_features",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_412-Her2-TestFold_2/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "hl5_40": {
                        "DataSet Name": r"FEATURES: Exp_355-ER-TestFold_1 With Locations",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50398-ER-TestFold_2/Inference/CAT_1345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50398-ER-TestFold_2/Inference/CAT_2/",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "hl50": {
                        "DataSet Name": r"FEATURES: Exp_355-ER-TestFold_1 With Locations",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50397-ER-TestFold_2/Inference/CAT_1345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50397-ER-TestFold_2/Inference/CAT_2/",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_355-ER-TestFold_-1+Exp_20010-PR-TestFold_-1",
                        "TrainSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/CAT_Fold1345_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/CAT_Fold1345_PR_features_for_OR/",
                        ],
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/CAT_Fold2_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/CAT_Fold2_PR_features_for_OR/",
                        ],
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_20063-PR-TestFold_2 With Locations",
                        "TrainSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/train_w_features_new",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/test_w_features",
                        "REG Model Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                },
                "Fold 3": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_472-ER-TestFold_3",
                        "TrainSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_472-ER-TestFold_3/Inference/train_w_features",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_472-ER-TestFold_3/Inference/test_w_features",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_472-ER-TestFold_3/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_20114-Her2-TestFold_3",
                        "TrainSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20114-Her2-TestFold_3/Inference/train_w_features",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20114-Her2-TestFold_3/Inference/test_w_features",
                        "REG Model Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20114-Her2-TestFold_3/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_355-ER-TestFold_-1+Exp_20010-PR-TestFold_-1",
                        "TrainSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_472-ER-TestFold_3/Inference/CAT_Fold1245_ER_features_for_OR/",
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_497-PR-TestFold_3/Inference/CAT_Fold1245_PR_features_for_OR/",
                        ],
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_472-ER-TestFold_3/Inference/CAT_Fold3_ER_features_for_OR/",
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_497-PR-TestFold_3/Inference/CAT_Fold3_PR_features_for_OR/",
                        ],
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_497-PR-TestFold_3",
                        "TrainSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_497-PR-TestFold_3/Inference/train_w_features",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_497-PR-TestFold_3/Inference/test_w_features",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_497-PR-TestFold_3/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                },
                "Fold 4": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_542-ER-TestFold_4",
                        "TrainSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_542-ER-TestFold_4/Inference/train_w_features",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_542-ER-TestFold_4/Inference/test_w_features",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_542-ER-TestFold_4/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_20201-Her2-TestFold_4",
                        "TrainSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20201-Her2-TestFold_4/Inference/train_w_features",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20201-Her2-TestFold_4/Inference/test_w_features",
                        "REG Model Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20201-Her2-TestFold_4/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_355-ER-TestFold_-1+Exp_20010-PR-TestFold_-1",
                        "TrainSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_542-ER-TestFold_4/Inference/CAT_Fold1235_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20207-PR-TestFold_4/Inference/CAT_Fold1235_PR_features_for_OR/",
                        ],
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_542-ER-TestFold_4/Inference/CAT_Fold4_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20207-PR-TestFold_4/Inference/CAT_Fold4_PR_features_for_OR/",
                        ],
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_20207-PR-TestFold_4",
                        "TrainSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20207-PR-TestFold_4/Inference/train_w_features",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20207-PR-TestFold_4/Inference/test_w_features",
                        "REG Model Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20207-PR-TestFold_4/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                },
                "Fold 5": {
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_20228-Her2-TestFold_5",
                        "TrainSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20228-Her2-TestFold_5/Inference/train_w_features",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20228-Her2-TestFold_5/Inference/test_w_features",
                        "REG Model Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20228-Her2-TestFold_5/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_611-ER-TestFold_5",
                        "TrainSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_611-ER-TestFold_5/Inference/train_w_features",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_611-ER-TestFold_5/Inference/test_w_features",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_611-ER-TestFold_5/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_355-ER-TestFold_-1+Exp_20010-PR-TestFold_-1",
                        "TrainSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_611-ER-TestFold_5/Inference/CAT_Fold1234_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20235-PR-TestFold_5/Inference/CAT_Fold1234_PR_features_for_OR/",
                        ],
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_611-ER-TestFold_5/Inference/CAT_Fold5_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20235-PR-TestFold_5/Inference/CAT_Fold5_PR_features_for_OR/",
                        ],
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_20235-PR-TestFold_5",
                        "TrainSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20235-PR-TestFold_5/Inference/train_w_features",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20235-PR-TestFold_5/Inference/test_w_features",
                        "REG Model Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20235-PR-TestFold_5/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                },
            },
            "ABCTB": {
                "Fold 1": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_50214-ER100-TestFold_-1",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50408-ER-TestFold_1/Inference/ABCTB_2345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50408-ER-TestFold_1/Inference/ABCTB_1/",
                        "REG Model Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50214-ER100-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                },
            },
            "CARMEL_ABCTB": {
                "Fold 1": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_50214-ER100-TestFold_-1",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50410-ER-TestFold_1/Inference/CARMEL_ABCTB_2345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50410-ER-TestFold_1/Inference/CARMEL_ABCTB_1/",
                        "REG Model Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50214-ER100-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                },
            },
            "Carmel_IHC": {
                "Fold 1": {
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_50214-ER100-TestFold_-1",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50311-Her2-TestFold_1/Inference/carmel_ihc_2345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50311-Her2-TestFold_1/Inference/carmel_ihc_1/",
                        "REG Model Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50214-ER100-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                },
            },
            "CARMEL100": {
                "Fold 1": {
                    "IsHighRisk26": {
                        "DataSet Name": r"FEATURES: Exp_50214-ER100-TestFold_-1",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50338-IsHighRisk26-TestFold_1/Inference/folds_2345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50338-IsHighRisk26-TestFold_1/Inference/folds_1/",
                        "REG Model Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50214-ER100-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                    "IsHighRisk31": {
                        "DataSet Name": r"FEATURES: Exp_50214-ER100-TestFold_-1",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50339-IsHighRisk31-TestFold_1/Inference/folds_2345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50339-IsHighRisk31-TestFold_1/Inference/folds_1/",
                        "REG Model Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50214-ER100-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                },
                "Fold 2": {
                    "IsHighRisk26": {
                        "DataSet Name": r"FEATURES: Exp_50214-ER100-TestFold_-1",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50340-IsHighRisk26-TestFold_2/Inference/folds_1345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50340-IsHighRisk26-TestFold_2/Inference/folds_2/",
                        "REG Model Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50214-ER100-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                    "IsHighRisk31": {
                        "DataSet Name": r"FEATURES: Exp_50214-ER100-TestFold_-1",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50342-IsHighRisk31-TestFold_2/Inference/folds_1345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50342-IsHighRisk31-TestFold_2/Inference/folds_2/",
                        "REG Model Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50214-ER100-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                },
                "Fold 3": {
                    "IsHighRisk26": {
                        "DataSet Name": r"FEATURES: Exp_50214-ER100-TestFold_-1",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50341-IsHighRisk26-TestFold_3/Inference/folds_1245/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50341-IsHighRisk26-TestFold_3/Inference/folds_3/",
                        "REG Model Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50214-ER100-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                    "IsHighRisk31": {
                        "DataSet Name": r"FEATURES: Exp_50214-ER100-TestFold_-1",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50344-IsHighRisk31-TestFold_3/Inference/folds_1245/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50344-IsHighRisk31-TestFold_3/Inference/folds_3/",
                        "REG Model Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50214-ER100-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                },
                "Fold 4": {
                    "IsHighRisk26": {
                        "DataSet Name": r"FEATURES: Exp_50214-ER100-TestFold_-1",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50343-IsHighRisk26-TestFold_4/Inference/folds_1235/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50343-IsHighRisk26-TestFold_4/Inference/folds_4/",
                        "REG Model Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50214-ER100-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                    "IsHighRisk31": {
                        "DataSet Name": r"FEATURES: Exp_50214-ER100-TestFold_-1",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50349-IsHighRisk31-TestFold_4/Inference/folds_1235/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50349-IsHighRisk31-TestFold_4/Inference/folds_4/",
                        "REG Model Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50214-ER100-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                },
                "Fold 5": {
                    "IsHighRisk26": {
                        "DataSet Name": r"FEATURES: Exp_50214-ER100-TestFold_-1",
                        "TrainSet Location": r"//home/shacharcohen/workspace/WSI/legacy/runs/Exp_50348-IsHighRisk26-TestFold_5/Inference/folds_1234/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50348-IsHighRisk26-TestFold_5/Inference/folds_5/",
                        "REG Model Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50214-ER100-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                    "IsHighRisk31": {
                        "DataSet Name": r"FEATURES: Exp_50214-ER100-TestFold_-1",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50350-IsHighRisk31-TestFold_5/Inference/folds_1234/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50350-IsHighRisk31-TestFold_5/Inference/folds_5/",
                        "REG Model Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50214-ER100-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                }
            },
            "CARMEL": {
                "Fold None": {
                    "ER100": {
                        "DataSet Name": r"FEATURES: Exp_50214-ER100-TestFold_-1",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50214-ER100-TestFold_-1/Inference/CARMEL_fold12345_ER100_features/",
                        "TestSet Location": None,
                        "REG Model Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50214-ER100-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                    "ER_with_cancer": {
                        "DataSet Name": r"FEATURES: Exp_40022-ER-TestFold_-1",
                        "TrainSet Location": [
                            "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40022-ER-TestFold_-1/Inference/carmel_features_synced/",
                            "/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50323-is_cancer-TestFold_-1/Inference/carmel_er_ep_595/",
                        ],
                        "TestSet Location": [None, None],
                        "REG Model Location": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40022-ER-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                    "PR_with_cancer": {
                        "DataSet Name": r"FEATURES: Exp_40022-ER-TestFold_-1",
                        "TrainSet Location": [
                            "/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50263-PR-TestFold_-1/Inference/carmel_pr/",
                            "/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50323-is_cancer-TestFold_-1/Inference/carmel_pr_ep_595/",
                        ],
                        "TestSet Location": [None, None],
                        "REG Model Location": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40022-ER-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                    "Her2_with_cancer": {
                        "DataSet Name": r"FEATURES: Exp_40022-ER-TestFold_-1",
                        "TrainSet Location": [
                            "/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50289-Her2-TestFold_-1/Inference/carmel/",
                            "/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50323-is_cancer-TestFold_-1/Inference/carmel_her2_ep_595/",
                        ],
                        "TestSet Location": [None, None],
                        "REG Model Location": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40022-ER-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_40022-ER-TestFold_-1",
                        "TrainSet Location": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40022-ER-TestFold_-1/Inference/train_w_features",
                        "TestSet Location": None,
                        "REG Model Location": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40022-ER-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_40023-Ki67-TestFold_-1",
                        "TrainSet Location": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40023-Ki67-TestFold_-1/Inference/train_w_features",
                        "TestSet Location": None,
                        "REG Model Location": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40023-Ki67-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt",
                    },
                    "Her2": {
                        "DataSet Name": None,
                        "TrainSet Location": None,
                        "TestSet Location": None,
                        "REG Model Location": None,
                    },
                    "PR": {
                        "DataSet Name": None,
                        "TrainSet Location": None,
                        "TestSet Location": None,
                        "REG Model Location": None,
                    },
                },
                "Fold 1": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_358-ER-TestFold_1",
                        "TrainSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_358-ER-TestFold_1/Inference/train_w_features",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_358-ER-TestFold_1/Inference/test_w_features",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_358-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_419-Ki67-TestFold_1",
                        "TrainSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_419-Ki67-TestFold_1/Inference/train_w_features",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_419-Ki67-TestFold_1/Inference/test_w_features",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_419-Ki67-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "Her2": {
                        "DataSet Name": None,
                        "TrainSet Location": None,
                        "TestSet Location": None,
                        "REG Model Location": None,
                    },
                    "PR": {
                        "DataSet Name": None,
                        "TrainSet Location": None,
                        "TestSet Location": None,
                        "REG Model Location": None,
                    },
                },
                "Fold 2": {
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_490-Ki67-TestFold_2",
                        "TrainSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_490-Ki67-TestFold_2/Inference/train_w_features",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_490-Ki67-TestFold_2/Inference/test_w_features",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_490-Ki67-TestFold_2/Model_CheckPoints/model_data_Epoch_1000.pt",
                    }
                },
                "Fold 3": {
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_20152-Ki67-TestFold_3",
                        "TrainSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20152-Ki67-TestFold_3/Inference/train_w_features",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20152-Ki67-TestFold_3/Inference/test_w_features",
                        "REG Model Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20152-Ki67-TestFold_3/Model_CheckPoints/model_data_Epoch_1000.pt",
                    }
                },
                "Fold 4": {
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_30090-Ki67-TestFold_4",
                        "TrainSet Location": r"/home/talneoran/workspace/wsi/legacy/runs/Exp_30090-Ki67-TestFold_4/Inference/train_w_features",
                        "TestSet Location": r"/home/talneoran/workspace/wsi/legacy/runs/Exp_30090-Ki67-TestFold_4/Inference/test_w_features",
                        "REG Model Location": r"/home/talneoran/workspace/wsi/legacy/runs/Exp_30090-Ki67-TestFold_4/Model_CheckPoints/model_data_Epoch_1000.pt",
                    }
                },
                "Fold 5": {
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_30092-Ki67-TestFold_5",
                        "TrainSet Location": r"/home/talneoran/workspace/wsi/legacy/runs/Exp_30092-Ki67-TestFold_5/Inference/train_w_features",
                        "TestSet Location": r"/home/talneoran/workspace/wsi/legacy/runs/Exp_30092-Ki67-TestFold_5/Inference/test_w_features",
                        "REG Model Location": r"/home/talneoran/workspace/wsi/legacy/runs/Exp_30092-Ki67-TestFold_5/Model_CheckPoints/model_data_Epoch_1000.pt",
                    }
                },
            },
            "CARMEL 9-11": {
                "Fold None": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Model From Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40015-ER-TestFold_-1/Inference/CARMEL9",
                            "Carmel 10": "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40015-ER-TestFold_-1/Inference/CARMEL10",
                            "Carmel 11": "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40015-ER-TestFold_-1/Inference/CARMEL11",
                        },
                    },
                    "ER_with_cancer": {
                        "DataSet Name": r"FEATURES: Exp_40022-ER-TestFold_-1",
                        "TestSet Location": {
                            "Carmel 9": [
                            "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40022-ER-TestFold_-1/Inference/carmel9_features_synced/",
                            "/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50323-is_cancer-TestFold_-1/Inference/carmel_9_ep_595/",
                            ],
                            "Carmel 11": [
                            "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40022-ER-TestFold_-1/Inference/carmel11_features_synced/",
                            "/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50323-is_cancer-TestFold_-1/Inference/carmel_11_ep_595/",
                            ]
                        },
                    },
                    "PR_with_cancer": {
                        "DataSet Name": r"FEATURES: Exp_40022-ER-TestFold_-1",
                        "TestSet Location": {
                            "Carmel 9": [
                            "/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50263-PR-TestFold_-1/Inference/carmel9/",
                            "/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50323-is_cancer-TestFold_-1/Inference/carmel_9_ep_595/",
                            ],
                            "Carmel 11": [
                            "/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50263-PR-TestFold_-1/Inference/carmel11/",
                            "/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50323-is_cancer-TestFold_-1/Inference/carmel_11_ep_595/",
                            ]
                        },
                    },
                    "Her2_with_cancer": {
                        "DataSet Name": r"FEATURES: Exp_40022-ER-TestFold_-1",
                        "TestSet Location": {
                            "Carmel 9": [
                            "/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50289-Her2-TestFold_-1/Inference/carmel9/",
                            "/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50323-is_cancer-TestFold_-1/Inference/carmel_9_ep_595/",
                            ],
                            "Carmel 11": [
                            "/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50289-Her2-TestFold_-1/Inference/carmel11/",
                            "/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50323-is_cancer-TestFold_-1/Inference/carmel_11_ep_595/",
                            ]
                        },
                    },
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": [
                                "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40015-ER-TestFold_-1/Inference/CARMEL9_ER_features_for_OR/",
                                "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40046-PR-TestFold_-1/Inference/CARMEL9_PR_features_for_OR/",
                            ],
                            "Carmel 10": [
                                "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40015-ER-TestFold_-1/Inference/CARMEL10_ER_features_for_OR/",
                                "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40046-PR-TestFold_-1/Inference/CARMEL10_PR_features_for_OR/",
                            ],
                            "Carmel 11": [
                                "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40015-ER-TestFold_-1/Inference/CARMEL11_ER_features_for_OR/",
                                "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40046-PR-TestFold_-1/Inference/CARMEL11_PR_features_for_OR/",
                            ],
                        },
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Model From Exp_40046-PR-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40046-PR-TestFold_-1/Inference/CARMEL9",
                            "Carmel 10": "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40046-PR-TestFold_-1/Inference/CARMEL10",
                            "Carmel 11": "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40046-PR-TestFold_-1/Inference/CARMEL11",
                        },
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Model From Exp_40019-Her2-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40019-Her2-TestFold_-1/Inference/CARMEL9",
                            "Carmel 10": "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40019-Her2-TestFold_-1/Inference/CARMEL10",
                            "Carmel 11": "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40019-Her2-TestFold_-1/Inference/CARMEL11",
                        },
                    },
                },
                "Fold 1": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Model From Exp_355-ER-TestFold_1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/CARMEL9",
                            "Carmel 10": "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/CARMEL10",
                            "Carmel 11": "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/CARMEL11",
                        },
                    },
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Model From Exp_10-PR-TestFold_1+Model From Exp_355-ER-TestFold_1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": [
                                "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/CARMEL9_ER_features_for_OR/",
                                "/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/CARMEL9_PR_features_for_OR/",
                            ],
                            "Carmel 10": [
                                "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/CARMEL10_ER_features_for_OR/",
                                "/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/CARMEL10_PR_features_for_OR/",
                            ],
                            "Carmel 11": [
                                "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/CARMEL11_ER_features_for_OR/",
                                "/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/CARMEL11_PR_features_for_OR/",
                            ],
                        },
                    },
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_419-Ki67-TestFold_1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_419-Ki67-TestFold_1/Inference/CARMEL9/",
                            "Carmel 10": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_419-Ki67-TestFold_1/Inference/CARMEL10/",
                            "Carmel 11": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_419-Ki67-TestFold_1/Inference/CARMEL11/",
                        },
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_392-Her2-TestFold_1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_392-Her2-TestFold_1/Inference/CARMEL9",
                            "Carmel 10": "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_392-Her2-TestFold_1/Inference/CARMEL10",
                            "Carmel 11": "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_392-Her2-TestFold_1/Inference/CARMEL11",
                        },
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Model From Exp_10-PR-TestFold_1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": "/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/CARMEL9",
                            "Carmel 10": "/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/CARMEL10",
                            "Carmel 11": "/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/CARMEL11",
                        },
                    },
                },
                "Fold 2": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Model From Exp_393-ER-TestFold_2, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/CARMEL9",
                            "Carmel 10": "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/CARMEL10",
                            "Carmel 11": "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/CARMEL11",
                        },
                    },
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_490-Ki67-TestFold_2, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_490-Ki67-TestFold_2/Inference/CARMEL9/",
                            "Carmel 10": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_490-Ki67-TestFold_2/Inference/CARMEL10/",
                            "Carmel 11": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_490-Ki67-TestFold_2/Inference/CARMEL11/",
                        },
                    },
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Model From Exp_10-PR-TestFold_1+Model From Exp_355-ER-TestFold_1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": [
                                "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/CARMEL9_ER_features_for_OR/",
                                "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/CARMEL9_PR_features_for_OR/",
                            ],
                            "Carmel 10": [
                                "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/CARMEL10_ER_features_for_OR/",
                                "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/CARMEL10_PR_features_for_OR/",
                            ],
                            "Carmel 11": [
                                "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/CARMEL11_ER_features_for_OR/",
                                "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/CARMEL11_PR_features_for_OR/",
                            ],
                        },
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_412-Her2-TestFold_2, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_412-Her2-TestFold_2/Inference/CARMEL9",
                            "Carmel 10": "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_412-Her2-TestFold_2/Inference/CARMEL10",
                            "Carmel 11": "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_412-Her2-TestFold_2/Inference/CARMEL11",
                        },
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Model From Exp_20063-PR-TestFold_2, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/CARMEL9",
                            "Carmel 10": "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/CARMEL10",
                            "Carmel 11": "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/CARMEL11",
                        },
                    },
                },
                "Fold 3": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Model From Exp_472-ER-TestFold_3, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_472-ER-TestFold_3/Inference/CARMEL9",
                            "Carmel 10": "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_472-ER-TestFold_3/Inference/CARMEL10",
                            "Carmel 11": "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_472-ER-TestFold_3/Inference/CARMEL11",
                        },
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_20114-Her2-TestFold_3, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20114-Her2-TestFold_3/Inference/CARMEL9",
                            "Carmel 10": "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20114-Her2-TestFold_3/Inference/CARMEL10",
                            "Carmel 11": "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20114-Her2-TestFold_3/Inference/CARMEL11",
                        },
                    },
                     "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Model From Exp_10-PR-TestFold_1+Model From Exp_355-ER-TestFold_1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": [
                                "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_472-ER-TestFold_3/Inference/CARMEL9_ER_features_for_OR/",
                                "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_497-PR-TestFold_3/Inference/CARMEL9_PR_features_for_OR/",
                            ],
                            "Carmel 10": [
                                "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_472-ER-TestFold_3/Inference/CARMEL10_ER_features_for_OR/",
                                "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_497-PR-TestFold_3/Inference/CARMEL10_PR_features_for_OR/",
                            ],
                            "Carmel 11": [
                                "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_472-ER-TestFold_3/Inference/CARMEL11_ER_features_for_OR/",
                                "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_497-PR-TestFold_3/Inference/CARMEL11_PR_features_for_OR/",
                            ],
                        },
                    },
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_20152-Ki67-TestFold_3, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20152-Ki67-TestFold_3/Inference/CARMEL9/",
                            "Carmel 10": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20152-Ki67-TestFold_3/Inference/CARMEL10/",
                            "Carmel 11": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20152-Ki67-TestFold_3/Inference/CARMEL11/",
                        },
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Model From Exp_497-PR-TestFold_3, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_497-PR-TestFold_3/Inference/CARMEL9",
                            "Carmel 10": "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_497-PR-TestFold_3/Inference/CARMEL10",
                            "Carmel 11": "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_497-PR-TestFold_3/Inference/CARMEL11",
                        },
                    },
                },
                "Fold 4": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Model From Exp_542-ER-TestFold_4, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_542-ER-TestFold_4/Inference/CARMEL9",
                            "Carmel 10": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_542-ER-TestFold_4/Inference/CARMEL10",
                            "Carmel 11": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_542-ER-TestFold_4/Inference/CARMEL11",
                        },
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Model From Exp_20201-Her2-TestFold_4, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20201-Her2-TestFold_4/Inference/CARMEL9",
                            "Carmel 10": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20201-Her2-TestFold_4/Inference/CARMEL10",
                            "Carmel 11": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20201-Her2-TestFold_4/Inference/CARMEL11",
                        },
                    },
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Model From Exp_10-PR-TestFold_1+Model From Exp_355-ER-TestFold_1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": [
                                "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_542-ER-TestFold_4/Inference/CARMEL9_ER_features_for_OR/",
                                "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20207-PR-TestFold_4/Inference/CARMEL9_PR_features_for_OR/",
                            ],
                            "Carmel 10": [
                                "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_542-ER-TestFold_4/Inference/CARMEL10_ER_features_for_OR/",
                                "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20207-PR-TestFold_4/Inference/CARMEL10_PR_features_for_OR/",
                            ],
                            "Carmel 11": [
                                "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_542-ER-TestFold_4/Inference/CARMEL11_ER_features_for_OR/",
                                "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20207-PR-TestFold_4/Inference/CARMEL11_PR_features_for_OR/",
                            ],
                        },
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Model From Exp_20207-PR-TestFold_4, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20207-PR-TestFold_4/Inference/CARMEL9",
                            "Carmel 10": "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20207-PR-TestFold_4/Inference/CARMEL10",
                            "Carmel 11": "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20207-PR-TestFold_4/Inference/CARMEL11",
                        },
                    },
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_30090-Ki67-TestFold_4, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": r"/home/talneoran/workspace/wsi/legacy/runs/Exp_30090-Ki67-TestFold_4/Inference/CARMEL9",
                            "Carmel 10": r"/home/talneoran/workspace/wsi/legacy/runs/Exp_30090-Ki67-TestFold_4/Inference/CARMEL10",
                            "Carmel 11": r"/home/talneoran/workspace/wsi/legacy/runs/Exp_30090-Ki67-TestFold_4/Inference/CARMEL11",
                        },
                    },
                },
                "Fold 5": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Model From Exp_611-ER-TestFold_5, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_611-ER-TestFold_5/Inference/CARMEL9",
                            "Carmel 10": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_611-ER-TestFold_5/Inference/CARMEL10",
                            "Carmel 11": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_611-ER-TestFold_5/Inference/CARMEL11",
                        },
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Model From Exp_20228-Her2-TestFold_5, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20228-Her2-TestFold_5/Inference/CARMEL9",
                            "Carmel 10": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20228-Her2-TestFold_5/Inference/CARMEL10",
                            "Carmel 11": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20228-Her2-TestFold_5/Inference/CARMEL11",
                        },
                    },
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Model From Exp_10-PR-TestFold_1+Model From Exp_355-ER-TestFold_1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": [
                                "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_611-ER-TestFold_5/Inference/CARMEL9_ER_features_for_OR/",
                                "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20235-PR-TestFold_5/Inference/CARMEL9_PR_features_for_OR/",
                            ],
                            "Carmel 10": [
                                "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_611-ER-TestFold_5/Inference/CARMEL10_ER_features_for_OR/",
                                "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20235-PR-TestFold_5/Inference/CARMEL10_PR_features_for_OR/",
                            ],
                            "Carmel 11": [
                                "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_611-ER-TestFold_5/Inference/CARMEL11_ER_features_for_OR/",
                                "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20235-PR-TestFold_5/Inference/CARMEL11_PR_features_for_OR/",
                            ],
                        },
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Model From Exp_20235-PR-TestFold_5, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20235-PR-TestFold_5/Inference/CARMEL9",
                            "Carmel 10": "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20235-PR-TestFold_5/Inference/CARMEL10",
                            "Carmel 11": "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20235-PR-TestFold_5/Inference/CARMEL11",
                        },
                    },
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_30092-Ki67-TestFold_5, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": {
                            "Carmel 9": r"/home/talneoran/workspace/wsi/legacy/runs/Exp_30092-Ki67-TestFold_5/Inference/CARMEL9",
                            "Carmel 10": r"/home/talneoran/workspace/wsi/legacy/runs/Exp_30092-Ki67-TestFold_5/Inference/CARMEL10",
                            "Carmel 11": r"/home/talneoran/workspace/wsi/legacy/runs/Exp_30092-Ki67-TestFold_5/Inference/CARMEL11",
                        },
                    },
                },
            },
            "TCGA": {
                "Fold 1": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_393-ER-TestFold_2 With Locations",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50404-ER-TestFold_1/Inference/TCGA_2345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50404-ER-TestFold_1/Inference/TCGA_1/",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_412-Her2-TestFold_2 With Locations",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50405-Her2-TestFold_1/Inference/TCGA_2345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50405-Her2-TestFold_1/Inference/TCGA_1/",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_412-Her2-TestFold_2/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "esr20": {
                        "DataSet Name": r"FEATURES: Exp_40015-ER-TestFold_-1, Carmel Rescan Slides",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50390-ER-TestFold_1/Inference/TCGA_2345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50390-ER-TestFold_1/Inference/TCGA_1/",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "esr50": {
                        "DataSet Name": r"FEATURES: Exp_40015-ER-TestFold_-1, Carmel Rescan Slides",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50389-ER-TestFold_1/Inference/TCGA_2345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50389-ER-TestFold_1/Inference/TCGA_1/",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "erbb15": {
                        "DataSet Name": r"FEATURES: Exp_40015-ER-TestFold_-1, Carmel Rescan Slides",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50391-ER-TestFold_1/Inference/TCGA_2345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50391-ER-TestFold_1/Inference/TCGA_1/",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "erbb50": {
                        "DataSet Name": r"FEATURES: Exp_40015-ER-TestFold_-1, Carmel Rescan Slides",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50392-ER-TestFold_1/Inference/TCGA_2345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50392-ER-TestFold_1/Inference/TCGA_1/",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "erbb85": {
                        "DataSet Name": r"FEATURES: Exp_40015-ER-TestFold_-1, Carmel Rescan Slides",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50393-ER-TestFold_1/Inference/TCGA_2345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50393-ER-TestFold_1/Inference/TCGA_1/",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                },
                "Fold 2": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_393-ER-TestFold_2 With Locations",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50407-ER-TestFold_2/Inference/TCGA_1345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50407-ER-TestFold_2/Inference/TCGA_2/",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_412-Her2-TestFold_2 With Locations",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50406-Her2-TestFold_2/Inference/TCGA_1345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50406-Her2-TestFold_2/Inference/TCGA_2/",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_412-Her2-TestFold_2/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "esr20": {
                        "DataSet Name": r"FEATURES: Exp_40015-ER-TestFold_-1, Carmel Rescan Slides",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50399-ER-TestFold_2/Inference/TCGA_1345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50399-ER-TestFold_2/Inference/TCGA_2/",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "esr50": {
                        "DataSet Name": r"FEATURES: Exp_40015-ER-TestFold_-1, Carmel Rescan Slides",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50400-ER-TestFold_2/Inference/TCGA_1345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50400-ER-TestFold_2/Inference/TCGA_2/",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "erbb15": {
                        "DataSet Name": r"FEATURES: Exp_40015-ER-TestFold_-1, Carmel Rescan Slides",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50403-ER-TestFold_2/Inference/TCGA_1345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50403-ER-TestFold_2/Inference/TCGA_2/",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "erbb50": {
                        "DataSet Name": r"FEATURES: Exp_40015-ER-TestFold_-1, Carmel Rescan Slides",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50402-ER-TestFold_2/Inference/TCGA_1345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50402-ER-TestFold_2/Inference/TCGA_2/",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                    "erbb85": {
                        "DataSet Name": r"FEATURES: Exp_40015-ER-TestFold_-1, Carmel Rescan Slides",
                        "TrainSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50401-ER-TestFold_2/Inference/TCGA_1345/",
                        "TestSet Location": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50401-ER-TestFold_2/Inference/TCGA_2/",
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    },
                },
            },
            "Carmel_Rescan": {
                "Fold None": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_40015-ER-TestFold_-1, Carmel Rescan Slides",
                        "TestSet Location": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40015-ER-TestFold_-1/Inference/rescan",
                    },
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_355-ER-TestFold_-1+Exp_20010-PR-TestFold_-1",
                        "TestSet Location": [
                            "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40015-ER-TestFold_-1/Inference/rescan_filtered_colormapped_for_or/",
                            "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40046-PR-TestFold_-1/Inference/rescan_filtered_colormapped_for_or/",
                        ],
                        "REG Model Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    }
                },
            },
            "HAEMEK": {
                "Fold None": {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40015-ER-TestFold_-1/Inference/HAEMEK_ER_features_for_OR/",
                            "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40046-PR-TestFold_-1/Inference/HAEMEK_PR_features_for_OR/",
                        ]
                    },
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_40015-ER-TestFold_-1, HAEMEK ONLY Slides",
                        "TestSet Location": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40015-ER-TestFold_-1/Inference/HAEMEK",
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1, HAEMEK ONLY Slides",
                        "TestSet Location": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40046-PR-TestFold_-1/Inference/HAEMEK",
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_40019-Her2-TestFold_-1, HAEMEK ONLY Slides",
                        "TestSet Location": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40019-Her2-TestFold_-1/Inference/HAEMEK",
                    },
                },
                "Fold 1": {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/HAEMEK_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/HAEMEK_PR_features_for_OR/",
                        ]
                    },
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_355-ER-TestFold_1, HAEMEK ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/HAEMEK",
                    },
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_419-Ki67-TestFold_1, HAEMEK ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_419-Ki67-TestFold_1/Inference/HAEMEK",
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_392-Her2-TestFold_1, HAEMEK ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_392-Her2-TestFold_1/Inference/HAEMEK",
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_20010-PR-TestFold_1, HAEMEK ONLY Slides",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/HAEMEK",
                    },
                },
                "Fold 2": {
                     "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/HAEMEK_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/HAEMEK_PR_features_for_OR/",
                        ]
                    },
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_393-ER-TestFold_2, HAEMEK ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/HAEMEK",
                    },
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_490-Ki67-TestFold_2, HAEMEK ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_490-Ki67-TestFold_2/Inference/HAEMEK",
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_412-Her2-TestFold_2, HAEMEK ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_412-Her2-TestFold_2/Inference/HAEMEK",
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_20063-PR-TestFold_2, HAEMEK ONLY Slides",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/HAEMEK",
                    },
                },
                "Fold 3": {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_472-ER-TestFold_3/Inference/HAEMEK_ER_features_for_OR/",
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_497-PR-TestFold_3/Inference/HAEMEK_PR_features_for_OR/",
                        ]
                    },
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_472-ER-TestFold_3, HAEMEK ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_472-ER-TestFold_3/Inference/HAEMEK",
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_20114-Her2-TestFold_3, HAEMEK ONLY Slides",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20114-Her2-TestFold_3/Inference/HAEMEK",
                    },
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_20152-Ki67-TestFold_3, HAEMEK ONLY Slides",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20152-Ki67-TestFold_3/Inference/HAEMEK",
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_497-PR-TestFold_3, HAEMEK ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_497-PR-TestFold_3/Inference/HAEMEK",
                    },
                },
                "Fold 4": {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_542-ER-TestFold_4/Inference/HAEMEK_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20207-PR-TestFold_4/Inference/HAEMEK_PR_features_for_OR/",
                        ]
                    },
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_542-ER-TestFold_4, HAEMEK ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_542-ER-TestFold_4/Inference/HAEMEK",
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_20201-Her2-TestFold_4, HAEMEK ONLY Slides",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20201-Her2-TestFold_4/Inference/HAEMEK",
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_20207-PR-TestFold_4, HAEMEK ONLY Slides",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20207-PR-TestFold_4/Inference/HAEMEK",
                    },
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_30090-Ki67-TestFold_4, HAEMEK ONLY Slides",
                        "TestSet Location": r"/home/talneoran/workspace/wsi/legacy/runs/Exp_30090-Ki67-TestFold_4/Inference/HAEMEK",
                    },
                },
                "Fold 5": {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_611-ER-TestFold_5/Inference/HAEMEK_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20235-PR-TestFold_5/Inference/HAEMEK_PR_features_for_OR/",
                        ]
                    },
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_611-ER-TestFold_5, HAEMEK ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_611-ER-TestFold_5/Inference/HAEMEK",
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_20228-Her2-TestFold_5, HAEMEK ONLY Slides",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20228-Her2-TestFold_5/Inference/HAEMEK",
                    },
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_30092-Ki67-TestFold_5, HAEMEK ONLY Slides",
                        "TestSet Location": r"/home/talneoran/workspace/wsi/legacy/runs/Exp_30092-Ki67-TestFold_5/Inference/HAEMEK",
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_20235-PR-TestFold_5, HAEMEK ONLY Slides",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20235-PR-TestFold_5/Inference/HAEMEK",
                    },
                },
            },
            "TCGA_ABCTB->CARMEL": {
                "Fold None": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_40021-ER-TestFold_-1",
                        "TestSet Location": {
                            "CARMEL": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40021-ER-TestFold_-1/Inference/CARMEL1-8",
                            "CARMEL9": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40021-ER-TestFold_-1/Inference/CARMEL9",
                            "CARMEL10": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40021-ER-TestFold_-1/Inference/CARMEL10",
                            "CARMEL11": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40021-ER-TestFold_-1/Inference/CARMEL11",
                        },
                    }
                },
                "Fold 1": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_293-ER-TestFold_1",
                        "TestSet Location": {
                            "CARMEL": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_293-ER-TestFold_1/Inference/CARMEL1-8",
                            "CARMEL 9-11": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_293-ER-TestFold_1/Inference/CARMEL9-11",
                        },
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_308-Her2-TestFold_1",
                        "TestSet Location": {
                            "CARMEL": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_308-Her2-TestFold_1/Inference/CARMEL1-8",
                            "CARMEL 9-11": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_308-Her2-TestFold_1/Inference/CARMEL9-11",
                        },
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_309-PR-TestFold_1",
                        "TestSet Location": {
                            "CARMEL": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_309-PR-TestFold_1/Inference/CARMEL1-8",
                            "CARMEL 9-11": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_309-PR-TestFold_1/Inference/CARMEL9-11",
                        },
                    },
                },
                "Fold 2": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_299-ER-TestFold_2",
                        "TestSet Location": {
                            "CARMEL": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_299-ER-TestFold_2/Inference/CARMEL1-8",
                            "CARMEL 9-11": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_299-ER-TestFold_2/Inference/CARMEL9-11",
                        },
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_310-Her2-TestFold_2",
                        "TestSet Location": {
                            "CARMEL": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_310-Her2-TestFold_2/Inference/CARMEL1-8",
                            "CARMEL 9-11": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_310-Her2-TestFold_2/Inference/CARMEL9-11",
                        },
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_320-PR-TestFold_2",
                        "TestSet Location": {
                            "CARMEL": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_320-PR-TestFold_2/Inference/CARMEL1-8",
                            "CARMEL 9-11": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_320-PR-TestFold_2/Inference/CARMEL9-11",
                        },
                    },
                },
                "Fold 3": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_301-ER-TestFold_3",
                        "TestSet Location": {
                            "CARMEL": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_301-ER-TestFold_3/Inference/CARMEL1-8",
                            "CARMEL 9-11": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_301-ER-TestFold_3/Inference/CARMEL9-11",
                        },
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_311-Her2-TestFold_3",
                        "TestSet Location": {
                            "CARMEL": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_311-Her2-TestFold_3/Inference/CARMEL1-8",
                            "CARMEL 9-11": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_311-Her2-TestFold_3/Inference/CARMEL9-11",
                        },
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_312-PR-TestFold_3",
                        "TestSet Location": {
                            "CARMEL": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_312-PR-TestFold_3/Inference/CARMEL1-8",
                            "CARMEL 9-11": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_312-PR-TestFold_3/Inference/CARMEL9-11",
                        },
                    },
                },
                "Fold 4": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_302-ER-TestFold_4",
                        "TestSet Location": {
                            "CARMEL": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_302-ER-TestFold_4/Inference/CARMEL1-8",
                            "CARMEL 9-11": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_302-ER-TestFold_4/Inference/CARMEL9-11",
                        },
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_334-Her2-TestFold_4",
                        "TestSet Location": {
                            "CARMEL": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_334-Her2-TestFold_4/Inference/CARMEL1-8",
                            "CARMEL 9-11": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_334-Her2-TestFold_4/Inference/CARMEL9-11",
                        },
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_313-PR-TestFold_4",
                        "TestSet Location": {
                            "CARMEL": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_313-PR-TestFold_4/Inference/CARMEL1-8",
                            "CARMEL 9-11": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_313-PR-TestFold_4/Inference/CARMEL9-11",
                        },
                    },
                },
                "Fold 5": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_303-ER-TestFold_5",
                        "TestSet Location": {
                            "CARMEL": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_303-ER-TestFold_5/Inference/CARMEL1-8",
                            "CARMEL 9-11": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_303-ER-TestFold_5/Inference/CARMEL9-11",
                        },
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_348-Her2-TestFold_5",
                        "TestSet Location": {
                            "CARMEL": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_348-Her2-TestFold_5/Inference/CARMEL1-8",
                            "CARMEL 9-11": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_348-Her2-TestFold_5/Inference/CARMEL9-11",
                        },
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_321-PR-TestFold_5",
                        "TestSet Location": {
                            "CARMEL": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_321-PR-TestFold_5/Inference/CARMEL1-8",
                            "CARMEL 9-11": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_321-PR-TestFold_5/Inference/CARMEL9-11",
                        },
                    },
                },
            },
            "CARMEL->CARMEL 9-11": {
                "Fold None": {
                     "ER100": {
                        "DataSet Name": r"FEATURES: Exp_50214-ER100-TestFold_-1",
                        "TestSet Location": {
                            "CARMEL": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50214-ER100-TestFold_-1/Inference/CARMEL_fold12345_ER100_features/",
                            "CARMEL9": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50214-ER100-TestFold_-1/Inference/CARMEL9_ER100_features/",
                            "CARMEL10": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50214-ER100-TestFold_-1/Inference/CARMEL10_ER100_features/",
                            "CARMEL11": r"/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50214-ER100-TestFold_-1/Inference/CARMEL11_ER100_features/",
                        },
                    },
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_40022-ER-TestFold_-1",
                        "TestSet Location": {
                            "CARMEL": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40022-ER-TestFold_-1/Inference/CARMEL1-8",
                            "CARMEL9": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40022-ER-TestFold_-1/Inference/CARMEL9",
                            "CARMEL10": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40022-ER-TestFold_-1/Inference/CARMEL10",
                            "CARMEL11": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40022-ER-TestFold_-1/Inference/CARMEL11",
                        },
                    },
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_40023-Ki67-TestFold_-1",
                        "TestSet Location": {
                            "CARMEL": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40023-Ki67-TestFold_-1/Inference/CARMEL1-8",
                            "CARMEL9": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40023-Ki67-TestFold_-1/Inference/CARMEL9",
                            "CARMEL10": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40023-Ki67-TestFold_-1/Inference/CARMEL10",
                            "CARMEL11": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40023-Ki67-TestFold_-1/Inference/CARMEL11",
                        },
                    },
                }
            },
            "HIC": {
                "Fold None": {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40015-ER-TestFold_-1/Inference/HIC_ER_features_for_OR/",
                            "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40046-PR-TestFold_-1/Inference/HIC_PR_features_for_OR/",
                        ]
                    },
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_40015-ER-TestFold_-1, HIC ONLY Slides",
                        "TestSet Location": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40015-ER-TestFold_-1/Inference/HIC_new",
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1, HIC ONLY Slides",
                        "TestSet Location": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40046-PR-TestFold_-1/Inference/HIC_new",
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_40019-Her2-TestFold_-1, HIC ONLY Slides",
                        "TestSet Location": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40019-Her2-TestFold_-1/Inference/HIC_new",
                    },
                },
                "Fold 1": {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/HIC_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/HIC_PR_features_for_OR/",
                        ]
                    },
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_355-ER-TestFold_1, HIC ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/HIC_new",
                    },
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_419-Ki67-TestFold_1, HIC ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_419-Ki67-TestFold_1/Inference/HIC_new",
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_392-Her2-TestFold_1, HIC ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_392-Her2-TestFold_1/Inference/HIC_new",
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_20010-PR-TestFold_1, HIC ONLY Slides",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/HIC_new",
                    },
                },
                "Fold 2": {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/HIC_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/HIC_PR_features_for_OR/",
                        ]
                    },
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_393-ER-TestFold_2, HIC ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/HIC_new",
                    },
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_490-Ki67-TestFold_2, HIC ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_490-Ki67-TestFold_2/Inference/HIC_new",
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_412-Her2-TestFold_2, HIC ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_412-Her2-TestFold_2/Inference/HIC_new",
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_20063-PR-TestFold_2, HIC ONLY Slides",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/HIC_new",
                    },
                },
                "Fold 3": {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_472-ER-TestFold_3/Inference/HIC_ER_features_for_OR/",
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_497-PR-TestFold_3/Inference/HIC_PR_features_for_OR/",
                        ]
                    },
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_472-ER-TestFold_3, HIC ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_472-ER-TestFold_3/Inference/HIC_new",
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_20114-Her2-TestFold_3, HIC ONLY Slides",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20114-Her2-TestFold_3/Inference/HIC_new",
                    },
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_20152-Ki67-TestFold_3, HIC ONLY Slides",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20152-Ki67-TestFold_3/Inference/HIC_new",
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_497-PR-TestFold_3, HIC ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_497-PR-TestFold_3/Inference/HIC_new",
                    },
                },
                "Fold 4": {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_542-ER-TestFold_4/Inference/HIC_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20207-PR-TestFold_4/Inference/HIC_PR_features_for_OR/",
                        ]
                    },
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_542-ER-TestFold_4, HIC ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_542-ER-TestFold_4/Inference/HIC_new",
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_20201-Her2-TestFold_4, HIC ONLY Slides",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20201-Her2-TestFold_4/Inference/HIC_new",
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_20207-PR-TestFold_4, HIC ONLY Slides",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20207-PR-TestFold_4/Inference/HIC_new",
                    },
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_30090-Ki67-TestFold_4, HIC ONLY Slides",
                        "TestSet Location": r"/home/talneoran/workspace/wsi/legacy/runs/Exp_30090-Ki67-TestFold_4/Inference/HIC_new",
                    },
                },
                "Fold 5": {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_611-ER-TestFold_5/Inference/HIC_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20235-PR-TestFold_5/Inference/HIC_PR_features_for_OR/",
                        ]
                    },
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_611-ER-TestFold_5, HIC ONLY Slides",
                        "TestSet Location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_611-ER-TestFold_5/Inference/HIC_new",
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_20228-Her2-TestFold_5, HIC ONLY Slides",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20228-Her2-TestFold_5/Inference/HIC_new",
                    },
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_30092-Ki67-TestFold_5, HIC ONLY Slides",
                        "TestSet Location": r"/home/talneoran/workspace/wsi/legacy/runs/Exp_30092-Ki67-TestFold_5/Inference/HIC_new",
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_20235-PR-TestFold_5, HIC ONLY Slides",
                        "TestSet Location": r"/mnt/gipnetapp_public/sgils/ran/runs/Exp_20235-PR-TestFold_5/Inference/HIC_new",
                    },
                },
            },
            "TCGA_ABCTB->HIC": {
                "Fold None": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_40021-ER-TestFold_-1",
                        "TestSet Location": {
                            "HIC": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40021-ER-TestFold_-1/Inference/HIC_new"
                        },
                    }
                },
                "Fold 1": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_293-ER-TestFold_1",
                        "TestSet Location": {
                            "HIC": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_293-ER-TestFold_1/Inference/HIC_new"
                        },
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_308-Her2-TestFold_1",
                        "TestSet Location": {
                            "HIC": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_308-Her2-TestFold_1/Inference/HIC_new"
                        },
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_309-PR-TestFold_1",
                        "TestSet Location": {
                            "HIC": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_309-PR-TestFold_1/Inference/HIC_new"
                        },
                    },
                },
                "Fold 2": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_299-ER-TestFold_1",
                        "TestSet Location": {
                            "HIC": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_299-ER-TestFold_1/Inference/HIC_new"
                        },
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_310-Her2-TestFold_2",
                        "TestSet Location": {
                            "HIC": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_310-Her2-TestFold_2/Inference/HIC_new"
                        },
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_320-PR-TestFold_2",
                        "TestSet Location": {
                            "HIC": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_320-PR-TestFold_2/Inference/HIC_new"
                        },
                    },
                },
                "Fold 3": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_301-ER-TestFold_1",
                        "TestSet Location": {
                            "HIC": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_301-ER-TestFold_1/Inference/HIC_new"
                        },
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_311-Her2-TestFold_3",
                        "TestSet Location": {
                            "HIC": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_311-Her2-TestFold_3/Inference/HIC_new"
                        },
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_312-PR-TestFold_3",
                        "TestSet Location": {
                            "HIC": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_312-PR-TestFold_3/Inference/HIC_new"
                        },
                    },
                },
                "Fold 4": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_302-ER-TestFold_1",
                        "TestSet Location": {
                            "HIC": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_302-ER-TestFold_1/Inference/HIC_new"
                        },
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_334-Her2-TestFold_4",
                        "TestSet Location": {
                            "HIC": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_334-Her2-TestFold_4/Inference/HIC_new"
                        },
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_313-PR-TestFold_4",
                        "TestSet Location": {
                            "CARMEL": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_313-PR-TestFold_4/Inference/HIC_new"
                        },
                    },
                },
                "Fold 5": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_303-ER-TestFold_1",
                        "TestSet Location": {
                            "HIC": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_303-ER-TestFold_1/Inference/HIC_new"
                        },
                    },
                    "Her2": {
                        "DataSet Name": r"FEATURES: Exp_348-Her2-TestFold_5",
                        "TestSet Location": {
                            "HIC": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_348-Her2-TestFold_5/Inference/HIC_new"
                        },
                    },
                    "PR": {
                        "DataSet Name": r"FEATURES: Exp_321-PR-TestFold_5",
                        "TestSet Location": {
                            "HIC": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_321-PR-TestFold_5/Inference/HIC_new"
                        },
                    },
                },
            },
            "CARMEL->HIC": {
                "Fold None": {
                    "ER": {
                        "DataSet Name": r"FEATURES: Exp_40022-ER-TestFold_-1",
                        "TestSet Location": {
                            "HIC": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40022-ER-TestFold_-1/Inference/HIC_new"
                        },
                    },
                    "Ki67": {
                        "DataSet Name": r"FEATURES: Exp_40023-Ki67-TestFold_-1",
                        "TestSet Location": {
                            "HIC": r"/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40023-Ki67-TestFold_-1/Inference/HIC_new"
                        },
                    },
                }
            },
            'CAT->PORTUGAL': {
                'Fold None': {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40015-ER-TestFold_-1/Inference/PORTUGAL_ER_features_for_OR/",
                            "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40046-PR-TestFold_-1/Inference/PORTUGAL_PR_features_for_OR/",
                        ]
                    },
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40015-ER-TestFold_-1/Inference/PORTUGAL/'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40046-PR-TestFold_-1/Inference/PORTUGAL'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40019-Her2-TestFold_-1/Inference/PORTUGAL'
                    }
                },
                'Fold 1': {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/PORTUGAL_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/PORTUGAL_PR_features_for_OR/",
                        ]
                    },
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/PORTUGAL'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/PORTUGAL'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_392-Her2-TestFold_1/Inference/PORTUGAL'
                    }
                },
                'Fold 2': {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/PORTUGAL_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/PORTUGAL_PR_features_for_OR/",
                        ]
                    },
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/PORTUGAL'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/PORTUGAL'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_412-Her2-TestFold_2/Inference/PORTUGAL'
                    }
                },
                'Fold 3': {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_472-ER-TestFold_3/Inference/PORTUGAL_ER_features_for_OR/",
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_497-PR-TestFold_3/Inference/PORTUGAL_PR_features_for_OR/",
                        ]
                    },
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_472-ER-TestFold_3/Inference/PORTUGAL'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_497-PR-TestFold_3/Inference/PORTUGAL'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_20114-Her2-TestFold_3/Inference/PORTUGAL'
                    }
                },
                'Fold 4': {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_542-ER-TestFold_4/Inference/PORTUGAL_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20207-PR-TestFold_4/Inference/PORTUGAL_PR_features_for_OR/",
                        ]
                    },
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_542-ER-TestFold_4/Inference/PORTUGAL'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_20207-PR-TestFold_4/Inference/PORTUGAL'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_20201-Her2-TestFold_4/Inference/PORTUGAL'
                    }
                },
                'Fold 5': {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_611-ER-TestFold_5/Inference/PORTUGAL_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20235-PR-TestFold_5/Inference/PORTUGAL_PR_features_for_OR/",
                        ]
                    },
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_611-ER-TestFold_5/Inference/PORTUGAL'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_20235-PR-TestFold_5/Inference/PORTUGAL'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_20228-Her2-TestFold_5/Inference/PORTUGAL'
                    }
                }
            },
            'TCGA_ABCTB->PORTUGAL': {
                'Fold None': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40021-ER-TestFold_-1/Inference/PORTUGAL'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50219-PR-TestFold_-1/Inference/PORTUGAL'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50220-Her2-TestFold_-1/Inference/PORTUGAL'
                    }
                },
                'Fold 1': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_293-ER-TestFold_1/Inference/PORTUGAL'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_309-PR-TestFold_1/Inference/PORTUGAL'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_308-Her2-TestFold_1/Inference/PORTUGAL'
                    }
                },
                'Fold 2': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_299-ER-TestFold_2/Inference/PORTUGAL'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_320-PR-TestFold_2/Inference/PORTUGAL'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_310-Her2-TestFold_2/Inference/PORTUGAL'
                    }
                },
                'Fold 3': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_301-ER-TestFold_3/Inference/PORTUGAL'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_312-PR-TestFold_3/Inference/PORTUGAL'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_311-Her2-TestFold_3/Inference/PORTUGAL'
                    }
                },
                'Fold 4': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_302-ER-TestFold_4/Inference/PORTUGAL'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_313-PR-TestFold_4/Inference/PORTUGAL'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_334-Her2-TestFold_4/Inference/PORTUGAL'
                    }
                },
                'Fold 5': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_303-ER-TestFold_5/Inference/PORTUGAL'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_321-PR-TestFold_5/Inference/PORTUGAL'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_348-Her2-TestFold_5/Inference/PORTUGAL'
                    }
                }
            },
            'CARMEL->PORTUGAL': {
                'Fold None': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40022-ER-TestFold_-1/Inference/PORTUGAL'
                    }
                }
            },
            'CAT->TA 6': {
                'Fold None': {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40015-ER-TestFold_-1/Inference/TA_6_ER_features_for_OR/",
                            "/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40046-PR-TestFold_-1/Inference/TA_6_PR_features_for_OR/",
                        ]
                    },
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40015-ER-TestFold_-1/Inference/TA_fold6/'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40046-PR-TestFold_-1/Inference/TA_fold6'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40019-Her2-TestFold_-1/Inference/TA_fold6'
                    }
                },
                'Fold 1': {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/TA_6_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/TA_6_PR_features_for_OR/",
                        ]
                    },
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/TA_fold6'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/TA_fold6'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_392-Her2-TestFold_1/Inference/TA_fold6'
                    }
                },
                'Fold 2': {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/TA_6_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/TA_6_PR_features_for_OR/",
                        ]
                    },
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/TA_fold6'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/TA_fold6'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_412-Her2-TestFold_2/Inference/TA_fold6'
                    }
                },
                'Fold 3': {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_472-ER-TestFold_3/Inference/TA_6_ER_features_for_OR/",
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_497-PR-TestFold_3/Inference/TA_6_PR_features_for_OR/",
                        ]
                    },
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_472-ER-TestFold_3/Inference/TA_fold6'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_497-PR-TestFold_3/Inference/TA_fold6'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_20114-Her2-TestFold_3/Inference/TA_fold6'
                    }
                },
                'Fold 4': {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_542-ER-TestFold_4/Inference/TA_6_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20207-PR-TestFold_4/Inference/TA_6_PR_features_for_OR/",
                        ]
                    },
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_542-ER-TestFold_4/Inference/TA_fold6'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_20207-PR-TestFold_4/Inference/TA_fold6'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_20201-Her2-TestFold_4/Inference/TA_fold6'
                    }
                },
                'Fold 5': {
                    "ER_OR_PR": {
                        "DataSet Name": r"FEATURES: Exp_40046-PR-TestFold_-1+Exp_40015-ER-TestFold_-1, CARMEL ONLY Slides Batch 9-11",
                        "TestSet Location": [
                            "/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_611-ER-TestFold_5/Inference/TA_6_ER_features_for_OR/",
                            "/mnt/gipnetapp_public/sgils/ran/runs/Exp_20235-PR-TestFold_5/Inference/TA_6_PR_features_for_OR/",
                        ]
                    },
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_611-ER-TestFold_5/Inference/TA_fold6'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_20235-PR-TestFold_5/Inference/TA_fold6'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_20228-Her2-TestFold_5/Inference/TA_fold6'
                    }
                }
            },
            'TCGA_ABCTB->TA 6': {
                'Fold None': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40021-ER-TestFold_-1/Inference/TA_fold6'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50219-PR-TestFold_-1/Inference/TA_fold6'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50220-Her2-TestFold_-1/Inference/TA_fold6'
                    }
                },
                'Fold 1': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_293-ER-TestFold_1/Inference/TA_fold6'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_309-PR-TestFold_1/Inference/TA_fold6'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_308-Her2-TestFold_1/Inference/TA_fold6'
                    }
                },
                'Fold 2': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_299-ER-TestFold_2/Inference/TA_fold6'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_320-PR-TestFold_2/Inference/TA_fold6'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_310-Her2-TestFold_2/Inference/TA_fold6'
                    }
                },
                'Fold 3': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_301-ER-TestFold_3/Inference/TA_fold6'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_312-PR-TestFold_3/Inference/TA_fold6'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_311-Her2-TestFold_3/Inference/TA_fold6'
                    }
                },
                'Fold 4': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_302-ER-TestFold_4/Inference/TA_fold6'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_313-PR-TestFold_4/Inference/TA_fold6'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_334-Her2-TestFold_4/Inference/TA_fold6'
                    }
                },
                'Fold 5': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_303-ER-TestFold_5/Inference/TA_fold6'
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_321-PR-TestFold_5/Inference/TA_fold6'
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': 
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_348-Her2-TestFold_5/Inference/TA_fold6'
                    }
                }
            },
            'CARMEL->TA 6': {
                'Fold None': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': 
                        r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40022-ER-TestFold_-1/Inference/TA_fold6'
                    }
                }
            },
            'CARMEL->HAEMEK': {
                'Fold None': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40022-ER-TestFold_-1',
                        'TestSet Location': {
                            'HAEMEK':
                                r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40022-ER-TestFold_-1/Inference/HAEMEK'
                        }
                    },
                    'Ki67': {
                        'DataSet Name': r'FEATURES: Exp_40023-Ki67-TestFold_-1',
                        'TestSet Location': {
                            'HAEMEK':
                                r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40023-Ki67-TestFold_-1/Inference/HAEMEK'
                        }
                    }
                }
            },
            'TCGA_ABCTB->HAEMEK': {
                'Fold None': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40021-ER-TestFold_-1',
                        'TestSet Location': {
                            'HAEMEK':
                                r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40021-ER-TestFold_-1/Inference/HAEMEK'
                        }
                    }
                },
                'Fold 1': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40005-ER-TestFold_1',
                        'TestSet Location': {
                            'HAEMEK':
                                r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40005-ER-TestFold_1/Inference/HAEMEK'
                        }
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_308-Her2-TestFold_1',
                        'TestSet Location': {
                            'HAEMEK':
                                r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_308-Her2-TestFold_1/Inference/HAEMEK'
                        }
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_309-PR-TestFold_1',
                        'TestSet Location': {
                            'HAEMEK':
                                r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_309-PR-TestFold_1/Inference/HAEMEK'
                        }
                    }
                },
                'Fold 2': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40006-ER-TestFold_2',
                        'TestSet Location': {
                            'HAEMEK':
                                r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40006-ER-TestFold_2/Inference/HAEMEK'
                        }
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_310-Her2-TestFold_2',
                        'TestSet Location': {
                            'HAEMEK':
                                r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_310-Her2-TestFold_2/Inference/HAEMEK'
                        }
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_320-PR-TestFold_2',
                        'TestSet Location': {
                            'HAEMEK':
                                r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_320-PR-TestFold_2/Inference/HAEMEK'
                        }
                    }
                },
                'Fold 3': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40007-ER-TestFold_3',
                        'TestSet Location': {
                            'HAEMEK':
                                r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40007-ER-TestFold_3/Inference/HAEMEK'
                        }
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_311-Her2-TestFold_3',
                        'TestSet Location': {
                            'HAEMEK':
                                r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_311-Her2-TestFold_3/Inference/HAEMEK'
                        }
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_312-PR-TestFold_3',
                        'TestSet Location': {
                            'HAEMEK':
                                r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_312-PR-TestFold_3/Inference/HAEMEK'
                        }
                    }
                },
                'Fold 4': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40008-ER-TestFold_4',
                        'TestSet Location': {
                            'HAEMEK':
                                r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40008-ER-TestFold_4/Inference/HAEMEK'
                        }
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_334-Her2-TestFold_4',
                        'TestSet Location': {
                            'HAEMEK':
                                r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_334-Her2-TestFold_4/Inference/HAEMEK'
                        }
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_313-PR-TestFold_4',
                        'TestSet Location': {
                            'CARMEL':
                                r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_313-PR-TestFold_4/Inference/HAEMEK'
                        }
                    }
                },
                'Fold 5': {
                    'ER': {
                        'DataSet Name': r'FEATURES: Exp_40009-ER-TestFold_5',
                        'TestSet Location': {
                            'HAEMEK':
                                r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40009-ER-TestFold_5/Inference/HAEMEK'
                        }
                    },
                    'Her2': {
                        'DataSet Name': r'FEATURES: Exp_348-Her2-TestFold_5',
                        'TestSet Location': {
                            'HAEMEK':
                                r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_348-Her2-TestFold_5/Inference/HAEMEK'
                        }
                    },
                    'PR': {
                        'DataSet Name': r'FEATURES: Exp_321-PR-TestFold_5',
                        'TestSet Location': {
                            'HAEMEK':
                                r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_321-PR-TestFold_5/Inference/HAEMEK'
                        }
                    }
                },
            },
            'TCGA_GRADE': {
                'Fold 1': {
                    'Grade': {
                        'DataSet Name':
                        r'FEATURES: Exp_50219-PR-TestFold_-1',
                        'TrainSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50378-Grade-TestFold_1/Inference/tcga_456/',
                        'TestSet Location': 
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50378-Grade-TestFold_1/Inference/tcga_123/',
                        'REG Model Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50219-PR-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt'
                    },
                },
                'Fold 2': {
                    'Grade': {
                        'DataSet Name':
                        r'FEATURES: Exp_50219-PR-TestFold_-1',
                        'TrainSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50382-Grade-TestFold_2/Inference/tcga_123/',
                        'TestSet Location': 
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50382-Grade-TestFold_2/Inference/tcga_456/',
                        'REG Model Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50219-PR-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt'
                    },
                },
            },
            'TCGA_ABCTB': {
                'Fold None': {
                    'PR': {
                        'DataSet Name':
                        r'FEATURES: Exp_50219-PR-TestFold_-1',
                        'TrainSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50219-PR-TestFold_-1/Inference/TA_fold12345',
                        'TestSet Location': None,
                        'REG Model Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50219-PR-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt'
                    },
                    'Her2': {
                        'DataSet Name':
                        r'FEATURES: Exp_50220-Her2-TestFold_-1',
                        'TrainSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50220-Her2-TestFold_-1/Inference/TA_fold12345',
                        'TestSet Location': None,
                        'REG Model Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50220-Her2-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt'
                    },
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_40021-ER-TestFold_-1',
                        'TrainSet Location':
                        r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40021-ER-TestFold_-1/Inference/train_w_features',
                        'TestSet Location': None,
                        'REG Model Location':
                        r'/home/dahen/WSI_ran_legacy/WSI/runs/Exp_40021-ER-TestFold_-1/Model_CheckPoints/model_data_Last_Epoch.pt'
                    }
                },
                'Fold 1': {
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_293-ER-TestFold_1',
                        'TrainSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_293-ER-TestFold_1/Inference/train_inference_w_features',
                        'TestSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_293-ER-TestFold_1/Inference/test_inference_w_features',
                        'REG Model Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_293-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt'
                    },
                    'Her2': {
                        'DataSet Name':
                        r'FEATURES: Exp_308-Her2-TestFold_1',
                        'TrainSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_308-Her2-TestFold_1/Inference/train_w_features',
                        'TestSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_308-Her2-TestFold_1/Inference/test_w_features',
                        'REG Model Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_308-Her2-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt'
                    },
                    'PR': {
                        'DataSet Name':
                        r'FEATURES: Exp_309-PR-TestFold_1',
                        'TrainSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_309-PR-TestFold_1/Inference/train_w_features',
                        'TestSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_309-PR-TestFold_1/Inference/test_features_with_tiff_slides',
                        'REG Model Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_309-PR-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                },
                'Fold 2': {
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_299-ER-TestFold_2',
                        'TrainSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_299-ER-TestFold_2/Inference/train_w_features',
                        'TestSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_299-ER-TestFold_2/Inference/test_w_features',
                        'REG Model Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_299-ER-TestFold_2/Model_CheckPoints/model_data_Epoch_1000.pt'
                    },
                    'Her2': {
                        'DataSet Name':
                        r'FEATURES: Exp_310-Her2-TestFold_2',
                        'TrainSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_310-Her2-TestFold_2/Inference/train_w_features',
                        'TestSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_310-Her2-TestFold_2/Inference/test_w_features',
                        'REG Model Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_310-Her2-TestFold_2/Model_CheckPoints/model_data_Epoch_1000.pt'
                    },
                    'PR': {
                        'DataSet Name':
                        r'FEATURES: Exp_320-PR-TestFold_2',
                        'TrainSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_320-PR-TestFold_2/Inference/train_w_features',
                        'TestSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_320-PR-TestFold_2/Inference/test_w_features',
                        'REG Model Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_320-PR-TestFold_2/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                },
                'Fold 3': {
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_301-ER-TestFold_3',
                        'TrainSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_301-ER-TestFold_3/Inference/train_w_features',
                        'TestSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_301-ER-TestFold_3/Inference/test_w_features',
                        'REG Model Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_301-ER-TestFold_3/Model_CheckPoints/model_data_Epoch_1000.pt'
                    },
                    'Her2': {
                        'DataSet Name':
                        r'FEATURES: Exp_311-Her2-TestFold_3',
                        'TrainSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_311-Her2-TestFold_3/Inference/train_w_features',
                        'TestSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_311-Her2-TestFold_3/Inference/test_w_features',
                        'REG Model Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_311-Her2-TestFold_3/Model_CheckPoints/model_data_Epoch_1000.pt'
                    },
                    'PR': {
                        'DataSet Name':
                        r'FEATURES: Exp_312-PR-TestFold_3',
                        'TrainSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_312-PR-TestFold_3/Inference/train_w_features',
                        'TestSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_312-PR-TestFold_3/Inference/test_w_features',
                        'REG Model Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_312-PR-TestFold_3/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                },
                'Fold 4': {
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_302-ER-TestFold_4',
                        'TrainSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_302-ER-TestFold_4/Inference/train_w_features',
                        'TestSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_302-ER-TestFold_4/Inference/test_w_features',
                        'REG Model Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_302-ER-TestFold_4/Model_CheckPoints/model_data_Epoch_1000.pt'
                    },
                    'Her2': {
                        'DataSet Name':
                        r'FEATURES: Exp_334-Her2-TestFold_4',
                        'TrainSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_334-Her2-TestFold_4/Inference/train_w_features',
                        'TestSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_334-Her2-TestFold_4/Inference/test_w_features',
                        'REG Model Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_334-Her2-TestFold_4/Model_CheckPoints/model_data_Epoch_1000.pt'
                    },
                    'PR': {
                        'DataSet Name':
                        r'FEATURES: Exp_313-PR-TestFold_4',
                        'TrainSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_313-PR-TestFold_4/Inference/train_w_features',
                        'TestSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_313-PR-TestFold_4/Inference/test_w_features',
                        'REG Model Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_313-PR-TestFold_4/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                },
                'Fold 5': {
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_303-ER-TestFold_5',
                        'TrainSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_303-ER-TestFold_5/Inference/train_w_features',
                        'TestSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_303-ER-TestFold_5/Inference/test_w_features',
                        'REG Model Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_303-ER-TestFold_5/Model_CheckPoints/model_data_Epoch_1000.pt'
                    },
                    'Her2': {
                        'DataSet Name':
                        r'FEATURES: Exp_348-Her2-TestFold_5',
                        'TrainSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_348-Her2-TestFold_5/Inference/train_w_features',
                        'TestSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_348-Her2-TestFold_5/Inference/test_w_features',
                        'REG Model Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_348-Her2-TestFold_5/Model_CheckPoints/model_data_Epoch_1000.pt'
                    },
                    'PR': {
                        'DataSet Name':
                        r'FEATURES: Exp_321-PR-TestFold_5',
                        'TrainSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_321-PR-TestFold_5/Inference/train_w_features',
                        'TestSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_321-PR-TestFold_5/Inference/test_w_features',
                        'REG Model Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_321-PR-TestFold_5/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                },
            },
            'CAT with Location': {
                'Fold 1': {
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_355-ER-TestFold_1 With Locations',
                        'TrainSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/train_w_features_w_locs',
                        'TestSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/test_w_features_locs',
                        'REG Model Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt'
                    },
                    'Her2': {
                        'DataSet Name':
                        r'FEATURES: Exp_392-Her2-TestFold_1 With Locations',
                        'TrainSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_392-Her2-TestFold_1/Inference/train_w_features',
                        'TestSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_392-Her2-TestFold_1/Inference/test_w_locs_w_features',
                        'REG Model Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_392-Her2-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt'
                    },
                    'PR': {
                        'DataSet Name':
                        r'FEATURES: Exp_10-PR-TestFold_1  With Locations',
                        'TrainSet Location':
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/train_w_features_new',
                        'TestSet Location':
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Inference/test_w_locs_w_features',
                        'REG Model Location':
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_10-PR-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt'
                    },
                },
                'Fold 2': {
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_393-ER-TestFold_2 With Locations',
                        'TrainSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/train_w_features_new',
                        'TestSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Inference/test_w_features',
                        'REG Model Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_393-ER-TestFold_2/Model_CheckPoints/model_data_Epoch_1000.pt'
                    },
                    'Her2': {
                        'DataSet Name':
                        r'FEATURES: Exp_412-Her2-TestFold_2 With Locations',
                        'TrainSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_412-Her2-TestFold_2/Inference/train_w_features',
                        'TestSet Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_412-Her2-TestFold_2/Inference/test_w_features',
                        'REG Model Location':
                        r'/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_412-Her2-TestFold_2/Model_CheckPoints/model_data_Epoch_1000.pt'
                    },
                    'PR': {
                        'DataSet Name':
                        r'FEATURES: Exp_20063-PR-TestFold_2 With Locations',
                        'TrainSet Location':
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/train_w_features_new',
                        'TestSet Location':
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Inference/test_w_features',
                        'REG Model Location':
                        r'/mnt/gipnetapp_public/sgils/ran/runs/Exp_20063-PR-TestFold_2/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                }
            },
            'HAEMEK_transfer': {
                'Fold 1': {
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_50015-ER-TestFold_1 transfered from CAT',
                        'TrainSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50015-ER-TestFold_1/Inference/features_fold2345',
                        'TestSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50015-ER-TestFold_1/Inference/features_fold1',
                        'REG Model Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50015-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                },
                'Fold 2': {
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_50143-ER-TestFold_2 transfered from CAT',
                        'TrainSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50143-ER-TestFold_2/Inference/features_fold1345/',
                        'TestSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50143-ER-TestFold_2/Inference/features_fold2/',
                        'REG Model Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50143-ER-TestFold_2/Model_CheckPoints/model_data_Epoch_400.pt'
                    }
                },
                'Fold 3': {
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_50157-ER-TestFold_3 transfered from CAT',
                        'TrainSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50157-ER-TestFold_3/Inference/features_fold1245/',
                        'TestSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50157-ER-TestFold_3/Inference/features_fold3/',
                        'REG Model Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50157-ER-TestFold_3/Model_CheckPoints/model_data_Epoch_400.pt'
                    }
                },
                'Fold 4': {
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_50171-ER-TestFold_4 transfered from CAT',
                        'TrainSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50171-ER-TestFold_4/Inference/features_fold1235/',
                        'TestSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50171-ER-TestFold_4/Inference/features_fold4/',
                        'REG Model Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50171-ER-TestFold_4/Model_CheckPoints/model_data_Epoch_400.pt'
                    }
                }
            },
            'HAEMEK_finetuned': {
                'Fold 1': {
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_50151-ER-TestFold_1 finetuned from CAT',
                        'TrainSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50151-ER-TestFold_1/Inference/features_fold2345',
                        'TestSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50151-ER-TestFold_1/Inference/features_fold1',
                        'REG Model Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50151-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_400.pt'
                    }
                },
                'Fold 2': {
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_50161-ER-TestFold_2 finetuned from CAT',
                        'TrainSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50161-ER-TestFold_2/Inference/features_fold1345',
                        'TestSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50161-ER-TestFold_2/Inference/features_fold2/',
                        'REG Model Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50161-ER-TestFold_2/Model_CheckPoints/model_data_Epoch_400.pt'
                    }
                },
                'Fold 3': {
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_50163-ER-TestFold_3 finetuned from CAT',
                        'TrainSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50163-ER-TestFold_3/Inference/features_fold1245',
                        'TestSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50163-ER-TestFold_3/Inference/features_fold3/',
                        'REG Model Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50163-ER-TestFold_3/Model_CheckPoints/model_data_Epoch_400.pt'
                    }
                },
                'Fold 4': {
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_50172-ER-TestFold_4 finetuned from CAT',
                        'TrainSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50172-ER-TestFold_4/Inference/features_fold1235',
                        'TestSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50172-ER-TestFold_4/Inference/features_fold4/',
                        'REG Model Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50172-ER-TestFold_4/Model_CheckPoints/model_data_Epoch_400.pt'
                    }
                }
            },
            #only HAEMEK is actually CAT->HAEMEK
            'HAEMEK->HAEMEK': {
                'Fold 1': {
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_50014-ER-TestFold_1 trained from scratch',
                        'TrainSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50014-ER-TestFold_1/Inference/features_fold2345',
                        'TestSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50014-ER-TestFold_1/Inference/features_fold1',
                        'REG Model Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50014-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                },
                'Fold 2': {
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_50142-ER-TestFold_2 trained from scratch',
                        'TrainSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50142-ER-TestFold_2/Inference/features_fold1345',
                        'TestSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50142-ER-TestFold_2/Inference/features_fold2',
                        'REG Model Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50142-ER-TestFold_2/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                },
                'Fold 3': {
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_50159-ER-TestFold_3 trained from scratch',
                        'TrainSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50159-ER-TestFold_3/Inference/features_fold1245',
                        'TestSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50159-ER-TestFold_3/Inference/features_fold3',
                        'REG Model Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50159-ER-TestFold_3/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                },
                'Fold 4': {
                    'ER': {
                        'DataSet Name':
                        r'FEATURES: Exp_50175-ER-TestFold_4 trained from scratch',
                        'TrainSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50175-ER-TestFold_4/Inference/features_fold1235',
                        'TestSet Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50175-ER-TestFold_4/Inference/features_fold4',
                        'REG Model Location':
                        r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50175-ER-TestFold_4/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                }
            },
            'SHEBA': {
                'Fold None': {
                    'onco_score_26': {
                        'DataSet Name': r'FEATURES: Exp_50209-onco_score_26-TestFold_-1',
                        'TrainSet Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50209-onco_score_26-TestFold_-1/Inference/SHEBA_fold12345_onco_features/',
                        'TestSet Location': None,
                        'REG Model Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50209-onco_score_26-TestFold_-1/Model_CheckPoints/model_data_Epoch_1000.pt'
                    },
                    'onco_score_31': {
                        'DataSet Name': r'FEATURES: Exp_50212-onco_score_31-TestFold_-1',
                        'TrainSet Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50212-onco_score_31-TestFold_-1/Inference/SHEBA_fold12345_onco_features/',
                        'TestSet Location': None,
                        'REG Model Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50212-onco_score_31-TestFold_-1/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                },
                'Fold 1': {
                    'onco_score_26': {
                        'DataSet Name': r'FEATURES: Exp_50197-onco_score_26-TestFold_1',
                        'TrainSet Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50197-onco_score_26-TestFold_1/Inference/SHEBA_fold2345_onco_features/',
                        'TestSet Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50197-onco_score_26-TestFold_1/Inference/SHEBA_fold1_onco_features/',
                        'REG Model Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50197-onco_score_26-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                },
                'Fold 2': {
                    'onco_score_26': {
                        'DataSet Name': r'FEATURES: Exp_50200-onco_score_26-TestFold_2',
                        'TrainSet Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50200-onco_score_26-TestFold_2/Inference/SHEBA_fold1345_onco_features/',
                        'TestSet Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50200-onco_score_26-TestFold_2/Inference/SHEBA_fold2_onco_features/',
                        'REG Model Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50200-onco_score_26-TestFold_2/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                },
                'Fold 3': {
                    'onco_score_26': {
                        'DataSet Name': r'FEATURES: Exp_50202-onco_score_26-TestFold_3',
                        'TrainSet Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50202-onco_score_26-TestFold_3/Inference/SHEBA_fold1245_onco_features/',
                        'TestSet Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50202-onco_score_26-TestFold_3/Inference/SHEBA_fold3_onco_features/',
                        'REG Model Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50202-onco_score_26-TestFold_3/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                },
                'Fold 4': {
                    'onco_score_26': {
                        'DataSet Name': r'FEATURES: Exp_50203-onco_score_26-TestFold_4',
                        'TrainSet Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50203-onco_score_26-TestFold_4/Inference/SHEBA_fold1235_onco_features/',
                        'TestSet Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50203-onco_score_26-TestFold_4/Inference/SHEBA_fold4_onco_features/',
                        'REG Model Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50203-onco_score_26-TestFold_4/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                },
                'Fold 5': {
                    'onco_score_26': {
                        'DataSet Name': r'FEATURES: Exp_50204-onco_score_26-TestFold_5',
                        'TrainSet Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50204-onco_score_26-TestFold_5/Inference/SHEBA_fold1234_onco_features/',
                        'TestSet Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50204-onco_score_26-TestFold_5/Inference/SHEBA_fold5_onco_features/',
                        'REG Model Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50204-onco_score_26-TestFold_5/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                }
            },
            'SHEBA->SHEBA 6': {
                'Fold None': {
                    'onco_score_26': {
                        'DataSet Name': r'FEATURES: Exp_50209-onco_score_26-TestFold_-1',
                        'TestSet Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50209-onco_score_26-TestFold_-1/Inference/SHEBA_fold6_onco_features/',
                        'REG Model Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50209-onco_score_26-TestFold_-1/Model_CheckPoints/model_data_Epoch_1000.pt'
                    },
                    'onco_score_31': {
                        'DataSet Name': r'FEATURES: Exp_50212-onco_score_31-TestFold_-1',
                        'TestSet Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50212-onco_score_31-TestFold_-1/Inference/SHEBA_fold6_onco_features/',
                        'REG Model Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50212-onco_score_31-TestFold_-1/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                },
                'Fold 1': {
                    'onco_score_26': {
                        'DataSet Name': r'FEATURES: Exp_50197-onco_score_26-TestFold_1',
                        'TestSet Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50197-onco_score_26-TestFold_1/Inference/SHEBA_fold6_onco_features/',
                        'REG Model Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50197-onco_score_26-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                },
                'Fold 2': {
                    'onco_score_26': {
                        'DataSet Name': r'FEATURES: Exp_50200-onco_score_26-TestFold_2',
                        'TestSet Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50200-onco_score_26-TestFold_2/Inference/SHEBA_fold6_onco_features/',
                        'REG Model Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50200-onco_score_26-TestFold_2/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                },
                'Fold 3': {
                    'onco_score_26': {
                        'DataSet Name': r'FEATURES: Exp_50202-onco_score_26-TestFold_3',
                        'TestSet Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50202-onco_score_26-TestFold_3/Inference/SHEBA_fold6_onco_features/',
                        'REG Model Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50202-onco_score_26-TestFold_3/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                },
                'Fold 4': {
                    'onco_score_26': {
                        'DataSet Name': r'FEATURES: Exp_50203-onco_score_26-TestFold_4',
                        'TestSet Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50203-onco_score_26-TestFold_4/Inference/SHEBA_fold6_onco_features/',
                        'REG Model Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50203-onco_score_26-TestFold_4/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                },
                'Fold 5': {
                    'onco_score_26': {
                        'DataSet Name': r'FEATURES: Exp_50204-onco_score_26-TestFold_5',
                        'TestSet Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50204-onco_score_26-TestFold_5/Inference/SHEBA_fold6_onco_features/',
                        'REG Model Location': r'/home/shacharcohen/workspace/WSI/legacy/runs/Exp_50204-onco_score_26-TestFold_5/Model_CheckPoints/model_data_Epoch_1000.pt'
                    }
                }
            }
        }
    }

    if "+is_Tumor" in target:
        receptor = target.split("+")[0]
        if receptor == "Her2":
            return (
                All_Data_Dict[sys.platform][train_DataSet]["Fold " + str(test_fold)][
                    receptor
                ],
                All_Data_Dict[sys.platform][train_DataSet]["Fold " + str(test_fold)][
                    "is_Tumor_for_Her2"
                ],
            )

        elif receptor == "PR":
            return (
                All_Data_Dict[sys.platform][train_DataSet]["Fold " + str(test_fold)][
                    receptor
                ],
                All_Data_Dict[sys.platform][train_DataSet]["Fold " + str(test_fold)][
                    "is_Tumor_for_PR"
                ],
            )

        elif receptor == "ER":
            return (
                All_Data_Dict[sys.platform][train_DataSet]["Fold " + str(test_fold)][
                    "ER_for_is_Tumor"
                ],
                All_Data_Dict[sys.platform][train_DataSet]["Fold " + str(test_fold)][
                    "is_Tumor_for_ER"
                ],
            )

    else:
        return All_Data_Dict[sys.platform][train_DataSet]["Fold " + str(test_fold)][
            target
        ]


def dataset_properties_to_location(
    dataset_name_list: list, receptor: str, test_fold: int, is_train: bool = False
):
    # Basic data definition:
    if sys.platform == "darwin":
        dataset_full_data_dict = {
            "TCGA_ABCTB": {
                "ER": {
                    1: {
                        "Train": r"/Users/wasserman/Developer/WSI_MIL/All Data/Features/ER/Ran_Exp_293-TestFold_1/Train",
                        "Test": r"/Users/wasserman/Developer/WSI_MIL/All Data/Features/ER/Ran_Exp_293-TestFold_1/Test",
                        "Dataset name": r"FEATURES: Exp_293-ER-TestFold_1",
                    }
                }
            },
            "CAT": {
                "ER": {
                    1: {
                        "Train": r"/Users/wasserman/Developer/WSI_MIL/All Data/Features/ER/Ran_Exp_355-TestFold_1/Train",
                        "Test": r"/Users/wasserman/Developer/WSI_MIL/All Data/Features/ER/Ran_Exp_355-TestFold_1/Test",
                        "Dataset name": r"FEATURES: Exp_355-ER-TestFold_1",
                        "Regular model location": r"/Users/wasserman/Developer/WSI_MIL/Data from gipdeep/runs/Ran_models/ER/CAT_355_TF_1/model_data_Epoch_1000.pt",
                    }
                }
            },
            "CARMEL": {
                "ER": {
                    1: {
                        "Train": r"/Users/wasserman/Developer/WSI_MIL/All Data/Features/ER/Ran_Exp_358-TestFold_1/Train",
                        "Test": r"/Users/wasserman/Developer/WSI_MIL/All Data/Features/ER/Ran_Exp_358-TestFold_1/Test",
                        "Dataset name": r"FEATURES: Exp_358-ER-TestFold_1",
                        "Regular model location": r"/Users/wasserman/Developer/WSI_MIL/Data from gipdeep/runs/Ran_models/ER/CARMEL_358-TF_1/model_data_Epoch_1000.pt",
                    }
                }
            },
            "CARMEL_40": {
                "ER": {
                    1: {
                        "Train": r"/Users/wasserman/Developer/WSI_MIL/All Data/Features/ER/Ran_Exp_381-TestFold_1/Train",
                        "Test": r"/Users/wasserman/Developer/WSI_MIL/All Data/Features/ER/Ran_Exp_381-TestFold_1/Test",
                        "Dataset name": r"FEATURES: Exp_381-ER-TestFold_1",
                        "Regular model location": r"/Users/wasserman/Developer/WSI_MIL/Data from gipdeep/runs/Ran_models/ER/CARMEL_381-TF_1/model_data_Epoch_1200.pt",
                    }
                }
            },
        }
    elif sys.platform == "linux":
        dataset_full_data_dict = {
            "TCGA_ABCTB": {
                "ER": {
                    1: {
                        "Train": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_293-ER-TestFold_1/Inference/train_inference_w_features",
                        "Test": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_293-ER-TestFold_1/Inference/test_inference_w_features",
                        "Dataset name": r"FEATURES: Exp_293-ER-TestFold_1",
                    }
                }
            },
            "CAT": {
                "ER": {
                    1: {
                        "Train": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/train_w_features",
                        "Test": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Inference/test_w_features",
                        "Dataset name": r"FEATURES: Exp_355-ER-TestFold_1",
                        "Regular model location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_355-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    }
                }
            },
            "CARMEL": {
                "ER": {
                    1: {
                        "Train": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_358-ER-TestFold_1/Inference/train_w_features",
                        "Test": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_358-ER-TestFold_1/Inference/test_w_features",
                        "Dataset name": r"FEATURES: Exp_358-ER-TestFold_1",
                        "Regular model location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_358-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1000.pt",
                    }
                }
            },
            "CARMEL_40": {
                "ER": {
                    1: {
                        "Train": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_381-ER-TestFold_1/Inference/train_w_features",
                        "Test": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_381-ER-TestFold_1/Inference/test_w_features",
                        "Dataset name": r"FEATURES: Exp_358-ER-TestFold_1",
                        "Regular model location": r"/home/rschley/code/WSI_MIL/WSI_MIL/runs/Exp_381-ER-TestFold_1/Model_CheckPoints/model_data_Epoch_1200.pt",
                    }
                }
            },
        }

    dataset_location_list = []

    if receptor == "ER_Features":
        receptor = "ER"
    for dataset in dataset_name_list:
        location = dataset_full_data_dict[dataset][receptor][test_fold][
            "Train" if is_train else "Test"
        ]
        dataset_name = dataset_full_data_dict[dataset][receptor][test_fold][
            "Dataset name"
        ]
        regular_model_location = dataset_full_data_dict[dataset][receptor][test_fold][
            "Regular model location"
        ]
        dataset_location_list.append(
            [dataset, location, dataset_name, regular_model_location]
        )

    return dataset_location_list


def save_all_slides_and_models_data(
    all_slides_tile_scores,
    all_slides_final_scores,
    all_slides_weights_before_softmax,
    all_slides_weights_after_softmax,
    models,
    Output_Dirs,
    Epochs,
    data_path,
    true_test_path: str = "",
    sub_dir: str = "",
):
    # Save slide scores to file:
    for num_model in range(len(models)):
        if type(Output_Dirs) == str:
            output_dir = Output_Dirs
        elif type(Output_Dirs) is list:
            output_dir = Output_Dirs[num_model]

        epoch = Epochs[num_model]
        model = models[num_model]

        full_output_dir = os.path.join(
            data_path,
            output_dir,
            "Inference",
            "Tile_Scores",
            "Epoch_" + str(epoch),
            true_test_path,
            sub_dir,
        )

        if not os.path.isdir(full_output_dir):
            Path(full_output_dir).mkdir(parents=True)

        model_bias_filename = "bias.xlsx"
        full_model_bias_filename = os.path.join(full_output_dir, model_bias_filename)
        if not os.path.isfile(full_model_bias_filename):
            try:  # In case this part in not packed in Sequential we'll need this try statement
                last_layer_bias = model.classifier[0].bias.detach().cpu().numpy()
            except TypeError:
                last_layer_bias = model.classifier.bias.detach().cpu().numpy()

            last_layer_bias_diff = last_layer_bias[1] - last_layer_bias[0]

            last_layer_bias_DF = pd.DataFrame([last_layer_bias_diff])
            last_layer_bias_DF.to_excel(full_model_bias_filename)

        if type(all_slides_tile_scores) == dict:
            all_slides_tile_scores_REG = all_slides_tile_scores["REG"]
            all_slides_final_scores_REG = all_slides_final_scores["REG"]
            all_slides_tile_scores = all_slides_tile_scores["MIL"]
            all_slides_final_scores = all_slides_final_scores["MIL"]

            all_slides_tile_scores_REG_DF = pd.DataFrame(
                all_slides_tile_scores_REG[num_model]
            ).transpose()
            all_slides_final_scores_REG_DF = pd.DataFrame(
                all_slides_final_scores_REG[num_model]
            ).transpose()

            tile_scores_file_name_REG = os.path.join(
                full_output_dir, "tile_scores_REG.xlsx"
            )
            slide_score_file_name_REG = os.path.join(
                full_output_dir, "slide_scores_REG.xlsx"
            )

            all_slides_tile_scores_REG_DF.to_excel(tile_scores_file_name_REG)
            all_slides_final_scores_REG_DF.to_excel(slide_score_file_name_REG)

        all_slides_tile_scores_DF = pd.DataFrame(
            all_slides_tile_scores[num_model]
        ).transpose()
        all_slides_final_scores_DF = pd.DataFrame(
            all_slides_final_scores[num_model]
        ).transpose()
        all_slides_weights_before_sofrmax_DF = pd.DataFrame(
            all_slides_weights_before_softmax[num_model]
        ).transpose()
        all_slides_weights_after_softmax_DF = pd.DataFrame(
            all_slides_weights_after_softmax[num_model]
        ).transpose()

        tile_scores_file_name = os.path.join(full_output_dir, "tile_scores.xlsx")
        slide_score_file_name = os.path.join(full_output_dir, "slide_scores.xlsx")
        tile_weights_before_softmax_file_name = os.path.join(
            full_output_dir, "tile_weights_before_softmax.xlsx"
        )
        tile_weights_after_softmax_file_name = os.path.join(
            full_output_dir, "tile_weights_after_softmax.xlsx"
        )

        all_slides_tile_scores_DF.to_excel(tile_scores_file_name)
        all_slides_final_scores_DF.to_excel(slide_score_file_name)
        all_slides_weights_before_sofrmax_DF.to_excel(
            tile_weights_before_softmax_file_name
        )
        all_slides_weights_after_softmax_DF.to_excel(
            tile_weights_after_softmax_file_name
        )

        logging.info(
            "Tile scores for model {}/{} has been saved !".format(
                num_model + 1, len(models)
            )
        )


def extract_tile_scores_for_slide(all_features, models, is_or=False):
    """
    If all_features has shape[0] == 1024, than it;s originated from train type Receptor + is_Tumor.
    In that case we'll need only the first 512 features to compute the tile scores.
    """
    if all_features.shape[0] == 1024 and not is_or:
        all_features = all_features[:512, :]

    # Save tile scores and last models layer bias difference to file:
    tile_scores_list = []
    for index in range(len(models)):
        model = models[index]
        # Compute for each tile the multiplication between its feature vector and the last layer weight difference
        # vector:
        try:  # In case this part in not packed in Sequential we'll need this try statement
            last_layer_weights = model.classifier[0].weight.detach().cpu().numpy()
        except TypeError:
            last_layer_weights = model.classifier.weight.detach().cpu().numpy()

        f = last_layer_weights[1] - last_layer_weights[0]
        mult = np.matmul(f, all_features.detach().cpu())

        if len(mult.shape) == 1:
            tile_scores_list.append(mult)
        else:
            tile_scores_list.append(mult[:, index])

    return tile_scores_list