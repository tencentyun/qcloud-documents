## 1. High-IO Version
### 1.1 Purchase Instruction
The brand new high-IO version was released on June 15th, 2015. Its performance grew tenfold compared to before.
It has been completely released in Guangzhou region. High-IO version will be delivered by default when users purchase new cloud databases.
A gated launch has been carried out in Shanghai region. Users may purchase high-IO version through whitelist. Whitelist application link: http://manage.qcloud.com/cdb/apply.php 
High-IO version is currently not supported in Hong Kong and North America regions.

The page for purchasing high-IO cloud database is shown below:
![](//mccdn.qcloud.com/img568280339e902.png)

### 1.2 Performance of High-IO Cloud Database

For details, see:  [Performance of High-IO Version](http://www.qcloud.com/doc/product/236/%E5%90%84%E7%89%88%E6%9C%AC%E6%80%A7%E8%83%BD%E8%AF%B4%E6%98%8E#2-高io版性能说明)

##  2. High-performance Version
High-performance cloud database is a MySQL service platform with high performance level and high reliability. It is newly developed by Tencent Cloud, aimed to satisfy the operation demands for MySQL businesses.
It improves the IO capabilities for standalone storage through distributed storage mechanism, which in turn improves the query performance of single MySQL instance database. It also keeps the data in databases secure and reliable by storing multiple copies of data on multiple nodes. High-performance version is compatible with the instance management and statistical features of standard version. You can use the high-performance version in exact the same way as you use the standard version. This version is especially suitable for applications that require high performance on single MySQL instance and high data security.

### 2.1 Infrastructure

High-performance version achieves final data storage by using cloud storage. The infrastructure is shown below:
![](//mccdn.qcloud.com/img568281130fbe2.png)

### 2.2 Other Features

Features include hot backup, failure recovery, data cold backup and monitoring statistics, etc. The same features as the existing standard version (see here)

### 2.3 Restriction

#### 2.3.1 InnoDB Storage Format

For InnoDB storage engine, high-performance version uses DYNAMIC format by default. Users are advised not to modify this format in order to avoid affecting normal usage.

#### 2.3.2 Maximum Number of Concurrent Transactions Supported

Currently, this version supports a maximum of 1,000 concurrent transactions.

#### 2.3.3 Maximum In-row Record Length Supported by InnoDB

The maximum in-row record length supported by high-performance InnoDB is 1,982 bytes. The following error will occur if this limit is exceeded:

```
ERROR 1118 (42000): Row size too large. The maximum row size for the used table type, not counting BLOBs, is 1982. You have to change some columns to TEXT or BLOBs 
```

## 3. The Overall Structure of Standard Version

### 3.1 Hot Backup and Failure Recovery

The standard version provides hot backup support by using the Replication characteristic of MySQL, where master and slave are deployed separately on two independent high-performance storage machines. The SAS disk array used by the machines provides reliable data storage. As shown in the figure below:

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukubiaozhunbanshuoming-1.png)

The MySQL client does not connect to the master and slave directly. The connection is forwarded via the access module instead. This means requests can be automatically transferred to slave when master fails. Thus, seamless handover is achieved. As shown in the figure below:

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukubiaozhunbanshuoming-2.png)

When master fails and requests are transferred to slave, the automatic migration procedure will be initiated, in which case the data will be migrated to another pair of master/slave machines. When the process is completed, requests will be transferred to the new master/slave machines at the relay module, achieving a migration process that is transparent to the user. As shown in the figure below:

![](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yunshujukubiaozhunbanshuoming-3.png)

### 3.2 Cold Data Backup

The cloud database will back-up its data on a daily basis and store the data in the backend cold backup center. Cold backup data will be retained for 4 days, which means you can use this data to reverse your business data to 5 days ago. Refer to Cloud Database Cold Backup Data Retrieval for details if you wish to retrieve your cold backup data.

### 3.3 Comprehensive Monitoring and Statistical Features

Cloud database provides monitoring and statistical features for critical data in various dimensions, such as disk IO, network traffic, CPU usage, connection, query, slow query, master-slave synchronization, data backup. Refer to Monitoring Services for details.


Users are advised to keep the storage length of in-row records as short as possible. For example, try to declare the length of varchar fields as 256 or above (in which case the fields will be stored outside rows), or use text/blob as replacement. In addition, the total number of text\blob\varchar fields cannot exceed 48 

### 3.4 InnoDB Does Not Support compressed

To improve performance, high-performance version adopted O_DIRECT method to handle IO, while the page size and disk sector size of innodb engine are also adjusted. compress format is not supported due to system restrictions.

