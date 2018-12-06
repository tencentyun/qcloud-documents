To use Tencent Cloud Monitor to view the **CVM** metric data and generate alarms, you need to properly install the monitoring components on the Tencent Cloud CVM, which will be used to collect the metric data of CVM.

Note: In order to normally report the metric data, you need to open port tcp dport 80 of CVM to Internet. 

## Installing on Linux
After [logging in to Linux instance](/doc/product/213/5436), you can execute the following command to install required components, as shown below:
```
wget http://update2.agent.tencentyun.com/update/linux_stargate_installer
chmod +x linux_stargate_installer
./linux_stargate_installer
```

Once installed, you will see the following results:
![](//mccdn.qcloud.com/img568a75015695c.png)
![](//mccdn.qcloud.com/img568a750882880.png)
![](//mccdn.qcloud.com/img568a751592aea.png)

## Installing on Windows
1) After [logging in to Windows instance](/doc/product/213/5435), you can visit `http://update2.agent.tencentyun.com/update/windows-stargate-installer.exe` through the private network and download the installer `windows-stargate-installer.exe`.

2) Run the installer to install it automatically.

Once installed, you will see the following results:
![](//mccdn.qcloud.com/img568a758c4c308.png)
![](//mccdn.qcloud.com/img568a75948c917.png)
