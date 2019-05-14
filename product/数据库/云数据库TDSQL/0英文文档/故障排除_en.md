#### What if the database parameter to be modified cannot be found in parameter configuration options or some parameters cannot be modified?
Tencent Cloud Database Console supports most of the common database parameters, and sets the security thresholds for each parameter. If the parameter to be modified does not exist, or you cannot modify it to a specified value, please submit a ticket and we will process it as soon as possible.

#### Do I need to configure read-write separation on the program?
Read-write separation of database is not configured automatically. You need to first [create a read-only account](https://cloud.tencent.com/document/product/237/2081) in the console, and modify the program configuration.

#### Why does my CPU utilization exceed 100%?
By default, MariaDB (TDSQL) adopts the policy of excess usage of idle resources that allows your business to preempt some idle CPU resources. Therefore, when the number of CPU cores of your instance exceeds the default value, you will see in the monitoring view that your CPU utilization excess 100%.

But if your CPU load always exceeds 60%, it is recommended that you expand the database as soon as possible.

#### The monitor says I always run out of the 16 GB memory I purchased. But why is the business not affected?
The memory allocation mechanism of the database uses the idle memory to improve the cache hit rate, rather than reading data from the disk. Therefore, it is normal that your memory is run out. Generally, you only need to consider whether your business performance is affected.




