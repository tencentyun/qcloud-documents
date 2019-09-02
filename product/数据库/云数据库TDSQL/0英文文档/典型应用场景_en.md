## Data Cloud Disaster Recovery (Remote Disaster Recovery)

Data is indispensable to enterprise operations. Informatization brings convenience while it has drawbacks that electronic data and stored information are easy to damage and lose. Facing natural disasters, system failures, employee misoperation and virus infection, enterprises may suffer operation interruption and even catastrophic losses due to any of the accidents. Therefore, each enterprise must ensure the security and integrity of data, especially the core database.

However, building a remote data disaster recovery center is usually a great expenditure for enterprises, including huge costs for hardware and software in the data center and annual operating costs for continuous maintenance. Spending so much money for accidents of low probability does not match enterprises' financial needs.

Therefore, you can use cloud databases and cloud access products to directly build a cloud data disaster recovery center database. In this way, you can synchronize the data in main data center to the cloud remote backup center through the security private network. It helps you operate and manage massive data in a cost-effective manner.
 


## Launch Business System on the Cloud

If you have not launch business system on the cloud, you may face the following situations:

- Business is developing rapidly. However, if you prepare the server based on peak business every year, its growth scale will cause a huge cost.
- A new business department usually needs to launch new businesses quickly. However, if preparations and purchase are needed every time, it is bound to affect efficiency.
- Almost every business system has experienced that visits surge to a record high so that backend resources cannot support the system.
- Many enterprise leaders believe that IT department is the cost center, so the core concerns for them are not to promote business, but to solve problems such as system instability and performance poverty.

Facing challenges such as launching business systems on the cloud, Tencent Cloud database can provide you with the following based on years of heritage:

- Secure and open database solutions;
- High availability solutions, with strongsync replication technology and high availability (HA) re to achieve high disaster recovery;
- Auto Scaling.

## Hybrid Cloud

CDB for MariaDB (TDSQL) supports private cloud deployment solutions, and can be deployed in the data center built by users. Business systems and data are synchronized securely through Direct Connect (or VPN) to build an easy-to-scale up hybrid cloud architecture.

## Read/Write Separation
All slaves of cloud database instances support read/write separation strategy by default, meaning that the slaves can be read-only.
 
- You can achieve the read-only feature via SQL syntaxes or read-only accounts.
- If you configure multiple slaves, the read-only policy will load automatically.
- You can add more slaves by upgrading the configuration.


## Development Test
You may need to maintain multiple software version environments for tests, and even require large resources for stress tests.

The traditional solution is to build servers and databases by yourselves. However, the test resources are seldom used by developers, so they are often idle and many hardware resources are wasted. In contrast, with the auto scaling of CVMs and cloud databases, you can effectively solve the problems of test resource insufficiency or waste.

