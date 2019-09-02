> Note: This only applies to Windows Server 2008 R2 and Windows Server 2012. For any need to batch edit SID, you can create a custom image (select "Run Sysprep to Create an Image").

## 1. Background
Microsoft's operating system uses a security identifier (SID) to identify computers and users. When there is a need to build a Window domain environment, modification of SIDs is required to overcome the inability to join the domain due to the fact that CVM SIDs generated based on the same image are the same.

## 2. Operation Steps
1) [Log into the CVM using the console VNC](https://cloud.tencent.com/doc/product/213/2155)

2) Save the current network configuration

Click "Start" - "Run". Type cmd to open the command line. Run the command ipconfig / all. Keep record or save screenshots of the result information.

3) Open the Sysprep tool

Run the sysprep.exe program under the folder C: \ windows \ system32 \ sysprep.

As shown below, select "Enter System Out-of-Box Experience (OOBE)" under "System Cleanup Action", and meanwhile check the "General" option. Select "Restart" under "Shutdown Options".

![](//mccdn.qcloud.com/static/img/1dfa18a861c0a70b880b5130ff40d572/image.png)

4) Clicking on "OK" will restart the system. When the restart is done, complete the configuration steps following the wizard (select language, reset password, etc.)

5) Verify SID
Click "Start" - "Run". Type cmd to open a command line. Run the whoami / user command and refer to the figure below to verify if SID has been modified:

![](//mccdn.qcloud.com/static/img/6c1c0784b3e51b5dca3a19f381ea2e02/image.png)

6) Refer to the configuration saved in Step 2 to reset network card information (IP address, gateway address, DNS, etc.).


　　

