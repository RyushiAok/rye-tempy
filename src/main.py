import torch
import utils

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

print(utils.add(1, 2))
