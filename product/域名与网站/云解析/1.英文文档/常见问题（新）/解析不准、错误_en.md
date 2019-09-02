### The monitoring project reports "The domain name cannot be resolved" - What is the reason for this?
The third-party monitoring process is different from the general resolution process.
**Normal resolution process:**
1. Generally, a local DNS server sends a request to multiple NS server addresses at the same time and takes the first returned value. (Each NS address in Tencent Cloud contains at least 3 servers and each package contains 2 NS addresses. This means there are more than 5 servers in total. The resolution works as long as one of the servers returns result);
2. When a connection error occurs, multiple retries will be performed (usually 3 retries).

**The third-party monitoring process:**
1. Send the request to only one NS server address without testing other addresses.
2. No retry or only one retry is performed when an error occurs.
![](//mc.qcloudimg.com/static/img/a6d35a738914b4667055da73a01618d1/image.png)
Although the monitoring project keeps reporting error, user can resolve to the IP without an error.

### An intelligent resolution has been implemented with Tencent Cloud DNSPod, with the default line directed to China Telecom server IP and China Unicom line to China Unicom server IP - Why are the China Unicom users still resolved to China Telecom server IP?
1. First, make sure that you're not using Hangzhou Wasu or Beijing GreatWall Broadband Network lines.
2. If the DNSPod resolution has been performed for less than 72 hours, wait for the resolution to take effect.
3. If China Unicom server is down, D monitoring automatically switches record values of China Unicom lines to the China Telecom server IP. When the server is restored, the record values are switched back automatically to China Unicom IP. 
4. Visit `http://ip.dnspod.cn` through a browser to verify whether your computer's DNS is matched with the line. If not, change the DNS.
5. Check if your computer is set to direct hosts domain name to a certain IP.

### Why is the result of domain name resolution different from the resolution IP?
It is recommended to go to Cloud DNS **Detection Tools** -> **Domain Name Diagnosis** for a diagnosis. If you have changed DNS service provider for less than 72 hours and changed the IP, wait for it to take effect.

### Why does the search engine spider still crawl the previous server after the IP of the domain name is changed?
The update period varies with different search engines and the shortest one is 1 week. It takes some time for a search engine to complete the update when the IP of a domain name is changed.
 
 
