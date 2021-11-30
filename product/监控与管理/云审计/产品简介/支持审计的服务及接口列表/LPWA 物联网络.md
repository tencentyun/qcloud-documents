腾讯云 LPWA（Low Power Wide Area）物联网络是为传感终端提供用于通讯的基础网络。LPWA 物联网络支持 LoRaWAN/CLAA（China LoRa Application Alliance）标准协议，按设备数量和租用时长计费，网络租用方式灵活，为您提供稳定的网络覆盖，节约建网成本，降低您的物联通讯费用，且无需关注网络运维。

下表为云审计支持的 LPWA 物联网络操作列表：

| 操作名称             | 资源类型 | 事件名称                       |
|------------------|------|----------------------------|
| 网关指定输入           | lpwa | CreateAccessGateways       |
| 节点指定输入           | lpwa | CreateAccessNodes          |
| 网关自动生成           | lpwa | CreateAutoAccessGateways   |
| 节点自动生成           | lpwa | CreateAutoAccessNodes      |
| 删除网关节点配置信息       | lpwa | DeleteGateway              |
| 获取网关入网列表         | lpwa | DescribeAccessGateways     |
| 获取节点入网列表         | lpwa | DescribeAccessNodes        |
| 获取告警列表           | lpwa | DescribeAlarms             |
| 系统状态折线图          | lpwa | DescribeCpuMem             |
| 获取设备信息           | lpwa | DescribeDevice             |
| 获取设备通信信息         | lpwa | DescribeDeviceActivation   |
| 获取设备密钥           | lpwa | DescribeDeviceKey          |
| 设备列表清单           | lpwa | DescribeDevices            |
| 根据用户 ID 获取设备列表清单   | lpwa | DescribeDevicesByUser      |
| 获取网关信息           | lpwa | DescribeGateway            |
| 获取网关信息列表         | lpwa | DescribeGateways           |
| 运营监控分用户激活节点数    | lpwa | DescribeMonitorActiveNodes |
| 运营监控分用户启用节点数    | lpwa | DescribeMonitorEnableNodes |
| 运营监控网关统计         | lpwa | DescribeMonitorGateway     |
| 运营监控节点分用户在线节点数 | lpwa | DescribeMonitorInlineNode  |
| 监控运营所有节点信息       | lpwa | DescribeMonitorNode        |
| 流量历史折线图          | lpwa | DescribeNetStat            |
| 运行参数上下行统计        | lpwa | DescribeNetSumary          |
| 更新节点设备配置信息       | lpwa | ModifyGateway              |


