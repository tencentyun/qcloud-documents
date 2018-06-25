### How to add a domain name for a server?
Purchase a domain name, then add an A record which is pointed to your server in the domain name console. For more information, please see [domain name-related instructions](https://cloud.tencent.com/document/product/242).

### What need to be done if a domain name is inaccessible?
This may be caused by the security group configuration which doesn't allow the public network access your server's port 80. In this case, you need to configure your security group in the console. For more information, please see [security group-related instructions](https://cloud.tencent.com/document/product/213/5221).

### How long does it take for the modified Tencent Cloud DNS to take effect?
Tencent Cloud DNS is `f1g1ns1.dnspod.net f1g1ns2.dnspod.net`, and a modified DNS takes effect in 0-72 hours.

### Is there a limit on the number of domain names that can be resolved with Tencent Cloud DNS service?
No.

### Why does the resolution of a domain name transferred from someone else's account failed?
Log in to Tencent Cloud Console and go to **Cloud Products** -> **Cloud DNS** and then click **Add Resolution** to conduct the resolution. If the **Domain Name Retrieval** dialog box appears, proceed with the operation.

### The Tencent Cloud domain name was renewed the next day after expiration and the DNS was not changed. Why didn't the resolution work?
DNS becomes invalid upon the expiration of domain name, and it takes 0-72 hours for the DNS to take effect after renewal.

### How to check the operation log for domain name resolution?
Log in to Tencent Cloud [Console](https://console.cloud.tencent.com/), and go to **Cloud Products** -> **Domain Names and Websites** -> **Domain Name Management** -> **Management** -> **Operation Log** to view the operation log.

### What need to be done if domain name status is "serverHold" and resolution is suspended by the registry?
This may occur if the identity verification is not completed. Check if the identity verification for the domain name is completed. The resolution will resume after the identity verification is completed. If you have already completed the identity verification, [submit a ticket](https://console.cloud.tencent.com/workorder/category) for the assistance from our specialists.

### How long does it take for a new resolution record to take effect?
A new resolution record takes effect immediately after being added (sometimes with a delay of several minutes). This depends on the TTL value you set.

### What is the reason for the message "You haven't been registered as a cloud DNS user yet" when I add a domain name resolution?
This is because you have not completed qualification verification information in the cloud platform. You need to complete qualification verification before you can perform the operation. Log in to **User Center** -> **Account Information**, fill in all the required information and upload required certificates. You can perform cloud DNS operations immediately after the verification is completed successfully.

### What need to be done if the message "System is busy. Try again later" appears when I add a cloud DNS record?
This is because the domain name resolution already exists. Log in to Tencent Cloud [Console](https://console.cloud.tencent.com/) -> **Cloud Products** -> **Domain Name Management** to go to domain name console and click **Resolution** in the domain name list to check whether the domain name resolution exists. If not, [submit a ticket](https://console.cloud.tencent.com/workorder/category) for the assistance from our specialists.

### How long does it take for a modified domain name record DNS to take effect?
This depends on the cache refresh time of DNS servers of ISPs in different regions (the resolution records prior to modification are cached on the DNS servers of ISPs in different regions and are not updated in real time). In most cases, the time equals to the TTL you set for the resolution. In some regions, forced cache is implemented. In this case, it depends on how long the forced cache lasts.

### When I perform an A record resolution in Cloud DNS for a domain name purchased from www.net.cn, the console shows that the A record resolution is already added. Why doesn't the resolution take effect when I ping the domain name?
After adding a domain name in Cloud DNS, you need to go to www.net.cn to change the DNS address into `f1g1ns1.dnspod.net f1g1ns2.dnspod.net` provided by Cloud DNS before you can add the record value. If the DNS address on www.net.cn is not changed, it will be confused with the one provided by Cloud DNS, and the record value added doesn't take effect.

### What does the TTL in a resolution record mean?
TTL (Time to Live) refers to how long the local DNS caches your domain name record information. The cache acquires record values again from the DNS server when it expires.

### Why does the CNAME resolution fail after a dot (.) is automatically added?
When you add a CNAME record, the record value is the domain name to which the CNAME points. You can only enter a domain name. A "." is added to the domain name automatically when the record is generated. This is normal and does not affect the resolution. Check whether other information or settings are correct. For more information, please see [CNAME Record](https://cloud.tencent.com/document/product/302/3450) on our official website. For any questions, please contact us.

### The 6-GB anti-attack protection and maximum protection capacity of 50 GB are provided in the cloud DNS package for enterprises. What do they mean?
The 6-GB anti-attack protection provided in the cloud DNS package for enterprises means the protection can defend against any attacks arising from domain name resolution, including domain name hijacking, cache poisoning, DDOS attacks, DNS attacks, etc. The maximum protection capacity means the package can provide protection for 50 GB traffic at most. When the 6-GB free capacity is used up, you need to make a payment to use the additional protection capacity.

### Are dynamic resolutions of domain name supported?
Yes. Dynamic resolutions require the use of [client](https://support.dnspod.cn/Kb/showarticle/tsid/19/) or [calling API](https://www.dnspod.cn/docs/records.html#dns).

### How to upgrade the existing DNS package to a higher level?
Go to the cloud DNS package management page, click **Upgrade Package**, choose the package you want, and then pay the price difference.







