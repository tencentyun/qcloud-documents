
### 1. 如何提取SDK输出的Log?
推流或播放过程中出现问题，Log是帮助我们排查问题的重要手段，我们建议您在调试或测试阶段将Log级别设置为DEBUG，这个级别的Log是最全的，有助于我们排查问题，Log级别的定义如下：
![](//mccdn.qcloud.com/static/img/cfe3402e5f9f4bef1f900db2a967e3be/image.png)
您可以通过调用TXLivePlayer或TxLivePush中的**setLogLevel**接口设置Log级别。
如果您使用的安卓手机，我们的Log存储在/sdcard/txRtmpLog目录下，您可以通过adb相关命令查看并提取Log文件：
![](//mccdn.qcloud.com/static/img/1a38cf482394d8e6ab678d44c4059a63/image.png)
如果您使用iPhone手机，我们的Log直接存储在Documents目录下，您可以通过itools工具导出Log文件：
![](//mccdn.qcloud.com/static/img/38ef348f3623dcea65cc4f5a8529dacf/image.png)

### 2. 命名冲突（duplicate symbol）
在集成本SDK时常遇到的一种编译错误，因为一个进程中不能有重名函数（编译器会将函数编译成symbol），如果出现重复的，就会给链接器带来“选择困难症”。

如果您的APP之前使用过类似ffplay这样的播放器，请先将其从工程中移除掉。目前我们团队还没有实力去研发自己的H264软件编解码器，所以也是使用了ffmpeg这样的开源模块来实现H264视频流的编码和解码，只是修复了其中的一些bug而已。如果您的工程中之前就已经包含了它们，自然会带来命名冲突的问题。

如果命名冲突源自其它模块，请联系我们，基于先来后到的原则，我们更改我们的函数命名是情理之中的。
![txc_rtmp_sdk_duplicated_symbol](http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/txc_rtmp_sdk_duplicated_symbol.jpg)

### 3. ffmpeg冲突怎么办？
一般IOS的工程会比较容易遇到这个问题，如果您APP原来就打包有ffmpeg而且确实无法放弃，这里的应对方案如下：
1. 确保您的工程中的ffmpeg已经更新至最新版本（3.0.2）。
2. 检查一下Xcode工程设置中"Other Linker Flags"是否包含**-all_load**，如有请去掉。

这种方案的本质是让APP里链接两份ffmpeg，但是Xcode链接器没有办法做到聪明的可以判断出来两个库的精确调用关系，所以实际上APP内部的两个ffmpeg的调用关系是不可控的（有可能两个库之间的函数交错式调用）。

所以，<font color='red'>如果两个ffmpeg版本不一致，会出现莫名其妙的各种crash</font>，而且这种crash看堆栈一般都是崩溃在ffmpeg内部函数里。

### 4. Android 出现程序崩溃（CRASH）
- **代码混淆原因**
  请注意**com.tencent 包下的文件不要做混淆**，因为有jni封装，混淆会导致java无法定位到期望的接口函数。

- **工程配置原因**
  不少客户会遭遇如下这个错误，解释一下错误原因就是java代码在寻找一个叫做 getSDKVersion 的jni函数，但是发现这个函数没有实现。具体原因是实现这个函数的so没有被您当前的工程加载起来。
```java
java.lang.UnsatisfiedLinkError: No implementation found for 
int[] com.tencent.rtmp.TXRtmpApi.getSDKVersion() 
(tried Java_com_tencent_rtmp_TXRtmpApi_getSDKVersion and Java_com_tencent_rtmp_TXRtmpApi_getSDKVersion)
```
解决方法就是检查一下工程配置，这里要特别说明一下，1.4.1 以及以前的版本，我们都是使用了aar作为sdk打包方案，这种android studio推荐的打包方案虽然感觉比较高大上，但实际兼容性并不好，所以在1.4.2版本开始，我们开始推行传统的jar解决方案，如果您现在拿到的是aar版本的sdk组件包，我建议您尝试一下jar版本的。

- **编解码器冲突**
  不少客户在APP中集成了不止一家的播放器，这里我们需要注意的是，目前国内少有互联网公司会自己研发H264编解码器，包括腾讯在内也是使用现在常见的ffmpeg等开源组件实现视频的软件编解码，所以编解码库的冲突非常普遍。如果您遇到各种百思不得解的运行冲突问题，可以考虑先临时把其它播放器屏蔽一下，看看是不是对稳定定位有所帮助。


### 5. IOS 找不到函数定义（Undefined Symbols  ）
一般是工程配置问题，尤其是IOS下分多种指令架构，armv7, arm64, x86模拟器等等，另外检查下IOS工程的Link Binary With Libraries的配置，我们的SDK需要依赖的库如下（请参考demo工程的配置）：
![txc_rtmp_sdk_link_lib](//mccdn.qcloud.com/static/img/6605e78efb384799b9b4e1c6a5a7aac6/image.jpg)
如果出现如下错误：
![](//mccdn.qcloud.com/static/img/8424405ffd2e666c481c1792d8296172/image.jpg)
请检查工程的c++库的配置：
![](//mccdn.qcloud.com/static/img/07665b7aa7f6495417bb8e2f850f3afa/image.jpg)

### 6. 画面渲染异常（OpenGL ES冲突）
指集成视频云SDK之后，客户原APP的UI渲染界面表现异常（且原工程中有使用cocos2d或者OpenGL ES）
- **可能情况一**：
>原APP中使用了cocos2d，cocos2d是游戏开发中常使用的一套基础库，它在渲染图像时使用了OpenGL ES，而腾讯视频云SDK内部也使用了OpenGL ES，且SDK内部会调用 [EAGLContext setCurrentContext]方法。
>
>所以，如果在启动SDK的推流或者播放功能以后，原APP的某个模块依然在不停地调用[EAGLContext setCurrentContext]方法，会导致OpenGL上下文环境异常。
>
>建议：在推流和播放前调用[[CCDirectorCaller sharedDirectorCaller] stopMainLoop]先停止cocos2d的渲染，等结束后再调用[[CCDirectorCaller sharedDirectorCaller] startMainLoop]恢复之。

- **可能情况二**：
>原APP中没有使用cocos2d，但使用了OpenGL ES，此时iOS控制台会打印“Warning: currentContext != [[AVGLShareInstance shareInstance] context]” ，这是腾讯视频云SDK检测到EAGLContext的context被其它模块篡改后的一次warning打印，它说明您的APP里可能有其他模块也在调用OpenGL。通常情况下，没有必要同时渲染两个OpenGL View。
>
>建议：调整一下目前APP里的逻辑，不要让视频云SDK的渲染逻辑和您的OpenGL ES逻辑同时运行。
