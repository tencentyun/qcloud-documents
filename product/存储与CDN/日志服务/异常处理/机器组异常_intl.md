## Problem Description
An exception occurred with log collection, and the associated server group is found to be exceptional.

## Possible Cause
The heartbeat between the server group and CLS system is interrupted, resulting in a failure to collect and report logs. Possible causes of the server group exception include:
1. IP address is incorrect.
2. Network is disconnected.
3. LogListener fails.
4. Configuration of LogListener is incorrect.

## Solution
Troubleshoot problems according to the above causes.

## Procedure
1. Check whether the IP address added to the server group is correct.

2. Confirm whether the network is connected using the following command:
```
telnet <region>.cls.myqcloud.com 80
```
"region" is the abbreviation for the region where CLS resides. All region abbreviations allowed for CLS include ap-shanghai, ap-beijing, ap-chengdu, ap-guangzhou.
In case of normal network connection, the following code is shown. Otherwise, connection failure will be shown. Check the network to ensure normal connection.
![](https://main.qcloudimg.com/raw/7eb7367a22c300bb22e4cd3635adc311.png)

3. Check whether LogListener processes are running normally using the following command:
```
cd loglistener/tools; ./p.sh
```
Generally, there are three processes:
```
bin/loglistenerm -d                                #Daemon
bin/loglistener --conf=etc/loglistener.conf        #Main process    
bin/loglisteneru -u --conf=etc/loglistener.conf    #Update process
```
**If any process fails**, restart LogListener using the following start command:
```
cd loglistener/tools; ./start.sh
```

4. Check whether the configuration of the key and IP identifiers in LogListener is correct. Configuration file path: `/loglistener/etc/loglistener.conf`.
![](https://main.qcloudimg.com/raw/2deabe7e486a5e75002230ab62518f4b.png)
 - The key is the API key for the Tencent Cloud account or the collaborator. The project key is not supported.
 - group_ip in the configuration file must be consistent with the IP entered in the server group on the console. Since LogListener obtains the server IP automatically, check the consistency regularly when the server is bound with multiple ENIs.

