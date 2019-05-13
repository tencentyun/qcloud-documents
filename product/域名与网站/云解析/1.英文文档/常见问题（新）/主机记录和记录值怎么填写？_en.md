**Host Name:**
A host name is the prefix of a domain name. Common usage is as follows:
**www:** Domain name after resolution is www.87677677.com
**@:** Primary domain name 87677677.com is directly resolved
***:** Pan resolution, in which case all other domain names *.87677677.com are matched

**Record Types:**
Choose A record for pointing towards IP address provided by server provider. Choose CNAME record for pointing towards a domain name.
**A Record:** Address record, which is used to specify IPv4 address of the domain name (e.g. 8.8.8.8). If you need to point the domain name to an IP address, you must add an A record.
**CNAME Record:** You need to add CNAME record if the domain name is required to point to another domain name which provides the IP address.
**NS Record:** Domain name server record. It should be added if you need to deliver the sub domain name to other DNS service providers for resolution.
**AAAA Record:** This is used to specify the corresponding IPv6 address (such as ff06:0:0:0:0:0:0:c3) record of the host name (or domain name).
**MX Record:** It should be added if you need to set up an e-mail to receive emails.

**Line:** It allows users of specific lines to access this IP.
Common usage:
**Default:** Must be added, otherwise only lines specially specified can access your website. It is recommended to enter "China Telecom IP" as "Default" for dual-line resolution.
**China Unicom:** Specify server IP for "China Unicom Users". Other users still access the "Default" one.
**Search Engine:** Specify a server IP for web crawlers to capture.

**Record Value:** The IP address provided by server provider is usually entered here. Common record values for different types are shown below:
**A Record:** Enter your server IP. If you are not sure about this, please ask your server provider for help.
**CNAME Record:** Enter the domain name provided by your server provider (such as 2.com).
**MX Record:** Enter the IP address of your e-mail server or the domain name provided by enterprise e-mail provider. If you are not sure about this, ask your e-mail service provider for help.
**AAAA Record:** (Not commonly used) IPv6 address to which a domain name is resolved.
**NS Record:** (Not commonly used) Do not modify the two NS records provided by the system by default. It is used for NS downward authorization. Enter the DNS domain name, such as ns3.dnsv3.com.
**TTL:** Time to live for caches. This is the duration for regional DNS caches to keep your domain name record information. When the cache is expired, it acquires record value from DNSPod again. The default TTL (600 seconds) is most commonly used and does not need to be changed.
600 (10 minutes): It is recommended to use 600 in normal conditions.
60 (1 minute): Use this if you change your IP frequently, so the changed record can take effect after 1 minute. Using this option for a long term may affect resolution speed. 3,600 (1 hour): It is recommended to use 3,600 for faster resolution if your IP rarely changes (several times in a year). In case you need to modify IP, change this option to 60 a day in advance to allow the modification to take effect quickly.
