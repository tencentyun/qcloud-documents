## 配置场景

腾讯云 CDN 支持 HTTPS 加速服务，您可以通过上传证书进行部署，也可以将已经托管至腾讯云 SSL 证书管理的证书，直接部署至 CDN 平台，启用 HTTPS 加速服务，实现全网数据加密传输。



## 配置须知

配置过程中，若您需要了解证书和密钥的格式要求以及如何补齐证书链，请参考  [HTTPS 配置须知](https://cloud.tencent.com/document/product/228/41686)  的相关内容。

## 查看配置

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在菜单栏里选择**域名管理**，单击域名右侧**管理**，即可进入域名配置页面 **Https 配置**中，查看指定域名的 HTTPS 配置情况：
![](https://main.qcloudimg.com/raw/69edff4f784c5c5bf3ec62d9c89e8185.png)
也可前往左侧菜单栏**证书管理**页面，查看账号下所有配置了 HTTPS 加速的域名列表、证书列表。

- 域名列表：展示已配置证书的域名列表。
![](https://qcloudimg.tencent-cloud.cn/raw/fd49b84c8d85c1cd789a4bd023d96ab6.jpg)
- 证书列表：展示已托管证书列表。
![](https://qcloudimg.tencent-cloud.cn/raw/2a84c321de4e72f3be53b182068b28c6.jpg)


## 证书配置
### 1. 域名配置方法

####  1.1 配置证书

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在左侧菜单栏选择**域名管理**，单击域名操作列的**管理**，进入域名配置页面，切换 Tab 至 **HTTPS 配置**，即可找到 **HTTPS 配置**。您可在此处编辑及管理该域名的证书配置。
![](https://qcloudimg.tencent-cloud.cn/raw/37f323e8a22034a992839cd5e6b7532c.png)
单击**配置证书**按钮，新增一个域名证书，新增证书可以以下三种方式：
![](https://qcloudimg.tencent-cloud.cn/raw/7ecf2c307ba1238936dda8f22830a7de.png)

|配置方法|	说明|
|--|--|
|新上传证书	|新上传证书需要您手动上传该证书的证书内容及私钥内容，请您在上传证书前准备好相关的证书内容，如需了解如何获取证书内容及私钥内容，可参考 [HTTPS 配置须知](https://cloud.tencent.com/document/product/228/41686)。|
|已托管证书|	已托管证书可选择您已托管在 [SS L证书](https://console.cloud.tencent.com/ssl) 服务内的证书文件，根据当前您配置的域名，已托管证书只显示符合当前域名的证书文件，如不存在符合的证书文件，您也可以在 SSL 证书管理页面内申请免费证书。|
|SaaS 证书	|CDN SaaS 证书功能提供域名证书的全生命周期管理服务，包括 ssl/tls 证书的批量申请、绑定、证书过期自动更新等服务，如果您当前的证书已通过 SaaS 证书功能进行管理，您可以直接选择 SaaS 证书进行关联。SaaS 证书功能介绍及使用方式可参考：[SaaS 证书](https://cloud.tencent.com/document/product/228/75135)。|

>!
>1. 您当前配置的加速域名如果在已关闭状态时，不可进行 HTTPS 证书配置；
>2. `file.myqcloud.com` 后缀为腾讯云对象存储默认加速域名，无需配置证书可直接进行 HTTPS 加速。
>3. `image.myqcloud.com` 后缀域名为腾讯云数据万象默认加速域名，无需配置证书可直接进行 HTTPS 加速服务。

#### 1.2 编辑证书

证书配置成功后，您可以在该域名的HTTPS配置页面查看该证书的状态及到期时间，也可以通过**编辑**按钮对证书进行修改，通过**删除**按钮删除该证书配置。
![](https://qcloudimg.tencent-cloud.cn/raw/de4dd82719bf51ce7d32eed741556848.png)

### 2. 证书管理下配置方法

#### 2.1 选择域名

在左侧菜单栏中，进入**证书管理** > **证书配置**，单击上方的**配置证书**，选中需要配置证书的加速域名；

>!
>- 加速域名的状态需要为“部署中”或“已启动”，关闭状态的加速域名不可进行 HTTPS 加速配置。
>- `.file.myqcloud.com`后缀为腾讯云对象存储默认加速域名，无需配置证书可直接进行 HTTPS 加速。
>- `.image.myqcloud.com`后缀域名为腾讯云数据万象默认加速域名，无需配置证书可直接进行 HTTPS 加速服务。
>
![](https://main.qcloudimg.com/raw/e5e59c614f3e7461f088e11c7353be9e.png)

#### 2.2 选择证书

若已有证书，可直接将 PEM 格式的证书内容和私钥粘贴入对应位置即可：

- 腾讯云 CDN 现已支持 ECC 证书部署。
- 证书内容需要为 PEM 格式，非此格式证书请参考 [PEM 格式转换](https://cloud.tencent.com/document/product/228/41686#.E6.A0.BC.E5.BC.8F.E8.BD.AC.E6.8D.A2)。
- 可选择腾讯云托管证书，直接进行一键部署。
![](https://qcloudimg.tencent-cloud.cn/raw/33e7ec5685282f7f0a17eb2d0edcdfa7.png)



### 3.证书管理下批量配置方法

在左侧菜单栏中，进入**证书管理** > **证书配置**，单击上方的**批量配置**，可通过上传证书，自动匹配适配的域名，进行批量配置；
![](https://qcloudimg.tencent-cloud.cn/raw/c635d26d684ff8d5cfea3c7aeff25622.png)

#### 3.1 选择证书

若已有证书，可直接将 PEM 格式的证书内容和私钥粘贴入对应位置即可：

- 腾讯云 CDN 现已支持 ECC 证书部署。
- 证书内容需要为 PEM 格式，非此格式证书请参考 [PEM 格式转换](https://cloud.tencent.com/document/product/228/41686#.E6.A0.BC.E5.BC.8F.E8.BD.AC.E6.8D.A2)。
- 可选择已托管证书，直接进行一键部署。
![](https://qcloudimg.tencent-cloud.cn/raw/e2442be6bcb13f2c60b2375f5ad89245.jpg)

#### 3.2 选择域名

根据上传 / 选择的证书，CDN 会自动匹配出允许配置的域名列表，可按需进行勾选配置：
![](https://qcloudimg.tencent-cloud.cn/raw/068cf040a9332c3139817e65905d5173.png)



## 变更证书

#### 证书修改

在左侧菜单栏中，进入**证书管理** > **证书配置**，根据需要修改的证书，单击证书右侧**编辑**，可指定域名进行证书更新，也可重新进行批量配置，覆盖原有证书配置。
![](https://qcloudimg.tencent-cloud.cn/raw/73034c0dfa7867e3afdfd3235a105a5c.jpg)
更新证书全网逐节点生效，无缝切换，不会影响现网 HTTPS 服务，也可单击**删除**，取消 HTTPS 加速服务。

## 证书过期

证书过期前30天、前15天、前7天及过期当天，腾讯云都会以短信、邮件、站内信形式向用户账号发送到期提醒。现已支持 SSL 证书自定义告警接收人，您可进入 [消息订阅](https://console.cloud.tencent.com/message/subscription) 配置。


