import os
from tqdm import tqdm
import json


def load_risks_dicts():
    data_folder = './data/staging/risks'
    risk_dicts = []
    skipped = []

    if os.path.exists(data_folder) and os.path.isdir(data_folder):
        for file_name in tqdm(os.listdir(data_folder)):
            with open(os.path.join(data_folder, file_name)) as fp:
                try:
                    content = fp.read()
                    data = json.loads(json.loads(content))
                    data['symbol_name'] = file_name  # Add the file name field
                    risk_dicts.append(data)
                except Exception as e:
                    skipped.append(file_name)
                    print(file_name)
        if skipped:
            print(f"Skipped {len(skipped)}")
            print(f"Skipped examples: {skipped[:5]}")
        return risk_dicts
