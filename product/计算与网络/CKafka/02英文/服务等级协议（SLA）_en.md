## 1 Tencent Cloud CKafka Message Service

CKafka (Cloud Kafka) is a distributed, high-throughput, and highly scalable messaging system, which is compatible with the open-source Kafka API (version 0.9 and 0.10). Based on the publishing/subscription model, Ckafka decouples messages and enables producers and consumers to interact asynchronously without having to wait for each other. Ckafka has many advantages such as data compression and supporting offline and real-time data processing at the same time. It is suitable for log compression collection, monitoring data aggregation and other scenarios.

## 2. Service Guarantee Indicators

Tencent Cloud will stipulate the customized service level indicators for the cloud service you bought, and will commit itself to providing you with the maximum guarantee in terms of data management and business quality. Meanwhile, Tencent Cloud will reserve the right to make a proper adjustment in any indicators according to changes. Unless otherwise specified, the "month" referred to herein has a length of 30 calendar days, and shall be calculated on the basis of a calendar month.

## 2.1 CKafka Message Service

#### 2.1.1 Data Storage Persistence

The CKafka you apply for every month has a data storage persistence of '99.999999%'.

#### 2.1.2 Destroyable Data

When you request to delete any data or before you discard or resell any device, Tencent Cloud will perform a complete, permanent deletion on all your data through low-level disk formatting, and degauss the hard disks that are due for scrap.

#### 2.1.3 Right to Know

For now, users' CKafka service is deployed in six data centers, which are Shanghai Data Center, Guangzhou Data Center, Beijing Data Center, Chengdu Data Center, Shanghai Financial Data Center, and Shenzhen Financial Data Center.

Tencent Cloud helps users choose a data center with the best network condition to store their data. Users can select the region where they belong (Guangzhou, Shanghai, Beijing, Chengdu, Shanghai Finance, or Shenzhen Finance) when making a CVM purchase.

Those data centers available to users shall comply with local laws and regulations and applicable laws and regulations of the PRC.

Tencent Cloud will not disclose any of users' data to any third party, unless such disclosure is required by regulatory authorities for supervision and auditing purposes.

#### 2.1.4 Data Auditing

In accordance with the applicable laws and regulations and on condition of compliance with relevant process and availability of all necessary documents, Tencent Cloud may provide information regarding CVMs, including operation log of key components, operation records of OPS personnel and operation records of users, if required by regulatory authorities or if it is necessary to do so for other reasons such as collection of evidences during investigation into security incidents.

#### 2.1.5 Service Availability

A service availability of '99.95%' is guaranteed for the CKafka Message Service, which means that the CKafka Message Service should be available for users for at least '30 x 24 x 60 x 99.95% = 43178.4 minutes' each month, and be unavailable for users for '43200-43178.4=21.6 minutes' at most each month. Service unavailable time is calculated by the user's single instance.

If the service recovers from failure within `5 minutes`, it will not be counted into service downtime. Unavailability duration refers to the period from the moment the failure occurs to the recovery of service, including maintenance duration. If the service recovers from failure for over 5 minutes, it will be counted into the unavailability duration.

#### 2.1.6 Failure Recovery Capability

Tencent CKafka is designed with the failure recovery capability. When the physical server fails, the service will be automatically migrated to a new parent host without requiring any user intervention, so as to ensure continued service for customers. Meanwhile, Tencent Cloud's professional team provides maintenance support on a `24/7` basis.

## 3. Service Billing Accuracy

The billing details for Tencent Cloud services are displayed on the customer's purchase and order pages. You can choose the services you need from a variety of service categories and make a purchase at the listed prices. Please refer to the information published on Tencent Cloud website for the actual prices, and the fee will be charged based on the service specifications and the length of usage.

## 4. Compensation

### 4.1 Scope

Compensation is applicable to circumstances where a user claims for compensation for incidents/failures caused by Tencent Cloud, such as the user's inability to use services properly or access them and the inability to access any particular website (service site for developers).

### 4.2 Compensation Standards

Downtime duration = time when the failure is resolved - start time of failure. Downtime duration is calculated in minutes, and the duration less than 1 minute will be counted as `1 minute`.
For example, if the downtime duration is `1 minute and 1 second`, the duration will be counted as `2 minutes`.

Hundred-fold compensation for CKafka Message Service failures:

Postpaid: `a cash coupon in an amount equal to the daily fee of the failed instance ÷ 24 ÷ 60 × downtime duration (in minutes) × 100` will be offered. The upper limit of the cash coupon shall not exceed the total fee of the CKafka service.


