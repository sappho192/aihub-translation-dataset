import os
import json

from AiHub.AiHubDatasetBase import AiHubDatasetBase


class AiHubDataset027(AiHubDatasetBase):
    def __init__(self, dataset_name, dataset_root):
        dataset_train_root = os.path.join(dataset_root, "1_Training", "라벨링데이터", "TL1")
        dataset_val_root = os.path.join(dataset_root, "2_Validation", "라벨링데이터", "VL1")
        super().__init__(dataset_name, dataset_root, dataset_train_root, dataset_val_root)
        self.make_dataset()

    def make_dataset(self):
        self._dataset_train = self.make_train_dataset()
        self._dataset_val = self.make_val_dataset()

    def make_train_dataset(self):
        labeledJKDataRoot = os.path.join(self._dataset_train_root, "일한")
        usualLifeDataRoot = os.path.join(labeledJKDataRoot, "일상생활")
        chatDataRoot = os.path.join(labeledJKDataRoot, "채팅")
        overseaSalesRoot = os.path.join(labeledJKDataRoot, "해외영업")

        # Set json path
        usualLifeJKJsonPath = os.path.join(usualLifeDataRoot, "라벨링데이터_일한_일상생활_TTA품질검증_250000_training.json")
        chatJKJsonPath = os.path.join(chatDataRoot, "라벨링데이터_일한_채팅_TTA품질검증_150000_training.json")
        overseaSalesJKJsonPath = os.path.join(overseaSalesRoot, "라벨링데이터_일한_해외영업_TTA품질검증_350000_training.json")

        # Read json file
        usualLifeJKData = self.read_json(usualLifeJKJsonPath)
        chatJKData = self.read_json(chatJKJsonPath)
        overseaSalesJKData = self.read_json(overseaSalesJKJsonPath)

        return [usualLifeJKData, chatJKData, overseaSalesJKData]

    def make_val_dataset(self):
        labeledJKDataRoot = os.path.join(self._dataset_val_root, "일한")
        usualLifeDataRoot = os.path.join(labeledJKDataRoot, "일상생활")
        chatDataRoot = os.path.join(labeledJKDataRoot, "채팅")
        overseaSalesRoot = os.path.join(labeledJKDataRoot, "해외영업")

        # Set json path
        usualLifeJKJsonPath = os.path.join(usualLifeDataRoot, "라벨링데이터_일한_일상생활_TTA품질검증_250000_validation.json")
        chatJKJsonPath = os.path.join(chatDataRoot, "라벨링데이터_일한_채팅_TTA품질검증_150000_validation.json")
        overseaSalesJKJsonPath = os.path.join(overseaSalesRoot, "라벨링데이터_일한_해외영업_TTA품질검증_350000_validation.json")

        # Read json file
        usualLifeJKData = self.read_json(usualLifeJKJsonPath)
        chatJKData = self.read_json(chatJKJsonPath)
        overseaSalesJKData = self.read_json(overseaSalesJKJsonPath)

        return [usualLifeJKData, chatJKData, overseaSalesJKData]

    def read_json(self, json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        translations = {}
        for item in data:
            translations[item["원문"]] = item["최종번역문"]

        return translations

    def get_dataset_train(self):
        return self._dataset_train

    def get_dataset_val(self):
        return self._dataset_val
