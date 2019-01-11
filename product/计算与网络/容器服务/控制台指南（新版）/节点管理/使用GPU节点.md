## 使用GPU节点
如果您的业务需要进行深度学习、高性能计算等场景，您可以使用腾讯云容器服务支持 GPU 功能，通过该功能可以帮助您快速使用 GPU 容器。如需要开通 GPU 功能，您可以 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=350&source=0&data_title=容器服务TKE&step=1) 进行申请。

### 使用限制
1. 需要单独开通GPU支持功能，[提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=350&source=0&data_title=容器服务TKE&step=1)申请。
2. 添加的节点需要选择GPU机型，选择GPU相关镜像
3. 容器服务TKE仅在集群 kubernetes 版本大于 **1.8.* ** 时支持使用 GPU 调度。
4. 容器之间不共享 GPU，每个容器可以请求一个或多个 GPU。无法请求 GPU 的一小部分。

### 操作指引
#### 方法 1：新建 GPU 云服务器
1. 在 [容器服务控制台](https://console.cloud.tencent.com/tke2) 新建集群时选择新建 GPU 云服务器，选择 GPU 机型。
![][1]
2. 选择 GPU 的操作系统，并完成创建。
![][2]

#### 方法 2：添加已有 GPU 云服务器
1. 在 [容器服务控制台](https://console.cloud.tencent.com/tke2) 新建集群时选择已有的 GPU 节点
![][3]
2. 选择 GPU 的操作系统，并完成添加。
![][4]

[1]:https://main.qcloudimg.com/raw/a7427e2c5867f87d60757f908feb5c96.png
[2]:https://main.qcloudimg.com/raw/4efd38af40d6c358542bfb9480ee7f88.png
[3]:https://main.qcloudimg.com/raw/5b3c85a8a289a5a61c05dfada9499f20.png
[4]:https://main.qcloudimg.com/raw/280b74f99ae9180bdbc493afe5dc9c57.png
