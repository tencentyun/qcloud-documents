DDoS 高防支持通过配置 IP 黑名单和白名单，实现对访问 DDoS 高防已接入防护的网站业务封禁或者放行，从而限制访问您业务资源的用户。配置 IP 黑白名单后，当白名单中的 IP 访问时，将被直接放行，不经过任何防护策略过滤。当黑名单中的 IP 访问时，将会被直接阻断。
>?
>- 轻量应用服务器（Lighthouse）定制版不支持 DDoS 防护、CC 防护的自定义防护配置。
>- 当发生 CC 攻击时，IP 黑白名单的过滤才会生效。
>  - 白名单中的 IP，访问时将被直接放行，不经过任何防护策略过滤。
>  - 黑名单中的 IP，访问时将会被直接阻断。


## 前提条件
您需要成功 [购买 DDoS 高防包](https://cloud.tencent.com/document/product/1021/43894) ，并设置防护对象。


## 操作步骤
1. 登录 [DDoS 高防包（新版）管理控制台](https://console.cloud.tencent.com/ddos/antiddos-native/package)，在左侧导航中，选择**防护配置** > **CC 防护**。
2. 在 CC 防护页面的左侧列表中，选中高防包的 ID，如“bgp-00xxxxxx”。
![](https://qcloudimg.tencent-cloud.cn/raw/87a4773836c1e230b9b742325f35270c.png)
3. 在右侧 IP 黑白名单卡片中，单击**设置**，进入 IP 黑白名单列表。
![](https://qcloudimg.tencent-cloud.cn/raw/f178836ceec3cd9604e3eaae0d850f56.png)
4. 在 IP 黑白名单列表，单击**新建**，填写相关字段，填写完成后，单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/d8cd6ff611f7c68cf36db6f6c10711d9.png)
5. 新建完成后，IP 黑白名单列表将新增一条 IP 黑白名单规则，可以在右侧操作栏中，单击**删除**，删除 IP 黑白名单规则。
![](https://qcloudimg.tencent-cloud.cn/raw/3d862f49ef067b0516dd1cb4dbe47798.png)
