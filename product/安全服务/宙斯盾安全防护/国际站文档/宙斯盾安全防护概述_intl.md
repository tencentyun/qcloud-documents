## **Overview**
Leveraging Tencent's over a decade of experience in security accumulated from various lines of business, Tencent Cloud Aegis Anti-DDoS is a multi-layer, all-around, cost-effective protection solution against DDoS attacks for your business. It is capable of precise purge of various types of network attack traffic and directing of normal traffic to business servers, preventing business fluctuations, service interruptions and user experience downgrading caused by potential DDoS attacks. In addition, it features protective resources at the Tbps level, dedicated protective clusters and customizable advanced security policies to ensure uninterrupted fast development of your business.

## **Pricing**
Tencent Cloud Aegis Anti-DDoS uses a mixed billing model. Peak bandwidth for base protection is prepaid on a monthly basis, while peak bandwidth for elastic protection and forwarded business traffic are postpaid on a daily basis. For more information, see [Product Pricing](https://cloud.tencent.com/document/product/685/15262).

## **How to Use**
Tencent Cloud Aegis Anti-DDoS has web-based UIs (i.e. console). If you have already signed up for a Tencent Cloud account and applied for Aegis Anti-DDoS [whitelist](https://cloud.tencent.com/act/apply/Aegis), you can log in to Aegis Anti-DDoS Console to perform various operations.

## **Related Concepts**
The following concepts are usually involved in Aegis Anti-DDoS:
- **DDoS**
This is short for distributed denial-of-service, a network attack technique that uses network resources to initiate service requests to specific target servers and makes end user's normal service requests impossible to be completed by exhausting the bandwidth or other resources of the target servers.
- **IP blocking**
If the DDoS attack traffic exceeds the peak bandwidth for protection set by the user, Aegis Anti-DDoS will block all service requests to the attacked target servers for a period of time.
- **BGP network**
This is the type of network directly connected to the Internet AS using the Border Gateway Protocol (BGP). Tencent Cloud's BGP links are connected to 28 ISPs, eliminating cross-network latency and enabling an excellent network access experience.
- **MUT network**
This refers to the non-BGP networks of China Mobile, China Unicom and China Telecom. They provide static IP resources, and non-local users need cross-network access when using these resources.
- **Forwarding rule**
This is to configure the rule according to which the business request first accesses the high-defense IP's service port and then is forwarded to the origin server port of the origin server's IP address. Port forwarding rules can be configured and origin server polling by weight or by minimum number of connections is supported.
- **Origin-pull exit IP address**
This is the exit IP address used when forwarding the business request from the high-defense IP to the origin server. If relevant security policies are configured for the origin server, the exit IP address should be added to the whitelist to avoid mistaking normal requests for attacks.
- **Peak bandwidth for protection**
This is divided into peak bandwidth for base protection and peak bandwidth for elastic protection. If optional elastic protection is chosen, the peak bandwidth for protection is the highest peak bandwidth that can protect against the actual attacks. If the attack traffic exceeds the highest peak bandwidth for protection, the system will temporarily block the attacked IPs.
- **Region**
This refers to the region where a high-defense IP or high-defense packet is available. It is recommended to choose the region closest to the origin server. High-defense packet can only be bound to the Tencent Cloud public IP addresses in the same region where it is available.

## **Related Services**
- **DDoS high-defense IP**
This is a large-traffic DDoS protection service for Tencent Cloud customers (including off-cloud servers). The high-defense IP is used as the access point for the business traffic. The backend protection system checks the traffic and performs traffic purges if any DDoS attacks are detected, and then forwards the normal business request to the origin server of the business.
- **Protective domain name**
Protective domain name is provided free of charge when the user creates a business in the console. The user can configure the CNAME of their primary domain name to resolve to the protective domain name for easy access. Resolution to the high-defense IP can be turned on for the protective domain name to enable smart resolution based on request source.
- **DDoS high-defense packet**
This is an enhanced DDoS protection service for Tencent Cloud customers' in-cloud servers. It works in single-IP or multi-IP mode. Single-IP high-defense packet can be bound to one Tencent Cloud public IP, while multi-IP high-defense packet can be bound to multiple Tencent Cloud public IPs.
