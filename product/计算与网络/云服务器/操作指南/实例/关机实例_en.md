Shutdown instance is equivalent to the shutdown operation of local computers (such as shutdown command in Windows system and Linux system). The following instance attributes are modifiable only if the instance is in the shutdown state:
- Instance configuration (CPU, MEM)
- The size of Cloud Block Storage mounted on the instance
- Reset Password
- Load Key

When you shut down a CVM instance,

- the instance will be shut down with all services stopped. The state of instance will first change to shutting-down and then shutdown completed after it has been shut down.
- all the storage of the instance will remain connected to the instance, and all data are saved.
- data in memory will be lost while the instance is being shut down.
- all the services associated with the instance as well as their associated relationships are maintained, including [public IP](/doc/product/213/5224), [private IP](/doc/product/213/5225), [EIP](/doc/product/213/5733) and [Classiclink](/doc/product/215/5002).
- If the instance belongs to a [Backend Server Cluster of a CLB Instance](https://cloud.tencent.com/doc/product/214/1155), it will stop providing services. If a health check policy is configure for this CLB instance, this CVM instance will be blocked. If no health check policy is configured, the client may receive 502 error. For more information, please see [Health Check](https://cloud.tencent.com/doc/product/214/3394).
- If the instance is in [Auto Scaling Group](https://cloud.tencent.com/doc/product/377/3590), the Auto Scaling service will mark shutdown instance as poor performance, move the same out of Auto Scaling group and launch replacement instance. For more information, please see [auto scaling documentation](https://cloud.tencent.com/doc/product/377).
## Shutting Down Instances on Console
1) Log in to [CVM Console](https://console.cloud.tencent.com/cvm/).

2) To shut down one running CVM instance, click "Shutdown" on the action bar to the right side.

3) To shut down multiple running CVM instances, check all the CVMs to be shut down, and click **More** - **Shutdown** on the top of the list. Reasons will be given for CVMs that cannot be shut down.

## Shutting Down Instances via API
Please refer to [StopInstances API](https://cloud.tencent.com/doc/api/229/1250).

## Follow-up actions

To change the instance type, see [Adjust the Instance Configuration](/doc/product/213/5730).

To adjust the size of Cloud Block Storage, see [Expand the Cloud Block Storage](https://cloud.tencent.com/doc/product/362/2928).

To reset password, see [Login Password](/doc/product/213/6093).

To load keys, see [SSH Key](/doc/product/213/6092).
