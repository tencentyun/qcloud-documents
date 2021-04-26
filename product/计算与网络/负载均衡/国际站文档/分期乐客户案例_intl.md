>**Note:**
> [FenQiLe] is an online shopping mall and financial service provider focusing on shopping by installments of college students. It provides installment loans and repayment services. Aiming at creating an "installment shopping mall that is most trusted by the young people", the company provides high-growth people with the latest installment buying and consumption method through a simple and fast handling process.

![](//mc.qcloudimg.com/static/img/5607fd04d0d9592131f8d72b759b5c75/image.png)

## 1. Original Architecture and Its Problems

The original e-commerce portal of fenqile.com has more than 30 business modules, which are separated by multiple second-level domain names and public network IPs. The daily PV of the portal exceeds 100 million, and its peak bandwidth exceeds 5 GB. Therefore, in addition to service performance, it is important to deal with traffic during peak period. The original program was to deploy nginx in IDC as the load balancer of the access layer. However, there existed problems such as frequent packet loss, inaccurate matching of secondary domain names, and slow domain name resolution. Therefore, FenQiLe hopes to use the cloud load balancer service to guarantee a smooth service for promotion on November 11th.

## 2. Specific Solution

Tencent Cloud's [Public Network Application-based Cloud Load Balancer](https://cloud.tencent.com/product/clb.html) products were mainly applied in the big smooth promotion. FenQiLe experienced the application-based cloud load balancer as an early invited customer. Specifically, Tencent Cloud provided the following solutions for FenQiLe, which ensured steady traffic distribution during the school promotion in September and promotion on November 11th for FenQiLe.
![](//mc.qcloudimg.com/static/img/a2239aeb6f3373b779ba1b5b19d617d5/image.png)

### 	Provide content-based routing forwarding capability

Public network application-based cloud load balancer can obtain HTTP header information, and route requests to different RS clusters according to the actual needs of the user. Therefore, the cloud load balancer can perform content-based routing forwarding to achieve business separation. Meanwhile, public network application-based cloud load balancer can provide fine health check at the forwarding group level, which is more flexible and can meet the needs of multiple business scenarios. **On the day of the promotion, the daily PV of the portal exceeded 100 million, and the peak bandwidth exceeded 5 GB, and the transaction amount exceeded USD 15 million.**

For example, in the business architecture of FenQiLe, content-based routing forwarding is achieved by customizing the domain name/URL. According to the types of business, FenQiLe configures two URL paths: a.fenqile.com/image and a.fenqile.com/text. Public network application-based cloud load balancer can identify the request content, forward the requests with suffix of /image to the RS group 1, and forward the requests with suffix of /text to the RS group 2.

### 	Increase access speed and reduce DNS polling

Tencent Cloud public network application-based cloud load balancer allows users to replace second-level domain names with custom forwarding paths, thus effectively reducing DNS polling, improving user access speed, and ensuring efficient service operation. For mobile App clients, the access speed of FenQiLe **increases 15% or higher.**

For example, in the service architecture of FenQiLe, the original services are hosted by a.fenqile.com and b.fenqile.com. With the public network application-based cloud load balancer, only the two forwarding rules (a.fenqile.com/a and a.fenqile.com/b) are required, thus greatly reducing the use of second-level domain names and DNS polling.

### 	Hybrid cloud solution with direct connect

Tencent Cloud Hybrid Cloud provides enterprises with massive computing, storage, CDN, network and other resources. With flexible weight configuration, the business is gradually migrated to the cloud. In combination with data transmission of Direct Connect, Tencent Hybrid Cloud enables enterprises to implement flexible, fast, highly reliable, and low-cost service deployment.

For example, FenQiLe has achieved the following advantages by using Tencent Cloud Hybrid Cloud solution:
- FenQiLe can gradually migrate the business to the cloud. Taking the domain name mall.fenqile.com/iphone as an example, 30% of the traffic is migrated to Tencent Cloud, and 70% of the traffic goes back to IDC based on weight ratio. As the business operates stably, FenQiLe can gradually increase the weight on the Tencent Cloud to smoothly replace the existing IDC services.
- The cloud-based data center can achieve autoscaling. That is, when the traffic increases, the backend CVM can be scaled out horizontally in time to effectively respond to the sudden increase in traffic.
- Connect user IDC and Tencent Cloud with VPC high-speed channel (DC) or VPN to ensure high-speed and stable data transmission.
