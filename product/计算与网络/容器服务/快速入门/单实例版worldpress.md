## 操作场景
WordPress 是使用 PHP 语言开发的博客平台。用户可以在支持 PHP 和 MySQL 数据库的服务上架设属于自己的网站，也可以把 WordPress 当作一个内容管理系统来使用。
本文以 [原 TKE 控制台](https://console.cloud.tencent.com/tke) 为例进行操作，使用 `tutum/wordpress` 镜像创建一个公开访问的 WordPress 网站。


## 前提条件
>!
>- `tutm/wordpress` 该镜像中包含了 WordPress 所有的运行环境，直接拉取创建服务即可。
>- 创建单实例版的 WordPress 仅供测试使用，不能保证数据的持久化存储。建议您使用自建的 MySQL 或使用腾讯云数据库 TencentDB 来保存您的数据，详情请见 [使用 TencentDB 的 WordPress](/doc/product/457/7447)。 
>
- 已 [注册腾讯云账户](https://cloud.tencent.com/register)。
- 已创建集群。有关创建集群，详情请参见 [创建集群](https://cloud.tencent.com/document/product/457/9091#.E5.88.9B.E5.BB.BA.E9.9B.86.E7.BE.A4) 。

## 操作步骤
### 创建 WordPress 服务
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke) 。
2. 单击左侧导航栏中的【服务】，选择服务列表页的【新建】。如下图所示：
![](https://main.qcloudimg.com/raw/2aad4d77b314aa3bbfc1ecd741203776.png)
3. 设置服务的基本信息。如下图所示：
   - **服务名称**：要创建的服务的名称。服务名称由小写字母、数字和 - 组成，且由小写字母开头，小写字母或数字结尾。本例中服务名称为 wordpress。
   - **所在地域**：选择运行该服务集群所在的地域。
   - **运行集群**：选择服务所要运行的集群，选择运行中和集群内有可用主机的集群。
   - **服务描述**：创建服务的相关信息。该信息将显示在 **服务信息** 页面。
>!其他选项保持为默认设置。

![](https://main.qcloudimg.com/raw/24cc9024e48e1dc247a0d5531324d54a.png)
4. 根据以下参数信息进行镜像配置。如下图所示：
   - **名称**：输入运行容器的名称，以 wordpress 为例。
   - **镜像**：输入 `tutum/wordpress` 。
   - **版本（Tag）**：输入 latest。
![](https://main.qcloudimg.com/raw/732f3be423585e6a5a9009cdb43d8e95.png)
5. 设置端口映射，将容器端口和服务端口都设置为80 。如下图所示：
>!服务所在集群的安全组需要放通节点网络及容器网络，同时需要放通30000-32768端口，否则可能会出现容器服务无法使用问题。详情参见 [容器服务安全组设置](https://cloud.tencent.com/document/product/457/9084)。
>
 ![](https://mc.qcloudimg.com/static/img/a86f50da339892896871ab9408514433/image.png)
6. 单击**创建服务**，即可完成 WordPress 服务的创建。


###  访问 WordPress 服务
可通过以下三种方式访问 WordPress 服务。
#### 通过负载均衡 IP 来访问 WordPress 服务
1. 进入集群 [服务列表](https://console.cloud.tencent.com/tke/service/detail/container) 页。
2. 单击【服务信息】查看负载均衡 IP。如下图所示：
![](https://main.qcloudimg.com/raw/829059210ef222e0c5fefdae70c6b097.png)
3. 在浏览器地址栏输入负载均衡 IP，按 “Enter” 即可访问服务。


#### 通过**域名**来访问 WordPress 服务
1.进入服务信息详情页，单击服务的负载均衡 ID。如下图所示：
![](https://main.qcloudimg.com/raw/0c2a9347c4b495d631aa0950b5673453.png)
2. 进入负载均衡详情页，查看域名。如下图所示：
![](https://main.qcloudimg.com/raw/b00fc781aa59c8435bf7d203b602e677.png)
3. 在浏览器地址栏输入该域名，按 “**Esc**” 即可访问服务

#### 通过服务名称访问服务
集群内的其他服务或容器可以直接通过服务名称访问。

### 验证 WordPress 服务
服务创建成功，访问服务时直接进入 WordPress 服务器的配置页。如下图所示：
![](https://main.qcloudimg.com/raw/4ccbffc42a7f9381e2595175ea32be65.png)

若容器创建失败，可查看 [事件常见问题](https://cloud.tencent.com/document/product/457/8187)。

