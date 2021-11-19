
## 准备工作

[开通 CloudBase 云托管](https://docs.cloudbase.net/run/activation.html)


## 步骤1：新建服务
1. 登录 [CloudBase 云托管控制台](https://console.cloud.tencent.com/tcb/service)，切换到指定的环境，单击**新建服务**。
![](https://main.qcloudimg.com/raw/c40c181b17c5299dd699b7d5eea61c6c.jpg)
2. 在新建服务页面配置相关选项：
	- 服务名称：本文示例填写为“helloworld”。服务名称作为环境下服务的唯一标识，创建成功后不支持修改。
	- 镜像仓库：本文示例选择**使用系统默认仓库（推荐）**。
>?云托管服务在创建时，会绑定一个腾讯云镜像仓库，后续该服务下的所有版本相关镜像，都必须存放在绑定的镜像仓库中。更多关于腾讯云镜像仓库的介绍，请参见 [容器镜像服务](https://cloud.tencent.com/document/product/1141)。
3. 单击**提交**，即可新建服务。

## 步骤2：新建、配置版本
1. 完成上述步骤1后，系统将提示新建版本：
![](https://main.qcloudimg.com/raw/890cc6d9e8dd0f086bec6ff3145681d8.jpg)
2. 单击**新建版本**。
	- 上传方式：选择**镜像拉取**；
	- 来源：选择**Demo**；
	- 监听端口：保持默认值**80**；
	- 流量策略：保持默认值**部署完成后保持流量为0，稍后手动配置流量**。
3. 随后单击**开始部署**，在控制台将看到版本状态初始为**创建中**，部署成功则状态变为**正常**。
>?此时流量为0%，还无法接受请求。如果单击**访问服务**，将提示错误。

## 步骤3：配置流量

1. 单击「流量配置」，将版本“helloworld-001”配置流量100%：
![](https://main.qcloudimg.com/raw/0473dc788cae472b85f18e8f45575206.jpg)
2. 成功后，可以看到流量变为100%：
![](https://main.qcloudimg.com/raw/419e5070e9a1a1b47b433fb70bb710b0.png)


## 访问您的服务
单击**访问服务**，因流量已经配置为100%，服务已经开始处理请求，可以看到 Demo 效果：
![](https://main.qcloudimg.com/raw/60119b59be875421760bc593fdbe5b24.png)

