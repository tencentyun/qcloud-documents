### Overview
Debug mode is a service that verifies the validity and integrity of SDK integration by collecting and displaying logs sent by registered test devices. 
All App logs sent by registered devices are displayed in real time. You can conveniently view log data, such as App version, model information, and event details, to improve the work efficiency of integration and debugging.
>**Note:**
>After the integration test is used, all test data will not be included in the statistical backend of the App, and can only be viewed in **Real-time Log** or **History Debug**. You do not need to worry about the data pollution caused by tests, and the data can reflect the user usage more authentically and effectively.

The real-time debugging is only supported on Android devices, and the support for iOS devices is under development and will be available soon.
### Obtaining MID Tutorial
The identification information of your test devices is required to distinguish between test and normal devices. We provide codes to help you collect the device information. You can follow the steps below:

#### Android Devices
You can refer to the following DEMO for getting MID:
1. Copy the following function into your codes, and call it;
```
requestMidEntity(context, new MidCallback() { 
            @Override
            public void onSuccess(Object data) {
                if (data != null) {
                    MidEntity entity = MidEntity.parse(data.toString());
                    log.d("success to get mid:" + entity.getMid());
                    callback.onSuccess(entity.getMid());
                }
            }
```
2. The codes produce the corresponding log output, that is, identification information of device.

#### iOS Devices
You can refer to the following method for getting MID:
1. Open the debug mode of MTA. Before MTA starts the function, add the following codes:
```
<span><span> [[MTAConfig getInstance] setSmartReporting:YES]; </span></span>
```
2. Find the output similar to the following in the log output by MTA:
![](//mc.qcloudimg.com/static/img/2cdd34bb813532d52b51f4b56054a67c/image.jpg)
3. If the value of middle field is "none", it is because the server has not issued MID yet. Restart the App several times and you can get MID normally.

