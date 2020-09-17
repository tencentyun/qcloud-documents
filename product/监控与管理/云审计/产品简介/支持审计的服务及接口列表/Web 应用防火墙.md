腾讯云 Web 应用防火墙是一款基于 AI 的一站式 Web 业务运营风险防护方案。沉淀了腾讯云安全大数据检测能力和 19 年自营业务 Web 安全防护经验。通过 Web 入侵防护、0day 漏洞补丁修复、恶意访问惩罚、云备份防篡改等多维度防御策略全面防护网站的系统及业务安全。

下表为云审计支持的 Web 应用防火墙操作列表：

| 操作名称                | 资源类型 | 事件名称                           |
|---------------------|------|--------------------------------|
| Bot\_V2 获取 bot 开关     | waf  | BotV2GetSwitchStat             |
| Waf CC V2 Query 接口   | waf  | DescirbeCCRule                 |
| 获取访问日志游标            | waf  | DescribeAccessCursor           |
| 查询访问日志下载任务          | waf  | DescribeAccessDownloadRecords  |
| 查询满足搜索条件的访问日志数量     | waf  | DescribeAccessLogCount         |
| 查询访问日志              | waf  | DescribeAccessLogs             |
| Waf IP 状态统一查询接口      | waf  | DescribeActionedIp             |
| 获取 ai 模型状态            | waf  | DescribeAIModelStatus          |
| waf ai 在线验证          | waf  | DescribeAIVerifyResult         |
| 获取防篡改 url            | waf  | DescribeAntiFakeUrl            |
| 获取信息防泄漏规则列表         | waf  | DescribeAntiInfoLeakRules      |
| 获取地域封禁配置            | waf  | DescribeAreaBanAreas           |
| 获取 WAF 地域封禁支持的地域列表    | waf  | DescribeAreaBanSupportAreas    |
| 获取攻击日志详情            | waf  | DescribeAttackDetail           |
| 查询攻击日志的下载记录         | waf  | DescribeAttackDownloadRecords  |
| 查询攻击日志数量            | waf  | DescribeAttackLogCount         |
| 攻击城市分布              | waf  | DescribeAttackWorldMap         |
| Bot\_V2 获取 bot 动作统计   | waf  | DescribeBotActionStat          |
| Bot\_V2 域名 bot 统计     | waf  | DescribeBotAggregateDomainStat |
| bot 详情               | waf  | DescribeBotRecordDetail        |
| Bot\_V2 bot 记录访问详情   | waf  | DescribeBotRecordItems         |
| bot 记录访问趋势图          | waf  | DescribeBotRecordPoints        |
| Bot\_V2 bot 地理纬度统计   | waf  | DescribeBotRegionsStat         |
| Bot\_V2 Bot 流量统计     | waf  | DescribeBotStatisticPoints     |
| Bot\_V2 获取 bot 开关     | waf  | DescribeBotStatus              |
| Bot\_V2 获取 TCB 类型 Bots | waf  | DescribeBotTCBRecords          |
| Bot\_V2 获取 TCB 规则     | waf  | DescribeBotTCBRule             |
| Bot\_V2 Bot 类别统计     | waf  | DescribeBotTypeStat            |
| Bot\_V2 获取 UB 类型 Bots  | waf  | DescribeBotUBRecords           |
| Bot\_V2 获取 UCB 自定义策略  | waf  | DescribeBotUCBFeatureRule      |
| Bot\_V2 获取 UCB 预设策略   | waf  | DescribeBotUCBPreinstallRule   |
| Bot\_V2 获取 UCB 类型 Bots | waf  | DescribeBotUCBRecords          |
| Waf 斯巴达版本查询 cc 自动封堵状态 | waf  | DescribeCCAutoStatus           |
| 查询日志服务使用状况          | waf  | DescribeCLS                    |
| 查询自定义 payload 列表      | waf  | DescribeCustomPayloads         |
| 获取 DNS 劫持检测的被劫持用户数的数据 | waf  | DescribeDNSDetectDataChart     |
| DNS 劫持\-获取地图数据       | waf  | DescribeDNSDetectDataMap       |
| 获取 DNS 劫持检测的域名列表      | waf  | DescribeDNSDetectDomainList    |
| 获取 DNS 劫持检测的劫持记录      | waf  | DescribeDNSDetectHijackData    |
| Waf IP 黑白名单查询        | waf  | DescribeIpAccessControl        |
| Waf IP 封堵状态查询        | waf  | DescribeIpHitItems             |
| 查询业务和攻击概要趋势         | waf  | DescribePeakPoints             |
| 获取业务和攻击概览峰值         | waf  | DescribePeakValue              |
| 获取客户产品信息            | waf  | DescribeProductInfo            |
| 获取指定时间段内请求总数        | waf  | DescribeRequestCount           |
| Waf 会话定义查询接口        | waf  | DescribeSession                |
| 查询用户信息              | waf  | DescribeSpartUserInfo          |
| 拉取攻击类型统计数据          | waf  | DescribeStatisticTypes         |
| 批量下载访问日志            | waf  | ExportAccessLogs               |
| 查询 waf 的价格            | waf  | InquiryPriceWafInstance        |
| 日志使用情况              | waf  | WafClsOverview                 |
| 下载查询日志              | waf  | WafDownloadlogs                |
| 查询下载记录              | waf  | WafDownloadRecords             |
| 获取 ai 模型状态            | waf  | WafGetAIModelStatus            |
| waf ai 在线验证          | waf  | WafGetAIVerifyResult           |
| 查询自定义 payload 列表      | waf  | WafGetCustomPayloads           |
| 获取非标端口              | waf  | WafGetPort                     |
| WAF 通用接口             | waf  | WafInterface                   |
| 查询全量日志              | waf  | WafSearchLogs                  |
