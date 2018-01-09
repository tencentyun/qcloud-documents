### How to add domain name for a server?
Purchase a domain name, then add an A record in domain name console which is pointed to your server. For more information, please see [domain name-related instruction](https://cloud.tencent.com/document/product/242).

### What if my domain name is inaccessible?
This may be caused by the security group configuration which doesn't allow accesses to your server's Port 80 via public network. Go to the console and configure your security group first. For more information, please see [security group instructions](https://cloud.tencent.com/document/product/213/5221).

### How long does it take for the modified Tencent Cloud DNS to take effect?
Tencent Cloud DNS is `f1g1ns1.dnspod.net f1g1ns2.dnspod.net`, and a modified DNS takes effect in 0-72 hours.

### Is there a limit to how many domain names can be resolved in Tencent Cloud?
No.

### Why does the resolution of a domain name transferred from someone else's account failed?
Log in to Tencent Cloud console and go to **Cloud Product** -> **Cloud DNS** and then click **Add Resolution** to proceed with the corresponding resolution. If you encounter a Domain Name Retrieval dialog box, simply proceed with it.

### I renewed my Tencent Cloud domain name a day after expiration and did not change the DNS. Why is the resolution not working?
DNS will become invalid upon the domain name expiration, and it takes 0-72 hours for the DNS to take effect after renewal.

### How to check the operation log for domain name resolution?
Log in to Tencent Cloud [console](https://console.cloud.tencent.com/), go to **Cloud Product** -> **Domain Names and Websites** -> **Domain Name Management** -> **Management** -> **Operation Log** to view the record of resolution that were performed before.

### What can I do if my domain name status is "serverHold"?
First, check if the identity verification for the domain name is completed. This may occur if the identity verification is not completed. Your resolution will resume after its completion. If you have already completed the identity verification, [submit a ticket](https://console.cloud.tencent.com/workorder/category) to our professional staff who for help.

### How long does it take for a new resolution record to take effect?
A new resolution record usually takes effect immediately (sometimes with a delay of several minutes). This is determined by the TTL value you set.

### Why did it say "You haven't registered as a cloud domain name resolution user" when I tried to add a domain name resolution?
This is because you have not completed qualification certification information in the cloud platform. You need to complete qualification certification information before you can perform operations on cloud resolution product. Log in to User Center and go to **Account Information**, fill in all required information and upload related certificates. You will be able to perform cloud resolution operations once the certification is approved.

### What if I'm prompted "System is busy. Try again later" when I try to add a cloud resolution record?
This is because the domain name resolution already exists. Log in to Tencent Cloud [Console](https://console.cloud.tencent.com/) and go to **Cloud Product** -> **Domain Name Management** to enter domain name console and click **Resolution** in the domain name list to check whether the domain name resolution exists or not. If not, [submit a ticket](https://console.cloud.tencent.com/workorder/category) to contact our professional staff for help.

### How long does it take for a modified domain name record to take effect?
This depends on the cache refresh time of DNS servers of the ISPs in different regions (the resolution records before modification are cached on the DNS of ISPs in different regions and they are not updated in real time). In most cases, the time equals to the TTL you set for the resolution. The servers in certain regions implement forced cache, whose period determine when the modification takes effect.

### When I perform the A record resolution in the Cloud DNS platform for a domain name I purchased from www.net.cn, the console shows that the A record resolution is already added. But why doesn't the resolution work when I ping my domain name?
When adding domain name in the Cloud DNS platform, you first need to go to www.net.cn and change the DNS address into `f1g1ns1.dnspod.net f1g1ns2.dnspod.net` (provided by Cloud DNS), then add the record value. If the DNS address is not changed, the resolution will become confused because www.net.cn and Tencent Cloud DNS provide two different sets of DNS addresses, and the record value you added doesn't take effect.

### What is "TTL" in a resolution record?
TTL (Time to Live) refers to how long the regional DNS caches your domain name record information. The record value is obtained from the DNS server again when the cache expires.

### Why does the CNAME resolution fail after a dot(".") is automatically added?
When you add a CNAME record, the record value is the domain name to which the CNAME points. You can only enter a domain name here. A "." is added automatically after the domain name when the record is generated. This is normal and does not affect the resolution. Check whether other information or settings are correct. For detailed operation instruction, please see the tutorial about [CNAME record](https://cloud.tencent.com/document/product/302/3450) on our official website. Please feel free to call us if you have any questions.

### What does the "6 GB attack protection" and "50 GB maximum protection capacity" in enterprise DNS package mean?
The 6 GB attack protection mentioned in enterprise DNS package means that any attacks that come from domain name resolution can be prevented. For example: domain name hijacking, cache poisoning, DDOS attacks, DNS attacks and so on. The 50 GB maximum protection capacity means that the package can provide protection for 50 GB of traffic at most. When the free capacity (6 GB) is used up, you need the pay for additional protection capacity.

### Is the domain name resolution dynamic?
Dynamic domain name resolution is supported. Using this feature requires support of [client](https://support.dnspod.cn/Kb/showarticle/tsid/19/) or [call of API](https://www.dnspod.cn/docs/records.html#dns).

### How do I upgrade the DNS package I just purchased into a better one?
Go to the Cloud DNS package management page, click **Upgrade Package**, choose the package you want and pay the price difference.







