本文向您介绍如何将 Demo 服务（Hello World 项目）通过 Serverless 云应用进行部署。





## 步骤1：登录控制台

登录 [Serverless 云应用控制台](https://console.cloud.tencent.com/tcb/service)，再按需要切换到指定的环境。
![](https://main.qcloudimg.com/raw/7ccca44479b1c0cf092234a8e0f1ee5a.png)

> ?Serverless 云应用公测期间，需要先 [申请开通](https://cloud.tencent.com/apply/p/y5uji0g6a7p)，审核通过后，云开发控制台的左侧菜单才会出现 【Serverless 云应用】入口，否则入口将不可见。公测结束后，**Serverless 云应用**的入口将对所有云开发用户开放。



## 步骤2：新建服务

1. 在 Serverless 云应用控制台服务列表页面，单击【新建服务】。
2. 在新建服务页面配置相关选项：
	- **服务名称**：本文示例填写为“helloworld”。服务名称作为环境下服务的唯一标识，创建成功后不支持修改。
	- **备注**：展示在服务列表页面，仅您自己在控制台可见，不对部署产生任何影响。
	- **镜像仓库**：本文示例选择【使用系统默认仓库（推荐）】。服务在创建时会绑定一个腾讯云镜像仓库，后续该服务下的所有版本相关镜像，都必须存放在绑定的镜像仓库中，不支持分散在多个不同的镜像仓库。更多关于腾讯云镜像仓库的介绍，请参见 [容器镜像服务](https://cloud.tencent.com/document/product/1141)。
![](https://main.qcloudimg.com/raw/c40c181b17c5299dd699b7d5eea61c6c.jpg)
3. 单击【提交】，即可新建服务。


## 步骤3：新建版本

完成步骤2之后，系统将弹窗提示是否“新建版本”，单击【新建版本】。
![](https://main.qcloudimg.com/raw/890cc6d9e8dd0f086bec6ff3145681d8.jpg)



## 步骤4：配置版本

在新建版本窗口中，继续填写版本所需配置信息。可以通过以下两种上传方式配置版本：

#### 方式一：镜像拉取

- 上传方式：选择“镜像拉取”。
- 来源：选择“Demo”，
- 监听端口：保持默认值“80”，
- 流量策略：保持默认值“部署完成后保持流量为0，稍后手动配置流量”。
- 高级设置：保持默认值不做任何修改。
![](https://main.qcloudimg.com/raw/87a6a1e651598669cf690fbb3b76a21b.jpg)

#### 方式二：本地代码

- 上传方式：选择“本地代码”。
- 文件类型：选择“zip包”。单击【Java】或任意一种其他语言的下载链接，然后将下载的 zip 包直接上传到附件，无需对 zip 包做任何操作或修改。
- 监听端口：保持默认值“80”。
- 流量策略：保持默认值“部署完成后保持流量为0，稍后手动配置流量”。
- 高级设置：保持默认值不做任何修改。
![](https://main.qcloudimg.com/raw/6720092fbbd65e75ba1936d18057d9b7.jpg)







## 步骤3：进入“helloworld”服务详情

选择服务“helloworld”，单击服务名称进入服务详情页面。

![](https://main.qcloudimg.com/raw/252af6bc138cd26f7f109fe3ed8b5fa2.png)

## 步骤4：新建版本

单击【新建版本】
![](https://main.qcloudimg.com/raw/80be0e18962acdd5d131b08a688a544d.png)





## 步骤5：配置版本

在新建版本窗口中，继续填写版本所需配置信息。

上传方式选择“镜像拉取”，来源选择“Demo”，监听端口保持默认值“80”，流量策略保持默认值“部署完成后保持流量为0，稍后手动配置流量”，高级设置保持默认值不做任何修改。![](https://main.qcloudimg.com/raw/e85900bf0f71b48acf5e80bf14235515.png)

也可上传方式选择“本地代码”，文件类型选择“zip包”，单击【Java】或任意一种其他语言的下载链接，然后将下载的zip包直接上传到附件，无需对zip包做任何操作或修改。监听端口保持默认值“80”，流量策略保持默认值“部署完成后保持流量为0，稍后手动配置流量”，高级设置保持默认值不做任何修改。

![](https://main.qcloudimg.com/raw/f56c5dd860a22a870e88c16e94c9548d.png)



## 步骤6：开始部署

在新建版本窗口中，填写完版本配置信息后，单击【开始部署】。

版本初始为“创建中”。部署成功则状态变为“正常”。

此时流量为0%，还不能接受请求。如果单击【访问服务】会看到报错。

![](https://main.qcloudimg.com/raw/73914fd4b0e1216652d421f3e073c565.png)

## 步骤7：配置流量

单击【流量配置】。为版本“helloworld-001”配置流量100%。

单击【完成】。

![](https://main.qcloudimg.com/raw/bcc46bc970c5eeecbadf5ca006d7ab6d.png)



成功后，可以看到流量变为100%。

![](https://main.qcloudimg.com/raw/dd62fe608c1afd19bf9b7e5a696a5ebf.png)

## 步骤8：访问服务

单击【访问服务】，因流量已经配置为100%，服务已经开始处理请求，可以看到 Demo 效果。

![](https://main.qcloudimg.com/raw/60119b59be875421760bc593fdbe5b24.png)
