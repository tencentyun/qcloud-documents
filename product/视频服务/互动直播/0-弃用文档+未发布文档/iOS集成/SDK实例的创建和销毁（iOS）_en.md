## QAVContext Introduction
 Before launching AVSDK, you need to create a QAVContext (SDK context) object. QAVContext is used to manage SDK internal threads and running contexts. A QAVContext object can be considered as a running SDK instance. In most cases, an application only needs to create one unique QAVContext object to use all SDK features.


#### Note:
Ensure that the created QAVContext instance is unique. Creating multiple QAVContext instances may lead to unexpected consequences due to reasons such as device occupation.

## Creating/Terminating QAVContext
To ensure the uniqueness of the QAVContext instance, you need to use the singleton pattern to implement a class that inherits NSObject to create and terminate AVContext.

### 1. Create QAVContext
 To create context, follow the steps below:
- (1) Configure the parameters of QAVContext by using QAVContextConfig.
- (2) Create QAVContext based on the parameters.

API Description:

```
/**
 @brief creates the QAVContext object.
 
 @details App always starts from CreateContext when using the SDK, and the static member function returns a new instance of QAVContext.
 
 @param config creates the configuration information required for QAVContext.
 
 @return returns the instance pointer of QAVContext when successful; otherwise it returns nil.
 
 @remark
 - After it is successfully created, App needs to further call StartContext to start the QAVContext object.
 - App must ensure that the QAVContext instance is unique.
 */
+(QAVContext*)CreateContext:(QAVContextConfig*)config;
```

Create a class AVUtil that inherits NSObject and write the following sample code in its .m file (The parameters are for simulation only. You need to acquire the actual parameters from the Server end):
```
QAVContext *av_context;

#pragma mark - Create Context -
+ (QAVContext *)sharedContext
{
    if (!av_context) {

        //1. Configure the Parameter Config
        QAVContextConfig* config = [[QAVContextConfig alloc]init];
        config.sdk_app_id = @"1104620500";     //The AppId assigned by Tencent for each App that uses the SDK
        config.app_id_at3rd = @"1104620500";   //The AppId assigned by the OAuth authorization system used by App
        config.account_type = @"107";          //The account type assigned by Tencent for each access party
        config.identifier = @"rogerlin";       //Account Name

        //2. Create Context based on Parameters
        av_context = [QAVContext CreateContext:config];
    }
    return av_context;
}

```
2) Terminate QAVContext

(1) Terminating the current QAVContext is only available after createContext is called.

(2) The QAVContext object should be set as null after termination.

API Description:

```
/**
 @brief terminates the singleton object of the current QAVContext.
 
 @details needs to be called after CreateContext.
 
  @param context needs the terminated QAVContext object.
 
 */
+(void)DestroyContext:(QAVContext*)context;

```

Add the following sample code in AVUtil.m:

```
+ (void)destroyContext
{
    if (av_context) {
        [QAVContext DestroyContext:av_context];
        av_context = nil;
    }
}
```

 And add the API declaration in AVUtil.h:
 

```
+ (QAVContext *)sharedContext;

+ (void)destroyContext;

```
Then, you can call it in the corresponding ViewController.

## Launching/Terminating QAVContext
### 1. Launch QAVContext
Launching context requires two steps:

#### (1) Log in to ImSDK
The simulation parameters of LoginParam entered below are the same as above

```
    [[TIMManager sharedInstance]setEnv:0];//Set to the formal environment
    [[TIMManager sharedInstance]initSdk: @"1104620500"];//Initialize the SDK

    TIMLoginParam * loginParam = [[TIMLoginParam alloc]init];
    loginParam.accountType =@"107";
    loginParam.identifier = @"rogerlin";
    loginParam.appidAt3rd =@"1104620500";
    loginParam.userSig = @"123";
    loginParam.sdkAppId = @"1104620500";
    
    //Log in to Im, then you can create an instance of QAVContext when successful
    [[TIMManager sharedInstance]login:loginParam succ:^{
        NSLog(@"login success");
        //Create the sample code of QAVContext
       
    } fail:^(int code, NSString *msg) {
        NSLog(@"login error code = %d",code);
    }];
```
#### (2) Launch AVContext
API Description:

```
/**
 @brief launches the QAVContext object.
 
 @details StartContext is an asynchronous operation, in which working threads will be launched internally and various internal objects will be created.

 @param block returns whether the result for launching Context is successful or failed.

 @return indicates whether the asynchronous operation is successful or not; the execution result of asynchronous operation is returned by the callback function.
 
 @retval QAV_OK means the launch is successful.
 @retval other value means the launch is failed.
 
 @remark
 - Only when the asynchronous operation launches successfully, it will asynchronously return the execution result through the callback function;
 - When the asynchronous operation fails to launch, it returns an error directly through the return value of StartContext and will no longer trigger the callback function;
 - When App receives a block callback, it means the execution of StartContext is completed;
 - After startContext is successfully executed, App can further call the other member functions of QAVContext;
 - After startContext is successfully executed, App must call stopContext to terminate the QAVContext object.

 @attention the following two conventions also apply to other asynchronous operation APIs:
 -# Only when the asynchronous operation launches successfully, it will asynchronously return the execution result through the callback function;
 -# When the asynchronous operation fails to launch, it returns an error directly through the return value of StartContext and will no longer trigger the callback function;
 */
-(QAVResult)startContext:(ContextOperationBlock)block;
```
 

Sample code:

```
    [[AVUtil sharedContext]startContext:^(QAVResult result) {
            if (result == QAV_OK) {
                NSLog(@"startContext is OK");
                //You can join the audio/video room after successfully opening the Context.
            }
     }];
```
 
### 2. Terminate QAVContext
API Description:

```
/**
 @brief terminates the QAVContext object.
 
 @details stopContext is an asynchronous operation, in which working threads will be terminated internally and various internal objects will be terminated.
 
 @param block returns whether the result of Context termination is successful or failed.
 
 @return indicates whether the asynchronous operation is successful or not; the execution result of asynchronous operation is returned by the callback function.
 
 @retval QAV_OK means the launch is successful.
 @retval other value means the launch is failed.
 
 @remark
 - App should try to ensure the paired calling of startContext and stopContext;
 - stopContext will automatically call ExitRoom if the audio/video room is considered as not yet exited currently through the internal evaluation;
 */
-(QAVResult)stopContext:(ContextOperationBlock)block;
```

 Sample code:
 
```
- (void)stopContext
{
    [[AVUtil sharedContext]stopContext:^(QAVResult result) {
        if (result == QAV_OK) {
            NSLog(@"stopContext OK");
        }
    }];
}

```
