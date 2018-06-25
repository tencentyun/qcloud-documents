This chapter shows how to configure Failure Self-recovery for disk utilization alarm, allowing you to get started with Failure Self-recovery quickly.

## 1. Create a Disk Cleanup Self-recovery Package
First, we create a processing package for disk utilization alarm.

> When you receive a disk alarm, perform the corresponding operation to clean up the disk.

**Access Procedure**:

Select "Access Self-recovery" -> "Package Management" -> "Create Self-recovery Package".

By following the instructions on disk cleanup (applicable to Linux) package page, enter the package name and the directory for disk cleanup, select the number of days within which the files to be deleted and the name of files to be deleted, and then save the self-recovery package.

![](https://mc.qcloudimg.com/static/img/f95944a0d3a46176369eb34879100491/14954426910835.jpg)


> When a disk utilization alarm is generated based on this package, find and delete the files ending with '.log' under '/data/log/' directory for the last three days.


Next, you need to enable the disk cleanup package you just created for disk utilization alarms.

## 2. Access Disk Cleanup Self-recovery Solution

In the previous step, you created a disk cleanup self-recovery package. Now, enable this package for disk utilization alarms.

Click "Access Self-recovery"
![](https://mc.qcloudimg.com/static/img/99ead78efe2ea131823a384cb6a208aa/14954963492141.jpg)

Enter the "Access Self-recovery" page, and configure as follows.
Note: Select the package (disk cleanup package for '/data/log/' directory) we created in the previous step as the self-recovery package.
![](https://mc.qcloudimg.com/static/img/4473b6efb53dd3818a04f755838ebe27/14955044310872.jpg)
![](https://mc.qcloudimg.com/static/img/c240551477d3eddd089937a634d12432/14955045422350.jpg)


In this case, Failure Self-recovery is enabled for disk cleanup alarms.
![](https://mc.qcloudimg.com/static/img/fd9a722c77ea5e9f27be4d8e58630c2b/14955041094397.jpg)


## 3. Integrate Alarm Source

By default, Failure Self-recovery integrates the following monitor products: Tencent Cloud Monitor, BlueKing Monitor, Zabbix, Nagios and OpenFalcon. Tencent Cloud Monitor and BlueKing Monitor can be directly configured with Failure Self-recovery packages. Zabbix, Nagios and OpenFalcon can also be quickly configured with Failure Self-recovery by following access instructions.

![](https://mc.qcloudimg.com/static/img/9e4b6233e148aa9f0754c2163793327e/14949448553132.jpg)

### 3.1 Integrate Tencent Cloud Monitor
By default, Failure Self-recovery highly integrates Tencent Cloud Monitor and pulls alarms from it regularly.

When accessing Self-recovery, you can find the corresponding alarm type of Tencent Cloud Monitor.
![](https://mc.qcloudimg.com/static/img/d2610949950445f04fcbc0aec2476b04/14949454396797.jpg)

Note: You must set the alarm policy and associate with an alarm object in the Tencent cloud.
![](https://mc.qcloudimg.com/static/img/7b559153b37ba3f304aec1d9ce471995/14955047240702.jpg)

In this way, when a Tencent Cloud alarm is generated, you can find the corresponding alarm in the alarm list.
![](https://mc.qcloudimg.com/static/img/44a70ddb621b65b448d87a48a2f14b16/14955048096192.jpg)

### 3.2 Integrate Zabbix
![](https://mc.qcloudimg.com/static/img/cf578458d4c2ccab95759543b4ed5dbd/14955051484732.jpg)
![](https://mc.qcloudimg.com/static/img/43999b5b0b84cff574aa63bf2087f637/14955052137662.jpg)

### 3.3 Integrate Nagios
![](https://mc.qcloudimg.com/static/img/dbac93622b8f8a9d416e11a4ed05fc0b/14955056148118.jpg)

### 3.4 Integrate OpenFalcon
![](https://mc.qcloudimg.com/static/img/958c8200eb0adc45fbd7882dafc52158/14955054633512.jpg)

### 3.5 Integrate REST API
![](https://mc.qcloudimg.com/static/img/ac029af40ee061ae5089fb0088720fc2/14955055349670.jpg)

## 4. Alarm Notification Channels
Four channels are provided: WeChat, telephone, email and SMS.
![](https://mc.qcloudimg.com/static/img/352bb27bcc3c0404faaa319266274434/14955057653750.jpg)

![](https://mc.qcloudimg.com/static/img/d2781b798aca5bf9ecfab072382cdd20/14955061074598.jpg)

> For telephone channel, the maximum number of notifications per day is 24.







