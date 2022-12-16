
## 操作场景
本任务指导您为云原生 API 网关 Kong 添加 SSL 证书。

## 操作前提
1. 已经完成域名注册、实名认证、备案等流程，若您尚未完成，可以使用腾讯云提供的域名服务，[查看指引](https://cloud.tencent.com/document/product/242/39039)。
2. 已经拥有 SSL 证书，若您暂无证书，可以使用腾讯云提供的证书服务，[查看指引](https://cloud.tencent.com/document/product/400/43473)。

## 操作步骤
### 步骤1：配置 DNS 解析
1. 前往 [TSE 控制台](https://console.cloud.tencent.com/tse/kong)，获取 Kong 公网代理地址中的 IP。
![](https://qcloudimg.tencent-cloud.cn/raw/09caa29755ff71ea9ff2f67d4cbb6b96.jpg)
2. 根据 [快速添加域名解析](https://cloud.tencent.com/document/product/302/3446) 指引，将您的域名解析至 Kong 公网代理地址中的 IP。

### 步骤2：在 Konga 安装证书
1. 以腾讯云证书服务为例，登录 [SSL 证书控制台](https://console.cloud.tencent.com/ssl)，进入 “我的证书” 管理页面。
2. 选择您需要安装的证书，单击操作栏的下载。
![](https://qcloudimg.tencent-cloud.cn/raw/73b8b2890aa2b8db9f5f88774af95ef7.jpg)
3. 在下载对话框，选择**其他**进行下载。
![](https://qcloudimg.tencent-cloud.cn/raw/d9969a1bcc86b3ab6c1bc3785efb337c.jpg)
4. 在 [TSE 控制台](https://console.cloud.tencent.com/tse/kong)的**实例详情页** > **配置管理**，获取 Konga 控制台地址与访问方式。
![](https://qcloudimg.tencent-cloud.cn/raw/a22a05e28a215030c743c73e38f570bd.jpg)
5. 进入 Konga 控制台，单击侧边导航栏的 **CERTIFICATES**。
![](https://qcloudimg.tencent-cloud.cn/raw/b875fa07dab2047f06bd0ff641c5c476.png)
>? 若您初次登录管理控制台，需要激活 Connection，[查看指引](https://cloud.tencent.com/document/product/1364/72496)。
6. 单击 **ADD CERTIFICATE**。
![](https://qcloudimg.tencent-cloud.cn/raw/8f39eec4a0aeb46208d9f47088c665e8.png)
7. 填写 Certificate、Key，并填写您的域名到 Server Name Indications 中，单击 SUBMIT CERTIFICATES 提交。
>? Certificate 使用以 `.crt` 为后缀的文件；Key 使用以 `.key` 为后缀的文件。
>
![](https://qcloudimg.tencent-cloud.cn/raw/03165b3cf88d332149517e3c041bae97.jpg)
8. 查看安装好的证书。
![](https://qcloudimg.tencent-cloud.cn/raw/1fcc5f5ac8ee13421bc5c7be29c8361f.jpg)

### 步骤3：验证证书是否生效
访问 `https://域名` 验证是否生效。
