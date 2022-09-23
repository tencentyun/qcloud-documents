# python3 -m torch.distributed.launch --nnodes=$NODE_NUM --node_rank=$INDEX --nproc_per_node=$GPU_NUM_PER_NODE --master_addr=$CHIEF_IP --master_port=23457 mnist_ddp.py --train_dir /opt/ml/input/data -ckpt_dir /opt/ml/output --model_dir /opt/ml/model --epochs 5

# train_dir  数据路径。在该路径的./MNIST/raw路径下需要有t10k-images-idx3-ubyte.gz/t10k-labels-idx1-ubyte.gz/train-images-idx3-ubyte.gz/train-labels-idx1-ubyte.gz 4个文件

# ckpt_dir  checkpoint输出路径

# model_dir 最终模型文件输出路径

# epochs 训练的epoch数
