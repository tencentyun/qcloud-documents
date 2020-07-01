Tencent Cloud provides a wide range of flexible, economic and user-friendly data storage devices for the CVM instances. Various storage devices are provided to cater for different usage scenarios. The performance and price varies with the category of storage device. Storages can be divided into the following categories by dimensions:

<table class="cbscategory">
        <tbody><tr>
            <th style="width: 5%;">Dimensions</th>
            <th style="width: 5%;" >Categories</th>
            <th style="width: 20%;" >Description</th>
        </tr>
       
        <tr>
            <td rowspan="2">Storage medium</td>
            <td>HDD hard disk</td>
            <td>Use mechanical hard disk as the storage medium. It is characterized by a lower price and a better read/write speed. </td>
        </tr>
				<tr>
				    <td>SSD hard disk</td>
						<td>Use Solid State Drive (SSD) as the storage medium. It has an excellent performance in IOPS and read/write speed. It can achieve an IOPS and throughput up to 20 times and 16 times higher than those of ordinary hard disk, respectively. It is more expensive than ordinary hard disks.  </td> 
						
						        <tr>
            <td rowspan="2">Storage contents</td>
            <td>System disk</td>
            <td>Used to store the collection of systems that control and schedule the operation of CVM. It is operated by using image. <br>
						</td>
        </tr>
				<tr>
				    <td>Data disk</td>
						<td>Used to store all the user data. </td>
						
						<tr>
						<td rowspan="3">Architecture</td>
            <td>Cloud disk</td>
            <td>Cloud disk is an elastic, highly available, highly reliable low-cost and customizable network block device, which can be used as a standalone scalable hard disk for CVM. It provides data storage at data block level and employs a 3-copy distributed mechanism, thus ensuring the data reliability for CVM. <br><font color="red">For a CVM using cloud disks, adjustments can be made to hardware, disks and network.</font><br>
						</td>
        </tr>
				<tr>
				    <td>Local disk</td>
						<td>Local disk comes from the local storage of the physical machine where the CVM resides. It is a storage area reserved on the physical machine where the CVM resides. It allows the data access to be achieved with a low latency, but involves a risk of single point failure. <br>
						<font color="red">A CVM for which local disk is selected does not support the upgrade of hardware (CPU, memory) and only supports upgrade of bandwidth. </font>
						</td>
<tr>
				    <td>Object storage </td>
						<td>Object storage is a data storage device located on the Internet. It allows data retrieval from any location on CVM instance or the Internet, thus reducing the storage cost. It is not suitable to be used as a storage medium in the low-latency and high-IO scenarios.
						</td>
				</tbody></table>


## Cloud Disks

Cloud Block Storage is a persistent storage device at data block level. You can use it in the same way as you use an external hard disk for a computer. Cloud Block Storage is featured by high availability and high reliability and employs distributed storage technology to ensure a data availability of not less than 99.99%. It is suitable to be used as a main storage device (such as file system and database) for the data that requires frequent and fine-grained updates.

You can mount multiple elastic Cloud Block Storages to one instance, or dismount them from one instance and mount to another instance at any time. With its life cycle being independent of CVM instances, elastic Cloud Block Storage can be stored independently as a storage medium for important data.

You can keep a backup copy of data by creating a snapshot for Cloud Block Storage. You can also create a new Cloud Block Storage from the snapshot at any time and connect it to another instance. For more information about Cloud Block Storage, see [Tencent Cloud Cloud Block Storage product documentation](https://cloud.tencent.com/document/product/362).

## Local Disks

Local disk is a storage medium located on the same physical machine as the CVM instance and can provide low-latency storage for the instance. The data on the local disk will only be retained for the life cycle of CVM instance and will be lost when the CVM is destroyed. For more information, see [Local Disk](/doc/product/213/5798).

## Cloud Object Storage (COS)

Tencent Cloud COS is a data storage device located on the Internet. It allows data retrieval from any location on CVM instance or the Internet, thus reducing the storage cost. For example, you can use COS to store the backup copies of data and applications. For more information, see [Tencent Cloud COS product documentation](https://cloud.tencent.com/document/product/436).

## Block storage device mapping

Each instance has a system disk to keep the basic operation data. More data disks can be mounted to an instance. How to identify these storage devices in an instance? In fact, an instance uses block storage device-mapping to map the storage devices to locations that can be identified by it.

Block storage is a storage device that puts data into blocks in bytes and allows random access. Tencent Cloud supports two types of block storage devices:

- Local disk
- Cloud disk

![](https://mc.qcloudimg.com/static/img/7e8715ce6bba831c61d0cc807bec8ce9/device-mapping.png)

This figure shows how CBS maps the block storage device to the CVM and maps /dev/vda' to the system disk, and how it maps the two data disks to '/dev/vdb and /dev/vdc' respectively. 

The CVM instance can automatically create block storage device mapping for the local disk and cloud disk that are mounted to it. 
