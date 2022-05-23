#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import torchvision
import torch
import argparse
from torchvision import datasets, transforms
from torch.autograd import Variable
import torch.distributed as dist
import os
import torch.backends.cudnn as cudnn
import torch.multiprocessing as mp
from torch.nn.parallel import DistributedDataParallel as DDP
import torch.nn.functional as F
import math
from light import light, light_init


parser = argparse.ArgumentParser(description='PyTorch DDP mnist Example.',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--train-dir', default='./data', help='path to training data')
parser.add_argument('--checkpoint-dir', default='./checkpoints', help='checkpoint file format')
parser.add_argument('--batch-size', type=int, default=256, help='input batch size for training')
parser.add_argument('--epochs', type=int, default=2, help='number of epochs to train')
parser.add_argument('--base-lr', type=float, default=0.0125, help='learning rate for a single GPU')
parser.add_argument('--no-cuda', action='store_true', default=False, help='disables CUDA training')
parser.add_argument('--seed', type=int, default=42, help='random seed')
parser.add_argument('--local_rank', default=0, type=int, help='node rank for distributed training')


class Model(torch.nn.Module):
    
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = torch.nn.Sequential(torch.nn.Conv2d(1,64,kernel_size=3,stride=1,padding=1),
                                         torch.nn.ReLU(),
                                         torch.nn.Conv2d(64,128,kernel_size=3,stride=1,padding=1),
                                         torch.nn.ReLU(),
                                         torch.nn.MaxPool2d(stride=2,kernel_size=2))
        self.dense = torch.nn.Sequential(torch.nn.Linear(14*14*128,1024),
                                         torch.nn.ReLU(),
                                         torch.nn.Dropout(p=0.5),
                                         torch.nn.Linear(1024, 10))
    def forward(self, x):
        x = self.conv1(x)
        x = x.view(-1, 14*14*128)
        x = self.dense(x)
        return x

def accuracy(output, target):
    # get the index of the max log-probability
    pred = output.max(1, keepdim=True)[1]
    return pred.eq(target.view_as(pred)).cpu().float().mean()

@light_init(params={"training_framework": "pytorch_ddp"})
def main():
    args = parser.parse_args()
    args.cuda = not args.no_cuda and torch.cuda.is_available()
    torch.manual_seed(args.seed)

    if args.cuda:
        torch.cuda.set_device(args.local_rank)
        torch.cuda.manual_seed(args.seed)
        # dist.init_process_group('nccl')
    # else:
    #     dist.init_process_group('mpi')
    cudnn.benchmark = True
    torch.set_num_threads(4)

    if dist.get_rank() == 0 and not os.path.exists(args.checkpoint_dir):
        os.makedirs(args.checkpoint_dir)

    # dataset
    kwargs = {'num_workers': 4, 'pin_memory': True} if args.cuda else {}
    if (kwargs.get('num_workers', 0) > 0 and hasattr(mp, '_supports_context') and
            mp._supports_context and 'forkserver' in mp.get_all_start_methods()):
        kwargs['multiprocessing_context'] = 'forkserver'
    transform = transforms.Compose([transforms.ToTensor(), 
                                transforms.Normalize(mean=[0.5],std=[0.5])])
    dataset = datasets.MNIST(root = args.train_dir,
                            transform=transform,
                            train = True,
                            download = True)
    sampler = torch.utils.data.distributed.DistributedSampler(dataset, num_replicas=dist.get_world_size(), rank=dist.get_rank())
    loader = torch.utils.data.DataLoader(
                dataset, batch_size=args.batch_size,
                sampler=sampler, **kwargs)

    model = Model()
    optimizer = torch.optim.Adam(model.parameters())
    if args.cuda:
        model.cuda()
    if args.cuda:
        model = DDP(model, device_ids=[args.local_rank], output_device=args.local_rank, find_unused_parameters=True)
    else:
        model = DDP(model)

    # train
    for epoch in range(args.epochs):
        model.train()
        sampler.set_epoch(epoch)
        loss = 0.0
        acc = 0.0
        for ind, data in enumerate(loader):
            x, y = data
            x, y = Variable(x), Variable(y)
            if args.cuda:
                x, y = x.cuda(), y.cuda()
            optimizer.zero_grad()
            output = model(x)
            acc = accuracy(output, y)
            loss = F.cross_entropy(output, y)
            loss.div_(math.ceil(float(len(data)) / args.batch_size))
            loss.backward()
            optimizer.step()
            print(f"Train Epoch: {epoch}, batch: {ind}, loss: {loss}, accuracy: {100. * acc}")

    if dist.get_rank() == 0:
        torch.save(model.state_dict(), os.path.join(args.checkpoint_dir, "model_parameter.pkl"))

if __name__ == "__main__":
    main()