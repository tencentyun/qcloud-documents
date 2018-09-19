## Domain Name Registration

You can open the [Domain Registration Page](https://cloud.tencent.com/product/dm.html) to query and register domain names.

For more information, please see [How to Register a Domain](https://cloud.tencent.com/doc/product/242/3717).

## Adding CNAME Record

### Enter Domain Name Resolution Page

Log in to Tencent Cloud **Console** -> **Cloud Products** -> **Domain Name Management** -> **Resolution**. The main domain name of the example is `qcloudtest.com`.

![](//mccdn.qcloud.com/static/img/196c66e6643ccd88eba9f8b9373a297e/image.png)

### Add CNAME Record

Click **Add** in **Resolution** page to add CNAME record. Instructions are shown below:

1) Enter the server record as required.

A server record is domain name prefix. Common records are as follows:
- www: The resolved domain name is `www.qcloudtest.com`
- @: Directly resolve the main domain name `qcloudtest.com`
- *: Pan resolution, matching all other domain names `*.qcloudtest.com`

2) Record type. It is recommended to choose `CNAME Record`.

Each record type is shown below:

- A Record: Address record, which is used to specify IPv4 address of the domain name (e.g. 8.8.8.8). If you need to direct the domain name to an IP address, A Record must be added.
- CNAME: You need to add CNAME Record if the domain name is required to point to another domain name which provides IP address.
- TXT: You can enter anything here. Length limit: 255. Most TXT records are used as SPF records (anti-spam).
- NS: Domain name server record. This is required if you need to deliver the sub-domain name to other DNS service providers for resolution.
- AAAA: Used to specify the IPv6 address (such as ff06:0:0:0:0:0:0:c3) record corresponding to the server name (or domain name).
- MX: This is required if you need to set up an e-mail to receive mails.
- Explicit URL: Explicit URL record is required when an address with status code 301 is redirected to another address (Note: Currently DNSPod only supports 301 redirection).
- Implicit URL: Similar to explicit URL. The difference is that implicit URL does not change the domain name in the address bar.
- SRV: Records which services are provided by certain computers. Format: service name + dot + protocol type. For example: _xmpp-server._tcp.

3) Line is used to direct users on specific lines to access this domain.

Choose [Default] if the domain provider only provides one IP address or domain name.
Common line configuration:
- Default: Must be added, otherwise your website can only be accessed by specified lines. It is recommended to enter [China Telecom IP] as [Default]* for dual-line resolution.
- China Unicom: Specify server IP for [China Unicom Users]. Other users still access the [Default] one.
- Search engines: Specify a server IP for web crawlers to capture

4) For CNAME record, enter the domain name provided by your domain name provider (i.e. the domain name you just purchased).

Common record values for different types are shown below:
- A Record: Enter your server IP. Please ask your domain provider.
- CNAME Record: Enter the domain name provided by your domain provider. ***For example: Domain name of the LB instance, 1b16c9-0.ap-guangzhou.12345678.clb.myqcloud.com***.
- MX Record: Enter the IP address of your e-mail server or the domain name provided by enterprise e-mail provider. If you are not sure about this, ask your e-mail service provider for help.
- TXT Record: Usually used in anti-spam configurations of enterprise e-mails (such as Google, QQ and so on)
- Explicit URL Record: Enter the URL to be redirected to, for example: http://cloud.tencent.com
- Implicit URL Record: Enter the URL whose content is to be referenced, for example: http://cloud.tencent.com
- AAAA: Not commonly used. The address resolved to IPv6.
- NS Record: Not commonly used. Do not modify the two NS records provided by the system by default. It is used for NS downward authorization. Enter the DNS domain name, such as f1g1ns1.dnspod.net.
- SRV Record: Not commonly used. Format: priority + space + weight + space +port + space + server name. Once the record is generated, a "." is appended to the end of the server name. For example: 5 0 5269 xmpp-server.l.google.com.

Other values can be configured as default values. After entering the values, click **OK**.

![](//mccdn.qcloud.com/static/img/3d952308d0e576fa3a2be640b3238074/image.png)

### Viewing CNAME records

You can view, modify and manage the added CNAME records in **Resolution** page.

### Testing Resolution Result

To test whether the domain is resolved normally, you can directly access the bound CNAME domain name (such as www.qcloudtest.com mentioned in the example). Note: It takes about 10 minutes for the resolution to take effect.

