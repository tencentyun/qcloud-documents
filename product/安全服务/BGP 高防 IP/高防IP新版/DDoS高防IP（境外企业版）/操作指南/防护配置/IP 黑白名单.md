DDoS 高防 IP （境外企业版）支持通过配置 IP 黑名单和白名单实现对访问 DDoS 高防 IP （境外企业版）的源 IP 封禁或者放行，从而限制访问您业务资源的用户。配置 IP 黑白名单后，当流量超过清洗阈值时，若白名单中的 IP 进行访问，将被直接放行，不经过任何防护策略过滤。若黑名单中的 IP 进行访问，将会被直接阻断。

## 前提条件
- 您需要成功 [购买 DDoS 高防 IP （境外企业版）](https://cloud.tencent.com/document/product/1014/56255) ，并设置防护对象。
>?当发生 DDoS 攻击时，IP 黑白名单的过滤才会生效。
>- 白名单中的 IP，访问时将被直接放行，不经过任何防护策略过滤。
>- 黑名单中的 IP，访问时将会被直接阻断。


## 操作步骤
1. 登录 [DDoS 高防 IP（境外企业版）](https://console.cloud.tencent.com/ddos/antiddos-advanced/config/port) 控制台 ，在左侧导航中，单击 **DDOS 高防 IP** > **防护配置** > **DDoS 防护**。
2.	在左边的列表选中高防 IP 的 ID，如“xxx.xx.xx.xx bgpip-000003n2”。
![](https://qcloudimg.tencent-cloud.cn/raw/8522d4bfe3d8ebcc14c11a6403ab22d6.png)
3. 在 IP 黑白名单卡片中，单击**设置**。
4. 在 IP 黑白名单列表中，单击**新建**，选择类型并输入 IP，单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/2391345f7c2c4e4b72a8cc4e01482da9.png)
6. 新建完成后，IP 黑白名单列表将新增一条 IP 黑白名单规则，可以在右侧操作列，单击**删除**，删除 IP 黑白名单规则。
![](https://qcloudimg.tencent-cloud.cn/raw/8b41c23c24dce20eaedff68bf9f4bceb.png)
