开启智能防护后，AI 智能防护基于腾讯云的大数据能力，能够自主学习网站业务流量基线，结合算法分析攻击异常，并自动下发精确的防护规则，动态调整业务防护模型，帮助您及时发现并阻断恶意攻击。

## 前提条件
- 您需要成功 [购买 DDoS 高防包](https://cloud.tencent.com/document/product/1021/43894)，并设置防护对象。
- 智能 CC 防护当前仅支持域名接入的规则生效。

## 操作步骤
1.	登录 [DDoS 高防包（新版）管理控制台](https://console.cloud.tencent.com/ddos/antiddos-native/config/web)，在左侧导航中，单击**防护配置** > **CC 防护**。
2.	在 CC 防护页面的左侧列表中，选中高防包的 ID，如“bgp-00xxxxxx”。
![](https://qcloudimg.tencent-cloud.cn/raw/ccb38f5389e75aee5258221672d146a5.png)
3. 在 CC 防护开关及清洗阈值卡片中，单击![](https://qcloudimg.tencent-cloud.cn/raw/9795d7ce17dc03f5be0daae4ef488f98.png)开启 CC 防护开关，当防护开启后必须设置清洗阈值，否则无法使用智能 CC 防护。
>?
>- 清洗阈值是高防产品启动清洗动作的阈值，当指定域名收到的 HTTP 请求超过阈值时，将触发 CC 防护。
>- 当高防包的 IP 为“Web 应用防火墙” 的 IP 时，需要先到 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/tea-baseconfig) 为此 IP 开启 CC 防护，详情请参见 [CC 防护规则设置](https://cloud.tencent.com/document/product/627/64336)。
>
![](https://qcloudimg.tencent-cloud.cn/raw/080d63287105c7b0f0a6fd750bbf6a33.png)
4. 在智能 CC 防护卡片中，单击**设置**。
![](https://qcloudimg.tencent-cloud.cn/raw/31f69096004cf14fcf7415fcb186cdba.png)
5. 在智能 CC 防护页面中，单击**新建**，输入需要防护的域名，开启智能 CC 开关，选择防护状态，单击**保存**。
>?观察模式下智能生成防护规则但不生效。
>
![](https://qcloudimg.tencent-cloud.cn/raw/2b7ea653c8a824212a9b81ae0505b658.png)

6. 创建并开启智能 CC 防护后，基于每次攻击，智能防护自动生成防护规则。智能防护下发的规则存在**单次有效期**，单次攻击结束后，防护规则自动失效并清除。若需要针对下一次攻击调整。请单击右侧**查看**进行智能防护规则编辑。
![](https://qcloudimg.tencent-cloud.cn/raw/97fb3fb4f22391edf1124c77cd7c42e5.png)
7. 智能防护规则基于单次攻击自动生成与生效。智能防护下发的规则存在单次有效期，单次攻击结束后，防护规则自动失效并清除。根据防护需求，可单击**删除**，删除对应防护规则。
![](https://qcloudimg.tencent-cloud.cn/raw/a56fb4f5b174a964fa3d45dc9e6c79f8.png)
