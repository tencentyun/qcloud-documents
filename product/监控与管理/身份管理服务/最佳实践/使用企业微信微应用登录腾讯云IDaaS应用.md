

使用腾讯云身份管理服务 IDaaS 与企业微信微应用集成，实现在企业微信微应用单点登录进入 IDaaS 应用。
## 实现效果
在企业微信的微应用中打开 IDaaS 的工作台，单击微应用直接进入 IDaaS 中的应用。
![](https://main.qcloudimg.com/raw/2cf43a93f06a60370813ffb5393f36a2.gif)
仅需4个步骤即可实现：
![](https://main.qcloudimg.com/raw/2380966375fc32f2472f4b16a5f3db45.png)
 
## 实现步骤
### 添加 IDaaS 应用
在 IDaaS 中已创建好一个应用。如腾讯云控制台，并获得其应用 ID：421262****，创建步骤详见 [创建应用](https://cloud.tencent.com/document/product/1106/36360)。
 ![](https://main.qcloudimg.com/raw/738f11c8d9654f588034713f0583f120.png)

### 创建自建应用
1.	进入企业微信管理后台（需企业微信管理员操作），进入【应用管理】>【应用】。
![](https://main.qcloudimg.com/raw/fe059a5917b177c104f296cca2368136.png)
2.	在自建栏位中单击【创建应用】。补充好 logo、应用名称、应用简介、可见范围后即可创建成功。
![](https://main.qcloudimg.com/raw/5de6555baf3371368b5f1e77f9f851e6.png)
3.	进入详情页，获取 AgentId 和 Secret。
![](https://main.qcloudimg.com/raw/ebf0aa30f40837a3c22c64f1d0ecb4b2.png)
4.	在企业微信管理后台，【我的企业】企业信息页面底部，获得企业 ID。
![](https://main.qcloudimg.com/raw/24c40dfc273d0238bf3918cf00d8799a.png)

### 创建认证源
1.	登录 [IDaaS 控制台](https://console.cloud.tencent.com/idaas)，在认证源管理中，添加认证源选择【企业微信微应用认证】。
![](https://main.qcloudimg.com/raw/89c647cb143170627e324382491fa8eb.png)
2.	在详情中，将企业微信端的企业 ID、AgentId 和 Secret 填写到表单中。
![](https://main.qcloudimg.com/raw/7b24fb102d2d6156ff97f61e570f893d.png)
3.	创建成功后，获得企业微信授权登录回调域和应用主页地址。
复制目标应用地址 url，并将“<此位置替换为跳转目标 IDaaS 应用 ID>”替换为要访问的应用 ID，如
```html
https://open.weixin.qq.com/connect/oauth2/authorize?appid=ww01a04ace0ad7af0e&redirect_uri=https%3A%2F%2Fbanhuatian.cloudidaas.com%2Fidp%2Fwxwork-app%2Fcallback%3Fidp_id%3D4470%26idaas_app_id%3D<此位置替换为跳转目标 IDaaS 应用 ID>&response_type=code&scope=snsapi_base#wechat_redirect
```
替换为
```html
https://open.weixin.qq.com/connect/oauth2/authorize?appid=ww01a04ace0ad7af0e&redirect_uri=https%3A%2F%2Fbanhuatian.cloudidaas.com%2Fidp%2Fwxwork-app%2Fcallback%3Fidp_id%3D4470%26idaas_app_id%3D421262bc1cd3&response_type=code&scope=snsapi_base#wechat_redirect
```
复制“企业微信授权登录回调域”和替换应用ID后的“目标应用地址”，填写到企业微信微应用的设置中。
![](https://main.qcloudimg.com/raw/af1b903fae98302af4cbf579ecb3e849.png)
 
### 配置“应用主页”和“可信域名”
1.	设置应用主页：复制腾讯云 IDaaS 认证源详情中的替换应用 ID 后的“目标应用地址”，填写到企业微信的“工作台应用主页”。
2.	设置可信域名：复制腾讯云 IDaaS 认证源详情中的“企业微信授权登录回调域” ，填写到企业微信的“网页授权及 JS-SDK”。
![](https://main.qcloudimg.com/raw/23f7ca7cea31a086a498a09bd3bf9ecd.png)
设置完成后，开启该应用即可完成配置。

