import json
import csv

# accepts varidic number of datasets and merges them into one
def merge_aihub_datasets(*datasets, to_single_list: bool = True):
    merged = []
    for dataset in datasets:
        merged += dataset

    if to_single_list:
        merged = [item for sublist in merged for item in sublist]

    return merged


# Save dataset to JSON file.
# The tuple elements in the dataset should be saved as dictionary with keys "sourceString" and "targetString"
def save_dataset_to_json(dataset, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump([{"sourceString": src, "targetString": tgt} for src, tgt in dataset], f, ensure_ascii=False, indent=4)


# Save dataset to JSONLine file.
# The tuple elements in the dataset should be saved as dictionary with keys "sourceString" and "targetString"
def save_dataset_to_jsonl(dataset, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        for src, tgt in dataset:
            json.dump({"sourceString": src, "targetString": tgt}, f, ensure_ascii=False)
            f.write('\n')


# Save dataset to CSV file.
# The tuple elements in the dataset should be saved as dictionary with keys "sourceString" and "targetString"
# Use csv writer
def save_dataset_to_csv(dataset, file_path):
    with open(file_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["sourceString", "targetString"])
        for src, tgt in dataset:
            writer.writerow([src, tgt])
