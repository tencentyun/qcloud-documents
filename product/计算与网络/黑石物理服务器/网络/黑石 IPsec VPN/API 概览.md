您可以使用 API 操作来设置和管理您的 IPsec VPN 连接，黑石更多相关 API 可以参考 [黑石物理服务器 API 概览。](https://cloud.tencent.com/document/api/386/6632)

### IPsec VPN 网关相关接口

| 接口功能            | Action ID            | 功能描述                                     |
| --------------- | -------------------- | ---------------------------------------- |
| 购买 IPsec VPN 网关   | AddBmIpsecVpnGw      | 购买 IPsec VPN 网关。                           |
| 修改 IPsec VPN 网关属性 | ModifyBmVpnGw        | 修改指定 IPsec VPN 网关信息，例如名称。                  |
| 查询 IPsec VPN 网关列表 | DescribeBmIpsecVpnGw | 根据用户信息，如 IPsec VPN 网关 ID，名称，查询对应 IPsec VPN 网关的信息。 |
| 删除 IPsec VPN 网关   | DeleteBmIPsecVpnGw   | 删除 IPsec VPN 网关。                           |

### 对端网关相关接口

| 接口功能     | Action ID        | 功能描述                           |
| -------- | ---------------- | ------------------------------ |
| 创建对端网关   | AddBmUserGw      | 创建要连接的对端网关。                    |
| 删除对端网关   | DeleteBmUserGw   | 删除指定对端网关。                      |
| 修改对端网关属性 | ModifyBmUserGw   | 修改指定对端网关信息，例如名称。               |
| 查询对端网关列表 | DescribeBmUserGw | 根据用户信息，如对端网关 ID，名称，查询对应对端网关的信息。 |

### IPsec VPN 通道相关接口

| 接口功能            | Action ID            | 功能描述                          |
| --------------- | -------------------- | ----------------------------- |
| 创建 IPsec VPN 通道   | AddBmIPsecVpnConn    | 创建 IPsec VPN 加密通道，将 VPC 接入其他网络资源。 |
| 删除 IPsec VPN 通道   | DeleteBmIPsecVpnConn | 删除指定 IPsec VPN 通道。              |
| 修改 IPsec VPN 通道   | ModifyBmIPsecVpnConn | 修改指定 IPsec VPN 通道的信息，如名称。       |
| 查询 IPsec VPN 通道列表 | DescribeBmVpnConn    | 根据用户信息，如通道 ID，名称，查询对应通道的信息。    |
| 下载 IPsec VPN 通道配置 | GetBmVpnConnConfig   | 下载 IPsec VPN 通道配置，对通道配置做调整。     |
| 重置 IPsec VPN 通道配置 | ResetBmVpnConnSA     | 重置指定 IPsec VPN 通道 IKE SA。        |
