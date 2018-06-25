Reboot is a necessary method to maintain CVM. Rebooting CVM instances is equivalent to restarting operating systems of local computers. It is recommended that users reboot instances using the reboot operation provided by Tencent Cloud rather than running reboot command in instances (such as restart command in Windows and Reboot command in Linux). Generally speaking, it takes only a few minutes to reboot your instances after the reboot operation is performed, but instances are unable to provide services during rebooting. Therefore, please make sure the CVM has stopped receiving service requests before rebooting.

Since the physical characteristics of instances are not changed after the reboot, the Public IP address and Private IP address of, and any data stored in the instances will not be altered.

Rebooting instances will not start a new billing period. The length of time for use of postpaid instance will be kept, which will not affect its price range.


## Use console to reboot instances

1) Open [CVM console](https://console.cloud.tencent.com/cvm/).

2) To reboot a CVM instance running solely, click "Reboot" on the action bar to the right side.

3) To reboot CVM instances running in batch, check all the CVMs to be rebooted, and click "More" - "Reboot" on the top of the list. Reasons will be given for CVMs that cannot be rebooted.

## Use API to reboot instances
Please refer to [RestartInstances API](https://cloud.tencent.com/doc/api/229/1247).