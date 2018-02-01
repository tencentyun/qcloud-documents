## 应用云 Storage 服务 Android接入指南

## 文件引用

### 创建引用

要上传、下载或删除文件，或要获取或更新文件的元数据，请创建引用。引用可以看作是指向云端文件的指针。

```
TACStorageService storage = TACStorageService.getInstance();

TACStorageReference reference = storage.rootReference();
```

上面的代码是获取整个bucket的根目录的引用，如果想要创建某个子文件的引用，可以使用：

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

## 上传文件

### 上传文件

你可以将内存中的数据，本地文件路径，或者是数据流传输到远程Storage中。

```
StorageReference storageRef = storage.referenceWithPath('images/imageA.jpg');

// 通过内存中的数据上传文件
byte[] tmpData = new byte[200];
reference.putData(tmpData, null));

// 上传本地文件
File localFile = new File("path/to/file");
reference.putData(Uri.fromFile(localFile), null);

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
reference.putData(Uri.fromFile(localFile), metadata);

// 上传数据流，并带上metadata
reference.putStream(stream, metadata);
```


### 管理上传

如果你想要管理上传的行为，可以调用 pause 和 resume，注意暂停和继续只针对大文件的上传有效：

```
TACStorageUploadTask uploadTask = reference.putData(tmpData, TACMetadata));

// 暂停任务
uploadTask.pause();

// 继续任务
uploadTask.resume();

```

### 通过重新启动进程继续上传

对于本地的大文件上传，我们支持断点续传，您可以继续下上传的 uploadId，在下次app启动的时候从上次停止的地方上传，而不会重头开始，节省您的带宽和时间。

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
reference.putFile(Uri.fromFile(uploadFile), null, uploadId)
```

## 下载文件

你可以调用 downloadToFile 方法，将一个远程文件下载到本地：

```
TACStorageReference reference = storage.referenceWithPath("/tac_test/multipart");
Uri fileUri = Uri.fromFile(new File(getExternalCacheDir() + File.separator + "local_tmp"));
reference.downloadToFile(fileUri);
```

## 删除文件

你可以调用 delete 方法，删除一个远程文件：

```
TACStorageReference reference = storage.referenceWithPath("/tac_test/multipart");
reference.delete();
```

## 添加任务结果监听

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

## 添加任务进度监听

针对下载和上传任务，addProgressListener 方法可以监听数据的进度：

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

您可以调用 cancel 方法取消任务，注意一些已经开始运行的任务可能无法取消：

```
TACStorageReference reference = tacStorageService.referenceWithPath("/tac_test/multipart3");
File uploadFile = createFile(10 * 1024 * 1024);
TACStorageUploadTask uploadTask = reference.putFile(Uri.fromFile(uploadFile), null);

uploadTask.cancel();
```