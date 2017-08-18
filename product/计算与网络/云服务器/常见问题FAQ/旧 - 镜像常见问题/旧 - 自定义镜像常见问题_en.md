### 1. What if a Windows system custom image fails to be created?
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