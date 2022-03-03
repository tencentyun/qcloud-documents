## 防护说明
CC 防护根据访问特征和连接状态判定恶意行为， 阻断黑客的攻击。可根据不同的攻击场景配置相应的防护策略，保证业务稳定。清洗阈值是高防产品启动清洗动作的阈值。


## 前提条件
您需要成功 [购买 DDoS 高防 IP（境外企业版）](https://cloud.tencent.com/document/product/1014/56255)  ，并设置防护对象。


## 操作步骤
1. 登录 [DDoS 高防 IP（境外企业版）](https://console.cloud.tencent.com/ddos/ddos-basic) 控制台 ，在左侧导航中，单击 **DDoS 高防 IP** > **防护配置** > **CC 防护**。
2. 在 CC 防护页面的左侧列表中，选中高防 IP 的 ID，如“bgp-00xxxxxx”。
![](https://qcloudimg.tencent-cloud.cn/raw/8dffdad7a2bb7a9cf45d59390c4597d1.png)
3. 在 CC 防护开关和清洗阈值卡片中，单击**设置**。
4. 在 CC 防护开关及清洗阈值列表，单击**新建**，输入所需参数和清洗阈值。
![](https://qcloudimg.tencent-cloud.cn/raw/3bb75463601648bae803b71ffff4174d.png)
5. 单击**保存**，添加规则。
>!精细化的规则优先级高于高防 IP 实例全局维度下的规则。
>
6. 新建完成后，在 CC 防护开关及清洗阈值列表中，将新增一条 CC 防护域名规则。在自定义模式下，单击![](https://qcloudimg.tencent-cloud.cn/raw/1e38c0dc7ff3e8074918e49f85df84f6.png)和![](https://qcloudimg.tencent-cloud.cn/raw/ec3b78b7673c4cbe941c754547507839.png) ，支持修改 CC 防护域名开关和清洗阈值。
![](https://qcloudimg.tencent-cloud.cn/raw/307ae11dc76d9417bac37fe449d53e54.png)
