<font color="red">Currently, this method can only be used to configure custom domains for public network cloud load balancer instances with static IPs. Users can access it by registering domain then adding A record and CNAME record.</font>

## Domain Name Registration

Register domain by opening [Domain Registration Page](https://cloud.tencent.com/product/dm.html) for domain query and registration.

For relevant documents, please refer to [How to Register Domain](https://cloud.tencent.com/doc/product/242/3717)

## Adding CNAME record

### Entering Domain Resolution Page

Log in to Tencent Cloud "Console" - "Cloud Products" - "Domain Management" - "Resolution", the main domain of the example is `qcloudtest.com`.

![](//mccdn.qcloud.com/static/img/196c66e6643ccd88eba9f8b9373a297e/image.png)

### Adding CNAME record

Click "Add" in "Resolution" page, user can add CNAME record. Instructions are shown below:

1) Enter the host record as required.

A host record is domain prefix. Common usage are as follows:
- www: resolved domain is `www.qcloudtest.com`
- @: Directly resolve the main domain `qcloudtest.com`
- *: Wildcard resolution, matches all other domains `*.qcloudtest.com`

2) Record type. It is recommended to choose `CNAME Record`.

Each type of record is shown below:

- A Record: address record, which is used to specify IPv4 address of the domain (e.g. 8.8.8.8), if you need to direct the domain to an IP address, A Record must be added.
- CNAME：  You need to add CNAME Record if the domain is required to point to another domain which provides the IP address.
- TXT: You can enter anything here, the length limit is 255. Most TXT records are used as SPF records (anti-spam).
- NS: Domain server record. This is needed if you need to deliver the sub-domain to other DNS service providers for resolution.
- AAAA: Used to specify the corresponding IPv6 address (such as ff06:0:0:0:0:0:0:c3) record of the host name (or domain name).
- MX: This is need if you need to set up an e-mail to receive mails.
- Explicit URL: Explicit URL record is needed when an address 301 redirects to another address (Note: Currently DNSPod only supports 301 redirection).
- Implicit URL: Similar to explicit URL. The difference is that implicit URL will not change the domain in the address bar.
- SRV: Records which services are provided by certain computers. Format: <service name> + dot + <protocol type>. For example: _xmpp-server._tcp.

3) Line is used to direct users of specific lines to access this domain.

Choose [Default] if the domain provider only provided one IP address or domain.
Common usage:
- Default: Must be added, otherwise your website can only be accessed by specially specified lines. If it is dual-line resolution, it is recommended to enter [China Telecom IP] for [Default] line
- China Unicom: Specify server IP for [China Unicom Users]. Other users still access the [Default] one
- Search engines: Specify a server IP for web crawlers to capture.

4) For CNAME record, mainly enter the domain provided by your domain provider (i.e. domain you just purchased).

Record values of various types are usually like these:
- A Record: Enter your server IP. Please ask your domain provider.
- CNAME Record: Enter the domain provided by your domain provider.*** For example: Domain of the LB instance in cloud load balancer, 1b16c9-0.gz.12345678.clb.myqcloud.com***.
- MX Record: Enter the IP address of your e-mail server or the domain provided by your enterprise e-mail provider. Ask your e-mail service provider if you're not sure
- TXT Record:　Usually used in anti-spam configurations of enterprise e-mails (such as Google, QQ and so on)
- Explicit URL Record: Enter the URL to redirect to, for example: http://cloud.tencent.com
- Implicit URL Record: Enter the URL whose content is to be referenced, for example: http://cloud.tencent.com
- AAAA: Rarely used. IPv6 address to be resolved.
- NS Record:　Rarely used. Please do not modify the two NS records added by the system by default. NS downward authorization. Enter the DNS domain, for example: f1g1ns1.dnspod.net
- SRV Record:　Rarely Used Format: <priority>, space, <weight>, space, <port>, space, <host name>. Once the record is generated, it is normal that a "." will be added at the end. For example: 5 0 5269 xmpp-server.l.google.com.

For the other values, you can use their default. Click "OK" once you've completed the values.

![](//mccdn.qcloud.com/static/img/3d952308d0e576fa3a2be640b3238074/image.png)

### Viewing CNAME records

You can view the added CNAME records in "Resolution" page and perform actions such as modify, manage.

### Testing Resolution Result

To test whether the domain is resolved normally, users can directly access the bound CNAME domain (such as www.qcloudtest.com mentioned in the example). Note:  It will take about 10 minutes for the resolution to take effect.
