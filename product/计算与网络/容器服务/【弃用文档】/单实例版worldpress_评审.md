WordPress 是使用 PHP 语言开发的博客平台。用户可以在支持 PHP 和 MySQL 数据库的服务上架设属于自己的网站，也可以把 WordPress 当作一个内容管理系统来使用。

本文档旨在介绍如何使用 `tutum/wordpress` 镜像来创建一个公开访问的 WordPress 网站。

>**注意：**
>创建单实例版的 WordPress 仅供测试使用，该镜像中包含了 WordPress 所有的运行环境，直接拉取创建服务即可，但使用单实例版的 WordPress 不能保证数据的持久化存储，建议您使用自建的 MySQL 或使用腾讯云数据库 CDB 来保存您的数据。详情请参考 [使用 CDB 的 WordPress](/doc/product/457/7447)。 在创建 WordPress 服务之前，您必须拥有:
1. 一个腾讯云帐户。有关如何创建腾讯云帐户，请在 [注册页面](https://cloud.tencent.com/register) 填写相关信息注册腾讯云帐户。
2. 一个创建好的集群。有关如何创建集群的详细信息，参见 [新建集群](https://cloud.tencent.com/document/product/457/9091) 。


## 创建 WordPress 服务
1) 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/ccs) 。
2) 单击左侧导航栏中的**服务**，单击服务列表页的**+ 新建**。
![](//mc.qcloudimg.com/static/img/11f7f75d7b051a815da8bfe1e744a8e8/image.png)
3) 设置服务的基本信息。
 - **服务名称**：要创建的服务的名称。服务名称由小写字母、数字和 - 组成，且由小写字母开头，小写字母或数字结尾。
 - **所在地域**：建议您根据所在地理位置选择靠近的地域。
 - **运行集群**：选择服务所要运行的集群。运行集群需要选择运行中和集群内有可用主机的集群。
 - **服务描述**：创建服务的相关信息。该信息将显示在 **服务信息** 页面。
![](//mc.qcloudimg.com/static/img/9254649a08d86761bcb8287fe5a45141/image.png)

4) 镜像配置。
 - **名称**：输入运行容器的名称，此处以 wordpress 为例。
 - **镜像**：填写 `tutum/wordpress` 。
 - **版本（Tag）**：填写 latest。
![](//mc.qcloudimg.com/static/img/b5c035081625c15a1dcbdf0a3cabf6a7/image.png)

5) 设置端口映射。将容器端口和服务端口都设置为 80 。
>**注意**：服务所在集群的安全组需要放通节点网络及容器网络，同时需要放通30000-32768端口，否则可能会出现容器服务无法使用问题。详情参见[容器服务安全组设置](https://cloud.tencent.com/document/product/457/9084)

![](//mc.qcloudimg.com/static/img/a86f50da339892896871ab9408514433/image.png)

6) 单击 **创建服务**。完成 WordPress 服务的创建。
>**注意**：其他选项保持为默认设置。

## 访问 WordPress 服务
1) 提供三种方式访问 WordPress 服务。
 - 通过**负载均衡 IP**来访问 WordPress 服务。单击服务页面的**服务信息**查看负载均衡 IP和负载均衡ID。 
![](//mc.qcloudimg.com/static/img/f92f30a3360c46ac0e6e76d045f4484f/image.png) 
 - 通过 **域名** 来访问 WordPress 服务。在容器服务控制台左侧导航栏中，单击**负载均衡**，单击**TCP/UDP**，找到对应的负载均衡ID，复制域名访问服务。
 - 集群内的其他服务或容器可以直接通过服务名称访问。
 
2) 进入 WordPress 服务器的默认欢迎页。
![Alt text](https://mc.qcloudimg.com/static/img/c0132b35996db099c02af7f2cf747137/Image+023.png)

若容器创建失败，可查看[事件常见问题](https://cloud.tencent.com/document/product/457/8187)。