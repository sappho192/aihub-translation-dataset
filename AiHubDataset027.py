from AiHubDatasetBase import AiHubDatasetBase
import os


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
        # TODO: Implement this method
        return []

    def make_val_dataset(self):
        # TODO: Implement this method
        return []
