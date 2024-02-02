import os
import json

from AiHub.AiHubDatasetBase import AiHubDatasetBase


class AiHubDatasetKoJaTr(AiHubDatasetBase):
    def __init__(self, dataset_name, dataset_root):
        dataset_train_root = os.path.join(dataset_root, "Training", "[라벨]ko2ja_culture_training_json")
        dataset_val_root = os.path.join(dataset_root, "Validation", "[라벨]ko2ja_culture_validation_json")
        super().__init__(dataset_name, dataset_root, dataset_train_root, dataset_val_root)
        self.make_dataset()

    def get_dataset_train(self):
        return self._dataset_train

    def get_dataset_val(self):
        return self._dataset_val

    def make_dataset(self):
        self._dataset_train = self.make_train_dataset()
        self._dataset_val = self.make_val_dataset()

    def make_train_dataset(self):
        result = []

        # get all json files path in dataset_train_root
        json_files = [f for f in os.listdir(self._dataset_train_root) if f.endswith('.json')]
        # read json files using read_json method, and append to result list
        for json_file in json_files:
            json_path = os.path.join(self._dataset_train_root, json_file)
            result.append(self.read_json(json_path))

        return result

    def make_val_dataset(self):
        result = []

        # get all json files path in dataset_val_root
        json_files = [f for f in os.listdir(self._dataset_val_root) if f.endswith('.json')]
        # read json files using read_json method, and append to result list
        for json_file in json_files:
            json_path = os.path.join(self._dataset_val_root, json_file)
            result.append(self.read_json(json_path))

        return result

    def read_json(self, json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            sentences = json.load(f)

        translations = []
        for sentence in sentences:
            translations.append((sentence["일본어"], sentence["한국어"]))
        return translations
