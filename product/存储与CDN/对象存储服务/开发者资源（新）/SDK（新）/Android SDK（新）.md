### 开发准备

#### SDK 获取

对象存储服务的 Android SDK 的下载地址：[Android SDK](http://mccdn.qcloud.com/static/archive/5cabeb4ad4dc5652ba74302e3b8da190/qcloud-android-v1.1.3.332.zip) 。

更多示例可参考Demo：[Android SDK Demo APK](http://mccdn.qcloud.com/static/archive/0f2557ff9e7d3dfa09122fba07a76d5d/CloudDemo_1.1.3.332_4478_debug.apk) 以及 [Android SDK Demo 源码](http://mccdn.qcloud.com/static/archive/7ec66ae5a9104f94f597cfbb59885665/QloudDemoApp.zip)。



#### 开发准备

1. SDK 支持 Android 2.2 及以上版本的手机系统；
2. 手机必须要有网络（GPRS、3G或 WIFI 网络等）；
3. 手机可以没有存储空间，但会使部分功能无法正常工作；
4. 从控制台获取APP ID、SecretID、SecretKey，详情参考[权限控制](/doc/product/227/权限控制)。






#### SDK 配置

##### SDK导入

解压 SDK 包，将其中的 libs 目录合并到本地工程libs目录：

![加入so文件](//mccdn.qcloud.com/static/img/fc78c7bdd22a086a6d8d95aaa1cc59d9/image.png)

**注意：**如果工程中存在 armeabi-v7a/armeabi-v8a目录，需将上述.so 文件拷贝一份到此目录下，否则由于 android 系统的问题在安装 apk 后会找不到 so 。

**注意：**若项目需要兼容 x86 ，则将上述 so 复制一份放入 x86 目录即可。

配置工程导入下列 jar 包：

- upload.jar
- download.jar
- wup-1.0.0-SNAPSHOT.jar

**注意：**可根据业务功能所需，对 upload/download 包进行选择性导入。

##### SDK 配置

SDK 需要网络访问相关的一些权限，需要在 AndroidManifest.xml 中增加如下权限声明：

```html
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.READ_PHONE_STATE"/>
<uses-permission android:name="android.permission.WAKE_LOCK"/>
<uses-permission android:name="android.permission.MOUNT_UNMOUNT_FILESYSTEMS" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
```



### 生成签名

**签名类型：**

| 类型   | 含义            |
| ---- | ------------- |
| 多次有效 | 有效时间内多次始终有效   |
| 单次有效 | 与资源URL绑定，一次有效 |

**签名获取：**

SDK 中用到的 SIGN，推荐使用 [服务器端SDK](/doc/product/227/SDK%20概览)，并由移动端向业务服务器请求。SIGN 的具体生成和使用请参照 [签名算法](/doc/product/227/签名算法) 。



### 目录操作

#### 初始化

进行目录操作之前需要先实例化 UploadManager 对象。

##### *UploadManager* 原型：

```java
public UploadManager(Context context, String appId, FileType fileType, 
                     String persistenceId)
```

##### 参数说明

| 参数名称          | 类型       | 是否必填 | 说明                                       |
| :------------ | :------- | :--- | :--------------------------------------- |
| context       | Context  | 是    |                                          |
| appId         | String   | 是    | 腾讯云APP ID                                |
| fileType      | FileType | 是    | 业务类型，COS服务指明为：FileType.File              |
| persistenceId | String   | 否    | 持久化 ID，每个 UploadManager 需设置一个唯一的 ID 用于持久化保存未完成任务 列表，以便应用退出重进后能够继续进行上传；传入为 Null，则不会进行持久化保存 |

##### 示例

```java
import com.tencent.upload.UploadManager;
import com.tencent.upload.Const.FileType;

UploadManager fileUploadMgr = null;
fileUploadMgr = new UploadManager(this, "10000002", FileType.File, "qcloudobject");
```



#### 目录创建

调用此接口可在指定的 bucket 下创建目录，具体步骤如下：

1. 实例化 DirCreateTask 对象；
2. 调用 UploadManager  的 sendCommand 方法，传入 DirCreateTask  对象。

##### *DirCreateTask* 原型

```java
public DirCreateTask (FileType fileType, String bucket, String path, 
                      String bizAttr, IListener listener)
```

#####参数说明

| 参数名称     | 类型        | 是否必填 | 说明                           |
| :------- | :-------- | :--- | :--------------------------- |
| fileType | FileType  | 是    | 业务类型，COS 服务设置为：FileType.File |
| bucket   | String    | 是    | 目录所属bucket 名称                |
| path     | String    | 是    | 需要创建目录的路径                    |
| bizAttr  | String    | 否    | 目录绑定的属性信息，由业务维护              |
| listener | IListener | 是    | 结果回调                         |

#####示例

```java
import com.tencent.upload.task.impl.DirCreateTask;

DirCreateTask filetask = null;
filetask = new DirCreateTask(FileType.File, BUCKETNAME, DIRPATH, ATTRS, new DirCreateTask.IListener() {
	@Override
	public void onSuccess(final DirCreateTask.CmdTaskRsp result) {
		// 创建成功
	}
	@Override
	public void onFailure(final int ret, final String msg) {
		// 创建失败
	}
});

filetask.setAuth(SIGN);
fileUploadMgr.sendCommand(filetask);
```



#### 目录属性更新

通过此接口更新业务的自定义属性字段，具体步骤如下：

1. 实例化 ObjectUpdateTask 对象；
2. 调用 UploadManager  的 sendCommand 方法，传入 ObjectUpdateTask 对象。

##### *ObjectUpdateTask* 原型

```java
public ObjectUpdateTask(FileType fileType, String bucket, String path, 
                        String attr, int type, IListener listener)
```

##### 参数说明

| 参数名称     | 类型        | 是否必填 | 说明                            |
| :------- | :-------- | :--- | :---------------------------- |
| fileType | FileType  | 是    | 业务类型，COS 服务统一写为 FileType.File |
| bucket   | String    | 是    | 目录所属bucket 名称                 |
| path     | String    | 是    | 需要更新的目录路径                     |
| attr     | String    | 否    | 新的目录绑定的属性信息                   |
| type     | String    | 是    | 对象类型，目录更新设置为：Dentry.DIR       |
| listener | IListener | 是    | 结果回调                          |

##### 示例

```java
import com.tencent.upload.task.impl.ObjectUpdateTask;

ObjectUpdateTask filetask = null;
filetask = new ObjectUpdateTask(FileType.File, BUCKETNAME, DIRPATH, Dentry.DIR, ATTRS, new ObjectUpdateTask.IListener() {
	@Override
	public void onSuccess(ObjectDeleteTask.CmdTaskRsp result) {
		// 更新成功
	}
	
	@Override
	public void onFailure(final int ret, final String msg) {
		// 更新成功
	}
});

filetask.setAuth(SIGN);
fileUploadMgr.sendCommand(filetask);
```



#### 目录属性查询

通过此接口来查询目录的详细属性，具体步骤如下：

1. 实例化 ObjectStatTask 对象；
2. 调用 UploadManager  的 sendCommand 方法，传入 ObjectStatTask 对象。

##### *ObjectStatTask* 原型

```java
public ObjectStatTask(FileType fileType, String bucket, String path, 
                      int type, IListener listener);
```

##### 参数说明

| 参数名称     | 类型        | 是否必填 | 说明                           |
| :------- | :-------- | :--- | :--------------------------- |
| fileType | FileType  | 是    | 业务类型，COS 服务设置为：FileType.File |
| bucket   | String    | 是    | Bucket 名称                    |
| path     | String    | 是    | 需要查询的目录路径                    |
| type     | String    | 是    | 对象类型，目录属性查询时设置为：Dentry.DIR   |
| listener | IListener | 是    | 结果回调                         |

##### 示例

```java
import com.tencent.upload.task.impl.ObjectStatTask;

ObjectStatTask filetask = null;
filetask = new ObjectStatTask(FileType.File, BUCKETNAME, DIRPATH, Dentry.DIR, 
new ObjectStatTask.IListener() {
	@Override
	public void onSuccess(final ObjectStatTask.CmdTaskRsp result) {
		// 查询成功
	}

	@Override
	public void onFailure(final int ret, final String msg) {
		// 查询失败
	}
});

filetask.setAuth(SIGN);
fileUploadMgr.sendCommand(filetask);
```



#### 目录删除

调用此接口，进行指定 bucket 下目录的删除，如果目录中存在有效文件或目录，将不能删除。具体步骤如下：

1. 实例化 ObjectDeleteTask 对象；
2. 调用 UploadManager  的 sendCommand 方法，传入 ObjectDeleteTask 对象。

##### *ObjectDeleteTask* 原型

```java
public ObjectDeleteTask(FileType fileType, String bucket, String path, 
                        int type, IListener listener)
```

##### 参数说明

| 参数名称     | 类型        | 是否必填 | 说明                            |
| :------- | :-------- | :--- | :---------------------------- |
| fileType | FileType  | 是    | 业务类型，COS 服务设置为： FileType.File |
| bucket   | String    | 是    | 目录所属 bucket 名称                |
| path     | String    | 是    | 要删除的目录路径                      |
| type     | int       | 是    | 对象类型，删除目录时设置为：Dentry.DIR      |
| listener | IListener | 是    | 结果回调                          |

##### 示例

```java
import com.tencent.upload.task.impl.ObjectDeleteTask;

ObjectDeleteTask filetask= null;
filetask = new ObjectDeleteTask(FileType.File, BUCKETNAME, DIRPATH, Dentry.DIR, new ObjectDeleteTask.IListener() {
	@Override
	public void onSuccess(ObjectDeleteTask.CmdTaskRsp result) {
		// 删除成功
	}

  	@Override
	public void onFailure(final int ret, final String msg) {
		// 删除失败
	}
});

filetask.setAuth(SIGN);
fileUploadMgr.sendCommand(filetask);
```



#### 列举目录中的文件和目录

通过此接口查询目录下的文件、目录信息，具体步骤如下：

1. 实例化 DirListTask 对象；
2. 调用 UploadManager  的 sendCommand 方法，传入 DirListTask 对象。

##### *DirListTask* 原型

```java
public DirListTask (FileType fileType, String bucket, String path, int num, 
                    int pattern, boolean order, String content, IListener listener)
```

##### 参数说明

| 参数名称     | 类型        | 是否必填 | 说明                                       |
| :------- | :-------- | :--- | :--------------------------------------- |
| fileType | FileType  | 是    | 业务类型，COS 服务设置为： FileType.File            |
| bucket   | String    | 是    | 目录所属 bucket 名称                           |
| path     | String    | 是    | 请求的目录路径                                  |
| num      | int       | 是    | 拉取记录数目                                   |
| pattern  | int       | 是    | 拉取方式，Dentry.ListBoth - 目录和文件都拉取，Dentry.ListDirOnly - 只拉取目录，Dentry.ListFileOnly - 只拉取文件 |
| order    | boolean   | 是    | true - 反序，false - 正序                     |
| content  | String    | 否    | 首次拉取必须清空，拉取下一页是需要传入上一次拉取时返回的content      |
| listener | IListener | 是    | 结果回调                                     |

##### 示例

```java
import com.tencent.upload.task.impl.DirListTask;

// 第一次拉取目录传入空，拉取path下一页时填入上一次返回的result.content
String content = ""; 
DirListTask filetask = null;
filetask = new DirListTask(FileType.File, BUCKETNAME, DIRPATH, 10, Dentry.ListBoth, false, content, new DirListTask.IListener() {
	@Override
	public void onSuccess(final DirCreateTask.CmdTaskRsp result) {
		ArrayList<Dentry> dirList = result.inodes;
		String strEntryList = "";
		for (Dentry entry : dirList) {
			strEntryList += entry.path + "\n";
		}
		if (result.hasMore) {
			// 存在下一页保存当前页的状态信息
			String content = result.content;
		}
		// 拉取成功
    }
	
    @Override
	public void onFailure(final int ret, final String msg) {
		// 拉取失败
	}
});

filetask.setAuth(SIGN);
fileUploadMgr.sendCommand(filetask);
```



#### 列举目录下指定前缀文件&目录

通过此接口查询目录下的指定前缀的文件和目录，具体步骤如下：

1. 实例化 DirListTask 对象；
2. 调用  DirListTask 的 setPrefixSearch 方法设置前缀查询开关；
3. 调用 fileUploadMgr 的 sendCommand 方法，传入 DirListTask  对象。

##### *DirListTask* 原型

```java
public DirListTask (FileType fileType, String bucket, String path, int num, 
                    int pattern, boolean order, String content, IListener listener)
//前缀查询开关
public void setPrefixSearch(boolean prefixSearch);
```

##### 参数说明

| 参数名称     | 类型        | 是否必填 | 说明                                       |
| :------- | :-------- | :--- | :--------------------------------------- |
| fileType | FileType  | 是    | 业务类型，COS 服务统一写为 FileType.File            |
| bucket   | String    | 是    | 目录所属 bucket 名称                           |
| path     | String    | 是    | 搜索的目录路径                                  |
| num      | int       | 是    | 拉取记录数目设定                                 |
| pattern  | int       | 是    | 拉取方式，Dentry.ListBoth - 目录和文件都拉取，Dentry.ListDirOnly - 只拉取目录，Dentry.ListFileOnly - 只拉取文件 |
| order    | boolean   | 是    | true - 反序，false - 正序                     |
| content  | String    | 否    | 首次拉取必须清空，拉取下一页是需要传入上一次拉取时返回的 content     |
| listener | IListener | 是    | 结果回调                                     |

| 参数名称         | 类型      | 是否必填 | 说明                               |
| :----------- | :------ | :--- | :------------------------------- |
| prefixSearch | boolean | 是    | true - 开启前缀搜索开关，false - 关闭前缀搜索开关 |

##### 示例

```java
import com.tencent.upload.task.impl.DirListTask;

// 第一次拉取目录传入空，拉取path下一页时填入result.content
String content = ""; 
DirListTask filetask = null;
filetask = new DirListTask(FileType.File, BUCKETNAME, DIRPATH, 10, Dentry.ListBoth, false, content, new DirListTask.IListener() {
	@Override
	public void onSuccess(final DirCreateTask.CmdTaskRsp result) {
		ArrayList<Dentry> dirList = result.inodes;
		String strEntryList = "";
		for (Dentry entry : dirList) {
			strEntryList += entry.path + "\n";
		}
		if (result.hasMore) {
			// 存在下一页保存当前页的状态信息
			String content = result.content;
		}
		// 拉取成功
	}

	@Override
	public void onFailure(final int ret, final String msg) {
		// 拉取失败
	}
});

filetask.setPrefixSearch(true);
filetask.setAuth(SIGN);
fileUploadMgr.sendCommand(filetask);
```



### 文件操作

#### 初始化

进行文件操作之前需要先实例化 UploadManager 对象。

##### *UploadManager* 原型

```java
public UploadManager(Context context, String appId, FileType fileType, 
                     String persistenceId)
```

##### 参数说明

| 参数名称          | 类型       | 是否必填 | 说明                                       |
| :------------ | :------- | :--- | :--------------------------------------- |
| context       | Context  | 是    |                                          |
| appId         | String   | 是    | 腾讯云APP ID                                |
| fileType      | FileType | 是    | 业务类型，COS服务指明为：FileType.File              |
| persistenceId | String   | 否    | 持久化 ID，每个 UploadManager 需设置一个唯一的 ID 用于持久化保存未完成任务						 列表，以便应用退出重进后能够继续进行上传；传入为 Null，则不会进行持久化						 保存 |

##### 示例

```java
import com.tencent.upload.UploadManager;
import com.tencent.upload.Const.FileType;

UploadManager fileUploadMgr = null;
fileUploadMgr = new UploadManager(this, "10000002", FileType.File, "qcloudobject");
```



#### 文件上传

调用者可通过此接口进行本地文件上传操作，具体步骤如下：

1. 实例化  FileUploadTask 对象；
2. 调用 UploadManager 的 upload 方法，将 FileUploadTask  对象传入。

##### *FileUploadTask* 原型

```java
public FileUploadTask(String bucket, String srcFilePath, String destFilePath, 
                      String bizAttr, IUploadTaskListener listener);

public interface IUploadTaskListener {
	void onUploadSucceed(FileInfo result);
	void onUploadFailed(int errorCode, String errorMsg);
	void onUploadProgress(long totalSize, long recvDataSize);
	void onUploadStateChange(TaskState state); 
}
```

##### 参数说明

| 参数名称         | 类型                  | 是否必填 | 说明           |
| :----------- | :------------------ | :--- | :----------- |
| bucket       | String              | 是    | 目标 bucket 名称 |
| srcFilePath  | String              | 是    | 本地绝对路径       |
| destFilePath | String              | 是    | 远程相对路径       |
| bizAttr      | String              | 否    | 文件属性，业务维护    |
| listener     | IUploadTaskListener | 是    | 上传回调监听器      |

##### 回调接口说明

| 方法名称                                     | 说明       |
| :--------------------------------------- | :------- |
| onUploadSucceed(FileInfo result);        | 上传成功     |
| onUploadFailed(int errorCode, String errorMsg); | 上传失败     |
| onUploadProgress(long totalSize, long recvDataSize); | 上传进度     |
| onUploadStateChange(TaskState state);    | 上传任务状态变化 |

##### 示例

```java
import com.tencent.upload.task.impl.FileUploadTask;
import com.tencent.upload.task.IUploadTaskListener;

FileUploadTask task = new FileUploadTask(BUCKETNAME, FILEPATH, TARGETDIR, ATTRS, new IUploadTaskListener() {
	@Override
	public void onUploadSucceed(final FileInfo result) {
		// 上传成功
	}

	@Override
	public void onUploadStateChange(TaskState state) {
    	// 上传状态变化
	}

	@Override
	public void onUploadProgress(long totalSize, long sendSize) {
		// 上传进度
	}

	@Override
	public void onUploadFailed(final int errorCode, final String errorMsg) {
		// 上传失败
	}
});

filetask.setAuth(SIGN);
fileUploadMgr.upload(task);
```



#### 文件属性更新

用于目录业务自定义属性的更新，调用者可以通过此接口更新业务的自定义属性字段，具体步骤如下：

1. 实例化 ObjectUpdateTask 对象；
2. 调用 UploadManager 的 sendCommand 方法，将 ObjectUpdateTask 对象传入。

##### *ObjectUpdateTask* 原型

```java
public ObjectUpdateTask(FileType fileType, String bucket, String path, 
                        String attr, int type, IListener listener)
```

##### 参数说明

| 参数名称     | 类型        | 是否必填 | 说明                          |
| :------- | :-------- | :--- | :-------------------------- |
| fileType | FileType  | 是    | 业务类型，COS服务设置为：FileType.File |
| bucket   | String    | 是    | 文件所属 bucket名称               |
| path     | String    | 是    | 需要更新的文件路径                   |
| attr     | String    | 否    | 新的文件绑定属性                    |
| type     | String    | 是    | 对象类型，文件属性更新时设置为：Dentry.FILE |
| listener | IListener | 是    | 结果回调                        |

##### 示例

```java
import com.tencent.upload.task.impl.ObjectUpdateTask;

ObjectUpdateTask filetask = null;
filetask = new ObjectUpdateTask (FileType.File, BUCKETNAME, FILEPATH,  Dentry.FILE, ATTRS, new ObjectUpdateTask.IListener() {
	@Override
	public void onSuccess(ObjectDeleteTask.CmdTaskRsp result) {
		// 更新成功
	}
	
	@Override
	public void onFailure(final int ret, final String msg) {
		// 更新失败
	}
});

filetask.setAuth(SIGN);
fileUploadMgr.sendCommand(filetask);
```



#### 文件属性查询

用于文件的查询，调用者可以通过此接口查询文件的各项属性信息，具体步骤如下：

1. 实例化 ObjectStatTask 对象；
2. 调用 UploadManager 的 sendCommand 方法，将 ObjectStatTask 对象传入。

##### *ObjectStatTask* 原型

```java
public ObjectStatTask(FileType fileType, String bucket, String path, 
                      int type, IListener listener);
```

#####参数说明

| 参数名称     | 类型        | 是否必填 | 说明                           |
| :------- | :-------- | :--- | :--------------------------- |
| fileType | FileType  | 是    | 业务类型，COS 服务设置为：FileType.File |
| bucket   | String    | 是    | 文件所属 bucket名称                |
| path     | String    | 是    | 需要查询的文件路径                    |
| type     | String    | 是    | 对象类型，文件属性查询时设置为：Dentry.FILE  |
| listener | IListener | 是    | 结果回调                         |

##### 示例

```java
import com.tencent.upload.task.impl.ObjectStatTask;

ObjectStatTask filetask = null;
filetask = new ObjectStatTask(FileType.File, BUCKETNAME, FILEPATH, Dentry.FILE, new ObjectStatTask.IListener() {
	@Override
	public void onSuccess(final ObjectStatTask.CmdTaskRsp result) {
		// 查询成功
	}

	@Override
	public void onFailure(final int ret, final String msg) {
		// 查询失败
	}
});

filetask.setAuth(SIGN);
fileUploadMgr.sendCommand(filetask);
```



#### 文件删除

调用此接口可进行文件的删除操作，具体步骤如下：

1. 实例化 ObjectDeleteTask 对象；
2. 调用 UploadManager 的 sendCommand 方法，将 ObjectDeleteTask 对象传入。

##### *ObjectDeleteTask*原型

```java
public ObjectDeleteTask(FileType fileType, String bucket, String path, 
                        int type, IListener listener)
```

##### 参数说明

| 参数名称     | 类型        | 是否必填 | 说明                          |
| :------- | :-------- | :--- | :-------------------------- |
| fileType | FileType  | 是    | 业务类型，COS服务设置为：FileType.File |
| bucket   | String    | 是    | 文件所属 bucket名称               |
| path     | String    | 是    | 删除文件的路径                     |
| type     | int       | 是    | 对象类型，删除文件时设置为：Dentry.FILE   |
| listener | IListener | 是    | 结果回调                        |

##### 示例

```java
import com.tencent.upload.task.impl.ObjectDeleteTask;

ObjectDeleteTask filetask= null;
filetask = new ObjectDeleteTask(FileType.File, BUCKETNAME, FILEPATH, Dentry.FILE, new ObjectDeleteTask.IListener() {
	@Override
	public void onSuccess(ObjectDeleteTask.CmdTaskRsp result) {
		// 删除成功
	}

  	@Override
	public void onFailure(final int ret, final String msg) {
		// 删除失败
	}
});

filetask.setAuth(SIGN);
fileUploadMgr.sendCommand(filetask);
```



### 对象下载

#### 初始化

在使用对象下载器时，需要先实例化一个Downloader对象，并对下载器的一些属性进行配置。

##### *Downloader*原型

```java
public Downloader(Context context, String appid, String persistenceId);
```

##### 参数说明

| 参数名称          | 类型      | 是否必填 | 说明           |
| :------------ | :------ | :--- | :----------- |
| context       | Context | 是    |              |
| appid         | String  | 是    | 腾讯云注册的APP ID |
| persistenceId | String  | 否    | 资源的持久化ID     |

##### 示例

```java
Downloader downloader = new Downloader(this, "10000002","qcloudobject");
```



**下载并发数设置：**可以指定下载器最大并发数。

方法原型：

```java
public void setMaxConcurrent(int count);
```

示例：

```java
downloader.setMaxConcurrent(10);
```



**长连接/断点续传设置：**下载器提供开关，可以设定是否开启长连接和断点续传功能。

**方法原型**

```java
// enable True-支持断点续传，False-不支持
public void enableHTTPRange(boolean enable);
// enable Ture-支持HTTP长连接，False-不支持
public void enableKeepAlive(boolean keepalive);
```

##### **示例**

```java
downloader.enableHTTPRange(true);
downloader.enableKeepAlive(true);
```



#### 对象下载器

对已知URL的资源进行下载，异步模式进行。

##### 方法原型

```java
public boolean download(String url, DownloadListener listener);

public interface DownloadListener{
	public void onDownloadSucceed(String url, DownloadResult result);
	public void onDownloadFailed(String url, DownloadResult result);
	public void onDownloadCanceled(String url);
	public void onDownloadProgress(String url, long totalSize, float progress);
}
```

##### 参数说明

| 参数名称     | 类型               | 是否必填 | 说明         |
| :------- | :--------------- | :--- | :--------- |
| url      | String           | 是    | 请求资源的URL地址 |
| listener | DownloadListener | 是    | 回调结果       |

##### 监听器接口说明

| 方法名称                                     | 说明   |
| :--------------------------------------- | :--- |
| onDownloadSucceed(String url, DownloadResult result); | 下载成功 |
| onDownloadFailed(String url, DownloadResult result); | 下载失败 |
| onDownloadCanceled(String url);          | 取消下载 |
| onDownloadProgress(String url, long totalSize, float progress); | 下载进度 |

##### 示例

```java
DownloadListener listener = new DownloadListener() {
	@Override
	public void onDownloadSucceed(String url, DownloadResult result) {
		// 下载成功
	}
	
	@Override
	public void onDownloadProgress(String url, long totalSize, float progress) {
		// 下载进度
	}
	
	@Override
	public void onDownloadFailed(String url, DownloadResult result) {
		// 下载失败
	}
	
	@Override
	public void onDownloadCanceled(String url) {
		// 下载被取消
	}
};

downloader.download(URL,  listener);
```



#### 取消下载任务

取消对指定URL资源的下载任务，或取消所有 downloader 开启的下载任务。

##### 方法原型

```java
//取消指定URL资源下载任务
public void cancel(String url, DownloadListener listener);
//取消所有下载任务
public void cancelAll();
```

##### 示例

```java
downloader.cancel(URL,  listener);
downloader.cancelAll();
```