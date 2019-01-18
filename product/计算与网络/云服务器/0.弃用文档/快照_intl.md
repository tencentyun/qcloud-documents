Snapshot is a way of data backup provided by Tencent Cloud, which can create a fully usable copy of a specified cloud disk so that the backup is independent of the life cycle of the cloud disk. Snapshots include the images of the cloud disk at the time when the copy starts. Snapshots do not occupy users' storage space, and Tencent Cloud will store the snapshots created by users redundantly in multiple available zones to further ensure the reliability of backups. Snapshots are incremental backups, which means only the data changed after the latest snapshot creation will be saved. In this way, the time needed to create snapshots will be minimized and storage cost will be reduced.

You can create new cloud disks from snapshots, and the cloud disks will have the data in the snapshots upon creation, and can be used as an accurate copy of the original cloud disk. Snapshots are region-related, which means that snapshots can only be used under the same region where a cloud disk needs to be created. For more information, please refer to [Creating a Cloud Disk from a Snapshot](/doc/product/362/5757).

> - Currently, the snapshot function is available only in China's regions (except Guangzhou Zone 1)


## Snapshot Functions

1) Copy online data in real time
Snapshots are fully usable copies of cloud disks, which can be used to recover the disk quickly when a problem occurs. Before making any major change to a cloud disk, you can take snapshots of the disk, which can be used for rollback in case of failure in the change.

2) Back up critical milestones persistently
Snapshots can be used as persistent backups of business data, which can keep the milestone status of the business data.

3) Create a new cloud disk quickly
When disk A creates a snapshot file, users can use it to quickly clone multiple disks, thus achieving a fast server deployment.

## Application Scenarios of Snapshots

As a convenient and efficient way of data protection, snapshots are recommended for the following business scenarios:

- **Daily data backup**: Daily backup of system disks and data disks. You can use snapshots to regularly back up important business data to cope with the risk of data loss caused by misoperation, attack or virus.
- **Quick data recovery**: You can create one or more data snapshots before major operations such as replacing operating systems, upgrading application software or migrating business data. In this way, once any problem occurs during the upgrade or migration, you can timely recover the business data to normal system data through the data snapshots.
- **Multiple copies of production data**: You can provide real and near real-time production data for applications such as data digging, report query, and development and testing by creating snapshots of production data.

## What Do Snapshots Cost?

At the initial stage, Tencent Cloud provides a charging policy of limited free trails, that is, the snapshots are free of charge but with limited number.

1) Number of trial snapshots = Number of disks × 7
Here, the number of disks refers to the total number of cloud disks among users' data disks and system disks.

2) Snapshot creation policy
When the current number of snapshots is less than the current number of disks × 7, you can create snapshots.

3) Snapshot retention policy
For example, a user has 5 cloud disks, so he/she can and already has created 35 snapshots. If one of the cloud disks is terminated, the maximum number of snapshots that can be created becomes 28, but all the 35 snapshots need to be retained. At this time, the system will not delete the user's snapshots automatically unless the user does it by him/herself.
