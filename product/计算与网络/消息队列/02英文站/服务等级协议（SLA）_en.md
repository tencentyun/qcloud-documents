## 1. Tencent Cloud Services

Tencent Cloud Services are a set of cloud system services, comprising Cloud Virtual Machine (CVM), Cloud Bandwidth, Cloud Storage, Cloud Database, Cloud Security, Cloud Monitoring, Cloud Automated Testing and more, delivered by Tencent Cloud to meet different needs from various websites and applications. With regard to specific service categories, the relevant service information publicly released by Tencent Cloud shall prevail.

## 2. Service Guarantee Indicators

Tencent Cloud stipulates the customized service level indicators for the cloud service you bought, and commits itself to providing you with the maximum guarantee in terms of data management and business quality. Meanwhile, Tencent Cloud reserves the right to make a proper adjustment in any indicators according to changes. Unless otherwise specified, the "month" referred to herein has a length of 30 calendar days, and shall be calculated on the basis of a calendar month.

### 2.1 CMQ Queue Services

#### 2.1.1 Data storage persistence

The CMQ Queue you apply for every month has the persistence of `99.999999%`.

#### 2.1.2 Data disposability

When you request to delete any data or before you discard or resell any device, Tencent Cloud will perform a complete, permanent deletion on all your data through low-level disk formatting, and degauss the hard disks that are due for scrap.

#### 2.1.3 Data privacy

CMQ can be integrated with the KMS encryption service. When a message is produced, the body of this message will be encrypted to prevent any plaintext from uploading.

#### 2.1.4 Right to know data

For now, users' CMQ service is deployed in six data centers, which are located in Shanghai, Guangzhou, Beijing, Hong Kong, Singapore and North America.

Tencent Cloud helps users choose a data center with the best network condition to store their data. Users can select the region where they belong (Guangzhou, Shanghai, Beijing, Hong Kong, Singapore or North America) when making a CVM purchase.

Those data centers available to users shall comply with local laws and regulations and applicable laws and regulations of the PRC.

Any of users' data will not be disclosed to any third party, unless such disclosure is required by regulatory authorities for supervision and auditing purposes. Any of users' data will not be saved in any overseas data center or will not be used for any overseas business or data analysis.

To keep user data secure, Tencent Cloud adopts a three-copy mechanism for data storage, and carries out cold data backup on a regular basis.

#### 2.1.5 Data examinability

To the extent permitted by current laws and regulations, Tencent Cloud may disclose CVM-related information, including operating logs of key components, operation records of OPS personnel and operation records of users, as long as applicable procedures are followed and appropriate formalities have been completed to satisfy the requirement of cooperating with regulators to supervise or investigate security issues.

#### 2.1.6 Service availability

A service availability of `99.95%` is guaranteed for the CMQ Queue Service, which means that the CMQ Queue Service should be available for users for at least `30 x 24 x 60 x 99.95% = 43178.4 minutes` each month, and be unavailable for users for `43200-43178.4=21.6 minutes` at most each month. Service unavailable time is calculated by the user's single instance.

If the service recovers from failure within `5 minutes`, it will not be counted into service downtime. Unavailability duration refers to the period from the moment the failure occurs to the recovery of service, including maintenance duration. If the service recovers from failure for over 5 minutes, it will be counted into the unavailability duration.

#### 2.1.7 Failure recovery capability

Tencent Cloud CMQ Queue is designed with the failure recovery capability. When the physical server fails, the service will be automatically migrated to a new parent host without requiring any user intervention, so as to ensure continued service for customers. Meanwhile, Tencent Cloud's professional team provides maintenance support on a `24/7` basis.

## 3. Service Billing Accuracy

The billing details for Tencent Cloud services are displayed on the customer's purchase and order pages. You can choose the services you need from a variety of service categories and make a purchase at the listed prices. Please refer to the information published on Tencent Cloud website for the actual prices, and the fee will be charged based on the service specifications and the length of usage.

## 4. Compensation

### 4.1 Scope

Compensation is applicable to circumstances where a user claims for compensation for incidents/failures caused by Tencent Cloud, such as the user's inability to use CVMs properly and the inability to access any particular website (service site for developers).

### 4.2 Compensation Standards

Downtime duration = time when the failure is resolved - start time of failure. Downtime duration is calculated in minutes, and the duration less than 1 minute will be counted as `1 minute`.
For example, if the downtime duration is `1 minute and 1 second`, the duration will be counted as `2 minutes`.

Hundred-fold compensation for CMQ message queue failures:

Postpaid: `a cash coupon in an amount equal to the daily fee of the failed Queue ÷ 24 ÷ 60 × downtime duration × 100` will be offered. The upper limit of the cash coupon shall be no more than the total fee of the CMQ service.


