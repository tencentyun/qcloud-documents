Monitor Overview allows you to access the overall monitoring information of your cloud products, including the exceptions detected during the monitoring. They are:

## CVM Unreachable Ping 
The number of alarms with the policy type of "CVM", the alarm status of "Not Recovered" and the alarm type of "ping Unreachable" for nearly one month are displayed. You should pay close attention to these unrecovered CVM alarms, because they probably affect normal operation of your business.

## CVM Disk is Read-only
The number of alarms with the policy type of "CVM", the alarm status of "Not Recovered" and the alarm type of "Disk is Read-only" for the recent month are displayed. Such exception may affect the business that requires data writing in the CVM.

## CVM Failed to Be Monitored

Such exception may occur if you did not install [Agent](https://cloud.tencent.com/doc/product/248/2258) in your CVM. To find the reason, do the followings:

1. Check if barad_agent is installed

   If you don't install the agent in your CVM, we can't do a detailed monitoring for your CVM, and can't inform you in case of any failure, which is high risky. For more information on installing monitoring components, please see [Install Monitoring Components](https://cloud.tencent.com/document/product/248/6211).

2. If you have installed the agent on your CVM, check if the barad_agent log is rolled every minute in real time and reported successfully 

   > 1) Linux system log path: /usr/local/qcloud/monitor/barad/log/dispatcher.log
   >
   > ​    Each log contains "nws send succ" 

   > 2) Windows system log path: C:\Program Files\QCloud\Monitor\Barad\logs\info.log
   >
   > ​    Each log contains "nws send succ"

3. If the log is not rolled, there may be something wrong with agent scheduling (only in Linux system, probably due to change of system time)

   You can reboot barad_agent and check if the log /usr/local/qcloud/monitor/barad/log/executor.log is correct.

4. If the report failed (nws send fail), you should identify the problem (such as timeout, unable to connect to the CVM or unable to resolve domain name) based on logs 

   The report address can be seen in nws_url of plugin.ini file under etc directory.

5. If "nws send fail" does not appear when reporting

   1) Check whether uuid is modified

   uuid file path:

   > linux: /etc/uuid

   > windows: c:\windows\system32\drivers\etc\uuid
   >
   > ​                    c:\windows\system32\drivers\etc\the most recent file named in the format of uuid

   2) If the uuid file is not modified, check the timestamp of the sub-machine

    For Linux, you can use `/usr/sbin/ntpdate ntpupdate.tencentyun.com` to check whether the adjusted value of the time is less than 50 seconds. If the adjusted value is greater than 50 seconds, reboot barad_agent and the original time will be resumed.! [img](http://tapd.oa.com/tfl/captures/2016-05/tapd_10114711_base64_1464166851_22.png)

6. If the problem still exists after you complete the above procedures, use check_agent_profile script for Linux.

   In your CVM, execute the following command:

   `wget http://update2.agent.tencentyun.com/check_barad_agent && sh check_barad_agent`

   Submit the ticket that contains the output result, and we will fix your problem as quickly as possible.
