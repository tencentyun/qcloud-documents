## 命名空间

Namespace=QCE/TXMR_ALLUXIO



## 监控指标

### Alluxio-Cluster

<table>
<thead>
<tr>
<th><width=30%>指标英文名</th>
<th><width=15%>指标中文名</th>
<th><width=40%>指标含义</th>
<th><width=5%>指标单位</th>
<th><width=10%>维度</th>
</tr>
</thead>
<tbody><tr>
<td>AlluxioClusterBytesBytesreadalluxio</td>
<td>数据读写总量 BytesReadAlluxio</td>
<td>所有 worker 上报的从 Alluxio 存储读取的总字节数</td>
<td>B</td>
<td>id4alluxiooverview</td>
</tr>
<tr>
<td>AlluxioClusterBytesBytesreadufsall</td>
<td>数据读写总量 BytesReadUfsAll</td>
<td>所有 worker 从所有 Alluxio UFSes 读取的字节总数</td>
<td>B</td>
<td>id4alluxiooverview</td>
</tr>
<tr>
<td>AlluxioClusterBytesByteswrittenalluxio</td>
<td>数据读写总量 BytesWrittenAlluxio</td>
<td>写入所有 worker 的 Alluxio 存储的总字节数</td>
<td>B</td>
<td>id4alluxiooverview</td>
</tr>
<tr>
<td>AlluxioClusterBytesByteswrittenufsall</td>
<td>数据读写总量 BytesWrittenUfsAll</td>
<td>所有 worker 写入所有 Alluxio UFSes 的总字节数</td>
<td>B</td>
<td>id4alluxiooverview</td>
</tr>
<tr>
<td>AlluxioClusterBytesThroughputBytesreadalluxiothroughput</td>
<td>数据读写吞吐量 BytesReadAlluxioThroughput</td>
<td>所有 worker 从 Alluxio 存储读取数据的吞吐量</td>
<td>B</td>
<td>id4alluxiooverview</td>
</tr>
<tr>
<td>AlluxioClusterBytesThroughputBytesreadufsthroughput</td>
<td>数据读写吞吐量 BytesReadUfsThroughput</td>
<td>所有 worker 从所有 Alluxio UFSes 读取的吞吐量</td>
<td>B</td>
<td>id4alluxiooverview</td>
</tr>
<tr>
<td>AlluxioClusterBytesThroughputByteswrittenalluxiothroughput</td>
<td>数据读写吞吐量 BytesWrittenAlluxioThroughput</td>
<td>所有 worker 写入 Alluxio 存储的吞吐量</td>
<td>B</td>
<td>id4alluxiooverview</td>
</tr>
<tr>
<td>AlluxioClusterBytesThroughputByteswrittenufsthroughput</td>
<td>数据读写吞吐量 BytesWrittenUfsThroughput</td>
<td>所有 worker 写入所有 Alluxio UFSes 的吞吐量</td>
<td>B</td>
<td>id4alluxiooverview</td>
</tr>
<tr>
<td>AlluxioClusterCapacityCapacityfree</td>
<td>worker的层上容量 CapacityFree</td>
<td>所有 worker 的所有层上的总可用字节</td>
<td>B</td>
<td>id4alluxiooverview</td>
</tr>
<tr>
<td>AlluxioClusterCapacityCapacitytotal</td>
<td>worker的层上容量 CapacityTotal</td>
<td>所有 worker 的所有层上的总容量</td>
<td>B</td>
<td>id4alluxiooverview</td>
</tr>
<tr>
<td>AlluxioClusterCapacityCapacityused</td>
<td>worker的层上容量 CapacityUsed</td>
<td>所有 worker 的所有层上的已用字节总数</td>
<td>B</td>
<td>id4alluxiooverview</td>
</tr>
<tr>
<td>AlluxioClusterWorkersWorkers</td>
<td>worker 总数 Workers</td>
<td>群集中的 active worker 总数</td>
<td>个</td>
<td>id4alluxiooverview</td>
</tr>
</tbody></table>


### Alluxio-Master

| 指标英文名                                          | 指标中文名                               | 指标含义                                | 指标单位 | 维度                                               |
| --------------------------------------------------- | ---------------------------------------- | --------------------------------------- | -------- | -------------------------------------------------- |
| AlluxioMasterGcUtilGcCountFgc                       | GC次数FGC                               | Full GC 次数                            | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterGcUtilGcCountYgc                       | GC次数YGC                               | Young GC 次数                           | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterGcUtilGcTimeFgct                       | GC时间FGCT                              | Full GC 消耗时间                        | s        | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterGcUtilGcTimeGct                        | GC时间GCT                               | 垃圾回收时间消耗                        | s        | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterGcUtilGcTimeYgct                       | GC时间YGCT                              | Young GC 消耗时间                       | s        | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterGcUtilMemoryCcs                        | 内存区域占比CCS                         | Compressed class space 区内存使用占比   | %        | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterGcUtilMemoryE                          | 内存区域占比E                           | Eden 区内存使用占比                     | %        | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterGcUtilMemoryM                          | 内存区域占比M                           | Metaspace 区内存使用占比                | %        | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterGcUtilMemoryO                          | 内存区域占比O                           | Old 区内存使用占比                      | %        | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterGcUtilMemoryS0                         | 内存区域占比S0                          | Survivor 0区内存使用占比                | %        | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterGcUtilMemoryS1                         | 内存区域占比S1                          | Survivor 1区内存使用占比                | %        | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterGetFileBlockInfoOpsFileblockinfosgot   | GetFileBlockInfo操作FileBlockInfosGot   | GetFileBlockInfo 操作总数               | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterGetFileBlockInfoOpsGetfileblockinfoops | GetFileBlockInfo操作GetFileBlockInfoOps | 成功的 GetFileBlockInfo 操作总数        | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterGetFileInfoOpsFileinfosgot             | GetFileInfo操作FileInfosGot             | GetFileInfo 操作总数                    | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterGetFileInfoOpsGetfileinfoops           | GetFileInfo操作GetFileInfoOps           | 成功的 GetFileBlockInfo 操作总数        | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterGetNewBlockOpsGetnewblockops           | GetNewBlock操作GetNewBlockOps           | GetNewBlock 操作总数                    | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterGetNewBlockOpsNewblocksgot             | GetNewBlock操作NewBlocksGot             | 成功的 GetNewBlock 操作总数             | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterMountOpsMountops                       | Mount操作MountOps                       | Mount 操作总数                          | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterMountOpsPathsmounted                   | Mount操作PathsMounted                   | 成功 Mount 操作总数                     | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterRenamePathOpsPathsrenamed              | Rename操作PathsRenamed                  | Rename 操作总数                         | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterRenamePathOpsRenamepathops             | Rename操作RenamePathOps                 | 成功的 Rename 操作总数                  | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterSetAclOpsSetaclops                     | SetAcl操作SetAclOps                     | SetAcl 操作总数                         | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterSetAttributeOpsSetattributeops         | SetAttribute操作SetAttributeOps         | SetAttribute 操作总数                   | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterTotalPathsTotalpaths                   | 文件目录总数TotalPaths                  | Alluxio 命名空间中的文件和目录总数      | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterCompleteFileOpsCompletefileops         | CompleteFile操作CompleteFileOps         | CompleteFile 操作总数                   | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterCompleteFileOpsFilescompleted          | CompleteFile操作FilesCompleted          | 成功的 CompleteFile 操作总数            | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterCreateDirectoryOpsCreatedirectoryops   | CreateDirectory操作CreateDirectoryOps   | CreateDirectory 操作总数                | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterCreateDirectoryOpsDirectoriescreated   | CreateDirectory操作DirectoriesCreated   | 成功的 CompleteFile 操作总数            | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterCreateFileOpsCreatefileops             | CreateFile操作CreateFileOps             | CreateFile 操作总数                     | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterCreateFileOpsFilescreated              | CreateFile操作FilesCreated              | 成功的 CreateFile 操作总数              | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterDeletePathOpsDeletepathops             | Delete操作DeletePathOps                 | Delete 操作总数                         | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterDeletePathOpsPathsdeleted              | Delete操作PathsDeleted                  | 成功 Delete 操作的总数                  | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterFreeFileOpsFilesfreed                  | FreeFile操作FilesFreed                  | FreeFile 操作总数                       | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterFreeFileOpsFreefileops                 | FreeFile操作FreeFileOps                 | 成功的 FreeFile 操作总数                | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterFilesOpsFilespersisted                 | 操作文件总数FilesPersisted              | 成功保存的文件总数                      | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterFilesOpsFilespinned                    | 操作文件总数FilesPinned                 | 当前固定的文件总数                      | 次       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterUnmountOpsPathsunmounted               | Unmount操作PathsUnmounted               | Unmount 操作总数                        | 个       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterUnmountOpsUnmountops                   | Unmount操作UnmountOps                   | 成功 Unmount 操作的总数                 | 个       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterJvmMemMemheapcommittedm                | JVM内存MemHeapCommittedM                | JVM 已经提交的 HeapMemory 的数量        | MB       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterJvmMemMemheapinitm                     | JVM内存MemHeapInitM                     | JVM 初始 HeapMem 的数量                 | MB       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterJvmMemMemheapmaxm                      | JVM内存MemHeapMaxM                      | JVM 配置的 HeapMemory 的数量            | MB       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterJvmMemMemheapusedm                     | JVM内存MemHeapUsedM                     | JVM 当前已经使用的 HeapMemory 的数量    | MB       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterJvmMemMemnonheapcommittedm             | JVM内存MemNonHeapCommittedM             | JVM 当前已经提交的 NonHeapMemory 的数量 | MB       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterJvmMemMemnonheapinitm                  | JVM内存MemNonHeapInitM                  | JVM 初始 NonHeapMem 的数量              | MB       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |
| AlluxioMasterJvmMemMemnonheapusedm                  | JVM内存MemNonHeapUsedM                  | JVM 当前已经使用的 NonHeapMemory 的数量 | MB       | host4alluxioalluxiomaster、id4alluxioalluxiomaster |**

### Alluxio-Worker

| 指标英文名                                                 | 指标中文名                                | 指标含义                                    | 指标单位 | 维度                                               |
| ---------------------------------------------------------- | ----------------------------------------- | ------------------------------------------- | -------- | -------------------------------------------------- |
| AlluxioWorkerAsyncCacheBlocksAsynccachefailedblocks        | async缓存块数量AsyncCacheFailedBlocks    | worker async 缓存失败的块总数               | 个       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerAsyncCacheBlocksAsynccacheremoteblocks        | async缓存块数量AsyncCacheRemoteBlocks    | worker 接收的重复 async 缓存请求总数        | 个       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerAsyncCacheBlocksAsynccachesucceededblocks     | async缓存块数量AsyncCacheSucceededBlocks | worker async 缓存成功的块总数               | 个       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerAsyncCacheBlocksAsynccacheufsblocks           | async缓存块数量AsyncCacheUfsBlocks       | 需要从本地源进行 async 缓存的数据块总数     | 个       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerAsyncCacheRequestsAsynccacheduplicaterequests | async缓存请求AsyncCacheDuplicateRequests | worker 接收的 async 缓存请求总数            | 个       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerAsyncCacheRequestsAsynccacherequests          | async缓存请求AsyncCacheRequests          | worker 接收的 async 缓存请求总数            | 个       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerBlocksBlocksaccessed                          | Block数量BlocksAccessed                  | 访问此 worker 中任何一个块的总次数          | 个       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerBlocksBlockscached                            | Block数量BlocksCached                    | 在 worker 中用于缓存数据的块总数            | 个       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerBlocksBlockscancelled                         | Block数量BlocksCancelled                 | worker 中中止的临时块总数                   | 个       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerBlocksBlocksdeleted                           | Block数量BlocksDeleted                   | 按外部请求列出的此 worker 中已删除的块总数  | 个       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerBlocksBlocksevicted                           | Block数量BlocksEvicted                   | worker 中逐出的块总数                       | 个       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerBlocksBlockslost                              | Block数量BlocksLost                      | worker 中丢失的数据块总数                   | 个       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerBlocksBlockspromoted                          | Block数量BlocksPromoted                  | worker 中的任何一个数据块移动到新层的总次数 | 个       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerCapacityCapacityfree                          | worker的层上容量CapacityFree             | worker 的所有层上的总可用字节               | B        | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerCapacityCapacitytotal                         | worker的层上容量CapacityTotal            | worker 的所有层上的总容量                   | B        | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerCapacityCapacityused                          | worker的层上容量CapacityUsed             | worker 的所有层上的已用字节总数             | B        | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerGcUtilGcCountFgc                              | GC次数FGC                                | Full GC 次数                                | 次       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerGcUtilGcCountYgc                              | GC次数YGC                                | Young GC 次数                               | 次       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerGcUtilGcTimeFgct                              | GC时间FGCT                               | Full GC 消耗时间                            | s        | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerGcUtilGcTimeGct                               | GC时间GCT                                | 垃圾回收时间消耗                            | s        | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerGcUtilGcTimeYgct                              | GC时间YGCT                               | Young GC 消耗时间                           | s        | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerGcUtilMemoryCcs                               | 内存区域占比CCS                          | Compressed class space 区内存使用占比       | %        | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerGcUtilMemoryE                                 | 内存区域占比E                            | Eden 区内存使用占比                         | %        | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerGcUtilMemoryM                                 | 内存区域占比M                            | Metaspace 区内存使用占比                    | %        | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerGcUtilMemoryO                                 | 内存区域占比O                            | Old 区内存使用占比                          | %        | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerGcUtilMemoryS0                                | 内存区域占比S0                           | Survivor 0区内存使用占比                    | %        | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerGcUtilMemoryS1                                | 内存区域占比S1                           | Survivor 1区内存使用占比                    | %        | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerJvmMemMemheapcommittedm                       | JVM内存MemHeapCommittedM                 | JVM 已经提交的 HeapMemory 的数量            | MB       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerJvmMemMemheapinitm                            | JVM内存MemHeapInitM                      | JVM 初始 HeapMem 的数量                     | MB       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerJvmMemMemheapmaxm                             | JVM内存MemHeapMaxM                       | JVM 配置的 HeapMemory 的数量                | MB       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerJvmMemMemheapusedm                            | JVM内存MemHeapUsedM                      | JVM 当前已经使用的 HeapMemory 的数量        | MB       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerJvmMemMemnonheapcommittedm                    | JVM内存MemNonHeapCommittedM              | JVM 当前已经提交的 NonHeapMemory 的数量     | MB       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerJvmMemMemnonheapinitm                         | JVM内存MemNonHeapInitM                   | JVM 初始 NonHeapMem 的数量                  | MB       | host4alluxioalluxioworker、id4alluxioalluxioworker |
| AlluxioWorkerJvmMemMemnonheapusedm                         | JVM内存MemNonHeapUsedM                   | JVM 当前已经使用的 NonHeapMemory 的数量     | MB       | host4alluxioalluxioworker、id4alluxioalluxioworker |





## 各维度对应参数总览

| 参数名称                       | 维度名称                  | 维度解释                     | 格式                                                         |
| :----------------------------- | :------------------------ | :--------------------------- | :----------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | id4alluxiooverview        | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4alluxiooverview                 |
| Instances.N.Dimensions.0.Value | id4alluxiooverview        | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |
| Instances.N.Dimensions.0.Name  | host4alluxioalluxiomaster | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4alluxioalluxiomaster          |
| Instances.N.Dimensions.0.Value | host4alluxioalluxiomaster | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr)，单击**实例 > 集群资源 > 资源管理 > 节点内网 IP**。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4alluxioalluxiomaster   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4alluxioalluxiomaster            |
| Instances.N.Dimensions.0.Value | id4alluxioalluxiomaster   | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |
| Instances.N.Dimensions.0.Name  | host4alluxioalluxioworker | EMR 实例中节点 IP 的维度名称 | 输入 String 类型维度名称：host4alluxioalluxioworker          |
| Instances.N.Dimensions.0.Value | host4alluxioalluxioworker | EMR 实例中具体节点 IP        | 输入具体节点 IP ，可从控制台获取，登录 [腾讯云 MapReduce 控制台](https://console.cloud.tencent.com/emr) ，单击**实例 > 集群资源 > 资源管理 > 节点内网 IP**。也可通过 [查询节点信息](https://cloud.tencent.com/document/product/589/41707) API 获取。 |
| Instances.N.Dimensions.0.Name  | id4alluxioalluxioworker   | EMR 实例 ID 的维度名称       | 输入 String 类型维度名称：id4alluxioalluxioworker            |
| Instances.N.Dimensions.0.Value | id4alluxioalluxioworker   | EMR 实例具体 ID              | 输入 EMR 具体实例 ID，例如：emr-mm8bs222                     |



## 入参说明

**查询弹性 MapReduce（Alluxio-Cluster）监控数据，入参取值如下：**

Namespace=QCE/TXMR_ALLUXIO
&Instances.N.Dimensions.1.Name=id4alluxiooverview
&Instances.N.Dimensions.1.Value=EMR 实例具体 ID



**查询弹性 MapReduce（Alluxio-Master）监控数据，入参取值如下：**

Namespace=QCE/TXMR_ALLUXIO
&Instances.N.Dimensions.0.Name=host4alluxioalluxiomaster
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4alluxioalluxiomaster
&Instances.N.Dimensions.1.Value=EMR 实例具体 ID、

**查询弹性 MapReduce（Alluxio-Worker）监控数据，入参取值如下：**

Namespace=QCE/TXMR_ALLUXIO
&Instances.N.Dimensions.0.Name=host4alluxioalluxioworker
&Instances.N.Dimensions.0.Value=EMR 实例中具体节点 IP
&Instances.N.Dimensions.1.Name=id4alluxioalluxioworker
&Instances.N.Dimensions.1.Value=EMR 实例具体 ID
