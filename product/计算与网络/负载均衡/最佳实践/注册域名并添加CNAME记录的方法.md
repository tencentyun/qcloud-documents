目前负载均衡支持 A 记录和 CNAME 的绑定，用户可通过注册域名并添加 A 记录和 CNAME 记录进行访问。详情请参见 [云解析 A 记录操作指南](https://cloud.tencent.com/document/product/302/3449)，[云解析 CNAME 记录操作指南](https://cloud.tencent.com/document/product/302/3450)。

## 1. 域名注册

注册域名可以通过 [域名注册页面](https://console.cloud.tencent.com/domain/mydomain) 进行域名查询和注册。

相关文档可以参考 [如何注册域名](https://cloud.tencent.com/doc/product/242/3717)。

## 2. 添加 CNAME 记录

### 2.1. 进入域名解析页面
登录腾讯云 [云解析控制台](https://console.cloud.tencent.com/cns)，在操作拦中单击【解析】。
![](https://main.qcloudimg.com/raw/14a23a600162daaee162f246dd081eef.png)

### 2.2. 添加 CNAME 记录

1. 在“记录管理”页面，单击【添加记录】。
![](https://main.qcloudimg.com/raw/993cd7c1fb1309f42429d4090da3a9c1.png)
2. 用户可以添加 CNAME 记录，操作指引如下：
 1. 主机记录可以按照需求说明填写。
 主机记录就是域名前缀，常见用法有：
    - www：解析后的域名为` www.qcloudtest.com`
    - @：直接解析主域名 `qcloudtest.com`
     - \*：泛解析，匹配其他所有域名 `*.qcloudtest.com`

 2. 记录类型用户可选 `CNAME` 记录
![](https://main.qcloudimg.com/raw/29564b0e024351387aa0a54fada5ae78.png)
各个记录类型如下：
    - A 记录：地址记录，用来指定域名的 IPv4 地址（如`8.8.8.8`），如果需要将域名指向一个 IP 地址，就需要添加 A 记录。
    - CNAME： 如果需要将域名指向另一个域名，再由另一个域名提供 IP 地址，就需要添加 CNAME 记录。
    - TXT：在这里可以填写任何东西，长度限制 255。绝大多数的TXT记录是用来做 SPF 记录（反垃圾邮件）。
    - NS：域名服务器记录，如果需要把子域名交给其他DNS服务商解析，就需要添加 NS 记录。
    - AAAA：用来指定主机名（或域名）对应的 IPv6 地址（如`ff06:0:0:0:0:0:0:c3`）记录。
    - MX：如果需要设置邮箱，让邮箱能收到邮件，就需要添加 MX 记录。
    - 显性 URL：从一个地址301重定向到另一个地址的时候，就需要添加显性 URL 记录（注：DNSPod 目前只支持301重定向）。
    - 隐性 URL：类似于显性URL，区别在于隐性 URL 不会改变地址栏中的域名。
    - SRV：记录了哪台计算机提供了哪个服务。格式为：服务的名字、点、协议的类型，例如 xmpp-server.tcp。

 3. 线路类型是为了让指定线路的用户访问这个 IP
 若空间商只提供了一个 IP 地址或域名，选择【默认】即可。
 常见用法有：
    - 默认：必须添加，否则只有单独指定的线路才能访问您的网站。如果双线解析，建议「默认」线路填写「电信 IP」。
    - 联通：单独为「联通用户」指定服务器 IP，其他用户依然访问「默认」。
    - 搜索引擎：指定一个服务器 IP 让蜘蛛抓取。

  4. CNAME 记录值主要填写空间商给您提供的域名。
各类型的记录值一般是这样的：
    - A 记录：填写您服务器 IP，如果您不知道，请咨询您的空间商。
    - CNAME 记录：填写空间商给您提供的域名，**例如，负载均衡中 CLB 实例的域名`1b16c9-0.ap-guangzhou.12345678.clb.myqcloud.com`**。
    - MX 记录：填写您邮件服务器的 IP 地址或企业邮箱给您提供的域名，如果您不知道，请咨询您的邮件服务提供商。
    - TXT 记录：一般用于 Google、QQ 等企业邮箱的反垃圾邮件设置。
    - 显性 URL 记录：填写要跳转到的网址，例如`http://cloud.tencent.com` 。
    - 隐性 URL 记录：填写要引用内容的网址，例如`http://cloud.tencent.com` 。
    - AAAA：不常用。解析到 IPv6 的地址。
    - NS 记录：不常用。系统默认添加的两个 NS 记录请不要修改。NS 向下授权，填写 dns 域名，例如`f1g1ns1.dnspod.net`。
    - SRV 记录：不常用。格式为：优先级、空格、权重、空格、端口、空格、主机名，记录生成后会自动在域名后面补一个“.”，这是正常现象。例如 `5 0 5269 xmpp-server.l.google.com.`。

其余值可以按照默认进行操作。操作完成后，单击【保存】。
![](https://main.qcloudimg.com/raw/9c68a7108eb33b0594bf0eb9f8f83213.png)
### 2.3. 查看 CNAME 记录
添加记录完毕后，可以在“记录管理”页面查看所添加的 CNAME 记录，并对其进行修改、暂停等操作。
![](https://main.qcloudimg.com/raw/a86ac1086efaba7b4ad76f56d40e868a.png)

### 2.4. 测试解析结果
用户为测试域名是否解析正常，可以直接访问绑定后的 CNAME 域名（如例子中的`www.qcloudtest.com` ）。
>?解析大概需要十分钟左右生效。
