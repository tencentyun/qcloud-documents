### How many LVB channels can be created at most under a test account?  
Currently, only 5 channels are allowed by default.
	
### What is push?  
Push refers to uploading local videos to the cloud for a non-interactive broadcasting, which can be played on the Web or other players.

### What is the default storage directory of OpenSDK logs?

#### Android

Under the sub-directory tencent/imsdklogs/com/tencent/avsdk of the built-in SD         

#### iOS

Under the sub-directory /Library/Caches of the installation directory of DEMO APP As shown below:

![iOSLog Directory](//mccdn.qcloud.com/static/img/0837b7ff0ec0d611b0f2c7ddaef0c0a2/image.png)

#### Windows

Current directory If DEMO executable is run directly, the executable is located under the current directory; if DEMO executable is compiled and run from VS2010, VS2010 DEMO project is located under the current directory, that is, OpenSDK\Demo\PC\src\.

#### Notes

For all open SDKs, IMSDK provides APIs for setting directories for storing logs. Audio/video SDKs just obtain the configured directories to store the logs, and IMSDK is responsible for reporting logs.

### Whether IPV6 is supported in iOS versions?
Supported in version 1.8.

### Doesn't SDK support x86 platform?
No, it doesn't.

### Which role is used for joining broadcasting - viewer or VJ?
To change your permission to join a broadcasting, you need to apply for the third account on the console and set it to ILVB mode, and then set the permission for joining the room to the default.

### Why central node is used even if the roles of viewers are correctly configured?
For any room with not more than five people, the central node is used regardless of the role configuration.

