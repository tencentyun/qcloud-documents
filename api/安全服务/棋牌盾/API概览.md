## 基本信息类接口
| 接口名称                   | 功能描述                                 |
| -------------------------- | ---------------------------------------- |
| [ShieldGetServiceStatistics](https://cloud.tencent.com/document/product/1022/31410) | 获取棋牌盾的历史使用天数和防御 DDoS 次数 |
| [ShieldIPRename](https://cloud.tencent.com/document/product/1022/31406)             | 修改指定的棋牌盾 IP 名称                   |
| [ShieldIPAddTransRules](https://cloud.tencent.com/document/product/1022/31405)      | 为指定棋牌盾 IP 添加转发规则             |
| [ShieldIPEditTransRules](https://cloud.tencent.com/document/product/1022/31404)     | 编辑指定转发规则                         |
| [ShieldIPDeleteTransRules](https://cloud.tencent.com/document/product/1022/31403)   | 删除指定转发规则                         |
| [ShieldIPGetTransRules](https://cloud.tencent.com/document/product/1022/31399)      | 获取指定棋牌盾 IP 的转发规则             |
| [ShieldSetCCThreshold](https://cloud.tencent.com/document/product/1022/31398)       | 设置指定棋牌盾 IP 的 CC 防护状态         |
| [ShieldGetServicePacks](https://cloud.tencent.com/document/product/1022/31397)      | 获取所有棋牌盾 IP 列表                   |
| [ShieldIPGetInfo](https://cloud.tencent.com/document/product/1022/31396)            | 获取指定棋牌盾 IP 详情                   |

## 白名单类接口
| 接口名称              | 功能描述             |
| --------------------- | -------------------- |
| [ShieldWhitelistGet](https://cloud.tencent.com/document/product/1022/31413)    | 获取棋牌盾 IP 的白名单列表 |
| [ShieldWhitelistAdd](https://cloud.tencent.com/document/product/1022/31412)    | 为棋牌盾 IP 添加白名单   |
| [ShieldWhitelistRemove](https://cloud.tencent.com/document/product/1022/31411) | 删除棋牌盾 IP 的白名单     |

## 分组模式类接口
| 接口名称                    | 功能描述                                         |
| --------------------------- | ------------------------------------------------ |
| [ShieldAddGroup](https://cloud.tencent.com/document/product/1022/31429)              | 添加分组                                         |
| [ShieldEditGroup](https://cloud.tencent.com/document/product/1022/31428)             | 编辑分组                                         |
| [ShieldDeleteGroup](https://cloud.tencent.com/document/product/1022/31427)           | 删除分组                                         |
| [ShieldGroupAddTransRules](https://cloud.tencent.com/document/product/1022/31426)    | 为指定棋牌盾分组添加转发规则                     |
| [ShieldGroupEditTransRules](https://cloud.tencent.com/document/product/1022/31425)   | 编辑指定棋牌盾分组的转发规则                     |
| [ShieldGroupCopyTransRules](https://cloud.tencent.com/document/product/1022/31424)   | 复制棋牌盾 A 分组的转发规则到 B 分组           |
| [ShieldGroupDeleteTransRules](https://cloud.tencent.com/document/product/1022/31423) | 删除指定棋牌盾分组的某个转发规则                 |
| [ShieldGroupGetFreeIPs](https://cloud.tencent.com/document/product/1022/31422)       | 获取棋牌盾闲置 IP （不属于任何分组）列表         |
| [ShieldGetGroupList](https://cloud.tencent.com/document/product/1022/31420)          | 获取用户名下所有棋牌盾分组                       |
| [ShieldGroupGetInfo](https://cloud.tencent.com/document/product/1022/31419)          | 获取某个棋牌盾分组的详细信息                     |
| [ShieldGroupGetTransRules](https://cloud.tencent.com/document/product/1022/31418)    | 获取某个棋牌盾分组的转发规则                     |
| [ShieldGroupGetIPInfo](https://cloud.tencent.com/document/product/1022/31417)        | 获取棋牌盾分组 IP 列表信息                       |
| [ShieldGetIPStatus](https://cloud.tencent.com/document/product/1022/31416)           | 通过分组 ID 获取分组内所有棋牌盾 IP 的封堵状态 |
| [ShieldGroupGetRandomIP](https://cloud.tencent.com/document/product/1022/31415)      | 通过分组 ID 获取分组内一个随机可用的 IP          |
| [ShieldGroupGetAvailableIP](https://cloud.tencent.com/document/product/1022/31414)   | 通过分组 ID 获取分组内所有可用棋牌盾 IP             |

## CC 防护详情类接口
| 接口名称              | 功能描述                                 |
| --------------------- | ---------------------------------------- |
| [ShieldCCGetCounter](https://cloud.tencent.com/document/product/1022/31433)    | 获取棋牌盾 IP 的 CC 攻击次数和 CC 攻击峰值 |
| [ShieldCCGetStatistics](https://cloud.tencent.com/document/product/1022/31432) | 获取棋牌盾 IP 的 CC 攻击统计                   |
| [ShieldCCGetDetails](https://cloud.tencent.com/document/product/1022/31431)    | 获取棋牌盾 IP 的 CC 攻击详情                 |

## DDoS 防护详情类接口
| 接口名称                | 功能描述                             |
| ----------------------- | ------------------------------------ |
| [ShieldDDoSGetCounter](https://cloud.tencent.com/document/product/1022/31436)    | 获取棋牌盾 IP 的 DDoS 攻击次数和攻击峰值 |
| [ShieldDDoSGetStatistics](https://cloud.tencent.com/document/product/1022/31435) | 获取棋牌盾 IP 的 DDoS 攻击统计           |
| [ShieldDDoSGetDetails](https://cloud.tencent.com/document/product/1022/31434)    | 获取棋牌盾 IP 的 DDoS 攻击详情           |

## 转发流量类接口
| 接口名称                  | 功能描述                                                     |
| ------------------------- | ------------------------------------------------------------ |
| [ShieldGetTransFlow](https://cloud.tencent.com/document/product/1022/31437)        | 获取棋牌 IP 的转发流量                                           |
| [ShieldGroupGetNetworkInfo](https://cloud.tencent.com/document/product/1022/31438) | 获取棋牌盾 IP 的网络流量信息的接口，包括连接数、入流量、入包量、出包量和出流量 |
