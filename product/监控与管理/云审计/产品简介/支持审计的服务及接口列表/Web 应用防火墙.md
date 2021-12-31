腾讯云 Web 应用防火墙是一款基于 AI 的一站式 Web 业务运营风险防护方案。沉淀了腾讯云安全大数据检测能力和 19 年自营业务 Web 安全防护经验。通过 Web 入侵防护、0day 漏洞补丁修复、恶意访问惩罚、云备份防篡改等多维度防御策略全面防护网站的系统及业务安全。

下表为云审计支持的 Web 应用防火墙操作列表：

| 操作名称                | 资源类型 | 事件名称                           |
|---------------------|------|--------------------------------|
| 添加防篡改 url  | waf  | AddAntiFakeUrl         |
| 添加信息防泄漏规则 | waf  | AddAntiInfoLeakRules                 |
| 添加一条 api 规则         | waf  | AddApiRule           |
| 添加封禁地域          | waf  | AddAreaBanAreas  |
| 添加自定义拦截页面   | waf  | AddBlockPage         |
| 添加自定义载荷              | waf  | AddCustomPayload             |
| 增加自定义策略    | waf  | AddCustomRule             |
| 增加域名规则白名单         | waf  | AddDomainWhiteRule          |
|添加 Spart 防护域名        | waf  | AddSpartaProtection         |
| 给域名应用自定义拦截页面           | waf  | ApplyBlockPage            |
| Bot_V2 TCB 策略域名拷贝        | waf  | CopyBotTCBRule      |
| Bot_V2 UCB 自定义策略拷贝          | waf  | CopyBotUCBFeatureRules           |
| Bot_V2 UCB 预设策略拷贝   | waf  | CopyBotUCBPreinstallRule    |
| waf 斯巴达-添加缓存路径           | waf  | CreateCachePath           |
| 后付费创建日志服务         | waf  | CreateClsForAfterpay  |
| 复制地域封禁到其他域名            | waf  | CreateCopyAreaBan         |
| 复制自定义规则到其他域名              | waf  | CreateCopyCustomRule         |
| 添加 DNS 劫持检测的域名   | waf  | CreateDNSDetectDomain          |
| 添加防护域名    | waf  | CreateHost |
| 新增业务白名单             | waf  | CreateWhiteList        |
| 删除防篡改 url  | waf  | DeleteAntiFakeUrl         |
| 信息防泄漏删除规则       | waf  | DeleteAntiInfoLeakRule        |
| 删除攻击日志下载任务记录   | waf  | DeleteAttackDownloadRecord         |
| 删除自定义拦截页面    | waf  | DeleteBlockPage     |
| Waf CC V2 Delete接口     | waf  | DeleteCCRule              |
| waf 斯巴达-删除缓存路径 | waf  | DeleteCachePath          |
| 删除自定义 payload    | waf  | DeleteCustomPayloads             |
| 删除自定义规则     | waf  | DeleteCustomRule            |
|  删除DNS劫持检测的域名 | waf  | DeleteDNSDetectDomain  |
| 删除域名规则白名单  | waf  |  DeleteDomainWhiteRules |
|  删除访问日志下载记录 | waf  | DeleteDownloadRecord  |
|  删除 CLB-WAF 防护域名 | waf  | DeleteHost  |
|  Waf IP黑白名单 Delete 接口 | waf  |  DeleteIpAccessControl |
|   删除 CC 攻击的 session 设置 | waf  | DeleteSession  |
|  waf 斯巴达-删除防护域名 | waf  | DeleteSpartaProtection  |
|  删除业务白名单 | waf  |  DeleteWhiteList  |
|  刷新防篡改 url | waf  | FreshAntiFakeUrl  |
| 用户手动导入 api 规则  | waf  | ImportApiRules  |
| 模型训练  | waf  | ModifyAIModelai  |
|  编辑防篡改 url | waf  | ModifyAntiFakeUrl  |
|  切换防篡改开关 | waf  |  ModifyAntiFakeUrlStatus |
| 信息防泄漏切换规则开关  | waf  |  ModifyAntiInfoLeakRuleStatus |
| 编辑信息防泄漏规则  | waf  |  ModifyAntiInfoLeakRules |
| 修改地域封禁中地域信息  | waf  | ModifyAreaBanAreas|
|  修改地域封禁状态 | waf  |  ModifyAreaBanStatus |
|  Bot_V2 bot 开关更新 | waf  | ModifyBotStatus  |
|  Bot_V2 TCB 策略更新 | waf  | ModifyBotTCBRule  |
|  Bot_V2 UCB 预设规则更新 | waf  |  ModifyBotUCBPreinstallRule |
|  waf 斯巴达-编辑缓存路径  | waf  |  ModifyCachePath |
|  编辑自定义规则 | waf  | ModifyCustomRule  |
|  开启或禁用自定义策略 | waf  | ModifyCustomRuleStatus  |
|  编辑 DNS 劫持检测的域名 | waf  |  ModifyDNSDetectDomain |
|  更改某一条规则 | waf  | ModifyDomainWhiteRule  |
|  修改域名列表的访问日志开关 | waf  |  ModifyDomainsCLSStatus |
|  修改域名列表的 WAF 开关 | waf  |  ModifyDomainsStatus |
| 编辑防护域名  | waf  | ModifyHost  |
|  设置域名访问日志开关 | waf  | ModifyHostAccessLogStatus  |
| 设置防护域名的流量模式  | waf  | ModifyHostFlowMode  |
|   设置防护域名防护状态 | waf  |  ModifyHostMode |
| 设置防护域名 WAF 开关  | waf  | ModifyHostStatus  |
|  修改实例的 QPS 弹性计费开关 | waf  |  ModifyInstanceElasticMode |
|  修改实例的自动续费开关 | waf  | ModifyInstanceRenewFlag  |
|  更新前端对抗规则 | waf  | ModifyJsInjectRule  |
| 更新前端对抗规则的状态  | waf  | ModifyJsInjectRuleStatus  |
|  设置套餐自动续费 | waf  |  ModifyPackageRenew  |
| 更改防护等级  | waf  | ModifyProtectionLevel  |
| 斯巴达-waf 开关  | waf  |  ModifyProtectionStatuswaf  |
|   版本 WAF 自动续费开关设置 | waf  | ModifySpartaPackageRenewSparta  |
| 修改域名配置  | waf  |  ModifySpartaProtection  |
| 设置 waf 防护状态  | waf  | ModifySpartaProtectionMode  |
|  设置 webshell 状态 | waf  |  ModifyWebshellStatus |
|  更新业务白名单 | waf  |  ModifyWhiteList |
|  创建搜索下载攻击日志任务 | waf  | PostAttackDownloadTask  |
|  刷新接入检查的结果 | waf  | RefreshAccessCheckResult  |
| 启用或者停用 Api 规则  | waf  | SwitchApiRules  |
| 切换域名的规则开关  | waf  |  SwitchDomainRules |
| 切换域名白名单的开关  | waf  |  SwitchDomainWhiteRules  |
|  切换弹性 QPS 的开关 | waf  | SwitchElasticMode  |
| Bot_V2 UCB 策略更新  | waf  | UpsertBotUCBFeatureRule   |
|   Waf 斯巴达版本更新 cc 自动封堵状态 | waf  | UpsertCCAutoStatus  |
|  Waf CC V2 Upsert 接口 | waf  |  UpsertCCRule |
| 是否透传客户端的 IP 和端口  | waf  | UpsertClientMsg  |
|  Waf IP 黑白名单 Upsert 接口 | waf  | UpsertIpAccessControl  |
|  会话定义 Upsert 接口  | waf  |  UpsertSessionWaf |
|  查询下载记录 | waf  | WafDownloadRecords  |
| 下载查询日志  | waf  |  WafDownloadlogs |
