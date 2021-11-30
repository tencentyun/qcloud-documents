## What Is WAF?
Tencent Cloud Web Application Firewall (WAF) is an AI-based one-stop protection solution against Web business operation risks. With strong security and big data capabilities and 19 years of Web security protection experience of Tencent, WAF provides effective security guarantee for websites.
Tencent Cloud WAF can effectively prevent SQL injection, cross-site scripting (XSS), trojan upload, unauthorized access and other OWASP attacks. In addition, it can provide all-round protection for website systems and businesses by effectively filtering CC attacks, detecting DNS linkage hijacking, providing zero-day vulnerability patches, and preventing webpage tampering.

## Key Features

<style>
table th:first-of-type {
    width: 180px;
}
</style>

| Feature | Description |
| ---------- | ---------------------------------------- |
| AI+Web application firewall | With the Web attack identification based on AI+ rules, anti-bypass, low false negative and low false positive, it can precisely and effectively defend against common Web attacks, such as SQL injection, unauthorized access, XSS, cross-site request forgery (CSRF), Webshell trojan upload and other Top 10 Web security threats and attacks defined by OWASP. |
| Virtual patching for zero-day vulnerabilities | Tencent security team provides 24/7 monitoring to uncover vulnerabilities and make responses. It will issue virtual patches for high-risk Web vulnerabilities and zero-day vulnerabilities within 24 hours upon detection, and protected users can obtain the defense capability against emergency vulnerability and zero-day vulnerability attacks without performing any operation. The response cycle is greatly shortened. |
| Webpage tamper resistance | You can set it to back up core webpage contents to the cloud, and publish the backed up webpage contents to achieve webpage substitution, thus avoiding adverse impacts on your organization caused by webpage tampering. |
| Data leakage prevention | It can prevent backend databases from being hacked by means of ex-ante server application hiding, real-time intrusion protection, and ex-post sensitive data replacement and hiding policies. |
| CC attack defense | Multi-dimensionally custom precise access control in combination with human-machine identification and frequency control can effectively filter junk access and mitigate CC attacks. |
| Crawler bot behavior management | The webpage crawler and bot management based on the AI+ rules repository can help enterprises mitigate business risks, such as website user data leakage, content infringement, competitive pricing, inventory query, black hat SEO and business strategy disclosure, caused by malicious BOT behaviors. |
| DNS illegal hijacking detection | It performs nationwide DNS verification on domain names submitted by users, perceives and displays the hijacking details of the protected domain names in each region, to help enterprises avoid data interception and financial loss caused by website users being maliciously hijacked. |
| 30-line BGP IP access protection | Tencent Cloud WAF supports exclusive 30-line BGP IP linkage access for defense nodes. The nodes are scheduled intelligently, which effectively solves the access delay problem and ensures the site access speed of users in all tiers of cities, thus achieving the unaware cloud WAF security protection deployment without affecting the website access speed. |

## Why Is WAF Necessary?
In the following scenarios, Tencent Cloud WAF can provide effective defense and prevention against risks, and ensure system and business security of enterprise websites.
- **Data leakage (core information asset is leaked)**
As web sites are used as the entry for the information assets of many enterprises, hackers can steal enterprise information assets by means of invading web sites, resulting in incalculable losses to enterprises.
- **Malicious access and data crawling (the service is not running normally because data is leveraged by opponents)**
Hackers controlling zombie computers launch CC attacks on the web sites, which then will be unable to provide services due to resource depletion. Malicious users capture the core content of websites (literature blogs, recruitment sites, forum sites, and e-commerce site comments) via web crawlers. Product details of e-commerce sites are gathered deliberately by competitors for research. Bonus hunters seek for arbitrage by searching for low-priced product information or obtaining marketing intelligence in advance.
- **Website malicious code and tampering (affecting credibility and image)**
After obtaining permissions of web sites or servers, attackers will inject malicious codes to make users execute malicious programs, to earn traffic, to steal accounts or to show off; insert links of pornographic, gambling, or illegal contents; and tamper with webpage images and texts. These will severely influence the operation of websites and impair the image and credibility of website operators.
- **Framework vulnerabilities (attacked during patch fixing period)**
Many web systems are based on common open source frameworks, such as Structs2, Spring, and WordPress, which often carry security vulnerabilities. It is really a tough and dangerous period before patches are ready to use, because many attacks spring up soon after the vulnerabilities are uncovered.
- **Illegal hijacking (hijacking cannot be perceived)**
The normal DNS requests of websites cannot be responded properly or the accessed content is maliciously modified due to the efforts of obtaining traffic or increasing advertising revenue. These are common hijacks on the Internet. Website operators generally cannot perceive these before receiving customer complaints.
- **Service interruption caused by DDoS attacks with large traffic**
Being cheap and low-threshold, DDoS attack is often used to disrupt the operation of competitors or to make key portals inaccessible, leading to significant impact on business continuity and branding. And usually there isn't much operators can do when they are attacked.


## Basic Defense Process
![Before and after using WAF](https://main.qcloudimg.com/raw/4bf7d1db508ece27812ffa524e215a91.png)
Tencent WAF defense diagram:
![WAF defense diagram](https://main.qcloudimg.com/raw/68d007e4581ee9753d069ff6b1c3fc7c.png)

