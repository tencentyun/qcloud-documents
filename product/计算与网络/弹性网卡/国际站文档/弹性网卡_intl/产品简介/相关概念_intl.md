The following information is associated with an ENI:

1. Primary ENI or secondary ENI: The ENI created with the creation of CVM within VPC is the primary ENI, and those created by users are secondary ENIs. The primary ENI does not support binding and unbinding, while secondary ENIs support.
2. Primary private IP: The primary private IP of an ENI is assigned by the system or specified by user when the ENI is created. The primary private IP of primary ENI can be modified, but that of secondary ENI cannot.
3. Secondary private IP: The secondary private IP bound to an ENI in addition to the primary IP. It is configured by user during the creation or editing of ENI, and supports binding and unbinding.
4. EIP: Bound with private IPs of an ENI in a one-to-one manner.
5. Security group: An ENI can be bound with one or more security groups.
6. MAC address: Each ENI has a unique global MAC address.