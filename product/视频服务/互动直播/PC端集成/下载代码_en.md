## Overview
ILVB SDK for Windows (hereafter referred to as ILiveSDK (Windows)) is an ILVB SDK on Windows platform. Features such as ILVB, joint broadcasting and basic IM can be achieved just through several simple API calls.

## Download SDK and Demo
Clone the project from [github](https://github.com/zhaoyang21cn/iLiveSDK_PC_Demos). In addition to ILiveSDK (IE), API document, js API file and API call examples as shown below are also included:


| File | Description | 
|----|------|
| /suixinbo | demo FreeShow project source code, which can be linked with FreeShow on other platforms | 
| /iLiveSDK | SDK header and library files | 
| /doc | API-related and other documentation | 
| suixinbo_run | demo program that can be directly run | 


## Run and Try out demo
FreeShow is a live show App based on ILVB SDK of Tencent Cloud. It demonstrates the implementations of business scenarios such as VJ's LVB, interactive joint broadcasting with viewers, messaging and gift for giving likes.
### Run the demo program
suixinbo_run.zip is a compiled executable package. After decompression, double-click suixinbo_Qt.exe to run it.

### Registration and login
Before using other features, you need to log in or register the program by clicking the button at the top right corner.

### Watch LVB
Select the **LVB List** tab, and then refresh the LVB list to see the LVBs in progress. Click one of the LVBs to watch.
![LVB List](https://mc.qcloudimg.com/static/img/170ae5e7bbaf52943c975a8ad79b2fdd/2.png)

### Create an LVB
Select **I want to broadcast** tab and click the button to start the LVB
![VJ Starts Broadcasting](https://mc.qcloudimg.com/static/img/b6522dc3bad8e79c5709a104781e16c0/suixinbo_kaibo.png)

### Live room operations
VJ and viewers can perform device management, push/recording, messaging and joint broadcasting interactions in the live room.
![Live Room](https://mc.qcloudimg.com/static/img/aa77c098fe7f2a2885fd817cd2643987/avroom.png)

## Run the Demo Project
### Install Qt environment
You can directly install Qt on the VS later than VS2010 by selecting **Tools** -> **Extension and Update**.

![Step 1 for Installing Qt](https://mc.qcloudimg.com/static/img/e669d4451aca22173f8bf2ad67a894ab/pic.png)

Online -> Search **qt** -> Click **Download**

![Step 2 for Installing Qt](https://mc.qcloudimg.com/static/img/da49e7fd3f853bfed5814369811188ed/pic.png)

Then restart VS. The following Qt menu items appears in the menu.

![Step 3 for Installing Qt](https://mc.qcloudimg.com/static/img/cb5b67ec89f573185a5ce7fbbd85ac9a/pic.png)

Then, you need to configure the Qt directory in VS by selecting **Qt VS Tools** -> **Qt Options** -> **Add** and then selecting Qt installation directory, as shown below.

![Step 4 for Installing Qt](https://mc.qcloudimg.com/static/img/a6bfa24ca0c3ef8d39a289a4a120f4c0/pic.png)

Click **OK** after addition, as shown below,

![Step 5 for Installing Qt](https://mc.qcloudimg.com/static/img/c5aacc84343bb566097960e1dd595339/pic.png)

Note: If Qt plug-in cannot be found in VS2010, you need to download Qt plug-in from Qt official website, or [directly download Qt5.0.0 and VS2010 Plug-in](http://dldir1.qq.com/hudongzhibo/git/Qt/Qt_5.0.0.zip), and then manually install them (install Qt first, then the Qt plug-in)

### Compile FreeShow project
Open suixinbo.sln under directory suixinbo\sample in VS; for versions later than VS2010, when you are prompted to upgrade the project configurations, click **OK**. Next, right-click project suixinbo_Qt, select **Qt Project Settings**, and then configure Qt version of the project, as shown below.

![](https://mc.qcloudimg.com/static/img/1580d6b0287ea3ac8a88d81ee4d917c1/pic.png)
Now you can compile and run FreeShow.

## Integrate iLive SDK into Your Project
- iLive SDK is located in the iLiveSDK folder you downloaded in step 1. Copy the entire iLiveSDK folder to the directory where the solution file (.sln file) is located.
- Add the include directory:<br/>
	Add the include directory to the project's additional include directory, $(SolutionDir)iLiveSDK\include, as shown below.<br/>
![](http://mc.qcloudimg.com/static/img/3ab82b780f87b8749813f028a904ea0e/image.png)
- Add library directory:<br/>
	Add the directory containing the lib file to the project's additional library directory, $(SolutionDir)iLiveSDK\libs\$ (Configuration), as shown below.<br/>
![](http://mc.qcloudimg.com/static/img/0fbd938dbbf189c40e195cb60689baf4/image.png)
- Include header files:<br/>
	Include the header files (usually in the precompiled header) in the project and use the relevant namespace to load the lib file of the dynamic library. The code is as follows.

```C++
	#include "ilive.h"
	#pragma comment(lib, "ilivesdk.lib")
	using namespace ilive;
```

- Copy the dll file to the directory containing exe:<br/>
	Copy all the dll files under the libs\Debug directory to the running directory of Debug version, and copy all the dll files under the libs\Release directory to the running directory of Debug version;

- Verify whether the configuration is successful:<br/>
	Call GetILive() -> getVersion(). Then current version number of iLiveSDK is returned.
  
	
	

