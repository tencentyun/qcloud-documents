## Downloading Demo
Demo project of XGPush is located in SDK file. You first need to [download SDK](http://xg.qq.com/ctr_index/download).

## Registering Test Application
The name of the test application to be registered is not limited, but the package name must be com.qq.xgdemo. You must obtain the ACCESSID and ACCESSKEY of the application after the registration is completed.
>Note:
>If package names are not consistent, you need to select multiple package names when pushing.

![](https://main.qcloudimg.com/raw/5953bfa11a6fbf60fb1dddb3c00719e8.png)
## Configuring Project

### Android Studio Project

Configure the ACCESSID and ACCESSKEY of test application under the ManifestPlaceholders node in the build.gradle file under the App module of Demo project, as shown below:

![](https://main.qcloudimg.com/raw/ac1dc3a4d212781138c5d4840c6c5bbd.png)

### Eclipse Project

Configure the ACCESSID and ACCESSKEY of test application under the node in the AndroidManifest.xml file of Demo project.

![](https://main.qcloudimg.com/raw/eb3b760d5b7c013e0f360d6d0ba6116c.png)

## Running Code

The following log indicates XGPush is registered successfully. (Log tag: "TPush"):

```
10-09 20:08:46.922 24290-24303/com.qq.xgdemo I/XINGE: [TPush] get RegisterEntity:RegisterEntity [accessId=2100250470, accessKey=null, token=5874b7465d9eead746bd9374559e010b0d1c0bc4, packageName=com.qq.xgdemo, state=0, timestamp=1507550766, xgSDKVersion=3.11, appVersion=1.0]
10-09 20:08:47.232 24290-24360/com.qq.xgdemo D/TPush: Registration successful. Device token:5874b7465d9eead746bd9374559e010b0d1c0bc4
```
## Push Test
Obtain the token of the device for log output. Create push in Application Management on XGPush for Web, as shown below:

![](https://main.qcloudimg.com/raw/039180137ff4776e4dfcaf53e72ee9b8.png)
