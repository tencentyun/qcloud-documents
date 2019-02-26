The lifecycle of CVM instance refers to the period ranging from launching to termination. 

The chart below shows the lifecycle of prepaid and postpaid CVM instances. For more information the different billing types, please see [here](/doc/product/213/2180).

![](//Mc.qcloudimg.com/static/img/551771757a0419084585ccbfad776d86/image.png)

Status of CVM instances including:
- Launching 
- Running 
- Restarting
- Shutting down 
- Shutdown 
- Reinstalling
- Terminating 
- Terminated 
- (Optional) Reclaimed


## Launching Instances
Once you launch a CVM, the instance status becomes **Launching**. The launch specifications are determined by the [instance type](/document/product/213/7153). The system will use the specified image to launch the instance. It may take a while for launching. When the instance is ready, its status becomes **Running**.

The instance will obtain a private IP address, with which other CVMs in the same regions and of the same network environment (VPC or basic network) are able to communicate with the instance. For instance with public bandwidth/traffic, a public IP address is assigned for accesses from Internet.

For more information, see [Purchase and Launch Instances](/doc/product/213/4855), [Log In to Windows Instance](/doc/product/213/5435), and [Log In to Linux Instance](/doc/product/213/5436).

## Restarting Instances
It's suggested to restart instance on Console or via API, instead of running the rebooting command in the operating system. 

Restarting an instance is similar to rebooting a computer. The public IP address, private IP address and all data on the disk are remained unchanged. It may take about several seconds to minutes to restart the instance, depending on the instance configuration.

For more information, see [Restarting Instances](/doc/product/213/4928).

## Shutting down Instances

You can shut down instance to stop services on Console or via API. 

Shutdown CVM instances are still visible on the console. For postpaid CVMs, the billing does not stop. It should be noted that users ***cannot*** connect to the instance that has been shut down.

You need to shut down the instance before certain operations, like adjusting configuration, resetting password, etc.. The public IP address, private IP address and all data on the disk are remained unchanged.

For more information, see [Shutting Down Instances](/doc/product/213/4929).

## Terminating Instances
You can terminate unnecessary instances if required.
Note:
- Prepaid instances will be moved into the Recycle Bin upon expiration, and be terminated automatically after 7 days.
- For postpaid instances, users can terminate them manually on the Console or via API.

When terminating an instance, the system disks and data disks designated when purchasing will be terminated as well. But elastic cloud disks mounted on it will not be affected.

For more information, see [Terminating Instances](/doc/product/213/4930).