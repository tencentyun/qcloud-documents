The life cycle of Tencent Cloud CVM instance refers to the period ranging from its launching state till its termination. Using Tencent Cloud CVM to manage the instance during its life cycle can help ensure that the applications on CVM render services in an efficient and cost-effective manner.

The following shows the conversion between different instance states. For more information about instances with an annual or monthly plan as well as instances charged by quantity, see [Billing Model Instruction](/doc/product/213/2180).

! [](//Mc.qcloudimg.com/static/img/551771757a0419084585ccbfad776d86/image.png)

CVM instance has the following states:
- Creating 
- Running 
- Rebooting
- Shutting-down 
- Shutdown completed 
- Resetting
- Terminating 
- Terminated 
- (Optional) Recycled


## Instance starting
After starting, the instance will go into pending state. The [Instance Types](/document/product/213/7153) specified when starting will determine the hardware configuration of the instance. The system will use image specified when starting to launch the instance. It will be connected to the instance after a short period of time. When the instance is ready, it will enter into running state.

The instance will obtain a private IP address. Other CVMs in the same regions and of the same network environment (VPC or basic network) are able to communicate with it; if you select an instance with public bandwidth/traffic, you will also get a public IP address that allows you to communicate with the instance from Internet. Users can connect to a running instance, and then use it like a normal computer.

For more information, see [Purchase and Start an Instance](/doc/product/213/4855), [Logging into Windows Instance](/doc/product/213/5435), and [Logging into Linux Instance](/doc/product/213/5436).

## Instance rebooting
We suggest that users can choose Tencent Cloud Console or Tencent Cloud API to reboot the instance, instead of running the rebooting command in the operating system. After rebooting, it will enter into rebooting state.

Instance rebooting is equivalent to the restarting of computers. After rebooting, the instance will maintain its public IP address, private IP address and all the data on the hard disk. Normally, it takes dozens of seconds or even several minutes to reboot the instance, depending on the instance configuration.

For more information, see [Reboot Instance](/doc/product/213/4928).

## Instance shutdown

Users can perform shutdown operation on the instance to stop services if necessary. You can choose Tencent Cloud Console or Tencent Cloud API to shut down an instance. 

After shutdown, the CVM instance will still be displayed in the console. <font color="red">The instance charged by quantity will continue its billing until the user terminates it whether it has been shut down or not. </font>After a certain period time following the expiration, instances with an annual or monthly plan will be shut down and moved to the Recycle Bin. It should be noted that users ***cannot*** connect to the instance that has been shut down.

Instance shutdown is equivalent to the shutdown of computers. Shutdown is the prerequisite for certain operations (for example, adjusting configuration, resetting password, etc.). The shutdown operation will not change public IP address, private IP address and all the data on the hard disk of CVM. But follow-up operations (adjusting hardware configuration) may change IP. Please refer to corresponding operation steps.

For more information, see [Shutdown Instance](/doc/product/213/4929).

## Instance termination
Users can terminate the instance if they no longer need CVM instances. Note:
- For prepaid instances, it will be moved into the Recycle Bin upon expiration, and be terminated automatically after 7 days.
- For postpaid instances, users can terminate them manually either through Tencent Cloud Console or Tencent Cloud API.

When terminating an instance, the system disks and data disks designated when purchasing will be terminated as well. But elastic cloud disks mounted on it will not be affected.

For more information, see [Terminate Instance](/doc/product/213/4930).