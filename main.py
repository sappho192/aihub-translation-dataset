import os
from AiHub.AiHubDataset027 import AiHubDataset027

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
print(f'{dataset027.get_dataset_name()}')
