import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder

def load_dataset(data_path):
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    dataset = ImageFolder(root=data_path, transform=transform)
    return dataset
