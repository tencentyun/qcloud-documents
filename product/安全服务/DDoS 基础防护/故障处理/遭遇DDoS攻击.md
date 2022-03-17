
## 现象描述
业务遭受 DDoS 大流量攻击，消耗目标服务器性能/网络带宽，造成服务器无法正常提供服务。

## 可能原因
用户 IP 遭受的攻击大小，超过了腾讯云赠送的基础防护能力（普通用户 2Gbps/VIP 用户 10Gbps）。

## 解决思路
- **更换公网 IP（攻击停止时，临时方案）**
攻击者发起 DDoS 攻击是针对具体业务 IP，通过临时更换 IP，只能临时规避被封堵的问题，无法根本解决，攻击者可能随时针对新 IP 发起第二次攻击，产生二次影响。
- **购买高防产品（推荐方案）**
通过购买 DDoS 高防产品，提升 IP 的防护能力，抵御大流量攻击，如攻击流量超过了高防包所在地域的能力，可按需选择更大防护能力的高防 IP 产品。

## 处理步骤
### 更换公网 IP（攻击停止时，临时方案）
更换公网 IP 相关限制如下：
- 单个账号单个地域不超过3次/天。
- 单台实例仅允许更换1次公网 IP。
- 更换后原公网 IP 将被释放。

更换操作详情，请参见 [更换公网 IP 地址](https://cloud.tencent.com/document/product/213/16642)。

### 购买配置高防产品（推荐方案）
- 购买并配置 DDoS 高防包，请参见 [购买指引](https://cloud.tencent.com/document/product/1021/43894) 和 [快速入门](https://cloud.tencent.com/document/product/1021/43898)。
- 购买并配置 DDoS 高防 IP，请参见 [购买指引](https://cloud.tencent.com/document/product/1014/44082) 和 [快速入门](https://cloud.tencent.com/document/product/1014/44087)。

DDoS 高防包和 DDoS 高防 IP 的对比，请参见 [DDoS 防护解决方案对比](https://cloud.tencent.com/document/product/1021/44463)。

