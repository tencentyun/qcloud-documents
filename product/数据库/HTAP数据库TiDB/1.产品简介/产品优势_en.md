


**Infinitely Scalable MySQL** 

The share-nothing distributed architecture supports distributed transactions and elastically horizontal scaling with strong consistency. No matter how large the volume of data is, the problem can be solved simply by adding a node. Developers don't need to consider distributed transactions and consistency issues, greatly simplifying code design and maintenance. It's an ideal alternative to traditional distributed database middlewares (Cobar, TDDL, MyCAT and KingShard).

**Compatible with MySQL Protocol**

Support all peripheral tools of MySQL community (drivers, management tools and application frameworks) such as myloader/mydumper/MySQL JDBC Driver/Navicat/Workbench/WordPress/mainstream ORM frameworks.


**The Greater the Volume of Data, the Faster the Reading and Writing**

It provides a high-concurrency and high-throughput clustered capability with unlimited linear scalability just through addition of nodes, and has a superior advantage over MySQL in terms of performance of random writing and complex queries in case of massive data volume (tens of millions of bytes).

**OLAP Performance**

It can perform large volume of complex queries in parallel, including aggregation and join.


**Multi-site active-active Data Centers**

Based on Raft distributed voting algorithm, multi-replica writing, and splitting, aggregation and redistribution of data sharding are automatically completed. 100% strong consistency of data is ensured across availability zones. This ensures that data will not be lost and automatic switch is enabled in case of crash in any availability zone.

**Cloud Database DBaaS**

The bottom layer achieves the most effective isolation, assignment and scheduling of resources at the data level via technologies such as Kubernets, Docker, and multi-tenancy. It provides automatic fault recovery, one-click scale-up and rolling upgrade, making operation and maintenance easier and cheaper.











