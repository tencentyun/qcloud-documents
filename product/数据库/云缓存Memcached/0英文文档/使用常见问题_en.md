### 1. Does Cloud Memcached provide support for transactions? Or, does Tencent have any development plan for this feature?
Implementing transactions on a distributed storage system involves high complexity, and there is no effective solution to this problem now even in academia.
Support for transactional features is unavailable now in Cloud Memcached. Developers must implement rollback operations themselves to avoid affecting data consistency. It is recommended that developers reduce or eliminate reliance on transactions as can as possible.

### 2. Does Cloud Memcached provide APIs of Memcached?
No. You can download the open-source Memcached APIs.

### 3. We may have a very large amount of game data - To which extent can the Cloud Memcached expand capacity automatically?
No upper limit is set on the capacity supported by Cloud Memcached, as long as you have paid sufficient deposit. If your daily growth of business data is below 20%, automatic expansion can be implemented in Cloud Memcached. Otherwise you need to submit the application for a storage expansion using the template (submit a ticket to provide details).

### 4. Can Cloud Memcached clear all the data automatically?
Yes.
Please note that the data cannot be restored after being cleared. Before the clearing, please confirm that the data in the table has been backed up or is no longer used.
On the Cloud Memcached management view page in Console, click the "Clear" button next to the table to be cleared up. After your confirmation for the operation, the clearing begins at backend. When the clearing is completed, a message indicating the successful clearing will appear.

### 5. What is the maximum access capacity supported by Cloud Memcached? What should be done when capacity expansion is needed?
Cloud Memcached supports a maximum of access capacity of 10,000/sec/GB. The supported access capacity depends on the capacity actually allocated to the business. A higher capacity allocated to business means a higher access capacity. Cloud Memcached capacity is monitored by Tencent OPS system. If the daily growth of business data is less than 20%, the OPS system automatically implements expansion without user intervention. Otherwise, user needs to apply for a storage expansion (submit a ticket to provide details).

### 6. I have applied for 1 GB instance capacity - Why does the capacity displayed on console is less than 1 GB?
1. Cloud Memcached itself consumes some indexes and control meta information, which are counted into the 1 GB capacity but no charge is billed for these data.
2. In addition to the indexes and meta information, we also reserve some storage space for each instance to make provision for a business surge.
3. Indexes, meta information and reserved space account for almost 25% of the instance capacity, so the available space is about 75%.
4. We only charge you for the 75% available space. The prepaid fee for 1 GB space is frozen upon your first purchase, and is unfrozen in monthly settlement. After deduction of the fee for the actually used space from the prepaid fee, the balance is frozen for the next month.

### 7. Are Cloud Memcached operations atomic ones?
Yes.

### 8. Which protocols does Cloud Memcached support?
Currently, Cloud Memcached only supports Memcached open-source protocols, including commands: set, get, add, replace, append, prepend, cas, bget, gets, delete, incr, decr, quit, get_ext and gets_ext. Unsupported commands: stats, flush_all, version, verbosity. ERROR is returned when these commands are used. For more information about the commands, please see the description in Memcached text protocol list.

### 9. How to implement table capacity expansion in Cloud Memcached?
Table capacity expansion means increasing the table-occupied space, that is, storage expansion. Cloud Memcached automatically reserves about 20% of the space as a data growth buffer for each business each day. For example, if the space to be used for a business is 80 GB, it will allocate 96 GB to the business. If the business data has a daily growth of more than 20%, you need to submit an application for expansion (submit a ticket to provide details). Capacity expansion in Cloud Memcached is a data migration process, which does not affect the hit rate. 

### 10. How to implement table capacity reduction in Cloud Memcached?
Table capacity reduction refers to the reduction of table-occupied space, that is, storage capacity reduction. Because of the need to reserve buffer space, the table utilization after capacity reduction will not exceed 80%. The table capacity is reduced by a minimum of 1 GB decrement. A reduction that can cause a utilization above 80% is not allowed. 
For example: 
If table-occupied space is 2 GB with a table utilization of 41%, capacity reduction is not allowed. This is because the reduction of 1 GB will make the table utilization exceed 80%. 

Currently, Cloud Memcached tables do not support automatic capacity reduction. To implement capacity reduction, you need to submit a ticket for an application. Our OPS personnel will implement capacity reduction for you.
Before your application, the service is still charged based on the originally occupied space (including the buffer space expanded automatically from the original used space) during peak hours.

### 11. How to implement interface/port expansion or enable/disable expire in Cloud Memcached?
For interface/port expansion in Cloud Memcached, you need to submit an application (submit a ticket to provide details), which will be handled by Tencent technical support personnel at the backend. To enable or disable expire, you can also submit an application using a template if operations on pages are impossible.

### 12. The client connection to Cloud Memcached service failed or has a low success rate.
This is may be caused by the server where your client resides in or by the network environment between the client and Cloud Memcached. Cloud Memcached provides tools for diagnosing the server environment of client and the connection problems between the client and Cloud Memcached. For more information , please see [Cloud Memcached Connection Diagnostics](/doc/product/241/云缓存Memcached连接诊断).
### 13. Does Cloud Memcached support binary protocol?
No. Please use an ascii-protocol-based client.
