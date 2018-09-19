> Currently, DCDB is only applicable for OLTP businesses, such as trading system, frontend system, but not for systems with a large number of OLAP businesses, such as ERP, BI, etc.

## Large Applications (Real-time Transaction with Ultra-high Concurrency)

Service providers from e-commerce, finance, O2O, social applications, retail, SaaS industries generally have the following problems that restrict the development of business: a large user base (up to a million or above), frequent marketing activities and slower response from core trading system database. DCDB provides linear scale-out feature to improve processing capacity in real time and increase the access efficiency up to over 15 million QPS, allowing rapid respond to real-time transactions with high concurrency.

Currently, WeChat Pay, Tenpay, pay.qq.com, JD.com, taobao.com and many other platforms use the DCDB-based database.
  
## IoT Data (Storage and Access of PB-level Data)

Many sensor monitoring devices with high sampling rate and large-scale data are used in IoT scenarios, including industrial monitoring and remote control, extension of smart city, smart home, Internet of Vehicles, etc. Generally, data stored for a year can reach PB level or even EB level. However, traditional database based on x86 server architecture and open source database solution cannot store or use such huge volumes of data. DCDB provides capacity scale-out feature and the compression capacity of storage engines (such as tokudb) to help users store massive data at a low cost (relative to the shared storage solution).
  
## File Index (Instant Access to Trillions Lines of Data)

Generally, a cloud service platform contains hundreds of millions to trillions of images, documents and video data. Service platforms need to store the indexes of these files and perform addition, modification, read and deletion (in case of a large file, the index is deleted instead of the file) operations at index level in real time. The access of other users to the service platform makes the requirement extremely high for service quality and performance. Traditional database cannot support such a large volume of access and usage. With ultra-high performance and scalability in combination with strongsync capability, DCDB effectively guarantees the platform's service quality and data consistency.
  
## Cost-effective Business Database Solution

To support the storage of large-scale data and the access to database with high concurrency, government agencies, large enterprises, banks and other industries rely heavily on small servers and high-end storage. Internet companies can achieve a performance that is the same with or even higher than that of business database using low-cost x86 server and open source software. DCDB is applicable for scenarios including the integration of national or provincial business systems, e-commerce and channel platforms of large enterprises, Internet businesses and trading systems of banks, etc.



