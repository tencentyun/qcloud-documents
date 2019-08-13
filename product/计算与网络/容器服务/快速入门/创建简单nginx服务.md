## 操作场景
本文以 [原TKE控制台](https://console.cloud.tencent.com/tke) 为例进行操作，快速创建一个容器集群内的 nginx 服务。

## 前提条件
- 已 [注册腾讯云账户](https://cloud.tencent.com/register)。
- 已创建集群。关于创建集群，详情请参见 [创建集群](https://cloud.tencent.com/document/product/457/9091#.E5.88.9B.E5.BB.BA.E9.9B.86.E7.BE.A4) 。


## 操作步骤
### 创建 Nginx 服务
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke) 。
2. 单击左侧导航栏中的【服务】，选择服务列表页上方的【新建】。如下图所示：
![](https://main.qcloudimg.com/raw/36688cf67af80f32cdeb531e7f6d1919.png)
3. 设置服务的基本信息。如下图所示：
 - **服务名称**：要创建的服务的名称。服务名称由小写字母、数字和 - 组成。且由小写字母开头，小写字母或数字结尾。本例中服务名称为 nginx 。
 - **所在地域**：选择运行该服务集群所在的地域。
 - **运行集群**：选择服务所要运行的集群，选择运行中及该集群内有可用主机的集群。
 - **服务描述**：创建服务的相关信息。该信息将显示在**服务信息**页面。
  >!其他选项保持为默认设置。
  >
![](https://main.qcloudimg.com/raw/761d51aba410392296168a9bf2974379.png)

4. 选择镜像。输入运行容器的名称（以 nginx 为例）后，单击【选择镜像】。如下图所示：
![](https://main.qcloudimg.com/raw/8248aa5497093d1b8744f5ea5526c0b5.png)
在弹出对话框中，选择【DockerHub 镜像】> **nginx** ，单击 【确定】。如下图所示：
![](https://mc.qcloudimg.com/static/img/0cec90a9a793d8769d586376935bf361/image.png)
**版本（Tag）**： latest 。容器服务会默认使用最新版本。如下图所示：
![](https://main.qcloudimg.com/raw/76d962e9b89d64bd4fc9ad6662f46ee6.png)
5. 设置端口映射，将容器端口和服务端口都设置为80 。如下图所示：
>!服务所在集群的安全组需要放通节点网络及容器网络，同时需要放通30000 - 32768端口，否则可能会出现容器服务无法使用问题。详情参见 [容器服务安全组设置](https://cloud.tencent.com/document/product/457/9084)。
>
![](https://mc.qcloudimg.com/static/img/a86f50da339892896871ab9408514433/image.png)
6. 单击【创建服务】，即可完成 nginx 服务的创建。


### 访问 Nginx 服务
可通过以下三种方式访问 nginx 服务。
#### 通过负载均衡 IP 访问 Nginx 服务
1. 进入集群 [服务列表](https://console.cloud.tencent.com/tke/service/detail/container) 页。
2. 单击【服务信息】进入服务信息详情页，查看负载均衡 IP 和负载均衡 ID。 如下图所示：
![](https://main.qcloudimg.com/raw/4700a84b57f61bfc97b5622b743cd6a6.png)
3. 在浏览器地址栏输入负载均衡 IP，按 “**Enter**” 即可访问服务。

#### 通过域名访问 Nginx 服务
1. 进入服务信息详情页，单击服务的负载均衡 ID。如下图所示：
![](https://main.qcloudimg.com/raw/b7c9497dc573613d963a6c8b097c9e6c.png)
2. 进入负载均衡详情页，查看域名。如下图所示：
![](https://main.qcloudimg.com/raw/20cf06e2cbf2a2d12e3e318c59031020.png)
3. 在浏览器地址栏输入该域名，按 “**Enter**” 即可访问服务。

#### 通过服务名称访问 Nginx 服务
集群内的其他服务或容器可以直接通过服务名称访问。

### 验证 Nginx 服务
服务创建成功，访问服务时直接进入 nginx 服务器的默认欢迎页。如下图所示：
![](https://mc.qcloudimg.com/static/img/a3cbbc5c902bd162210a4615c0955f19/image.png)

### 更多 Nginx 设置
- 可查看 [使用腾讯云容器服务来构建简单 web service ](https://cloud.tencent.com/community/article/223421)。
- 若容器创建失败，可查看 [事件常见问题](https://cloud.tencent.com/document/product/457/8187)。
