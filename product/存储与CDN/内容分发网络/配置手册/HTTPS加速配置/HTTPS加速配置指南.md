## 配置场景
腾讯云 CDN 支持 HTTPS 加速服务，您可以通过上传证书进行部署，也可以将已经托管至腾讯云 SSL 证书管理的证书，直接部署至 CDN 平台，启用 HTTPS 加速服务，实现全网数据加密传输。

## 配置指南
### 查看配置

登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在菜单栏里选择【域名管理】，单击域名右侧【管理】，即可进入域名配置页面【Https 配置】中，查看指定域名的 HTTPS 配置情况：
![](https://main.qcloudimg.com/raw/69edff4f784c5c5bf3ec62d9c89e8185.png)
也可前往左侧菜单栏【证书管理】页面，查看账号下所有配置了 HTTPS 加速的域名列表：
![](https://main.qcloudimg.com/raw/ee27b41bc508d85ce92b6642b167cb11.png)

### 证书配置
#### 1. 选择域名
在【证书管理】菜单栏下，单击【配置证书】，选中需要配置证书的加速域名：
+ 加速域名的状态需要为“部署中”或“已启动”，关闭状态的加速域名不可进行 HTTPS 加速配置。
+ `.file.myqcloud.com`后缀为腾讯云对象存储默认加速域名，无需配置证书可直接进行 HTTPS 加速。
+ `.image.myqcloud.com`后缀域名为腾讯云数据万象默认加速域名，无需配置证书可直接进行 HTTPS 加速服务。

![](https://main.qcloudimg.com/raw/e5e59c614f3e7461f088e11c7353be9e.png)

#### 2. 选择证书
若已有证书，可直接将 PEM 格式的证书内容和私钥粘贴入对应位置即可：
+ 腾讯云 CDN 现已支持 ECC 证书部署。
+ 证书内容需要为 PEM 格式，非此格式证书请参考 [PEM 格式转换](https://cloud.tencent.com/document/product/228/41686#.E6.A0.BC.E5.BC.8F.E8.BD.AC.E6.8D.A2)。
+ 可选择腾讯云托管证书，直接进行一键部署。

![](https://main.qcloudimg.com/raw/05bf07790a4cffc1ca98877c14767471.png)



### 批量配置
单击上方【批量配置】，可通过上传证书，自动匹配适配的域名，进行批量配置：
#### 1. 选择证书
若已有证书，可直接将 PEM 格式的证书内容和私钥粘贴入对应位置即可：
+ 腾讯云 CDN 现已支持 ECC 证书部署。
+ 证书内容需要为 PEM 格式，非此格式证书请参考 [PEM 格式转换](https://cloud.tencent.com/document/product/228/41686#.E6.A0.BC.E5.BC.8F.E8.BD.AC.E6.8D.A2)。
+ 可选择腾讯云托管证书，直接进行一键部署。

![](https://main.qcloudimg.com/raw/35bf20677f1f640c81d289d20f056ce4.png)

#### 2. 选择域名
根据上传 / 选择的证书，CDN 会自动匹配出允许配置的域名列表，可按需进行勾选配置：
![](https://main.qcloudimg.com/raw/89ad35a4fb3a5b30c0736c88bb06cf37.png)



### 变更证书
#### 证书修改
单击证书右侧【编辑】，可指定域名进行证书更新，也可重新进行批量配置，覆盖原有证书配置。
![](https://main.qcloudimg.com/raw/0156b76f7081747b9619bb171fef740d.png)
更新证书全网逐节点生效，无缝切换，不会影响现网 HTTPS 服务，也可单击【删除】，取消 HTTPS 加速服务。

#### 证书过期
证书过期前30天、前15天、前7天及过期当天，腾讯云都会以短信、邮件、站内信形式向用户账号发送到期提醒。现已支持 SSL 证书自定义告警接收人，您可进入 [消息订阅](https://console.cloud.tencent.com/message/subscription) 配置。

### 区域特殊配置
若加速域名服务区域为全球，则所配置的 HTTPS 证书会境内、境外一起生效，暂时不支持境内境外配置不同证书。

若域名存在境内、境外证书配置不一致的特殊场景，可在【证书管理】页面看到中国境内、中国境外等标识，表明该域名存在遗留的区域特殊配置：
![](https://main.qcloudimg.com/raw/23192c43c0611c34d07490f19ea7dfb0.png)
在域名【高级配置】中，也可看见两份配置：
![](https://main.qcloudimg.com/raw/febb17a67f10eb81941013895e67913f.png)


