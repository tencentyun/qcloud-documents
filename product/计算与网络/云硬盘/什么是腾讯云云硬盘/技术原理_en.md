## Data Organization
We divide the storage space on Chunk server into several blocks with a fixed size, which are the basic units for space allocation and recovery; the uniform logical address space visible to users is comprised of the blocks distributed on different chunk servers; chunk server is responsible for distributing blocks, and saving user data.

If the routing of entire system is managed using block as granularity, it will definitely place huge pressure on the memories of Master and Client (for a PB-level system, its routing entries may reach the GB level). To optimize routing, most distributed storage systems will add a logical management layer based on the block, which is called partition.

Partition is the basic unit of routing and failure recovery, each of which contains several blocks; with the introduction of partition, routing entries can be reduced to the MB level.

![](//mccdn.qcloud.com/static/img/07dad25d196a1511bd8b46174ca8eb3d/image.png)

## Consistent Hashing
**Consistent hashing will solve node failure.**

In the distributed systems, the node failure often happens. Therefore, the primary consideration in distributed system design is how to reduce the impact of node failure on user access, and decrease the volume of data needed to migrate for failure recovery. Consistent hash algorithm can effectively solve the two issues, so it is widely applied in the distributed system design.

In order to balance user accesses, we divide hash ring into more than one hash node, which corresponds to a partition group (including three partitions), and different hash nodes may correspond to the same partition group.

- First, each cloud disk has a unique disk ID, and the disk ID and the block ID (ID in logical address space) in user request can constitute a unique key to identify a block;
- Then, the specific hash node can be located in the consistent hash ring using the key to find the partition group that the block belongs to. The partition group contains IP of the chunk server three copies of data belongs to, as well as the disk information;
- Finally, the client will forward the request to the specified chunk server based on the information.

![](//mccdn.qcloud.com/static/img/6b29e258c2bb0c2008f1d2e19a9b7517/image.png)

## Multiple-copy Redundancy
**Multiple-copy redundancy is used to ensure data reliability.**

Since we apply the storage of three copies, in case of the exception of any copy, the other two copies of data must be available, which requires the three copies of data to be strictly consistent.

Usually, there are two methods to write multiple copies in the distributed system:
Write multiple copies directly from the client to the stored copies;
First write to master copy from the client, and then synchronize the data to auxiliary copies by the master copy.

The first method has lower write latency but higher network traffic pressure due to the fact that the client writes three copies of data, while the second method has lower client traffic pressure but higher write latency.

We have applied the trade-off solution: the client first writes the master copy, and also writes two auxiliary copies, and then it will return the result of write success to users after the auxiliary copies are updated successfully. The principle is that it is required to write three copies of data successfully before returning the result of success to users. For read requests, request data directly from the master copy.

![](//mccdn.qcloud.com/static/img/1724b5db3c838602c6e4bb71093c09f8/image.png)

## Fast Recovery
**Incremental recovery policy will rapidly resolve copy failures.**

In the distributed system, the copy failure often happens, during which the distributed system provides degraded services. How to complete the data recovery fast is one of the important metrics to measure the performance of storage system.

There are many reasons resulting in the copy failures, such as hardware problem of storage device itself, network problem, drive or internal procedure bug, etc.

If the same recovery method is used for all the failures, the recovery cost will be higher. For example, for 4T sata disk with limited disk bandwidth, it will take about 23 hours to recover at the rate of 50MB/s, and the recovery cost is even higher for recovery of the whole machine.

In fact, except the hardware failure, the software or network failure can actually be recovered in a short time, and there are not many data changes occurred during this period.

We apply incremental recovery technology to speed up the data recovery for users. The incremental recovery means that, after the recovery of failure node, only data changes during the failure need to be synchronized to the main node, for which the volume of data is far less than that for recovery in full volume.

![](//mccdn.qcloud.com/static/img/fb13ace73a2e0eb5dac28f78bd95b8f8/image.png)

**Incremental recovery policy**:
The smallest logical unit of migration recovery is partition, and the smallest physical unit is block. Each block has its own seq number to be maintained, which will be auto incremented for each update. The user's new write request will still be written into three copies (including the failure recovery copy), but the new data for the failure copy can only be written in the memory cache, and cannot be refreshed to the disk. The comparison of block seq numbers between the failure copy and master copy will be performed in the backend process; if the numbers are the same, data will skip recovery, and if different, data will be recovered to the disk of failure copy.

![](//mccdn.qcloud.com/static/img/1f7135c4c04fba632ebd4ae9c9ec8167/image.png)

## Data Migration
**Data migration policy can resolve irreversible hardware failures.**

For irreversible hardware failures, it is impossible to recover fast, and it will take more time to replace physical devices. In this case we may need to perform the data migration in full volume, that is, to migrate all data of the failed partition to the other three normal partitions.

Three destination partitions are allocated by Master. After the user's new request is written into master node, it will also be written to the other auxiliary copy and destination master copy. Then it will be synchronized to two destination auxiliary copies by the destination master copy, and the existing data will be synchronized from the source master copy to the destination copies by the backend process.

Here it is necessary to take into account the mutual exclusion between the backend process and the user's write request, and the specific implementation mechanism is the same with that of fast recovery.

![](//mccdn.qcloud.com/static/img/086b806102327a1e874df22f413339a9/image.png)

## Snapshot
**Snapshot is used for data disaster recovery; the snapshot rollback function can be applied for the real-time data rollback.**

Snapshot refers to a complete copy or image of data collection at a certain point in time (the time point when starting to copy). If the data of production system is lost, it can be fully recovered to the snapshot point in time using the snapshot, so it is an important approach for data disaster recovery.

Disk snapshot is to block the disk data at a certain point in time in order to form a copy, and when necessary, data on the copy can be traced back anytime. It is a very useful system for reinforcement or regular backup of user data.

**Snapshot storage**:
There are two approaches for snapshot storage: one is to keep snapshot data and disk storage data together; the other one is to store snapshot data in the third-party system.

The first approach has the advantage of faster snapshot creation and rollback for users, but is not really effective for disaster recovery. The second approach can be really effective for disaster recovery, but it will consume a certain amount of time and bandwidth in the process of data migration. Considering that the core requirement for snapshot is to achieve real disaster recovery, we choose the second approach.

We store the snapshot data in TFS system isolated from the production system with different storage engines. In addition to disaster recovery for the hardware, disaster recovery can also be implemented at the software and operation level.

**Snapshot creation**:
After the snapshot is created, we will immediately start the backend process to copy the user data from production system to snapshot system. In order to ensure the consistent point in time for the user data, we have applied multiple versions and Cow (Copy on Write) technology in the snapshot design.

Every time a user creates snapshot, the write data version of the user will be auto incremented, and new block will be assigned for saving data to avoid the change of original data, so as to ensure the data has consistent point in time.

Since the snapshot assignment also uses block as granularity, and the user write data may not cover the whole block, when the user writes at the first time, the data on old block needs to be copied to new block before it is changed. All the old blocks will be copied to the snapshot system by the backend process.

Therefore, creating snapshot is an instant process, but it takes some time to complete the backup of all snapshot data, and the time varies depending on the bandwidth for backup.

![](//mccdn.qcloud.com/static/img/de1ff31e363ad1e7fac17298403e1575/image.png)

**Snapshot rollback**:
The real-time rollback of data is implemented by using the trigger mechanism for read/write.

Once the user has used the snapshot for rollback, the rollback process will be immediately started to implement the data mitigation, during which the user can use the snapshot data.

Blocks mitigated completely are recorded using bitmap in the backend. When a user is requesting, it will first check whether the rollback action has been completed for the corresponding block. If the rollback is not completed, it will first block the user request, give priority to the block to trigger its rollback, and perform the user request after the rollback is completed, so that the user can use rollback data in real time.

![](//mccdn.qcloud.com/static/img/f359c850d50a92c328f114ea7e525c8d/image.png)

**Create disk using snapshot**:
The mechanism is similar to snapshot rollback, that is, to provide the capability to quickly clone disks in batch to meet the requirements of server deployment in batch.

## Continuous Data Protection
**Continuous Data Protection (CDP system) is used to eliminate the RPO window of snapshot to guarantee the integrity of the data disaster recovery results.**

Although the snapshot can effectively and quickly recover the data to a certain point in time, but as a certain RPO window exists, the part of data lost in the window may be the lifeline of a business.

In order to completely eliminate the RPO window, we have introduced the CDP mechanism. Its implementation is very simple, that is, all the change requests of users, in addition to being applied to the production system, will be bypassed to the CDP system. When data corruption occurs in the online system of users, you can replay the request to help users to recover to the data at any point in time.

We have combined the changed data of snapshot retained for 7 days in the CDP system, to ensure that users can recover to the data at any time within 7 days, completely resolving users' concern about data loss.

![](//mccdn.qcloud.com/static/img/b31fd3844df86ad4973899f0f5ad0a88/image.png)


