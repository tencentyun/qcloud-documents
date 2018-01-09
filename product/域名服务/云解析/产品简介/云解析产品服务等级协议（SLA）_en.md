
Cloud DNS Service Level Agreement

### 1 Features of Cloud DNS
Tencent Cloud DNS provides smart domain name resolution, precise scheduling and security protection features. It can also be associated with cloud resources such as Tencent Cloud Virtual Machines, providing one-stop cloud service for users. For detailed service types, please see related service information published by Tencent Cloud.

### 2 Business Availability
Cloud DNS provides four packages: individual professional, enterprise basic, enterprise standard and enterprise ultimate. We guarantee no less than 99% service availability for individual professional edition, enterprise basic and standard editions, and no less than 100% for enterprise ultimate edition.

>For example, the available time for service provided by enterprise basic edition in June should be 30 (days) X 24 (hours) X 60 (minutes) X 99.9% = 43,156.8 minutes, which means there are 43,200 – 43,156.8 = 43.2 minutes when the service is unavailable.
Availability = (1 – unavailability duration within the service period for DNS/total service time within the service period for DNS) X 100%.

Notes:
(1)	A calendar month is counted as a service period. Any duration less than a month will not be counted as a service period, in which case service availability will not be calculated.
(2)	Unavailability duration: A time period equal to or longer than a certain threshold during which the cloud resolution service is unavailable, is counted as unavailability duration (this threshold is different for different packages). Any duration shorter than the threshold will not be calculated as unavailability duration.
Individual professional edition: No less than 10 minutes are counted as unavailability duration;
Enterprise basic/standard/ultimate edition: No less than 5 minutes are counted as unavailability duration.
(3)	Unavailability definition: The interruption of resolution service caused by DNS server device problems, data center breakdowns, product feature issues or improper operations.
(4)	The following situations are not counted as unavailability duration:
- A.	Service interruption due to daily system maintenance or failure of recursive server on which DNS depends;
- B.	Interruption of service caused by users, third parties or force majeure;
- C.	Service interruption when domain name is blocked due to user's unauthorized operations or other reasons;
- D.	Resolution service interruption when user website receives DNS attacks beyond the protection capacity promised by the service package;
- E.	Interruption of service when user switches DNS server;
- F.	Interruption of service after user modifies resolution and waits for new resolution to take effect (longest waiting time worldwide is 72 hours);
- G.	Interruption of service caused by network failures, device failures or configuration adjustments on non-Tencent Cloud devices.

### 3 Failure Recovery
By providing at least dual network redundancy and device redundancy, Tencent Cloud can offer fault-tolerant service for emergent network line failure to ensure the continuity of service. At the same time, Tencent Cloud provides a 24/7 on-call professional assistance team, as well as technical support via tickets, phone calls and other means, forming an emergency response mechanism which includes failure monitoring, automatic alarm, fast failure positioning and recovery.

### 4 Resource Allocation Capability
Cloud DNS sets the capacity limit for packages. Users are free to extend their service within the limit according to their actual business demands, or upgrade their packages if their demands exceed the current limit.
Note that users can only upgrade packages by themselves. Contact us via ticket if you need package degrade and refund.

### 5 Destroyable Service and Data
When using Cloud DNS, users can create or delete and terminate domain names and resolution records. Tencent Cloud will not save any terminated domain name or resolution record, and they're not recoverable after termination.
Users can choose to export their resolution records and perform data restoration and migration according to their needs.

### 6 Service Privacy
Due to the particularity of DNS, the resolution records of authorized DNS servers are public to the whole Internet. However, users may restrict or prevent the access from non-project members by configuring access authentication policies to ensure data operation privacy.

### 7 The Right to Know the Service Status
(1)	Users can query for the locations of IDCs where their Cloud DNS service reside by submitting tickets.
(2)	Tencent Cloud IDCs comply with applicable local laws and regulations, while customers have the right to know what is going on at all times and can make queries by submitting tickets.
(3)	Tencent will not keep, publish, delegate or disclose any domain name resolution data or information provided by users to third parties without written approval from the users, or use the data for any purposes other than following this agreement, unless requested by regulatory authorities for auditing purposes.
(4)	Customer behavior logs will not present any personal user information to others, unless such behavior log is used for the statistical analysis of the running status of Tencent Cloud DNS service.

### 8 Service Auditability
In accordance with the applicable laws and regulations and on condition of compliance with relevant process and availability of all necessary documents, Tencent Cloud may provide information, including operation log of key components of speech recognition service, operation records of OPS personnel and operation records of users, if required by regulatory authorities or if it is necessary to do so for other reasons such as collection of evidences during investigation into security incidents.

### 9 Service Billing Accuracy
The cost for using Tencent Cloud DNS service is calculated according to purchased package and service years. Each package is bound to a single domain name upon purchase. For more information of billing standard, please see the billing modes and prices published on Tencent Cloud official website.

### 10 Service Compensation

#### 10.1 Scope
If Tencent Cloud DNS service purchased by users becomes unavailable due to Tencent Cloud device failure, design defects, product feature issues or improper operations, Tencent Cloud will compensate users for the unavailability duration. However, this does not apply to the unavailability duration caused by factors unrelated to Tencent Cloud as described in Section "Business Availability" in this Agreement, or factors described in Section "Force Majeure" of master contract.

#### 10.2 Compensation Standards
For each domain name that falls below the promised business availability, Tencent Cloud will compensate the user with extra service time equal to 10 times of service period.
> Compensated service period = downtime (minutes) x 10

Notes:
(1)	Downtime duration = time when service is recovered – start time of failure. Downtime duration is calculated in minutes, and duration less than 1 minute will be counted as 1 minute. For example, a downtime duration of 1 minute and 1 second is counted as 2 minutes.
(2)	Compensation is only applied for users who purchased Cloud DNS package which already generated service fee.

