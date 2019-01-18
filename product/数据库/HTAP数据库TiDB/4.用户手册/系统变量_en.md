
## How to Set Up ##

Variables can be set by using the SET statement, as shown below:



    set @@tidb_distsql_scan_concurrency = 10

If you need to set a global variable, execute statement below:

    set @@global.tidb_distsql_scan_concurrency = 10


## System Variables ##

**tidb_distsql_scan_concurrency**

Scope: SESSION | GLOBAL

The default value is 10

This variable is used to set the concurrency of the scan operation. OLAP applications are suitable for larger values while OLTP applications for smaller values. For OLAP applications, the maximum value is recommended not to exceed the count of CPU core of all TiKV nodes.


**tidb_index_lookup_size**

Scope: SESSION | GLOBAL

The default value is 20000

This variable is used to set the batch size of the index lookup operation. Larger values are suitable for OLAP applications while smaller values for OLTP applications.


**tidb_index_lookup_concurrency**

Scope: SESSION | GLOBAL

The default value is 4

This variable is used to set the concurrency of the index lookup operation. Larger values are suitable for OLAP applications while smaller values for OLTP applications.


**tidb_index_serial_scan_concurrency**

Scope: SESSION | GLOBAL

The default value is 1

This variable is used to set the concurrency of the sequential scan operation. Larger values are suitable for OLAP applications while smaller values for OLTP applications.



