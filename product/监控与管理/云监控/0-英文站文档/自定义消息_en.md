Custom Messages offers a command line delivery tool (cagent_tools). Developers can call the corresponding command to set the content of a customized message and deliver the content when an alarm is triggered.

- Currently, custom messages can only be reported using a command line tool. Related API will be provided in the future to make it easier for users to report custom messages in codes.
- cagent_tools is applicable to CVMs created with system images in Tencent Cloud.

## Configuring Custom Messages in Linux Systems
1) Install Linux monitoring components. For the installation method, please see [Install Monitoring Components](/doc/product/248/6211).

2) View the tool helper

Execute the following commands directly and view the help information:

```
cagent_tools
```
The result is as follows:
![](//mccdn.qcloud.com/img56cacd38f3fb9.png)

3) Example

Execute the following command line:

```
cagent_tools alarm "Alarm content"
```

PHP Example:

```
$link = mysql_connect('192.168.0.2', 'mysql_user', 'mysql_password');
if (!$link) {
 //alarm content
  $alarmContent = " Connection failed ";
  $cmd = "cagent_tools alarm $alarmContent"; 
  system($cmd);
  die('Could not connect: ' . mysql_error());
}
```
Shell Example:

```
#!/bin/sh
PATH=/usr/local/sbin:/usr/sbin:/sbin:/usr/local/bin:/usr/bin:/bin:$PATH
CAGENT_CMD = /usr/bin/cagent_tools
cnt=$(ps -ef | grep mysqld | grep -v grep | wc -l)
if [ $cnt -eq 0 ] ; then
    # alarm content 
    cagent_tools alarm "the process mysqld died."
fi
```

If circumstances such as hit-bottom traffic, decreased online users, and abnormal income are found during the analysis of collected data, developers can also send alarms by calling cagent_tools.

5) Configuration completed

When cagent_tools has been successfully called, Tencent Cloud Monitor will automatically send custom messages to related alarm recipient if the monitored object becomes abnormal. You can log in to Tencent Cloud Console, and go to "Cloud Monitoring" - "My Alarms" - "Custom Messages" to view historical alarm data.

> Note:
>
- Currently, only UTF-8 encoding is supported for Chinese alarm content.
- The maximum length of an alarm message is 256 bytes, and the excess part will be truncated.
- If an alarm message is sent successfully, "send alarm OK!" will be displayed in the command line, and the error code for process execution is 0. If an alarm message is not sent successfully, the relevant error will be indicated in the command line and the error code for process execution is not 0.

## Configuring Custom Messages in Windows Systems
1) Install Windows monitoring components. For the installation method, please see [Install Monitoring Components](/doc/product/248/6211).

2) View the tool helper

Execute the following commands directly on the command line interface and view the help information:

```
cagent_tools
```
The results are:
![](//mccdn.qcloud.com/img56cacf193430e.png)

3) Example

Execute the following commands:

```
cagent_tools alarm "Alarm content"
```

DOS Example:

```
@echo off
set service_name=StargateSvc
sc query %service_name% > nul
if not %errorlevel% == 0 (
    cagent_tools alarm "service %service_name% didn't exist"
)
```

If circumstances such as hit-bottom traffic, decreased online users, and abnormal income are found during the analysis of collected data, developers can also send alarms by calling cagent_tools.

5) Configuration completed
When cagent_tools has been successfully called, Tencent Cloud Monitor will automatically send custom messages to related alarm recipient if the monitored object becomes abnormal. You can log in to Tencent Cloud Console, and go to "Cloud Monitoring" - "My Alarms" - "Custom Messages" to view alarm data history.

> Note:
>
- Currently, both UTF-8 and GBK encoding forms are supported for Chinese alarm content.
- The maximum length of an alarm message is 256 bytes, and the excess part will be truncated.
- If an alarm message is sent successfully, "send alarm OK!" will be displayed in the command line, and the error code for process execution is 0. If an alarm message is not sent successfully, the relevant error will be indicated in the command line and the error code for process execution is not 0.