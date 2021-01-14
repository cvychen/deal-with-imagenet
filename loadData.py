import torchvision.datasets as datasets
import torchvision.transforms as transforms

def loadData(path='./imagenet'):

    #set the path of dataset
    train_path = os.path.join(path + 'train')
    val_path = os.path.join(path + 'val')

    #set transform method, the default img size of imagenet is 224
    normalizer = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    train_transform = transforms.Compose([
        # transforms.Resize(300),
        transforms.RandomResizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        normalizer
    ])
    valid_transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        normalizer
    ])

    #import train\val dataset
    train_data = datasets.ImageFolder(root=train_path, transform=train_transform)
    valid_data = datasets.ImageFolder(root=val_path, transform=valid_transform)

    #load dataset into Dataloader
    train_queue = torch.utils.data.DataLoader(
            train_data, batch_size=args.batch_size, shuffle=True, pin_memory=True, num_workers=args.num_workers)

    valid_queue = torch.utils.data.DataLoader(
        valid_data, batch_size=200, shuffle=False, pin_memory=True, num_workers=args.num_workers)

    print(len(train_data)) #1151273
    print(len(valid_data)) #50000

if __name__ == "__main__":
    loadData()