###  开发准备

#### SDK 获取

COS服务的java sdk的下载地址： [https://github.com/tencentyun/cos-java-sdk.git](https://github.com/tencentyun/cos-java-sdk.git)



#### 开发环境

1. sdk采用1.7版本的jdk开发， 推荐使用相同的版本；
2. 从控制台获取APP ID、SecretID、SecretKey，详情参考[权限控制](/doc/product/227/权限控制)；




#### Maven 配置（推荐）

建议使用Maven软件项目管理工具，其pom.xml配置信息如下。

```
<dependency>
			<groupId>com.qcloud</groupId>
			<artifactId>cos_api</artifactId>
			<version>3.1</version>
</dependency>
```


#### SDK 源码导入

通过git命令行，执行 git clone [https://github.com/tencentyun/cos-java-sdk.git](https://github.com/tencentyun/cos-java-sdk.git)

若需支持 HTTPS，修改 CosCloud.java 中 COSAPI_CGI_URL 的值为：

[https://web.file.myqcloud.com/files/v1/](https://web.file.myqcloud.com/files/v1/) 




### 生成签名

#### 多次有效签名

##### 方法原型

```java
String appSignature(int appId, String secretId, String secretKey, long expired, String bucketName)
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| appId      | String | 是        | 无       | 开发者的授权appid                              |
| secret_id  | String | 是        | 无       | 开发者的授权secret_id                          |
| secret_key | String | 是        | 无       | 开发者的授权secret_key，以上三项获取参见[项目设置](http://console.qcloud.com/cos) |
| expired    | long   | 否        | 无       | 过期时间，Unix时间戳                             |
| bucketName | String | 否        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |

##### 返回值说明

返回：签名字符串

##### 示例

```java
long expired = System.currentTimeMillis() / 1000 + 2592000;
String sign = Sign.appSignature(m_appid, m_secret_id, m_secret_key, expired, bucketName);
```



#### 单次有效签名

##### 方法原型

```java
String appSignatureOnce(int appId, String secretId, String secretKey, String resourcePath, String bucketName)
```

##### 参数说明

| **参数名**      | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ------------ | ------ | -------- | ------- | ---------------------------------------- |
| appId        | String | 是        | 无       | 开发者的授权appid                              |
| secret_id    | String | 是        | 无       | 开发者的授权secret_id                          |
| secret_key   | String | 是        | 无       | 开发者的授权secret_key，以上三项获取参见[项目设置](http://console.qcloud.com/cos) |
| bucketName   | String | 否        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| resourcePath | String | 是        | 无       | 文件唯一的标识，文件上传时会返回，格式/filepath/filename，文件在此bucketname下的全路径 |

##### 返回值说明

返回值：签名字符串

##### 示例

```java
String resourcePath= "/myFloder/myCosFile.txt";
String sign = Sign.appSignatureOnce(m_appid, m_secret_id, m_secret_key, resourcePath, "myBucketName");
```



更多签名相关详细说明，请参考[权限控制](#) 。



### 目录操作

#### 创建目录

接口说明：用于目录的创建，可以通过此接口在指定bucket下创建目录。

##### 方法原型

```java
String createFolder(String bucketName,String remotePath)
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| bucketName | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| remotePath | String | 是        | 无       | 需要创建目录的全路径，以"/"开头,以"/"结尾，api会补齐          |

##### 返回值说明(json)

| **参数名**            | **类型** | **参数描述**        |
| ------------------ | ------ | --------------- |
| code               | Int    | 错误码，成功时为0       |
| message            | String | 错误信息            |
| data               | Array  | 返回数据            |
| data.ctime         | String | 目录的创建时间，unix时间戳 |
| data.resource_path | String | 目录的资源路径         |

##### 示例

```java
CosCloud cos = new CosCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/";
String result = cos.createFolder("bucketname", remotePath);
```



#### 目录属性更新

接口说明：用于目录业务自定义属性的更新，可以通过此接口更新业务的自定义属性字段。

##### 方法原型

```java
String updateFolder(String bucketName, String remotePath, String bizAttribute) 
```

##### 参数说明

| **参数名**      | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ------------ | ------ | -------- | ------- | ---------------------------------------- |
| bucketName   | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| remotePath   | String | 是        | 无       | 需要创建目录的全路径，以"/"开头,以"/"结尾，api会补齐          |
| bizAttribute | String | 是        | 无       | 新的目录绑定的属性信息                              |

##### 返回值说明(json)

| **参数名** | **类型** | **参数描述**  |
| ------- | ------ | --------- |
| code    | Int    | 错误码，成功时为0 |
| message | String | 错误信息      |

##### 示例

```java
CosCloud cos = new CosCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/";
String result = cos.updateFolder("bucketname", remotePath,"bizAttribute_new");
```



#### 目录查询

接口说明：用于目录属性的查询，可以通过此接口查询目录的属性。

##### 方法原型

```java
String getFolderStat(String bucketName, String remotePath) 
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| bucketName | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| remotePath | String | 是        | 无       | 目录的全路径，以"/"开头,以"/"结尾，api会补齐              |

##### 返回值说明(json)

| **参数名**       | **类型** | **参数描述**         |
| ------------- | ------ | ---------------- |
| code          | Int    | 错误码，成功时为0        |
| message       | String | 错误信息             |
| data          | Array  | 目录属性数据           |
| data.biz_attr | String | 目录绑定的属性信息，业务自行维护 |
| data.ctime    | String | 目录的创建时间，unix时间戳  |
| data.mtime    | String | 目录的修改时间，unix时间戳  |
| data.name     | String | 目录的名称            |

##### 示例

```java
CosCloud cos = new CosCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/";
String result = cos.getFolderStat("bucketname", remotePath);
```



#### 目录删除

接口说明：用于目录的删除，可以通过此接口删除空目录，如果目录中存在有效文件或目录，将不能删除。

##### 方法原型

```java
String deleteFolder(String bucketName, String remotePath) 
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| bucketName | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| remotePath | String | 是        | 无       | 目录的全路径，以"/"开头,以"/"结尾，api会补齐              |

##### 返回值说明(json)

| **参数名** | **类型** | **参数描述**  |
| ------- | ------ | --------- |
| code    | Int    | 错误码，成功时为0 |
| message | String | 错误信息      |

##### 示例

```java
CosCloud cos = new CosCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/";
String result = cos.deleteFolder("bucketname", remotePath);
```



#### 列举目录下文件&目录

接口说明：用于列举目录下文件和目录，可以通过此接口查询目录下的文件和目录属性。

##### 方法原型

```java
String getFolderList(String bucketName, String remotePath, int num, String context, int order, FolderPattern pattern) 
```

##### 参数说明

| **参数名**    | **类型**        | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------------- | -------- | ------- | ---------------------------------------- |
| bucketName | String        | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| remotePath | String        | 是        | 无       | 目录的全路径，以"/"开头,以"/"结尾，api会补齐              |
| num        | int           | 是        | 无       | 要查询的目录/文件数量                              |
| context    | String        | 是        | 无       | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页 |
| order      | int           | 是        | 无       | 默认正序(=0), 填1为反序                          |
| pattern    | FolderPattern | 是        | 无       | pattern File=>仅列举文件；Folder=>仅列举目录；Both=>列举文件和目录 |

##### 返回值说明(json)

| **参数名**               | **类型** | **是否必然返回**   | **参数描述**                                 |
| --------------------- | ------ | ------------ | ---------------------------------------- |
| code                  | Int    | 是            | API 错误码，成功时为0                            |
| message               | String | 是            | 错误信息                                     |
| data                  | Array  | 是            | 返回数据                                     |
| data.has_more         | Bool   | 是            | 是否有内容可以继续往前/往后翻页                         |
| data.context          | String | 是            | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页 |
| data.dircount         | String | 是            | 子目录数量(总)                                 |
| data.filecount        | String | 是            | 子文件数量(总)                                 |
| data.infos            | Array  | 是            | 文件、目录集合，可以为空                             |
| data.infos.name       | String | 是            | 文件或目录名                                   |
| data.infos.biz_attr   | String | 是            | 目录或文件属性，业务端维护                            |
| data.infos.ctime      | String | 是            | 目录或文件的创建时间，unix时间戳                       |
| data.infos.mtime      | String | 是            | 目录或文件的修改时间，unix时间戳                       |
| data.infos.filesize   | Int    | 否(当类型为文件时返回) | 文件大小                                     |
| data.infos.filelen    | Int    | 否(当类型为文件时返回) | 文件已传输大小(通过与filesize对比可知文件传输进度)           |
| data.infos.sha        | String | 否(当类型为文件时返回) | 文件sha                                    |
| data.infos.access_url | String | 否(当类型为文件时返回) | 生成的文件下载url                               |

##### 示例

```java
CosCloud cos = new CosCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/";
String result = cos.getFolderList("bucketname", remotePath, 100, "", 0, FolderPattern.Both);
```



#### 列举目录下指定前缀文件&目录

接口说明：用于列举目录下指定前缀的文件和目录，可以通过此接口查询目录下的指定前缀的文件和目录信息。

##### 方法原型

```java
String getFolderList(String bucketName, String remotePath, String prefix, int num, String context, int order, FolderPattern pattern) 
```

##### 参数说明

| **参数名**    | **类型**        | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------------- | -------- | ------- | ---------------------------------------- |
| bucketName | String        | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| remotePath | String        | 是        | 无       | 需要创建目录的全路径，以"/"开头,以"/"结尾，api会补齐          |
| prefix     | String        | 是        | 无       | 读取文件/目录前缀                                |
| num        | int           | 是        | 无       | 要查询的目录/文件数量                              |
| context    | String        | 是        | 无       | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页 |
| order      | int           | 是        | 无       | 默认正序(=0), 填1为反序                          |
| pattern    | FolderPattern | 是        | 无       | pattern File=>仅列举文件；Folder=>仅列举目录；Both=>列举目录和文件 |

##### 返回值说明(json)

| **参数名**               | **类型** | **是否必然返回**   | **参数描述**                                 |
| --------------------- | ------ | ------------ | ---------------------------------------- |
| code                  | Int    | 是            | 错误码，成功时为0                                |
| message               | String | 是            | API 错误信息                                 |
| data                  | Array  | 是            | 返回数据                                     |
| data.has_more         | Bool   | 是            | 是否有内容可以继续往前/往后翻页                         |
| data.context          | String | 是            | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页 |
| data.dircount         | String | 是            | 子目录数量(总)                                 |
| data.filecount        | String | 是            | 子文件数量(总)                                 |
| data.infos            | Array  | 是            | 文件、目录集合，可以为空                             |
| data.infos.name       | String | 是            | 文件或目录名                                   |
| data.infos.biz_attr   | String | 是            | 目录或文件属性，业务端维护                            |
| data.infos.ctime      | String | 是            | 目录或文件的创建时间，unix时间戳                       |
| data.infos.mtime      | String | 是            | 目录或文件的修改时间，unix时间戳                       |
| data.infos.filesize   | Int    | 否(当类型为文件时返回) | 文件大小                                     |
| data.infos.filelen    | Int    | 否(当类型为文件时返回) | 文件已传输大小(通过与filesize对比可知文件传输进度)           |
| data.infos.sha        | String | 否(当类型为文件时返回) | 文件sha                                    |
| data.infos.access_url | String | 否(当类型为文件时返回) | 生成的文件下载url                               |

##### 示例

```python
CosCloud cos = new CosCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/";
String result = cos.getFolderList("bucketname", remotePath,"20150701_", 100,"",0,FolderPattern.Both);
```



### 文件操作

#### 文件上传

接口说明：用于较小文件(一般小于8MB)的上传，可以通过此接口上传较小的文件并获得文件的url，较大的文件请使用分片上传接口。

##### 方法原型

```python
String uploadFile(String bucketName, String remotePath,String localPath)
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| bucketName | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| remotePath | String | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname       |
| localPath  | String | 是        | 无       | 本地要上传文件的全路径                              |

##### 返回值说明(json)

| **参数名**            | **类型** | **是否必然返回** | **参数描述**                   |
| ------------------ | ------ | ---------- | -------------------------- |
| code               | Int    | 是          | 错误码，成功时为0                  |
| message            | String | 是          | 错误信息                       |
| data               | Array  | 是          | 返回数据                       |
| data.access_url    | Bool   | 是          | 生成的文件下载url                 |
| data.url           | String | 是          | 操作文件的url                   |
| data.resource_path | String | 是          | 资源路径. 格式:/appid/bucket/xxx |

##### 示例

```python
CosCloud cos = new CosCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/myCosFile.txt";
String localPath = "d:\\myCosFile.txt";
String result = cos.upload("bucketname", remotePath,localPath);
```



#### 文件分片上传

接口说明：用于较大文件(一般大于8MB)的上传，可以通过此接口上传较大文件并获得文件的url。

##### 方法原型

```java
String sliceUploadFile(String bucketName,String remotePath,String localPath) 

String sliceUploadFile(String bucketName,String remotePath,String localPath,int sliceSize) 
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值**    | **参数描述**                                 |
| ---------- | ------ | -------- | ---------- | ---------------------------------------- |
| bucketName | String | 是        | 无          | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| remotePath | String | 是        | 无          | 文件在COS服务端的全路径，不包括/appid/bucketname       |
| localPath  | String | 是        | 无          | 本地要上传文件的全路径                              |
| sliceSize  | Int    | 否        | 512*1024字节 | 分片大小，用户可以根据网络状况自行设置                      |

##### 返回值说明(json)

| **参数名**            | **类型** | **是否必然返回** | **参数描述**                   |
| ------------------ | ------ | ---------- | -------------------------- |
| code               | Int    | 是          | 错误码，成功时为0                  |
| message            | String | 是          | 错误信息                       |
| data               | Array  | 是          | 返回数据                       |
| data.access_url    | Bool   | 是          | 生成的文件下载url                 |
| data.url           | String | 是          | 操作文件的url                   |
| data.resource_path | String | 是          | 资源路径. 格式:/appid/bucket/xxx |

##### 示例

```java
CosCloud cos = new CosCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/myCosFile.txt";
String localPath = "d:\\myCosFile.txt";
String result = cos.sliceUploadFile("bucketname", remotePath,localPath,1024*1024);
```



#### 文件属性更新

接口说明：用于文件业务自定义属性的更新，可以通过此接口更新业务的自定义属性字段。

#### 方法原型

```java
String updateFile(String bucketName, String remotePath, String bizAttribute);
```

##### 参数说明

| **参数名**      | **类型** | *是否必填** | **默认值** | **参数描述**                                 |
| ------------ | ------ | ------- | ------- | ---------------------------------------- |
| bucketName   | String | 是       | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| remotePath   | String | 是       | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname       |
| bizAttribute | String | 否       | 无       | 待更新的文件属性信息                               |

##### 返回值说明(json)

| **参数名** | **类型** | **是否必然返回** | **参数描述**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | 是          | 错误码，成功时为0 |
| message | String | 是          | 错误信息      |

##### 示例

```python
CosCloud cos = new CosCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/myCosFile.txt";
String result = cos.updateFile("bucketname", remotePath, "new bizattr");
```



####  文件查询

接口说明：用于文件的查询，可以通过此接口查询文件的各项属性信息。

##### 方法原型

```
String getFileStat(String bucketName, String remotePath) 
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| bucketName | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| remotePath | String | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname       |

#####返回值说明(json) 

| **参数名**         | **类型** | **是否必然返回** | **参数描述**                       |
| --------------- | ------ | ---------- | ------------------------------ |
| code            | Int    | 是          | 错误码，成功时为0                      |
| message         | String | 是          | 错误信息                           |
| data            | Array  | 是          | 文件属性数据                         |
| data.name       | String | 是          | 文件或目录名                         |
| data.biz_attr   | String | 是          | 文件属性，业务端维护                     |
| data.ctime      | String | 是          | 文件的创建时间，unix时间戳                |
| data.mtime      | String | 是          | 文件的修改时间，unix时间戳                |
| data.filesize   | Int    | 是          | 文件大小                           |
| data.filelen    | Int    | 是          | 文件已传输大小(通过与filesize对比可知文件传输进度) |
| data.sha        | String | 是          | 文件sha                          |
| data.access_url | String | 是          | 生成的下载url                       |

##### 示例

```java
CosCloud cos = new CosCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/myCosFile.txt";
String result = cos.getFileStat("bucketname", remotePath);
```



#### 文件删除

接口说明：用于文件的删除，可以通过此接口删除已经上传的文件。

##### 方法原型

```
String deleteFile(String bucketName, String remotePath)
```

##### 参数说明

| **参数名**    | **类型** | 是否必填 | **默认值** | **参数描述**                                 |
| ---------- | ------ | ---- | ------- | ---------------------------------------- |
| bucketName | String | 是    | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| remotePath | String | 是    | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname       |

##### 返回值说明(json)

| **参数名** | **类型** | **必然返回** | **参数描述**  |
| ------- | ------ | -------- | --------- |
| code    | Int    | 是        | 错误码，成功时为0 |
| message | String | 是        | 错误信息      |

##### 示例

```java
CosCloud cos = new CosCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/myCosFile.txt";
String result = cos.deleteFile("bucketname", remotePath);
```