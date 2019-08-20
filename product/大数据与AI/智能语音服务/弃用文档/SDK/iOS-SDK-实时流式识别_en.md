## Preparations for Development

### Obtaining SDK

You can download Artificial Audio Intelligence iOS SDK for streaming speech recognition at [iOS SDK](https://mc.qcloudimg.com/static/archive/e681b228c06e53096510b3b61c012d36/QCloudAAI_IOSSDK.zip)

For more demos, please see [iOS Demo](https://mc.qcloudimg.com/static/archive/44653a19a6f274ebc2b3f7ef028bb72b/QCloudAAI_IOSDemo.zip)

### Preparations for Development

-  Only iOS 8.0 and later are supported. bitcode version is not supported.
-  To conduct streaming speech recognition, your mobile phone must be connected to such networks as GPRS, 3G or WIFI.
-  Obtain APP ID, SecretID and SecretKey from the console. For more information, please see [Basic Concepts](https://cloud.tencent.com/document/product/441/6194).


### Configuring SDK

#### Importing SDK

iOS SDK package name: QCloudAAIClientSDK.zip, including a ` .a` static library and a header file folder Headers.

#### Configuring Project

Configure "Other Linker Flags" in "Build Settings" and add the parameter `-ObjC`.

![Parameter Configuration](https://mccdn.qcloud.com/static/img/58327ba5d83809c77da158ff95627ef7/image.png)

Configure the project's ` info.plist` file as follows:

1. Add "App Transport Security Settings", and then add "Allow Arbitrary Loads" as "Boolean" in "App Transport Security Settings", and set its value to `YES`.

2. Initialize "QCloudAAIClient" instance object "myClient" in the program, ` [myClient openHTTPSrequset:YES]`. HTTPS is supported by the program.

3. Add "Privacy - Microphone Usage Description" in the project's `info.plist ` file to enable microphone.
Add dependent library in the project, and then add the following libraries in "build Phases Link Binary Whith Libraries":
	- libstdc++.6.0.9.tbd
	- libc++.tdb

## Acquiring Signature

It is recommended that the mobile device request the business server to generate the signature for the mobile SDK. For more information on how the business server generates the signature and how to use the signature, please see [Signature Authentication](https://cloud.tencent.com/document/product/441/6203). QCloudAAIGetSignDelegate protocol in QCloudAAIClient is required to recognize the SDK signature, and the (NSString*)param provided by SDK needs to be encrypted.

```objective-c
// Acquire the signature
- (NSString *)getRequestSign:(NSString*)param;
```


## Initialization

Introduce the header file *QCloudAAIClient .h* of the SDK. Directory-related operations need first instantiate QCloudAAIClient object.

#### Method Prototype

```objective-c
-(id)initWithAppid:(NSString *)appid secretid:(NSString *)sid  projectId:(NSString *)pid ;
```

#### Parameter Description

| Parameter Name | Type | Required | Description |
| ------------- | ------------ | ---- | ---------------------------------------- |
| appId  | NSString * | Yes | Project ID, i.e. APP ID |
| sid | NSString * | Yes | SecretID of the project |
| pid  | NSString * | Yes | ProjectID of the project |


### STEP1: Initialize QCloudAAIClient

#### Example

```objective-c
QCloudAAIClient *client= [[QCloudAAIClient alloc] initWithAppid:appid secretid:sid projectId:projectId]];
```
### STEP2: Start Speech Recognition

```
-(BOOL)startDetectionWihtCompletionHandle:(QCloudAAICompletionHandler)handler stateChange:(QCloudAAIChangeHandler)stateChange；
```

#### Example

```objective-c

 client = [[QCloudAAIClient alloc] initWithAppid:appid secretid:sid projectId:projectId];
  client.delegate = self;
 [client startDetectionWihtCompletionHandle:^(QCloudAAIRsp *rsp) {
        if (rsp.retCode == 0) {
            UITextView *strong = temp;
            if (![t isEqualToString:rsp.voiceId]) {
                t = rsp.voiceId;
                previous = strong.text;
            }
            strong.text= [NSString stringWithFormat:@"%@%@",previous,rsp.text];
        }else{
            NSLog(@"speech recognition failure code= %dmsg:%@",rsp.retCode,rsp.descMsg);
        }
       
    }
    stateChange:^(QCloudAAIState state) {
        UITextView *strong = dTemp;
        if (state == QCloudAAIStateOpen) {
            strong.text = [NSString stringWithFormat:@"status: %@",@"Recognizing"] ;
        }else if(state == QCloudAAIStateClose){
             strong.text = [NSString stringWithFormat:@"status: %@",@"Stop Recognizing"] ;
        }else if(state == QCloudAAIStateFail){
            strong.text = @"Microphone is not enabled. Recognition failed";
        }
    }];

```
### STEP3: Stop Speech Recognition

```objective-c
 [client stop];

```

