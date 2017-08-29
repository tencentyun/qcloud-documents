## 集群创建
集群创建参见 [创建一个 EMR 集群](https://www.qcloud.com/document/product/589/10981)。
## 集群管理
集群创建成功后，登录弹性 MapReduce [控制台](https://www.qcloud.com/login?s_url=https%3A%2F%2Femr.qcloud.com%2Findex)，进入集群列表页面。
![](//mc.qcloudimg.com/static/img/82b888deb0e7e8c47590956227234816/image.png)
* 勾选【实例 ID】可以分配集群至项目。
* 单击【项目下拉列表】可以切换项目。
* 单击【地域下拉列表】可以切换地域。
* 单击【详情】可以查看集群详情。

### 集群详情查看
在集群列表页面，单击相应集群的【详情】按钮后进入集群管理页。
用户可以在实例详情页查看集群的基本信息、软件以及硬件信息。
**基本信息：**
![](//mc.qcloudimg.com/static/img/7ee2d62da259f6fc05c8dfdcced0be2f/image.png)
Master 公网 IP 是快捷入口页面的地址入口 IP。
**软件以及节点信息：**
![](//mc.qcloudimg.com/static/img/d82d45bbfdeb37d72c0b62996a5b3169/image.png)
* 软件信息显示了本集群安装的软件。
* 硬件信息展示了各节点硬件配置详细信息。

### 节点详情查看
在集群管理页面单击【节点信息】，可以查看当前集群节点信息。
![](//mc.qcloudimg.com/static/img/252f9c0d712eaba8c5872dff3917fbd0/image.png)
* 可以通过切换子 tab 查看不同节点信息。
* 节点信息展示了集群内私有网络的 IP、部署的进程以及硬件配置。

### 节点扩容
在节点详情页面切换到 Core 节点或者 Task 节点会出现【增加节点】按钮，用户可进行节点扩容。
当前只支持 Core 节点和 Task 节点扩容。扩容的节点规格和之前的节点规格一致。
![](//mc.qcloudimg.com/static/img/d59e3b0839c52350f4fcc906630949ad/image.png)
### 节点缩容
节点缩容即减少节点个数，目前仅 Task 节点支持该功能。
### 快捷入口
在集群（实例）管理页单击【快捷入口】可以进入到快捷入口页面。快捷入口集成了各组件（Software）的 Web UI 访问入口(地址入口)，登录这些组件需要进行用户名和密码验证（用户名和密码是登录子机的用户名和密码）。
![](//mc.qcloudimg.com/static/img/937bc871fece5ec0003f780f7caf4ff0/image.png)
* Hue 登录后需要二次验证，首次登录 Hue 需要在 Hue 里添加用户。
* 集群文件系统超级用户名为 Hadoop, 在 Hue 添加用户的时候建议用户名设置为 Hadoop。


