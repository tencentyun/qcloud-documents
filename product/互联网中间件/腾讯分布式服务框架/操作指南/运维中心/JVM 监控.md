## 操作场景
该任务指导您通过 TSF 控制台查看 JVM 进程监控详情。
>!
>- JVM 监控能力依赖实例上安装的探针。如您发现 JVM 监控不可用（2020年9月2日前导入集群的节点默认没有携带可以支持 JVM 监控的探针），针对虚拟机部署的业务，可以通过重新导入集群或重新安装 Agent 来使用 JVM 监控能力。针对容器部署的业务，则需要在 Dockerfile 中增加 JVM 监控组件 `TencentCloudJvmMonitor-1.1.2`（[下载地址](https://tsf-doc-attachment-1300555551.cos.ap-guangzhou.myqcloud.com/%E5%85%AC%E6%9C%89%E4%BA%91/jvm%E7%9B%91%E6%8E%A7/TencentCloudJvmMonitor-1.1.2-RELEASE.jar)）。容器部署详细操作请参考 [制作容器镜像](https://cloud.tencent.com/document/product/649/50610)。
>- 如果您在使用时遇到问题，请参考 [JVM 监控常见问题](https://cloud.tencent.com/document/product/649/42891)。


## 操作步骤
### 进入实例监控详情页
1. 登录 [TSF 控制台](https://console.cloud.tencent.com/tsf/index)。 
2. 在左侧菜单栏中，单击运维中心分类下的【JVM 监控】。
3. 在 JVM 监控的查询条件中，选择查询条件后，单击【查询】，符合条件的实例列表将会呈列在实例列表中。
 - 命名空间：选择您所需要查询的服务所在的命名空间
 - 服务：选择您所需要查询的服务
 - 实例：选择需要查询的实例，不选则展示已选命名空间和服务下的所有实例
4.  从列表中，选择目标实例，单击【实例ID】，进入该实例的监控详情页。
![](https://main.qcloudimg.com/raw/f4481760f4be5a7dd0190b9a01cf2a89.png)


### 查看实例 JVM 监控的基本信息
您可在【实例概览】标签页中，查看实例的基本信息、实时的指标信息以及近一小时的 CPU 使用率、堆内存使用量、活动线程数、已加载类数的时间变化曲线（曲线时间粒度为1分钟）。
基本信息：
![](https://main.qcloudimg.com/raw/21f38bc46f524d3421251892b6d913e0.png)

JVM 监控概览：
![](https://main.qcloudimg.com/raw/8bcf7fe20501feed35b2f41adc7f21e7.png)

### 查看实例 JVM 进程的内存信息
您可在【内存】标签页中，查看到进程 JVM 内存主要指标变化曲线，了解选定时段内，内存指标随时间的变化情况。
您可通过曲线图上方的【时间范围选择器】修改曲线显示的时间范围（时间粒度目前仅支持1分钟）。
支持的监控指标包括：
- 堆内存（MB）
- 非堆内存（MB）
- Eden Space（MB）
- Survivor Space（MB）
- Young GC（次数）
- Full GC（次数）	
- Old Space（MB）
- Meta Space（MB）

堆内存的【max】展示的是堆内存真实可用的最大值（会扣除 to_space内存），而不是配置的 xmx 参数；JDK1.8版本部分 GC 算法（如 G1GC 的 Survivor space），其 max 值会设置为 max_int 值，此时值会显示为-1。
![](https://main.qcloudimg.com/raw/559a9620a812c2e9178b74c583f1da7f.png)

您还可以通过单击图片卡片右上方的放大图标<img src="https://main.qcloudimg.com/raw/c9a7b0fb759613666b13ece6cb9f32c3.png" style="margin:0;"> ，放大当前图片；或通过单击下载图标<img src="https://main.qcloudimg.com/raw/e5689012a21e45ac1170e916a2b63c63.png" style="margin:0;"> ，将当前图片下载到本地（.png格式）。

### 查看实例 JVM 进程的线程信息
您可在【线程】标签页中，查看到当前进程的线程信息，并进行死锁检测。

#### 线程详情
您可在【线程详情】卡片中查看到当前实例所有的 JVM 线程列表及其详细堆栈信息：
- 在【线程】tab中，以列表形式列出了当前实例的所有线程。
	- 您可查看每个线程的名称、状态、CPU 利用率、堆内存使用量、阻塞计数、CPU 运行时长
	- 您可根据“状态”对线程列表进行筛选，或根据“CPU利用率”或“堆内存使用量”对线程列表进行排序
- 您可通过列表上方的搜索框，快速查找感兴趣的线程。
- 单击某线程行所在区域，可在下方的展开区域中，查看到所选线程的详细信息。

所展示的线程列表为进入页面时刻获取的数据，您可通过单击卡片右上方的刷新按钮，拉取当前的最新数据。
![](https://main.qcloudimg.com/raw/c5de57742bb7ba2540aa07aad2d05890.jpg)


#### 死锁检测
在【线程详情】卡片中，单击【死锁检测】tab 卡片页中的【检测死锁】，实时检测当前进程中存在的死锁线程
![](https://main.qcloudimg.com/raw/a699eb4518f1b6bf24ab6a2ee8dc06ea.jpg)
>?死锁检测目前的实现，是可以打印互相死锁的线程栈；多个线程等待同一个死锁的情况下，并不能检测出全部的死锁线程，只能找到死锁的根源；建议修复死锁后，重复检测以确认不出现嵌套死锁。

#### 线程数
您可在【线程数】卡片中查看到当前实例的 JVM 线程总数、活动线程数、 daemon 线程数随时间的变化情况。
您可通过曲线图上方的【时间范围选择器】修改曲线显示的时间范围（时间粒度目前仅支持1分钟）。
![](https://main.qcloudimg.com/raw/4a1e2d3bc418a7cd7b2cfe83ff498960.jpg)

### 查看实例 JVM 进程的火焰图
您可在【火焰图】标签页中，采集并查看指定时段内程序执行过程所形成的“火焰图”，用以进行性能分析。
操作步骤如下：
1. 选择您所需的数据采集时长。
	目前支持的数据采集时长有：近5秒、近10秒、近30秒、近1分钟、近3分钟
2. 选择您需要采集的火焰图类型，目前支持CPU、Latency、Allocation三种类型。
3. 单击【开始采集】，等待所选时长后，可在页面中查看到所采集到的数据形成的火焰图。
4. 再次进入【火焰图】页面时，可查看到上一次采集的火焰图。您可通过步骤1和2重新采集当前实时的火焰图。
![](https://main.qcloudimg.com/raw/6d4aedc14528560104d05bdf26936441.jpg)
>?数据量过大、无热点函数、或出现进程连接失败等异常情况时，火焰图可能采集失败。具体可查看 JVM 监控 [常见问题](https://cloud.tencent.com/document/product/649/42891)。 
