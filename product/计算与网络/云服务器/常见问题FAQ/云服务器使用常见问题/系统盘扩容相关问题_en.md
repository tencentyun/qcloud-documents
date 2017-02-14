##   FAQs on scale-out of Linux CVM system disks
### 1. Can I adjust the capacity of the system disk when reinstalling the system for Linux CVM?
By reinstalling the system for a Linux CVM that comes with a Cloud Block Storage, you can scale out (Min. 20GB by default) but cannot scale in the system disk.
By reinstalling the system for a Linux CVM that comes with a local disk, the system disk can only be scaled out to 20GB.

### 2. Which types of disks are supported for scale-out of Linux system disk? 
By default, you can scale out a Linux system disk to a minimum of 20GB by reinstalling the system:
- a maximum of 50GB for a Cloud Block Storage
- a non-adjustable capacity of 20GB for a local disk
- Windows system disk comes with a non-adjustable capacity of 50GB by default



| System Disk Type | Cloud Block Storage | Local Disk|
| --------- | --------- | --------- |
| Fee-free Capacity | Linux: 20~50GB <br>Windows: 50GB | Linux: 20GB <br>Windows: 50GB |
| Fee-free Capacity | Linux: 20GB <br>Windows: 50GB | Linux: 20GB <br>Windows: 50GB |


### 3. Which regions and availability zones are supported when the system disks are reinstalled for scale-out?
There is no geographical limitation on this capacity upgrade. All regions are supported.


### 4. Can the system disk of an old user's Linux CVM that comes with a local disk be scaled out to 20GB? 
For a Linux CVM that comes with a local disk of 8GB, the system disk can be scaled out to 20GB by reinstalling the system.


### 5. Can the system disk of an old user's CVM that comes with a Cloud Block Storage be scaled out to a capacity larger than 20GB? 
If an old user's CVM comes with a Cloud Block Storage, the system disk can be scaled out by reinstalling the Linux system, with the fee being calculated by the corresponding unit price of hard disk.  See [Hard Disk Prices](http://www.qcloud.com/doc/product/213/%E7%A1%AC%E7%9B%98%E4%BB%B7%E6%A0%BC) for details.


### 6. A user has purchased a Linux CVM that comes with an over-20GB Cloud Block Storage. How the charges are calculated if the user reinstalls the operating system and changes it to Windows? 
If a user purchases a Linux CVM that comes with an over-20GB Cloud Block Storage, and then changes the operating system to Windows, the charges will be calculated based on the billing mode:
- If the CVM is based on an annual or monthly plan, a refund will be made (exclusive of the amount of voucher used in payment) or the price will be lowered according to the payment conditions.
- If the CVM is based on charge-by-quantity, the calculation of configuration charge for the part exceeding 20GB of the system disk will be stopped (i.e. the system disk will be free of charge afterwards) after the operating system is changed to Windows;

### 7. A user has purchased a Windows CVM that comes with a Cloud Block Storage. How the charges are calculated if the user reinstalls the operating system and changes it to Linux?
Since the current system disk does not support capacity reduction, when a 50GB Windows Cloud Block Storage is changed to Linux, the capacity shall be kept and corresponding fees for the Cloud Block Storage shall be paid. (The first 20GB is free of charge, and fees for another 30GB shall be paid). See [Hard Disk Prices](http://www.qcloud.com/doc/product/213/%E7%A1%AC%E7%9B%98%E4%BB%B7%E6%A0%BC) for details.

### 8. Can a system disk that has been scaled out be scaled in by reinstalling the system?
System disks cannot be scaled in.

### 9. Is there any way to save current data on the CVM and scale out the system disk?
You can create an image first, and then use the image to reinstall the system and thus scale out your system disk.

### 10. To what capacity can the system disk be adjusted if I use a 20GB-minus low-capacity image to create or reinstall the CVM?
It does not matter. The system disk can be scaled out to a minimum of 20GB regardless of the image capacity.

### 11. Can I use an image with a capacity larger than that of the specified system disk to create or reinstall the CVM?
The image you select must not have a larger capacity than the specified system disk.

