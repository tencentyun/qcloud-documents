## 现象描述
负载均衡 UDP 健康检查中，后端服务器端口的真实状态与健康检查状态不一致。

## 可能原因
UDP 健康检查的原理是负载均衡发送 UDP 探测报文到后端服务器，若 PING 成功，且响应超时时间内未返回` port XX unreachable` 消息，则健康检查判定为正常，反之则为异常。

出现状态不一致问题的可能原因有两种：
- 健康检查响应超时时间过小，后端服务器回复的 `reply` 或 `port unreachable` 类型的 ICMP 消息未能在超时时间内到达健康检查的节点，导致健康检查结果不准确。
- 后端服务器限制了 ICMP 消息产生的速率，因此，即便服务器已经出现异常，但由于无法向前端返回 `port XX unreachable` 报错信息，导致负载均衡由于没收到 ICMP 应答进而判定健康检查成功，最终导致服务真实状态与健康检查不一致。

## 处理步骤
1. 首先排查健康检查的响应超时时间是否设置过小。登录 [负载均衡控制台](https://console.cloud.tencent.com/clb)，适当调大 UDP 监听器的健康检查的响应超时时间，详情请参见 [配置 UDP 健康检查](https://cloud.tencent.com/document/product/214/36387#.E6.AD.A5.E9.AA.A42.EF.BC.9A.E9.85.8D.E7.BD.AE.E7.9B.91.E5.90.AC.E5.99.A8)。
>? 由于 UDP 健康检查的原理不同于其他健康检查，建议健康检查的超时时间不要过小，否则后端服务器可能会反复上下线。
2. 若调整健康检查的响应超时时间后，仍出现状态不一致的问题，则可选择排查后端服务器是否限制了 ICMP 消息产生的速率。登录后端云服务器，执行以下命令检查 ICMP 消息速率的限制。
```
sysctl -q net.ipv4.icmp_ratelimit
sysctl -q net.ipv4.icmp_ratemask
```
3. 确认 `net.ipv4.icmp_ratelimit` 速率参数的返回值是否为0或为默认值1000。建议改为默认值1000，不建议超过1000。
4. 若调整速率限制后，仍出现状态不一致的问题，则执行以下命令关闭 `port unreachable` 类型的 ICMP 消息的速率限制。
>!不再限制 `port unreachable` 类型的 ICMP 消息发送速度后，会让暴露在公网的服务器在受到 UDP 端口扫描攻击时，不受限制次数地返回 `port unreachable` 消息。
>
```
# 请根据以上步骤2的 net.ipv4.icmp_ratemask 参数查询结果，修改以下代码中的“xxxx”数值。
# 将以下代码中的“xxxx”修改为前三位数不变，最后一位数减8的数值，例如：6168改为6160，1819改为1811。
sysctl -w net.ipv4.icmp_ratemask=xxxx
```


