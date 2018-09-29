The lifecycle of Tencent Cloud CVM instance refers to all the statuses from the launch of the instance to its termination. Properly managing Tencent Cloud instances in different statuses (from launch to termination) can ensure that the applications running on the instances provide services in an efficient and economical way.

## Instance Statuses

- **An instance has the following statuses:**

| Status Name | Status Attributes | Description |
| ------ | ------ | ------ |
| Creating | Intermediate status | The instance is created, but is not running yet. |
| Running | Steady status | The instance is running normally. Instances in this status can be used to run your business. |
| Restarting | Intermediate status | A restart operation is performed for the instance via the console or APIs, but is not running yet. If this status lasts for a long time, there may be an exception. |
| Resetting | Intermediate | The instance's system is reinstalled or its disk is reset via the console or APIs, but the instance is not running yet. |
| Shutting down | Intermediate status | A shutdown operation is performed for the instance, but it is not completely shut down yet. If this status lasts for a long time, there may be an exception. Forced shutdown is not recommended. |
| Shut down | Steady status | The instance is shut down normally. Instances in this status cannot provide external services. Some attributes of instance can only be modified when the instance is in the shutdown status. |
| Terminating | Intermediate | The user actively performed the termination operation, but the termination has not yet completed.|
| Terminated | Steady status | The termination operation is completed. The original instance does not exist and cannot provide services. Its data is completely cleared. |

- **Instance Status Transition:**
![](https://main.qcloudimg.com/raw/1c018b2724bf142b1f3e90b97002d7a0.png)

## Instance Launching
 - After an instance is launched, it enters the creating status. The hardware specifications are configured according to the specified [Instance Specifications](/document/product/213/7153) for the instance in the creating status, and the system launches the instance using the image specified on launch.
 - The instance enters the running status after it is created. An instance in the running status can be connected and accessed normally.

For more information on instance launching, please see [Purchase and Launch an Instance](/doc/product/213/4855), [Log in to Windows Instance](/doc/product/213/5435), and [Log in to Linux Instance](/doc/product/213/5436).

## Instance Restarting
You are recommended to restart an instance via Tencent Cloud Console or Tencent Cloud APIs, instead of running the OS restart command in the instance.
 - After restarting, it enters restarting status.
 - Restarting an instance is like restarting the computer. After restarting, the instance maintains its public IP address, private IP address and all data on the disk.
 - Normally, it takes dozens of seconds or even several minutes to restart the instance, depending on the instance configuration.

For more information on instance restarting, please see [Restart Instance](/doc/product/213/4928).

## Instance Shutdown
You can shut down the instance via the console or APIs.
 - Shutting down an instance is like shutting down the computer.
 - An shutdown instance no longer provides external services, but the billing is not stopped.
 - The shutdown instance will still be displayed in the console.
 - Shutdown is required for some configuration operations, such as adjusting hardware configurations and resetting passwords.
 - Shutdown operation does not change the CVM's public IP, private IP, or any data on its disk.
 
For more information on instance shutdown, please see [Instance Shutdown](/doc/product/213/4929).

## Instance Termination
You can terminate an CVM instance if you no longer need it. You can terminate an instance through Tencent Cloud Console or Tencent Cloud APIs.

- Manual termination: you can actively terminate postpaid instances and prepaid instances in the recycle bin through the console.
- Auto termination: postpaid instances cannot be automatically terminated.

When terminating an instance, the system disks and data disks designated when purchasing will be terminated. But elastic cloud disks mounted on it will not be affected.
For more information on instance termination, please see [Terminate Instance](/doc/product/213/4930).
