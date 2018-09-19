


## 手动集成 SDK

如果您无法通过 gradle 远程依赖的方式来集成 SDK，我们提供了手动的方式来集成服务：

### 1. 下载服务资源压缩包。

1. 下载 [移动开发平台（MobileLine）核心框架资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-core-1.0.0.zip)，并解压。

2. 下载 [移动开发平台（MobileLine） Storage 资源包](http://tac-android-libs-1253960454.cosgz.myqcloud.com/1.0.0/tac-storage-1.0.0.zip)，并解压。

### 2. 集成 jar 包。

将资源文件中的所有 jar 包拷贝到您工程的 `libs` 目录。

## 配置服务

Storage 服务因为需要一个有效的签名提供者，无法直接使用默认配置，您有两种方式可以提供签名。**请在 Storage 服务启动前完成配置，一旦服务启动，后续所有的参数修改都不会生效**。

### 1. 提供一个返回有效签名的 HTTP 网络接口

您可以在自己的后台服务器部署该接口，并在 SDK 端通过调用 TACStorageOptions 的 setCredentialProvider 方法配置。SDK 会在需要签名的时候，自动调用该接口获取签名。

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

接口的通用返回格式如下：

```
{
	"credentials": {
		"sessionToken": "xxxxxxx",
		"tmpSecretId": "xxxxxxx",
		"tmpSecretKey": "xxxxxxx"
	},
	"expiredTime": 1522038254,
	"bucket": "p123123-storage-1251668577",   // bucket名称
	"region": "ap-shanghai"   // bucket所在地区
}
```

### 2. 自己实现一个签名提供者

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



## 文件引用

### 创建引用

引用可以看作是指向云端文件的指针：要上传、下载或删除文件，或要获取或更新文件的元数据，请创建引用。
 
```
TACStorageService storage = TACStorageService.getInstance();

TACStorageReference reference = storage.rootReference();
```

上面的代码是获取整个 bucket 的根目录的引用，如果想要创建某个子文件的引用，可以使用：

```
TACStorageReference reference = storage.referenceWithPath('images');
```

### 引用导航

引用可以向上或者向下导航：

```
// 获取根节点的引用
TACStorageReference rootRef = reference.root();

// 获得父节点的引用
TACStorageReference parentRef = reference.parent();

// 获取当前引用下某个子节点的引用
TACStorageReference childRef = reference.child('imageA.jpg');

```

### 引用属性

您可以使用 getPath()、getName() 和 getBucket() 方法检查引用，以便更好地了解它们指向的文件。

```
// 获取文件路径
reference.getPath();

// 获取文件名
reference.getName();

// 获取文件所在bucket
reference.getBucket();

// 获取bucket所在区域
reference.getRegion();
```

## 上传文件

### 上传文件

您可以将内存中的数据，本地文件路径，或者是数据流传输到远程 Storage 中。

```
StorageReference storageRef = storage.referenceWithPath('images/imageA.jpg');

// 通过内存中的数据上传文件
byte[] tmpData = new byte[200];
reference.putData(tmpData, null));

// 上传本地文件
File localFile = new File("path/to/file");
reference.putFile(Uri.fromFile(localFile), null);

// 上传数据流
InputStream stream = new FileInputStream(new File("path/to/file"));
reference.putStream(stream, null);
```

### 添加文件元数据

在上传文件时，您还可以带上元数据。此元数据包含常见的文件元数据属性，如 name、size 和 contentType（通常称为 MIME 类型）。

```
StorageReference storageRef = storage.referenceWithPath('images/imageA.jpg');
TACStorageMetadata metadata = new TACStorageMetadata.Builder().contentLanguage("CN").build();

// 通过内存中的数据上传文件，并带上metadata
reference.putData(tmpData, metadata));

// 上传本地文件，并带上metadata
reference.putFile(Uri.fromFile(localFile), metadata);

// 上传数据流，并带上metadata
reference.putStream(stream, metadata);
```


### 管理上传

如果您想要管理上传的行为，可以调用 pause 和 resume，注意暂停和继续只针对大文件的上传有效：

```
TACStorageUploadTask uploadTask = reference.putData(tmpData, TACMetadata));

// 暂停任务
uploadTask.pause();

// 继续任务
uploadTask.resume();

```

### 通过重新启动进程继续上传

对于本地的大文件上传，我们支持断点续传，您可以本地记录上传的 uploadId，在下次 app 启动的时候从上次停止的地方上传，而不会重头开始，节省您的带宽和时间。

```
TACStorageReference reference = tacStorageService.referenceWithPath("/tac_test/multipart");
File uploadFile = createFile(10 * 1024 * 1024);
TACStorageUploadTask uploadTask = reference.putFile(Uri.fromFile(uploadFile), null)
      .addProgressListener(new StorageProgressListener<TACStorageTaskSnapshot>() {
            @Override
            public void onProgress(TACStorageTaskSnapshot snapshot) {
                uploadId = snapshot.getUploadId();
            }
      });
```

您可以在 uploadId 存放在您本地的 sharedPreference，下次启动后，您可以继续上传：

```
// 传入上次的 uploadId，将会从之前断开的地方继续上传
TACStorageReference reference = tacStorageService.referenceWithPath("/tac_test/multipart");
reference.putFile(Uri.fromFile(uploadFile), null, uploadId);
```

## 下载文件

您可以调用 downloadToFile 方法，将一个远程文件下载到本地：

```
TACStorageReference reference = storage.referenceWithPath("/tac_test/multipart");
Uri fileUri = Uri.fromFile(new File(getExternalCacheDir() + File.separator + "local_tmp"));
reference.downloadToFile(fileUri);
```

## 删除文件

您可以调用 delete 方法，删除一个远程文件：

```
TACStorageReference reference = storage.referenceWithPath("/tac_test/multipart");
reference.delete();
```

## 添加任务结果监听

您可以调用 TACStorageTask 的 addResultListener 方法，监听任务结果：

```
TACStorageUploadTask uploadTask = reference.putData(tmpData, TACMetadata));
uploadTask.addResultListener(new StorageResultListener<TACStorageTaskSnapshot>() {
            @Override
            public void onSuccess(final TACStorageTaskSnapshot snapshot) {
                showMessage(new Runnable() {
                    @Override
                    public void run() {
                        // 上传成功
                    }
                });
            }

            @Override
            public void onFailure(final TACStorageTaskSnapshot snapshot) {
                showMessage(new Runnable() {
                    @Override
                    public void run() {
                        // 上传失败
                        Exception exception = snapshot.getError();
                    }
                });
            }

```

## 添加任务进度监听

针对下载和上传任务，您可以使用 addProgressListener 方法可以监听数据的进度：

```
TACStorageUploadTask uploadTask = reference.putData(tmpData, TACMetadata));
uploadTask.addProgressListener(new StorageProgressListener<TACStorageTaskSnapshot>() {
            @Override
            public void onProgress(TACStorageTaskSnapshot snapshot) {
                Log.i("QCloudStorage", "progress = " + snapshot.getBytesTransferred() + "," +
                        snapshot.getTotalByteCount());
            }
        });
```

## 取消任务

您可以调用 cancel 方法取消任务，请注意，根据任务当时的运行进度，**取消指令不一定能成功**。

```
TACStorageReference reference = tacStorageService.referenceWithPath("/tac_test/multipart3");
File uploadFile = createFile(10 * 1024 * 1024);
TACStorageUploadTask uploadTask = reference.putFile(Uri.fromFile(uploadFile), null);

uploadTask.cancel();
```
