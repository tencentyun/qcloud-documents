API（Application Programming Interface）应用程序接口，可以应用于所有计算机平台和操作系统，以不同的格式连接数据调用数据，用户可以跟踪电商平台购买的货物位置，就是电商平台与物流公司之间使用了 API 位置实时调用产生的效果。

许多组织更关注于快速的 API 和应用程序交付，而忽视了 API 安全保护，这也是近几年来 API 攻击和数据泄露的主要原因。

API 的调用场景可分为如下三种类型：

<table>
<thead>
<tr>
<th width=10%>API 类型</th>
<th width=45%>API 描述</th>
<th width=45%>安全现状</th>
</tr>
</thead>
<tbody><tr>
<td>公开 API</td>
<td align="center">支持任何人从任何地方访问服务，被暴露在互联网中，调用方可根据相关接口，提供相关字段的数据，即可完成相关数据、流程的调度。公开 API 对安全性、使用性的监控、处置程度最高。</td>
<td align="center">网络限制少，可能存在相关认证等授权的限制，但是相关业务鉴权逻辑漏洞也更为频发，攻击者更加偏爱对此类 API 通过自动化模糊测试、定向安全测试等方式进行定向攻击及绕过。</td>
</tr>
<tr>
<td>内部  API</td>
<td align="center">通常在数据中心或私有云网络环境中部署和运行，以运营管理、内部服务支撑为主。通常用于用户的内部之间的快速调度及使用，通常不暴露在外网</td>
<td align="center">网络限制较大，可能存在相关鉴权等操作，通常校验力度较低，安全防护力度较低，攻击者如果发现并嗅探到了此类内部 API 接口，就会针对此类 API 接口进行定向攻击。在多起数据泄露事件中， 对内部 API 的攻击、是导致泄露的罪魁祸首。</td>
</tr>
<tr>
<td>渠道 API</td>
<td align="center">通常在数据中心或私有云网络环境中部署和运行，向特定的外部合作伙伴、供应商提供对内部 API 的有限制的访问。 通常用于特定合作伙伴的定向数据拉取及管控，对数据拉取的敏感度低，但对数据外泄的敏感程度较高。</td>
<td align="center">访问程度控制权位于内部和外部 API 之间，安全管控层级也是一样，主流手段是通过 API 网关管控，但缺少安全方面的考虑。很少对此类 API 进行相关越权方面的业务管控。如果上下游供应链上的合作伙伴被入侵进而调度相关的 API 进行数据滥用，在渠道 API 上通常会缺少滥用的监控监管机制，因此多起数据泄漏事件就因为没有对渠道 API 进行滥用管控造成的。</td>
</tr>
</tbody></table>

## 为什么要做 API 敏感数据发现
据《Salt Labs State of API Security Report, Q1 2022》报告，在受访者最关心的 API 安全问题中，僵尸 API 以43%占比高居第一；远超过以22%的占比位居第二的账户接管/滥用；还有83%的受访者对组织 API 资产清单是否完整没有信心。

为何企业对 API 资产有如此大的担忧？安全隐患往往藏于“未知”，未知的僵尸 API、未知的影子 API、未知的敏感数据暴露等，根源都在于企业对 API 资产全貌的未知。安全的管理与防护始于“已知”和“可见”，人们难以掌控那些被遗忘的、看不见摸不着的资产安全状况。然而正是这些被人遗忘、不可管控的 API，往往会有相关敏感数据在上面运行，如果没有办法及时的发现这些敏感的 API 接口则会导致相关 API 数据被拖取或意外暴露的情况，攻击者很有可能就会通过此类 API 接口对业务敏感数据进行定向发现及攻击，紧接着进行相关敏感数据拖取，更有甚者会进一步的扩大 API 攻击的利用权限，对服务器、数据库的权限进行进一步获取。从而导致页数受损。

即便是企业已经开始重视并着手治理僵尸 API 问题，也仍有一处容易被忽略的巨大风险——僵尸参数。不同于那些被彻底遗忘的僵尸 API，这些僵尸参数有可能还存在于当前仍在服务且持续维护的 API 接口中。常见的僵尸参数，例如在开发测试周期内设置的调试参数、系统属性参数，它们在接口正式上线后未对外暴露给用户，但仍能被暗处的攻击者恶意调用。攻击者基于僵尸参数，能够利用批量分配等漏洞获得越权的响应。一旦这些未知的 API 脆弱点被恶意利用，背后的核心业务数据、平台用户数据等海量敏感数据在黑客面前就变成了内部 API 调用，没有任何安全管制，再无秘密可言。

## 操作步骤
### 步骤1：发现 API 资产
1. 登录 [Web 应用防火墙控制台](https://console.cloud.tencent.com/guanjia/tea-overview)，在左侧导航栏中，选择 **API 流量分析**。
>?API 流量分析功能当前处于公测中，支持 [提交工单](https://console.cloud.tencent.com/workorder/category?step=0&source=14) 或联系商务经理申请试用该功能，公测期间仅支持开启3个域名。
>
2. 在 API 流量分析页面，左上角选择需要防护的域名，并单击开启是否开启分析的![](https://qcloudimg.tencent-cloud.cn/raw/54de1d8ce243aa5ab8de791a85f43ef6.png)。
![](https://qcloudimg.tencent-cloud.cn/raw/b1d6eb3422531dd07052c945a63ef44b.png)
3. 开启开关后，即可在相关 API 详情页查看对应 API 的相关详情信息。
![](https://qcloudimg.tencent-cloud.cn/raw/46e433367ced0824db036bc256df6c80.png)

### 步骤2：API 安全加固
1. 在 [基础安全](https://console.cloud.tencent.com/guanjia/tea-baseconfig) > API 安全页面，根据相关 API 进行 API 合法性加固。
![](https://qcloudimg.tencent-cloud.cn/raw/32d970e07b66975a56003fec9f804952.png)
2. 在 CC 防护页面，根据相关 API 进行容量保护措施。
![](https://qcloudimg.tencent-cloud.cn/raw/cf349addeb37e485333daae06ef2f2c5.png)
3. 在访问控制页面，单击**添加规则**，根据相关 API 进行敏感操作保护措施。
![](https://qcloudimg.tencent-cloud.cn/raw/adc48e886f530cfe430158a095801ad8.png)
4. 在 BOT 与业务安全页面，根据相关 API 进行异常行为保护措施。
![](https://qcloudimg.tencent-cloud.cn/raw/8a67fd2a54853cee91dbe3c1f9e1f612.png)

### 步骤3：API 生命周期管理
1. API 上线监测。
![](https://qcloudimg.tencent-cloud.cn/raw/8b0a76c951a280e17975437795888b55.png)
2. API 参数新增检测，API 参数新增检测。
![](https://qcloudimg.tencent-cloud.cn/raw/6f1f93399adaa9817bbeb4f924f9f7b9.png)
3. API 下线回收，API 临时阻断。
![](https://qcloudimg.tencent-cloud.cn/raw/f2c794626ccd0b5f3e6ca0e20d9426ad.png)
