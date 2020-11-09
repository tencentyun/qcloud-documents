2020年9月3日，腾讯安全团队监控到 Jenkins 发布了9月安全通告，里面包含14个 CVE 漏洞（CVE-2020-2238，CVE-2020-2239，CVE-2020-2240， CVE-2020-2241， CVE-2020-2242， CVE-2020-2243， CVE-2020-2244， CVE-2020-2245， CVE-2020-2246， CVE-2020-2247， CVE-2020-2248， CVE-2020-2249， CVE-2020-2250， CVE-2020-2251），有10个插件受影响，涉及以下插件：
- Build Failure Analyzer Plugin
- Cadence vManager Plugin
- database Plugin
- Git Parameter Plugin
- JSGames Plugin
- Klocwork Analysis Plugin
- Parameterized Remote Trigger Plugin
- SoapUI Pro Functional Testing Plugin
- Team Foundation Server Plugin
- Valgrind Plugin

其中以下漏洞定义为高危：
- CVE-2020-2248（JSGames Plugin XSS 漏洞）
- CVE-2020-2247（Klocwork Analysis Plugin 中的 XXE 漏洞）
- CVE-2020-2246（Valgrind plugin XSS 漏洞）
- CVE-2020-2245（Valgrind plugin XXE 漏洞）
- CVE-2020-2244（Build Failure Analyzer Plugin 存在 XSS 漏洞）
- CVE-2020-2243（Cadence vManager Plugin 存在存储型 XSS 漏洞）
- CVE-2020-2240（database Plugin CSRF 漏洞）
- CVE-2020-2238（Git Parameter Plugin 存储型 XSS 漏洞）

Jenkins 是一款基于 Java 开发的开源项目，用于持续集成和持续交付的自动化中间件，是开发过程中常用的产品，为避免您的业务受影响，腾讯云安全建议您及时开展安全自查，如在受影响范围，请您及时进行更新修复，避免被外部攻击者入侵。由于有部分漏洞目前尚无修补程序，建议使用采取腾讯 Web 应用防火墙进行防御。

## 漏洞详情

- **Git Parameter Plugin 存在存储型 XSS 漏洞 （CVE-2020-2238）**
	- Git Parameter Plugin 0.9.12 及更早版本不会在“Build with Parameters”页面上转义，导致存储的跨站点脚本（XSS）漏洞可由具有“Job/Configure”权限的攻击者利用。
	- Git Parameter Plugin  在0.9.13上完成修复工作。
	- Parameterized Remote Trigger Plugin 将密码明文存储在纯文本中（CVE-2020-2239）。
	- Parameterized Remote Trigger Plugin 3.1.3和更早版本将密码明文存储。
- **database Plugin 存在 CSRF 漏洞 CVE-2020-2240**
	- database Plugin 1.6 和更早版本不需要数据库控制台的 POST 请求，从而导致跨站点请求伪造（CSRF）漏洞，此漏洞使攻击者可以执行任意 SQL 脚本。
	- database Plugin CSRF 漏洞和越权漏洞 CVE-2020-2241 (CSRF)，CVE-2020-2242（permission check）。
	- database Plugin 1.6 和更早版本在实现表单验证的方法中不执行权限检查。 这使具有对 Jenkins 的“Overall/Read ”访问权限的攻击者，可以使用攻击者指定的用户名和密码连接到攻击者指定的数据库服务器。此外，此表单验证方法不需要 POST 请求，从而导致跨站点请求伪造（CSRF）漏洞。
	- database Plugin 1.7 需要 POST 请求和受影响的表单验证方法的“Overall/Read”权限。
- **Cadence vManager Plugin 存在存储型 XSS 漏洞 CVE-2020-2243**
	- Cadence vManager Plugin 3.0.4 及更早版本不会在工具提示中转义构建说明，从而导致存储的跨站点脚本（XSS）漏洞可由具有运行/更新权限的攻击者利用。
	- Cadence vManager Plugin 3.0.5 删除了受影响的工具提示。
- **Build Failure Analyzer Plugin 存在 XSS 漏洞  CVE-2020-2244**
	- Build Failure Analyzer Plugin 1.27.0 及更早版本不会在表单验证响应中转义匹配的文本，从而导致跨站点脚本（XSS）漏洞，攻击者可以利用此漏洞，为用于测试构建日志指示的构建提供控制台输出。
	- Build Failure Analyzer Plugin 1.27.1 会在受影响的表单验证响应中转义匹配的文本。
- **Valgrind Plugin 存在 XXE 漏洞 CVE-2020-2245**
	- Valgrind Plugin 0.28 和更早版本没有配置其 XML 解析器来防止 XML 外部实体（XXE）攻击，从而使攻击者能够控制 Valgrind Plugin 解析器的输入文件，使 Jenkins 解析使用外部实体，从 Jenkins 控制器或服务器端请求伪造中提取机密的制作好的文件。  
	- 截至本公告发布之时，尚无修复程序。
- **Valgrind Plugin 中存储的 XSS 漏洞 CVE-2020-2246**
	- Valgrind Plugin 0.28 和更早版本不会在 Valgrind XML 报表中转义内容，从而导致存储的跨站点脚本（XSS）漏洞可由能够控制 Valgrind XML 报告内容的攻击者利用。
	- 截至本公告发布之时，尚无修复程序。

- **Klocwork Analysis Plugin 中的 XXE 漏洞 CVE-2020-2247**
	- Klocwork Analysis Plugin 2020.2.1和更早版本没有配置其 XML 解析器来防止 XML 外部实体（XXE）攻击，从而攻击者能够控制 Klocwork 插件解析器的输入文件，使 Jenkins 解析使用外部实体，从 Jenkins 控制器或服务器端请求伪造中提取机密的制作好的文件。
	- 截至本公告发布之时，尚无修复程序。
- **JSGames Plugin 存在反射型的 XSS 漏洞 CVE-2020-2248**
	- JSGames Plugin 0.2及更早版本将 URL 的一部分作为代码进行评估，从而会导致反映出跨站点脚本（XSS）漏洞。
	- 截至本公告发布之时，尚无修复程序。
- **Team Foundation Server Plugin 以明文格式存储凭据 CVE-2020-2249**
	Team Foundation Server Plugin 5.157.1 和更早版本将 Webhook 机密未加密地存储，在 Jenkins 控制器的全局配置文件中 hudson.plugins.tfs.TeamPluginGlobalConfig.xml 作为其配置的一部分，攻击者可以访问 Jenkins 控制器文件系统来查看此凭据。
- **SoapUI Pro Functional Testing Plugin 使用明文存储密码 CVE-2020-2250**
	SoapUI Pro Functional Testing Plugin 1.3 和更早版本将未加密的项目密码存储在 job config.xml 文件中，作为其配置的一部分，具有扩展读取权限或访问 Jenkins 控制器文件系统的攻击者可以查看这些项目密码。一旦再次保存受影响的 job 配置，SoapUI Pro Functional Testing Plugin 1.4 将存储加密的项目密码。
- **SoapUI Pro Functional Testing Plugin 使用明文传输密码 CVE-2020-2251**
	- SoapUI Pro 功能测试插件将项目密码存储在 Jenkins 控制器上的 job 文件中，config.xml 作为其配置的一部分。
	- 自 SoapUI Pro 功能测试插件1.4起，这些密码以加密方式存储在磁盘上，但 SoapUI Pro 功能测试插件1.5及更早版本以全局配置形式将它们以纯文本格式传输，具有扩展读取权限的攻击者可以查看这些密码。
	- 仅会影响2.236（包括 2.235.x LTS）之前的 Jenkins，因为 Jenkins 2.236 引入了安全性强化功能，可以透明地加密和解密用于 Jenkins 密码表单字段的数据。
	- 截至本公告发布之时，尚无修复程序。

## 风险等级
- CVE-2020-2249 低风险
- CVE-2020-2239 低风险
- CVE-2020-2241 中风险
- CVE-2020-2242 中风险
- CVE-2020-2250 中风险
- CVE-2020-2251 中风险
- CVE-2020-2240 高风险
- CVE-2020-2247 高风险
- CVE-2020-2248 高风险
- CVE-2020-2246 高风险
- CVE-2020-2245 高风险
- CVE-2020-2243 高风险
- CVE-2020-2238 高风险
- CVE-2020-2244 高风险

## 影响版本
- Build Failure Analyzer Plugin  <= 1.27.0
- Cadence vManager Plugin <= 3.0.4
- database Plugin <= 1.6
- Git Parameter Plugin <= 0.9.12
- JSGames Plugin  <= 0.2
- Klocwork Analysis Plugin  <= 2020.2.1
- Parameterized Remote Trigger Plugin  <= 3.1.3
- SoapUI Pro Functional Testing Plugin  <= 1.3
- SoapUI Pro Functional Testing Plugin  <= 1.5
- Team Foundation Server Plugin <= 5.157.1
- Valgrind Plugin <= 0.28

## 修复版本
- Build Failure Analyzer Plugin should be updated to version 1.27.1
- Cadence vManager Plugin should be updated to version 3.0.5
- database Plugin should be updated to version 1.7
- Git Parameter Plugin should be updated to version 0.9.13
- Parameterized Remote Trigger Plugin should be updated to version 3.1.4
- SoapUI Pro Functional Testing Plugin should be updated to version 1.4

## 等待修补版本
- JSGames Plugin
- Klocwork Analysis Plugin
- SoapUI Pro Functional Testing Plugin
- Team Foundation Server Plugin
- Valgrind Plugin


## 修复建议
官方发布部分升级插件修复该漏洞，但是由于部分插件缺少修复版本，腾讯云安全建议您：
- 更新对应 Jenkins 插件（由于明文存储漏洞为本地漏洞，需等待插件更新）。
- 由于 Jenkins 的敏感性，建议 Jenkins 不对外开放，如果有公网访问需求，可以在腾讯云 Web 应用防火墙上面 [配置 IP 白名单](https://cloud.tencent.com/document/product/627/35359) 等访问策略。
- 推荐企业用户采取腾讯云 Web 应用防火墙检测并拦截 Jenkins 9月安全更新通告中基于网络的漏洞攻击。

腾讯云 Web 应用防火墙（Web Application Firewall）已支持拦截防御 Jenkins 9月安全更新通告内包含的漏洞。


## 参考信息
 官方通告如下:
- [Jenkins Security Advisory 2020-09-01](https://www.jenkins.io/security/advisory/2020-09-01/) 
- [CVE-2020-2238](https://nvd.nist.gov/vuln/detail/CVE-2020-2238)
- [CVE-2020-2239](https://nvd.nist.gov/vuln/detail/CVE-2020-2239)
- [CVE-2020-2240](https://nvd.nist.gov/vuln/detail/CVE-2020-2240)
- [CVE-2020-2241](https://nvd.nist.gov/vuln/detail/CVE-2020-2241)
- [CVE-2020-2242](https://nvd.nist.gov/vuln/detail/CVE-2020-2242)
- [CVE-2020-2243](https://nvd.nist.gov/vuln/detail/CVE-2020-2243)
- [CVE-2020-2244](https://nvd.nist.gov/vuln/detail/CVE-2020-2244)
- [CVE-2020-2245](https://nvd.nist.gov/vuln/detail/CVE-2020-2245)
- [CVE-2020-2246](https://nvd.nist.gov/vuln/detail/CVE-2020-2246)
- [CVE-2020-2247](https://nvd.nist.gov/vuln/detail/CVE-2020-2247)
- [CVE-2020-2248](https://nvd.nist.gov/vuln/detail/CVE-2020-2248)
- [CVE-2020-2249](https://nvd.nist.gov/vuln/detail/CVE-2020-2249)
- [CVE-2020-2250](https://nvd.nist.gov/vuln/detail/CVE-2020-2250)
- [CVE-2020-2251](https://nvd.nist.gov/vuln/detail/CVE-2020-2251)
- [CloudBees Jenkins XSS 漏洞（CVE-2020-2246）](http://www.cnnvd.org.cn/web/xxk/ldxqById.tag?CNNVD=CNNVD-202009-036)  
- [CloudBees Jenkins XSS 漏洞（CVE-2020-2243）](http://www.cnnvd.org.cn/web/xxk/ldxqById.tag?CNNVD=CNNVD-202009-035)  
- [CloudBees Jenkins XXE 漏洞](http://www.cnnvd.org.cn/web/xxk/ldxqById.tag?CNNVD=CNNVD-202009-037) 




