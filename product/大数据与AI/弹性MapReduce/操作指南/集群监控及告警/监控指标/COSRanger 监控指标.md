### COSRanger-Server

| 指标名称                                          | 指标单位  | 指标含义                                                  |
| ------------------------------------------------- | --------- | --------------------------------------------------------- |
| YGC                                               | 次        | Young GC 次数                                             |
| FGC                                               | 次        | Full GC 次数                                              |
| FGCT                                              | s         | Full GC 消耗时间                                          |
| GCT                                               | s         | 垃圾回收时间消耗                                          |
| YGCT                                              | s         | Young GC 消耗时间                                         |
| S0                                                | %         | Survivor 0 区内存使用占比                                  |
| E                                                 | %         | Eden 区内存使用占比                                       |
| CCS                                               | %         | Compressed class space 区内存使用占比                     |
| S1                                                | %         | Survivor 1 区内存使用占比                                  |
| O                                                 | %         | Old 区内存使用占比                                        |
| M                                                 | %         | Metaspace 区内存使用占比                                  |
| MemNonHeapUsedM                                   | MB        | JVM 当前已经使用的 NonHeapMemory 的数量                   |
| MemNonHeapCommittedM                              | MB        | JVM 当前已经提交的 NonHeapMemory 的数量                   |
| MemHeapUsedM                                      | MB        | JVM 当前已经使用的 HeapMemory 的数量                      |
| MemHeapCommittedM                                 | MB        | JVM 当前已经提交的 HeapMemory 的数量                      |
| MemHeapMaxM                                       | MB        | JVM 配置的 HeapMemory 的数量                              |
| MemHeapInitM                                      | MB        | JVM 初始 HeapMemory 的数量                                 |
| MemNonHeapInitM                                   | MB        | JVM 初始 NonHeapMemory 的数量                             |
| ProcessCpuLoad                                    | %         | CPU 利用率                                                |
| MaxFileDescriptorCount                            | 个        | 最大文件描述符数                                          |
| OpenFileDescriptorCount                           | 个        | 已打开文件描述符数                                        |
| ProcessCpuTime                                    | ms        | CPU 累计使用时间                                          |
| Uptime                                            | s         | 进程运行时长                                              |
| ThreadCount                                       | 个        | 线程数量                                                  |
| PeckThreadCount                                   | 个        | 峰值线程数量                                              |
| DaemonThreadCount                                 | 个        | 后台线程数量                                              |
| check 统计\_PermissionAllowCnt                     | count(次) | check 统计：鉴权通过总数                                  |
| check 统计\_AuthDenyCnt                            | count(次) | check 统计：认证失败总数                                  |
| check 统计\_PermissionDenyCnt                      | count(次) | check 统计：鉴权失败总数                                  |
| 认证成功统计\_Qps                                  | count(次) | 认证成功统计：每秒查询率                                  |
| 认证成功统计\_Total_5m                             | count(次) | 认证成功统计：五分钟请求总数                              |
| 认证成功统计\_Total_1m                             | count(次) | 认证成功统计：一分钟请求总数                              |
| 认证成功统计\_Qps_5m                               | count(次) | 认证成功统计：五分钟平均请求数                            |
| 认证成功统计\_Qps_1m                               | count(次) | 认证成功统计：一分钟平均请求数                            |
| accessStat\_DELETE 操作统计\_Qps                    | count(次) | accessStat_DELETE 操作统计：每秒查询率                    |
| accessStat_DELETE 操作统计\_Total_5m               | count(次) | accessStat_DELETE 操作统计：五分钟请求总数                |
| accessStat_DELETE 操作统计\_Total_1m               | count(次) | accessStat_DELETE 操作统计：一分钟请求总数                |
| accessStat_DELETE 操作统计\_Qps_5m                 | count(次) | accessStat_DELETE 操作统计：五分钟平均请求数              |
| accessStat_DELETE 操作统计\_Qps_1m                 | count(次) | accessStat_DELETE 操作统计：一分钟平均请求数              |
| accessStat_LIST 操作统计\_Qps                      | count(次) | accessStat_LIST 操作统计：每秒查询率                      |
| accessStat_LIST 操作统计\_Total_5m                 | count(次) | accessStat_LIST 操作统计：五分钟请求总数                  |
| accessStat_LIST 操作统计\_Total_1m                 | count(次) | accessStat_LIST 操作统计：一分钟请求总数                  |
| accessStat_LIST 操作统计\_Qps_5m                   | count(次) | accessStat_LIST 操作统计：五分钟平均请求数                |
| accessStat_LIST 操作统计\_Qps_1m                   | count(次) | accessStat_LIST 操作统计：一分钟平均请求数                |
| accessStat_READ 操作统计\_Qps                      | count(次) | accessStat_READ 操作统计：每秒查询率                      |
| accessStat_READ 操作统计\_Total_5m                 | count(次) | accessStat_READ 操作统计：五分钟请求总数                  |
| accessStat_READ 操作统计\_Total_1m                 | count(次) | accessStat_READ 操作统计：一分钟请求总数                  |
| accessStat_READ 操作统计\_Qps_5m                   | count(次) | accessStat_READ 操作统计：五分钟平均请求数                |
| accessStat_READ 操作统计\_Qps_1m                   | count(次) | accessStat_READ 操作统计：一分钟平均请求数                |
| accessStat_WRITE 操作统计\_Qps                     | count(次) | accessStat_WRITE 操作统计：每秒查询率                     |
| accessStat_WRITE 操作统计\_Total_5m                | count(次) | accessStat_WRITE 操作统计：五分钟请求总数                 |
| accessStat_WRITE 操作统计\_Total_1m                | count(次) | accessStat_WRITE 操作统计：一分钟请求总数                 |
| accessStat_WRITE 操作统计\_Qps_5m                  | count(次) | accessStat_WRITE 操作统计：五分钟平均请求数               |
| accessStat_WRITE 操作统计\_Qps_1m                  | count(次) | accessStat_WRITE 操作统计：一分钟平均请求数               |
| rpc_getRangerAuthPolicy 调用数统计\_Qps            | count(次) | rpc_getRangerAuthPolicy 调用数统计：每秒查询率            |
| rpc_getRangerAuthPolicy 调用数统计\_Total_5m       | count(次) | rpc_getRangerAuthPolicy 调用数统计：五分钟请求总数        |
| rpc_getRangerAuthPolicy 调用数统计\_Total_1m       | count(次) | rpc_getRangerAuthPolicy 调用数统计：一分钟请求总数        |
| rpc_getRangerAuthPolicy 调用数统计\_Qps_5m         | count(次) | rpc_getRangerAuthPolicy 调用数统计：五分钟平均请求数      |
| rpc_getRangerAuthPolicy 调用数统计\_Qps_1m         | count(次) | rpc_getRangerAuthPolicy 调用数统计：一分钟平均请求数      |
| rpc_checkPermission 调用数统计\_Qps                | count(次) | rpc_checkPermission 调用数统计：每秒查询率                |
| rpc_checkPermission 调用数统计\_Total_5m           | count(次) | rpc_checkPermission 调用数统计：五分钟请求总数            |
| rpc_checkPermission 调用数统计\_Total_1m           | count(次) | rpc_checkPermission 调用数统计：一分钟请求总数            |
| rpc_checkPermission 调用数统计\_Qps_5m             | count(次) | rpc_checkPermission 调用数统计：五分钟平均请求数          |
| rpc_checkPermission 调用数统计\_Qps_1m             | count(次) | rpc_checkPermission 调用数统计：一分钟平均请求数          |
| rpc_getDelegationToken 调用数统计\_Qps             | count(次) | rpc_getDelegationToken 调用数统计：每秒查询率             |
| rpc_getDelegationToken 调用数统计\_Total_5m        | count(次) | rpc_getDelegationToken 调用数统计：五分钟请求总数         |
| rpc_getDelegationToken 调用数统计\_Total_1m        | count(次) | rpc_getDelegationToken 调用数统计：一分钟请求总数         |
| rpc_getDelegationToken 调用数统计\_Qps_5m          | count(次) | rpc_getDelegationToken 调用数统计：五分钟平均请求数       |
| rpc_getDelegationToken 调用数统计\_Qps_1m          | count(次) | rpc_getDelegationToken 调用数统计：一分钟平均请求数       |
| rpc_renewDelegationToken 调用数统计\_Qps           | count(次) | rpc_renewDelegationToken 调用数统计：每秒查询率           |
| rpc_renewDelegationToken 调用数统计\_Total_5m      | count(次) | rpc_renewDelegationToken 调用数统计：五分钟请求总数       |
| rpc_renewDelegationToken 调用数统计\_Total_1m      | count(次) | rpc_renewDelegationToken 调用数统计：一分钟请求总数       |
| rpc_renewDelegationToken 调用数统计\_Qps_5m     | count(次) | rpc_renewDelegationToken 调用数统计：五分钟平均请求数     |
| rpc_renewDelegationToken 调用数统计\_Qps_1m     | count(次) | rpc_renewDelegationToken 调用数统计：一分钟平均请求数     |
| rpc_cancelDelegationToken 调用数统计\_Qps          | count(次) | rpc_cancelDelegationToken 调用数统计：每秒查询率          |
| rpc_cancelDelegationToken 调用数统计\_Total_5m     | count(次) | rpc_cancelDelegationToken 调用数统计：五分钟请求总数      |
| rpc_cancelDelegationToken 调用数统计\_Total_1m     | count(次) | rpc_cancelDelegationToken 调用数统计：一分钟请求总数      |
| rpc_cancelDelegationToken 调用数统计\_Qps_5m     | count(次) | rpc_cancelDelegationToken 调用数统计：五分钟平均请求数    |
| rpc_cancelDelegationToken 调用数统计\_Qps_1m    | count(次) | rpc_cancelDelegationToken 调用数统计：一分钟平均请求数    |
| rpc_getSTS 调用数统计\_Qps                         | count(次) | rpc_getSTS 调用数统计：每秒查询率                         |
| rpc_getSTS 调用数统计\_Total_5m                    | count(次) | rpc_getSTS 调用数统计：五分钟请求总数                     |
| rpc_getSTS 调用数统计\_Total_1m                    | count(次) | rpc_getSTS 调用数统计：一分钟请求总数                     |
| rpc_getSTS 调用数统计\_Qps_5m                      | count(次) | rpc_getSTS 调用数统计：五分钟平均请求数                   |
| rpc_getSTS 调用数统计\_Qps_1m                      | count(次) | rpc_getSTS 调用数统计：一分钟平均请求数                   |
| cosRpc_getSTS 调用耗时\_Cost_Avg                   | μs(微秒)  | cosRpc_getSTS 调用耗时：当前一秒内平均耗时                |
| cosRpc_getSTS 调用耗时\_Cost_Avg_1m                | μs(微秒)  | cosRpc_getSTS 调用耗时：一分钟平均耗时                    |
| cosRpc_getSTS 调用耗时\_Cost_Avg_5m                | μs(微秒)  | cosRpc_getSTS 调用耗时：五分钟平均耗时                    |
| cosRpc_getSTS 调用耗时\_Cost_Max                   | μs(微秒)  | cosRpc_getSTS 调用耗时：当前一秒内最大耗时                |
| cosRpc_getSTS 调用耗时\_Cost_Max_1m                | μs(微秒)  | cosRpc_getSTS 调用耗时：一分钟内最大耗时                  |
| cosRpc_getSTS 调用耗时\_Cost_Max_5m                | μs(微秒)  | cosRpc_getSTS 调用耗时：五分钟内最大耗时                  |
| cosRpc_getSTS 调用耗时\_Cost_Min                   | μs(微秒)  | cosRpc_getSTS 调用耗时：当前一秒内最小耗时                |
| cosRpc_getSTS 调用耗时\_Cost_Min_1m                | μs(微秒)  | cosRpc_getSTS 调用耗时：一分钟内最小耗时                  |
| cosRpc_getSTS 调用耗时\_Cost_Min_5m                | μs(微秒)  | cosRpc_getSTS 调用耗时：五分钟内最小耗时                  |
| cosRpc_renewDelegationToken 调用耗时\_Cost_Avg | μs(微秒)  | cosRpc_renewDelegationToken 调用耗时：当前一秒内平均耗时 
| cosRpc_renewDelegationToken 调用耗时\_Cost_Avg_1m  | μs(微秒)  | cosRpc_renewDelegationToken 调用耗时：一分钟平均耗时      |
| cosRpc_renewDelegationToken 调用耗时\_Cost_Avg_5m  | μs(微秒)  | cosRpc_renewDelegationToken 调用耗时：五分钟平均耗时      |
| cosRpc_renewDelegationToken 调用耗时\_Cost_Max     | μs(微秒)  | cosRpc_renewDelegationToken 调用耗时：当前一秒内最大耗时  |
| cosRpc_renewDelegationToken 调用耗时\_Cost_Max_1m  | μs(微秒)  | cosRpc_renewDelegationToken 调用耗时：一分钟内最大耗时    |
| cosRpc_renewDelegationToken 调用耗时\_Cost_Max_5m  | μs(微秒)  | cosRpc_renewDelegationToken 调用耗时：五分钟内最大耗时    |
| cosRpc_renewDelegationToken 调用耗时\_Cost_Min     | μs(微秒)  | cosRpc_renewDelegationToken 调用耗时：当前一秒内最小耗时  |
| cosRpc_renewDelegationToken 调用耗时\_Cost_Min_1m  | μs(微秒)  | cosRpc_renewDelegationToken 调用耗时：一分钟内最小耗时    |
| cosRpc_renewDelegationToken 调用耗时\_Cost_Min_5m  | μs(微秒)  | cosRpc_renewDelegationToken 调用耗时：五分钟内最小耗时    |
| cosRpc_cancelDelegationToken 调用耗时\_Cost_Avg    | μs(微秒)  | cosRpc_cancelDelegationToken 调用耗时：当前一秒内平均耗时 |
| cosRpc_cancelDelegationToken 调用耗时\_Cost_Avg_1m | μs(微秒)  | cosRpc_cancelDelegationToken 调用耗时：一分钟平均耗时     |
| cosRpc_cancelDelegationToken 调用耗时\_Cost_Avg_5m | μs(微秒)  | cosRpc_cancelDelegationToken 调用耗时：五分钟平均耗时     |
| cosRpc_cancelDelegationToken 调用耗时\_Cost_Max    | μs(微秒)  | cosRpc_cancelDelegationToken 调用耗时：当前一秒内最大耗时 |
| cosRpc_cancelDelegationToken 调用耗时\_Cost_Max_1m | μs(微秒)  | cosRpc_cancelDelegationToken 调用耗时：一分钟内最大耗时   |
| cosRpc_cancelDelegationToken 调用耗时\_Cost_Max_5m | μs(微秒)  | cosRpc_cancelDelegationToken 调用耗时：五分钟内最大耗时   |
| cosRpc_cancelDelegationToken 调用耗时\_Cost_Min    | μs(微秒)  | cosRpc_cancelDelegationToken 调用耗时：当前一秒内最小耗时 |
| cosRpc_cancelDelegationToken 调用耗时\_Cost_Min_1m | μs(微秒)  | cosRpc_cancelDelegationToken 调用耗时：一分钟内最小耗时   |
| cosRpc_cancelDelegationToken 调用耗时\_Cost_Min_5m | μs(微秒)  | cosRpc_cancelDelegationToken 调用耗时：五分钟内最小耗时   |
| cosRpc_getDelegationToken 调用耗时\_Cost_Avg       | μs(微秒)  | cosRpc_getDelegationToken 调用耗时：当前一秒内平均耗时 |
| cosRpc_getDelegationToken 调用耗时\_Cost_Avg_1m    | μs(微秒)  | cosRpc_getDelegationToken 调用耗时：一分钟平均耗时    |
| cosRpc_getDelegationToken 调用耗时\_Cost_Avg_5m    | μs(微秒)  | cosRpc_getDelegationToken 调用耗时：五分钟平均耗时    |
| cosRpc_getDelegationToken 调用耗时\_Cost_Max       | μs(微秒)  | cosRpc_getDelegationToken 调用耗时：当前一秒内最大耗时 |
| cosRpc_getDelegationToken 调用耗时\_Cost_Max_1m    | μs(微秒)  | cosRpc_getDelegationToken 调用耗时：一分钟内最大耗时 |
| cosRpc_getDelegationToken 调用耗时\_Cost_Max_5m    | μs(微秒)  | cosRpc_getDelegationToken 调用耗时：五分钟内最大耗时 |
| cosRpc_getDelegationToken 调用耗时\_Cost_Min       | μs(微秒)  | cosRpc_getDelegationToken 调用耗时：当前一秒内最小耗时  |
| cosRpc_getDelegationToken 调用耗时\_Cost_Min_1m    | μs(微秒)  | cosRpc_getDelegationToken 调用耗时：一分钟内最小耗时 |
| cosRpc_getDelegationToken 调用耗时\_Cost_Min_5m | μs(微秒)  | cosRpc_getDelegationToken 调用耗时：五分钟内最小耗时    |
| cosRpc_checkPermission 调用耗时\_Cost_Avg         | μs(微秒)  | cosRpc_checkPermission 调用耗时：当前一秒内平均耗时       |
| cosRpc_checkPermission 调用耗时\_Cost_Avg_1m     | μs(微秒)  | cosRpc_checkPermission 调用耗时：一分钟平均耗时           |
| cosRpc_checkPermission 调用耗时\_Cost_Avg_5m     | μs(微秒)  | cosRpc_checkPermission 调用耗时：五分钟平均耗时           |
| cosRpc_checkPermission 调用耗时\_Cost_Max        | μs(微秒)  | cosRpc_checkPermission 调用耗时：当前一秒内最大耗时       |
| cosRpc_checkPermission 调用耗时\_Cost_Max_1m    | μs(微秒)  | cosRpc_checkPermission 调用耗时：一分钟内最大耗时         |
| cosRpc_checkPermission 调用耗时\_Cost_Max_5m    | μs(微秒)  | cosRpc_checkPermission 调用耗时：五分钟内最大耗时         |
| cosRpc_checkPermission 调用耗时\_Cost_Min          | μs(微秒)  | cosRpc_checkPermission 调用耗时：当前一秒内最小耗时       |
| cosRpc_checkPermission 调用耗时\_Cost_Min_1m     | μs(微秒)  | cosRpc_checkPermission 调用耗时：一分钟内最小耗时         |
| cosRpc_checkPermission 调用耗时\_Cost_Min_5m       | μs(微秒)  | cosRpc_checkPermission 调用耗时：五分钟内最小耗时       |
| cosRpc_getRangerAuthPolicy 调用耗时\_Cost_Avg     | μs(微秒)  | cosRpc_getRangerAuthPolicy 调用耗时：当前一秒内平均耗时|
| cosRpc_getRangerAuthPolicy 调用耗时\_Cost_Avg_1m   | μs(微秒)  | cosRpc_getRangerAuthPolicy 调用耗时：一分钟平均耗时  |
| cosRpc_getRangerAuthPolicy 调用耗时\_Cost_Avg_5m   | μs(微秒)  | cosRpc_getRangerAuthPolicy 调用耗时：五分钟平均耗时  |
| cosRpc_getRangerAuthPolicy 调用耗时\_Cost_Max      | μs(微秒)  | cosRpc_getRangerAuthPolicy 调用耗时：当前一秒内最大耗时   |
| cosRpc_getRangerAuthPolicy 调用耗时\_Cost_Max_1m   | μs(微秒)  | cosRpc_getRangerAuthPolicy 调用耗时：一分钟内最大耗时     |
| cosRpc_getRangerAuthPolicy 调用耗时\_Cost_Max_5m   | μs(微秒)  | cosRpc_getRangerAuthPolicy 调用耗时：五分钟内最大耗时     |
| cosRpc_getRangerAuthPolicy 调用耗时\_Cost_Min    | μs(微秒)  | cosRpc_getRangerAuthPolicy 调用耗时：当前一秒内最小耗时|
| cosRpc_getRangerAuthPolicy 调用耗时\_Cost_Min_1m | μs(微秒)  | cosRpc_getRangerAuthPolicy 调用耗时：一分钟内最小耗时 |
| cosRpc_getRangerAuthPolicy 调用耗时\_Cost_Min_5m   | μs(微秒)  | cosRpc_getRangerAuthPolicy 调用耗时：五分钟内最小耗时     |

 
