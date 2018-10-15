### How do I connect to Redis?
 If the CVM and the database are deployed in the same region, perform access via a private network. For more information on how to connect to Redis, see [Connection Guide](https://cloud.tencent.com/document/product/239/9897).

 ### How do I connect to Redis if the CVM and the database are deployed in different regions?
 If communication is available between basic networks and VPCs, see [Classiclink](https://cloud.tencent.com/document/product/215/5002).
 If communication is available between VPCs, see [Peering Connection](https://cloud.tencent.com/document/product/215/5000).

 ### Why do I fail to ping CRS? 
 By default, the ping command is not allowed for Redis. You can use telnet to test the connectivity.

 ### How do I enable access to CRS via public networks? 
 Access to CRS via public networks is not supported at the moment, but will be available in the future.
 But you can achieve this indirectly through a CVM with public networks by means of the Iptable proxy.

 ### How do I configure password-free login for Redis? 
 Password-free login is not supported at the moment, but will be available in the future.


