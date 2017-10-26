This section describes the design and implementation of backend distributed storage system of the Cloud Block Storage, and its storage system architecture is as follows:
![](//mccdn.qcloud.com/static/img/5bf39a359912506f94ab5e205422eb42/image.png)

Backend distributed storage system of Cloud Block Storage consists of three modules: Client, Master, and Chunk server.
- **Client**: It is usually deployed on the hypervisor and is responsible for:
	- First, disk virtualization. The abstract volume (virtual disk) of the storage pool is mapped to the local disk. The volume of the storage pool is made up of Blocks distributed on different Chunk servers. The client can map them into a unified logical address;
	- Second, storage protocol conversion. The user's IO request is split according to the fixed block size and the request is routed to a different Chunk server.

- **Chunk server**: it is a storage node, responsible for managing the allocation of Block and saving user data.
	- It saves three redundant copies for each user data to ensure data security. Each Block is distributed across three different Chunk servers.
	- It exercises user access authentication to protect user data isolation. Only the valid Client can access Chunk server data. Authentication control granularity depends on the Cloud Block Storage and user granularity.

- **Master**: It is responsible for managing the routing from the Client to Chunk server, and troubleshooting and recovery of Chunk server.
	- Master forwards the routing information to the Client, and then the Client forwards the user IO request according to the routing information.
	- Master is responsible for monitoring the status of Chunk server.When a disk breaks down or crashes in the cluster, Master eliminates the failed disk and starts data migration and recovery.
