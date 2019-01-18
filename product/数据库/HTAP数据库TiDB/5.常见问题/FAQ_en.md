## 1. Is HTAP Database for TiDB Developed Based on MySQL?

No, but HTAP Database for TiDB Supports MySQL syntax and protocol.

## 2. Is It Easy to Use?

Yes, HTAP Database for TiDB is easy to use. After you start the entire set of service, you can use HTAP Database for TiDB as a normal MySQL Server. You can use HTAP Database for TiDB in any application that uses MySQL as backend storage service without any major changes to your application code. It's compatible with most MySQL management tools.

## 3. How to Migrate Applications Running on MySQL to HTAP Database for TiDB?

HTAP Database for TiDB supports the majority of MySQL syntax and generally it's unnecessary to modify the code. You can use the tool Checker to check whether Schema in MySQL is compatible.

## 4. How to Improve Performance by Extending HTAP Database for TiDB?

As business continues to grow, the database may face three bottlenecks:

- The first one is insufficient storage resources, that is, disk space is not enough;
- The second one is insufficient computing resources, such as high CPU utilization; 
- The third one is throughput.

A horizontal expansion can be performed for database cluster.



- If there are not enough storage resources, you can add a TiKV Server node. After the new node is started, PD will automatically migrate part of the data of other nodes to it without manual intervention.
- If there are not enough computing resources, you can check the CPU utilization of TiDB and TiKV nodes, and then consider adding TiDB or TiKV nodes to solve the problem.
- If throughput cannot satisfy your needs, you can generally consider adding both TiDB and TiKV nodes.




