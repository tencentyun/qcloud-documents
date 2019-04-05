## Persistency of Stored Data

The persistency of Cloud Object Storage refers to the rate of stored object data that is intact within the contract period, which is: Number of intact objects of the month/(Number of intact objects of the month + Number of lost objects of the month). Statistical period is one calendar month (counted as one month if less).

The persistency of Cloud Object Storage is 99.999999999%. This means if a users stores 100,000,000 data objects every month, there will be only one object that is possible to be lost each month.

## Destroyable Data

Destroyable data means that when a user asks to delete object data, the data will be deleted from RAM and disk, then the original space will be overwritten by new object data in order to completely delete the original data with no chance of recovery.

When a storage server goes offline and is discarded, the data will be erased by demagnetizing the disk.

## Migratable Data

Objects stored using Cloud Object Storage can be downloaded directly via HTTP. Users can easily transfer objects stored in Tencent Cloud Object Storage onto local servers or other clouds through standard HTTP method. They can also batch import/export objects by using tools provided by Tencent Cloud. Data migration is available for all types of files.

## Data Privacy

The privacy of data stored in Cloud Object Storage is ensured by unified authentication service provided by Tencent Cloud Security platform.

Cloud Object Storage organize object data using bucket method. Any request that is used to create or operate objects in a bucket will need to use the key of the bucket user to calculate a signature, which is used to verify whether the request is legitimate. This ensures that object data of a user is not visible to other users with data in the same resource pool.

Users can control the read privilege for their object data in the bucket by configuring it as public or private according to their demands. No signature is required for accessing objects in a public bucket. Signature authentication is required for accessing objects in a private bucket.

## The Right to Know

- Currently, user cloud object storages are deployed among three major data centers: the Shanghai Data Center, the Shenzhen Data Center and the Tianjin Data Center. You may query this by submitting a ticket.
- The number of data backups and in which data center the backup data is stored. You may query this by submitting a ticket.
- We will help users select the data center that is most suitable to their network environment to store data. Cold backup is dynamically allocated according to resource usage. By default, users do not need to choose data center and cold backup center location. You can submit a ticket if you wish to choose for yourself.
- Data centers are required to comply with local laws/regulations and relevant laws of PRC. You may query this by submitting a ticket.
- Any data stored by customers will not be provided to any third party, except when required by regulatory authorities for supervision and auditing purposes.
- Cloud Object Storage will not analyze data stored by customers.

## Audit of Data

In accordance with the applicable laws and regulations and on condition of compliance with relevant process and availability of all necessary documents, Tencent Cloud may disclose information regarding Cloud Database, including operation log of key components, operation records of operation & maintenance personnel and operation records of users, if required by regulatory authorities or if it is necessary to do so for other reasons such as collection of evidences during investigation into security accidents.

## Overview of Services

Cloud Object Storage features provided by Tencent Cloud include creating, deleting, controlling access privileges, customizing access domains, viewing monitoring information and operation data of buckets; creating, deleting, updating and viewing attributes, file lists of directories as well as searching by prefixes; uploading (normal upload or multipart upload), deleting, updating and viewing attributes of objects as well as downloading them. Plus other relevant features. All features are provided with detailed introduction and instruction documents. Meanwhile, Tencent Cloud provides corresponding APIs and SDKs.

## Service Availability

We guarantee that Cloud Object Storage has a 99.95% service availability, which means the monthly service available time should be 30(d)*24(h)*60(min)*99.95%=43,178.4 minutes, in other words, there will be 43200 - 43178.4 = 21.6 minutes in each month when the service will be unavailable. The statistics of service unavailability is calculated based on user's single service instance, or bucket, in this case.

It will not be accounted as service unavailable time if the service recovers from failure within 5 minutes. Unavailable time refers to the period from the start of failure to the recovery from failure, including maintenance time.

## Resource Allocation Capability

Cloud Object Storage is able to automatically expand or reduce resource in a dynamic manner by monitoring user's storage and request amount, without the user's awareness. Resource expansion is directed at storage capacity. Each expansion action can be completed within an hour and has a minimum expansion volume of 400T (no upper limit).

## Failure Recovery Capability

Tencent Cloud Object Storage utilizes dual redundant data storage method, which means the same data is stored into three copies. Customer service consistency can be maintained even if up to two copies of data are corrupted. Meanwhile, Tencent Cloud's professional team provides maintenance assistance on a 24/7 basis to help you repair failed storage servers in time.


