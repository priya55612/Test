import os
import argparse

import numpy as np
import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
from torchvision import datasets, transforms, models
from torch.autograd import Variable
from torchvision.utils import save_image


import argparse
parser = argparse.ArgumentParser()


parser.add_argument("--model", default = "mobilenet_v2", type = str)
 
parser.add_argument("--test_data", default = "/mount_data/test_data", type = str)
parser.add_argument("--results_dir", default = "/mount_data/test_results", type = str)
parser.add_argument("--pth", default = "fingermodel_bal_mobilenet_v2_0.0001_50.pth", type = str)

args = parser.parse_args()


device = torch.device("cuda" if torch.cuda.is_available() 
                                  else "cpu")


model = torch.hub.load('pytorch/vision:v0.5.0', args.model, pretrained=False, num_classes=2)
model.to(device)

checkpoint = torch.load(args.pth, map_location = device)
model.load_state_dict(checkpoint)

model.eval()
#print(model)


test_data_dir = args.test_data
test_transforms = transforms.Compose([transforms.Resize([224,224]),transforms.ToTensor(),transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])
data = datasets.ImageFolder(test_data_dir, transform = test_transforms)

# classes = data.classes

# print(classes)


loader = torch.utils.data.DataLoader(data, batch_size=1)

def predict_image(image):
    image_tensor = image
    image_tensor = image_tensor.to(device)
    output = model(image_tensor)
    index = output.data.cpu().numpy().argmax(axis=1)
    return index




os.makedirs(args.results_dir,exist_ok = True)
labels_map = {0: 'distal', 1: 'non_distal'}

for ii,(images,labels) in enumerate(loader):
    index = predict_image(images)
    print("The predicted class is ",labels_map[index[0]])
    save_image(images, os.path.join(args.results_dir,'image_'+str(ii)+'_'+str(labels_map[index[0]])+'.png'))
       
