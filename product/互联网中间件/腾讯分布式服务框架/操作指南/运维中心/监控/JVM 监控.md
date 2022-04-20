## 操作场景

JVM 监控功能用于监控重要的 JVM 指标，包含已用堆内存（MB）、CPU 使用率（%）、已加载类数（次数）和活动线程数（次数）。仅 Java 应用支持 JVM 监控能力。

> ?
>
> - JVM 监控能力依赖实例上安装的探针。如您发现 JVM 监控不可用（2020年9月2日前导入集群的节点默认没有携带可以支持 JVM 监控的探针），针对虚拟机部署的业务，可以通过重新导入集群或重新安装 Agent 来使用 JVM 监控能力。针对容器部署的业务，则需要在 Dockerfile 中增加 JVM 监控组件 `TencentCloudJvmMonitor-1.1.0`（[下载地址](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/jvm%E7%9B%91%E6%8E%A7/TencentCloudJvmMonitor-1.1.0-RELEASE.jar)）。容器部署详细操作请参见 [制作容器镜像](https://cloud.tencent.com/document/product/649/50610)。
> - 如果您在使用时遇到问题，请参见 [JVM 监控常见问题](https://cloud.tencent.com/document/product/649/42891)。

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

  ![](https://main.qcloudimg.com/raw/74a13ceea3c30a5de276aa74b12548d9.png)

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

所展示的线程列表为进入页面时刻获取的数据，您可通过单击卡片右上方的刷新按钮，拉取当前的最新数据。![](https://main.qcloudimg.com/raw/563edbf3f11700af6d5aaef8914dc980.png)
:::
::: 死锁检测
在线程详情卡片中，单击**死锁检测**tab 卡片页中的**检测死锁**，实时检测当前进程中存在的死锁线程。

![](https://main.qcloudimg.com/raw/d52be0c6edde1b0d3d7682fcbc6de66e.png)

<dx-alert infotype="explain" title="">
死锁检测目前的实现，是可以打印互相死锁的线程栈；多个线程等待同一个死锁的情况下，并不能检测出全部的死锁线程，只能找到死锁的根源；建议修复死锁后，重复检测以确认不出现嵌套死锁。
</dx-alert>

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
