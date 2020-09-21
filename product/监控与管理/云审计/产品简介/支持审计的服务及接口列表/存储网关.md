存储网关（Cloud Storage Gateway，CSG）是一种混合云存储方案，旨在帮助企业或个人实现本地存储与公有云存储的无缝衔接。您无需关心多协议本地存储设备与云存储的兼容性，只需要在本地安装云存储网关即可实现混合云部署，并拥有媲美本地性能的海量云端存储。

下表为云审计支持的存储网关操作列表：

| 操作名称   | 资源类型 | 事件名称                       |
|--------|------|----------------------------|
| 激活网关   | csg  | ActivateGateway            |
| 删除网关   | csg  | DeleteGateway              |
| 查询网关信息 | csg  | DescribeGatewayInformation |
| 查询网关列表 | csg  | ListGateways               |
| 停止网关   | csg  | ShutdownGateway            |
| 启动网关   | csg  | StartGateway               |
