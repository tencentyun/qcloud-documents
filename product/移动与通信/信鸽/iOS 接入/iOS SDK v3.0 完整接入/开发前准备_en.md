## Overview
XGPush iOS SDK is a development platform that provides Push services and simple and easy-to-use APIs for developers to achieve quick connection.

## Connection Method
1. Obtain AppId and AppKey.
2. Configure projects.

### Obtaining AppId and AppKey
Sign up at [http://xg.qq.com](http://xg.qq.com) to obtain the AppKey.

### Configuring Projects
1. Download the XGPush SDK and decompress it. Note: Version 3.0 SDK does not support pods.
2. Add XGPush.h and libXG-SDK.a to the project.
3. Add the references of the following library/framework, including CoreTelephony.framework, SystemConfiguration.framework,
UserNotifications.framework, libXG-SDK.a, libz.tbd, and libsqlite3.0.tbd. After that, the library references are as follows:
![](//mc.qcloudimg.com/static/img/a8375845f7a6dc63a951255da13730ad/image.jpg)
4. Open the push in the project configuration and backend modes, as shown below 
![](//mc.qcloudimg.com/static/img/e875b2b189be94311d65b5c70a17b730/image.png)
5. Add compilation parameter - ObjC 
![](//mc.qcloudimg.com/static/img/03ca0cdeeb661b38dd3a731392330ab4/image.jpg)
6. Add relevant codes in reference to Demo.














