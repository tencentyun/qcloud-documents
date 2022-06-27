# python3 /opt/ml/code/fully_connected_feed.py  --train_dir /opt/ml/input/data  --max_steps 100000 --batch_size 1000  --log_dir /opt/ml/output/summary  --ckpt_dir /opt/ml/output --model_dir /opt/ml/model

# train_dir 训练样本路径。在该路径下应该有t10k-images-idx3-ubyte.gz/t10k-labels-idx1-ubyte.gz/train-images-idx3-ubyte.gz/train-labels-idx1-ubyte.gz 4个文件

# max_steps 最长训练步数

# batch_size  batchsize

# log_dir  tensorboard文件输出路径

# ckpt_dir  checkpoint输出路径

# model_dir 最终模型文件输出路径