## What is Tencent Cloud Virtual Private Cloud?
Tencent Cloud Virtual Private Cloud (VPC) is a customized network space on Tencent Cloud that is logically isolated, which is similar to the traditional network you run in the data center. The service resources hosted in Tencent Cloud VPC include [Cloud Virtual Machine](https://cloud.tencent.com/doc/product/213/495), [Cloud Load Balance](https://cloud.tencent.com/doc/product/214/524), [Cloud Database](https://cloud.tencent.com/doc/product/236) and other resources of Cloud Services in your Tencent Cloud. You can fully control your VPC environment, including customizing network segmentation, IP address and routing policy, and achieve multi-layer security protections through [Network ACL](https://cloud.tencent.com/doc/product/215/5132) and [Security Group](https://intl.cloud.tencent.com/document/product/213/5221) and so on. At the same time, you can also use [IPsec VPN](https://cloud.tencent.com/doc/product/215/4956)/Direct Connect to connect the VPC with your data center, and deploy hybrid cloud flexibly.

## Why would a customer choose Tencent Cloud Virtual Private Cloud?
- **No need to purchase network device, simplified O&M**----In Tencent Cloud VPC, you can customize network segmentation, create subnet, configure routing table and gateway through the console or API, using software to define network, and saving device and O&M costs.
- **Global deployment, cross-account connection**----Through [Peering Connection](https://cloud.tencent.com/doc/product/215/5000) service, you can connect the cloud resources in multiple regions around the world within one minute, easily achieving "One Server Covering the Globe" and the disaster recovery deployment at "Two Regions, Three Centers". At the same time, through cross-account peering connection, you can also achieve data interconnection with other partners in Tencent Cloud to quickly build open cloud ecosystem.
- **High-performance and flexible Internet access**----You can easily break the Internet access performance bottleneck with [NAT Gateway](https://cloud.tencent.com/doc/product/215/4975), which supports 10,000,000 concurrent connections and 5 GB bandwidth master/slave hot backup. You can also flexibly bind cloud resource services by using [Elastic IP](https://intl.cloud.tencent.com/document/product/213/5733) to easily configure which instances can access the Internet.
- **Deploy hybrid cloud easily**---- You can connect Tencent Cloud Virtual Private Cloud to your data center with stable and reliable [IPsec VPN](https://cloud.tencent.com/doc/product/215/4956)/Direct Connect. By flexibly expanding the CVM and other resources of the application according to business volume, you can reduce the IT O&M costs of the enterprise without worrying about the proliferation of core data, and build a hybrid cloud easily.
- **All-round security**----Tencent Cloud VPC is a network environment that the private and public networks are isolated. It could control network traffic from subnet and CVM dimensions respectively through [Network ACL](https://cloud.tencent.com/doc/product/215/5132) and [Security Group](https://intl.cloud.tencent.com/document/product/213/5221), providing access control with protocol-level and port-level granularity, and meeting your network security requirement in a multi-dimensional and all-round manner.

## Choose VPC or basic network?
The network types of Tencent Cloud are classified as VPC and basic network:
- The basic network is the resource pool of public network for all users on Tencent Cloud (as shown in the left figure). All private IPs of [Cloud Virtual Machine](https://cloud.tencent.com/doc/product/213/495) are assigned by Tencent Cloud. It is easy to configure and convenient to use, suitable for scenarios that have high usability requirements and need to get started with the CVM quickly.
- Virtual Private Cloud refers to a logically isolated network space built by user on Tencent Cloud (as shown in the right figure). Users can customize network segmentation, IP address and routing policy in the VPC. Compared with the basic network, VPC is more suitable for the scenarios that have network custom configuration requirements.
![](https://mc.qcloudimg.com/static/img/ddd99874bc4e553bae7543db3377dc42/VPC-Overview.png)
    　　　　　    　　　　　  Figure 1:  Comparison of basic network and VPC
						
The functional differences between VPC and basic network are shown in the following table:

| Function | VPC | Basic Network |
|---------|---------|---------|
| Tenant associativity | Logically isolated network based on GRE encapsulation | Tenant associated |
| Network customization | Support | Not supported |
| Routing customization | Support | Not supported |
| IP customization | Support | Not supported |
| Connection rules | Support cross-region and cross-account connection | Same tenant and same region connection |
| Security control | [Security Group](https://intl.cloud.tencent.com/document/product/213/5221) and [Network ACL](https://cloud.tencent.com/doc/product/215/5132)| Security group |

## Quick Start
- When you get started with Tencent Cloud VPC, there are some commonly occurring basic concepts. Click here to view [Glossary](https://cloud.tencent.com/doc/product/215/4925).
- If it is the first time for you to use Tencent Cloud VPC, please complete the practice [VPC Quick Start](https://cloud.tencent.com/document/product/215/8119) to get the practice instructions of Tencent Cloud VPC. This practice will guide you through the steps of creating a VPC with subnet, and starting CVM instance to access the public network in your subnet.
- The following table lists the resources that will help you when you use the Tencent Cloud VPC service.

| Resource | Description | 
|---------|---------|
| [Main functions of VPC](https://cloud.tencent.com/doc/product/215/3075)  | Overview of the functions of VPC | 
| [VPC Usage Restrictions](https://cloud.tencent.com/doc/product/215/537)  | Service usage restrictions in VPC | 
| [Tencent Cloud VPC documentation](https://cloud.tencent.com/doc/api/245) | API documentation and developer guide | 
|  [Tencent Cloud VPC buying guide](https://cloud.tencent.com/doc/product/215/3079) | Charging standard, expiration notice and other information |
| [FAQs](https://cloud.tencent.com/doc/product/215/6512)   | FAQs on VPC | 


