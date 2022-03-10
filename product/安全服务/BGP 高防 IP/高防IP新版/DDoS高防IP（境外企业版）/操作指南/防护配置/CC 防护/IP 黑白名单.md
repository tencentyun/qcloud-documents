DDoS 高防  IP（境外企业版）支持通过配置 IP 黑名单和白名单，实现对访问 DDoS 高防已接入防护的网站业务封禁或者放行，从而限制访问您业务资源的用户。配置 IP 黑白名单后，当白名单中的 IP 访问时，将被直接放行，不经过任何防护策略过滤。当黑名单中的 IP 访问时，将会被直接阻断。
>?当发生 CC 攻击时，IP 黑白名单的过滤才会生效。
>- 白名单中的 IP，访问时将被直接放行，不经过任何防护策略过滤。
>- 黑名单中的 IP，访问时将会被直接阻断。


## 前提条件
您需要成功 [购买 DDoS 高防 IP（境外企业版）](https://cloud.tencent.com/document/product/1014/56255)  ，并设置防护对象。


## 操作步骤
1. 登录 [DDoS 高防 IP（境外企业版）](https://console.cloud.tencent.com/ddos/ddos-basic) 控制台 ，在左侧导航中，单击 **DDoS 高防 IP** > **防护配置** > **CC 防护**。
2. 在 CC 防护页面的左侧列表中，选中高防 IP 的 ID，如“bgp-00xxxxxx”。
![](https://qcloudimg.tencent-cloud.cn/raw/8dffdad7a2bb7a9cf45d59390c4597d1.png)
3. 在 IP 黑白名单卡片中，单击**设置**。
4. 在 IP 黑白名单列表，单击**新建**，填写相关字段。
![](https://qcloudimg.tencent-cloud.cn/raw/7e978b233c7aac61dcbc4a53cf0e681e.png)
**参数说明：**
 - 协议类型：根据实际需求选择 http 或 https。
 - 域名：该资源 IP 下的业务域名。
 - IP 名单：支持IP 或 IP 段，以 IP 或 IP/掩码的格式填写。
 - 类型：根据实际需求选择黑名单或白名单。
5. 单击**保存**，添加规则。
6. （可选）新建完成后，IP 黑白名单列表将新增一条 IP 黑白名单规则，可以在右侧操作栏中，单击**删除**，删除 IP 黑白名单规则。
![](https://qcloudimg.tencent-cloud.cn/raw/7e5d5767bb2f2a96d87348db5a3c094d.png)
