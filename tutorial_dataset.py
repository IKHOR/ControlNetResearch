import json
import cv2
import numpy as np

from torch.utils.data import Dataset


class MyDataset(Dataset):
    def __init__(self):
        self.data = []
        with open('./data/fill50k/prompt.json', 'rt') as f:
            for line in f:
                self.data.append(json.loads(line))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]

        source_filename = item['source']
        target_filename = item['target']
        prompt = item['prompt']

        source = cv2.imread('./data/fill50k/' + source_filename)
        target = cv2.imread('./data/fill50k/' + target_filename)

        if source is None:
            print(f"Failed to load source image at index {idx} with filename {source_filename}")
        else:
            # Do not forget that OpenCV read images in BGR order.
            source = cv2.cvtColor(source, cv2.COLOR_BGR2RGB)

        if target is None:
            print(f"Failed to load target image at index {idx} with filename {target_filename}")
        else:
            target = cv2.cvtColor(target, cv2.COLOR_BGR2RGB)


        # Normalize source images to [0, 1].
        source = source.astype(np.float32) / 255.0

        # Normalize target images to [-1, 1].
        target = (target.astype(np.float32) / 127.5) - 1.0

        return dict(jpg=target, txt=prompt, hint=source)

