## 简介

GooseFS 为用户提供了一个就近计算端的缓存文件系统，当文件存储在远端存储系统时（例如对象存储），用户可以通过 distributedload 指令将需要使用的文件数据和元数据加载到 GooseFS 集群中，起到减少访问延迟、加速计算作业的效果。

GooseFS distributedLoad 指令如下：
```
distributedLoad [-A] [--replication <num>] [--active-jobs <num>] [--expire-time] <path>
-A 是否启用原子性的distributed load 能力
--active-jobs <active job count> 可以同时启用的数据加载任务数量，默认上限值为3000，如果超过该数值，新增任务需要等候当前任务完成后再执行。
--expire-time <arg> 设置清除用于数据加载的临时目录的过期时间，默认为24小时（单位默认ms，支持s，min，hour，如100s）
--replication <replicas> 每个加载任务加载的Block数据副本数，默认为1。
```

## 实践步骤

### 流程说明

distributedLoad 指令的完整执行流程涉及到 GooseFS client、JobMaster、JobWorker、Worker 模块，分环节说明如下：
1. 由 GooseFS Client 发起任务。
2. 由 GooseFS JobMaster 将每个文件转换为 Job，并按照 Block 的集合拆分为不同的 Task。
3. 由 GooseFS JobMaster 将不同的 Task 拆分给 JobWorker ，有不同的 JobWorker 发起 Load 操作。
4. GooseFS JobWorker 并发执行 Tasks，每个 Task 都会向 Worker 执行请求读操作，并发起写操作，其中每个读操作会向 Cosn 发起一个 Read request。

根据上述流程，可以推断出可能存在的瓶颈点如下：
1. GooseFS Client 按照 file 粒度去发起任务的并发。
2. GooseFS JobMaster 组织并分发任务的速度。
3. GooseFS JobWorker 执行任务的并发度。
4. GooseFS Worker 线程执行读操作与写操作的并发度。
5. Cosn 的处理 Read Request 的速度。

其中，第2项组织任务是内存操作，基本为信令流操作，分发任务的周期为 Worker 的心跳间隔（1s），基本上不会产生瓶颈。因此，主要调优方向集中在 JobWorker、Worker 和 Cosn 模块，涉及的关键参数如下：
1. JobWorker 模块：
```
goosefs.user.block.worker.client.pool.max: 建立读写流的时候，会从client pool中去获取，过小会阻塞获取client
goosefs.job.worker.max.active.task.num : 同时允许执行的task数目
goosefs.job.worker.threadpool.size: 处理task的线程数目
goosefs.user.block.worker.client.pool.max：设置jobworker worker client数量，过小会阻塞获取client
```
2. Worker 模块：
```
goosefs.worker.network.reader.buffer.size:会影响worker的内存占用
goosefs.worker.network.block.reader.threads.max:决定了worker用于read的最大线程数目
```
3. Cosn 模块：
```
fs.cosn.block.size：load上来的block的大小
fs.cosn.upload_thread_pool： read thread的大小，每个worker会共用一个
fs.cosn.read.ahead.block.size：cosn会按照这个粒度去请求cos
fs.cosn.read.ahead.queue.size：cosn是有预读功能的，主要针对大文件顺序读场景，而load刚好是顺序读，但是不一定是大文件。
```

### 配置调优

#### Cosn 配置

GooseFS 缓存集群提供的吞吐规模取决于集群和对象存储之间的吞吐情况，依赖于 Cosn 的性能，一般情况下可以根据业务需要调整 Cosn 的配置：

在大数据场景下，文件平均大小比较大，推荐配置如下：
1. `fs.cosn.block.size`：推荐设置为128MB。
2. `fs.cosn.upload_thread_pool`：推荐设置为 CPU 数目的2 - 3倍，也需要根据 CPU 的使用率适当增加或降低线程池数量
3. `fs.cosn.read.ahead.block.size`：需要根据 block 大小来调整：
 - 如果文件平均大小为几十 MB 量级，则可以设置为4MB。
 - 如果为 MB 级或者 KB 级文件，推荐设置为文件大小的平均值或者中位值。尽量一次 rpc 可以读回来，其原因是数据长度占用了 HTTP 请求较小的 body，rpc 的消耗可能会大于本身读数据的消耗，所以尽量减少 rpc 次数。
4. `fs.cosn.read.ahead.queue.size`：推荐设置为8 - 32，需要根据内存容量数值来设置。一般情况下，一个文件输入流（inputstream）的内存占用等于 block.size\*queue.size。由于 block 大小等于`fs.cosn.block.size`/`fs.cosn.read.ahead.block.size`，以推荐设置为例，该数值等于32，所以设置值不需要大于32，如果设置超过32反而会浪费资源。

#### Worker 节点配置

确定 Cosn 配置之后，可以进一步明确 Worker 节点配置：
Worker 节点配置：`goosefs.worker.network.reader.buffer.size`，这个值也需要根据内存评估，读操作总共占用的内存大小等于 `worker read 并发数量` x（`buffer.size` + 一个`inputstream`的内存占用 + 单次`readRequest`的长度（默认是1MB））。

#### JobWorker 配置

接下来明确 JobWorker 的配置：
1. `goosefs.job.worker.max.active.task.num`：这一数值可以略大于`fs.cosn.upload_thread_pool`的数值，从而充分利用 cosn 的能力。
2. `goosefs.user.block.worker.client.pool.max`：默认是1024，原则上要保证这个配置值需要等于`goosefs.job.worker.max.active.task.num`的2倍。
3. `goosefs.job.worker.threadpool.size`：默认是10，这一数值的最大值需要小于等于`goosefs.job.worker.max.active.task.num`。

使用 GooseFS Client 发起操作时，可以根据`goosefs.job.worker.max.active.task.num`的值调整客户端的活跃任务数量，原则上需要保证`active-jobs` 的值大于 `goosefs.job.worker.max.active.task.num` 的值。
