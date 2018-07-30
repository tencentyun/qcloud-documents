[ENI](https://cloud.tencent.com/product/eni) is an elastic network interface bound to CVMs in a VPC, which can be migrated freely among multiple CVMs. It is very useful for configuring management networks and establishing highly reliable network solutions.

Elastic NIC has VPC, availability zone and subnet attributes. You can only bind it to CVMs under the same availability zone. A CVM can be bound with multiple ENIs. The maximum number of ENIs allowed to be bound to a CVM depends on the CVM's specification.

## Concepts

 - **Primary ENI or secondary ENI:** The ENI created with the creation of CVM within VPC is the primary ENI, and those created by users are secondary ENIs. The primary ENI does not support binding and unbinding, while secondary ENIs support.
 - **Primary private IP:** The primary private IP of an ENI is assigned by the system or specified by users when the ENI is created. You can modify the primary private IP of the primary ENI, but not the ones of secondary ENIs.
 - **Secondary private IP:** The secondary private IPs bound to the ENI, other than the primary IP, are configured by users when they create or modify the ENI. You can bind/unbind these IPs.
 - **EIP:** Bound with private IPs of an ENI in a one-to-one manner.
 - **Security group:** An ENI can be bound with one or more security groups.
 - **MAC address:** An ENI has a globally unique MAC address.

## Application Scenarios
- **Isolation among private network, public network and management network**:
Isolation among private network, public network and management network for the purpose of secure data transmission is required for the network deployment of important businesses. Data security and network isolation are guaranteed by employing different routing policies and security group policies. Like a physical server, a CVM can be bound with ENIs residing in different subnets to achieve isolation among three networks.
- **Highly reliable application deployment:**
The high availability of key components in the system architecture is ensured through multi-server hot backup. Tencent Cloud provides ENIs and private IPs that can be flexibly bound and unbound. You can configure the disaster recovery of Keepalived to achieve highly available deployment of key components.

## Use Limits

The number of ENIs bound to a CVM is quite different from that of private IPs bound to an ENI depending on the CPU and memory configurations. These allowed numbers are shown in the following table:

| CVM Configuration | Max. Number of ENIs | Max. Number of IPs Bound to Each ENI |
| ------------------- | :---- | :------ |
| CPU: 1-core. Memory: 1 GB |  2     | 2       |
| CPU: 1-core. Memory: > 1 GB |  2     | 6       |
| CPU: 2-core |  2     | 10      |
| CPU: 4-core. Memory: < 16 GB |  4     | 10      |
| CPU: 4-core. Memory: > 16 GB |  4     | 20      |
| CPU: 8- to 12-core |  6     | 20      |
| CPU: > 12-core |  8     | 30      |


## API Overview
CVM-related APIs of ENI are shown below. For more information on how to work with ENIs, please see [Overview of ENI APIs](/doc/product/215/6513#api.E6.A6.82.E8.A7.8819).

| Feature |  Action ID | Description |
|---------|---------|---------|
| Create ENI |  [CreateNetworkInterface](/doc/api/245/4811) | Create an ENI |
| Apply for private IPs for ENI |  [AssignPrivateIpAddresses](/doc/api/245/4817) | Apply for private IPs for an ENI |
| Bind EIP to CVM |  [AttachNetworkInterface](/doc/api/245/4820) | Bind an EIP to a CVM |

