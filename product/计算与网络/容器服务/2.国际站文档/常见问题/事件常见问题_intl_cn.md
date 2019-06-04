## 创建服务常见错误事件解决方法

### 1.Back-off restarting failed docker container
说明：正在重启异常的Docker容器。
解决方法：检查镜像中执行的Docker进程是否异常退出，若镜像内并无一持续运行的进程，可在创建服务的页面中添加执行脚本。

### 2.fit failure on node: Insufficient cpu
说明：集群CPU不足。
解决方法：原因是节点无法提供足够的计算核心，请在服务页面修改CPU限制或者对集群进行扩容。

### 3.no nodes available to schedule pods
说明：集群资源不足。
解决方法：原因是没有足够的节点用于承载实例，请在服务页面修改服务的实例数量，修改实例数量或者CPU限制。

### 4.pod failed to fit in any node
说明：没有合适的节点可供实例使用。
解决方法：原因是服务配置了不合适的资源限制，导致没有合适的节点用于承载实例，请在服务页面修改服务的实例数量或者CPU限制。

### 5.Liveness probe failed: 
说明：容器健康检查失败
解决方法：检查镜像内容器进程是否正常，检查检测端口是否配置正确。

### 6.Error syncing pod, skipping 
Error syncing pod, skipping failed to "StartContainer" for with CrashLoopBackOff: "Back-off 5m0s restarting failed container
说明：容器进程崩溃或退出。
解决方法：检查容器内是否有持续运行的前台进程，若有检查其是否有异常行为。详情请参考构建docker镜像指南 https://cloud.tencent.com/document/product/457/7208。

如果以上解决方法未能解决您的问题，请联系客服。





