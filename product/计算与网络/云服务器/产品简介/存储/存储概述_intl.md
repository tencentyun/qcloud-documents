Tencent Cloud provides a wide range of flexible, economic and user-friendly data storage devices for the CVM instances. Various storage devices are provided to cater for different usage scenarios. The performance and price varies with the category of storage device.
## Storage Device Classification
Storage devices can be divided into the following categories by dimensions:
<table class="cbscategory">
        <tbody>
		<tr>
            <th style="width: 5%;">Dimension</th>
            <th style="width: 5%;" >Category</th>
            <th style="width: 20%;" >Description</th>
        </tr>
       
        <tr>
            <td rowspan="2">Storage medium</td>
            <td>HDD disk</td>
            <td>Uses mechanical hard disk as the storage medium. It is characterized by a lower price and a good read/write speed.</td>
        </tr>
				<tr>
				    <td>SSD disk</td>
					<td>Uses Solid State Drive (SSD) as the storage medium. It has an excellent performance in IOPS and read/write speed, with an IOPS and throughput up to 20 times and 16 times higher than those of HDD disk, respectively. It is more expensive than HDD disk.</td>
						
			    <tr>
            		<td rowspan="2">Application scenarios</td>
            		<td>System disk</td>
            		<td>Used to store the collection of systems that control and schedule the operation of CVM. It is operated by using images.</td>
        </tr>
				<tr>
				    <td>Data disk</td>
						<td>Used to store all the user data.</td>
						
						<tr>
						<td rowspan="3">Architectural pattern</td>
            <td>Cloud storage</td>
            <td>Cloud storage is an elastic, highly available, highly reliable low-cost and customizable network block device that can be used as a standalone scalable hard disk for CVM. It provides data storage at data block level and employs a 3-copy distributed mechanism to ensure the data reliability for CVM.<br><font style="font-weight:bold"> For a CVM with cloud storage, adjustments of hardware, disks and network are allowed.</font><br>
						</td>
        </tr>
				<tr>
				    <td>Local disk</td>
						<td>It is a local storage reserved on the physical machine where the CVM resides in. It allows a data access with a low latency, but involves a risk of single point failure.<br>
						<font style="font-weight:bold">For a CVM with local disk, you cannot upgrade hardware (CPU, memory and disk), and can only upgrade bandwidth.</font>
						</td>
				<tr>
				    <td>COS</td>
						<td>COS is a data storage device on the Internet. It allows data retrieval from any location on CVM instance or the Internet, thus reducing the storage cost. It is not suitable to be used as a storage medium in the low-latency and high-IO scenarios.
						</td>
				</tbody></table>

## Block Storage Device Mapping

Each instance has a system disk to keep the basic operation data. More data disks can be mounted to an instance. An instance uses block storage device-mapping to map the storage devices to locations it can identify.
Block storage is a storage device that puts data into blocks in bytes and allows random access. Tencent Cloud supports two types of block storage devices: local disk and cloud disk.
![](https://main.qcloudimg.com/raw/3815bb250f6178d67b8fe2be11a50bf8.svg)
This figure shows how CBS maps the block storage device to the CVM and maps `/dev/vda' to the system disk, and how it maps the two data disks to '/dev/vdb and /dev/vdc' respectively.
The CVM instance can automatically create block storage device mapping for the local disks and cloud storages mounted to it.


