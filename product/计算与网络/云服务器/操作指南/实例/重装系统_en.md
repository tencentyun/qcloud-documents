System reinstallation enables instances to recover to a newly started status. It is a recovery method when CVM instances are suffering software failures. CVM instances support reinstallation of different types of systems. Whether you choose to change to a Linux series system or a Windows series system, Tencent Cloud will offer various-sized system disks to you.

It should be noted that reinstalling the system will result in loss of all contents of ***system disks***. Data in data disks will not be affected, but need to be re-recognized. Therefore, in case that system operation data need to be retained, it is strongly recommended that you [Create Custom Image] (/doc/product/213/4942) before reinstalling the system and decide whether to use the image for reinstallation.

## Sizes of system disks of different operating systems
- If the newly purchased Linux CVM comes with a cloud block storage, it can support a system disk of 20GB - 50GB.
- If the newly purchased Linux CVM comes with a local disk, it can support a system disk of 20GB.
- A newly purchased Windows CVM with any type of hard disk supports a system disk of 50GB.

## Charges for system disks
- For Linux instance system disks, the first 20GB of Tencent Cloud is free of charge. If the system disk supports capacity adjustment (i.e. if it is a Cloud Block Storage), the part beyond 20GB will be charged as per the charging standard of Cloud Block S
- For Windows instance system disks, the first 50GB of Tencent Cloud is free of charge. Since Windows instances do not support system disk capacity adjustment, no fees will be charged for system disks of Windows instances.

## Use console to reinstall system
1) Open [CVM Console] (https://console.cloud.tencent.com/cvm/).

2) For CVM instances that requires system reinstallation, click "More" - "Reinstall System" on the action bar to the right side.

3) In the pop-up box of system reinstallation, select the image used by the current machine or other images.

4) If other operating systems are needed, choose from the images provided by Tencent Cloud. Click "Reinstall System".

>Note:
>
- Do not perform other operations during system disk reinstallation.
- The data in current system disks cannot be recovered after system disk reinstallation.
- The data in data disks will be retained and will not be affected after system disk reinstallation, which however need to be mounted manually before use. See [File System Creation, Partitioning and Formatting](https://cloud.tencent.com/doc/product/362/5448)
## Questions about the switching between Windows system instances and Linux system instances

### Can the system disk of an old user's Linux CVM that comes with a local disk be scaled out to 20GB? 
For a Linux CVM that comes with a local disk of 8GB, the system disk can be scaled out to 20GB by reinstalling the system.

### A user has purchased a Linux CVM that comes with an over-20GB Cloud Block Storage. How the charges are calculated if the user reinstalls the operating system and changes it to Windows? 
If a user purchases a Linux CVM that comes with an over-20GB Cloud Block Storage, and then changes the operating system to Windows, the charges will be calculated based on the billing mode:
- If the CVM is based on an annual or monthly plan, a refund will be made (exclusive of the amount of voucher used in payment) or the price will be lowered according to the payment conditions.
- If the CVM is based on charge-by-quantity, the calculation of configuration charge for the part exceeding 20GB of the system disk will be stopped (i.e. the system disk will be free of charge afterwards) after the operating system is changed to Windows;

### A user has purchased a Windows CVM that comes with a Cloud Block Storage. How the charges are calculated if the user reinstalls the operating system and changes it to Linux?
Since the current system disk does not support capacity reduction, when a 50GB Windows Cloud Block Storage is changed to Linux, the capacity shall be kept and corresponding fees for the Cloud Block Storage shall be paid. (The first 20GB is free of charge, and fees for another 30GB shall be paid). See [Hard Disk Prices](http://cloud.tencent.com/doc/product/213/%E7%A1%AC%E7%9B%98%E4%BB%B7%E6%A0%BC) for details