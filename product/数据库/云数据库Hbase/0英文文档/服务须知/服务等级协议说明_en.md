# Tencent Cloud Database HBase Service Level Agreement
Welcome to use Tencent cloud database HBase service!


#### 1. Definition of Service
Tencent Cloud Database Hbase is a high-performance distributed data storage service created by Tencent Cloud based on Hbase, the world's most promising open source NoSQL database. It is fully compatible with Hbase protocols, and applicable to non-relational database-oriented scenarios.
At the same time Tencent cloud database Hbase provides Hbase cluster services of high performance, high reliability, ease of use. Each instance is built with at least two data backup masters to ensure high availability of user's data and high stability of system.

#### 2. Data Persistence
During the period of service (service period of the Hbase that is purchased by user), we guarantee a 99.9996% persistency for the data stored in the instances applied by users. That is to say, if a user stored 1,000,000 files in the instances, there are only 4 files among them that are possible to be lost every month.

#### 3. Destroyable Data
The data will need to be destroyed when a user actively deletes data or the service expires. After data is deleted or before devices are discarded/resold, Tencent Cloud will completely erase all of the user data by performing a low-level formatting on the disk. The erased data cannot be recovered and the disk will be demagnetized upon expiry or being scrapped.

#### 4. Right to Know
A. The location of data centers where the data is stored. You can make an inquiry about this by submitting a ticket.
B. The number of data backups and the location of data centers where the backup data is stored. You can make an inquiry about this by submitting a ticket.
C. Tencent Cloud will help users select the data center that is most suitable for their network environment to store data. Cold backup will be dynamically allocated according to resource usage. By default, users do not need to choose data center and cold backup center location. If a user needs to do so, he or she can make an inquiry about this by submitting a ticket.
D. Data centers shall comply with local laws and regulations and applicable laws and regulations of the PRC. (Users can make an inquiry about this by submitting a ticket)
E. Any of users' data will not be disclosed to any third party, unless such disclosure is required by regulatory authorities for supervision and auditing purposes. User's behavior logs are used for data analysis for keeping track of database status, and any of users' personal information will not be disclosed to any third party.

#### 5. Data Privacy
Tencent Cloud achieves network isolation by configuring firewall policy and using white list filtering mechanism, and ensures the invisibility of each user's data within the same resource pool with each Hbase cluster independently accessing its own HDFS storage.

#### 6. Data Auditing
In accordance with the applicable laws and regulations and on condition of compliance with relevant process and availability of all necessary documents, Tencent Cloud may provide information regarding databases, including operation log of key components, operation records of operation & maintenance personnel and operation records of users, if required by regulatory authorities or if it is necessary to do so for other reasons such as collection of evidences during investigation into security incidents

#### 7. Service Availability
A. Tencent Cloud Database Hbase guarantees a data availability of 99.95%. That is, the available time/service period of a single database instance during each service period is not less than 99.95%. The statistics of service unavailability is calculated based on a single user database instance.
B. If the service recovers from failure within 5 minutes, it will not be accounted into service downtime. Unavailability duration refers to the period from the moment the failure occurs to the recovery of service, including maintenance duration.

#### 8. Failure Recovery Capability
Tencent Cloud's professional team provides maintenance support on a 24/7 basis.
