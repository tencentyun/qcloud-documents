专线接入（Direct Connect，DC）为您提供了一种便捷的连接企业数据中心与腾讯云的方法，您可通过专线接入建立与公网完全隔离的私有连接服务，相比公网，专线接入具备更安全、更稳定、更低时延、更大带宽等特性。您只需要一条运营商物理专线一点接入腾讯云，便可快速创建多条专用通道打通部署于腾讯云的计算资源，实现灵活可靠的混合云部署。另外，专用通道多样的计费模式能为您在不同情况下节省专线使用成本。

下表为云审计支持的专线接入操作列表：

| 操作名称      | 资源类型 | 事件名称                            |
|-----------|------|---------------------------------|
| 创建物理专线    | dc   | CreateDirectConnect             |
| 创建互联网专用通道 | dc   | CreatePublicDirectConnectTunnel |
| 删除物理专线    | dc   | DeleteDirectConnect             |
| 查询物理专线接入点 | dc   | DescribeAccessPoints            |
| 获取物理专线列表  | dc   | DescribeDirectConnects          |
| 更新物理专线属性  | dc   | ModifyDirectConnectAttribute    |

