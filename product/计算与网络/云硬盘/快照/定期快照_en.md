## 1. Overview of Auto Snapshot

Tencent Cloud's CBS Snapshot has recently launched the **Auto Snapshot** function (under beta test, expected to be available in March 2017), which allows developers to set backup task policies flexibly. Common policies include:

- For non-core business data disks, you can set to make an automatic snapshot backup at 00:00 every Monday, and to delete the backup automatically after 1 month;
 
- For core business data disks, a snapshot backup can be made every 12 hours, and the backup will be deleted after 1 week.
  
## 2. Auto Snapshot Policy Instructions

**Object**: cloud disks - system disks/data disks

 **Execution policy**: Customers can set a snapshot creation time point for each cloud disk per week. The time point can be specific to week-hour (The snapshot creation task will be completed within 1 hour from the set creation time point according to the snapshot system's business volume). The execution policy is valid in long term after being saved. The execution policy can be modified, and will take effect immediately after a successful modification.

**Auto termination* (Important)***: Auto Snapshot provides an auto termination function. For instance, you can set to automatically delete a snapshot after 7 days (You can choose from 1 day to 10 days. Default is 7 days.) to reduce backup costs. The option is checked by default. If it is unchecked, the snapshot will be retained forever.

**Batch**: An auto snapshot policy should be set first. You can check multiple cloud disks, and implement the same policy on them in batch.
 
 **Script pause**: HDD cloud disks that are not in use will not execute the automatic snapshot policy. "Not in use" means the virtual machine associated with the system disk or data disk is shut down, or the data disk is not mounted.

 **Naming rule**: Automatic snapshots should be named in the format of snap_yyyyMMdd_HH. yyyyMMdd is the date of the day, and HH is the hour. For instance, snap_20140418_11 represents an automatic snapshot that is created at 11 o'clock on April 18, 2014. You can also modify the snapshot name by yourself.

**Life cycle* (Important)***: There are 2 kinds of snapshot life cycles. For snapshots created manually, their life cycle is **long-term retention** by default, as long as the account balance is sufficient. For auto snapshots, you can set a time point for **auto termination** according to the creation rules. This time point can be changed to **long-term retention** on the snapshot details page, which should be triggered manually.

**Snapshot conflicts**: Automatic snapshots do not conflict with custom snapshots. When an automatic snapshot is being taken on a disk, the user needs to wait for the automatic snapshot to be completed before he can create a custom snapshot (and vice versa). If a snapshot-taking duration is longer than the interval between two automatic snapshot time points due to large amount of data on the disk, the automatic snapshot will not be taken at the next time point. For example, a user sets 9:00, 10:00 and 11:00 as automatic snapshot time points. However, the snapshot-taking starting from 9:00 takes 70 minutes, which means it doesn't end until 10:10. In this case, the next automatic snapshot will not be taken at the preset time point of 10:00, and will start at 11:00.

 **Snapshot limit**: The limit of snapshots for each disk is 64. If the limit of snapshots on a disk has been reached, the automatic snapshot task will be suspended and blocked. The snapshot limit is set to prevent developers from forgetting an automatic snapshot policy, thus resulting in an endless increase in storage costs.
 
 **ASP**: ASP refers to Auto Snapshot Policy.

 **ASP limit**: Under a single account, a maximum of 10 ASP policies can be set in each region. Each ASP can associate with up to 50 hard disks.

**Snapshot creation frequency**: As only 10 ASPs are allowed to be set under a single account, an ASP can only specify one time point. A cloud disk is only allowed to associate with one ASP policy.

 **Region attribute**: The region attribute for snapshots is region. For example, the snapshot files in Guangzhou Zone can be used to create cloud disks for Guangzhou Zone 2 and Guangzhou Zone 3.

 **Retention period**: For automatic snapshots, the console displays the countdown for recycling.  For snapshots created manually, permanent retention is displayed. Automatic snapshots can be manually modified to permanent retention.

 
**ASP pause**: Auto Snapshot Policy (ASP) allows you to **pause** the function manually. After paused, snapshots will no longer be created automatically. But the life cycle of automatic snapshots will not be affected. The snapshot will be automatically removed upon expiration. For example, if an automatic snapshot has a life cycle of 7 days, it will still be removed upon expiration.

 
**Operation log**: The operation log shows the creation process of all automatic snapshots, the same as that for manually added snapshots.
 

## 3. Operation Instructions


### 3.1 Creating an Auto Snapshot Policy

You can create an auto snapshot policy in the snapshot console.

![](//mc.qcloudimg.com/static/img/da713a35fc8e204baec28a4a61f4e418/image.jpg)

![](//mc.qcloudimg.com/static/img/dffffb2a9248765fd1782bceb57e001b/image.jpg)


### 3.2 Associating with Cloud Disks

You can add cloud disks to an auto policy to achieve automatic snapshots.

![](//mc.qcloudimg.com/static/img/6aebd3dfb757ba73a2047d61fd56c2ed/image.jpg)


### 3.3 Converting an Autosnap to a Permanently Retained Snapshot

![](//mc.qcloudimg.com/static/img/6238e66c512784793558bc0e23692e3c/image.jpg)

![](//mc.qcloudimg.com/static/img/db861fd909ed450ac3a10dbfc507490a/image.jpg)


