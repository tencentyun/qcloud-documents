

## 漏洞详情
2020年10月20日，腾讯安全团队检测到 Oracle 发布的 [安全更新公告](https://www.oracle.com/security-alerts/cpuoct2020.html ) 。在本次更新的 Weblogic 相关漏洞中的 CVE-2020-14882 及 CVE-2020-14883 漏洞，存在于 WebLogic 的 Console 控制台中。此组件为 WebLogic 全版本默认自带组件，攻击者通过将 CVE-2020-14882 和 CVE-2020-14883 漏洞进行组合利用后，在未经授权的情况下，可以直接在服务端执行任意代码，获取系统权限，控制 Oracle WebLogic Server，影响数据的保密性、完整性和可用性。

腾讯安全旗下的全系列安全产品已针对该漏洞升级规则库及漏洞库，以防御黑客攻击利用。

为避免您的业务受影响，腾讯云安全建议您及时开展安全自查，如在受影响范围，请您及时进行更新修复，避免被外部攻击者入侵。

## 风险等级
高风险。

## 漏洞风险
攻击者可利用该漏洞控制 Oracle WebLogic Server，影响数据的保密性、完整性和可用性。

## 影响版本
- Oracle Weblogic Server 10.3.6.0.0
- Oracle Weblogic Server 12.1.3.0.0
- Oracle Weblogic Server 12.2.1.3.0
- Oracle Weblogic Server 12.2.1.4.0
- Oracle Weblogic Server 14.1.1.0.0


## 修复建议
官方已发布新版本安全产品修复该漏洞，腾讯云安全建议您：
- 推荐方案：及时 [安装更新补丁](https://www.oracle.com/security-alerts/cpuoct2020.html)。
- 使用 Web 应用防火墙拦截防御此类 Weblogic 漏洞攻击。


## 参考信息
更多信息，请参见 [官方安全更新公告](https://www.oracle.com/security-alerts/cpuoct2020.html) 。
