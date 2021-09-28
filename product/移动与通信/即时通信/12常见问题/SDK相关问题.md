
### TUIKit 源码是否支持 Androidx？
TUIKit 最新源码已经支持 Androidx。

### 登录报错 6012 或  TLSSDK exchange ticket fail ？

- 初始化接口和登录接口要分开调用，不能连续调用（因为初始化方法中有异步操作）；
- 如果您当前是即时通信 IM 体验版，需要升级为专业版，升级后可正常登录，可以到 [即时通信 IM 购买页面](https://buy.cloud.tencent.com/avc) 进行购买升级，详细价格说明请参阅 [产品价格](https://cloud.tencent.com/document/product/269/11673)。

### 出现 6013 SDK 未初始化错误？

如果出现 6013 SDK 未初始化错误，您可以尝试以下方式排查：
1. 查看是否没有登录成功就进行收发消息等其他操作；
2. 查看是否登录时被其它终端踢掉，IM SDK 默认一个帐号仅能在一个终端上登录。处理方式请参考 [多终端同时登录](https://cloud.tencent.com/document/product/269/3665#.E5.A4.9A.E7.AB.AF.E7.99.BB.E5.BD.95) 文档；
3. Android 请关注库文件是否未能全部加载，或是使用过程中被系统回收。

### code: 6205 desc: QALSERVICE not ready？

在初始化后调用了 `stopQALService` 导致此错误，可以参考客户分享的 [配置方法](https://blog.csdn.net/qq_16131393/article/details/54895733)。

### 发送表情，消息列表显示为空、或者乱码?

即时通信 IM 不提供表情包，具体的解析需要自己对齐。
表情使用方式有两种方式：
- 一种是使用 TIMFaceElem 中的 index，标识表情的索引，例如 Android 和 iOS 两端都有同一套表情图，索引2为笑脸，index=2 就表示笑脸，两端发送和接收都显示同一张索引表情图片即可。
- 另一种是使用 TIMFaceElem 中的 data，例如表情图片是由字符串命名，smile 表示笑脸，可在 data 中存储 smile，iOS 和 Android 两端都通过 data 作为 key 找到对应表情图片进行显示。

另外也可以两个字段都使用，如 data 表示哪一套表情，index 表示这套表情的哪个索引，可以实现类似 QQ 的多种不同表情效果。甚至可以在 data 数据中存储更为复杂的数据结构，只要多端解析规则一致即可。



### 有时进行操作时返回错误码：10002?

在需要进行服务端验证的操作时，如果网络异常、超时或者票据切换失败，就会返回此状态码，遇到此状态码时稍后重试即可。

### 收发消息时，收到错误码 6200 或 6201？

返回此状态码时，是客户端在网络离线、超时或无网络访问时出现，6200 的定义为请求时没有网络，6201 的定义为响应时没有网络，遇到此状态码时，请检查网络或等待网络恢复后重试。


### 收发消息时返回错误码：20003？

请检查用户帐号（UserID）是否已在腾讯云导入，当 UserID 无效或 UserID 未导入腾讯即时通信 IM 时，会返回此错误码。

### 语音消息播放语音时返回错误码：6010？

通常情况是语音消息超过了漫游保存有效期，请求失败导致，可 [延长漫游消息时间](https://cloud.tencent.com/document/product/269/38656#.E5.8E.86.E5.8F.B2.E6.B6.88.E6.81.AF.E5.AD.98.E5.82.A8.E6.97.B6.E9.95.BF.E9.85.8D.E7.BD.AE) 或获取语音文件到本地播放（已过期的文件无法恢复）。但不同版本的 SDK 支持延长历史消息存储时长的消息类型不同，详情请参见 [消息存储](https://cloud.tencent.com/document/product/269/3571#MsgType)。

### 帐号鉴权时返回错误码 70001 或 70003 或 70009 或 70013？

这些状态码对应的原因是 UserID 与 UserSig 不匹配，请检查 UserID 及 UserSig 的有效性。其中，70001 定义为 UserSig 已过期，70003 定义为 UserSig 被截断导致校验失败，70009 定义为 UserSig 公钥校验不匹配，70013 定义为 UserID 不匹配。

### Web 端使用 IM SDK 时返回错误码-2或-5？

- \-2：Web 端请求服务器失败，通常为网络问题，Web 端使用 HTTP Long Polling 方式向服务端请求，网络存在问题时会返回此状态码，请检查网络或重试。
- \-5：登录操作未完成，SDK 未获取到服务器返回的 a2key 和 tinyID 时，直接调用其它接口会出现“tinyid或a2为空”的错误提示信息和-5的错误码。

### 在 armeabi 平台上 SDK 报"java.lang.UnsatisfiedLinkError: No implementation found for"错误该如何处理？
拷贝 imsdk 的 aar 里面的 jni/armeabi-v7a/libImSDK.so 到源码工程的 src/main/jniLibs/armeabi 目录里，并在 build.gradle 中加载即可。

### 上架 App Store 时，出现 x86_64, i386 架构错误该如何解决？
该问题是由于 App Store 不支持 x86_64, i386 架构引起的，具体解决方法如下：
1. 清空项目编译缓存：
 选择**Product**>**clean**，按住Alt变成 clean build Folder...，等待操作完成。
2. 剔除 App Store 不支持的 x86_64 和 i386 架构：
 a. 选择**TARGETS**>**Build Phases**。
 b. 单击加号，选择**New Run Script Phase**。
 c. 添加如下代码：
 
```
APP_PATH="${TARGET_BUILD_DIR}/${WRAPPER_NAME}"  

# This script loops through the frameworks embedded in the application and  

# removes unused architectures.  

 find "$APP_PATH" -name '*.framework' -type d | while read -r FRAMEWORK  
 do  
 FRAMEWORK_EXECUTABLE_NAME=$(defaults read "$FRAMEWORK/Info.plist" CFBundleExecutable)  
 FRAMEWORK_EXECUTABLE_PATH="$FRAMEWORK/$FRAMEWORK_EXECUTABLE_NAME"  
 echo "Executable is $FRAMEWORK_EXECUTABLE_PATH"  

 EXTRACTED_ARCHS=()  

 for ARCH in $ARCHS  
 do  
 echo "Extracting $ARCH from $FRAMEWORK_EXECUTABLE_NAME"  
 lipo -extract "$ARCH" "$FRAMEWORK_EXECUTABLE_PATH" -o "$FRAMEWORK_EXECUTABLE_PATH-$ARCH"  
 EXTRACTED_ARCHS+=("$FRAMEWORK_EXECUTABLE_PATH-$ARCH")  
 done  

 echo "Merging extracted architectures: ${ARCHS}"  
 lipo -o "$FRAMEWORK_EXECUTABLE_PATH-merged" -create "${EXTRACTED_ARCHS[@]}"  
 rm "${EXTRACTED_ARCHS[@]}"  

 echo "Replacing original executable with thinned version"  
 rm "$FRAMEWORK_EXECUTABLE_PATH"  
 mv "$FRAMEWORK_EXECUTABLE_PATH-merged" "$FRAMEWORK_EXECUTABLE_PATH"  

 done
```

 ![](https://main.qcloudimg.com/raw/f343cb4d7674d58623dfa0097d2c6484.png)

3. 重新打包上传。

