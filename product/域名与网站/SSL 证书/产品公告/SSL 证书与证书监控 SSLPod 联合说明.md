为了让您有更好的体验，现提供腾讯云证书管理控制台与证书监控 SSLPod 联合集成功能，可快速帮助您检查使用 SSL 证书时的证书健康问题。
>?当您遇到问题需要咨询时，您可以直接通过 [在线客服](https://cloud.tencent.com/act/event/Online_service) 进行提问，腾讯云工程师7 × 24小时在线为您提供服务。

## 功能概述
| 模块 | 说明 | 
|---------|---------|
| 卡片式证书管理 | 卡片式证书管理帮助您更清晰的管理 SSL 证书，拥有更好的交互体验。您只需在证书管理控制台中，通过快捷的方式即可在横栏式与卡片式进行快速切换。 | 
| SSL 证书与证书监控 SSLPod 联合集成 | SSL 证书与证书监控 SSLPod 联合集成后，您可以在 SSL 证书详情页或卡片式证书详情页快速查看 SSL 证书状态与监控报告。 | 

## 使用卡片式证书管理[](id:function1)
1. 登录 [腾讯云证书管理控制台](https://console.cloud.tencent.com/ssl)，单击左侧菜单栏的**我的证书**，即可进入 “证书列表” 管理页面。
2. 在 “证书列表” 管理页面中，单击<span ><img src="https://main.qcloudimg.com/raw/9bac42e46774a5cafb865e62fc2ff9fa.png" style="margin-bottom:-4px;"/></span>即可进行切换。如下图所示：
![](https://main.qcloudimg.com/raw/4cec977e849fdfb0b6bbc34618e553c2.png)
>? 若您需切换横栏式证书管理，单击<span ><img src="https://main.qcloudimg.com/raw/ca7c290ac7c322d017675111be659b37.png" style="margin-bottom:-4px;"/></span>图标即可进行切换。

## SSL 证书与证书监控 SSLPod 联合集成[](id:function2)
1. 登录 [腾讯云证书管理控制台](https://console.cloud.tencent.com/ssl)，单击左侧菜单栏的**我的证书**，即可进入 “证书列表” 管理页面。
2. 在 “证书列表” 管理页面中，单击 证书 ID，即可进入证书详情页。
3. 您可以通过以下两个方式查看证书监控状态：
 - 证书详情页。
![](https://main.qcloudimg.com/raw/9d56e76b779719abbfaccb2b0cfc3b0b.png)
 - 卡片式的证书详情页。
![](https://main.qcloudimg.com/raw/d81ef2d63202febac2ba91feca8640c0.png)

### 证书状态说明
| 图标 | 状态说明 | 操作 |
|---------|---------|---------|
| ![](https://main.qcloudimg.com/raw/e82dae0e4c34b0af62456319f70226aa.png) | 目前该 SSL 证书状态异常 | 单击**查看监控报告**，即可跳转至健康报告页查看详情。 |
| ![](https://main.qcloudimg.com/raw/043b9f8792c40f017c78bd7d3c0e36ae.png)| 该域名目前还开启未证书监控 | 单击**免费开通**，即可快速对该证书进行监控。 |
| ![](https://main.qcloudimg.com/raw/078535ca3f663659f4014c4ed1261d76.png) | 目前该 SSL 证书状态良好 | 单击**查看监控报告**，即可跳转至健康报告页查看详情。 |
|![](https://main.qcloudimg.com/raw/9bb019a73e9b4572d5bb31b4f9b6b40e.png)| 该域名正在使用其它证书 | 单击**查看监控报告**，即可跳转至健康报告页查看详情。 |

