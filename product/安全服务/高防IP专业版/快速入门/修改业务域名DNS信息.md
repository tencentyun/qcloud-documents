使用高防 IP 专业版防护前，需要将业务域名 DNS 的 CNAME 记录修改为高防 IP 专业版实例的 CNAME，使所有用户访问网站的流量都先经过高防 IP 再回到源站（即先将所有流量都牵引到高防 IP 再回到源站）。
>?各个 DNS 解析提供商的配置原理相同，具体配置步骤可能有细微差别，本文以使用腾讯云域名解析产品为例。
## 前提条件
在修改业务域名 DNS 信息前，您需要成功购买域名解析产品，如 [云解析](https://cloud.tencent.com/document/product/302/2589)。
## 操作步骤
1.	登录 [腾讯云控制台](https://console.cloud.tencent.com)，选择【云产品】>【域名与网站】>【云解析】，在【域名解析列表】中，单击目标域名所在行的【解析】，进入域名记录管理界面。
![](https://main.qcloudimg.com/raw/c3f533833140fba7d808a87d39b4c9ae.png)
2. 在域名记录管理界面，单击【添加记录】，添加需要解析的 CNAME 记录。
![](https://main.qcloudimg.com/raw/37562512d1068c4a751f15f4fc33627d.png)
