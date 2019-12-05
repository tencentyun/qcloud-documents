The instance can be shut down when you need to stop the instance service or modify the configurations only for the instance that have been shut down. Shutting down an instance is like shutting down a local computer.

## Overview
 - **Preparation for shutdown:** The instance will no longer function to provide services after shutdown. Make sure the CVM has stopped receiving service requests before shutdown.
 - **How to shut down a instance:** You can shut down instances by using system commands (such as the shutdown command under Windows system and Linux system) or on the Tencent Cloud console. It is recommended to view the shutdown process on the console to check whether any problem occurs.
 - **Shutdown process:** The instance will be shut down. The status of the instance will first change to "shutting down" and then "off" after it has been shut down. Overlong shutdown may cause problems. For more information, please see [shutdown-related information](/doc/product/213/2917) to avoid forced shutdown.
 - **Data storage:** All the storage of the instance will remain connected to the instance, and all disk data are saved. Data in memory will be lost.
 - **Physical attributes of instances:** Shutting down an instance does not change any of its physical attributes. The instance public IP and private IP remain unchanged, and [Elastic Public IP](/doc/product/213/5733) maintains a binding relationship, but accessing these IP will get you an error response (for stopped services); if the instance is part of the [Classiclink](/doc/product/215/5002), this interconnection will remain unchanged.
 - **Load balancer:** If the shutdown instance belongs to [Real Server Cluster of Load Balancer Instances](/doc/product/214/6095), it will no longer function to provide services after shutdown. If the load balancer instance is configured with the health check policy, such shutdown instance will be automatically blocked from the request; but if not, the client may receive a 502 error code. For more information, please see [Health Check](/doc/product/214/3394).
 - **Auto scaling:** If the shutdown instance is in an [auto scaling group](/doc/product/377/3590), the Auto Scaling service will mark shutdown instance as poor performance, move the same out of the auto scaling group and launch a replacement instance. For more information, please see [Auto Scaling Product Documentation](/doc/product/377).

## Shutdown Instance via the Console
 1. Log in to the [CVM Console](https://console.cloud.tencent.com/cvm/).
 2. Shut down an instance: Select the instance to be shut down, and click **Shutdown** at the top of the list or click **More** -> **CVM Status** -> **Shutdown** in the Operation column on the right side.
 3. Restart an instance: Select all the instance to be shut down, and click **Shutdown** at the top of the list. Instances can be shut down in batches. Reasons are given for instances that cannot be shut down.

## Shutdown instance via API
For more information, please see the [API StopInstances](/doc/product/213/9383).

## Modify a Instance that Has Been Shut Down
You cannot modify the following instance attributes until the instance has been shut down.
- **Instance configuration (CPU and memory):** To change the instance type, please see [Adjust the Instance Configuration](/doc/product/213/5730).
- **Size of a mounted cloud disk:** To adjust the size of a cloud disk, please see [Expanding Capacity of Cloud Disks](/doc/product/362/5747).
- **Change password:** Please see [Login Password](/doc/product/213/6093).
- **Load key:** Please see [SSH Key](/doc/product/213/6092).

