This document describes how to terminate an instance. For more information on expiration, please see [Expiry Reminder](/doc/product/213/2181).

## Overview
 - **Manual termination:** Prepaid instances can be terminated by users before they expire. After terminated, these instances are retained in the recycle bin for 7 days, and can also be terminated completely in the recycle bin. Postpaid instances can be terminated manually.
 - **Automatic termination:** Prepaid instances that have not been restored after being retained in the recycle bin for 7 calendar days are automatically terminated. Postpaid instances are automatically terminated when your account balance has remained below 0 for 24 hours. You can continue to use them if you finish [Renewal](/doc/product/213/6143) within a specified period of time.
 - **Instance data:** Since mounted local disks and non-elastic cloud disks are terminated altogether, the data may be lost, so back them up beforehand. Elastic cloud disks are not affected.
 - **Billing:** Once an instance is being terminated or has been terminated, no expenses related to this instance are incurred.
 - **EIP:** EIPs (including IPs on the secondary ENI) of a terminated instance are kept, and idle IPs may incur expenses. If you do not need these IPs, release them in time.

## Terminating Prepaid Instance
### Terminating Unexpired Instance on the Console

A prepaid instance can be terminated if you no longer need it. Once an instance is being terminated or has been terminated, no expenses related to it are incurred. This instance is then moved to CVM recycle bin and kept for 7 days, and services running on this instance are completely suspended.

After a prepaid instance is returned, local disks and non-elastic cloud disks mounted to this instance are returned as well, and data stored on these disks will be lost. However, elastic cloud disks mounted to this instance are retained and the data are not affected.

1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/).
2. Terminate a single instance: Find the instance to be terminated in the list, and click "Terminate" button in Operation column.
3. Terminate instances in batches: Select all the instances to be terminated, and click "Terminate in Batches" on the top.
4. In the pop-up box, confirm descriptions related to the CVM to be terminated, and click "OK". Then, you are directed to "Check Refund Information" page.
5. Carefully check the refund information related to the instance. After "Confirm Refund" is submitted, refund is initiated and the instance is terminated.
For more information on rules for returning prepaid instances, please see [Refund Rules for Terminated Prepaid Instances](https://cloud.tencent.com/document/product/213/9711).

### Completely Terminate Prepaid Instances in Recycle Bin
You can terminate prepaid instances retained in the [Recycle Bin](/doc/product/213/4931) through the console.

 1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/).
 2. On the left navigation bar, click "Recycle Bin" -> "CVM Recycle Bin" to enter the CVM reclaiming list.
 3. Terminate a single instance: Find the instance to be terminated in the list, and click "Terminate" button in Operation column.
 4. Terminate instances in batches: Select all the instances to be terminated, and click "Terminate in Batches" on the top.
 5. In the pop-up box, enter the verification code, and click "OK" to complete the termination process.

## Terminating Postpaid Instance
After terminated, a postpaid instance is still visible in the console within a short period of time. It will be automatically removed from the instance list later, and its services will be completely suspended.
### Terminate Instances on the Console
 1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/).
 2. Terminate a single instance: Find the instance to be terminated in the list, and click "More" -> "CVM Status" -> "Terminate" on the right side.
 3. Terminate instances in batches: Select all the instances to be terminated. On the top of the list, click the "More" drop-down box, and then click "Terminate". Reasons are given for instances that cannot be terminated.

### Terminate Instances using API
For more information, please see [API TerminateInstances](/doc/product/213/9395).



