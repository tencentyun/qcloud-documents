Tencent Cloud provides the following network and security features:

- Security group
- Encryption login method
- Elastic IP
- Internet access
- Private network access
- Basic network and private network

You can use [Security Group](/doc/product/213/5221) to control access to your instance. These security groups resemble a network firewall, allowing you to specify the protocols, ports, and source/target IP ranges that are allowed access. You can create multiple security groups and assign different rules to each security group. You can then assign one or more security groups to each instance, and we will use these rules to determine what traffic is allowed to access instances and which resources the instance can access. You can configure a security group so that only a specific IP address or a specific security group can access the instance.

Tencent Cloud provides two encryption login methods: [Password Login](/doc/product/213/6093) and [SSH Key Pair Login](/doc/product/213/6092). Users are free to choose two ways to securely connect with the CVM.

Instances may fail because of uncontrollable reasons. If an instance fails and you start a replacement instance, the public IP of the alternate instance will be different from the original instance. However, if your application requires a static IP address, you can use an [Elastic IP Address](/doc/product/213/5733).

Tencent's [Internet Link](/doc/product/213/5224) gives access to more than 20 domestic mainstream network operators to ensure that your customers, regardless of ISP, can enjoy the same high-speed access; [Private Network Link](/doc/product/213/5225) goes through an underlying 10 Gigabit / Gigabit network interoperability to ensure high-speed access, high reliability and low latency.

The user's [Network Environment](/doc/product/213/5227) can be roughly divided into 'basic network' and 'private network'. Under a basic network, your cloud product instance is located in a large resource pool preset by Tencent Cloud; under a private network, your cloud product instance can be activated under your own preset, custom network segments, and isolated from other users.

The above network and security services protect your instances; making them safe, efficient and able to freely provide external services.

