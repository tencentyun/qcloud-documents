# -*- coding: utf-8 -*-

'''
使用合成数据集的启动命令:
horovodrun -np 2 python3 light_pytorch_benchmark.py

使用ImageNet数据集的启动命令:
horovodrun -np 2 python3 light_pytorch_benchmark.py --train-dir '/root/imagenet/train'
'''

import torch
import argparse
import torch.backends.cudnn as cudnn
import torch.multiprocessing as mp
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data.distributed
from torchvision import datasets, transforms, models
import os
import math
from tqdm import tqdm

import timeit
import numpy as np

## 修改点1：导入Light程序包
from light import light, light_init


parser = argparse.ArgumentParser(description='PyTorch ImageNet/Synthetic Example',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--train-dir', default=None, help='path to training data')
parser.add_argument('--batch-size', type=int, default=256, help='input batch size for training')
parser.add_argument('--epochs', type=int, default=20, help='number of epochs to train')
parser.add_argument('--base-lr', type=float, default=0.0125, help='learning rate for a single GPU')
parser.add_argument('--momentum', type=float, default=0.9, help='SGD momentum')
parser.add_argument('--wd', type=float, default=0.00005, help='weight decay')
parser.add_argument('--no-cuda', action='store_true', default=False, help='disables CUDA training')
parser.add_argument('--seed', type=int, default=42, help='random seed')

parser.add_argument('--num-warmup-batches', type=int, default=10,
                    help='number of warm-up batches that don\'t count towards benchmark')
parser.add_argument('--num-batches-per-epoch', type=int, default=10,
                    help='number of batches per benchmark epoch.')

parser.add_argument('--use-adasum', action='store_true', default=False,
                    help='use adasum algorithm to do reduction')
parser.add_argument('--fp16-allreduce', action='store_true', default=False,
                    help='use fp16 compression during allreduce')
parser.add_argument('--batches-per-allreduce', type=int, default=1,
                    help='number of batches processed locally before executing allreduce '
                         'across workers; it multiplies total batch size.')
parser.add_argument('--warmup-epochs', type=float, default=5,
                    help='number of warmup epochs')
args = parser.parse_args()
args.cuda = not args.no_cuda and torch.cuda.is_available()


def log(s, nl=True):
    ## 修改点2：获取当前Light进程在分布式训练中的rank
    if light.cc.rank() == 0:
        print(s, end='\n' if nl else '')


class Metric(object):
    def __init__(self, name):
        self.name = name
        self.sum = torch.tensor(0.)
        self.n = torch.tensor(0.)

    def update(self, val):
        ## 修改点3：对指定Tensor进行allreduce操作
        self.sum += light.cc.allreduce(val.detach().cpu(), name=self.name)
        self.n += 1

    @property
    def avg(self):
        return self.sum / self.n

# Notice: using `lr = base_lr * light.cc.size()` from the very beginning leads to worse final
# accuracy. Scale the learning rate `lr = base_lr` ---> `lr = base_lr * light.cc.size()` during
# the first five epochs. After the warmup reduce learning rate by 10 on the 30th, 60th and 80th epochs.
def adjust_learning_rate(train_loader, optimizer, epoch, batch_idx):
    if epoch < args.warmup_epochs:
        epoch += float(batch_idx + 1) / len(train_loader)
        ## 修改点4：获取分布式训练程序中Light进程数量
        lr_adj = 1. / light.cc.size() * (epoch * (light.cc.size() - 1) / args.warmup_epochs + 1)
    elif epoch < 30:
        lr_adj = 1.
    elif epoch < 60:
        lr_adj = 1e-1
    elif epoch < 80:
        lr_adj = 1e-2
    else:
        lr_adj = 1e-3
    for param_group in optimizer.param_groups:
        param_group['lr'] = args.base_lr * light.cc.size() * args.batches_per_allreduce * lr_adj


def train_synthetic(model, optimizer, data, target):
    def benchmark_step():
        optimizer.zero_grad()
        output = model(data)
        loss = F.cross_entropy(output, target)
        loss.backward()
        optimizer.step()
    device = 'GPU' if args.cuda else 'CPU'
    # Warm-up
    log('Running warmup...')
    timeit.timeit(benchmark_step, number=args.num_warmup_batches)
        
    log('Running benchmark...')
    img_secs = []
    for x in range(args.epochs):
        time = timeit.timeit(benchmark_step, number=args.num_batches_per_epoch)
        img_sec = args.batch_size * args.num_batches_per_epoch / time
        log('Epoch #%d: %.1f img/sec per %s' % (x, img_sec, device))
        img_secs.append(img_sec)
        
    # Results
    img_sec_mean = np.mean(img_secs)
    img_sec_conf = 1.96 * np.std(img_secs)
    log('Img/sec per %s: %.1f +-%.1f' % (device, img_sec_mean, img_sec_conf))
    log('Total img/sec on %d %s(s): %.1f +-%.1f' % (light.cc.size(), device, 
                       light.cc.size() * img_sec_mean, light.cc.size() * img_sec_conf))


def train_synthetic_(model, optimizer, data, target):
    log('Running benchmark...')
    train_loss = Metric('train_loss')
    train_accuracy = Metric('train_accuracy')

    for epoch in range(args.epochs):
        with tqdm(total=args.num_batches_per_epoch,
                  desc='Train Epoch #{}'.format(epoch + 1),
                  disable=not (1 if light.cc.rank() == 0 else 0)) as t:
            for i in range(args.num_batches_per_epoch):
                optimizer.zero_grad()
                output = model(data)
                loss = F.cross_entropy(output, target)
                train_loss.update(loss)
                # Average gradients among sub-batches
                loss.div_(math.ceil(float(len(data)) / args.batch_size))
                loss.backward()

                # Gradient is applied across all ranks
                optimizer.step()
                t.set_postfix({'loss': train_loss.avg.item()})
                t.update(1)
        
def train_imagenet(model, optimizer, train_loader, train_sampler):
    def accuracy(output, target):
        # get the index of the max log-probability
        pred = output.max(1, keepdim=True)[1]
        return pred.eq(target.view_as(pred)).cpu().float().mean()
    
    for epoch in range(0, args.epochs):
        model.train()
        train_sampler.set_epoch(epoch)
        train_loss = Metric('train_loss')
        train_accuracy = Metric('train_accuracy')
        ## 修改点5：获取当前Light进程在分布式训练中的rank
        with tqdm(total=len(train_loader),
                desc='Train Epoch #{}'.format(epoch + 1),
                disable=not (1 if light.cc.rank() == 0 else 0)) as t:
            for batch_idx, (data, target) in enumerate(train_loader):
                adjust_learning_rate(train_loader, optimizer, epoch, batch_idx)
                if args.cuda:
                    data, target = data.cuda(), target.cuda()
                optimizer.zero_grad()
                # Split data into sub-batches of size batch_size
                for i in range(0, len(data), args.batch_size):
                    data_batch = data[i:i + args.batch_size]
                    target_batch = target[i:i + args.batch_size]
                    output = model(data_batch)
                    train_accuracy.update(accuracy(output, target_batch))
                    loss = F.cross_entropy(output, target_batch)
                    train_loss.update(loss)
                    # Average gradients among sub-batches
                    loss.div_(math.ceil(float(len(data)) / args.batch_size))
                    loss.backward()
                # Gradient is applied across all ranks
                optimizer.step()
                t.set_postfix({'loss': train_loss.avg.item(),
                               'accuracy': 100. * train_accuracy.avg.item()})
                t.update(1)


## 修改点6：填写加速信息字段
params = {
    "training_framework": "pytorch",
    "enable_optimizations": True,
    "application_scenario": "Torch-CV"
}

## 修改点7：给主函数添加Light初始化装饰器
@light_init(params=params)
def main():
    # base information.
    log('Model: %s' % 'ResNet50')
    log('Batch size: %d' % args.batch_size)
    device = 'GPU' if args.cuda else 'CPU'
    log('Number of %ss: %d' % (device, light.cc.size()))
    
    torch.manual_seed(args.seed)
    if args.cuda:
        # light: pin GPU to local rank.
        torch.cuda.set_device(light.cc.local_rank())
        torch.cuda.manual_seed(args.seed)
    cudnn.benchmark = True
    
    #light: By default, Adasum doesn't need scaling up learning rate.
    lr_scaler = args.batches_per_allreduce * light.cc.size() if not args.use_adasum else 1

    # Set up standard ResNet-50 model. & Move model to GPU.
    model = models.resnet50()
    if args.cuda:
        model.cuda()
        if args.use_adasum and light.cc.nccl_built():
            ## 修改点8：获取当前机器节点上Light进程数量
            lr_scaler = args.batches_per_allreduce * light.cc.local_size()
    
    optimizer = optim.SGD(model.parameters(), lr=args.base_lr * lr_scaler, 
                          momentum=args.momentum, weight_decay=args.wd)
    
    ## 修改点9：指定Light梯度压缩数据类型fp16
    compression = light.cc.Compression.fp16 if args.fp16_allreduce else light.cc.Compression.none
    ## 修改点10：用Light分布式优化器包装原有优化器，让其具有分布式能力
    optimizer = light.cc.get_distributed_optimizer(optimizer,
                                         named_parameters=model.named_parameters(),
                                         compression=compression,
                                         op=light.cc.Adasum if args.use_adasum else light.cc.Average)
    ## 修改点11：调用Light广播变量方法
    light.cc.broadcast_variable(model.state_dict(), root_rank=0)
    light.cc.broadcast_variable(optimizer, root_rank=0)

    if args.train_dir is not None:
        log('Use imagenet dataset.')
        # limit # of CPU threads to be used per worker.
        torch.set_num_threads(4)

        kwargs = {'num_workers': 4, 'pin_memory': True} if args.cuda else {}
        # When supported, use 'forkserver' to spawn dataloader workers instead of 'fork' to prevent
        # issues with Infiniband implementations that are not fork-safe
        if (kwargs.get('num_workers', 0) > 0 and hasattr(mp, '_supports_context') and
            mp._supports_context and 'forkserver' in mp.get_all_start_methods()):
            kwargs['multiprocessing_context'] = 'forkserver'

        train_dataset = datasets.ImageFolder(args.train_dir,
                        transform=transforms.Compose([transforms.RandomResizedCrop(224),
                        transforms.RandomHorizontalFlip(), transforms.ToTensor(),
                        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
                        ]))
        
        ## 修改点12：用分布式Sampler在各个机器节点上分配训练数据，需要手动指定`num_replicas=light.cc.size()` and `rank=light.cc.rank()`
        train_sampler = torch.utils.data.distributed.DistributedSampler(
                        train_dataset, num_replicas=light.cc.size(), rank=light.cc.rank())

        train_loader = light.io.get_data_loader(train_dataset,
                        batch_size=args.batch_size * args.batches_per_allreduce,
                        sampler=train_sampler, **kwargs)
        train_imagenet(model, optimizer, train_loader, train_sampler)
    else:
        log('Use synthetic dataset.')
        data = torch.randn(args.batch_size, 3, 224, 224)
        target = torch.LongTensor(args.batch_size).random_() % 1000
        if args.cuda:
            data, target = data.cuda(), target.cuda()
        train_synthetic_(model, optimizer, data, target)


# please surround your entry function with
#
#   if __name__ == "__main__":
#
# otherwise, some multiprocess issues may be triggered.
if __name__ == '__main__':
    main()

