# -*- coding: utf-8 -*-

'''
使用合成数据集的启动命令:
horovodrun -np 2 python3 light_tensorflow2_benchmark.py

使用ImageNet数据集的启动命令:
horovodrun -np 2 python3 light_tensorflow2_benchmark.py --data-path '/jizhicfs/public_dataset/imagenet'
'''


from __future__ import absolute_import, division, print_function
import argparse
import os
import numpy as np
import timeit
import tensorflow as tf
from tensorflow.keras import applications
from horovod.tensorflow.tensor_fusion import auto_fusion_allreduce
## 修改点1：导入Light程序包
from light import light, light_init


# Benchmark settings
parser = argparse.ArgumentParser(description='TensorFlow Synthetic / ImageNet Benchmark',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--fp16-allreduce', action='store_true', default=False,
                    help='use fp16 compression during allreduce')

parser.add_argument('--model', type=str, default='ResNet50',
                    help='model to benchmark')
parser.add_argument('--batch-size', type=int, default=32,
                    help='input batch size')
parser.add_argument('--num-warmup-batches', type=int, default=10,
                    help='number of warm-up batches that don\'t count towards benchmark')
parser.add_argument('--num-batches-per-iter', type=int, default=10,
                    help='number of batches per benchmark iteration')
parser.add_argument('--num-iters', type=int, default=20,
                    help='number of benchmark iterations')
parser.add_argument('--no-cuda', action='store_true', default=False,
                    help='disables CUDA training')
parser.add_argument('--auto-fusion-threshold', type=int, default=32*1024*1024, help='')
parser.add_argument('--data-path', default=None, help='train data file path')
args = parser.parse_args()

## 修改点2：填写加速信息字段
params = {
    "training_framework": "tensorflow",
    "enable_optimizations": True,
    "application_scenario": "TF-CV"
}

## 修改点3：给主函数添加Light初始化装饰器
@light_init(params=params)
def main():
    args.cuda = not args.no_cuda
    
    # light: pin GPU to be used to process local rank (one GPU per process)
    if args.cuda:
        gpus = tf.config.experimental.list_physical_devices('GPU')
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        if gpus:
            ## 修改点4：获取当前机器节点上，Light进程的本地编号rank
            tf.config.experimental.set_visible_devices(gpus[light.cc.local_rank()], 'GPU')
    else:
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
    
    # Set up standard model.
    model = getattr(applications, args.model)(weights=None)
    opt = tf.optimizers.SGD(0.01)
    
    def get_synthetic_dataset(height=224, width=224, num_channels=3, data_format="NHWC", num_classes=1000, dtype=tf.float32):
        if data_format == "NHWC":
            input_shape = [args.batch_size, height, width, num_channels]
        else:
            input_shape = [args.batch_size, num_channels, height, width]
    
        inputs = tf.random.truncated_normal(input_shape, dtype=dtype, mean=127, stddev=60, name='synthetic_inputs')
        labels = tf.random.uniform([args.batch_size], minval=0, maxval=num_classes - 1, dtype=tf.int32, name='synthetic_labels')
    
        ds = tf.data.Dataset.from_tensors((inputs, labels))
        ds = ds.repeat()
        ds = ds.prefetch(buffer_size=6)
        ds = ds.apply(tf.data.experimental.prefetch_to_device("/gpu:0"))
        return ds
    def get_dataset(train=True):
        from dataset import parse_and_preprocess

        filename_list =  [os.path.join(args.data_path, 'train-%05d-of-01024.tfrecord' % i) for i in range(1024)]
        
        ## 修改点5：使用Light数据分片
        file_list = light.io.files_shard(filename_list, size=light.cc.size(), rank=light.cc.rank())
        
        if len(file_list) <= 0:
            raise ValueError('Found no files')
        ds = tf.data.TFRecordDataset.list_files(file_list)
        ds = ds.apply(
            tf.data.experimental.parallel_interleave(tf.data.TFRecordDataset,
                                               cycle_length=10))
        counter = tf.data.Dataset.range(args.batch_size)
        counter = counter.repeat()
        ds = tf.data.Dataset.zip((ds, counter))
        
        ds = ds.prefetch(buffer_size=args.batch_size)
        if train:
            ds = ds.shuffle(buffer_size=args.batch_size * 10)
        ds = ds.repeat()
        ds = ds.apply(
            tf.data.experimental.map_and_batch(
                map_func=parse_and_preprocess,
                batch_size=args.batch_size,
                num_parallel_batches=1))
        ds = ds.prefetch(buffer_size=1) 
        return ds

    if args.data_path is None:
        print('Use the synthetic dataset.')
        dataset = get_synthetic_dataset()
    else:
        print('Use imagenet dataset.')
        dataset = get_dataset()
    
    ## 修改点6：创建Light iterator，为dataset初始化创建迭代器
    train_data = light.io.get_iterator(dataset)
    
    @tf.function
    def benchmark_step(data, first_batch):
        ## 修改点7：指定Light梯度压缩数据类型fp16
        compression = light.cc.Compression.fp16 if args.fp16_allreduce else light.cc.Compression.none
    
        with tf.GradientTape() as tape:
            probs = model(data[0], training=True)
            loss = tf.losses.sparse_categorical_crossentropy(data[1], probs)
    
        # light: add light Distributed GradientTape.
        ## 修改点8：将gradient tape扩展，让其具有分布式能力
        tape = light.cc.get_distributed_gradient_tape(tape, compression=compression)
    
        gradients = tape.gradient(loss, model.trainable_variables)
        # gradvars = auto_fusion_allreduce(gradients, auto_fusion_threshold=args.auto_fusion_threshold)
        # opt.apply_gradients(zip(gradvars, model.trainable_variables))
        opt.apply_gradients(zip(gradients, model.trainable_variables))
    
        ## 修改点9：调用Light广播变量方法
        # This is necessary to ensure consistent initialization of all workers when
        # training is started with random weights or restored from a checkpoint.
        #
        # Note: broadcast should be done after the first gradient step to ensure optimizer
        # initialization.
        if first_batch:
            light.cc.broadcast_variables(model.variables, root_rank=0)
            light.cc.broadcast_variables(opt.variables(), root_rank=0)
    
    
    def log(s, nl=True):
        ## 修改点10：获取当前Light进程在分布式训练中的rank
        if light.cc.rank() != 0:
            return
        print(s, end='\n' if nl else '')
    
    
    log('Model: %s' % args.model)
    log('Batch size: %d' % args.batch_size)
    device = 'GPU' if args.cuda else 'CPU'
    log('Number of %ss: %d' % (device, light.cc.size()))
    
    
    with tf.device(device):
        # Warm-up
        #log('Running warmup...')
        #benchmark_step(first_batch=True)
        #timeit.timeit(lambda: benchmark_step(first_batch=False),
        #              number=args.num_warmup_batches)
    
        # Benchmark
        log('Running benchmark...')
        img_secs = []
        for step, sample in enumerate(train_data):
            time = timeit.timeit(lambda: benchmark_step(sample, first_batch=False),
                                 number=args.num_batches_per_iter)
            img_sec = args.batch_size * args.num_batches_per_iter / time
            log('Iter #%d: %.1f img/sec per %s' % (step, img_sec, device))
            img_secs.append(img_sec)
            if step >= args.num_iters:
                break
    
        # Results
        img_sec_mean = np.mean(img_secs)
        img_sec_conf = 1.96 * np.std(img_secs)
        log('Img/sec per %s: %.1f +-%.1f' % (device, img_sec_mean, img_sec_conf))
        log('Total img/sec on %d %s(s): %.1f +-%.1f' %
            (light.cc.size(), device, light.cc.size() * img_sec_mean, light.cc.size() * img_sec_conf))


# please surround your entry function with
#
#   if __name__ == "__main__":
#
# otherwise, some multiprocess issues may be triggered.
if __name__ == "__main__":
      main()
