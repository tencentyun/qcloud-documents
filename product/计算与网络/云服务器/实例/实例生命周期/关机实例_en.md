Shutdown instance is equivalent to the shutdown operation of local computers (such as shutdown command in Windows system and Linux system). The following instance attributes are modifiable only if the instance is in the shutdown state:
- Instance configuration (CPU, memory)
- The size of Cloud Block Storage mounted on the instance
- Change Password
- Load Key

When shutting down a running instance,

- the instance will be shut down with all services stopped. The state of instance will first change to shutting-down and then shutdown completed after it has been shut down.
- all the storage of the instance will remain connected to the instance, and all data are saved.
- data in memory will be lost while the instance is being shut down.
- all the services associated with the instance as well as their associated relationships are maintained, for example: instance [Public IP](/doc/product/213/5224) and [Private IP](/doc/product/213/5225) remain unchanged, and [Elastic Public IP](/doc/produ- If the instance belongs to [Backend Server Cluster of Cloud Load Balance Instances](https://www.qcloud.com/doc/product/214/1155), it will no longer function to provide services after shutdown. If the Cloud Load Balance instance is configured with health- If the instance is in [Auto Scaling Group](https://www.qcloud.com/doc/product/377/3590), the Auto Scaling service will mark shutdown instance as poor performance, move the same out of Auto Scaling group and launch replacement instance. For more informat
## Shutdown instance via the console
1) Log in to [CVM Console](https://console.qcloud.com/cvm/).

2) To shut down a CVM instance running solely, click "Shutdown" on the action bar to the right side.

3) To shut down CVM instances running in batch, check all the CVMs to be shut down, and click "More" - "Shutdown" on the top of the list. Reasons will be given for CVMs that cannot be shut down.

## Shutdown instance via API
Please refer to [StopInstances API](https://www.qcloud.com/doc/api/229/1250).

## Follow-up actions

To change the instance type, see [Adjust the Instance Configuration](/doc/product/213/5730).

To adjust the size of Cloud Block Storage, see [Expand the Cloud Block Storage](https://www.qcloud.com/doc/product/362/2928).

To change password, see [Login Password](/doc/product/213/6093).

To load key, see [SSH Key](/doc/product/213/6092).
