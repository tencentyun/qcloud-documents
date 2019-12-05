## FAQ on Cluster Creation
### 1. Can I set a CVM without a public IP when I create clusters?

Yes. A CVM without public IP can only pull images from My Images under the image warehouse. It cannot pull dockerhub images or third-party images.
A CVM without public IP but with Internet bandwidth may access the Internet by binding an EIP.

### 2. Why do I need to choose a network when I create clusters?
The selected network and subnet is the subnet to which the CVM in the cluster belongs. Users may achieve cross-zone disaster recovery by adding different CVMs to subnets under different availability zones.

### 3. What are the supported model types for creating clusters?
All models with postpaid system disks worked as cloud storage are supported.

### 4. What operating systems are supported for the current CCS hosts?
Currently, Ubuntu 16.04 is supported. CentOS 7 will become supported soon. Submit a ticket or contact us through QQ group if you wish to use other operating systems.

### 5. What are the lower storage limit and upper storage limit for system disk?
The system disk is 20 GB by default (free). Lower and upper limits are 20 GB and 50 GB respectively. Submit a ticket to rwwish to use a larger system disk. It is recommended that you use a system disk configuration larger than 50 GB.

## FAQ on Adding Nodes
### 1. What are the restrictions when expanding CVMs?
You can only choose a region in which your current cluster resides, but you may choose a different availability zone. Clusters can be deployed across different availability zones.

### 2. Is there a limit for the number of CVMs?
Yes. A user cannot own more postpaid CVMs than his or her user quota. For for information, please see [Cloud Service Overview](https://console.cloud.tencent.com/cvm/overview).

## FAQ on CVM Termination
### 1. When I terminate a CVM, what happens to the containers that are deployed under this CVM by my service?
When a CVM is terminated, resources under the CVM such as containers are also terminated. If the number of containers for a certain service becomes smaller than the expected number of running containers, the cluster will launch more containers on other CVMs until the desired number is met.

