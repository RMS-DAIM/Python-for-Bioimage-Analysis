import os

import numpy as np
import torch
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms, utils


class CellsDataset(Dataset):
    # a very simple dataset

    def __init__(self, root_dir, transform=None, return_filenames=False):
        self.root = root_dir
        self.transform = transform
        self.return_filenames = return_filenames
        self.files = [os.path.join(self.root,filename) for filename in os.listdir(self.root)]
        self.files = [path for path in self.files
                      if os.path.isfile(path) and os.path.splitext(path)[1]=='.png']

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        path = self.files[idx]
        sample = Image.open(path)

        if self.transform:
            sample = self.transform(sample)

        if self.return_filenames:
            return sample, path
        else:
            return sample
