如果您细心对比过 JSON Android SDK 和 XML Android SDK 的文档，您会发现并不是一个简单的增量更新。XML Android SDK 不仅在架构、可用性和安全性上有了非常大的提升，而且在易用性、健壮性和传输性能上也做了非常大的改进。如果您想要升级到 XML Android SDK，请参考下面的指引，一步步完成 SDK 的升级工作。

## 功能对比

下表列出了 JSON Android SDK 和 XML Android SDK 的主要功能对比：

| 功能       | XML Android SDK         | JSON Android SDK                         |
| -------- | :------------: | :------------------:    |
| 文件上传 | 支持本地文件、字节流、输入流上传<br>默认覆盖上传<br>智能判断上传模式<br>简单上传最大支持5GB<br>分块上传最大支持48.82TB（50,000GB） | 只支持本地文件上传<br>可选择是否覆盖<br>需要手动选择是简单还是分片上传<br>简单上传最大支持20MB<br>分片上传最大支持64GB |
| 文件删除 | 支持批量删除 | 只支持单文件删除 |
| 存储桶基本操作 | 创建存储桶<br>获取存储桶<br>删除存储桶   | 不支持 |
| 存储桶ACL操作 | 设置存储桶ACL<br>获取设置存储桶ACL<br>删除设置存储桶ACL   | 不支持 |
| 存储桶生命周期 | 创建存储桶生命周期<br>获取存储桶生命周期<br>删除存储桶生命周期 | 不支持 |
| 目录操作 | 不单独提供接口   | 创建目录<br>查询目录<br>删除目录 |

## 升级步骤
请按照以下步骤升级 Android SDK。

**1. 更新 Android SDK**

COS XML Android SDK Android SDK 发布在 [Bintray](https://bintray.com) 的 maven 包管理平台，推荐您使用自动集成方式进行更新。

在您的项目根目录下的 build.gradle 文件中添加 maven 仓库，代码如下：

```
allprojects {

    repositories {
        ...
        // 添加如下 maven 仓库地址
        maven {
            url "https://dl.bintray.com/tencentqcloudterminal/maven"
        }
    }
}
```

在应用的根目录下的 build.gradle 中添加依赖，代码如下：

```
dependencies {
	...
    // 增加这行
    compile 'com.tencent.qcloud:cosxml:5.4.+'
}
```

当然，您也可以继续选择手动 jar 包依赖，您可以在这里 [COS XML Android SDK-release](https://github.com/tencentyun/qcloud-sdk-android/releases) 下载所有的 jar 包。

**2. 更改 SDK 鉴权方式**

在 JSON Android SDK 中您需要自己在后台计算好签名，再返回客户端使用。而在 XML SDK 使用了新的鉴权算法，在 XML Android SDK 中，强烈建议您后台接入我们的临时密钥 (STS) 方案。该方案不需要您了解签名计算过程，只需要在服务器端接入 CAM，将拿到的临时密钥返回到客户端，并设置到 SDK 中，SDK 会负责管理密钥和计算签名。临时密钥在一段时间后会自动失效，而永久密钥不会泄露。
您还可以按照不同的粒度来控制访问权限。具体的步骤请参考 [移动应用直传实践](https://cloud.tencent.com/document/product/436/9068) 以及 [临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048)。

如果您仍然采用后台手动计算签名，再返回客户端使用的方式，请注意我们的签名算法发生了改变。签名不再区分单次和多次签名，而是通过设置签名的有效期来保证安全性。请参考 [XML 请求签名](https://cloud.tencent.com/document/product/436/7778) 文档更新您签名的实现。

**3. 更改 SDK 初始化**

在 XML Android SDK 中，我们的初始化接口发生了一些变化：

* 为了区分，`CosXmlServiceConfig` 代替了 `COSClientConfig`，`CosXmlService` 代替了 `COSClient`，但他们的作用相同。
* 您需要在初始化时实例化一个密钥提供者 `QCloudCredentialProvider`，用于提供一个有效的密钥，建议使用临时密钥。

**JSON SDK 的初始化方式如下：**

```
//创建COSClientConfig对象，根据需要修改默认的配置参数
COSClientConfig config = new COSClientConfig();
//设置地域
config.setEndPoint(COSEndPoint.COS_GZ);

Context context = getApplicationContext()；
String appid =  "腾讯云注册的appid";
String peristenceId = "持久化Id";

//创建COSlient对象，实现对象存储的操作
COSClient cos = new COSClient(context,appid,config,peristenceId);
```

**XML SDK 的初始化方式如下：**

```
String appid = "1250000000";
String region = "ap-guangzhou"; 

//创建 CosXmlServiceConfig 对象，根据需要修改默认的配置参数
CosXmlServiceConfig serviceConfig = new CosXmlServiceConfig.Builder()
       .setAppidAndRegion(appid, region)
       .builder();
       
/**
 * 获取授权服务的 url 地址
 */
URL url = null; 
try {
    url = new URL("your_auth_server_url"); // 后台授权服务的 url 地址
} catch (MalformedURLException e) {
    e.printStackTrace();
}

/**
 * 初始化 {@link QCloudCredentialProvider} 对象，来给 SDK 提供临时密钥。
 */
QCloudCredentialProvider credentialProvider = new SessionCredentialProvider(new HttpRequest.Builder<String>()
                .url(url)
                .method("GET")
                .build());
                
                
CosXmlService cosXmlService = new CosXmlService(context, serviceConfig, credentialProvider);
```


**4. 更改存储桶名称和可用区域简称**

XML SDK 的存储桶名称和可用区域简称与 JSON SDK 的不同，需要您进行相应的更改。

**存储桶 Bucket**

XML Android SDK 存储桶名称由两部分组成：用户自定义字符串 和 APPID，两者以中划线“-”相连。例如 `examplebucket-1250000000`，其中 `examplebucket` 为用户自定义字符串，`1250000000` 为 APPID。

>?APPID 是腾讯云账户的账户标识之一，用于关联云资源。在用户成功申请腾讯云账户后，系统自动为用户分配一个 APPID。可通过 [腾讯云控制台](https://console.cloud.tencent.com/) 在【账号信息】查看 APPID。

在设置 Bucket 时，请参考下面的示例代码：

```
String bucket = "examplebucket-1250000000";
String cosPath = "exampleobject.doc";
String srcPath = Environment.getExternalStorageDirectory().getPath() + "/exampleobject.doc";
//上传文件
COSXMLUploadTask cosxmlUploadTask = transferManager.upload(bucket, cosPath, srcPath, uploadId);
```

**存储桶可用区域简称 Region**

XML Android SDK 的存储桶可用区域简称发生了变化，下列表格列出了不同区域在 JSON Android SDK 和 XML Android SDK 中的对应关系：

| 地域       | XML Android SDK 地域简称         | JSON Android SDK 地域简称                         |
| -------- | ------------ | ---------------------------------------- |
| 北京一区（华北） | ap-beijing-1 | tj |
| 北京       | ap-beijing   | bj |
| 上海（华东）   | ap-shanghai  | sh |
| 广州（华南）   | ap-guangzhou | gz |
| 成都（西南）   | ap-chengdu   | cd |
| 重庆       | ap-chongqing | 无 |
| 中国香港       | ap-hongkong  | hk |
| 新加坡      | ap-singapore | sgp |
| 多伦多      | na-toronto   | ca |
| 法兰克福     | eu-frankfurt | ger |
| 孟买       | ap-mumbai    | 无 |
| 首尔       | ap-seoul     | 无 |
| 硅谷       | na-siliconvalley     | 无 |
| 弗吉尼亚       | na-ashburn     | 无 |
| 曼谷       | ap-bangkok     | 无 |
| 莫斯科       | eu-moscow     | 无 |

在初始化时，请将存储桶所在区域简称设置到 `CosXmlServiceConfig` 中：

```
String appid = "1250000000";
String region = "ap-guangzhou"; 

CosXmlServiceConfig serviceConfig = new CosXmlServiceConfig.Builder()
       .setAppidAndRegion(appid, region)
       .builder();
```

**5. 更改 API**

升级到 XML SDK 之后，一些操作的 API 发生了变化，请您根据实际需求进行相应的更改。我们同时做了封装让 SDK 更加易用，具体请参考我们的示例和 [快速入门](https://cloud.tencent.com/document/product/436/12159) 文档。

API 变化有以下三点：

**1）没有单独的目录接口**

在 XML SDK 中，不再提供单独的目录接口。对象存储中本身是没有文件夹和目录的概念的，对象存储不会因为上传对象 project/a.txt 而创建一个 project 文件夹。
为了满足用户使用习惯，对象存储在控制台、COS browser 等图形化工具中模拟了「 文件夹」或「 目录」的展示方式，具体实现是通过创建一个键值为 project/，内容为空的对象，展示方式上模拟了传统文件夹。

例如：上传对象 project/doc/a.txt ，分隔符`/`会模拟「 文件夹」的展示方式，于是可以看到控制台上出现「 文件夹」project 和 doc，其中 doc 是 project 下一级「 文件夹」，并包含了 a.txt 。

因此，如果您的应用场景只是上传文件，可以直接上传即可，不需要先创建文件夹。

如果您的使用场景里面有文件夹的概念，需要提供创建文件夹的功能，您可以上传一个路径以 '/' 结尾的 0KB 文件。这样在您调用 `GetBucket` 接口时，就可以将这样的文件当做文件夹。


**2）TransferManager**

在 XML SDK 中，我们封装了上传、下载和复制操作，命名为 `TransferManager`，同时对 API 设计和传输性能都做了优化，建议您直接使用。`TransferManager`的主要特性有：

* 支持上传下载过程的暂停和恢复。
* 支持根据文件大小智能选择简单上传还是分片上传，您可以设置该判断临界。
* 支持任务状态的监听。

使用 `TransferManager`上传的示例代码：

```
// 初始化 TransferConfig
TransferConfig transferConfig = new TransferConfig.Builder().build();
/**
若有特殊要求，则可以如下进行初始化定制。如限定当文件 >= 2M 时，启用分片上传，且分片上传的分片大小为 1M, 当源文件大于 5M 时启用分片复制，且分片复制的大小为 5M。
TransferConfig transferConfig = new TransferConfig.Builder()
        .setDividsionForCopy(5 * 1024 * 1024) // 是否启用分片复制的文件最小大小
        .setSliceSizeForCopy(5 * 1024 * 1024) //分片复制时的分片大小
        .setDivisionForUpload(2 * 1024 * 1024) // 是否启用分片上传的文件最小大小
        .setSliceSizeForCopy(1024 * 1024) //分片上传时的分片大小
        .build();
*/

//初始化 TransferManager
TransferManager transferManager = new TransferManager(cosXml, transferConfig);

String bucket = "存储桶名称";
String cosPath = "对象键"; // 即存储到 COS 上的绝对路径,格式如 cosPath = "exampleobject.doc";
String srcPath = "本地文件的绝对路径"; // 如 srcPath=Environment.getExternalStorageDirectory().getPath() + "/exampleobject.doc";
String uploadId = "分片上传的UploadId";//用于续传，若无，则为null.
//上传文件
COSXMLUploadTask cosxmlUploadTask = transferManager.upload(bucket, cosPath, srcPath, uploadId);
//设置上传进度回调
cosxmlUploadTask.setCosXmlProgressListener(new CosXmlProgressListener() {
            @Override
            public void onProgress(long complete, long target) {
                float progress = 1.0f * complete / target * 100;
                Log.d("TEST",  String.format("progress = %d%%", (int)progress));
            }
        });
//设置返回结果回调
cosxmlUploadTask.setCosXmlResultListener(new CosXmlResultListener() {
            @Override
            public void onSuccess(CosXmlRequest request, CosXmlResult result) {
                Log.d("TEST",  "Success: " + result.printResult());
            }

            @Override
            public void onFail(CosXmlRequest request, CosXmlClientException exception, CosXmlServiceException serviceException) {
                Log.d("TEST",  "Failed: " + (exception == null ? serviceException.getMessage() : exception.toString()));
            }
        });
//设置任务状态回调, 可以查看任务过程
cosxmlUploadTask.setTransferStateListener(new TransferStateListener() {
            @Override
            public void onStateChanged(TransferState state) {
                Log.d("TEST", "Task state:" + state.name());
            }
        });

/**
若有特殊要求，则可以如下操作：
 PutObjectRequest putObjectRequest = new PutObjectRequest(bucket, cosPath, srcPath);
 putObjectRequest.setRegion(region); //设置存储桶所在的地域
 putObjectRequest.setSign(600); //设置签名sign有效期
 putObjectRequest.setNeedMD5(true); //是否启用Md5校验
 COSXMLUploadTask cosxmlUploadTask = transferManager.upload(putObjectRequest, uploadId);
*/

//取消上传
cosxmlUploadTask.cancel();


//暂停上传
cosxmlUploadTask.pause();

//恢复上传
cosxmlUploadTask.resume();
```

**3）新增 API**

XML Android SDK 新增 API，您可根据需求进行调用。包括：

* 存储桶的操作，如 PutBucketRequest、GetBucketRequest、ListBucketRequest 等。
* 存储桶 ACL 的操作，如 PutBucketACLRequest、GetBucketACLRequest 等。
* 存储桶生命周期的操作，如 PutBucketLifecycleRequest、GetBucketLifecycleRequest 等。

具体请参考我们的 [Android SDK 快速入门](https://cloud.tencent.com/document/product/436/12159) 文档。
