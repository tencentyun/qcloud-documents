## What is reverse resolution?
Reverse domain name resolution means to map an IP address to a domain name. Since a normal resolution is to map domain name to an IP address, if you need to confirm whether an IP corresponds to one or multiple domain names, you need to traverse the entire domain name system starting from this IP, which is impossible. Thus, RFC1035 defined Pointer Record (PTR). PTR is a data type in the email system, and it corresponds to A record. PTR points an IP address to a domain name.
## When to use reverse resolution?
Reverse resolution is mainly used in email servers. Enable reverse resolution to reject all messages from unregistered domain names. As most spam emails are sent from dynamic IPs or IPs without registered domain names to avoid being tracked down, you can set the email server to reject messages sent from IP addresses that cannot be reversely resolved to domain names, in order to filter out spam emails.
## How does Tencent Cloud realize reverse resolution?
From the descriptions above we can say that reverse resolution cannot be done by DNS service providers. You need to apply to ISPs to add reverse resolution. Thus Tencent Cloud __only supports reverse resolution for IP addresses that belong to Tencent Cloud resources__. Meanwhile, reverse resolution is only available for VIP enterprise customers for now. And you need to submit a [ticket](https://console.cloud.tencent.com/workorder/category/create?level1_id=16&level2_id=17&level1_name=%E5%85%B6%E4%BB%96%E6%9C%8D%E5%8A%A1&level2_name=%E5%9F%9F%E5%90%8D) to apply.
Other developers are suggested to use third-party enterprise emails.

>**Note:**
>When submitting a ticket, please provide the domain name and public IP (which should belong to Tencent Cloud resources) to Tencent Cloud engineers.

