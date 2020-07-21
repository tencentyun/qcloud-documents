## APP SDK简介

**APP SDK概述**

​	腾讯连连APP SDK是腾讯云物联网平台提供，设备厂商可通过SDK将设备接入腾讯云物联网平台，来进行设备管理。核心模块包含 设备配网的两种模式（SmartConfig与Soft AP）、设备消息操作、账户系统、设备管理

**业务包**

​	APP SDK位于 [iOS工程](https://github.com/tencentyun/iot-link-ios/tree/master/Source)/[Android工程](https://github.com/tencentyun/iot-link-android/tree/master/sdkdemo) 目录中，包含了SDK Demo演示工程，用户可根据SDK Demo快速接入App SDK；

同时也可通过已开源 [iOS腾讯连连工程](https://github.com/tencentyun/iot-link-ios)/[Android腾讯连连工程](https://github.com/tencentyun/iot-link-android) 快速搭建起自己的物联网智能设备管理APP。

**SDK的依赖关系**

​	在腾讯云物联网平台中，APP SDK扮演的角色如图所示。APP通过接入APP SDK来实现与智能设备的配网，和通过物联网平台对智能设备进行管理。目前APP SDK中与设备配网方式提供了SmartConfig配网和Soft AP配网模式。

![image-20200715161006778](https://main.qcloudimg.com/raw/17f887e25211ec5d54ef63592cb16cca.png)






