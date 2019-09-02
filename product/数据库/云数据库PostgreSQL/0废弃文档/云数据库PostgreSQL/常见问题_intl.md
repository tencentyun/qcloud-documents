### Why the used storage space increases with no data inserted? 
It's due to PostgreSQL's MVCC mechanism: 1) Rows deleted will not be physically deleted directly; 2) Rows are updated by inserting a new row, and expired data will not be physically deleted directly. So, the data volume will increase even with no data inserted.

The parameter "autovacuum" is enabled for the database by default. The kernel automatically reclaims expired data, and then the used storage space will be automatically freed up. You can also manually execute the "VACUUM" command to reclaim expired data, which will not lead to an immediate drop in the statistics on storage, but will reclaim and mark them as reusable. To clean up the data completely, use the "VACUUM FULL" command with parameters. (It is strongly recommended to use the command only during maintenance, as it will lock tables.) 
For more information on the "VACUUM" command, see [PostgreSQL official documentation](https://www.postgresql.org/docs/current/static/sql-vacuum.html).

### Why does my CPU utilization exceed 100%?
By default, PostgreSQL adopts the policy of excess usage of idle resources that allows your business to preempt some idle CPU resources. Therefore, when the number of CPU cores of your instance exceeds the default value, your CPU utilization may appear to exceed 100% in the monitoring view.

But if your CPU load always exceeds 60%, it is recommended that you upgrade your database as soon as possible.


### Why is the occupied disk capacity larger than the actual data volume?

Updates will cause xlog to rapidly grow in size. The logs will occupy disk space if the system doesn't archive and delete them in time. Or, the query operations include a large number of sort and connection operations involving a huge amount of data. This process produces temporary tables which will overflow to the disk and occupy disk space for a short time.


### How to enable/use plug-ins

Most commonly used plug-ins are supported by TencentDB for PostgreSQL and can be directly used. However, the super admin permission is required to enable certain plug-ins. You can enable them on the Tencent Cloud console. Or you can contact Tencent personnel and describe your instance ID and name of the plug-in to enable it.

