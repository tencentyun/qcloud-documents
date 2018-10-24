#### Tencent Cloud Redis Store (CRS) Service Level Agreement

**1. Persistency of Data Storage**
(1) Persistency of data storage refers to the probability that the stored data remains intact within the term of agreement. It is calculated as: number of key-values kept intact for the month/(number of key-values kept intact for the month + number of lost key-values for the month). The statistical period is 1 calendar month (less than one month should be counted as one month).
(2) Persistence of CRS should be 99.99%. This means that each month only 1 key out of the 10,000 keys stored by a user has the probability of loss.

**2. Destroyable Data**
(1) Destroyable data means that when a user requests to delete CRS table data, the data will be deleted from RAM and disk, then the used space of disk will be overwritten to completely delete the data with no possibility of recovery.
(2) When a storage server out of service is scraped, the disk will be demagnetized for destroying the data.

**3. Data Migration**
CRS allows the import and export of table data. The imported and exported data files are organized in the format of CRS backup files. The file organization format can be provided for the user.

**4. Data Privacy**
Through the firewall mechanism at authentication center, CRS can only be accessed by the servers with the same cloud account, thus preventing the illegal access by other accounts. Unless authorized by user, Tencent Cloud cannot view the stored data and operation log of user.

**5. Right to Know**
Users have the right to be informed of the following information about the data stored on the CRS:
(1) The location of the data center where the data is stored (users can make an inquiry about this through the enterprise QQ).
(2) The number of data backups and the location of data center where the backup data is stored (users can make an inquiry about this through the enterprise QQ).
(3) Users have the right to choose the data center location for their own data, but no right to choose the one for the backup data;
(4) Laws and regulations applicable to the location where the data is stored and data center (users can make an inquiry about this through the enterprise QQ);
(5) Any of users' data will not be disclosed to any third party, unless such disclosure is required by regulatory authorities for supervision and auditing purposes.
(6) CRS will not analyze any of the stored data of users.

**6. Data Auditing**
In accordance with the applicable laws and regulations and on condition of compliance with relevant process and availability of all necessary documents, Tencent Cloud may disclose information regarding Cloud Redis Store (CRS), including operation log of key components, operation records of operation & maintenance personnel and operation records of users, if required by regulatory authorities or if it is necessary to do so for other reasons such as collection of evidences during investigation into security accidents.

**7. Features of Service**
CRS provides purchase, data addition, deletion, modification and query, data import&export, expansion, automatic clean-up, monitoring information viewing and other features. All features come with detailed descriptions and documentation. Users will be notified of any change of each feature that can affect user's data result via enterprise QQ, telephone or email.

**8. Service Availability**
8.1 Tencent Cloud Redis Store guarantees a data availability of 99.95%. That is, the available time/available service period of a single database instance during each service period is not less than 99.95%. The statistics of service unavailability is calculated based on a single user database instance.
8.2 If the service recovers from failure within 5 minutes, it will not be counted into service downtime. Unavailability duration refers to the period from the moment the failure occurs to the recovery of service, including maintenance duration.

**9 Failure Recovery Capability**
Tencent Cloud's professional team provides maintenance support on a 24/7 basis.
