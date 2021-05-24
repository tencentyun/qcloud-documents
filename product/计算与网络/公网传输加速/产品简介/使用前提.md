本文介绍 Anycast 公网加速的使用限制。
- Anycast 公网加速仅加速除中国大陆以外的其他地区，不加速中国大陆与境外地区之间的跨境传输。
- 使用 Anycast 公网加速需要创建 Anycast 公网加速 IP，与此同时会自动创建 Anycast 加速 BGP 带宽包。
 - Anycast 公网加速 IP 支持绑定 CVM、NAT 网关、弹性网卡、高可用虚拟 IP、内网 CLB。
 - 单个地域仅会自动生成1个 Anycast 加速 BGP 带宽包。
 - Anycast 加速 BGP 带宽包不支持添加云资源。
