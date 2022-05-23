epoch=$1
if [[ $epoch == "" ]]; then
    epoch=1
fi
python3 -m torch.distributed.launch \
    --nnodes=$NODE_NUM \
    --node_rank=$INDEX \
    --nproc_per_node=$GPU_NUM_PER_NODE \
    --master_addr=$CHIEF_IP \
    --master_port=23457 \
    mnist_ddp.py --train-dir /opt/ml/input/data \
                 --checkpoint-dir /opt/ml/model \
                 --no-cuda \
                 --epochs $epoch