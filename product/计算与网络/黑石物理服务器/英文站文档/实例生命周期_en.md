The life cycle means all the statuses of a CPM from the moment of purchase to the reclaim of the CPM. This section describes each status in details. The status change for an instance is shown below.

![](http://mc.qcloudimg.com/static/img/525da2318d54046daeea964890fa24f8/image.jpg)

The statuses are as follows:

- Purchase a CPM
- Deploy operating system
- Running
- Reinstall operating system
- Shutting-down
- Rebooting
- In arrears
- Isolated
- Reclaimed

## Purchasing a CPM
Please go to the purchase page of CPM and select a CPM that meets your requirements. For more information on instance types, please see *[Instance Type](/document/product/386/7035) section*. For more information on how to purchase a CPM, please see Quick Start *[Purchase a CPM](/document/product/386/7134) section*

## Deploying Operating System
For more information on how to select and install a specified operating system, please see Quick Start *[CPM Configuration](/document/product/386/7135) section*. This process includes the following stages:

- Initialize infrastructure environment: Operations such as powering on the racks, and exception handling
- Initialize private network environment: The ping uplink switch, operations such as determination of private network availability, and exception handling
- Initialize PXE environment: Operations such as determination of CPM out-of-band availability, and exception handling
- PXE CLIENT boot-up: Operations such as PXE CLIENT boot-up, and exception handling
- Installing the operating system: Operations such as OS pulling and installation, and exception handling
- Configuring the system or formatting the disk: Configurations such as disk formatting, Bonding check, Ping check, SSH login check, Yum/NTP, etc., and exception handling

## Running and Shutting-down
This CPM has been delivered to you for operation. You can shut down or reboot the CPM as required. However, both operations will cause the CPM unable to provide services. Please proceed with caution.

## Rebooting
If a failure occurs to the CPM, such as memory failure, the reboot of the CPM will fail. If so, please contact customer service.

## In Arrears and Isolated
The CPM will be in arrears if its available duration is less than 0 day, and will be forced to shut down and reclaimed after a certain period of time. For more information, please see *[Recycle Bin](/document/product/386/7146) section*



