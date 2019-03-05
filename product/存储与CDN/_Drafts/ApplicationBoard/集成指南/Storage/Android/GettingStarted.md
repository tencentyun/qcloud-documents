# 应用云 Storage 服务 Android 集成指南

## 准备工作

在开始使用应用云 Storage 服务前，确保您已经完成：

[安装和配置SDK](https://github.com/tencentyun/qcloud-documents/blob/master/product/%E5%AD%98%E5%82%A8%E4%B8%8ECDN/_Drafts/ApplicationBoard/%E9%9B%86%E6%88%90%E6%8C%87%E5%8D%97/Core/Android/GettingStarted.md)

## 添加 SDK

如果希望将 Storage 库集成至自己的某个项目中，可以通过 gradle 远程依赖或者 jar 包两种方式集成。

### 通过 gradle 远程依赖集成

如果您使用 Android Studio 作为开发工具或者使用 gradle 编译系统，**我们推荐您使用此方式集成依赖**。

#### 1. 使用 jcenter 作为仓库来源

在工程根目录下的 build.gradle 使用 jcenter 作为远程仓库：

```
buildscript {
    repositories {
        jcenter()
    }
    dependencies {
        ...
    }
}

allprojects {
    repositories {
         jcenter()
    }
}
```

#### 2. 添加 Storage 库依赖

在您的应用级 build.gradle（通常是 app/build.gradle）添加 Storage 的依赖：

```
dependencies {
    //增加这行
    compile 'com.tencent.tac:tac-storage:1.0.0'
}
```

然后，点击您 IDE 的 【gradle】 同步按钮，会自动将依赖包同步到本地。

### 手动集成

如果您使用 Eclipse 作为开发工具并且使用 Ant 编译系统，您可以通过以下方式手动集成。

#### 1. 下载服务资源压缩包。

下载请点击[应用云 Storage 服务资源](https://console.cloud.tencent.com/tac)，并解压。

#### 2. 集成 jar 包。

将资源文件中的 libs 目录下的文件拷贝到您工程的 libs 目录。

## 配置服务

Storage 服务因为需要一个有效的签名提供者，无法直接使用默认配置，您有两种方式可以提供签名。**请在 Storage 服务启动前完成配置，一旦服务启动，后续所有的参数修改都不会生效**。

### 1.提供一个返回有效签名的 HTTP 网络接口

您可以在自己的后台服务器部署该接口，并在 SDK 端通过调用 TACStorageOptions 的 setCredentialProvider 方法配置。SDK会在需要签名的时候，自动调用该接口获取签名。

```
// 请确保已经正确配置好服务框架，否则options()方法会返回null
TACApplicationOptions applicationOptions = TACApplication.options();

TACStorageOptions storageOptions = applicationOptions.sub("storage");
// 配置签名获取接口
storageOptions.setCredentialProvider(new HttpRequest.Builder<String>()
	.scheme("http")					// "http" 或者 "https"
	.host("<SERVER_HOST>")			// 服务器地址
	.path("<PATH>")					// 路径
	.method("GET")
	.query("<name>", "<value>")		// Http query参数
	.header("<name>", "<value>")	// Http header参数
	.build());
```

接口的通用返回格式请参考 [这里](https://console.cloud.tencent.com/tac)。

### 2.自己实现一个签名提供者

如果您希望自己定义协议或者请求过程，您可以继承 SDK 提供的 BasicLifecycleCredentialProvider 类，实现 fetchNewCredentials 方法，获取签名。

```
// 此处使用本地密钥生成签名，只是作为示例。请不要把密钥放在客户端。

public class LocalCredentialProvider extends BasicLifecycleCredentialProvider{
    private String secretKey;
    private long keyDuration;
    private String secretId;

     public LocalCredentialProvider(String secretId, String secretKey, long keyDuration) {
        this.secretId = secretId;
        this.secretKey = secretKey;
        this.keyDuration = keyDuration;
     }

     /**
     返回 BasicQCloudCredentials
     */
     @Override
     public QCloudLifecycleCredentials fetchNewCredentials() throws CosXmlClientException {
         long current = System.currentTimeMillis() / 1000L;
         long expired = current + duration;
         String keyTime = current+";"+expired;
         return new BasicQCloudCredentials(secretId, secretKeyToSignKey(secretKey, keyTime), keyTime);
     }

     private String secretKeyToSignKey(String secretKey, String keyTime) {
         String signKey = null;
         try {
              if (secretKey == null) {
                   throw new IllegalArgumentException("secretKey is null");
              }
              if (keyTime == null) {
                    throw new IllegalArgumentException("qKeyTime is null");
              }
         } catch (IllegalArgumentException e) {
                e.printStackTrace();
         }
         try {
             byte[] byteKey = secretKey.getBytes("utf-8");
             SecretKey hmacKey = new SecretKeySpec(byteKey, "HmacSHA1");
             Mac mac = Mac.getInstance("HmacSHA1");
             mac.init(hmacKey);
             signKey = StringUtils.toHexString(mac.doFinal(keyTime.getBytes("utf-8")));
        } catch (UnsupportedEncodingException e) {
                e.printStackTrace();
        } catch (NoSuchAlgorithmException e) {
                e.printStackTrace();
        } catch (InvalidKeyException e) {
                e.printStackTrace();
        }
      return signKey;
    }
}
```

然后，调用 TACStorageOptions 的 setCredentialProvider 方法设置签名提供者：

```
LocalCredentialProvider crendentialProvider = ...;

// 请确保已经正确配置好服务框架，否则options()方法会返回null
TACApplicationOptions applicationOptions = TACApplication.options();

TACStorageOptions storageOptions = applicationOptions.sub("storage");
// 配置签名获取接口
storageOptions.setCredentialProvider(crendentialProvider);
```
