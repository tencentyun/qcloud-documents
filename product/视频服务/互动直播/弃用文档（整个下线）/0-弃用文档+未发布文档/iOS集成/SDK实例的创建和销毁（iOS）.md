## 一. QAVContext 介绍
 在启动AVSDK之前，需要创建一个QAVContext（SDK上下文）对象。QAVContext管理着SDK内部线程以及运行的上下文。可以认为， QAVContext对象代表着一个SDK运行实例。在大多数情况下，应用程序只需要创建唯一一个 QAVContext对象即可使用SDK的所有功能。


#### 注意：
创建的时候，必须保证QAVContext实例的唯一性，同时创建多个QAVContext实例可能会因为设备占用等方面的原因，出现无法预料的结果。

## 二. QAVContext的创建和销毁
为了保证QAVContext实例的唯一性，则要使用单例模式，实现一个继承NSObject的类来实现AVContext的创建和销毁。

### 1. 创建QAVContext
 创建上下文有以下两个步骤：
- （1）通过QAVContextConfig配置QAVContext的参数
- （2）根据参数创建QAVContext

接口描述：

```
/**
 @brief 创建QAVContext对象。
 
 @details App使用SDK总是从CreateContext开始的，该静态成员函数返回一个新的QAVContext实例。
 
 @param config 创建QAVContext所需的配置信息。
 
 @return 成功则返回QAVContext的实例指针；否则返回nil。
 
 @remark
 - 创建成功之后，App需要进一步调用StartContext来启动QAVContext对象。
 - App必须保证QAVContext实例的唯一性。
 */
+(QAVContext*)CreateContext:(QAVContextConfig*)config;
```

创建一个继承NSObject的类AVUtil并且在它的.m文件中，写入如下示例代码（参数为模拟参数，真实的参数需要在Server端获取）：
```
QAVContext *av_context;

#pragma mark - 创建Context -
+ (QAVContext *)sharedContext
{
    if (!av_context) {

        //1.配置Config参数
        QAVContextConfig* config = [[QAVContextConfig alloc]init];
        config.sdk_app_id = @"1104620500";     //腾讯为每个使用SDK的App分配的AppId
        config.app_id_at3rd = @"1104620500";   //App使用的OAuth授权体系分配的AppId
        config.account_type = @”107”;          //腾讯为每个接入方分配的账号类型
        config.identifier = @"rogerlin";       //账号名

        //2.根据参数创建Context
        av_context = [QAVContext CreateContext:config];
    }
    return av_context;
}

```
2. 销毁QAVContext

（1）销毁目前的QAVContext对象，必须要在调用createContext后才能使用

（2）销毁后要把QAVContext对象置为空。

接口描述：

```
/**
 @brief 销毁目前的QAVContext的单例对象。
 
 @details 需要在CreateContext之后才能调用
 
  @param context 需要销毁的QAVContext对象。
 
 */
+(void)DestroyContext:(QAVContext*)context;

```

在AVUtil.m里加入如下示例代码：

```
+ (void)destroyContext
{
    if (av_context) {
        [QAVContext DestroyContext:av_context];
        av_context = nil;
    }
}
```

 并在AVUtil.h里加入接口声明：
 

```
+ (QAVContext *)sharedContext;

+ (void)destroyContext;

```
之后即可在相应的ViewController中进行调用了。

## 三. QAVContext的启动和终止
### 1. 启动QAVContext
启动上下文分为以下两个步骤：

#### （1）登录ImSDK
以下填的LoginParam的模拟参数与上方的一样

```
    [[TIMManager sharedInstance]setEnv:0];            //设置为正式环境
    [[TIMManager sharedInstance]initSdk: @"1104620500"];        //初始化SDK

    TIMLoginParam * loginParam = [[TIMLoginParam alloc]init];
    loginParam.accountType =@”107”;
    loginParam.identifier = @"rogerlin";
    loginParam.appidAt3rd =@"1104620500";
    loginParam.userSig = @”123”;
    loginParam.sdkAppId = @"1104620500";
    
    //登录Im，成功就可以创建QAVContext的实例
    [[TIMManager sharedInstance]login:loginParam succ:^{
        NSLog(@"login success");
        //创建QAVContext的实例代码
       
    } fail:^(int code, NSString *msg) {
        NSLog(@"login error code = %d",code);
    }];
```
#### （2） 启动QAVContext
接口描述：

```
/**
 @brief 启动QAVContext对象。
 
 @details StartContext是一个异步操作，内部会启动工作线程，创建各种内部对象。

 @param  block	返回启动Context的结果是成功还是失败

 @return 返回值表示异步操作启动是否成功；异步操作执行结果通过回调函数返回。
 
 @retval QAV_OK 启动成功。
 @retval 其他值 启动失败。
 
 @remark
 - 只有当异步操作启动成功的时候，才会通过回调函数异步返回执行结果；
 - 当异步操作启动失败的时候，直接通过StartContext的返回值返回错误，不会再触发回调函数；
 - App收到block回调的时候，表示StartContext执行完毕；
 - startContext执行成功之后，App才能进一步调用QAVContext的其他成员函数；
 - startContext执行成功之后，App必须调用stopContext来终止QAVContext对象。

 @attention 以下两点约定也适用于SDK的其他异步操作接口：
 -# 只有当异步操作启动成功的时候，才会通过回调函数异步返回执行结果；
 -# 当异步操作启动失败的时候，直接通过StartContext的返回值返回错误，不会再触发回调函数。
 */
-(QAVResult)startContext:(ContextOperationBlock)block;
```
 

示例代码：

```
    [[AVUtil sharedContext]startContext:^(QAVResult result) {
            if (result == QAV_OK) {
                NSLog(@"startContext is OK");
                //开启Context成功后即可进入音视频房间
            }
     }];
```
 
### 2. QAVContext的终止
接口描述：

```
/**
 @brief 终止QAVContext对象。
 
 @details stopContext是一个异步操作，内部会终止工作线程，销毁各种内部对象。
 
 @param block 返回终止Context的结果是成功还是失败
 
 @return 返回值表示异步操作启动是否成功；异步操作执行结果通过回调函数返回。
 
 @retval QAV_OK 启动成功。
 @retval 其他值 启动失败。
 
 @remark
 - App应该设法保证startContext和stopContext的配对调用；
 - stopContext内部如果判断到当前还没退出音视频房间，会自动调用ExitRoom；
 */
-(QAVResult)stopContext:(ContextOperationBlock)block;
```

 示例代码：
 
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