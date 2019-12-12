import torch
import torch.nn as nn

class Convnet(nn.Module):
    """
    A custom convnet for convolving 1080x1080 fluorescence micrograph images.
    """

    def __init__(self):
        super(Convnet,self).__init__()
        self.main = nn.Sequential(
            nn.Conv2d(3,64,7,stride=3,padding=0),
            nn.LeakyReLU(0.2,inplace=False),
            nn.Conv2d(64,96,3,stride=2,padding=0),
            nn.LeakyReLU(0.2,inplace=False),
            nn.Conv2d(96,128,3,stride=2,padding=0),
            nn.LeakyReLU(0.2,inplace=False),
            nn.Conv2d(128,192,3,stride=2,padding=0),
            nn.LeakyReLU(0.2,inplace=False),
            nn.Conv2d(192,256,3,stride=2,padding=0),
            nn.LeakyReLU(0.2,inplace=False),
            nn.Conv2d(256,256,3,stride=2,padding=0),
            nn.LeakyReLU(0.2,inplace=False),
            nn.Conv2d(256,1,1,stride=1,padding=0)
        )

    def forward(self, x):
        # x: B x 2 x 1024 x 1024
        return self.main(x) # B x 1 x 9 x 9
