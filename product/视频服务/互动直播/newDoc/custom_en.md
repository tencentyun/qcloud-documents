## Feature Customization

If your application scenarios are so special that you can't find implementations of your demands throughout the documentation and demo code,<br/>
you can use the APIs of IMSDK and AVSDK to customize signaling, groups and audio/video interfaces.<br/>

* Android

##### Get IM Controller Instance

```
TIMManager imManager = ILiveSDK.getTIMManager();
```

For detailed information about Android IMSDK APIs, please click [here](https://www.qcloud.com/document/product/269/1557).

##### Get AV Context Instance

```
AVContext avContext = ILiveSDK.getAVContext();
```

For detailed information about Android AVSDK APIs, please click [here](https://www.qcloud.com/document/product/268/7685).

* iOS


##### Get IM Controller Instance

```
TIMManager *imManager = [[ILiveSDK getInstance] getTIMManager];
```

For detailed information about iOS IMSDK APIs, please click [here](https://www.qcloud.com/document/product/269/1565).

##### Get AV Context Instance

```
QAVContext *avContext = [[ILiveSDK getInstance] getAVContext];
```

For detailed information about iOS AVSDK APIs, please click [here](https://www.qcloud.com/document/product/268/7661).


**Notes:** Use above APIs after iLiveSDK has been initialized and logged in.


## Want to launch your product as fast as possible, regardless of the cost?

Sorry, there is no solution to this in the document.<br/>
However, we prepared a premium service channel for you. Please add this QQ number as friend: 3358225043 (specify your company name plus "ILVB" in the message).

