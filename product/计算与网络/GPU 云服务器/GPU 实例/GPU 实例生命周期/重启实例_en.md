Restart is indispensable to the maintenance of GCC instances. Restarting a GCC instance is equivalent to restarting the operating system of a local PC. It is recommended to restart an instance using the restart operation provided by Tencent Cloud, instead of running restart command in instance (such as restart command under Windows and Reboot command under Linux). Generally, it takes only a few minutes to restart an instance after the restart operation is performed, but the instance cannot provide service during restart. Please make sure the server has stopped receiving service requests before restart.

Starting an instance does not change any of its physical attributes, so the public IP, private IP, and any data stored on the instance will remain unchanged.


## Restarting instance using console

1) Open [CVM Console](https://console.cloud.tencent.com/cvm/).

2) To restart a single running GCC instance, select and click **Restart** from the right menu. 

3) To restart multiple running GCC instances in batch, check all the GCC instances you want to restart, and then click **More -> Restart** on the top of the list. For the GCC instances which cannot be restarted, the reason will be displayed.

## Restarting instance using API
Please see [RestartInstances API](https://cloud.tencent.com/doc/api/229/1247).


