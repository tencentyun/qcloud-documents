- Security groups are based on regions and projects. CVMs can only be bound with security groups in the same region and project.
- Security groups apply to any CVM instances in [network environment](/doc/product/213/5227).
- Each user can set up to 50 security groups for each project in each region.
- Up to 100 inbound/outbound access policies can be set for a security group.
- A CVM can be associated with multiple security groups, and a security group can be associated with multiple CVMs. No limit is imposes on the number.
- Security groups associated with CVMs on **basic network** are unable to filter packets of Tencent Cloud relational databases (CDBs) and elastic cache (Redis and Memcached). If necessary, you can use iptables to filter traffic for such instances.

| Feature | Limits |
|---------|---------|
| Security group | 50/Region |
| Access policy | 100 (Inbound/Outbound) |
| Security groups bound with a CVM | No limit |
| CVMs bound with a security group | No limit |

> **Note:**
> If you have a large number of instances that need to access each other, you can assign them to multiple security groups, and achieve mutual authorization and access by configuring security group ID rules.

