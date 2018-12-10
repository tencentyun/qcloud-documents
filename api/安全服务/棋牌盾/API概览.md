## 基本信息类接口
| 接口名称                   | 功能描述                                 |
| -------------------------- | ---------------------------------------- |
| ShieldGetServiceStatistics | 获取棋牌盾的历史使用天数和防御 DDoS 次数 |
| ShieldIPRename             | 修改指定棋牌盾实例名称                   |
| ShieldIPAddTransRules      | 为指定棋牌盾实例添加转发规则             |
| ShieldIPEditTransRules     | 编辑指定转发规则                         |
| ShieldIPGetTransRules      | 获取指定棋牌盾实例的转发规则             |
| ShieldIPDeleteTransRules   | 删除指定转发规则                         |
| ShieldSetCCThreshold       | 设置指定棋牌盾实例的 CC 防护状态         |
| ShieldGetServicePacks      | 获取所有棋牌盾实例列表                   |
| ShieldIPGetInfo            | 获取指定棋牌盾实例详情                   |

## 白名单类接口
| 接口名称              | 功能描述             |
| --------------------- | -------------------- |
| ShieldWhitelistGet    | 获取棋牌盾白名单列表 |
| ShieldWhitelistAdd    | 为棋牌盾添加白名单   |
| ShieldWhitelistRemove | 删除棋牌盾白名单     |

## 分组模式类接口
| 接口名称                    | 功能描述                                         |
| --------------------------- | ------------------------------------------------ |
| ShieldAddGroup              | 添加分组                                         |
| ShieldEditGroup             | 编辑分组                                         |
| ShieldDeleteGroup           | 删除分组                                         |
| ShieldGroupAddTransRules    | 为指定棋牌盾分组添加转发规则                     |
| ShieldGroupEditTransRules   | 编辑指定棋牌盾分组的转发规则                     |
| ShieldGroupCopyTransRules   | 复制棋牌盾 A 分组的转发规则到 B 分组             |
| ShieldGroupDeleteTransRules | 删除指定棋牌盾分组的某个转发规则                 |
| ShieldGroupGetFreeIPs       | 获取棋牌盾闲置 IP （不属于任何分组）列表         |
| ShieldGetGroupList          | 获取用户名下所有棋牌盾分组                       |
| ShieldGroupGetInfo          | 获取某个棋牌盾分组的详细信息                     |
| ShieldGroupGetTransRules    | 获取某个棋牌盾分组的转发规则                     |
| ShieldGroupGetIPInfo        | 获取棋牌盾分组 IP 列表信息                       |
| ShieldGetIPStatus           | 通过分组 ID 获取分组内所有棋牌盾   IP 的封堵状态 |
| ShieldGroupGetRandomIP      | 通过分组 ID 获取分组内一个随机可用的 IP          |
| ShieldGroupGetAvailableIP   | 通过分组ID获取分组内所有可用棋牌盾IP             |

## CC 防护详情类接口
| 接口名称              | 功能描述                                 |
| --------------------- | ---------------------------------------- |
| ShieldCCGetCounter    | 获取棋牌盾的 CC 攻击次数和 CC   攻击峰值 |
| ShieldCCGetStatistics | 获取棋牌盾的CC攻击统计                   |
| ShieldCCGetDetails    | 获取棋牌盾的 CC 攻击详情                 |

## DDoS 防护详情类接口
| 接口名称                | 功能描述                             |
| ----------------------- | ------------------------------------ |
| ShieldDDoSGetCounter    | 获取棋牌盾的 DDoS 攻击次数和攻击峰值 |
| ShieldDDoSGetStatistics | 获取棋牌盾的 DDoS 攻击统计           |
| ShieldDDoSGetDetails    | 获取棋牌盾的 DDoS 攻击详情           |

## 转发流量类接口
| 接口名称                  | 功能描述                                                     |
| ------------------------- | ------------------------------------------------------------ |
| ShieldGetTransFlow        | 获取棋牌的转发流量                                           |
| ShieldGroupGetNetworkInfo | 获取棋牌盾的网络流量信息的接口，包括连接数、入流量、入包量、出包量和出流量 |