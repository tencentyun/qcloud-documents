The CVM instance described below also refers to dedicated CVM.

Tencent Cloud provides the following network and security features:

- Security group
- Encryption login method
- EIP
- Internet access
- Private network access
- Basic network and VPC

You can use [Security Group](/doc/product/213/5221) to control access to your instance. These security groups resemble a network firewall, enabling you to specify the protocols, ports, and source/destination IP ranges that are allowed for access. You can create multiple security groups and assign different rules to each security group. You can then assign one or more security groups to each instance, and we will use these rules to determine which traffic is allowed to access instances and which resources the instance can access. You can configure a security group, so that only a specific IP or a specific security group can access the instance.

Tencent Cloud provides two encryption login methods: [Password Login](/doc/product/213/6093) and [SSH Key Pair Login](/doc/product/213/6092). Users are free to choose from the above two methods to securely connect with the CVM.

Instances may fail due to uncontrollable reasons. If an instance fails and you start another instance as alternative, the public IP of the alternate instance will be different from that of the original instance. However, if your application requires a static IP address, you can use an [EIP Address](/doc/product/213/5733).

Tencent Cloud's [Internet Linkage](/doc/product/213/5224) gives access to more than 20 domestic mainstream network ISPs to ensure that your customers can enjoy the same high-speed access, regardless of which ISP they use. [Private Network Linkage](/doc/product/213/5225) goes through an underlying 10 Gigabit/Gigabit network interconnection to ensure high-speed access, high reliability and low latency.

The user's [Network Environment](/doc/product/213/5227) can be divided into basic network and VPC. In the basic network, your cloud product instance is located in a large resource pool preset by Tencent Cloud. In VPC, your cloud product instance can be activated under your own preset, custom IP address range, and isolated from other users.

The above networks and security services ensure the security and efficiency of your instances, and make them capable of providing services internally and externally.


