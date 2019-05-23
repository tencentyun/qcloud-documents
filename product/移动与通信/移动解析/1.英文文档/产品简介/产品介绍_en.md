### What is HttpDNS?
HttpDNS sends domain name resolution requests to Tencent cloud DNS servers through HTTP protocol. Compared with traditional DNS service that implements resolution by accessing ISP LocalDNS, HttpDNS avoids domain name hijacking and cross-network access problems caused by LocalDNS, and solves domain name resolution exception in mobile Internet services.
With years of technology experience and supported by DNSPod, HttpDNS has provided reliable services for over 400 million users.

### What problems can HttpDNS solve?
HttpDNS can solve DNS resolution exception and domain name hijacking in mobile Internet:
- Status quo of mobile DNS: The LocalDNS export of ISP performs NAT according to the destination IP address of authoritative DNS, or forwards resolution requests to other DNS servers. This may cause that the authoritative DNS cannot correctly identify LocalDNS IP of ISP, resulting in domain name resolution failure and cross-network traffic.
- Consequences of domain name hijacking: Websites cannot be accessed (cannot connect to the server) and phishing sites may be accessed.
- Consequences of cross-domain, trans-provincial, cross-ISP or cross-border result resolution: The access is very slow, or the website cannot be accessed.

### How does HttpDNS work?
- Client directly accesses HttpDNS API to obtain the optimal IP of domain name. (Considering disaster recovery, it is recommended to use ISP LocalDNS as an alternative to resolve domain name.)
- When a business IP is obtained, the client sends business protocol requests to this IP. Take HTTP request as an example. Through specifying Host field in header, the client can send standard HTTP request to the IP returned by HttpDNS.

### Quality of HttpDNS service
HttpDNS service ensures high availability and fast response
- BGP Anycast network is deployed: HttpDNS deploys BGP Anycast network architecture and establishes BGP interconnection with Top 17 ISPs in China, enabling quick forwarding of user requests of all ISPs to HttpDNS servers. As more and more ISPs are connecting with HttpDNS, fast service response can be guaranteed.
- Remote disaster recovery and real-time failover: HttpDNS deploys multiple nodes in IDCs of North China, East China and South China. If any node fails, it can seamlessly switch to a backup node to ensure high availability of services.

### Features of HttpDNS Enterprise Edition
- Self-developed intelligent SDK (available for iOS and Android) with a coverage of over 100 million users
- Supports Encryption
- 99.99% availability guaranteed by SLA
- Unlimited queries
- Provides user access distribution report
- Supports edns-client-subnet
- Provides technical support via Ticket system and phone calls

