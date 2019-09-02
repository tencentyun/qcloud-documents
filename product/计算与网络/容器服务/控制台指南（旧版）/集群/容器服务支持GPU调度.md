## 简介
如果您的业务需要进行深度学习、高性能计算等场景，您可以使用腾讯云容器服务支持 GPU 功能，通过该功能可以帮助您快速使用 GPU 容器。如需要开通 GPU 功能，您可以 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=350&source=0&data_title=容器服务TKE&step=1) 进行申请。

## 使用指南
### 一. 在集群中添加 GPU 节点
添加 GPU 节点有以下两种方法：
#### 方法 1：新建 GPU 云服务器
1. 在 [容器服务控制台](https://console.cloud.tencent.com/ccs) 新建集群时选择新建 GPU 云服务器，选择 GPU 机型。
![][1]
2. 选择 GPU 的操作系统，并完成创建。
![][2]

#### 方法 2：添加已有 GPU 云服务器
1. 在 [容器服务控制台](https://console.cloud.tencent.com/ccs) 新建集群时选择已有的 GPU 节点
![][3]
2. 选择 GPU 的操作系统，并完成添加。
![][4]

### 二. 创建 GPU 服务的容器
您可以直接通过控制台创建服务时选择容器占用的 GPU 的个数。
![][5]

或通过应用或 kubectl 命令创建，在 YAML 文件中添加 GPU 字段。
![][6]

## 注意事项
1. 仅在集群 kubernetes 版本大于 **1.8.* ** 时支持使用 GPU 调度。
2. 当前 GPU 仅支持 CentOS 系统，请留意您的集群的操作系统。
3. 容器之间不共享 GPU，每个容器可以请求一个或多个 GPU。无法请求 GPU 的一小部分。
4. 建议搭配亲和性调度来使用 GPU 功能。



[1]: https://main.qcloudimg.com/raw/be839f6e431eb74d2b1cea2b4d785209.png
[2]: https://main.qcloudimg.com/raw/980efc42700803ce25fedfc8c692cafe.png
[3]: https://main.qcloudimg.com/raw/83701fb1644bd2be8f7adf408fff9ef8.png
[4]: https://main.qcloudimg.com/raw/72dd3a0c581e9157a51e09f4c3f1c058.png
[5]: https://main.qcloudimg.com/raw/a768a0610894587528573f959277ab9f.png
[6]: https://main.qcloudimg.com/raw/2f2b3a751fd4bc0a3d443d7495fb1050.png
