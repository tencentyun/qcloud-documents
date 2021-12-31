### ALLUXIO-Cluster
<table>
<tr>
<th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td rowspan=4>数据读写总量</td>
<td >BytesReadAlluxio</td>
<td >Bytes</td>
<td >所有 worker 上报的从 Alluxio 存储读取的总字节数</td>
</tr><tr>
<td >BytesReadUfsAll</td>
<td >Bytes</td>
<td >所有 worker 从所有 Alluxio UFSes 读取的字节总数</td>
</tr><tr>
<td >BytesWrittenAlluxio</td>
<td >Bytes</td>
<td >写入所有 worker 的 Alluxio 存储的总字节数</td>
</tr><tr>
<td >BytesWrittenUfsAll</td>
<td >Bytes</td>
<td >所有 worker 写入所有 Alluxio UFSes 的总字节数</td>
</tr><tr>
<td rowspan=4>数据读写吞吐量</td>
<td >BytesReadAlluxioThroughput</td>
<td >Bytes</td>
<td >所有 worker 从 Alluxio 存储读取数据的吞吐量</td>
</tr><tr>
<td >BytesReadUfsThroughput</td>
<td >Bytes</td>
<td >所有 worker 从所有 Alluxio UFSes 读取的吞吐量</td>
</tr><tr>
<td >BytesWrittenAlluxioThroughput</td>
<td >Bytes</td>
<td >所有 worker 写入 Alluxio 存储的吞吐量</td>
</tr><tr>
<td >BytesWrittenUfsThroughput</td>
<td >Bytes</td>
<td >所有 worker 写入所有 Alluxio UFSes 的吞吐量</td>
</tr><tr>
<td rowspan=3>worker 的层上容量</td>
<td >CapacityFree</td>
<td >Bytes</td>
<td >所有 worker 的所有层上的总可用字节</td>
</tr><tr>
<td >CapacityTotal</td>
<td >Bytes</td>
<td >所有 worker 的所有层上的总容量</td>
</tr><tr>
<td >CapacityUsed</td>
<td >Bytes</td>
<td >所有 worker 的所有层上的已用字节总数</td>
</tr><tr>
<td >worker 总数</td>
<td >Workers</td>
<td >个</td>
<td >群集中的 active worker 总数</td>
</tr></table>

### ALLUXIO-Master
<table>
<tr>
<th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td rowspan=2>CompleteFile 操作</td>
<td >CompleteFileOps</td>
<td >个</td>
<td >CompleteFile 操作总数</td>
</tr><tr>
<td >FilesCompleted</td>
<td >个</td>
<td >成功的 CompleteFile 操作总数</td>
</tr><tr>
<td rowspan=2>CreateDirectory 操作</td>
<td > CreateDirectoryOps</td>
<td >个</td>
<td >CreateDirectory 操作总数</td>
</tr><tr>
<td >DirectoriesCreated</td>
<td >个</td>
<td >成功的 CreateDirectory 操作总数</td>
</tr><tr>
<td rowspan=2>CreateFile 操作</td>
<td > CreateFileOps</td>
<td >个</td>
<td >CreateFile 操作总数</td>
</tr><tr>
<td >FilesCreated</td>
<td >个</td>
<td >成功的 CreateFile 操作总数</td>
</tr><tr>
<td rowspan=2>Delete 操作</td>
<td >DeletePathOps</td>
<td >个</td>
<td >Delete 操作总数</td>
</tr><tr>
<td >PathsDeleted</td>
<td >个</td>
<td >成功 Delete 操作的总数</td>
</tr><tr>
<td rowspan=2>FreeFile 操作</td>
<td > FreeFileOps</td>
<td >个</td>
<td >FreeFile 操作总数</td>
</tr><tr>
<td >FilesFreed</td>
<td >个</td>
<td >成功的 FreeFile 操作总数</td>
</tr><tr>
<td rowspan=2>GetFileBlockInfo 操作</td>
<td > GetFileBlockInfoOps</td>
<td >个</td>
<td >GetFileBlockInfo 操作总数</td>
</tr><tr>
<td >FileBlockInfosGot</td>
<td >个</td>
<td >成功的 GetFileBlockInfo 操作总数</td>
</tr><tr>
<td rowspan=2>GetFileInfo 操作</td>
<td > GetFileInfoOps</td>
<td >个</td>
<td >GetFileInfo 操作总数</td>
</tr><tr>
<td >FileInfosGot</td>
<td >个</td>
<td >成功的 GetFileInfo 操作总数</td>
</tr><tr>
<td rowspan=2>GetNewBlock 操作</td>
<td >GetNewBlockOps</td>
<td >个</td>
<td >GetNewBlock 操作总数</td>
</tr><tr>
<td >NewBlocksGot</td>
<td >个</td>
<td >成功的 GetNewBlock 操作总数</td>
</tr><tr>
<td rowspan=2>Mount 操作</td>
<td >MountOps</td>
<td >个</td>
<td >Mount 操作总数</td>
</tr><tr>
<td >PathsMounted</td>
<td >个</td>
<td >成功 Mount 操作总数</td>
</tr><tr>
<td rowspan=2>Unmount 操作</td>
<td >UnmountOps</td>
<td >个</td>
<td >Unmount 操作总数</td>
</tr><tr>
<td >PathsUnmounted</td>
<td >个</td>
<td >成功 Unmount 操作的总数</td>
</tr><tr>
<td rowspan=2>Rename 操作</td>
<td >RenamePathOps</td>
<td >个</td>
<td >Rename 操作总数</td>
</tr><tr>
<td >PathsRenamed</td>
<td >个</td>
<td >成功的 Rename 操作总数</td>
</tr><tr>
<td >SetAcl 操作</td>
<td >SetAclOps</td>
<td >个</td>
<td >SetAcl 操作总数</td>
</tr><tr>
<td >SetAttribute 操作</td>
<td >SetAttributeOps</td>
<td >个</td>
<td >SetAttribute 操作总数</td>
</tr><tr>
<td rowspan=2>操作文件总数</td>
<td >FilesPersisted</td>
<td >个</td>
<td >成功保存的文件总数</td>
</tr><tr>
<td >FilesPinned</td>
<td >个</td>
<td >当前固定的文件总数</td>
</tr><tr>
<td >文件目录总数</td>
<td >TotalPaths</td>
<td >个</td>
<td >Alluxio 命名空间中的文件和目录总数</td>
</tr><tr>
<td rowspan=2>GC 次数 </td>
<td >YGC </td>
<td >次 </td>
<td >Young GC 次数 </td>
</tr><tr>
<td >FGC </td>
<td >次 </td>
<td >Full GC 次数 </td>
</tr><tr>
<td rowspan=3>GC 时间 </td>
<td >FGCT </td>
<td >s </td>
<td >Full GC 消耗时间 </td>
</tr><tr>
<td >GCT </td>
<td >s </td>
<td >垃圾回收时间消耗 </td>
</tr><tr>
<td >YGCT </td>
<td >s </td>
<td >Young GC 消耗时间 </td>
</tr><tr>
<td rowspan=6>内存区域占比 </td>
<td >S0</td>
<td >% </td>
<td >Survivor 0区内存使用占比 </td>
</tr><tr>
<td >E </td>
<td >% </td>
<td >Eden 区内存使用占比 </td>
</tr><tr>
<td >CCS </td>
<td >% </td>
<td >Compressed class space 区内存使用占比 </td>
</tr><tr>
<td >S1 </td>
<td >% </td>
<td >Survivor 1区内存使用占比 </td>
</tr><tr>
<td >O </td>
<td >% </td>
<td >Old 区内存使用占比 </td>
</tr><tr>
<td >M </td>
<td >% </td>
<td >Metaspace 区内存使用占比 </td>
</tr></table>

### ALLUXIO-Worker
<table>
<tr>
<th width=20%>标题 </th>
<th width=20%>指标名称</th>
<th width=15%>指标单位</th>
<th width=45%>指标含义 </th>
</tr><tr>
<td rowspan=2>async 缓存请求</td>
<td >AsyncCacheDuplicateRequests</td>
<td >个</td>
<td >worker 接收的重复 async 缓存请求总数</td>
</tr><tr>
<td >AsyncCacheRequests</td>
<td >个</td>
<td >worker 接收的 async 缓存请求总数</td>
</tr><tr>
<td rowspan=4>Async 缓存块数量</td>
<td >AsyncCacheFailedBlocks</td>
<td >个</td>
<td >worker async 缓存失败的块总数</td>
</tr><tr>
<td >AsyncCacheRemoteBlocks</td>
<td >个</td>
<td >需要从远程源进行 async 缓存的块总数</td>
</tr><tr>
<td >AsyncCacheSucceededBlocks</td>
<td >个</td>
<td >worker async 缓存成功的块总数</td>
</tr><tr>
<td >AsyncCacheUfsBlocks</td>
<td >个</td>
<td >需要从本地源进行 async 缓存的数据块总数</td>
</tr><tr>
<td rowspan=7>Blocks</td>
<td >BlocksAccessed</td>
<td >个</td>
<td >访问此 worker 中任何一个块的总次数</td>
</tr><tr>
<td >BlocksCached</td>
<td >个</td>
<td >在 worker 中用于缓存数据的块总数</td>
</tr><tr>
<td >BlocksCancelled</td>
<td >个</td>
<td >worker 中中止的临时块总数</td>
</tr><tr>
<td >BlocksDeleted</td>
<td >个</td>
<td >按外部请求列出的此 worker 中已删除的块总数</td>
</tr><tr>
<td >BlocksEvicted</td>
<td >个</td>
<td >worker 中逐出的块总数</td>
</tr><tr>
<td >BlocksLost</td>
<td >个</td>
<td >worker 中丢失的数据块总数</td>
</tr><tr>
<td >BlocksPromoted</td>
<td >个</td>
<td >worker 中的任何一个数据块移动到新层的总次数</td>
</tr><tr>
<td rowspan=3>Worker 的层上容量</td>
<td >CapacityFree</td>
<td >Bytes</td>
<td >worker 的所有层上的总可用字节</td>
</tr><tr>
<td >CapacityTotal</td>
<td >Bytes</td>
<td >worker 的所有层上的总容量</td>
</tr><tr>
<td >CapacityUsed</td>
<td >Bytes</td>
<td >worker 的所有层上的已用字节总数</td>
</tr><tr>
<td rowspan=2>GC 次数 </td>
<td >YGC </td>
<td >次 </td>
<td >Young GC 次数 </td>
</tr><tr>
<td >FGC </td>
<td >次 </td>
<td >Full GC 次数 </td>
</tr><tr>
<td rowspan=3>GC 时间 </td>
<td >FGCT </td>
<td >s </td>
<td >Full GC 消耗时间 </td>
</tr><tr>
<td >GCT </td>
<td >s </td>
<td >垃圾回收时间消耗 </td>
</tr><tr>
<td >YGCT </td>
<td >s </td>
<td >Young GC 消耗时间 </td>
</tr><tr>
<td rowspan=6>内存区域占比 </td>
<td >S0</td>
<td >% </td>
<td >Survivor 0区内存使用占比 </td>
</tr><tr>
<td >E </td>
<td >% </td>
<td >Eden 区内存使用占比 </td>
</tr><tr>
<td >CCS </td>
<td >% </td>
<td >Compressed class space 区内存使用占比 </td>
</tr><tr>
<td >S1 </td>
<td >% </td>
<td >Survivor 1区内存使用占比 </td>
</tr><tr>
<td >O </td>
<td >% </td>
<td >Old 区内存使用占比 </td>
</tr><tr>
<td >M </td>
<td >% </td>
<td >Metaspace 区内存使用占比 </td>
</tr>
</table>
