>!您目前查阅的是历史版本 SDK 文档，已不再更新和维护，我们建议您查阅新版 [SDK 文档](https://cloud.tencent.com/document/product/436/6474)。

## 开发准备

### SDK 获取

GitHub 地址：[Android SDK](https://github.com/tencentyun/cos_android_sdk)。

更多示例可参考Demo：[Android SDK Demo](https://github.com/tencentyun/cos_android_sdk/tree/master/Demo)。 
（本版本 SDK 基于 JSON API 封装组成）

### 开发准备

1. SDK 支持 Android 2.2 及以上版本的手机系统。
2. 手机必须要有网络（GPRS、3G 或 WI-FI 网络等）。
3. 手机可以没有存储空间，但会使部分功能无法正常工作。
4. 从控制台获取 APPID、SecretId、SecretKey，详情参考权限控制。

### SDK 配置

配置工程导入下列 jar 包：

- cos-android-sdk1.4.3.18.jar
- okhttp-3.2.0.jar
- okio-1.6.0.jar
- sha1utils.jar
- jniLibs（对应的 sha1 值计算的 .so 库）

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

## 初始化

进行操作之前需要实例化COSClient 和 COSClientConfig；

#### 实例化 COSClientConfig

调用 COSClientConfig() 方法实例化 COSClientConfig 对象。

```java
COSClientConfig config = new COSClientConfig();
```

#### 配置 COSClientConfig

|                      方法                       |                           方法描述                           |
| :---------------------------------------------: | :----------------------------------------------------------: |
|          setEndPoint(String endPoint)           | 设置园区：华南 "gz"， 华北 "tj"， 华东"sh"，新加坡"sgp"。SDK 中默认为华南地区 |
|   setConnectionTimeout(int connectionTimeout)   |                    连接超时设置   (毫秒)                     |
|       setSocketTimeout(int socketTimeout)       |                  读取超时设置      （毫秒）                  |
| setMaxConnectionsCount(int maxConnectionsCount) |                        并发数大小设置                        |
|       setMaxRetryCount(int maxRetryCount)       |                       失败请求重试次数                       |
|      setHttpProtocol(String httpProtocol)       | 设置请求协议类型：默认为http请求，即"http://"; 若为https请求,则为 "https://" |

#### 实例化 COSClient

调用 COSClient（Context context, String appid, COSClientConfig config, String peristenceId) 方法实例化 COSClient 对象。

#### 参数说明

| 参数名称      | 类型            | 是否必填 | 参数描述                                                     |
| :------------ | :-------------- | :------- | :----------------------------------------------------------- |
| context       | Context         | 是       | 上下文                                                       |
| appid         | String          | 是       | 腾讯云注册的APPID                                            |
| config        | COSClientConfig | 否       | 配置设置                                                     |
| persistenceId | String          | 否       | 持久化 ID，每个 COSClient 需设置一个唯一的 ID 用于持久化保存未完成任务 列表，以便应用退出重进后能够继续进行上传；传入为 Null，则不会进行持久化保存 |

#### 示例

```Java
//创建COSClientConfig对象，根据需要修改默认的配置参数
COSClientConfig config = new COSClientConfig();
//设置园区
config.setEndPoint(COSEndPoint.COS_GZ);

Context context = getApplicationContext()；
String appid =  "腾讯云注册的appid";
String peristenceId = "持久化Id";

//创建COSlient对象，实现对象存储的操作
COSClient cos = new COSClient(context,appid,config,peristenceId);
```

## 快速入门 

### 初始化 COSClient

```java
String appid =  "腾讯云注册的appid";
Context context = getApplicationContext()；
String peristenceId = "持久化Id";

//创建COSClientConfig对象，根据需要修改默认的配置参数
COSClientConfig config = new COSClientConfig();
//如设置园区
config.setEndPoint(COSEndPoint.COS_GZ);

COSClient cos = new COSClient(context,appid,config,peristenceId);
```

### 上传文件

```java
String bucket = "cos空间名称";
String cosPath = "远端路径，即存储到cos上的路径";
String srcPath = "本地文件的绝对路径";
String sign = "签名，此处使用多次签名";

PutObjectRequest putObjectRequest = new PutObjectRequest();
putObjectRequest.setBucket(bucket);
putObjectRequest.setCosPath(cosPath);
putObjectRequest.setSrcPath(srcPath);
putObjectRequest.setSign(sign);
putObjectRequest.setListener(new  IUploadTaskListener(){
    @Override
    public void onSuccess(COSRequest cosRequest, COSResult cosResult) {

         PutObjectResult result = (PutObjectResult) cosResult;
         if(result != null){
             StringBuilder stringBuilder = new StringBuilder();
             stringBuilder.append(" 上传结果： ret=" + result.code + "; msg =" +result.msg + "\n");
             stringBuilder.append(" access_url= " + result.access_url == null ? "null" :result.access_url + "\n");
             stringBuilder.append(" resource_path= " + result.resource_path == null ? "null" :result.resource_path + "\n");
             stringBuilder.append(" url= " + result.url == null ? "null" :result.url);
             Log.w("TEST",stringBuilder.toString());
          }
     }

     @Override
     public void onFailed(COSRequest COSRequest, final COSResult cosResult) {
         Log.w("TEST","上传出错： ret =" +cosResult.code + "; msg =" + cosResult.msg);
     }

     @Override
     public void onProgress(COSRequest cosRequest, final long currentSize, final long totalSize) {
         float progress = (float)currentSize/totalSize;
         progress = progress *100;
         Log.w("TEST","进度：  " + (int)progress + "%"); 
      }
});
PutObjectResult result = cos.PutObject(putObjectRequest);
```

### 下载文件

```java
String downloadURl =  "下载文件的URL";
String savePath = "本地保存文件的路径";
String sign = "开启token防盗链了，则需要签名；否则，不需要";

GetObjectRequest getObjectRequest = new GetObjectRequest(downloadURl,savePath);
getObjectRequest.setSign(null);
getObjectRequest.setListener(new IDownloadTaskListener() {
    @Override
    public void onProgress(COSRequest cosRequest, final long currentSize, final long totalSize) {
        float progress =  currentSize / (float)totalSize;
        progress = progress * 100;
        progressText.setText("progress =" + (int) (progress) + "%");
        Log.w("TEST", "progress =" + (int) (progress) + "%");
   }

   @Override
   public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
       Log.w("TEST","code =" + cosResult.code + "; msg =" + cosResult.msg);
   }

   @Override
   public void onFailed(COSRequest COSRequest, COSResult cosResult) {
        Log.w("TEST","code =" + cosResult.code + "; msg =" + cosResult.msg);
   }
});

GetObjectResult getObjectResult = cos.getObject(getObjectRequest);                

```

## 生成签名

**签名类型：**

| 类型     | 含义                    |
| -------- | ----------------------- |
| 多次有效 | 有效时间内多次始终有效  |
| 单次有效 | 与资源URL绑定，一次有效 |

**签名获取：**

SDK 中用到的 SIGN，推荐使用 服务器端SDK，并由移动端向业务服务器请求。SIGN 的具体生成和使用请参照 [访问权限](https://cloud.tencent.com/document/product/436/6054)。

## 目录操作 

### 创建目录

#### 方法原型

调用此接口可在指定的 bucket 下创建目录，具体步骤如下：

1. 调用 CreateDirRequest() 实例化 CreateDirRequest 对象；
2. 调用 COSClient 的 createDir 方法，传入 CreateDirRequest，返回 CreateDirResult 对象；

#### 参数说明

| 参数名称 | 类型             | 是否必填 | 参数描述                       |
| :------- | :--------------- | :------- | :----------------------------- |
| appid    | String           | 是       | 腾讯云APPID                    |
| bucket   | String           | 是       | 目录所属bucket 名称            |
| cosPath  | String           | 是       | 需要创建目录的路径             |
| biz_attr | String           | 否       | 目录绑定的属性信息，由用户维护 |
| sign     | String           | 是       | 签名信息，此处使用多次签名     |
| listener | ICmdTaskListener | 否       | 结果回调                       |

#### 返回结果说明

通过CreateDirResult对象的成员变量返回请求结果。

| 成员变量名称 | 类型             | 变量说明     |
| :----------- | :--------------- | :----------- |
| code         | String           | 结果码       |
| msg          | String           | 详细结果信息 |
| ctime        | long(Unix时间戳) | 创建时间     |

#### 示例

```
CreateDirRequest createDirRequest = new CreateDirRequest();
createDirRequest.setBucket(bucket);
createDirRequest.setCosPath(cosPath);
createDirRequest.setBiz_attr(biz_attr);
createDirRequest.setSign(sign);
createDirRequest.setListener(new ICmdTaskListener() {
    public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
        final CreateDirResult createDirResult = (CreateDirResult) cosResult;
        Log.w("TEST","目录创建成功： ret=" + createDirResult.code + "; msg=" + createDirResult.msg 
            +"ctime = " + createDirResult.ctime));
    }

    @Override
    public void onFailed(COSRequest COSRequest, final COSResult cosResult) {
         Log.w("TEST","目录创建失败： ret=" + cosResult.code + "; msg=" + cosResult.msg);
    }
});

CreateDirResult result = cos.createDir(createDirRequest);
```

### 目录列表查询

#### 方法原型

调用此接口可查询指定目录下的列表信息，具体步骤如下：

1. 调用 ListDirRequest() 实例化 ListDirRequest 对象；
2. 调用 COSClient 的 listDir 方法，传入 ListDirRequest，返回 ListDirResult 对象；

#### 参数说明

| 参数名称 | 类型             | 是否必填 | 参数描述                                                     |
| :------- | :--------------- | :------- | :----------------------------------------------------------- |
| appid    | String           | 是       | 腾讯云APPID                                                  |
| bucket   | String           | 是       | 目录所属bucket 名称                                          |
| cosPath  | String           | 是       | 远程相对路径                                                 |
| num      | int              | 否       | 返回的数目，默认为1000，最大1000                             |
| content  | String           | 否       | 透传字段，首次拉取必须清空。拉取下一页，需要将前一页返回值中的context透传到参数中 |
| prefix   | String           | 否       | 前缀查询的字符串                                             |
| sign     | String           | 是       | 签名信息，此处使用多次签名                                   |
| listener | ICmdTaskListener | 否       | 结果回调                                                     |

#### 返回结果说明

通过ListDirResult对象的成员变量返回请求结果。

| 成员变量名称 | 类型         | 变量说明                                           |
| :----------- | :----------- | :------------------------------------------------- |
| code         | String       | 结果码                                             |
| msg          | String       | 详细结果信息                                       |
| content      | String       | 透传字段                                           |
| listover     | boolean      | 标识是否还有数据， true：列举结束；false：还有数据 |
| infos        | List<String> | 列举目录列表中文件或文件夹的属性                   |

#### 示例

```
ListDirRequest listDirRequest = new ListDirRequest();
listDirRequest.setBucket(bucket);
listDirRequest.setCosPath(cosPath);
listDirRequest.setNum(100);
listDirRequest.setContent("");
listDirRequest.setSign(sign);
listDirRequest.setListener(new ICmdTaskListener() {
    @Override
    public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
    		//查询成功
        ListDirResult listObjectResult = (ListDirResult) cosResult;
        if(listObjectResult.infos != null && listObjectResult.infos.size() > 0) {
        for(int i = 0; i < length; i++){
            String str = listObjectResult.infos.get(i);
            try {
                JSONObject jsonObject = new JSONObject(str);
                if(jsonObject.has("sha")){
                 //当前搜索的结果是文件
                }else{
                //当前搜索的结果是文件夹
                }
            } catch (JSONException e) {
               e.printStackTrace();
            } 
     }
     }

   	 if (!listover) {
			// 存在下一页保存当前页的状态信息
			String content = result.content;
		}
    }

    @Override
    public void onFailed(COSRequest COSRequest, final COSResult cosResult) {
        Log.w("TEST",目录查询失败：ret=" + cosResult.code  + "; msg =" + cosResult.msg);
   }
});


// 支持前缀查询
listDirRequest.setPrefix(prefix);
ListDirResult result=cos.listDir(listDirRequest);
```

### 目录更新

#### 方法原型

调用此接口可更新指定目录的信息，具体步骤如下：

1. 调用 UpdateObjectRequest() 实例化 UpdateObjectRequest 对象；
2. 调用 COSClient 的 updateObject 方法，传入 UpdateObjectRequest，返回 UpdateObjectResult 对象；

#### 参数说明

| 参数名称 | 类型             | 是否必填 | 参数描述                   |
| :------- | :--------------- | :------- | :------------------------- |
| appid    | String           | 是       | 腾讯云APPID                |
| bucket   | String           | 是       | 目录所属bucket 名称        |
| cosPath  | String           | 是       | 远程相对路径               |
| sign     | String           | 是       | 签名信息，此处使用单次签名 |
| bizAttr  | String           | 否       | 目录绑定的属性信息         |
| listener | ICmdTaskListener | 否       | 结果回调                   |

#### 返回结果说明

通过UpdateObjectResult对象的成员变量成员变量返回请求结果。

| 成员变量名称 | 类型   | 变量说明     |
| :----------- | :----- | :----------- |
| code         | String | 结果码       |
| msg          | String | 详细结果信息 |

#### 示例

```
UpdateObjectRequest updateObjectRequest = new UpdateObjectRequest();
updateObjectRequest.setBucket(bucket);
updateObjectRequest.setCosPath(cosPath);
updateObjectRequest.setBizAttr(biz_attr);
updateObjectRequest.setSign(onceSign);
updateObjectRequest.setListener(new ICmdTaskListener() {
    @Override
    public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
        //更新成功
        Log.w("TEST", cosResult.code+" : "+cosResult.msg);
    }

     @Override
     public void onFailed(COSRequest COSRequest, COSResult cosResult) {
         //更新失败
         Log.w("TEST", cosResult.code+" : "+cosResult.msg);
     }
});

UpdateObjectResult result = cos.updateObject(updateObjectRequest);
```

### 目录查询

#### 方法原型

调用此接口可查询指定目录的信息，具体步骤如下：

1. 调用 GetObjectMetadataRequest() 方法实例化 GetObjectMetadataRequest 对象；
2. 调用 COSClient 的 getObjectMetadata方法，传入 GetObjectMetadataRequest，返回 GetObjectMetadataResult对象；

#### 参数说明

| 参数名称 | 类型             | 是否必填 | 参数描述                   |
| :------- | :--------------- | :------- | :------------------------- |
| appid    | String           | 是       | 腾讯云APPID                |
| bucket   | String           | 是       | 目录所属bucket 名称        |
| cosPath  | String           | 是       | 远程相对路径               |
| sign     | String           | 是       | 签名信息，此处使用多次签名 |
| listener | ICmdTaskListener | 否       | 结果回调                   |

#### 返回结果说明

通过GetObjectMetadataResult对象的成员变量返回请求结果。

| 成员变量名称 | 类型             | 变量说明           |
| :----------- | :--------------- | :----------------- |
| code         | String           | 结果码             |
| msg          | String           | 详细结果信息       |
| biz_attr     | String           | 目录绑定的属性信息 |
| ctime        | long(Unix时间戳) | 创建时间           |
| mtime        | long(Unix时间戳) | 最后一次修改时间   |

#### 示例

```
GetObjectMetadataRequest getObjectMetadataRequest = new GetObjectMetadataRequest();
getObjectMetadataRequest.setBucket(bucket);
getObjectMetadataRequest.setCosPath(cosPath);
getObjectMetadataRequest.setSign(sign);
getObjectMetadataRequest.setListener(new ICmdTaskListener() {
     @Override
     public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
         GetObjectMetadataResult result = (GetObjectMetadataResult) cosResult;
         StringBuilder stringBuilder = new StringBuilder();
         stringBuilder.append("code=" + result.code + "; msg=" +result.msg + "\n");
         stringBuilder.append("ctime =" +result.ctime + "; mtime=" +result.mtime + "\n" );
         stringBuilder.append("biz_attr=" + result.biz_attr == null ? "" : result.biz_attr );
         Log.w("TEST",stringBuilder.toString());
      }

      @Override
      public void onFailed(COSRequest cosRequest, final COSResult cosResult) {
          Log.w("TEST", cosResult.code+" : "+cosResult.msg);
       }

});

GetObjectMetadataRequest result = cos.getObjectMetadata(getObjectMetadataRequest);  
```

### 目录删除

#### 方法原型

调用此接口可删除指定目录，具体步骤如下，注意只能删除空目录：

1. 调用 RemoveEmptyDirRequest() 方法实例化 RemoveEmptyDirRequest 对象；
2. 调用 COSClient 的 removeEmptyDir 方法，传入 RemoveEmptyDirRequest，返回 RemoveEmptyDirResult 对象；

#### 参数说明

| 参数名称 | 类型             | 是否必填 | 参数描述                   |
| :------- | :--------------- | :------- | :------------------------- |
| appid    | String           | 是       | 腾讯云 APPID               |
| bucket   | String           | 是       | 目录所属 bucket 名称       |
| cosPath  | String           | 是       | 远程相对路径               |
| sign     | String           | 是       | 签名信息，此处使用单次签名 |
| listener | ICmdTaskListener | 否       | 结果回调                   |

#### 返回结果说明

通过RemoveEmptyDirResult对象的成员变量返回请求结果。

| 成员变量名称 | 类型   | 变量说明     |
| :----------- | :----- | :----------- |
| code         | String | 结果码       |
| msg          | String | 详细结果信息 |

#### 示例

```
RemoveEmptyDirRequest removeEmptyDirRequest = new RemoveEmptyDirRequest();
removeEmptyDirRequest.setBucket(bucket);
removeEmptyDirRequest.setCosPath(cosPath);
removeEmptyDirRequest.setSign(onceSign);
removeEmptyDirRequest.setListener(new ICmdTaskListener() {
    @Override
    public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
        final DeleteObjectResult removeEmptyDirResult = (DeleteObjectResult) cosResult;
        Log.w("TEST","removeDir 结果： ret=" + removeEmptyDirResult.code + "; msg=" + removeEmptyDirResult.msg );
    }

    @Override
    public void onFailed(COSRequest COSRequest, final COSResult cosResult) {
        Log.w("TEST","目录删除失败：ret=" + cosResult.code  + "; msg =" + cosResult.msg);
    }
});

RemoveEmptyDirResult result = cos.removeEmptyDir(removeEmptyDirRequest); 

```

## 文件操作 

### 文件上传

#### 方法原型

调用此接口上传指定的文件，具体步骤如下：

1. 调用 PutObjectRequest() 方法实例化 PutObjectRequest对象；
2. 调用 COSClient 的 putObject 方法，传入 PutObjectRequest，返回 PutObjectResult对象；

#### 参数说明

| 参数名称   | 类型                | 是否必填 | 参数描述                               |
| :--------- | :------------------ | :------- | :------------------------------------- |
| appid      | String              | 是       | 腾讯云 APPID                           |
| bucket     | String              | 是       | 目录所属 bucket 名称                   |
| cosPath    | String              | 是       | 远程相对路径                           |
| srcPath    | String              | 是       | 本地绝对路径                           |
| slice_size | int                 | 否       | 分片上传时，设置的分片大小，默认为：1M |
| sign       | String              | 是       | 签名信息，此处使用多次签名             |
| listener   | IUploadTaskListener | 否       | 结果回调                               |

#### 返回结果说明

通过PutObjectResult对象的成员变量返回请求结果。

| 成员变量名称 | 类型   | 变量说明      |
| :----------- | :----- | :------------ |
| code         | String | 结果码        |
| msg          | String | 详细结果信息  |
| access_url   | String | 访问文件的URL |
| url          | String | 操作文件的url |

#### 示例

```
PutObjectRequest putObjectRequest = new PutObjectRequest();
putObjectRequest.setBucket(bucket);
putObjectRequest.setCosPath(cosPath);
putObjectRequest.setSrcPath(srcPath);
putObjectRequest.setSign(sign);

 /* 设置是否允许覆盖同名文件： "0"，允许覆盖；"1",不允许覆盖；
putObjectRequest.setInsertOnly("1");

//设置是否开启分片上传
putObjectRequest.setSliceFlag(true);//设置是否分片上传：true，分片上传;false,简单文件上传
putObjectRequest.setSlice_size(1024*1024);//分片上传时，分片的大小
 */

putObjectRequest.setListener(new  IUploadTaskListener(){
    @Override
    public void onSuccess(COSRequest cosRequest, COSResult cosResult) {

         PutObjectResult result = (PutObjectResult) cosResult;
         StringBuilder stringBuilder = new StringBuilder();
         stringBuilder.append(" 上传结果： ret=" + result.code + "; msg =" +result.msg + "\n");
         stringBuilder.append(" access_url= " + result.access_url + "\n");
         stringBuilder.append(" resource_path= " + result.resource_path + "\n");
         stringBuilder.append(" url= " result.url);
         Log.w("TEST",stringBuilder.toString();
     }

    @Override
    public void onFailed(COSRequest COSRequest, final COSResult cosResult) {
         Log.w("TEST","上传出错： ret =" +cosResult.code + "; msg =" + cosResult.msg);
    }

    @Override
    public void onProgress(COSRequest cosRequest, final long currentSize, final long totalSize) {
         float progress = (float)currentSize/totalSize;
         progress = progress *100;
         Log.w("TEST","进度：  " + (int)progress + "%");
    }
});

PutObjectResult result = cos.putObject(putObjectRequest);
```

### 文件更新

#### 方法原型

调用此接口可更新指定文件信息，具体步骤如下：

1. 调用 UpdateObjectRequest() 方法实例化 UpdateObjectRequest 对象；
2. 调用 COSClient 的 updateObject 方法，传入 UpdateObjectRequest，返回 UpdateObjectResult 对象；

#### 参数说明

| 参数名称       | 类型               | 是否必填 | 参数描述                                                     |
| :------------- | :----------------- | :------- | :----------------------------------------------------------- |
| appid          | String             | 是       | 腾讯云 APPID                                                 |
| bucket         | String             | 是       | 目录所属 bucket 名称                                         |
| cosPath        | String             | 是       | 远程相对路径                                                 |
| sign           | String             | 是       | 签名信息，此处使用单次签名                                   |
| bizAttr        | String             | 否       | 目录绑定的属性信息                                           |
| authority      | String             | 否       | 文件操作权限，与 bucket 拥有相同的权限（COSAuthority.EINVALID），私有读写权限（COSAuthority.EWRPRIVATE），私有写公有读权限（COSAuthority.EWPRIVATERPUBLIC） |
| custom_headers | Map<String,String> | 否       | 文件自定义的header: 如Cache-Control,  Content-Disposition,Content-Language,x-cos-meta-。 |
| listener       | ICmdTaskListener   | 否       | 结果回调                                                     |

#### 返回结果说明

通过UpdateObjectResult对象的成员变量返回请求结果。

| 成员变量名称 | 类型   | 变量说明     |
| :----------- | :----- | :----------- |
| code         | String | 结果码       |
| msg          | String | 详细结果信息 |

#### 示例

```
UpdateObjectRequest updateObjectRequest = new UpdateObjectRequest();
updateObjectRequest.setBucket(bucket);
updateObjectRequest.setCosPath(cosPath);
updateObjectRequest.setBizAttr(biz_attr);
updateObjectRequest.setAuthority(authority);
updateObjectRequest.setCustomHeader(customer);
updateObjectRequest.setSign(onceSign);
updateObjectRequest.setListener(new ICmdTaskListener() {
    @Override
    public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
        Log.w("TEST", cosResult.code+" : "+cosResult.msg);
    }

    @Override
    public void onFailed(COSRequest COSRequest, COSResult cosResult) {
                        Log.w("TEST", cosResult.code+" : "+cosResult.msg);
    }
});

UpdateObjectResult result= cos.updateObject(updateObjectRequest);
```

### 文件查询

#### 方法原型

调用此接口可查询指定文件信息，具体步骤如下：

1. 调用 GetObjectMetadataRequest() 方法实例化 GetObjectMetadataRequest 对象；
2. 调用 COSClien t的 getObjectMetadata 方法，传入 GetObjectMetadataRequest，返回 GetObjectMetadataResult 对象；

#### 参数说明

| 参数名称 | 类型             | 是否必填 | 参数描述                   |
| :------- | :--------------- | :------- | :------------------------- |
| appid    | String           | 是       | 腾讯云APPID                |
| bucket   | String           | 是       | 目录所属bucket 名称        |
| cosPath  | String           | 是       | 远程相对路径               |
| sign     | String           | 是       | 签名信息，此处使用多次签名 |
| listener | ICmdTaskListener | 否       | 结果回调                   |

#### 返回结果说明

通过GetObjectMetadataResult对象的成员变量返回请求结果。

| 成员变量名称    | 类型               | 变量说明           |
| :-------------- | :----------------- | :----------------- |
| code            | String             | 结果码             |
| msg             | String             | 详细结果信息       |
| biz_attr        | String             | 目录绑定的属性信息 |
| ctime           | long(Unix时间戳)   | 创建时间           |
| mtime           | long(Unix时间戳)   | 最后一次修改时间   |
| sha             | String             | 文件的sha值        |
| customs_headers | Map<String,String> | 文件的头部属性     |
| filelen         | int                | 文件的长度大小     |

#### 示例

```
GetObjectMetadataRequest getObjectMetadataRequest = new GetObjectMetadataRequest();
getObjectMetadataRequest.setBucket(bucket);
getObjectMetadataRequest.setCosPath(cosPath);
getObjectMetadataRequest.setSign(sign);
getObjectMetadataRequest.setListener(new ICmdTaskListener() {
     @Override
     public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
         GetObjectMetadataResult result = (GetObjectMetadataResult) cosResult;
         StringBuilder stringBuilder = new StringBuilder();
         stringBuilder.append("code=" + result.code + "; msg=" +result.msg + "\n");
         stringBuilder.append("ctime =" +result.ctime + "; mtime=" +result.mtime + "\n" );
         stringBuilder.append("biz_attr=" + result.biz_attr == null ? "" : result.biz_attr );
         stringBuilder.append("sha=" + result.sha);
         Log.w("TEST",stringBuilder.toString());
      }

      @Override
      public void onFailed(COSRequest cosRequest, final COSResult cosResult) {
          Log.w("TEST", cosResult.code+" : "+cosResult.msg);
       }

});

GetObjectMetadataRequest result=cos.getObjectMetadata(getObjectMetadataRequest);  
```

### 文件删除

#### 方法原型

调用此接口可删除指定文件，具体步骤如下：

1. 调用 DeleteObjectRequest() 方法实例化 DeleteObjectRequest 对象；
2. 调用 COSClient 的 deleteObject 方法，传入 DeleteObjectRequest，回 DeleteObjectResult 对象；

#### 参数说明

| 参数名称 | 类型             | 是否必填 | 参数描述               |
| :------- | :--------------- | :------- | :--------------------- |
| appid    | String           | 是       | 腾讯云APPID            |
| bucket   | String           | 是       | 目录所属bucket 名称    |
| cosPath  | String           | 是       | 远程相对路径           |
| sign     | String           | 是       | 签名信息，此处单次签名 |
| listener | ICmdTaskListener | 否       | 结果回调               |

#### 返回结果说明

通过DeleteObjectResult对象的成员变量返回请求结果。

| 成员变量名称 | 类型   | 变量说明     |
| :----------- | :----- | :----------- |
| code         | String | 结果码       |
| msg          | String | 详细结果信息 |

#### 示例

```
DeleteObjectRequest deleteObjectRequest = new DeleteObjectRequest();
deleteObjectRequest.setBucket(bucket);
deleteObjectRequest.setCosPath(cosPath);
deleteObjectRequest.setSign(onceSign);
deleteObjectRequest.setListener(new ICmdTaskListener() {
    @Override
    public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
         Log.w("TEST", cosResult.code+" : "+cosResult.msg);
    }

    @Override
    public void onFailed(COSRequest COSRequest, COSResult cosResult) {
        Log.w("TEST", cosResult.code+" : "+cosResult.msg);
   }
});

DeleteObjectResult result = cos.deleteObject(deleteObjectRequest); 
```

### 文件下载

#### 方法原型

调用此接口可下载指定文件，具体步骤如下：

1. 调用 GetObjectRequest(String downloadURl,String savePath) 方法实例化 GetObjectRequest对象；
2. 调用 COSClient 的 getObject 方法，传入 GetObjectRequest,返回 GetObjectResult 对象；

#### 参数说明

| 参数名称    | 类型                  | 是否必填 | 参数描述                                 |
| :---------- | :-------------------- | :------- | :--------------------------------------- |
| downloadUrl | String                | 是       | 下载文件的URL                            |
| localPath   | String                | 是       | 本地保存文件的绝对地址                   |
| sign        | String                | 否       | 签名信息：开启了防盗链则需要，否则不需要 |
| listener    | IDownloadTaskListener | 否       | 结果回调                                 |

#### 返回结果说明

通过GetObjectResult对象的成员变量返回请求结果。

| 成员变量名称 | 类型   | 变量说明     |
| :----------- | :----- | :----------- |
| code         | String | 结果码       |
| msg          | String | 详细结果信息 |

#### 示例

```
GetObjectRequest getObjectRequest = new GetObjectRequest(downloadURl,savePath);
getObjectRequest.setSign(null);
getObjectRequest.setListener(new IDownloadTaskListener() {
    @Override
    public void onProgress(COSRequest cosRequest, final long currentSize, final long totalSize) {
        float progress =  currentSize / (float)totalSize;
        progress = progress * 100;
        progressText.setText("progress =" + (int) (progress) + "%");
        Log.w("TEST", "progress =" + (int) (progress) + "%");
                            
    }

    @Override
    public void onSuccess(COSRequest cosRequest, COSResult cosResult) {
         Log.w("TEST","code =" + cosResult.code + "; msg =" + cosResult.msg);
    }

    @Override
    public void onFailed(COSRequest COSRequest, COSResult cosResult) {
                        Log.w("TEST","code =" + cosResult.code + "; msg =" + cosResult.msg);
    }
});


GetObjectResul result = cos.getObject(getObjectRequest);
```
