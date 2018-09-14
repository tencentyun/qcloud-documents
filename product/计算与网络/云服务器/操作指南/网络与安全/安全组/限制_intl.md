- Security groups are region and project-specific. CVMs can only be bound with the security groups in the same region and project.
- Security groups apply to any CVM instances in [network environment](/doc/product/213/5227).
- Each user can set a maximum of 50 security groups for each project in each region.
- A maximum of 100 inbound/outbound access policies can be set for a security group.
- A CVM can be associated with multiple security groups, and a security group can be associated with multiple CVMs. No number limit is imposed.
- Security groups bound with CVMs in **basic network** **cannot filter** data packets sent from (or to) relational database (CDB) and cloud cache service (Redis and Memcached) of Tencent Cloud. If necessary, you can use iptables to filter traffic of such instances.

| Feature | Count |
|---------|---------|
| Security group | 50/Region |
| Access policy | 100 (Inbound/Outbound) |
| Number of security groups associated with an instance | No limit |
| Number of instances associated with a security group | No limit |

> **Note:**
> If you have a large number of instances that need to access each other, you can assign them to multiple security groups, and achieve mutual authorization and access by configuring the rules for security group IDs.


