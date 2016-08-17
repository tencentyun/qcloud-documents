###  开发准备

#### SDK 获取

对象存储服务的C++ SDK的下载地址： [https://github.com/tencentyun/cos-cpp-sdk](https://github.com/tencentyun/cos-cpp-sdk)



#### 开发环境

1. 安装openssl的库和头文件 [http://www.openssl.org/source/](http://www.openssl.org/source/) 
2. 安装curl的库和头文件 [http://curl.haxx.se/download/curl-7.43.0.tar.gz](http://curl.haxx.se/download/curl-7.43.0.tar.gz) 
3. 安装jsoncpp的库和头文件 [https://github.com/open-source-parsers/jsoncpp](https://github.com/open-source-parsers/jsoncpp) 
4. 安装cmake工具 [http://www.cmake.org/download/](http://www.cmake.org/download/) 
5. 从控制台获取APP ID、SecretID、SecretKey，详情参考[权限控制](/doc/product/227/权限控制)。



注意：

1. sdk中提供了curl和jsoncpp的库以及头文件，以上库编译好后替换掉sdk中相应的库和头文件即可，如果以上库已经安装到系统里，也可删除sdk中相应的库和头文件。
2. curl默认不支持多线程环境，如果项目使用多线程，在编译curl执行 configure 时需指定 --enable-ares 参数来开启异步DNS解析，依赖 c-ares库，如果系统没有，可到[http://c-ares.haxx.se/](http://c-ares.haxx.se/) 下载安装。
3. jsoncpp的1.y.x版本需要c++11的支持，如果编译器不支持，可以换成 0.y.x版本。



#### SDK 配置

直接下载github上提供的源代码，集成到您的开发环境。 

执行下面的命令 ：

```
cd ${cos-cpp-sdk} 
mkdir -p build 
cd build 
cmake .. 
make 
```

需要将sample.cpp里的appid、secretId、secretKey、bucket等信息换成自己的信息。

生成的sample就可以直接运行，试用，生成的静态库，名称为：libcosdk.a。 

生成的 libcosdk.a 放到你自己的工程里lib路径下， include 目录下的 Auth.h Cosapi.h curl json openssl 都放到你自己的工程的include路径下。 

例如项目里只有一个 sample.cpp ，项目目录和sdk在同级目录， copy libcosdk.a 到项目所在目录那么编译命令为: 

```
g++ -o sample sample.cpp -I ./include/ -L. -L../cos-cpp-sdk/lib/ -lcosdk -lcurl -lcrypto -lssl -lrt -ljsoncpp
```

若需要 HTTPS 支持，修改 Cosapi.cpp 中 API_COSAPI_END_POINT 的值为：

[https://web.file.myqcloud.com/files/v1/](https://web.file.myqcloud.com/files/v1/) 



### 生成签名

#### 多次有效签名

##### 方法原型

```c++
static string appSign( const uint64_t appId, const string &secretId, const string &secretKey, const uint64_t expired, const string &bucketName); 
```

##### 参数说明

| 参数名        | **类型**   | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | -------- | -------- | ------- | ---------------------------------------- |
| appId      | uint64_t | 是        | 无       | 项目APP ID                                 |
| secretId   | String   | 是        | 无       | 用户 Secret ID                             |
| secretKey  | String   | 是        | 无       | 用户 SecretKey                             |
| expired    | uint64_t | 否        | 无       | 过期时间，Unix时间戳                             |
| bucketName | String   | 否        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |

##### 返回结果说明

返回值：签名字符串

##### 示例

```c++
uint64_t expired = time(NULL) + 60;
string sign = Auth::appSign(10000000, "SecretId", "SecretKey", expired , "bucketName");
```



#### 单次有效签名

##### 方法原型

```c++
static string appSign_once( const uint64_t appId, const string &secretId, const string &secretKey, const string &path, const string &bucketName); 
```

##### 参数说明

| **参数名**    | **类型**   | **必须** | **默认值** | **参数描述**                                 |
| ---------- | -------- | ------ | ------- | ---------------------------------------- |
| appId      | uint64_t | 是      | 无       | 项目 APP ID                                |
| secretId   | String   | 是      | 无       | 项目 SecretID                              |
| secretKey  | String   | 是      | 无       | 项目 SecretKey                             |
| bucketName | String   | 否      | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| path       | String   | 是      | 无       | 文件路径，以斜杠开头，例如/filepath/filename，为文件在此bucketname下的全路径 |

##### 返回值说明

返回值：签名字符串

##### 示例

```c++
string path= "/myFloder/myFile.rar";
sign = Auth::appSign_once(10000000, "SecretId", "SecretKey", path, bucketName);
```



更多签名相关详细说明，请参考[权限控制](#) 。



### 目录操作

#### 创建目录

接口说明：用于目录的创建，调用者可以通过此接口在指定bucket下创建目录。

##### 方法原型

```c++
int createFolder(const string &bucketName, const string &path, const string &biz_attr =""); 
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| bucketName | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| path       | String | 是        | 无       | 需要创建目录的全路径，以"/"开头,以"/"结尾，api会补齐          |
| biz_attr   | String | 否        | 空       | 目录绑定的属性信息，业务自行维护                         |

##### 返回结果说明

通过类的成员变量Json::Value retJson返回请求结果

| **参数名**            | **类型** | **参数描述**        |
| ------------------ | ------ | --------------- |
| code               | Int    | 错误码，成功时为0       |
| message            | String | 错误信息            |
| data               | Array  | 返回数据            |
| data.ctime         | String | 目录的创建时间，unix时间戳 |
| data.resource_path | String | 目录的资源路径         |

##### 示例

```c++
Cosapi api("your appid", "your secretId", "your secretKey", "interface timeout");
string bucketName = "myBucket";
string path = "/myFolder/";
string bizAttr = "attr_folder";
int result  = api.createFolder(bucketName, path,bizAttr);
api.dump_res();
```



#### 目录属性更新

接口说明：用于目录业务自定义属性的更新，可以通过此接口更新业务的自定义属性字段。

##### 方法原型

```c++
int updateFolder(const string &bucketName, const string &path, const string &biz_attr = ""); 
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| bucketName | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cost) |
| path       | String | 是        | 无       | 需要创建目录的全路径，以"/"开头,以"/"结尾，api会补齐          |
| biz_attr   | String | 是        | 空       | 新的目录绑定的属性信息                              |

##### 返回结果说明

通过类的成员变量Json::Value retJson返回请求结果

| **参数名** | **类型** | **参数描述**  |
| ------- | ------ | --------- |
| code    | Int    | 错误码，成功时为0 |
| message | String | 错误信息      |

##### 示例

```
Cosapi api("your appid", "your secretId", "your secretKey", "interface timeout");
string bucketName = "myBucket";
string path = "/myFolder/";
string bizAttr = "attr_folder";
int result  = api.updateFolder(bucketName, path,bizAttr);
api.dump_res();
```



#### 目录查询

接口说明：用于目录属性的查询，可以通过此接口查询目录的属性。

##### 方法原型

```c++
int statFolder(const string &bucketName, const string &path);  
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| bucketName | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| path       | String | 是        | 无       | 目录的全路径，以"/"开头,以"/"结尾，api会补齐              |

##### 返回结果说明

通过类的成员变量Json::Value retJson返回请求结果

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

```c++
Cosapi api("your appid", "your secretId", "your secretKey", "interface timeout");
string bucketName = "myBucket";
string path = "/myFolder/";
int result  = api.statFolder(bucketName, path);
api.dump_res();
```



#### 目录删除

接口说明：用于目录的删除，可以通过此接口删除空目录，如果目录中存在有效文件或目录，将不能删除。

##### 方法原型

```c++
int delFolder(const string &bucketName, const string &path); 
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| bucketName | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| path       | String | 是        | 无       | 目录的全路径，以"/"开头,以"/"结尾，api会补齐              |

##### 返回结果说明

通过类的成员变量Json::Value retJson返回请求结果

| **参数名** | **类型** | **参数描述**  |
| ------- | ------ | --------- |
| code    | Int    | 错误码，成功时为0 |
| message | String | 错误信息      |

##### 示例

```c++
Cosapi api("your appid", "your secretId", "your secretKey", "interface timeout");
string bucketName = "myBucket";
string path = "/myFolder/";
int result  = api.delFolder(bucketName, path);
api.dump_res();
```



#### 列举目录下文件&目录

接口说明：用于列举目录下文件和目录，可以通过此接口查询目录下的文件和目录属性。

##### 方法原型

```c++
int listFolder(const string &bucketName, const string &path, const int num = 20, const string &pattern = "eListBoth", const int order = 0, const string &context = "");
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值**   | **参数描述**                                 |
| ---------- | ------ | -------- | --------- | ---------------------------------------- |
| bucketName | String | 是        | 无         | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| path       | String | 是        | 无         | 目录的全路径，以"/"开头,以"/"结尾，api会补齐              |
| num        | int    | 否        | 20        | 要查询的目录/文件数量                              |
| context    | String | 否        | 空         | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页 |
| order      | int    | 否        | 0         | 默认正序(=0), 填1为反序                          |
| pattern    | String | 否        | eListBoth | eListBoth,eListDirOnly,eListFileOnly 默认eListBoth |

##### 返回结果说明

通过类的成员变量Json::Value retJson返回请求结果

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
| data.infos.access_url | String | 否(当类型为文件时返回) | 生成的下载url                                 |

##### 示例

```c++
Cosapi api("your appid", "your secretId", "your secretKey", "interface timeout");
string bucketName = "myBucket";
string path = "/myFolder/";
int result  = api.listFolder(bucketName, path);
api.dump_res();
```



#### 列举目录下指定前缀文件&目录

接口说明：用于列举目录下指定前缀的文件和目录，可以通过此接口查询目录下的指定前缀的文件和目录信息。

##### 方法原型

```c++
int prefixSearch(const string &bucketName, const string &path, const int num = 20, const string &pattern = "eListBoth", const int order = 0, const string &context = ""); 
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| bucketName | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| prefix     | String | 是        | 无       | 列出含此前缀的所有文件(带全路径)                        |
| num        | int    | 是        | 无       | 要查询的目录/文件数量                              |
| context    | String | 是        | 无       | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页 |
| order      | int    | 是        | 无       | 默认正序(=0), 填1为反序                          |
| pattern    | String | 是        | 无       | eListBoth,eListDirOnly,eListFileOnly 默认eListBoth |

##### 返回结果说明

通过类的成员变量Json::Value retJson返回请求结果

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
| data.infos.access_url | String | 否(当类型为文件时返回) | 生成的下载url                                 |

##### 示例

```c++
Cosapi api("your appid", "your secretId", "your secretKey", "interface timeout");
string bucketName = "myBucket";
string path = "/myFolder/";
int result  = api.prefixSearch(bucketName, path);
api.dump_res();
```



### 文件操作

#### 文件上传

接口说明：用于较小文件(一般小于8MB)的上传，可以通过此接口上传较小的文件并获得文件的url，较大的文件请使用分片上传接口。

##### 方法原型

```c++
int upload(const string &srcPath, const string &bucketName, const string &dstPath, const string &bizAttr = ""); 
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| srcPath    | String | 是        | 无       | 本地要上传文件的全路径                              |
| bucketName | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| dstPath    | String | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname       |
| bizAttr    | String | 否        | 空       | 文件属性，业务端维护                               |

##### 返回结果说明

通过类的成员变量Json::Value retJson返回请求结果

| **参数名**            | **类型** | **是否必然返回** | **参数描述**                   |
| ------------------ | ------ | ---------- | -------------------------- |
| code               | Int    | 是          | 错误码，成功时为0                  |
| message            | String | 是          | 错误信息                       |
| data               | Array  | 是          | 返回数据                       |
| data.access_url    | Bool   | 是          | 生成的文件下载url                 |
| data.url           | String | 是          | 操作文件的url                   |
| data.resource_path | String | 是          | 资源路径. 格式:/appid/bucket/xxx |

##### 示例

```c++
Cosapi api("your appid", "your secretId", "your secretKey", "interface timeout");
string srcPath= "/data/test.mp4";
string bucketName = "myBucket";
string dstPath = "/myFolder/test.mp4";
int result  = api.upload(srcPath,bucketName,dstPath);
api.dump_res();
```



#### 文件分片上传

接口说明：用于较大文件(一般大于8MB)的上传，可以通过此接口上传较大文件并获得文件的url和唯一标识resource_path（用于调用其他api）。

##### 方法原型

```c++
int upload_slice(const string &srcPath,  const string &bucketName, const string &dstPath, const string &bizAttr = "", const int sliceSize = 0, const string &session = "");
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值**    | **参数描述**                                 |
| ---------- | ------ | -------- | ---------- | ---------------------------------------- |
| srcPath    | String | 是        | 无          | 本地要上传文件的全路径                              |
| bucketName | String | 是        | 无          | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| dstPath    | String | 是        | 无          | 文件在COS服务端的全路径，不包括/appid/bucketname       |
| bizAttr    | String | 否        | 空          | 文件属性，业务端维护                               |
| sliceSize  | Int    | 否        | 512*1024字节 | 分片大小，用户可以根据网络状况自行设置                      |
| session    | String | 否        | 空          | 如果是断点续传, 则带上(唯一标识此文件传输过程的id, 由后台下发, 调用方透传) |

##### 返回结果说明

通过类的成员变量Json::Value retJson返回请求结果：

| **参数名**            | **类型** | **必然返回** | **参数描述**                   |
| ------------------ | ------ | -------- | -------------------------- |
| code               | Int    | 是        | 错误码，成功时为0                  |
| message            | String | 是        | 错误信息                       |
| data               | Array  | 是        | 返回数据                       |
| data.access_url    | Bool   | 是        | 生成的文件下载url                 |
| data.url           | String | 是        | 操作文件的url                   |
| data.resource_path | String | 是        | 资源路径. 格式:/appid/bucket/xxx |

##### 示例

```c++
Cosapi api("your appid", "your secretId", "your secretKey", "interface timeout");
string srcPath= "/data/test.mp4";
string bucketName = "myBucket";
string dstPath = "/myFolder/test.mp4";
int result  = api.upload_slice(srcPath,bucketName,dstPath);
api.dump_res();
```



#### 文件属性更新

接口说明：用于目录业务自定义属性的更新，可以通过此接口更新业务的自定义属性字段。

##### 方法原型

```C++
int update(const string &bucketName, const string &path, const string &biz_attr = "");
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| bucketName | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| path       | String | 是        | 无       | 文件在对象存储服务端的全路径，不包括/appid/bucketname      |
| biz_attr   | String | 否        | 无       | 待更新的文件属性信息                               |

##### 返回结果说明

通过类的成员变量Json::Value retJson返回请求结果

| **参数名** | **类型** | **是否必然返回** | **参数描述**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | 是          | 错误码，成功时为0 |
| message | String | 是          | 错误信息      |

##### 示例

```c++
Cosapi api("your appid", "your secretId", "your secretKey", "interface timeout");
string path = "/data/test.mp4";
string bucketName = "myBucket";
int result = api.update(bucketName,path);
api.dump_res();
```



#### 文件查询

接口说明：用于文件的查询，可以通过此接口查询文件的各项属性信息。

##### 方法原型

```c++
int stat(const string &bucketName, const string &path); 
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| bucketName | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| path       | String | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname       |

##### 返回结果说明

通过类的成员变量Json::Value retJson返回请求结果

| **参数名**         | **类型** | **必然返回** | **参数描述**                       |
| --------------- | ------ | -------- | ------------------------------ |
| code            | Int    | 是        | 错误码，成功时为0                      |
| message         | String | 是        | 错误信息                           |
| data            | Array  | 是        | 文件属性数据                         |
| data.name       | String | 是        | 文件或目录名                         |
| data.biz_attr   | String | 是        | 文件属性，业务端维护                     |
| data.ctime      | String | 是        | 文件的创建时间，unix时间戳                |
| data.mtime      | String | 是        | 文件的修改时间，unix时间戳                |
| data.filesize   | Int    | 是        | 文件大小                           |
| data.filelen    | Int    | 是        | 文件已传输大小(通过与filesize对比可知文件传输进度) |
| data.sha        | String | 是        | 文件sha                          |
| data.access_url | String | 是        | 生成的文件下载url                     |

##### 示例

```c++
Cosapi api("your appid", "your secretId", "your secretKey", "interface timeout");
string bucketName = "myBucket";
string path = "/myFolder/test.mp4";
int result = api.stat(bucketName, path);
api.dump_res();
```



#### 文件删除

接口说明：用于文件的删除，可以通过此接口删除已经上传的文件。

##### 方法原型

```c++
int del(const string &bucketName, const string &path); 
```

##### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| bucketName | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/cos) |
| path       | String | 是        | 无       | 文件在对象存储服务端的全路径，不包括/appid/bucketname      |

##### 返回结果说明

通过类的成员变量Json::Value retJson返回请求结果

| **参数名** | **类型** | **是否必然返回** | **参数描述**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | 是          | 错误码，成功时为0 |
| message | String | 是          | 错误信息      |

##### 示例

```c++
Cosapi api("your appid", "your secretId", "your secretKey", "interface timeout");
string bucketName = "myBucket";
string path = "/myFolder/test.mp4";
int result = api.del(bucketName, path);
api.dump_res();
```



