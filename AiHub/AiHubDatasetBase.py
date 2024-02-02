class AiHubDatasetBase:
    def __init__(self, dataset_name, dataset_root, dataset_train_root, dataset_val_root):
        self._dataset_name = dataset_name
        self._dataset_root = dataset_root
        self._dataset_train_root = dataset_train_root
        self._dataset_val_root = dataset_val_root

        self._dataset_train = []
        self._dataset_val = []

    def get_dataset_name(self):
        return self._dataset_name

    def get_dataset_root(self):
        return self._dataset_root

    def get_dataset_train_root(self):
        return self._dataset_train_root

    def get_dataset_val_root(self):
        return self._dataset_val_root

    def get_dataset_train(self):
        return self._dataset_train

    def get_dataset_val(self):
        return self._dataset_val

    def make_dataset(self):
        pass

