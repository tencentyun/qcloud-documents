### How long does it take for a modified domain name DNS to take effect?
When you modify domain name DNS to point to a DNSPod domain name, although DNSPod servers take effect immediately, the domain name DNS refresh time for ISPs in different regions are different. Thus it usually takes 0-72 hours for the resolution to function globally.
### How long does it take for a modified domain name record to take effect?
In theory, it is the time equals to the TTL you set for the domain name record. However, certain regional ISPs may prolong domain name records by force, which may cause domain name records to take effect later than the time defined by TTL.
### Why isn't the resolution working?
There are generally two situations where we consider a resolution as "not working":
1. Page cannot be opened
The resolution works as long as there is returned error code on the page, in which case we need to check server configurations.
Common error codes are listed below:
(1) Website under construction
(2) Object not found
(3) Error 404
(4) Access forbidden
(5) Error 403
(6) Forbidden
The problem is not caused by resolution if you see the error codes mentioned above on the web page. Please check server configurations.
2. Domain name cannot be pinged. Here are the possible reasons:
i. The record isn't added correctly
If the default line type is not selected, certain users will not be able to access the domain name. The "Default Line" must be added, otherwise, only the line explicitly specified can access your website. If you use dual-line resolution, you are suggested to enter "China Telecom IP" for "Default" line.
ii. The modified domain name DNS hasn't taken effect
When DNS is modified, it takes some time (more than several hours) for the new one to take effect. Your IP cannot be pinged if the local ISP's DNS server hasn't completely refreshed your domain name record. When this happens, simply wait for some time (less than 48 hours).
iii. The DNS record of the domain name is cached
The cache can be located in Windows (all windows systems will do this), routers (when the Internet is accessed via a router), the DNS servers of local ISPs (DNS servers use recursive method).

**Solution:**
1. If your Windows accesses the Internet via direct dial-up, go to "Start" -> "Run" -> "ipconfig /flushdns", wait for half a minute and try to ping again.
 ![1](https://mc.qcloudimg.com/static/img/5df3391c4144c0cb0963481cee4f93f9/1.png)
2. If your device accesses Internet via a router, you need to clear the router's DNS cache. You can do this by restarting the router. If it doesn't work , you need to change the DNS server of Windows to another address.
>**Note:**
>Using this approach to clear the router also requires you to run the ipconfig /flushdns command. 

3. If all of the methods above failed, it means the DNS server of your local ISP cached the data, in which case you can solve the problem by changing your Windows DNS server to another address, or wait for the DNS server of local ISP to clear the cache (usually within an hour).
>**Note:**
>Linux and Unix systems do not cache DNS records. For Mac OS X system, you can clear DNS cache by using "killall lookupd".

### Why can I still ping my IP after the record is deleted/paused?
This is because the server (recursive server) of the local ISP provider cached the record. In theory, the cache will expire after the TTL set for the record before has elapsed.
