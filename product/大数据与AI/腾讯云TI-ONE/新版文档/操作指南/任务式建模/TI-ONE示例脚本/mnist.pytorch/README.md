# python3 train.py --epochs 5 --input_data_dir /opt/ml/input/data --log_dir /opt/ml/output/summary  --ckpt_dir /opt/ml/output --model_dir /opt/ml/model

# input_data_dir  数据路径。在该路径的./MNIST/raw路径下需要有t10k-images-idx3-ubyte.gz/t10k-labels-idx1-ubyte.gz/train-images-idx3-ubyte.gz/train-labels-idx1-ubyte.gz 4个文件

# epochs 训练epoch数

# batch_size  batchsize

# log_dir  tensorboard文件输出路径

# ckpt_dir  checkpoint输出路径

# model_dir 最终模型文件输出路径
