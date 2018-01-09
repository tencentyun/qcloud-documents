### The monitor project reports "the domain name cannot be resolved". What happened?
The processes for third-party monitoring and normal resolution are different.
**Normal resolution process:**
1. A regular regional DNS server sends requests to multiple NS server addresses at the same time and takes the fastest returned value. (Every NS address in Tencent Cloud contains at least 3 servers. Each package contains 2 NS addresses, which means more than 5 servers in total. The resolution will function as long as at least one of them returns result);
2. The process is retried for multiple times (usually 3 times) when connection error occurs.

**Third-party monitor project monitoring process:**
1. Capture one NS server address and send request. The other addresses are not tested;
2. No retry or only 1 retry when error occurs.
![](//mc.qcloudimg.com/static/img/a6d35a738914b4667055da73a01618d1/image.png)
Although the monitor project keeps reporting error, users can resolve to IP without problem.

### Users implement smart resolution at Tencent Cloud DNSPod to direct default lines to China Telecom server IP and direct China Unicom lines to China Unicom server IP. Why are the China Unicom users still resolved to China Telecom server IP?
1. First, make sure that you're not using Hangzhou WASU or Beijing Great Wall network lines.
2. If the resolution using DNSPod is performed within the last 72 hours, wait for the resolution to take effect.
3. If China Unicom  server is down, the D monitor automatically switch record values of China Unicom lines to China Telecom server IP. The record values are automatically switched back to China Unicom IP when the server is restored. 
4.Visit `http://ip.dnspod.cn` through a browser to diagnose if your computer's DNS is consistent with the line. If not, change your computer's DNS.
5. Check if your computer is set to direct hosts domain name towards a certain IP.

### Why is the resolution result of domain name different from the resolution IP?
You are recommended to go to DNSPod official website and go to "Help Center" -> "Quick Diagnose" to perform the diagnosis. If you changed domain name resolution provider within the last 72 hours and changed the space, wait for it to take effect.

### I changed the IP for my domain name. Why is the search engine spider still crawling the previous server?
A search engine updates itself at a fixed interval which is different for different engines. The shortest update interval is 1 week. After you change the domain name IP, wait for the search engine to update the information.
 
 
