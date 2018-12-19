Snapshot is a way of data backup provided by Tencent Cloud, used to create a fully usable copy of a specified cloud disk to allow the backup to be independent of the life cycle of the cloud disk. Snapshots include the images of the cloud disk at the time when the copy starts. Snapshots do not occupy users' storage space, and Tencent Cloud stores the snapshots created by users redundantly in multiple available zones to further ensure the reliability of backups. Snapshots are incremental backups, which means only the data changed after the latest snapshot creation is stored. In this way, the time needed to create snapshots is minimized and storage cost is reduced.

You can create a new cloud disk from a snapshot. In this case, the cloud disk has all the data in the snapshot upon creation, and can be used as an accurate copy of the original cloud disk. Since snapshots are region-related, they can only be used under the same region where a cloud disk needs to be created. For more information, please see [Create Cloud Disk from Snapshot](/doc/product/362/5757).

>- Now, the snapshot feature is only available in Mainland China regions (except for Guangzhou Zone 1) and Hong Kong region. More regions will be available soon.


## How Does Snapshot Work?

1) Copy online data in real time
Snapshots are fully usable copies of cloud disks, which can be used to recover the disk quickly when a problem occurs. Before making any major change to a cloud disk, you can take a snapshot of the disk, which can be used for rollback in case of failure in the change.

2) Back up critical milestones persistently
Snapshots can be used as persistent backups of business data, which can keep the milestone status of the business data.

3) Create a new cloud disk quickly
When disk A creates a snapshot file, users can use it to quickly clone multiple disks, thus achieving a fast server deployment.

## Application Scenarios of Snapshots

As a convenient and efficient way of data protection, snapshots are recommended for the following business scenarios:

- **Daily data backup**: Daily backup of system disks and data disks. You can use snapshots to regularly back up important business data to cope with the risk of data loss caused by misoperation, attack or virus.
- **Quick data recovery**: You can create one or more data snapshots before performing major operations, such as changing operating systems, upgrading application software or migrating business data. In this way, when a problem occurs during the upgrade or migration, you can timely recover the business data to normal system data through the data snapshots.
- **Multiple copies of production data**: You can provide real and near real-time production data for applications such as data mining, report query, development and testing by creating snapshots of production data.

## Billing of Snapshots

At the initial stage, Tencent Cloud provides a charging policy of limited free trails, that is, the snapshots are free of charge but with limited number.

1) Number of trial snapshots = Number of disks × 7
The number of disks refers to the total number of cloud disks of the user, including data disks and system disks.

2) Snapshot creation policy
When your current number of snapshots is less than the current number of disks × 7, you can create snapshots.

3) Snapshot retention policy
For example, you have 5 cloud disks and create 35 snapshots. And then you terminate one of your cloud disks, your snapshot quota becomes 28 (4*7), but all the 35 snapshots created previously are retained. Tencent Cloud does not delete your snapshots automatically unless you do it yourself.


## Auto Snapshot Policy

- **Core business:** For core businesses which have extremely high requirement for RPO (Recovery Point Objective), you are recommended to back up snapshots once every few hours, and retain the backup data for a day.
- **Production business:** Back up snapshots once a week, and retain the snapshot data for a month.
- **Archive business:** Back up snapshots once a month, and retain the snapshot data for a year.

## Notes

Database business: Flush & Lock Table
File system: Sync

