专用通道支持资源级权限，即表示针对支持资源级权限的操作，控制何时允许用户执行操作或是允许用户使用的特定资源。

## 可授权策略介绍

在访问管理（Cloud Access Management，CAM）中可授权的资源类型如下：

| 资源类型         | 授权策略中的资源描述方法                         |
| :--------------- | :----------------------------------------------- |
| 专用通道相关操作 | qcs::dc::uin/${Uin}/dcx/${DirectConnectTunnelId} |

- 所有 `${Uin}` 为资源拥有者的 AccountId，或者“*”。
- 所有 `${DirectConnectTunnelId}` 为专用通道 ID，或者“*”。

## 专用通道相关操作

| 接口名称                                | 接口描述             | 六段式定义                                 |
| --------------------------------------- | -------------------- | ------------------------------------------ |
| CreatePublicDirectConnectTunnel         | 创建互联网专用通道   | qcs::dc::uin/:dcx/*                        |
| DescribeDirectConnectTunnels            | 获取专用通道列表     | qcs::dc::uin/:dcx/*                        |
| AcceptDirectConnectTunnel               | 接受专用通道         | qcs::dc::uin/:dcx/${DirectConnectTunnelId} |
| DeleteDirectConnectTunnel               | 删除专用通道         | qcs::dc::uin/:dcx/${DirectConnectTunnelId} |
| ModifyDirectConnectTunnelAttribute      | 修改专用通道属性     | qcs::dc::uin/:dcx/${DirectConnectTunnelId} |
| CreateDirectConnectTunnel               | 创建专用通道         | qcs::dc::uin/:dcx/*                        |
| RejectDirectConnectTunnel               | 拒绝专用通道申请     | qcs::dc::uin/:dcx/${DirectConnectTunnelId} |
| DescribePublicDirectConnectTunnelRoutes | 查询互联网通道路由表 | qcs::dc::uin/:dcx/${DirectConnectTunnelId} |
| DescribeDirectConnectTunnelExtra        | 查询专用通道扩展信息 | qcs::dc::uin/:dcx/${DirectConnectTunnelId} |
| ModifyDirectConnectTunnelExtra          | 修改专用通道扩展信息 | qcs::dc::uin/:dcx/${DirectConnectTunnelId} |

