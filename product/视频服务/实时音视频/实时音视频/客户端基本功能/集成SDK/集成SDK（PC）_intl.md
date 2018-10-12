This document describes how to integrate the TRTC SDK to a PC.
## Downloading Source Code
You can download the complete demo code used in this document. 
[Download Demo Code](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/PC/demo_import.zip)
## Procedure
### Create a Win32 Console project
1. Open Visual Studio, click the **File** menu, and then select **New** -> **Project** -> **Create a Project**:
![](https://main.qcloudimg.com/raw/d372db4d91a96b59e51b5d4e8666c92d.png)

2. Create an empty project:
![](https://main.qcloudimg.com/raw/45f4a6a7e495cc4519e11504eb5f5103.png)

3. Add a cpp file to the project and write an empty main function:
![](https://main.qcloudimg.com/raw/b8d0335b0411d85630b14729235fc4fc.png)

### Integrate iLiveSDK

1. Download iLiveSDK
[Download iLiveSDK](https://github.com/zhaoyang21cn/iLiveSDK_PC_Suixinbo) at Github

2. Copy files
Copy "include" and "libs" under the iLiveSDK directory to the directory where the solution file ".sln" is located:
![](https://main.qcloudimg.com/raw/bf2314afd8169bdd18d6f8930ce18b8d.png)

3. Add the "include" directory
Add `$(SolutionDir)include` to the project's additional include directory:
![](https://main.qcloudimg.com/raw/ac105f6a7e9c5aa62cded86f6bf646ff.png)

4. Add the library directory
Add `$(SolutionDir)libs` to the project's additional library directory:
![](https://main.qcloudimg.com/raw/078a7447425662586f2e4af0e04a00d8.png)
>**Note:** 
> You must configure Debug and Release versions before adding the above include directory and library directory.

5. Include the header file:
Include the header file in the project and use the ilive namespace to load the lib file of the dynamic library:
```c++
#include "iLive.h"
using namespace ilive;
#pragma comment(lib, "iLiveSDK.lib")
```

6. Copy the dll file to the directory containing .exe:
Copy all the dll files in the libs directory to the solution's Debug and Release directories (both directories will not be generated until Debug and Release are compiled at least once), and then delete the dll files in the libs directory.
>**Note:** 
>] Do not delete iLiveSDK.lib.

7. Verify whether the configuration is successful
Call GetILive() -> getVersion(). Then the current version number of iLiveSDK is returned.
```c++
cout << GetILive()->getVersion() << endl;
```

### Source code description

* Error compiling demo source code:
![](https://main.qcloudimg.com/raw/0d24bb5f04331191ce82587dd083aced.png)

 - Possibly because the 64-bit version is selected in project configuration.
![](https://main.qcloudimg.com/raw/6406babab972b935b36bdbef8741f6c5.png)
iLiveSDK is not supported on the 64-bit version. Change it to 32-bit.


### Execution results
Press [Ctrl + F5] to run the program, and then the version number displays:
![](https://main.qcloudimg.com/raw/9148232b9dee4bb1a7f7c6e90d8087cb.png)

You have successfully integrated iLiveSDK.


## Email
If you have any questions, send us an email to trtcfb@qq.com.

