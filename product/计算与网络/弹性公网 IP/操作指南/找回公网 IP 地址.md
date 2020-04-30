您可以找回使用过、且当前未分配给其他用户的公网 IP 地址，公网 IP 地址指普通公网 IP 和弹性公网 IP（EIP），两者均能找回，找回后的 IP 为 EIP。

## 背景信息 
 - EIP 总数不得超过产品总配额，详情请参见 [配额限制](https://cloud.tencent.com/document/product/1199/41648?!#.E9.85.8D.E9.A2.9D.E9.99.90.E5.88.B6)。
 - 每个账号单个地域申请找回 IP 不超过3次/月。
 
## 操作步骤
1. 登录 [EIP 控制台](https://console.cloud.tencent.com/cvm/eip)。
2. 在 EIP 管理页面，选择需找回的 IP 所在地域，并单击【找回IP】。
3. 在弹出的“找回IP”窗口中，输入公网 IP 地址，单击【查询】，检测 IP 是否可以申请找回。
 - 若显示该 IP 可申请，单击【立即申请】。
 - 若显示该 IP 已被分配等信息，表示待找回的 IP 资源已被使用等原因，暂不支持申请。请尝试申请其他 IP 或单击【取消】退出当前功能。
![](https://main.qcloudimg.com/raw/100d5be1d7e06b435b9797c7691a501b.png)

## 后续步骤
- 若需要为 EIP 绑定云资源，请参见 [EIP 绑定云资源](https://cloud.tencent.com/document/product/1199/41702)。

