### 1. 接口描述
获取棋牌盾闲置IP（不属于任何分组）列表
协议：HTTPS 
接口名：ShieldGroupGetFreeIPs

### 2.输出参数
| 参数名称 | 是否必须 | 类型 | 描述 |
|---------|---------|---------|---------|
|ipList | <font color=red> [obj,…]</font color=red> | Array |限制IP列表，数组元素如下：<br>{<br>"vipId": "bgpip-0000001", <br>"ip": "1.1.1.1",<br>"status":"idle/attacking/blocking/creating",<br>} |
| vipId| <font color=red> bgpip-000001 </font color=red> | String |棋牌盾IP的资源ID，格式是bgpip-XXXXXXX |
| ip | <font color=red> 1.2.3.4</font color=red> | String |棋牌盾IP的IP地址 |
| status | <font color=red> idle<br>attacking<br>blocking<br>creating </font color=red> | String |棋牌盾IP的状态：<br>idle:正常工作中<br>attacking:正在被攻击<br>blocking:被封堵<br>creating:正常创建中 |