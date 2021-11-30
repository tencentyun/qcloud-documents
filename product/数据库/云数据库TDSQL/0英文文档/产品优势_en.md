## 1. Strong Consistency of Data
CDB for MariaDB (TDSQL) supports the configuration of strongsync replication. Different from the async replication of MySQL, in the master/slave architecture, strongsync ensures strong consistency of data between the master and the slave to avoid data loss during master/slave switchover of your database. You can also disable strongsync by modifying the configuration to improve performance.

## 2. Higher Security
CDB for MariaDB (TDSQL) can provide comprehensive security for your database:

- Anti-DDos attacks: When you connect and access a CDB for MariaDB (TDSQL) instance via the Internet, the instances may suffer DDoS attacks. When considering your instance is under DDoS attacks, the security system of CDB for MariaDB (TDSQL) automatically starts traffic cleaning.
- System security: Even in the private network, CDB for MariaDB (TDSQL) is also protected by multi-layer firewalls, effectively combating various attacks and ensuring data security. In addition, physical servers cannot directly log in to CDB for MariaDB (TDSQL), and only ports needed for specific database services are opened, effectively isolating risky operations.
- VPC network isolation: CDB for MariaDB (TDSQL) supports VPC network to securely isolate the access of other devices within the private network.
- Private network risk control: Tencent Cloud's database team cannot directly access a physical machine or database instance of CDB for MariaDB (TDSQL), except through Tencent Cloud OPS management platform. Even troubleshooting must be made on a security device and is strictly managed by the internal risk control system.
- Permission management of object granularity: You can define table-level permission and configure IP addresses for CDB for MariaDB (TDSQL) access, and any unspecified IP address is not allowed to access.
- Database audit: CDB for MariaDB (TDSQL) supports database audit configuration to record operations of administrators or users for post-risk control and management.
- Database firewall (available soon): CDB for MariaDB (TDSQL) supports malicious behavior customization, and blocks malicious behavior and session.
- Operation log: The system records all your operations to CDB for MariaDB (TDSQL) made by accessing Tencent Cloud Web Console. It is commonly used for tracing back.


## 3. More Powerful Features
- Support multi-source replication, powerfully supporting complex enterprise-level businesses, such as frontend > middle end> backend > data warehouse in insurance service.
- Support more advanced storage engines such as XtraDB and TokuDB, and introduce technologies including group commit for the binary log, effectively improving business performance and reducing storage usage.
- Support thread pool, audit log and other abilities that MySQL Enterprise Edition has.
- Its clock is accurate to the microsecond so that CDB for MariaDB (TDSQL) can be used for financial transactions with high requirements for time accuracy.
- Provide virtual columns (function indexes), which can effectively provide performance of database analysis, statistics and computation.

## 4. Higher Availability
CDB for MariaDB (TDSQL) is designed to provide over 99.99% of availability. It provides an master/slave architecture for hot backup or one master and two slaves architecture for transparent failover. Besides, It features faulty node automatic repair, automatic backup, rollback and so on for more stable and secure business operation.

## 5. Higher Performance
Based on PCI-E SSD, CDB for MariaDB (TDSQL) features powerful IO performance to ensure database access capabilities. In addition, it uses NVMe protocol, specifically designed for PCI-E SSD, as storage firmware to further exert performance advantages. For example, a single high IO instance can support up to 6 TB capacity, 480 GB memory and over 220K QPS (queries per second). Such performance advantages allow you to support higher business concurrences with less database instances.

All CDB for MariaDB (TDSQL) instances use non-original MariaDB kernels that are modified based on actual needs by Tencent's top database R&D teams. Besides, the default parameters have been optimized based on years of production practice and are continually optimized by professional DBAs to ensure that CDB for MariaDB (TDSQL) is always running based on best practices.

## 6. Compatible with MySQL
CDB for MariaDB (TDSQL) uses the InnoDB storage engine and is compatible with MySQL 5.5 and 5.6. This means that, with little or no changes, you can use codes, applications, drivers and tools used for MySQL databases with CDB for MariaDB (TDSQL).



## 7. Easy to Use

Support instant-on and instant-off: You can custom the specifications of CDB for MariaDB (TDSQL) on Tencent Cloud official website. A CDB for MariaDB (TDSQL) will be generated automatically after you place an order. Using CDB for MariaDB (TDSQL) with CVM can reduce response time of applications and save Internet traffic fees.

On-demand upgrades: At the initial stage of your business, you can purchase a small CDB for MariaDB (TDSQL) instance to handle business stress. As the database stress and data storage change, you can flexibly adjust the instance specifications.


Easy management: Tencent Cloud is responsible for daily maintenance and management of CDB for MariaDB (TDSQL), including but not limited to handling hardware and software failure and updating database patches, to ensure its normal running. You can also add, delete, restart, backup and recover databases via Tencent Cloud Console.
