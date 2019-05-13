
## CNAME Domain Name



When Tencent Cloud's CDN console has been connected with the acceleration domain name, the system will assign a "CNAME domain name" (in a form of \ *. Cdn.dnsv1.com) to the domain name. Users need to set a CNAME record at domain name service provider. When the record takes effect, domain name resolution will be turned over to Tencent Cloud CDN, with all the requests of the domain name transferred to Tencent Cloud CDN nodes.



## CNAME Record



CNAME record refers to the Canonical Name record in a domain name resolution.



## Edge Node



Edge node refers to the CDN node that is closest to the user (also called "primary cache node"). Edge node is the network node to which the end user needs fewer intermediate steps to connect and provides a better responsiveness and faster connection speed.



## Origin Server

Origin Server refers to customer's business server.



## Intermediate Origin



Intermediate Origin refers to the back-to-origin server (also called "secondary cache node") between the business server (origin server) and CDN node. The intermediate origin server can cache the back-to-origin access of CDN node and reduce the access load on service server (origin server).



