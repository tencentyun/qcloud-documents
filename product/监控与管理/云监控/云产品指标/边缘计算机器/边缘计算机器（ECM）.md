

## 命名空间

Namespace=QCE/ECM

## 监控指标

| 指标英文名    | 指标中文名         |                                                              | 单位 | 维度 |
| ------------- | ------------------ | ------------------------------------------------------------ | ---- | ---- |
| CpuUsage      | CPU 使用率         | CPU 利用率是通过 CVM 子机内部监控组件采集上报，数据更加精准     | %    | UUID |
| CpuLoadavg    | CPU 平均负载       | 1分钟内 CPU 平均负载，取 /proc/loadavg 第一列数据（Windows 操作系统无此指标），依赖监控组件安装采集 | -    | UUID |
| MemUsed       | 内存使用量         | 使用的内存量，不包括系统缓存和缓存区占用内存，依赖监控组件安装采集 | MB   | UUID |
| BaseCpuUsage  | 基础 CPU 使用率      | 基础 CPU 使用率通过宿主机采集上报，无须安装监控组件即可查看数据，子机高负载情况下仍可持续采集上报数据 | %    | UUID |
| MemUsage      | 内存利用率         | 用户实际使用的内存量与总内存量之比，不包括缓冲区与系统缓存占用的内存 | %    | UUID |
| LanOuttraffic | 内网出带宽         | 内网网卡的平均每秒出流量                                     | Mbps | UUID |
| LanIntraffic  | 内网入带宽         | 内网网卡的平均每秒入流量                                     | Mbps | UUID |
| LanOutpkg     | 内网出包量         | 内网网卡的平均每秒出包量                                     | 个/s | UUID |
| LanInpkg      | 内网入包量         | 内网网卡的平均每秒入包量                                     | 个/s | UUID |
| TcpCurrEstab  | TCP 连接数         | 处于 ESTABLISHED 状态的 TCP 连接数量，依赖监控组件安装采集   | 个   | UUID |
| WanOuttraffic | 外网出带宽         | 外网平均每秒出流量，最小粒度数据为计算10秒总流量/10秒得出   | Mbps | UUID |
| WanIntraffic  | 外网入带宽         | 外网平均每秒入流量                                           | Mbps | UUID |
| WanOutpkg     | 外网出包量         | 外网平均每秒出包量                                           | 个/s | UUID |
| WanInpkg      | 外网入包量         | 外网平均每秒入包量                                           | 个/s | UUID |
| AccOuttraffic | 外网网卡每秒出流量 | 外网网卡的平均每秒出流量                                     | MB   | UUID |



## 各维度对应参数总览

| 参数名称                       | 维度名称 | 维度解释 | 格式                                                    |
| ------------------------------ | -------- | -------- | ------------------------------------------------------- |
| Instances.N.Dimensions.0.Name  | UUID     | 实例 UUID | 输入 String 类型维度名称，例如 uuid                      |
| Instances.N.Dimensions.0.Value | UUID     | 实例 UUID | 输入具体 UUID，例如 4ef19d31-3117-455c-ae8e-2029a07d8999 |

