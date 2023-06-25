import sys
import torch
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(name)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class DummyCNN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.main = torch.nn.Sequential(
            
            torch.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=(3, 3), padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d((2, 2)),
            
            torch.nn.Conv2d(in_channels=3, out_channels=2, kernel_size=(3, 3), padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d((2, 2)),
            
            torch.nn.Flatten(),
            torch.nn.Linear(625, 1)
        )

    def forward(self, x):
        out = self.main(x)
        return out

def random_inference():
    DEVICE = torch.device(
        'cuda' if torch.cuda.is_available()
        else 'mps' if torch.backends.mps.is_available()
        else 'cpu'
    )
    logger.debug(f'Using device: {DEVICE}')
    model = DummyCNN().eval().to(DEVICE)
    # 100px by 100px by 3 channels 
    random_tensor = (torch.rand(3, 100, 100) * 225).to(DEVICE)
    return model(random_tensor)

if __name__ == '__main__':
    result = random_inference()
    logger.debug(f'Inference Result = {result}')