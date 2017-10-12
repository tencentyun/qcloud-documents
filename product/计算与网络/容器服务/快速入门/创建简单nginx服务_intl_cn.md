本文档旨在帮助大家了解如何快速创建一个容器集群内的 nginx 服务。

## 前提条件
创建 nginx 服务的前提是您有创建好的集群。有关如何创建集群的详细信息，参见 [新建集群](https://cloud.tencent.com/document/product/457/9091) 。

## 操作步骤
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2. 单击左侧导航栏中的【服务】，在服务列表页单击【+新建】。
![](//mc.qcloudimg.com/static/img/52d71cfbf911db7a6b6d4f58548b0fe8/image.gif)
3. 填写服务的基本信息。
 - **服务名称**：要新建的服务名称，服务名称由小写字母、数字和 - 组成，且由小写字母开头，小写字母或数字结尾。本例中，服务名称为 nginx 。
 - **所在地域**：建议您根据所在地理位置选择靠近的地域。
 - **运行集群**：选择合适的集群和 Namespace 。
 - **服务描述**：服务的相关信息。该信息将显示在 **服务信息** 页面。
 ![](//mc.qcloudimg.com/static/img/abb593719ae3c4b7b3b3f79ce68b75a7/image.png)
4. 选择镜像。输入运行容器的名称，此处以 nginx 为例。单击【选择镜像】。
![](//mc.qcloudimg.com/static/img/2ecf52cd54db7b3cd44eda24f3b3a452/image.png)
单击【 DockerHub 镜像】，选择 **nginx** 。单击 【确定】。
![](//mc.qcloudimg.com/static/img/0cec90a9a793d8769d586376935bf361/image.png)
版本（Tag）： latest 。容器服务会默认使用最新版本。
![](//mc.qcloudimg.com/static/img/247064bd27464737d06d02d846c2c227/image.png)
5. 设置端口映射。将容器端口和服务端口都设置为 80 。
![](//mc.qcloudimg.com/static/img/a86f50da339892896871ab9408514433/image.png)
6. 单击【创建服务】。完成 nginx 服务的创建。
>**注意**：其他选项保持为默认设置。

## 访问 nginx 服务
1. 单击服务页面的【服务信息】查看负载均衡 ID 和负载均衡 IP 。 
![](//mc.qcloudimg.com/static/img/ce1634fd0c84c6aecfec315f3126d9d6/image.png)
2. 提供三种方式访问 nginx 服务。
 - 通过负载均衡 IP 来访问 nginx 服务。
 - 通过 **域名** 来访问 nginx 服务。
 在容器服务控制台左侧导航栏中，单击【负载均衡】，单击【TCP/UDP】，复制域名访问服务。
 ![](//mc.qcloudimg.com/static/img/23885bb932bdffb91d0a03b899429225/image.png)
 - 集群内的其他服务或容器可以直接通过服务名称访问。
3. 进入 nginx 服务器的默认欢迎页。
![](//mc.qcloudimg.com/static/img/a3cbbc5c902bd162210a4615c0955f19/image.png)

#### 更多 nginx 设置

可查看 [使用腾讯云容器服务来构建简单 web service ](https://cloud.tencent.com/community/article/223421)。
