import os
from AiHub.AiHubDataset027 import AiHubDataset027
from AiHub.AiHubDataset053 import AiHubDataset053
from AiHub.AiHubDataset054 import AiHubDataset054
from AiHub.AiHubDataset055 import AiHubDataset055
from AiHub.AiHubDatasetKoJaTr import AiHubDatasetKoJaTr
from AiHub.util.DatasetGenerator import merge_aihub_datasets, save_dataset_to_json, save_dataset_to_jsonl, \
    save_dataset_to_csv

AIHUB_ROOT = "K:\\DATASET\\aihub"

DATASET_NAME_027 = "027.일상생활 및 구어체 한-중, 한-일 번역 병렬 말뭉치 데이터"
DATASET_027 = os.path.join(AIHUB_ROOT, DATASET_NAME_027, "01.데이터")
DATASET_NAME_053 = "053.한국어-다국어(영어 제외) 번역 말뭉치(기술과학)"
DATASET_053 = os.path.join(AIHUB_ROOT, DATASET_NAME_053, "01-1.정식개방데이터")
DATASET_NAME_054 = "054.한국어-다국어 번역 말뭉치(기초과학)"
DATASET_054 = os.path.join(AIHUB_ROOT, DATASET_NAME_054, "01-1.정식개방데이터")
DATASET_NAME_055 = "055.한국어-다국어 번역 말뭉치(인문학)"
DATASET_055 = os.path.join(AIHUB_ROOT, DATASET_NAME_055, "01-1.정식개방데이터")
DATASET_NAME_KOJATR = "한국어-일본어 번역 말뭉치"
DATASET_KoJaTr = os.path.join(AIHUB_ROOT, DATASET_NAME_KOJATR)

dataset027 = AiHubDataset027(DATASET_NAME_027, DATASET_027)
print(f'Loaded {dataset027.get_dataset_name()}')

dataset053 = AiHubDataset053(DATASET_NAME_053, DATASET_053)
print(f'Loaded {dataset053.get_dataset_name()}')

dataset054 = AiHubDataset054(DATASET_NAME_054, DATASET_054)
print(f'Loaded {dataset054.get_dataset_name()}')

dataset055 = AiHubDataset055(DATASET_NAME_055, DATASET_055)
print(f'Loaded {dataset055.get_dataset_name()}')

datasetKoJaTr = AiHubDatasetKoJaTr(DATASET_NAME_KOJATR, DATASET_KoJaTr)
print(f'Loaded {datasetKoJaTr.get_dataset_name()}')

merged_dataset_train = merge_aihub_datasets(dataset027.get_dataset_train(),
                                            dataset053.get_dataset_train(),
                                            dataset054.get_dataset_train(),
                                            dataset055.get_dataset_train(),
                                            datasetKoJaTr.get_dataset_train())

print(f'Merged {len(merged_dataset_train)} train datasets to merged_dataset_train')

merged_dataset_val = merge_aihub_datasets(dataset027.get_dataset_val(),
                                            dataset053.get_dataset_val(),
                                            dataset054.get_dataset_val(),
                                            dataset055.get_dataset_val(),
                                            datasetKoJaTr.get_dataset_val())

print(f'Merged {len(merged_dataset_val)} val datasets to merged_dataset_val')

# Save merged datasets to JSON files
DATASET_MERGED = os.path.join(AIHUB_ROOT, "merged")
os.makedirs(DATASET_MERGED, exist_ok=True)

DATASET_MERGED_TRAIN = os.path.join(DATASET_MERGED, "train.json")
DATASET_MERGED_VAL = os.path.join(DATASET_MERGED, "val.json")

print(f'Saving merged datasets to {DATASET_MERGED_TRAIN} and {DATASET_MERGED_VAL}')
save_dataset_to_json(merged_dataset_train, DATASET_MERGED_TRAIN)
save_dataset_to_json(merged_dataset_val, DATASET_MERGED_VAL)

DATASET_MERGED_TRAIN = os.path.join(DATASET_MERGED, "train.jsonl")
DATASET_MERGED_VAL = os.path.join(DATASET_MERGED, "val.jsonl")

print(f'Saving merged datasets to {DATASET_MERGED_TRAIN} and {DATASET_MERGED_VAL}')
save_dataset_to_jsonl(merged_dataset_train, DATASET_MERGED_TRAIN)
save_dataset_to_jsonl(merged_dataset_val, DATASET_MERGED_VAL)

DATASET_MERGED_TRAIN = os.path.join(DATASET_MERGED, "train.csv")
DATASET_MERGED_VAL = os.path.join(DATASET_MERGED, "val.csv")

print(f'Saving merged datasets to {DATASET_MERGED_TRAIN} and {DATASET_MERGED_VAL}')
save_dataset_to_csv(merged_dataset_train, DATASET_MERGED_TRAIN)
save_dataset_to_csv(merged_dataset_val, DATASET_MERGED_VAL)

print('Done')
