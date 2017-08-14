### 1. 登录弹性 MapReduce 官网控制台
登录 [官网](https://www.qcloud.com/product/emr) 后访问 https://emr.qcloud.com 进入弹性 MapReduce 管理控制台
### 2. 集群创建
集群创建可参考 [创建弹性 MapReduce]( https://www.qcloud.com/document/product/589/10841?!preview&lang=cn)
### 3. 集群管理
登录后进入弹性 MapReduce [管理控制台](https://www.qcloud.com/login?s_url=https%3A%2F%2Femr.qcloud.com%2Findex), 如下图。
![](//mc.qcloudimg.com/static/img/82b888deb0e7e8c47590956227234816/image.png)
* 勾选 “实例ID” 可以分配集群至项目
* 单击 “项目下拉列表” 可以切换项目
* 单击 “地域下拉列表” 可以切换地域
* 单击 “详情” 可以查看集群详情
### 4. 集群详情查看
* 在集群管理页面单击详情后进入下图。
![](//mc.qcloudimg.com/static/img/2ab38b91148fb511e2b30be607467348/image.png)
* 软件以及节点信息
![](//mc.qcloudimg.com/static/img/d82d45bbfdeb37d72c0b62996a5b3169/image.png)
* 如上二图分别展示了集群的基本信息和集群的软件以及硬件信息
* master 公网 IP 是快捷入口访问的 IP
* 软件信息显示了本集群安装的软件
* 硬件信息展示了各节点硬件配置详细信息
### 5. 节点详情查看
在集群管理页面单击【节点信息】，可以查看当前集群节点信息，如下图。
![](//mc.qcloudimg.com/static/img/ef973a27959e0d04d3b212d85e2f96c2/image.png)
* 可以切换子 tab 查看不同节点信息
* 节点信息展示了 IP、部署的进程以及硬件配置
### 6. 节点扩容
在节点详情页面切换到 core 节点或者 task 节点会出现增加节点按钮，如下图。
![](//mc.qcloudimg.com/static/img/d59e3b0839c52350f4fcc906630949ad/image.png)
* 当前扩容只支持 core 节点和 task 节点扩容
* 扩容的节点规格和之前的节点规格一致
* 单击加号可以增加节点数量
### 7. 节点缩容
节点缩容即减少节点个数，目前仅 task 节点支持该功能。
### 8. 快捷入口
在详情页单击【快捷入口】可以到快捷入口页面，如下图。
![](//mc.qcloudimg.com/static/img/73c6b553a2dea93fce1bfe4a965a4827/image.png)
* 快捷入口集成了各组件的 Web UI 访问入口
* 登录这些服务需要进行用户名和密码验证（用户名和密码是登录子机的用户名和密码）
* 其中 Hue 登录后需要二次验证，首次登录 Hue 需要在 Hue 里添加用户
* 集群文件系统超级用户名为 Hadoop, 在 Hue 添加用户的时候建议用户名设置为 Hadoop


