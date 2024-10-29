import torch
import ipdb
from model.resnet import resnet18

model = resnet18(pretrained=True)

# step1 arch changes
# quantstub 

# step2 fuse model
# name base, graph base (later)

modules_to_fuse = model.modules_to_fuse()
ipdb.set_trace()
model = torch.ao.quantization.fuse_modules_qat(model, modules_to_fuse)



