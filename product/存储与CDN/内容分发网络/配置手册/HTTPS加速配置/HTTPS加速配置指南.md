## 配置场景

腾讯云 CDN 支持 HTTPS 加速服务，您可以通过上传证书进行部署，也可以将已经托管至腾讯云 SSL 证书管理的证书，直接部署至 CDN 平台，启用 HTTPS 加速服务，实现全网数据加密传输。


## 查看配置

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在菜单栏里选择**域名管理**，单击域名右侧**管理**，即可进入域名配置页面 **Https 配置**中，查看指定域名的 HTTPS 配置情况：
![](https://qcloudimg.tencent-cloud.cn/raw/c961650e935ea12ce99f7beefda575ab.png)
![](https://qcloudimg.tencent-cloud.cn/raw/9714c03124ab9e6487bce2273bad289b.png)
也可前往左侧菜单栏**证书管理**页面，查看账号下所有配置了 HTTPS 加速的域名列表。
- 证书列表：展示已托管证书列表。
![](https://qcloudimg.tencent-cloud.cn/raw/b061c0f41f4c07320c4a9d6fd596f1a4.png)


## 证书配置
### 1. 域名配置方法

####  1.1 确认开启HTTPS服务

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在左侧菜单栏选择**域名管理**，单击域名操作列的**管理**，进入域名配置页面，切换至 **HTTPS 配置**。
![](https://qcloudimg.tencent-cloud.cn/raw/d50bb12dfb27e0a5334260d9773c6ce3.png)
确认是否开启 HTTPS 服务，开启后 CDN 域名加速产生的 HTTPS 请求数将独立计费，[HTTPS 请求计费规则](https://cloud.tencent.com/document/product/228/75563)。
![](https://qcloudimg.tencent-cloud.cn/raw/2cae4bfcda457e2ccc9871ee9a1e8dca.png)


#### 1.2 配置证书
单击**配置证书**按钮，新增一个域名证书，新增证书可以以下两种方式：
![](https://qcloudimg.tencent-cloud.cn/raw/060ab1c77291449352dcc6cb0a03d660.png)

|配置方法|	说明|
|--|--|
|新上传证书	|新上传证书需要您手动上传该证书的证书内容及私钥内容，请您在上传证书前准备好相关的证书内容，如需了解如何获取证书内容及私钥内容，可参考 [HTTPS 配置须知](https://cloud.tencent.com/document/product/228/41686)。|
|已托管证书|	已托管证书可选择您已托管在 [SSL 证书](https://console.cloud.tencent.com/ssl) 服务内的证书文件，根据当前您配置的域名，已托管证书只显示符合当前域名的证书文件，如不存在符合的证书文件，您也可以在 SSL 证书管理页面内申请免费证书。|


>!
>1. 您当前配置的加速域名如果在已关闭状态时，不可进行 HTTPS 证书配置；
>2. `file.myqcloud.com` 后缀为腾讯云对象存储默认加速域名，无需配置证书可直接进行 HTTPS 加速。
>3. `image.myqcloud.com` 后缀域名为腾讯云数据万象默认加速域名，无需配置证书可直接进行 HTTPS 加速服务。

#### 1.3 编辑证书

证书配置成功后，您可以在该域名的HTTPS配置页面查看该证书的状态及到期时间，也可以通过**更新**按钮对证书进行修改，通过**删除**按钮删除该证书配置。
![](https://qcloudimg.tencent-cloud.cn/raw/e787406a8161d053b51d3a553222b693.png)

### 2. 证书管理下配置方法

#### 2.1 选择域名

在控制台左侧菜单栏中，进入**证书管理**，单击上方的**配置证书**，选中需要配置证书的加速域名；
![](https://qcloudimg.tencent-cloud.cn/raw/93779aa5d849b468927b96a3362a3834.png)

>!
>- 加速域名的状态需要为“部署中”或“已启动”，关闭状态的加速域名不可进行 HTTPS 加速配置。
>- `.file.myqcloud.com`后缀为腾讯云对象存储默认加速域名，无需配置证书可直接进行 HTTPS 加速。
>- `.image.myqcloud.com`后缀域名为腾讯云数据万象默认加速域名，无需配置证书可直接进行 HTTPS 加速服务。
>


#### 2.2 选择证书

若已有证书，可直接将 PEM 格式的证书内容和私钥粘贴入对应位置即可：

- 腾讯云 CDN 现已支持 ECC 证书部署。
- 证书内容需要为 PEM 格式，非此格式证书请参考 [PEM 格式转换](https://cloud.tencent.com/document/product/228/41686#.E6.A0.BC.E5.BC.8F.E8.BD.AC.E6.8D.A2)。
- 可选择腾讯云托管证书，直接进行一键部署。
![](https://qcloudimg.tencent-cloud.cn/raw/bb63e8c5e365db04962e1c40165a7a65.png)



### 3. 证书管理下批量配置方法

在左侧菜单栏中，进入**证书管理** > **证书配置**，单击上方的**批量配置**，可通过上传证书，自动匹配适配的域名，进行批量配置；
![](https://qcloudimg.tencent-cloud.cn/raw/d9c66001eaca2df106c33be44b5ff4c0.png)

#### 3.1 选择证书

若已有证书，可直接将 PEM 格式的证书内容和私钥粘贴入对应位置即可：

- 腾讯云 CDN 现已支持 ECC 证书部署。
- 证书内容需要为 PEM 格式，非此格式证书请参考 [PEM 格式转换](https://cloud.tencent.com/document/product/228/41686#.E6.A0.BC.E5.BC.8F.E8.BD.AC.E6.8D.A2)。
- 可选择已托管证书，直接进行一键部署。
![](https://qcloudimg.tencent-cloud.cn/raw/8e8e80b77e82e3b50f7a2705f4d8b4cb.png)

#### 3.2 选择域名

根据上传 / 选择的证书，CDN 会自动匹配出允许配置的域名列表，可按需进行勾选配置：
![](https://qcloudimg.tencent-cloud.cn/raw/d36fe660a1a1ee86d802adcb77b95bc4.png)



## 变更证书

#### 证书修改

在控制台左侧菜单栏中，进入**证书管理**，根据需要修改的证书，单击证书右侧**更新**，可指定域名进行证书更新，也可重新进行批量配置，覆盖原有证书配置。
![](https://qcloudimg.tencent-cloud.cn/raw/0b06c2da9e46fc4815c669d448bd7886.png)
更新证书全网逐节点生效，无缝切换，不会影响现网 HTTPS 服务，也可单击**删除**，取消 HTTPS 加速服务。

## 证书过期

证书过期前29天、前15天、前7天及过期当天，腾讯云都会以短信、邮件、站内信形式向用户账号发送到期提醒。现已支持 SSL 证书自定义告警接收人，您可进入 [消息订阅](https://console.cloud.tencent.com/message/subscription) 配置。


