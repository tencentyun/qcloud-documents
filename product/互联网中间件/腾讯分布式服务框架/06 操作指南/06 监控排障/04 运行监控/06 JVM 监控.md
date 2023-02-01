## 操作场景

JVM 监控功能用于监控重要的 JVM 指标，包含已用堆内存（MB）、CPU 使用率（%）、已加载类数（次数）和活动线程数（次数）。仅 Java 应用支持 JVM 监控能力。

> ?
>
> - JVM 监控能力依赖实例上安装的探针。如您发现 JVM 监控不可用（2020年9月2日前导入集群的节点默认没有携带可以支持 JVM 监控的探针），针对虚拟机部署的业务，可以通过重新导入集群或重新安装 Agent 来使用 JVM 监控能力。针对容器部署的业务，则需要在 Dockerfile 中增加 JVM 监控组件 `TencentCloudJvmMonitor-x.x.x-RELEASE.jar`。容器部署详细操作请参见 [制作容器镜像](https://cloud.tencent.com/document/product/649/50610)。
> - 如果您在使用时遇到问题，请参见 [JVM 监控常见问题](https://cloud.tencent.com/document/product/649/42891)。

## JVM 监控 jar 包版本信息
JVM 监控 jar 包（即 TencentCloudJvmMonitor-x.x.x-RELEASE.jar，又称 JVM Monitor 或 JVM Agent 包），以下是 JVM 监控包的版本更新信息：

|JVM 监控版本|新增特性以及修复问题|
|----|----|
|[1.3.1](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/jvm%E7%9B%91%E6%8E%A7/TencentCloudJvmMonitor-1.3.1-RELEASE.jar)|<li>修复方法执行分析功能模块执行异常的问题</li> |
|[1.3.0](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/jvm%E7%9B%91%E6%8E%A7/TencentCloudJvmMonitor-1.3.0-RELEASE.jar)|<li>整合 TSF 控制台新增方法执行分析功能</li><li>整合 TSF 控制台新增 GC 日志分析</li><li>修复 gcLog 文件不存在的异常提示</li><li>修复方法执行分析功能模块执行方法为空时超时的问题</li><li>修复线程方法总数计算不准确的问题</li>  |
|[1.2.3](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/jvm%E7%9B%91%E6%8E%A7/TencentCloudJvmMonitor-1.2.3-RELEASE.jar)|<li>修复安全漏洞：升级 jackson-databind 依赖版本到 2.13.2.2</li> |
|[1.2.2](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/jvm%E7%9B%91%E6%8E%A7/TencentCloudJvmMonitor-1.2.2-RELEASE.jar)|<li>修复 tsf 火焰图采集超时的 bug </li> |
|[1.2.1](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/jvm%E7%9B%91%E6%8E%A7/TencentCloudJvmMonitor-1.2.1-RELEASE.jar)|<li>添加一些 codecc 流水线配置</li> |
|[1.2.0](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/jvm%E7%9B%91%E6%8E%A7/TencentCloudJvmMonitor-1.2.0-RELEASE.jar)|<li>新增方法执行分析功能</li><li>支持 GC 日志分析</li> |
|[1.1.3](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/jvm%E7%9B%91%E6%8E%A7/TencentCloudJvmMonitor-1.1.3-RELEASE.jar)|<li>修复安全漏洞：升级 jackson-databind 依赖版本到 2.13.2.2</li> |
|[1.1.2](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/jvm%E7%9B%91%E6%8E%A7/TencentCloudJvmMonitor-1.1.2-RELEASE.jar)|<li>修复一些火焰图的 bug</li>|
|[1.1.1](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/jvm%E7%9B%91%E6%8E%A7/TencentCloudJvmMonitor-1.1.1-RELEASE.jar)|<li>修复一些采集的 so 依赖库</li>|
|[1.1.0](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/jvm%E7%9B%91%E6%8E%A7/TencentCloudJvmMonitor-1.1.0-RELEASE.jar)|<li>新增采集 JVM 内存、线程、火焰图等功能</li>|

## 查看 JVM 监控信息

1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)。
2. 在左侧菜单栏中，单击**服务监控**，选择好时间范围和命名空间，维度选择**服务**，查看当前筛选条件下所有服务的监控图表信息。
3. 单击目标服务卡片，进入服务监控详情页面。
4. 选择 **JVM 监控**页签，查看该服务的 JVM 监控信息。
![](https://qcloudimg.tencent-cloud.cn/raw/b8150eb2eb3adb42a1f46f8bf59268ba.png)



在每个监控曲线区域，您可以进行以下操作：

- 您可以将光标移到曲线上，查看具体时刻的监控数据。
- 您可以单击右上角**前往查看实例诊断和实例日志**跳转至服务实例详情页面查看详细 JVM 监控信息。

> ? 离线节点不支持死锁检测，火焰图和 local span 查询。



### 查看实例 JVM 进程的内存信息

您可在内存标签页中，查看到进程 JVM 内存主要指标变化曲线，了解选定时段内，内存指标随时间的变化情况。
您可通过曲线图上方的时间范围选择器修改曲线显示的时间范围（时间粒度目前支持1分钟和1小时）。
支持的监控指标包括：

- 堆内存（MB）
- 非堆内存（MB）
- Eden Space（MB）
- Survivor Space（MB）
- Old Space（MB）
- Meta Space（MB）
- Young GC（次数）
- Full GC（次数）	

堆内存的 **max** 展示的是堆内存真实可用的最大值（会扣除 to_space 内存），而不是配置的 xmx 参数；JDK1.8版本部分 GC 算法（如 G1GC 的 Survivor space），其 max 值会设置为 max_int 值，此时值会显示为-1。

  ![](https://qcloudimg.tencent-cloud.cn/raw/0045319a6f4847311c830fa88a58b1f9.png)

您还可以通过单击图片卡片右上方的放大图标<img src="https://main.qcloudimg.com/raw/c9a7b0fb759613666b13ece6cb9f32c3.png" style="margin:0;"> ，放大当前图片；或通过单击下载图标<img src="https://main.qcloudimg.com/raw/e5689012a21e45ac1170e916a2b63c63.png" style="margin:0;"> ，将当前图片下载到本地（.png格式）。

### 查看实例 JVM 进程的线程信息

您可在实例详情的**线程** tab 页中，查看到该实例的线程数变化情况、线程列表及线程详情，并进行死锁检测，了解实例的死锁情况。

<dx-tabs>
::: 线程详情
您可在线程详情卡片中查看到当前实例所有的 JVM 线程列表及其详细堆栈信息：

- 在**线程**tab中，以列表形式列出了当前实例的所有线程。
  - 您可查看每个线程的名称、状态、CPU 利用率、堆内存使用量、阻塞计数、CPU 运行时长
  - 您可根据“状态”对线程列表进行筛选，或根据“CPU利用率”或“堆内存使用量”对线程列表进行排序
- 您可通过列表上方的搜索框，快速查找感兴趣的线程。
- 单击某线程行所在区域，可在下方的展开区域中，查看到所选线程的详细信息。

所展示的线程列表为进入页面时刻获取的数据，您可通过单击卡片右上方的刷新按钮，拉取当前的最新数据。![](https://qcloudimg.tencent-cloud.cn/raw/6fd4b6218dedf41026f10e2692d76bcf.png)
:::
::: 死锁检测
在线程详情卡片中，单击**死锁检测**tab 卡片页中的**检测死锁**，实时检测当前进程中存在的死锁线程。

![](https://qcloudimg.tencent-cloud.cn/raw/be013c95e07312660968da2ac53d31c2.png)

<dx-alert infotype="explain" title="">
死锁检测目前的实现，是可以打印互相死锁的线程栈；多个线程等待同一个死锁的情况下，并不能检测出全部的死锁线程，只能找到死锁的根源；建议修复死锁后，重复检测以确认不出现嵌套死锁。
</dx-alert>

:::

::: 线程分析

线程分析功能提供详细的每类线程数量统计、栈帧统计和函数分布，帮助您快速定位线程问题。

在线程详情卡片中，单击**线程分析**页签，您可以查看线程分析结果。



![](https://qcloudimg.tencent-cloud.cn/raw/f048db3c96a3c200f95a48b95d17a276.png)



:::
::: 线程数
您可在线程数卡片中查看到当前实例的 JVM 线程总数、活动线程数、 daemon 线程数随时间的变化情况。
您可通过曲线图上方的时间范围选择器修改曲线显示的时间范围（时间粒度目前支持1分钟和1小时）。
![](https://main.qcloudimg.com/raw/4a1e2d3bc418a7cd7b2cfe83ff498960.jpg)
:::
</dx-tabs>




### 查看实例 JVM 进程的火焰图

您可在**火焰图**标签页中，采集并查看指定时段内程序执行过程所形成的“火焰图”，用以进行性能分析。
操作步骤如下：

1. 选择您所需的数据采集时长。
   目前支持的数据采集时长有：近5秒、近10秒、近30秒、近1分钟、近3分钟
2. 选择您需要采集的火焰图类型，目前支持 CPU、Latency、Allocation 三种类型。
3. 单击**开始采集**，等待所选时长后，可在页面中查看到所采集到的数据形成的火焰图。
4. 再次进入**火焰图**页面时，可查看到上一次采集的火焰图。您可通过步骤1和2重新采集当前实时的火焰图。

> ?数据量过大、无热点函数、或出现进程连接失败等异常情况时，火焰图可能采集失败。具体可查看 JVM 监控 [常见问题](https://cloud.tencent.com/document/product/649/42891)。

![](https://main.qcloudimg.com/raw/1056b0dd4ea9e128483c83323c9e9e8e.png)

### 查看 GC 日志分析

您可在**GC 日志分析**标签页中，输入 GC 日志路径，点击**开始分析**，查看 GC 日志分析结果，定位问题。



![](https://qcloudimg.tencent-cloud.cn/raw/67cdd378a46779c6fa9652556c6525fc.png)



## 常见问题

- [JVM 监控功能为何无法使用？](https://cloud.tencent.com/document/product/649/42891#jvm-.E7.9B.91.E6.8E.A7.E5.8A.9F.E8.83.BD.E4.B8.BA.E4.BD.95.E6.97.A0.E6.B3.95.E4.BD.BF.E7.94.A8.EF.BC.9F)
- [JVM 如何升级 tsf-agent？](https://cloud.tencent.com/document/product/649/42891#jvm-.E5.A6.82.E4.BD.95.E5.8D.87.E7.BA.A7-tsf-agent.EF.BC.9F)
- [火焰图采集失败如何处理？](https://cloud.tencent.com/document/product/649/42891#.E7.81.AB.E7.84.B0.E5.9B.BE.E9.87.87.E9.9B.86.E5.A4.B1.E8.B4.A5.E5.A6.82.E4.BD.95.E5.A4.84.E7.90.86.EF.BC.9F)
- [为何无法查看 JVM 日志？](https://cloud.tencent.com/document/product/649/42891#.E4.B8.BA.E4.BD.95.E6.97.A0.E6.B3.95.E6.9F.A5.E7.9C.8B-jvm-.E6.97.A5.E5.BF.97.EF.BC.9F)
