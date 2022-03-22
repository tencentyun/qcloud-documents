当 TEM 应用处于运行失败状态时，说明至少有一个实例不处于 Running 状态，本文将列举几个常见的实例错误状态，并指导如何进行对应的故障排查。

## 实例错误状态

### CrashLoopBackOff

#### 状态说明
实例中应用程序的运行有问题，容器启动/运行失败。

#### 解决方案
查看实例的日志，通过**日志内容**排查问题。

![](https://qcloudimg.tencent-cloud.cn/raw/34a8a91db77244e0262d162a9040f36e.png)

### Error

#### 状态说明
与 CrashLoopBackOff 类似，说明实例中应用程序的运行有问题，容器启动/运行失败。

#### 解决方案
查看实例的日志，通过**日志内容**排查问题。

![](https://qcloudimg.tencent-cloud.cn/raw/7a7517f08d6084f81636a02bf18b3e33.png)

### Running Unhealthy：Readiness probe failed

#### 状态说明
应用配置的就绪健康检查失败。

#### 解决方案
请在**应用部署** > **健康检查**页面中，检查应用的**就绪检查**配置是否正确。
![](https://qcloudimg.tencent-cloud.cn/raw/64f286deaeeb89cb75134c8bdee8728b.png)

### Running Unhealthy：Liveness probe failed

#### 状态说明
应用配置的存活健康检查失败。

#### 解决方案
请在**应用部署** > **健康检查**页面中，检查应用的**存活检查**配置是否正确。
![](https://qcloudimg.tencent-cloud.cn/raw/5ce2fa1f8e286d5203850a07f98fbe14.png)

### Running Unhealthy：Readiness check failed according to l4 listener: xxx of CLB xxx. Service: xxx

#### 状态说明
应用配置的访问配置无法连通。

#### 解决方案
请在**应用详情** > **基本信息** > **访问配置**页面中，检查应用配置的**访问配置**的端口和协议是否正确。
![](https://qcloudimg.tencent-cloud.cn/raw/2ff77b7003de14f060c5fbebd9337df2.jpg)

### PostStartHookError

#### 状态说明
为应用配置的 PostStart 运行失败。

#### 解决方案
请在**应用部署** > **启停管理**页面中，检查应用配置的 **PostStart** 是否能正常运行。

![](https://qcloudimg.tencent-cloud.cn/raw/3ce766f11d339bab23feedee5eec885a.png)

### ContainerCreating

#### 状态说明
实例容器创建失败。

#### 解决方案
请在**应用部署** > **持久化存储**页面中，检查应用是否挂载了不存在的数据卷。![](https://qcloudimg.tencent-cloud.cn/raw/ea34cc516fa202e403994d0e2fbc9f3f.png)

### CreateContainerConfigError

#### 状态说明
实例容器配置失败。

#### 解决方案
请在**应用部署** > **环境变量**页面中，检查应用是否引用了不存在的配置。

![](https://qcloudimg.tencent-cloud.cn/raw/7c41d941a559509f4f895e121434ea3d.png)

### ImagePullBackOff

#### 状态说明
实例镜像拉取失败。

#### 解决方案
前往 [TCR控制台](https://console.cloud.tencent.com/tcr/repository?rid=1) 检查应用使用的镜像是否存在或被误删除。
