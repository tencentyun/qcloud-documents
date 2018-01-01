## 应用云 Storage 服务 Android接入指南

### 准备工作

在开始使用应用云 Storage 服务前，您需要：

 1. 新建或者打开一个 Android 项目。
 2. 配置了应用云服务框架，配置方式请参见[应用云服务框架 Android 配置指南](https://github.com/tencentyun/qcloud-documents/blob/master/product/%E5%AD%98%E5%82%A8%E4%B8%8ECDN/_Drafts/ApplicationBoard/%E9%9B%86%E6%88%90%E6%8C%87%E5%8D%97/Core/Android/%E5%BA%94%E7%94%A8%E4%BA%91%20%E6%9C%8D%E5%8A%A1%E6%A1%86%E6%9E%B6%20Android%E6%8E%A5%E5%85%A5%E6%8C%87%E5%8D%97.md.md)。

### 集成 Storage 服务到你的应用

#### 通过远程依赖集成 (<font color='red'>推荐</font>)

在你的应用级 build.gradle（\<project\>/\<app-module\>/build.gradle）添加应用云 Storage 的依赖：

```
dependencies {
    //增加这行
    compile 'com.tencent.tac:storage:1.0.0'
}
```

#### 本地集成

1. 下载 Storage 服务资源打包文件，并解压。下载资源文件请点击[这里]()。
2. 将资源文件中的 libs 目录拷贝到您的 module 的根目录下。
4. 打开您自己 module 下的 AndroidManifest.xml 文件，然后按照下载的资源文件中的 AndroidManifest.xml 作为范例来修改。

### 配置 Storage 服务

Storage 服务无法直接使用默认配置，你必须提供一个返回有效签名的后台服务器接口。请通过以下方式配置该接口，SDK会在需要的时候，自动调用该接口获取需要的签名。请注意，服务启动之后配置将不允许被修改。

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

### 文件引用

#### 创建引用

要上传、下载或删除文件，或要获取或更新文件的元数据，请创建引用。引用可以看作是指向云端文件的指针。

```
TACStorageService storage = TACStorageService.getInstance();

TACStorageReference reference = storage.rootReference();
```

上面的代码是获取整个bucket的根目录的引用，如果想要创建某个子文件的引用，可以使用：

```
TACStorageReference reference = storage.referenceWithPath('images');
```

#### 引用导航

引用可以向上或者向下导航：

```
// 获取根节点的引用
TACStorageReference rootRef = reference.root();

// 获得父节点的引用
TACStorageReference parentRef = reference.parent();

// 获取当前引用下某个子节点的引用
TACStorageReference childRef = reference.child('imageA.jpg');

```

#### 引用属性

你可以使用 getPath()、getName() 和 getBucket() 方法检查引用，以便更好地了解它们指向的文件。

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

### 上传文件

你可以将内存中的数据，本地文件路径，或者是数据流传输到远程Storage中。

```
StorageReference storageRef = storage.referenceWithPath('images/imageA.jpg');

// 通过内存中的数据上传文件
byte[] tmpData = new byte[200];
reference.putData(tmpData, TACMetadata));

// 上传本地文件
File localFile = new File("path/to/file");
reference.putData(Uri.fromFile(localFile), TACMetadata);

// 上传数据流
InputStream stream = new FileInputStream(new File("path/to/file"));
reference.putStream(stream, TACMetadata);
```
### 下载文件

你可以调用 downloadToFile 方法，将一个远程文件下载到本地：

```
TACStorageReference reference = storage.referenceWithPath("/tac_test/multipart");
Uri fileUri = Uri.fromFile(new File(getExternalCacheDir() + File.separator + "local_tmp"));
reference.downloadToFile(fileUri);
```

### 删除文件

你可以调用 delete 方法，删除一个远程文件：

```
TACStorageReference reference = storage.referenceWithPath("/tac_test/multipart");
reference.delete();
```

### 添加任务监听

你可以调用 TACStorageTask 的 addResultListener 方法，监听任务结果：

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

针对下载和上传任务，addUploadListener 方法可以监听数据的进度：

```
TACStorageUploadTask uploadTask = reference.putData(tmpData, TACMetadata));
uploadTask.addUploadListener(new StorageProgressListener<TACStorageTaskSnapshot>() {
            @Override
            public void onProgress(TACStorageTaskSnapshot snapshot) {
                Log.i("QCloudStorage", "progress = " + snapshot.getBytesTransferred() + "," +
                        snapshot.getTotalByteCount());
            }
        });
```

