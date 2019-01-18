
**HTAP Database** (HTAP Database for TiDB) is a distributed database product developed by Tencent Cloud based on the latest domestic NewSQL open source database TiDB, which supports both Online Transaction Processing (OLTP) and Online Analysis Processing (OLAP). The product breaks the boundary of traditional business architecture by allowing two services to run based on the same data, eliminating the complex process of replicating data from the operational database and loading it to data warehouse after landing and conversion, which greatly reduces data storage costs, shortens the delay time of data analysis and processing, and provides guarantee for real-time commercial analysis and decision-making.

Inspired by the Google Spanner/F1 paper, its design enables important NewSQL features such as automatic horizontal scaling, distributed transactions with strong consistency, and multiple replicas based on the Raft algorithm. It makes the deployment simple by combining the advantages of RDBMS and NoSQL. Elastic expansion and asynchronous table structure changes do not affect the online services. It provides users with true multi-active data centers in regions and automatic fault recovery services. It is also compatible with MySQL protocol, enabling users to migrate at lowest cost.



> **HTAP** (Hybrid Transactional/Analytical Processing) is a noun proposed by Gartner, a famous American consulting firm.

![](//mc.qcloudimg.com/static/img/c5fd383a013002f299e2b1c65ccd0810/image.png)






