steps=$1
if [[ "$steps" == "" ]]; then
    steps=10000
fi
batchsize=$2
if [[ "$batchsize" == "" ]]; then
    batchsize="128"
fi

set -x
mpirun --allow-run-as-root -np $GPU_NUM -H $NODE_IP_SLOT_LIST python3 train.py --steps $steps --batch-size $batchsize
