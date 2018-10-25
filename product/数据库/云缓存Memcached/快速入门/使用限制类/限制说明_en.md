## 1. Data Removal

As a storage product, Cloud Memcached does not support data removal, that is, it does not delete old data automatically when storage becomes full. Users must configure expiration time on their own and enable expired data deletion feature in their Cloud Memcached.

## 2 Length Limit for key and value

Considering the latency for copying data, Cloud Memcached implemented the following length limit for key and value: key must be no longer than 10 KB, value must be no longer than 1 MB (1 MB is the limit of Memcached open source protocol). It is recommended to compress value when necessary.

## 3 Performance Limit

Cloud Memcached supports a maximum access volume of 10,000 visits/second/GB. The service may slow down if the limit is exceeded. The capacity mentioned here (GB) refers to actual allocated capacity, but not the maximum capacity.

For example, if the actual allocated capacity is 50 GB, then the 50 GB of data supports 50*10,000=500,000 visits per second.

The system will discard excessive requests if access goes beyond 10,000 visits/second/GB.

The currently provided access volume of 10,000 visits/second/GB is able to satisfy the access demand for most applications. Submit a ticket to apply for interface/port expansion if your access volume is over 10,000 visits/second/GB.

## 4 Access Restriction Regarding Clients and Number of Connections

(1) Cloud Memcached is a distributed system and does not support asynchronous client such as Spymemcached.
That is to day, if three requests A, B and C are sent in sequence through the same connection, the order of the replies is not fixed, which means logics based on sequence cannot be used. You must use open-source synchronous client where one reply follows the corresponding request.

(2) Socket connections have timeout limit for Cloud Memcached. If the client does not have any access requests for 180 seconds since the last access, the connection is automatically terminated. Therefore, the client should send at least one access request every 180 seconds.

(3) There is a limit for how many socket connections can be up towards a single Cloud Memcached. However, this limit is far beyond the number of temporary ports that can be created by the client, so you do not need to consider this problem.

## 5 Protocol Restriction

1. Cloud Memcached supports memcached protocols (see [Cloud Memcached Compatible Protocol Instruction](/doc/product/241/兼容的协议说明)), which means text and binary protocols are supported. 

2. In theory, binary decoding is faster then text, but the actual advantage is negligible. Plus, most users still use text protocol, which is relatively easy and stable. Few users use binary protocol.

3. Standard Memcached protocols come with certain defects, users should pay particular attention to them. See [Standard Memcached Protocol Defect Solution](/doc/product/241/标准协议缺陷解决方案说明).

## 6. Security and Disaster Recovery Restriction

Cloud Memcached provides master/slave hot backup feature which backs up data by using periodic images and real-time log synchronization. In extreme conditions, data that is not stored into disk briefly may be lost when Cloud Memcached encounters power failure. However this is extremely rare.


## 7 Capacity Expansion Restriction
To prevent balance lost caused by rapid instance capacity expansion due to business exceptions, we will detect instances that expand too fast through routing inspections (instances over 20 GB are taken into routing inspections) and attempt to contact you to make sure if the business is normal. We will suspend the instance (read-only) if we cannot reach you, or determine that the business is exceptional. Submit a ticket to contact us if you require a capacity over 20 GB.

