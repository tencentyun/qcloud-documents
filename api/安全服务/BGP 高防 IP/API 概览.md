## 基本信息类接口
| 接口名称                   | 接口功能                    |
| ------------------------------ | ------------------------------- |
| [BGPIPGetInfo](https://cloud.tencent.com/document/product/1014/31246)             | 获取指定 BGP 高防 IP 实例的详细信息       |
| [BGPIPRename](https://cloud.tencent.com/document/product/1014/31245)                    | 修改指定 BGP 高防 IP 实例的名称 |
| [BGPIPSetCCThreshold](https://cloud.tencent.com/document/product/1014/31244)            | 设置指定 BGP 高防 IP 实例的 CC 防护阈值 |
| [BGPIPSetElasticProtectionLimit](https://cloud.tencent.com/document/product/1014/31243) | 设置指定 BGP 高防 IP 实例的弹性防护峰值 |
|[ AddCustomCCStrategy](https://cloud.tencent.com/document/product/1014/31242)            | 添加单个 CC 自定义策略          |
| [EditCustomCCStrategy](https://cloud.tencent.com/document/product/1014/31241)           | 编辑单个 CC 自定义策略          |
| [GetCustomCCStrategy](https://cloud.tencent.com/document/product/1014/31240)            | 获取单个 CC 自定义策略信息      |
| [GetCustomCCStrategyList](https://cloud.tencent.com/document/product/1014/31239)        | 获取 CC 自定义策略列表          |
| [RemoveCustomCCStrategy](https://cloud.tencent.com/document/product/1014/31238)         | 删除单个 CC 自定义策略          |
| [SetCustomCCStrategyStatus](https://cloud.tencent.com/document/product/1014/31237)      | 开启或关闭单个 CC 自定义策略    |
| [OpenDomainCCProtection](https://cloud.tencent.com/document/product/1014/31236)         | 开启域名规则 CC 防护            |
| [CloseDomainCCProtection](https://cloud.tencent.com/document/product/1014/31235)        | 关闭域名规则 CC 防护            |

## 防护信息类接口
| 接口名称                | 接口功能                                                    |
| ----------------------- | ----------------------------------------------------------- |
| [BGPIPDDoSGetCounter](https://cloud.tencent.com/document/product/1014/31253)     | 获取指定 BGP 高防 IP 实例被 DDoS 攻击的次数、峰值和弹性防护开启次数 |
| [BGPIPDDoSGetStatistics](https://cloud.tencent.com/document/product/1014/31252)  | 获取指定 BGP 高防 IP 实例被 DDoS 攻击流量统计                       |
| [BGPIPDDoSGetDetails](https://cloud.tencent.com/document/product/1014/31251)     | 获取指定 BGP 高防 IP 实例被 DDoS 攻击流量详情                       |
| [BGPIPCCGetCounter](https://cloud.tencent.com/document/product/1014/31250)       | 获取指定 BGP 高防 IP 实例被 CC 攻击的次数、峰值                     |
| [BGPIPCCGetStatistics](https://cloud.tencent.com/document/product/1014/31249)    | 获取指定 BGP 高防 IP 实例被 CC 攻击流量统计图表                     |
| [BGPIPCCGetDetails](https://cloud.tencent.com/document/product/1014/31248)       | 获取指定 BGP 高防 IP 实例被 CC 攻击流量详情                         |
| [BGPIPTransGetStatistics](https://cloud.tencent.com/document/product/1014/31247) | 获取指定 BGP 高防 IP 实例向腾讯云外主机转发流量的统计图表           |

## 服务列表类接口
| 接口名称                  | 功能描述                                  |
| ------------------------- | ----------------------------------------- |
| [BGPIPGetServicePacks](https://cloud.tencent.com/document/product/1014/31261)      | 获取该用户名下所有 BGP 高防 IP 实例的列表 |
| [BGPIPGetServiceStatistics](https://cloud.tencent.com/document/product/1014/31262) | 获取 BGP 高防 IP 的历史使用天数和防御次数 |

## 转发规则类接口
| 接口名称                 | 功能描述                                  |
| ------------------------ | ----------------------------------------- |
| [BGPIPAddTransRules](https://cloud.tencent.com/document/product/1014/31270)       | 为指定 BGP 高防 IP 实例添加四层转发规则    |
| [BGPIPEditTransRules](https://cloud.tencent.com/document/product/1014/31269)      | 编辑指定 BGP 高防 IP 实例的指定四层转发规则       |
| [BGPIPGetTransRules](https://cloud.tencent.com/document/product/1014/31268)       | 获取指定 BGP 高防 IP 实例的四层转发规则列表 |
| [BGPIPDeleteTransRules](https://cloud.tencent.com/document/product/1014/31267)    | 删除指定 BGP 高防 IP 实例的指定四层转发规则         |
| [BGPIPAddWadTransRules](https://cloud.tencent.com/document/product/1014/31266)    | 为指定 BGP 高防 IP 实例的添加七层转发规则    |
| [BGPIPEditWadTransRules](https://cloud.tencent.com/document/product/1014/31265)   | 编辑指定 BGP 高防 IP 实例的指定七层转发规则             |
| [BGPIPGetWadTransRules](https://cloud.tencent.com/document/product/1014/31263)    | 获取 BGP 高防 IP 实例的七层转发规则列表   |
| [BGPIPDeleteWadTransRules](https://cloud.tencent.com/document/product/1014/31264) | 删除指定 BGP 高防 IP 实例的指定七层转发规则         |

## 白名单类接口
| 接口名称         | 功能描述                                      |
| ---------------- | --------------------------------------------- |
| [GetWhiteUrl](https://cloud.tencent.com/document/product/1014/31277)      | 获取指定 BGP 高防 IP 实例的白名单列表         |
| [AddWhiteUrl](https://cloud.tencent.com/document/product/1014/31276)      | 为指定 BGP 高防 IP 实例添加 URL 白名单列表     |
| [RemoveWhiteUrl](https://cloud.tencent.com/document/product/1014/31275)   | 删除指定 BGP 高防 IP 实例的 URL 白名单列表  |
| [GetSrcWhiteIP](https://cloud.tencent.com/document/product/1014/31274)    | 获取指定 BGP 高防 IP 实例的源 IP 白名单列表   |
| [AddSrcWhiteIP](https://cloud.tencent.com/document/product/1014/31273)    | 为指定BGP 高防 IP 实例添加源 IP 白名单列表    |
| [RemoveSrcWhiteIP](https://cloud.tencent.com/document/product/1014/31272) | 删除指定 BGP 高防 IP 实例的源 IP 白名单列表 |

## 黑名单类接口
| 接口名称         | 功能描述                                      |
| ---------------- | --------------------------------------------- |
| [AddSrcBlackIP](https://cloud.tencent.com/document/product/1014/31278)    | 为指定 BGP 高防 IP 实例添加源 IP 黑名单列表    |
| [RemoveSrcBlackIP](https://cloud.tencent.com/document/product/1014/31279) | 删除指定 BGP 高防 IP 实例的源 IP 黑名单列表 |

