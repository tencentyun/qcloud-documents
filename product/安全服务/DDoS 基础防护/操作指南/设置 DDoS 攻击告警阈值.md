## 操作场景
在 DDoS 防护管理控制台，可查看 DDoS 基础防护的防护详情，并可以对防护 DDos 攻击设置告警阈值。

## 操作步骤
1. 登录 [DDoS 防护管理控制台](https://console.cloud.tencent.com/ddos/dashboard/overview)，在左侧导航中，单击 **DDoS 基础防护**。
2. 单击**设置 DDoS 攻击告警阈值**，弹出设置告警阈值弹窗。
![](https://qcloudimg.tencent-cloud.cn/raw/efe47cee3aee3e59e588312361eb5e49.png)
3. 在设置告警阈值弹窗中，DDoS 攻击告警阈值可以选择默认、入流量带宽或清洗流量功能，并设置告警阈值，单击**确定**，即可保存设置。
![](https://main.qcloudimg.com/raw/3138880bc259c261cca7c992daeb51a6.png) 
首次进入，告警策略类型为“默认”。参数说明如下：
    - 默认：当攻击流量满足以下其中一条，即发起告警。
       - DDoS 攻击：当攻击入流量 >= 2Gbps或者清洗流量 > 100Mbps。任一条件满足，即发起告警。
       - CC 攻击：当攻击入流量 > 1000QPS。
    - 入流量带宽：检测出的攻击流量带宽。当入流量 >= 设置数值即发起告警。 
    - 清洗流量：被清洗的攻击流量。当清洗流量 >= 设置数值即发起告警。
