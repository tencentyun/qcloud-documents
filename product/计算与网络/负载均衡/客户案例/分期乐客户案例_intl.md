
> [Fenqile.com] is an online shopping mall and financial service provider which is committed to offering installment loans and repayment services to young people to cater for their installment buying needs. Aiming at "building the most trusted installment shopping mall for young people", the company provides the high-growth population with the most fashionable installment shopping and consumption experience and a fast, straight-forward transaction process.

![](//mc.qcloudimg.com/static/img/5607fd04d0d9592131f8d72b759b5c75/image.png)
 
## 1. The Old Architecture and Problems

The old e-commerce portal of fenqile.com owned more than 30 business modules, which were separated from each other through multiple secondary domains and public IPs. The portal had a daily PV of 100 million and its peak bandwidth exceeded 5GB. How to deal with the traffic during peak period while ensuring the service capabilities became an important consideration. The company originally deployed Nginx in their IDC by themselves to perform load balancing at the access layer, which led to a series of problems such as frequent packet loss, inaccurate matching of secondary domain names, slow domain name resolution, etc. Therefore, Fenqile desired to rely on the load balance service of a cloud platform to guarantee the success of promotion campaign on Double 11 Day.

## 2. Solution

Thanks to Tencent Cloud's [Public Network Application-based Cloud Load Balancer](https://cloud.tencent.com/product/clb.html), the company's promotion campaign on Double 11 Day achieved a success. Since the product was still under alpha test, Fenqile was invited to experience the product as its earlier-stage tester. Specifically, Tencent Cloud provided Fenqile with the following solutions to ensure the stable traffic distribution during the promotion campaigns for September School Days and Double 11 Day.

![](//mc.qcloudimg.com/static/img/a2239aeb6f3373b779ba1b5b19d617d5/image.png)
 
### 1) Provide content-based routing and forwarding capabilities

Public network application-based cloud load balancer can obtain the HTTP header information, and route the request to different CVM clusters according to the user's actual needs, so that the load balancer can provide routing and forwarding based on content to achieve business separation. In addition, the public network application-based cloud load balancer can provide health check down to the forwarding group level, delivering a greater flexibility to deal with a variety of business scenarios. ** On the day of promotion campaign, the portal's daily PV reached above 100 million and its peak bandwidth exceeded 5GB, paving the way for the trade volume of over RMB 100 million.**

For example, Fenqile's business architecture achieves content-based routing and forwarding through custom domains/URLs. According to the business type, Fenqile is configured with two URLs - a.fenqile.com/image and a.fenqile.com/text. The public network application-based cloud load balancer identifies the request content, forwards the requests with a suffix of /image to the backend CVM Cluster 1, and forwards the requests with a suffix of /text to the CVM Cluster 2.

### 2) Increase visiting speed and reduce DNS round robins

Tencent Cloud's public network application-based cloud load balancer allows the user to customize forwarding path in replace of the secondary domain name, so as to effectively reduce DNS round robins, increase user's visiting speed and ensure the efficient operation of service. The speed of visit to Fenqile. com from mobile app is **increased by more than 15%.**

For example, in Fenqile's business architecture, the services that were hosted by a.fenqile.com and b.fenqile.com previously are just hosted by the forwarding rules a.fenqile.com/a and a.fenqile .com / b now after the public network application-based cloud load balancer service is used, thereby significantly reducing the use frequency of the secondary domain names and number of DNS round robins.

### 3) Direct Connect hybrid cloud solution

Tencent Cloud's hybrid cloud provides enterprises with massive computing, storage, CDN, network and other resources. The combination of flexible weight configuration which allows the businesses to be migrated to the cloud step by step and the data transmission based on Direct Connect makes it possible for the company to achieve a flexible, fast, highly reliable and low-cost business deployment.

For example, Tencent Cloud's Direct Connect hybrid cloud solution provides the following advantages for Fenqile:

- The customer can gradually migrate their businesses (such as the domain mall.fenqile.com/iPhone) to the cloud by first migrating 30% of the traffic to Tencent Cloud and leaving 70% of traffic to the IDC through configuration of weight ratio. When the businesses maintain a stability, Tencent Cloud takes over the remaining services smoothly from the original IDC with its weight increasing gradually.

- With Cloud IDC's autoscaling capability, backend CVMs can be scaled out timely in case of a traffic surge to effectively cope with the business scenarios where a traffic burst occurs.

- VPC high-speed channel (Direct Connect) or VPN connects user's IDC with Tencent Cloud to ensure a high-speed and reliable data transmission.

