### What Is Custom Resolution?
Custom resolution allows you to define an IP range to access the specified server.

> **Note:**
> The IP range to be defined must be IPs of user's recursive DNS;
> An IP of recursive DNS is the outgoing IP of the DNS of a client that is accessing the Internet (i.e. the backend IP);
> You need to collect the backend DNS range by yourself.

### How to Collect IPs of Recursive DNS (Outgoin IPs of DNS)?

Access `http://ip.dnspod.cn/` using the client that configures the DNS address, and click "Start Detection". Whois will obtain the server address and you will see the outgoing IP range of the DNS. For example, the IP range obtained by Whois 219.141.136.10 is: 219.141.128.0 - 219.143.255.255.
>**Note:**
> It is suggested to refresh the detection for multiple times to avoid missing any missed IPs.

### When Do I Need to Use Custom Resolution?

Enable custom resolution if you need to differentiate the lines further, or define an IP range to access the specified server, or block the users from a certain DNS/region to access your website.
> **Note:**
> Custom Lines have higher priority than System-defined Lines;
> Google DNS still follows Google extension protocol.


