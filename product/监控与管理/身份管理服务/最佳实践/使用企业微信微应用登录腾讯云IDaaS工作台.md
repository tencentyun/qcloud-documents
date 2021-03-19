

使用腾讯云身份管理服务 IDaaS 与企业微信微应用集成，实现在企业微信微应用单点登录进入 IDaaS 工作台。
## 实现效果
在企业微信的微应用中打开 IDaaS 的工作台，进入 IDaaS 中的应用。
![](https://main.qcloudimg.com/raw/b20f565a7a0e342185acde3ea8168821.gif)
仅需3个步骤即可实现：
 ![](https://main.qcloudimg.com/raw/bd23d3d747d83415018ef24295550b77.png)
## 操作指南

### 创建自建应用
1. 进入企业微信管理后台（需企业微信管理员操作），进入【应用管理】>【应用】。
![](https://main.qcloudimg.com/raw/8c77831c3ec933aa33bb685a6dc04899.png)
2. 在自建栏位中单击【创建应用】。补充好 logo、应用名称、应用简介、可见范围后即可创建成功。
![](https://main.qcloudimg.com/raw/4204dce6e7f02a4e0a28620fbce4c37c.png)
3. 进入详情页，获取 AgentId 和 Secret。
 ![](https://main.qcloudimg.com/raw/74aeffd7877cb85e8242a42edd8b19c0.png)
4. 在企业微信管理后台，【我的企业】企业信息页面底部，获得企业 ID。
 ![](https://main.qcloudimg.com/raw/8a6656582d7276b5da85e867a171e567.png)
 
### 创建认证源
1.	登录 [IDaaS 控制台](https://console.cloud.tencent.com/idaas)，在认证源管理中，添加认证源选择【企业微信微应用认证】。
![](https://main.qcloudimg.com/raw/592785e72903c0b9cdd000ee9427658c.png)
2. 在详情中，将企业微信端的企业 ID、AgentId 和 Secret 填写到表单中。
![](https://main.qcloudimg.com/raw/efa4896e2a184e1a31f880bcce609996.png)
3. 创建成功后，获得企业微信授权登录回调域和应用主页地址，复制这两个地址，填写到企业微信微应用的设置中。
![](https://main.qcloudimg.com/raw/1371650e502214e477ec041a5176a225.png)
 
### 配置“应用主页”和“可信域名”
1.	设置应用主页：复制腾讯云 IDaaS 认证源详情中的“应用主页地址-目标门户地址”，填写到企业微信的“工作台应用主页”。
2.	设置可信域名：复制腾讯云 IDaaS 认证源详情中的“企业微信授权登录回调域” ，填写到企业微信的“网页授权及 JS-SDK”。
![](https://main.qcloudimg.com/raw/754acca9795881af487a542e65ee5e21.png)
设置完成后，开启该应用即可完成配置。

