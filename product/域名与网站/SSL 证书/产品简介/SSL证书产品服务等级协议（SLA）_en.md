### 1 Features of Service
Tencent Cloud provides SSL certificate services, including purchase and management of OV, EV and wildcard SSL certificates. For detailed service types, please see related service information published by Tencent Cloud.

### 2 Business Availability
A service availability of 99.99% is guaranteed for digital certificate CRL/OCSP of Tencent Cloud SSL Certificate Service.

For example, digital certificate CRL/OCSP service should be available for 30 x 24(h) x 60(min) x 99.99% = 43195.68 minutes, and be unavailable for 43200 - 43195.68 = 4.32 minutes in June.

> Availability = (1 - unavailability duration/total service time within the service period for digital certificate CRL/OCSP) x 100%.

Notes:
(1)	A calendar month is counted as a service period. Any duration less than a month will not be counted as a service period, in which case service availability will not be calculated.
(2)	Unavailability duration: If the digital certificate CRL/OCSP service is unavailable for successive 5 minutes or more, the duration will be counted as unavailability duration; if this persists for less than 5 minutes, the duration will not be counted as unavailability duration.
(3)	Definition of unavailability: The unavailability of service caused by issues of TrustAsia (certificate provider), or human error.
(4)	The following situations are not counted as unavailability duration:
A. Service interruption caused by system maintenance and upgrade of which TrustAsia has notified users in advance.
B. Unavailability of services caused by users' service calling not in accordance with the rules.
C. Unavailability due to API authorization data (AK/SK) loss or leak caused by users.
D. Unavailability caused by force majeure. For more information, refer to "Force majeure" section of the master contract.

### 3 Failure Recovery
By providing at least dual network redundancy and device redundancy, Tencent Cloud can offer fault-tolerant service for emergent network line failure to ensure the continuity of service. At the same time, Tencent Cloud provides a 24/7 on-call professional assistance team, as well as technical support via tickets, phone calls and other means, forming an emergency response mechanism which includes failure monitoring, automatic alarm, fast failure positioning and fast recovery.

### 4 Resource Allocation Capability
The bound domain name and certificate brand/model cannot be modified for issued SSL certificates. For expansion, users need to re-purchase and apply.

### 5 Destroyable Service and Data
When using SSL certificate service, users can delete and terminate uploaded and expired SSL certificates. Tencent Cloud does not save any deleted SSL certificates, so they cannot be restored after deletion.
Users can export their SSL certificates and perform data restoration and migration according to their needs.

### 6 Service Privacy
Users can manage certificates by projects according to actual needs, and control and isolate external access to protect the privacy of data.

### 7 The Right to Know the Service Status
(1)	Users can query for the locations of IDCs where their SSL certificate services reside by submitting tickets.
(2)	Tencent Cloud IDC will comply with applicable local laws and regulations, while customers have the right to know what is going on at all times and can make queries by submitting tickets.
(3)	Tencent will not keep, publish, delegate or disclose any SSL certificate data or information provided by users to third parties without written approval from the users, or use the data for any purposes other than following this agreement, unless requested by regulatory authorities for auditing purposes.
(4)	Customer behavior logs will not present any personal user information to others, unless such behavior log is used for the statistical analysis of the running status of Tencent Cloud SSL certificate service.

### 8 Service Auditability
In accordance with the applicable laws and regulations and on condition of compliance with relevant process and availability of all necessary documents, Tencent Cloud may provide information, including operation log of key components of SSL certificate service, operation records of OPS personnel and operation records of users, if required by regulatory authorities or if it is necessary to do so for other reasons such as collection of evidences during investigation into security incidents.

### 9 Service Billing Accuracy
The price of Tencent cloud SSL certificate service varies depending on different brands, models and number of supported domain names. For more information on billing standard, please see the billing modes and prices published on the official Tencent Cloud website.

### 10 Service Compensation
#### 10.1 Scope
If the CRL/OCSP service of SSL certificate purchased by users becomes unavailable due to Tencent Cloud device failure, design defects, product feature issues or improper operations, Tencent Cloud will compensate users for the unavailability duration. However, this does not apply to the unavailability duration caused by factors described in the "Force Majeure" section of the master contract.

#### 10.2 Compensation Standards
If information leakage caused by certificate hacking leads to user losses, Tencent Cloud and certificate providers will cooperate with users to apply for the guaranteed compensation with corresponding digital certificate authorities (CAs).

Compensation amount:

| Certificate Model | Compensation Amount |
|---|---|
| Symantec Extended Validation (EV) SSL Certificate Professional Edition | USD 1.75 million |
| Symantec Extended Validation (EV) SSL Certificate | USD 1.75 million |
| Symantec Organization Validation (OV) SSL Certificate Professional Edition | USD 1.75 million |
| Symantec Organization Validation (OV) SSL Certificate | USD 1.50 million |
| GeoTrust Extended Validation (EV) SSL Certificate | USD 1.50 million |
| GeoTrust Organization Validation (OV) SSL Certificate | USD 1.25 million |
| GeoTrust Domain Validation (DV) SSL Certificate | USD 500,000 |

