边界防护支持通过配置 IP 黑名单和白名单，实现对访问边界的源 IP 封禁或者放行，从而限制访问您业务资源的用户。配置 IP 黑白名单后，当流量超过清洗阈值时，若是白名单中的 IP 进行访问，将被直接放行，不需要经过任何的防护策略；若是黑名单中的 IP 进行访问，将会被直接阻断。

## 前提条件
您需要成功[ 购买边界防护](https://cloud.tencent.com/document/product/1014/60842)，并设置防护对象。
>?
>- 当发生 DDoS 攻击时，IP 黑白名单的过滤才会生效。
>   - 白名单中的 IP，访问时将被直接放行，不经过任何防护策略过滤。
>   -	黑名单中的 IP，访问时将会被直接阻断。

## 操作步骤
1. 登录 [边界防护管理控制台](https://console.cloud.tencent.com/ddos/antiddos-edge/policy/ddos) ，在左侧导航中，单击**防护策略**，并选择 **DDoS 防护**。
2. 在左边的列表选中实例的 ID，如“edge-xxxxxxx”。
![](https://main.qcloudimg.com/raw/e854c4c6423ee81d80ed7b964ac26df1.png)
3. 在右侧卡片中单击“IP 黑白名单”卡片中的**设置**，进入IP 黑白名单页面。
![](https://main.qcloudimg.com/raw/93c2fc39330b593470b21e0e3bca2da9.png)
4. 在 IP 黑白名单页面中，单击**新建**。
![](https://main.qcloudimg.com/raw/a04dd1610c7610bdbe495cda14dc9fa0.png)
5. 在新建 IP 黑白名单弹窗中，创建 IP 黑白名单规则，选择黑白名单类型，单击**确定**。
![](https://main.qcloudimg.com/raw/f57e24d63759642d2d38d388c08f76bc.png)
6. 新建完成后，IP 黑白名单列表将新增一条 IP 黑白名单规则，可以在右侧操作列，单击**删除**，删除 IP 黑白名单规则。
![](https://main.qcloudimg.com/raw/75911e8b50e5a2810dc66f22fd9e7132.png)
