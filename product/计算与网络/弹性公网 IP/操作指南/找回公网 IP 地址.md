若您误操作释放或退还了公网 IP 地址（包含 EIP 和普通公网 IP），可以在公网 IP 控制台找回，找回后的公网 IP 为 EIP。

## 使用限制
找回公网 IP 地址具有以下使用限制：
- 仅支持找回常规 BGP IP 线路类型的公网 IP 地址，其余类型不支持找回。
- 仅支持找回您已使用过、且当前未分配给其他用户的公网 IP 地址。
- 每个账户单个地域申请找回 IP 次数不超过3次/月。
- 加上找回的 EIP，EIP 总数不得超过产品总配额，详情请参见 [配额限制](https://cloud.tencent.com/document/product/1199/41648?!#.E9.85.8D.E9.A2.9D.E9.99.90.E5.88.B6)。
- 对于标准账户类型，找回的 EIP 默认计费模式为按流量计费，带宽上限为5Mbps，计费模式和带宽上限可在重新申请成功后修改。
 
## 操作步骤
1. 登录 [公网 IP 控制台](https://console.cloud.tencent.com/cvm/eip)。
2. 在“公网 IP” 页面顶部，选择需找回的 IP 所在地域，并单击**找回 IP**。
3. 在弹出的“找回IP”窗口中，输入公网 IP 地址，单击**查询**，检测 IP 是否可以申请找回。
 - 若显示该 IP 可申请，单击**立即申请**。
 - 若显示该 IP 已被分配等信息，表示待找回的 IP 资源已被使用等原因，暂不支持申请。请尝试申请其他 IP 或单击**取消**退出当前功能。
![](https://main.qcloudimg.com/raw/100d5be1d7e06b435b9797c7691a501b.png)
4. 在公网 IP 的 [列表页](https://console.cloud.tencent.com/cvm/eip?rid=1) 中，查看已找回的公网 IP（找回后的公网 IP 为 EIP）。

## 后续步骤
若需要为 EIP 绑定云资源，请参见 [EIP 绑定云资源](https://cloud.tencent.com/document/product/1199/41702)。

