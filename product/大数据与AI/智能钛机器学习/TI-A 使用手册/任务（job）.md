## 定义

Job 代表一个训练任务，他定义了训练该如何在腾讯云上执行。Job 有如下参数：

| 名称                   | 类型       | 描述                                       |
| :------------------- | :------- | :--------------------------------------- |
| name               |`string`         | Required, job 的名字, cluster 唯一              |
| createTime         |`string`      |  任务创建时间, RFC3339              |
| startTime          |`string`        |  任务开始时间, RFC3339|
| endTime            |`bool`         |  任务结束时间, RFC3339|
| state              |`string`        |  任务状态，状态为如下之一：Created，Running，Succeeded，Failed|
| message            |`string`       |  任务(错误)信息|
| masterType         |`string`  | Optional, 参考下面的[机器类型描述](#机器类型描述)         |
| workerType         |`string`  | Optional, 参考下面的[机器类型描述](#机器类型描述)         |
| parameterServerType|`string`  | Optional, 参考下面的[机器类型描述](#机器类型描述)  |
| workerCount        |`int32`              | Optional, worker机器数量|
| parameterServerCount |`int32`            | Optional, parameterServer机器数量|
| packageDir     | `[string]` | 训练代码/数据或输出路径, 参考下面的packageDir描述| 
| command        | `[string]`   | 任务启动命令, 包括用户包的相对或相对路径|
| args           | `[string]` | 任务启动参数|
| cluster        | `string`   | 运行集群, 支持ccs clusterid 作为参数，如：cls-kbjnobh2|
| runtimeVersion | `string`   | Optional, 训练环境, 指固定的运行环境版本，具体参考下面的[runtimeVersion描述](#runtimeVersion描述)|

## 机器类型描述

机器类型使用如"aUbGcP"的方式描述，表示使用 a Unit CPU，bG 内存，c 个 GPU卡。举例如下：

| 机器类型                  |  CPU | 内存 | GPU |
| :------------------- | :------ | :---- | :-----|
| 1U2G1P               |  1 Unit | 2G | 1个 |
| 1U2G0P               |  1 Unit | 2G | 0个 |
| 0U0G1P               |  默认设置 | 默认设置 | 1个 |
| 空                   | 默认设置 | 默认设置 | 0个 |

## runtimeVersion描述

runtimeVersion 是运行训练/serve的环境版本，目前支持 tf, tia 和 tfplus (用于训练), tiaserv 用于 serving。
其中 tf 为原生 tensorflow 环境，ti为平台定制训练环境，安装了 tensorflow、mxnet、xgboost 等常用的机器学习软件包，tfplus 为腾讯云对于 tensorflow 的 gpu 版本优化，使用 tfplus 在图像视频等领域比原生 tensorflow 最多能提高三倍性能。

| runtimeVersion                  |  描述                          |
| :------------------- | :--------------------------------------- |
| tf-1.4.0-py3              |  tensorflow 1.4.0 版本支持 python3   |
| tf-1.4.0-gpu              |  tensorflow 1.4.0 版本支持 python27/GPU  |
| tf-1.4.0                     |  tensorflow 1.4.0 版本支持 python27 |
| tf-1.4.0-gpu-py3      | tensorflow 1.4.0 版本支持 python3/GPU  |
| tf-1.5.0-py3              |  tensorflow 1.5.0 版本支持 python3   |
| tf-1.5.0-gpu              |  tensorflow 1.5.0 版本支持 python27/GPU  |
| tf-1.5.0                     |  tensorflow 1.5.0 版本支持 python27 |
| tf-1.5.0-gpu-py3      | tensorflow 1.5.0 版本支持 python3/GPU  |
| tf-1.6.0-py3              |  tensorflow 1.6.0 版本支持 python3   |
| tf-1.6.0-gpu              |  tensorflow 1.6.0 版本支持 python27/GPU  |
| tf-1.6.0                     |  tensorflow 1.6.0 版本支持 python27 |
| tf-1.6.0-gpu-py3      | tensorflow 1.6.0 版本支持 python3/GPU  |
| tf-1.7.0-py3              |  tensorflow 1.7.0 版本支持 python3   |
| tf-1.7.0-gpu              |  tensorflow 1.7.0 版本支持 python27/GPU  |
| tf-1.7.0                     |  tensorflow 1.7.0 版本支持 python27 |
| tf-1.7.0-gpu-py3      | tensorflow 1.7.0 版本支持 python3/GPU  |

| runtimeVersion                  |  描述                          |
| :------------------- | :--------------------------------------- |
| tia-1.4.0-py3              |  tensorflow 1.4.0, mxnet, xgboost, 支持cos, 版本支持 python3   |
| tia-1.4.0-gpu              |  tensorflow 1.4.0,  mxnet, xgboost, 持cos, 支持cos,版本支持 python27/GPU  |
| tia-1.4.0                     |  tensorflow 1.4.0, mxnet, xgboost, 支持cos, 版本支持 python27 |
| tia-1.4.0-gpu-py3      | tensorflow 1.4.0 版本支持, 支持cos, python3/GPU  |
| tia-1.5.0-py3              |  tensorflow 1.5.0, mxnet, xgboost, 支持cos, 版本支持 python3   |
| tia-1.5.0-gpu              |  tensorflow 1.5.0, mxnet, xgboost, 支持cos, 版本支持 python27/GPU  |
| tia-1.5.0                     |  tensorflow 1.5.0, 支持cos, 版本支持 python27 |
| tia-1.5.0-gpu-py3      | tensorflow 1.5.0, 支持cos, 版本支持 python3/GPU  |
| tia-1.6.0-py3              |  tensorflow 1.6.0, mxnet, xgboost, 支持cos, 版本支持 python3   |
| tia-1.6.0-gpu              |  tensorflow 1.6.0, mxnet, xgboost, 支持cos, 版本支持 python27/GPU  |
| tia-1.6.0                     |  tensorflow 1.6.0, mxnet, xgboost, 支持cos, 版本支持 python27 |
| tia-1.6.0-gpu-py3      | tensorflow 1.6.0, mxnet, xgboost, 支持cos, 版本支持 python3/GPU  |
| tia-1.7.0-py3              |  tensorflow 1.7.0, mxnet, xgboost, 支持cos, 版本支持 python3   |
| tia-1.7.0-gpu              |  tensorflow 1.7.0, mxnet, xgboost, 支持cos, 版本支持 python27/GPU  |
| tia-1.7.0                     |  tensorflow 1.7.0, mxnet, xgboost, 支持cos, 版本支持 python27 |
| tia-1.7.0-gpu-py3      | tensorflow 1.7.0, 支持cos, 版本支持 python3/GPU  |

| runtimeVersion                  |  描述                          |
| :------------------- | :--------------------------------------- |
| tfplus-1.6.0-gpu       | tfplus  1.6.0 版本支持 python27/GPU|

>**注意:**
>tfplus-1.6.0-gpu 为 tfplus 版本，需要对 tensorflow 代码有少量修改, 支持 tfplus 模式；
>tfplus 不支持非 gpu 版本，至少会使用一个gpu, 无ps，需要运行分布式版本的时候请设置 worker 数量, 不设置默认运行单机版本。

运行 tfplus 的例子, 这里例子运行了一个三个 worker（每个 worker 分配两张 gpu 卡，不限制 cpu，内存）的分布式训练。

```bash
$ tictl job create test73 \
  --cluster=cls-rgaisoe4 \
  --region=ap-guangzhou \
  --command="python /scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py \
            --model resnet50 \
            --batch_size 32 \
            --variable_update tfplus" \
  --runtime=tfplus-1.6.0-gpu \
  --wcount=3 \
  --workertype=0U0G2P
```

#### serving 环境

| runtimeVersion                  |  描述                          |
| :------------------- | :--------------------------------------- |
| tiaserv-1.6.0-cpu     | 1.6.0 版本的 serving 环境，支持 cpu|
| tiaserv-1.6.0-gpu     | 1.6.0 版本的 serving 环境，支持 gpu|












