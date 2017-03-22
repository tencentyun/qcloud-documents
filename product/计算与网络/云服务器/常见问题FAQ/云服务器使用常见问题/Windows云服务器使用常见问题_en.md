## What if the PING 127.0.0.1 command returns an error?
On a Windows system that has been running for a while, a ping command may fail and return an error message saying "Loopback address 127.0.0.1 doesn't exist" upon startup due to the system itself or third-party software. Try the methods below:

The figure below shows an example of the problem:
![](//mccdn.qcloud.com/static/img/ff82d382b0bdfa9c2163e80e1e90815d/image.png)

Tencent provides zipconfig_service for you to configure and fix IP address error. The above error can be fixed by downloading the upgrade package of this service.

How to: Download the toolkit zipconfig\_update1.0.0.6.zip, and run zipconfig\_update.bat after extraction.
Private network link: http://mirrors.tencentyun.com/install/windows/zipconfig_update1.0.0.6.zip

An example result upon execution:
![](//mccdn.qcloud.com/static/img/7ff1fc9dc1a9ff9201eea4237e6c6148/image.png)
Generally you do not need to restart the computer after execution.

## What if a Windows system custom image fails to be created?
If a Windows system image fails to be created, perform a check following the steps below.

1) Make sure that the following services are working properly
<table class="t">
<tbody><tr>
<th width="100"> <b>Program Name</b>
</th><th width="100"><b>Install Location</b>
</th><th width="100"><b>Service Name</b>
</th></tr>
<tr>
<td>QcloudService.exe
</td><td>C:\Windows\
</td><td>Tencent Cloud Service
</td></tr>
<tr>
<td>WinAgent.exe
</td><td>C:\WinAgent\
</td><td>WinAgent Display Name
</td></tr>
<tr>
<td>win-agent.exe
</td><td>C:\win-agent\
</td><td>win-agent
</td></tr></tbody></table>

Check and make sure the above services and all the services coming from the official source of Tencent Cloud and starting with Win_Agent are working properly.

2) The creation of a custom image relies on the Windows Modules Installer provided by Microsoft. Make sure this service is working properly.

3) Some anti-virus tools or safedog may block custom image creation scripts from executing. To avoid creation failure, it's recommended that you close these tools before creating a custom image.

4) If the above three steps do not resolve the problem, the reason may be that the some settings within the CVM that have caused the image creation tool to be interrupted by system pop-ups. Please remotely log onto the CVM, and then check and adjust the CVM settings to avoid pop-ups.