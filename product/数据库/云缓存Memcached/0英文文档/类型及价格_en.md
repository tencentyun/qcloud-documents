## 1. Billing of Cloud Memcached

1. Cloud Memcached is charged based on the assigned storage capacity. Space less than 1 GB will be counted as 1 GB.
2. Table capacity reduction means to reduce the space occupied by the table, i.e. storage capacity reduction. Because of the need to reserve buffer space, the table utilization after capacity reduction will not exceed 80%. The table capacity is reduced by a minimum of 1 GB decrement. A reduction that can cause a utilization above 80% is not allowed. 

Currently, Cloud Memcached tables do not support automatic capacity reduction. To implement capacity reduction, you need to submit a ticket for an application. Our OPS personnel will implement capacity reduction for you.

Before your application, the service is still charged based on the originally occupied space (including the buffer space expanded automatically from the original used space) during peak hours. 

## 2. Price of Cloud Memcached

Cloud Memcached is priced as below:

<table class="t" style="display:table;width:80%;">
<tbody><tr>
<th> Resource
</th><th> Configuration
</th><th> Price/GB/day
</th></tr>
<tr>
<td> Cloud Memcached
</td><td> With hot backup<br>
<p>A maximum of 10,000 visits per second is supported for 1 GB storage space. For example, if you apply for 10 GB storage, the access volume is limited to 100,000 visits per second.<br>
</p>
</td><td> 2 CNY/GB/day
</td></tr></tbody></table>
