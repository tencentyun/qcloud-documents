## 1 What is Cloud Memcached?

(1) Tencent Cloud Memcached is a distributed memory-level Key-Value storage service developed by Tencent, which has extremely high performance and persistency.
(2) It is designed to act as the final data storage and possesses database-level access assurance and consistent service capability.
(3) It supports Memcached protocol but with better capability than Memcached (can be finalized). Cloud Memcached can be used in any scenarios where Memcached or TTServer is applicable.
(4) It creates an easy way for developing massive access business by ensuring the reliability, distribution and persistency on memory data.

## 2 Benefits for using Cloud Memcached

(1) Low cost. Self-built Memcached with master/slave hot backup mechanism using CVM costs 3.21 CNY/GB/day, while Tencent Cloud Memcached service only costs 2 CNY/GB/day.
(2) High performance. A single Cache server can support an access volume of 500 thousand visits per second, a single table supports a maximum of 10 million visits per second, with an average latency about 1 ms.
(3) Low latency, with an average of about 1 ms. 
(4) Secure and reliable with the capability of rollback during disaster recovery. Data is not lost upon server restart. It is equipped with master/slave hot backup mechanism with switching between master and slave visible to the service. It can be deployed cross racks and exchanges.
(5) Cloud Memcached is fully developed, stable and is equipped with a mature disaster recovery scheme. It serves massive third-party users and Tencent businesses, with daily access volume over 1 trillion. Developers may fully trust and use this long-tested service. It has been connected to many businesses such as Hoolai SanGuo, Fantasy City, Shushan Legend, Qzone, WeChat, etc.
(6) Care-free with automatic capacity expansion feature. The expansion process is transparent to user access and does not affect services. Cloud Memcached has a comprehensive monitoring and operation team who can handle failures for users during midnight.
(7) Easy to use, immediately available after application and no installation needed. You can access Cloud Memcached by directly using Memcached API.

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/NoSQLStorageAdvantagesV3.png)
