## 基本信息类接口
| 接口名称                   | 接口功能                    |
| ------------------------------ | ------------------------------- |
| BGPIPGetInfo             | 获取指定 BGP 高防 IP 实例的详细信息       |
| BGPIPRename                    | 修改指定 BGP 高防 IP 实例名字 |
| BGPIPSetCCThreshold            | 设置指定 BGP 高防 IP 实例的 CC 防护阈值 |
| BGPIPSetElasticProtectionLimit | 设置指定 BGP 高防 IP 实例的弹性防护峰值 |
| AddCustomCCStrategy            | 添加单个 CC 自定义策略          |
| EditCustomCCStrategy           | 编辑单个 CC 自定义策略          |
| GetCustomCCStrategy            | 获取单个 CC 自定义策略信息      |
| GetCustomCCStrategyList        | 获取 CC 自定义策略列表          |
| RemoveCustomCCStrategy         | 删除单个 CC 自定义策略          |
| SetCustomCCStrategyStatus      | 开启或关闭单个 CC 自定义策略    |
| OpenDomainCCProtection         | 开启域名规则 CC 防护            |
| CloseDomainCCProtection        | 关闭域名规则 CC 防护            |

## 防护信息类接口
| 接口名称                | 接口功能                                                    |
| ----------------------- | ----------------------------------------------------------- |
| BGPIPDDoSGetCounter     | 获取指定 BGP 高防 IP 实例被 DDoS 攻击的次数、峰值和弹性防护开启次数 |
| BGPIPDDoSGetStatistics  | 获取指定 BGP 高防 IP 实例被 DDoS 攻击流量统计                       |
| BGPIPDDoSGetDetails     | 获取指定 BGP 高防 IP 实例被 DDoS 攻击流量详情                       |
| BGPIPCCGetCounter       | 获取指定 BGP 高防 IP 实例被 CC 攻击的次数、峰值                     |
| BGPIPCCGetStatistics    | 获取指定 BGP 高防 IP 实例被 CC 攻击流量统计图表                     |
| BGPIPCCGetDetails       | 获取指定 BGP 高防 IP 实例被 CC 攻击流量详情                         |
| BGPIPTransGetStatistics | 获取指定 BGP 高防 IP 实例向腾讯云外主机转发流量的统计图表           |

## 服务列表类接口
| 接口名称                  | 功能描述                                  |
| ------------------------- | ----------------------------------------- |
| BGPIPGetServicePacks      | 获取该用户名下所有 BGP 高防 IP 实例的列表 |
| BGPIPGetServiceStatistics | 获取 BGP 高防 IP 的历史使用天数和防御次数 |

## 转发规则类接口
| 接口名称                 | 功能描述                                  |
| ------------------------ | ----------------------------------------- |
| BGPIPAddTransRules       | 为指定 BGP 高防 IP 实例添加四层转发规则    |
| BGPIPEditTransRules      | 编辑指定 BGP 高防 IP 实例的指定四层转发规则       |
| BGPIPGetTransRules       | 获取指定 BGP 高防 IP 实例的四层转发规则列表 |
| BGPIPDeleteTransRules    | 删除指定 BGP 高防 IP 实例的指定四层转发规则         |
| BGPIPAddWadTransRules    | 为指定 BGP 高防 IP 实例的添加七层转发规则    |
| BGPIPEditWadTransRules   | 编辑指定 BGP 高防 IP 实例的指定七层转发规则             |
| BGPIPGetWadTransRules    | 获取 BGP 高防 IP 实例的七层转发规则列表   |
| BGPIPDeleteWadTransRules | 删除指定 BGP 高防 IP 实例的指定七层转发规则         |

## 白名单类接口
| 接口名称         | 功能描述                                      |
| ---------------- | --------------------------------------------- |
| GetWhiteUrl      | 获取指定 BGP 高防 IP 实例的白名单列表         |
| AddWhiteUrl      | 为指定 BGP 高防 IP 实例添加 URL 白名单列表     |
| RemoveWhiteUrl   | 删除指定 BGP 高防 IP 实例的 URL 白名单列表  |
| GetSrcWhiteIP    | 获取指定 BGP 高防 IP 实例的源 IP 白名单列表   |
| AddSrcWhiteIP    | 为指定BGP 高防 IP 实例添加源 IP 白名单列表    |
| RemoveSrcWhiteIP | 删除指定 BGP 高防 IP 实例的源 IP 白名单列表 |

## 黑名单类接口
| 接口名称         | 功能描述                                      |
| ---------------- | --------------------------------------------- |
| AddSrcBlackIP    | 为指定 BGP 高防 IP 实例添加源 IP 黑名单列表    |
| RemoveSrcBlackIP | 删除指定 BGP 高防 IP 实例的源 IP 黑名单列表 |

