
# CDB for MySQL Service Level Agreement

1. Persistency of Data Storage

During the term of this Agreement, the persistency of data storage for the instances applied for by a user every month shall be 99.9996%. This means every month there are only 4 instances that have the possibility of data loss out of 1,000,000 instances of a user. 

2. Destroyable Data

When a user requests for deletion of data or before a device is discarded/resold, Tencent Cloud will completely delete all of the data of the user by performing a low-level formatting on the disk. The deleted data cannot be recovered and the disk will be demagnetized upon expiry or being scrapped.

3. Data Migration

Tencent Cloud will provide data service in a standard MySQL database format, and allow users to save the files as standard sql files using the import/export tools provided by Tencent Cloud so as to migrant these files into cloud database or to user's virtual host or a local server.

4. Data Privacy

Tencent Cloud achieves network isolation by configuring firewall policy and using white list filtering mechanism, and ensure that the data of a user is not visible to any other user within the same resource pool by means of username and password of database instance and permission control mechanism for disabling database instance.

5. The Right to Know

(1) The location of data center where the data is stored. You can make an inquiry about this by submitting a ticket.
(2) The number of data backups and the location of data center where the backup data is stored. You can make an inquiry about this by submitting a ticket.
(3) Tencent Cloud will help users select the data center that is most suitable for their network environment to store data. Cold backup will be dynamically allocated according to the resource usage. By default, users does not need to choose data center and cold backup center location. If a user needs to do so, he or she can make an inquiry about this by submitting a ticket.
(4) Local laws and regulations and applicable laws and regulations of PRC with which the data centers shall comply. (Users can make an inquiry about this by submitting a ticket).
(5) Any of users' data will not be disclosed to any third party, unless such disclosure is required by regulatory authorities for supervision and auditing purposes. User's behavior log is used for data analysis for keeping track of database status, and will not be used to disclose any of users' personal information to any third party.

6. Audit of Data

In accordance with the applicable laws and regulations and on condition of compliance with relevant process and availability of all necessary documents, Tencent Cloud may disclose information regarding Cloud Database, including operation log of key components, operation records of operation & maintenance personnel and operation records of users, if required by regulatory authorities or if it is necessary to do so for other reasons such as collection of evidences during investigation into security accidents.

7. Features of Service

The features of cloud database instances provided by Tencent Cloud include: CDB instance application; login; addition, deletion, modification and query of database; cold backup extraction; data rollback; data import; multi-thread data import/export tool; O&M data query API; password reset. All features come with detailed descriptions and documentation. Users will be notified of any change of each feature that can affect user's data result via internal message.

8. Service Availability

(1) We guarantee a service availability of 99.95% for cloud database, which means the service availability duration in each month shall be 30(d)*24(h)*60(min)*99.95%=43,178.4 minutes, and the unavailability duration is 43200-43178.4=21.6 minutes. The statistics of service unavailability is calculated based on user's single service instance.
(2) If the service recovery from failure takes less than 5 minutes, it will not be counted in the calculation of service unavailability. Unavailability duration refers to the period from the moment the failure occurs to the recovery of service, including the maintenance duration.

9. Resource Allocation Capability

Tencent Cloud guarantees that when a user applies for the expansion of capacity for computing resources by less than 50% of existing resources and the number of requested instance resources is less than 10, the expansion will be completed within 1 hour; in case of less than 30 instance resources requested, the expansion will be completed within 24 hours; and in case of more than 30 instance resources requested, please submit a ticket to make an inquiry about the completion time. A maximum of 100% of existing capacity and a minimum of 25GB can be added for an expansion for a single user at a time.

10. Fault Recovery Ability

Tencent Cloud's professional team provides maintenance support on a 24/7 basis
