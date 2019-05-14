
RAID is the abbreviation for "Redundant Array of Independent Disks".

It basic concept is to combine multiple physical disks with a relatively lower cost into a single disk array. Depending on the RAID level, RAID has a higher data integration, fault tolerance, throughput or capacity compared with a single hard disk. In one word, RAID is designed to improve read and write performance and fault tolerance.

In addition, RAID looks like a single hard disk or logical storage unit for the server.

## Setting RAID Level

You can set the RAID level when buying and reinstalling a CPM. Please follow the steps below:

<li>Purchase a CPM with RAID card.</br>
Without an RAID card, you cannot set the RAID level; A server with an RAID card can be set to HBA mode, i.e., NO-RAID.</li>

<li>
Select the right RAID level based on your business scenario
</li>

The example below shows how to set RAID when purchasing a PS100 CPM.

### Purchasing a CPM with an RAID card
![](http://mc.qcloudimg.com/static/img/dd57a46f906360a82803191f3df53030/image.png)
*Please check the CPM list in the purchase page. RAID field indicates whether the CPM comes with an RAID card*

In this step, we choose a PS100 CPM.

### Setting RAID level
![](http://mc.qcloudimg.com/static/img/6008262c2f3ed43d8d44f11cd3f24e41/image.png)
Please select different RAID levels in the interface.

### Frequently used RAID levels
<table>
<tr>
<th>RAID Level</th>
<th>Description</th>
<th>Number of disks required</th>
<th>Disk space utilization</th>

</tr>

<tr>
<th>RAID0</th>
<td>It is a simple, parity-free data striping technique that does not provide fault tolerance and redundancy.  </br>RAID0 makes data distributed across all disks and allows independent read/write operations on multiple disks at the same time, thus </br>offering the highest performance among all RAID levels.</td>
<td>n≥1</td>
<td>100%</td>


<tr>
<th>RAID1</th>
<td>It is consists of a mirror that writes an exact copy of a set of data to two disks: "Working Disk" and "Mirror Disk".</br>
The response time can be affected during the write operation, but the read performance is not affected.  </br> It provides the best data protection. In case of a failure of working disk, the system automatically reads data from the mirror disk without affecting user's operation.</td>
<td>2</td>
<td>50%</td>


<tr>
<th>RAID5</th>
<td>RAID 5 is a storage solution striking a balance among storage performance, data security and storage cost.</br>
The data, which is made into blocks, is distributed among the disks. With RAID 5, data is not backed up. Instead, the data and its parity information are stored on different disks. In case of data corruption on a single disk, the data can be restored with the remaining data and parity information.</td>
<td>n>=3</td>
<td>(n-1)/n %</td>


</table>



## Selecting RAID level upon reinstallation
![](http://mc.qcloudimg.com/static/img/0f493a30a26797694ce4e80ce1cb126f/image.png)
You can still select the RAID level upon reinstallation.

*Please note that <font color='red'>disk will be formatted</font> during the rebuilding of RAID. Please be sure to back up data in advance.*





