### 说明
本文旨在帮助大家了解如何快速创建一个容器集群内的nginx服务。

#### 第一步：创建集群
1.首先要拥有一个可运行容器的集群。如无集群，请新建一个集群，详情查看[新建集群](https://www.qcloud.com/document/product/457/6779#.E5.88.9B.E5.BB.BA.E9.9B.86.E7.BE.A4)。

2.创建nginx服务，具体可查看下文详细步骤说明。

#### 第二步：创建nginx服务
1) 服务列表页点击"新建"按钮。
![Alt text](https://mc.qcloudimg.com/static/img/11081690d6b480bd66c68a3c2982b04d/Image+007.png)

2) 填写服务基本信息。

服务名称只能由小写字母和数字组成，并由小写字母开头。此处以nginx为例。

运行集群需要选择运行中和集群内有可用主机的集群。

在运行容器的镜像一栏中，当前只能选择腾讯云镜像仓库的镜像和Docker官方镜像，后续将可选择使用第三方镜像仓库创建服务。此处以nginx官方镜像为例。

点击显示高级设置后可填写内存限制、CPU限制、运行命令、运行参数、环境变量和容量健康检查等参数。

其他选项保持为默认设置，点击创建服务。


![Alt text](https://mc.qcloudimg.com/static/img/c18b47dfdbe50fbb87a3f29fb45b1539/%7B24E5F58D-4F21-468C-B8D1-6481E09736C1%7D.png)




3) 创建完成后，在列表中点击服务名称来查看负载均衡器域名或VIP。

![Alt text](https://mc.qcloudimg.com/static/img/b5eea292a440c16cb92c29bd37fe0c69/Image+071.png)

4) 通过域名或VIP来访问服务。
![Alt text](https://mc.qcloudimg.com/static/img/e48f617e80dce415d83aff243d299268/Image+015.png)
