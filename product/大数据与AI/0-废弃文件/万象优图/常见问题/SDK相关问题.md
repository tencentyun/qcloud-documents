## 1. Android 相关问题
### 1.1 为什么Android Studio导入Demo后运行无法上传， 会输出日志“!isLibraryPrepared”？
 版本1.1.1之前的Demo是使用Eclipse开发的，使用Android Studio导入时不会自动添加so，需要手动导入。可以在Android Studio的项目配置文件中加入如下配置：
```
sourceSets {
    main {
        jniLibs.srcDirs = ['libs']
    }
}
```

### 1.2上传失败，Log显示异常ClassNotFoundException。
项目使用了代码混淆功能将SDK的代码进行了混淆，上传SDK有些类被混淆之后会导致异常而上传失败。需要将下面的配置加入到项目的混淆配置中：
```
-keep class com.tencent.upload.network.base.ConnectionImpl
-keep class com.tencent.upload.network.base.ConnectionImpl {*;}
-keep class * extends com.qq.taf.jce.JceStruct { *; }
```
## 2.  iOS 相关问题
### 2.1 调用SDK上传API返回错误码-97，比如日志里有：upload return=-97。
表示使用的签名是非法的。可以调用UploadManager的validateSignature判断签名是否合法, 目前图片云的签名后台升级，增加了bucket信息。
### 2.1 调用SDK提供的API返回错误码-80。
表示使用的业务ID是非法的。需要使用在腾讯云控制台应用管理上注册APP时得到的AppID。
### 2.3 调用SDK提供的API返回错误码-79。
表示使用的SecretID不存在。需要使用在腾讯云控制台应用管理上注册APP时得到的SecretID。
### 2.4 调用SDK提供的API返回错误码-182。
 表示参数错误。必填参数不能为空或者不合法，需要校验。
### 2.5 图片云/文件云的写操作，比如删除和更新，需要传入单次签名信息，操作API返回-73。
表示单次签名的过期时间expired不为0。生成单次签名时必须将过期时间expired设置为0。