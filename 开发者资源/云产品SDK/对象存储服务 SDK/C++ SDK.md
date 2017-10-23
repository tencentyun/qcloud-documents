##  开发准备

### SDK 获取

对象存储服务的C++ SDK的下载地址： [https://github.com/tencentyun/cos-cpp-sdk/tree/3.3.0](https://github.com/tencentyun/cos-cpp-sdk/tree/3.3.0)

### 开发环境

1. 安装openssl的库和头文件 [http://www.openssl.org/source/](http://www.openssl.org/source/) 
2. 安装curl的库和头文件 [http://curl.haxx.se/download/curl-7.43.0.tar.gz](http://curl.haxx.se/download/curl-7.43.0.tar.gz) 
3. 安装jsoncpp的库和头文件 [https://github.com/open-source-parsers/jsoncpp](https://github.com/open-source-parsers/jsoncpp) 
4. 安装cmake工具 [http://www.cmake.org/download/](http://www.cmake.org/download/) 
5. 从控制台获取APP ID、SecretID、SecretKey，详情参考[权限控制](https://cloud.tencent.com/doc/product/227/1897#2.1-.E8.8E.B7.E5.8F.96.E7.AD.BE.E5.90.8D.E6.89.80.E9.9C.80.E4.BF.A1.E6.81.AF)。



注意：

1. sdk中提供了curl和jsoncpp的库以及头文件，以上库编译好后替换掉sdk中相应的库和头文件即可，如果以上库已经安装到系统里，也可删除sdk中相应的库和头文件。
2. curl默认不支持多线程环境，如果项目使用多线程，在编译curl执行 configure 时需指定 --enable-ares 参数来开启异步DNS解析，依赖 c-ares库，如果系统没有，可到[http://c-ares.haxx.se/](http://c-ares.haxx.se/) 下载安装。
3. jsoncpp的1.y.x版本需要c++11的支持，如果编译器不支持，可以换成 0.y.x版本。


### SDK 配置

直接下载github上提供的源代码，集成到您的开发环境。 

执行下面的命令 ：

```
cd ${cos-cpp-sdk} 
mkdir -p build 
cd build 
cmake .. 
make 
```

cos_demo.cpp里面有常见API的例子，需要将cos_demo.cpp里的appid、secretId、secretKey、bucket等信息换成自己的信息。

生成的cos_demo就可以直接运行，试用，生成的静态库，名称为：libcosdk.a。 

生成的 libcosdk.a 放到你自己的工程里lib路径下， include 目录下的 auth_utility.h cos_api.h curl json openssl 都放到你自己的工程的include路径下。 

例如项目里只有一个 sample.cpp ，项目目录和sdk在同级目录， copy libcosdk.a 到项目所在目录那么编译命令为: 

```
g++ -o sample sample.cpp -I ./include/ -L. -L../cos-cpp-sdk/lib/ -lcosdk -lcurl -lcrypto -lssl -lrt -ljsoncpp
```

若需要 HTTPS 支持，修改 cos_api_defines 中kApiCosapiEndpoint  的值为：

[https://web.file.myqcloud.com/files/v1/](https://web.file.myqcloud.com/files/v1/)

## 生成签名

### 多次有效签名

#### 方法原型

```c++
static string AppSignMuti(const uint64_t appId, 
                          const string &secretId, 
                          const string &secretKey, 
                          const uint64_t expired_time, 
                          const string &bucketName); 
```

#### 参数说明

| 参数名          | **类型**   | **是否必填** | **默认值** | **参数描述**                                 |
| ------------ | -------- | -------- | ------- | ---------------------------------------- |
| appId        | uint64_t | 是        | 无       | 项目APP ID                                 |
| secretId     | String   | 是        | 无       | 用户 Secret ID                             |
| secretKey    | String   | 是        | 无       | 用户 SecretKey                             |
| expired_time | uint64_t | 否        | 无       | 过期时间，Unix时间戳                             |
| bucketName   | String   | 否        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |

#### 返回结果说明

返回值：签名字符串

#### 示例

```c++
uint64_t expired = time(NULL) + 60;
string sign = AuthUtility::AppSignMuti(10000000, "SecretId", 
                                       "SecretKey", expired , 
                                       "bucketName");
```

### 单次有效签名

#### 方法原型

```c++
static string AppSignOnce(const uint64_t appId, 
                          const string &secretId, 
                          const string &secretKey, 
                          const string &path, 
                          const string &bucketName); 
```

#### 参数说明

| **参数名**    | **类型**   | **必须** | **默认值** | **参数描述**                                 |
| ---------- | -------- | ------ | ------- | ---------------------------------------- |
| appId      | uint64_t | 是      | 无       | 项目 APP ID                                |
| secretId   | String   | 是      | 无       | 项目 SecretID                              |
| secretKey  | String   | 是      | 无       | 项目 SecretKey                             |
| bucketName | String   | 否      | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| path       | String   | 是      | 无       | 文件路径，以斜杠开头，例如/filepath/filename，为文件在此bucketname下的全路径 |

#### 返回结果说明

返回值：签名字符串

#### 示例

```c++
string path= "/myFloder/myFile.rar";
sign = AuthUtility::AppSignOnce(10000000, "SecretId", "SecretKey", path, bucketName);
```

更多签名相关详细说明，请参考[权限控制](https://cloud.tencent.com/doc/product/227/1897#2.1-.E8.8E.B7.E5.8F.96.E7.AD.BE.E5.90.8D.E6.89.80.E9.9C.80.E4.BF.A1.E6.81.AF) 。

## 初始化操作

### 初始化

接口说明：在使用CosApi进行操作之前，需要首先初始化使用的库和资源。

#### 方法原型

```c++
int COS_Init();
```

#### 返回结果说明

返回0代表成功，否则代表失败

## 目录操作

### 创建目录

接口说明：用于目录的创建，调用者可以通过此接口在指定bucket下创建目录。

#### 方法原型

```c++
string CreateFolder(const string &bucketName, 
                    const string &path, 
                    const CustomOptions& options = CustomOptions()); 
```

#### 参数说明

| **参数名**    | **类型**        | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------------- | -------- | ------- | ---------------------------------------- |
| bucketName | String        | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| path       | String        | 是        | 无       | 需要创建目录的全路径，以"/"开头,以"/"结尾，api会补齐          |
| options    | CustomOptions | 否        | 空       | 用户自定义选项，为一组key-value对                    |

#### 返回结果说明

通过函数返回值返回请求结果的json字符串

| **参数名**            | **类型** | **参数描述**        |
| ------------------ | ------ | --------------- |
| code               | Int    | 错误码，成功时为0       |
| message            | String | 错误信息            |
| data               | Array  | 返回数据            |
| data.ctime         | String | 目录的创建时间，unix时间戳 |
| data.resource_path | String | 目录的资源路径         |

#### 示例

```c++
CosApiClientOption client_option("your appid", "your secretId", "your secretKey");
CosApi cos_client(client_option);
string bucketName = "myBucket";
string path = "/myFolder/";
CustomOptions options;
options.AddStringOption("biz_attr", "attr_folder");
string result  = cos_client.CreateFolder(bucketName, path, options);
```

### 目录属性更新

接口说明：用于目录业务自定义属性的更新，可以通过此接口更新业务的自定义属性字段。

#### 方法原型

```c++
string UpdateFolder(const string &bucketName, 
                    const string &path, 
                    const CustomOptions& options); 
```

#### 参数说明

| **参数名**    | **类型**        | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------------- | -------- | ------- | ---------------------------------------- |
| bucketName | String        | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cost) |
| path       | String        | 是        | 无       | 需要创建目录的全路径，以"/"开头,以"/"结尾，api会补齐          |
| options    | CustomOptions | 否        | 空       | 用户自定义选项，为一组key-value对                    |

#### Options说明

| **参数名**  | **类型** | **是否必填** | **默认值** | **参数描述**      |
| -------- | ------ | -------- | ------- | ------------- |
| biz_attr | String | 否        | ""      | 目录/文件属性，业务端维护 |

#### 返回结果说明

通过函数返回值返回请求结果的json字符串

| **参数名** | **类型** | **参数描述**  |
| ------- | ------ | --------- |
| code    | Int    | 错误码，成功时为0 |
| message | String | 错误信息      |

#### 示例

```
CosApiClientOption client_option("your appid", "your secretId", "your secretKey");
CosApi cos_client(client_option);
string bucketName = "myBucket";
string path = "/myFolder/";
CustomOptions options;
options.AddStringOption("biz_attr", "attr_folder");
string result  = cos_client.UpdateFolder(bucketName, path, options);
```

### 目录查询

接口说明：用于目录属性的查询，可以通过此接口查询目录的属性。

#### 方法原型

```c++
string StatFolder(const string &bucketName, const string &path);  
```

#### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| bucketName | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| path       | String | 是        | 无       | 目录的全路径，以"/"开头,以"/"结尾，api会补齐              |

#### 返回结果说明

通过函数返回值返回请求结果的json字符串

| **参数名**       | **类型** | **参数描述**         |
| ------------- | ------ | ---------------- |
| code          | Int    | 错误码，成功时为0        |
| message       | String | 错误信息             |
| data          | Array  | 目录属性数据           |
| data.biz_attr | String | 目录绑定的属性信息，业务自行维护 |
| data.ctime    | String | 目录的创建时间，unix时间戳  |
| data.mtime    | String | 目录的修改时间，unix时间戳  |
| data.name     | String | 目录的名称            |

#### 示例

```c++
CosApiClientOption client_option("your appid", "your secretId", "your secretKey");
CosApi cos_client(client_option);
string bucketName = "myBucket";
string path = "/myFolder/";
string result  = cos_client.StatFolder(bucketName, path, options);
```

### 目录删除

接口说明：用于目录的删除，可以通过此接口删除空目录，如果目录中存在有效文件或目录，将不能删除。

#### 方法原型

```c++
string DelFolder(const string &bucketName, const string &path); 
```

#### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| bucketName | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| path       | String | 是        | 无       | 目录的全路径，以"/"开头,以"/"结尾，api会补齐              |

#### 返回结果说明

通过函数返回值返回请求结果的json字符串

| **参数名** | **类型** | **参数描述**  |
| ------- | ------ | --------- |
| code    | Int    | 错误码，成功时为0 |
| message | String | 错误信息      |

#### 示例

```c++
CosApiClientOption client_option("your appid", "your secretId", "your secretKey");
CosApi cos_client(client_option);
string bucketName = "myBucket";
string path = "/myFolder/";
string result  = cos_client.DelFolder(bucketName, path, options);
```

### 列举目录下文件&目录

接口说明：用于列举目录下文件和目录，可以通过此接口查询目录下的文件和目录属性。

#### 方法原型

```c++
string ListFolder(const string &bucketName, 
                  const string &path, 
                  const CustomOptions& options = DefaultListOptions());
```

#### 参数说明

| **参数名**    | **类型**        | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------------- | -------- | ------- | ---------------------------------------- |
| bucketName | String        | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| path       | String        | 是        | 无       | 目录的全路径，以"/"开头,以"/"结尾，api会补齐              |
| options    | CustomOptions | 否        | 空       | 用户自定义选项，为一组key-value对                    |

#### Options说明

| **参数名** | **类型** | **是否必填** | **默认值**   | **参数描述**                                 |
| ------- | ------ | -------- | --------- | ---------------------------------------- |
| num     | int    | 否        | 20        | 拉去总数                                     |
| order   | int    | 否        | 0         | 0是正序，1是反序                                |
| pattern | String | 否        | eListBoth | eListBoth,eListDirOnly,eListFileOnly     |
| context | String | 否        | 空字符串      | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中 |

#### 返回结果说明

通过函数返回值返回请求结果的json字符串

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

#### 示例

```c++
CosApiClientOption client_option("your appid", "your secretId", "your secretKey");
CosApi cos_client(client_option);
string bucketName = "myBucket";
string path = "/myFolder/";
CustomOptions options;
options.AddUIntOption("num", 20);
options.AddUIntOption("order", 0);
options.AddStringOption("pattern", "eListBoth");
options.AddStringOption("context", "");
string result  = cos_client.ListFolder(bucketName, path, options);
```

### 列举目录下指定前缀文件&目录

接口说明：用于列举目录下指定前缀的文件和目录，可以通过此接口查询目录下的指定前缀的文件和目录信息。

#### 方法原型

```c++
string PrefixSearch(const string &bucketName, 
                    const string &path, 
                    const CustomOptions& options = DefaultListOptions()); 
```

#### 参数说明

| **参数名**    | **类型**        | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------------- | -------- | ------- | ---------------------------------------- |
| bucketName | String        | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| prefix     | String        | 是        | 无       | 列出含此前缀的所有文件(带全路径)                        |
| options    | CustomOptions | 否        | 空       | 用户自定义选项，为一组key-value对                    |

#### Options说明

| **参数名** | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ------- | ------ | -------- | ------- | ---------------------------------------- |
| num     | int    | 是        | 20      | 要查询的目录/文件数量                              |
| context | String | 是        | 无       | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页 |
| order   | int    | 是        | 无       | 默认正序(=0), 填1为反序                          |
| pattern | String | 是        | 无       | eListBoth,eListDirOnly,eListFileOnly 默认eListBoth |

#### 返回结果说明

通过函数返回值返回请求结果的json字符串

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

#### 示例

```c++
CosApiClientOption client_option("your appid", "your secretId", "your secretKey");
CosApi cos_client(client_option);
string bucketName = "myBucket";
string path = "/myFolder/";
string result  = cos_client.PrefixSearch(bucketName, path);
```

## 文件操作

### 文件上传

接口说明：用于较小文件(一般小于8MB)的上传，可以通过此接口上传较小的文件并获得文件的url，较大的文件请使用分片上传接口。

#### 方法原型

```c++
string Upload(const string &srcPath, 
              const string &bucketName, 
              const string &dstPath, 
              const CustomOptions& options = DefaultUploadOptions()); 
```

#### 参数说明

| **参数名**    | **类型**        | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------------- | -------- | ------- | ---------------------------------------- |
| srcPath    | String        | 是        | 无       | 本地要上传文件的全路径                              |
| bucketName | String        | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| dstPath    | String        | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname       |
| options    | CustomOptions | 否        | 空       | 用户自定义选项，为一组key-value对                    |

#### Options说明

| **参数名**  | **类型** | **是否必填** | **默认值** | **参数描述        |
| -------- | ------ | -------- | ------- | ------------- |
| biz_attr | String | 否        | ""      | 目录/文件属性，业务端维护 |

#### 返回结果说明

通过函数返回值返回请求结果的json字符串

| **参数名**            | **类型** | **是否必然返回** | **参数描述**                   |
| ------------------ | ------ | ---------- | -------------------------- |
| code               | Int    | 是          | 错误码，成功时为0                  |
| message            | String | 是          | 错误信息                       |
| data               | Array  | 是          | 返回数据                       |
| data.access_url    | Bool   | 是          | 生成的文件下载url                 |
| data.url           | String | 是          | 操作文件的url                   |
| data.resource_path | String | 是          | 资源路径. 格式:/appid/bucket/xxx |

#### 示例

```c++
CosApiClientOption client_option("your appid", "your secretId", "your secretKey");
CosApi cos_client(client_option);
string bucketName = "myBucket";
string srcPath= "/data/test.mp4";
string dstPath = "/myFolder/test.mp4";
CustomOptions upload_options;
upload_options.AddStringOption("biz_attr", "test");
string result = cos_client.Upload(srcPath, bucketName, dstPath, upload_options);
```

### 文件分片上传

接口说明：用于较大文件(一般大于8MB)的上传，可以通过此接口上传较大文件并获得文件的url和唯一标识resource_path（用于调用其他api）。

#### 方法原型

```c++
string UploadSlice(const string &srcPath, 
                   const string &bucketName, 
                   const string &dstPath, 
                   const CustomOptions& options = DefaultUploadSliceOptions());
```

#### 参数说明

| **参数名**    | **类型**        | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------------- | -------- | ------- | ---------------------------------------- |
| srcPath    | String        | 是        | 无       | 本地要上传文件的全路径                              |
| bucketName | String        | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| dstPath    | String        | 是        | 无       | 上传到cos的路径                                |
| options    | CustomOptions | 否        | 空       | 用户自定义选项，为一组key-value对                    |

#### Options说明

| **参数名**    | **类型** | **是否必填** | **默认值**    | **参数描述**            |
| ---------- | ------ | -------- | ---------- | ------------------- |
| slice_size | Int    | 是        | 512*1024字节 | 分片大小，用户可以根据网络状况自行设置 |
| biz_attr   | String | 否        | 空          | 文件属性，业务端维护          |
| insertOnly | String | 否        | 1          | 是否覆盖文件，0-允许，1-不允许   |

#### 返回结果说明

通过函数返回值返回请求结果的json字符串：

| **参数名**            | **类型** | **必然返回** | **参数描述**                   |
| ------------------ | ------ | -------- | -------------------------- |
| code               | Int    | 是        | 错误码，成功时为0                  |
| message            | String | 是        | 错误信息                       |
| data               | Array  | 是        | 返回数据                       |
| data.access_url    | Bool   | 是        | 生成的文件下载url                 |
| data.url           | String | 是        | 操作文件的url                   |
| data.resource_path | String | 是        | 资源路径. 格式:/appid/bucket/xxx |

#### 示例

```c++
CosApiClientOption client_option("your appid", "your secretId", "your secretKey");
CosApi cos_client(client_option);
string bucketName = "myBucket";
string srcPath= "/data/test.mp4";
string dstPath = "/myFolder/test.mp4";
CustomOptions upload_options;
upload_options.AddStringOption("biz_attr", "test");
string result = cos_client.UploadSlice(srcPath, bucketName, dstPath, upload_options);
```

### 文件属性更新

接口说明：用于目录业务自定义属性的更新，可以通过此接口更新业务的自定义属性字段。

#### 方法原型

```C++
int UpdateFile(const string &bucketName, 
               const string &path, 
               const CustomOptions& options = CustomOptions());
```

#### 参数说明

| **参数名**    | **类型**        | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------------- | -------- | ------- | ---------------------------------------- |
| bucketName | String        | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| path       | String        | 是        | 无       | 文件在对象存储服务端的全路径，不包括/appid/bucketname      |
| options    | CustomOptions | 否        | 空       | 用户自定义选项，为一组key-value对                    |

#### Options说明

| **参数名**  | **类型** | **是否必填** | **默认值** | **参数描述**   |
| -------- | ------ | -------- | ------- | ---------- |
| biz_attr | String | 否        | 无       | 待更新的文件属性信息 |

#### 返回结果说明

通过函数返回值返回请求结果的json字符串：

| **参数名** | **类型** | **是否必然返回** | **参数描述**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | 是          | 错误码，成功时为0 |
| message | String | 是          | 错误信息      |

#### 示例

```c++
CosApiClientOption client_option("your appid", "your secretId", "your secretKey");
CosApi cos_client(client_option);
string bucketName = "myBucket";
string path = "/data/test.mp4";
string result = cos_client.UpdateFile(bucketName， path);
```

### 文件查询

接口说明：用于文件的查询，可以通过此接口查询文件的各项属性信息。

#### 方法原型

```c++
int Stat(const string &bucketName, const string &path); 
```

#### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| bucketName | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| path       | String | 是        | 无       | 文件在COS服务端的全路径，不包括/appid/bucketname       |

#### 返回结果说明

通过函数返回值返回请求结果的json字符串

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

#### 示例

```c++
CosApiClientOption client_option("your appid", "your secretId", "your secretKey");
CosApi cos_client(client_option);
string bucketName = "myBucket";
string path = "/data/test.mp4";
string result = cos_client.StatFile(bucketName, path);
```

### 文件删除

接口说明：用于文件的删除，可以通过此接口删除已经上传的文件。

#### 方法原型

```c++
int DelFile(const string &bucketName, const string &path); 
```

#### 参数说明

| **参数名**    | **类型** | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------ | -------- | ------- | ---------------------------------------- |
| bucketName | String | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| path       | String | 是        | 无       | 文件在对象存储服务端的全路径，不包括/appid/bucketname      |

#### 返回结果说明

通过函数返回值返回请求结果的json字符串

| **参数名** | **类型** | **是否必然返回** | **参数描述**  |
| ------- | ------ | ---------- | --------- |
| code    | Int    | 是          | 错误码，成功时为0 |
| message | String | 是          | 错误信息      |

#### 示例

```c++
CosApiClientOption client_option("your appid", "your secretId", "your secretKey");
CosApi cos_client(client_option);
string bucketName = "myBucket";
string path = "/data/test.mp4";
string result = cos_client.DelFile(bucketName, path);
```

### 文件移动

接口说明：用于文件移动，可以通过此接口移动已经上传的文件。

方法原型

```c++
std::string MoveFile(
    const std::string& bucketName,
    const std::string& srcPath,
    const std::string& dstPath,
    const CustomOptions& options = DefaultRenameFileOptions()
);
```
#### 参数说明

| **参数名**    | **类型**        | **是否必填** | **默认值** | **参数描述**                                 |
| ---------- | ------------- | -------- | ------- | ---------------------------------------- |
| bucketName | String        | 是        | 无       | bucket名称，bucket创建参见[创建Bucket](http://console.cloud.tencent.com/cos) |
| srcPath    | String        | 是        | 无       | 要移动文件的源地址                                |
| dstPath    | String        | 是        | 无       | 要移动到的目的地址                                |
| options    | CustomOptions | 否        | 空       | 用户自定义选项，为一组key-value对                    |

#### 返回结果说明

通过函数返回值返回请求结果的json字符串

| **参数名** | **类型** | **是否必然返回** | **参数描述    |
| ------- | ------ | ---------- | --------- |
| code    | Int    | 是          | 错误码，成功时为0 |
| message | String | 是          | 错误信息      |

#### 示例

```c++
CosApiClientOption client_option("your appid", "your secretId", "your secretKey");
CosApi cos_client(client_option);
string bucketName = "myBucket";
string srcPath = "/data/test.mp4";
string dstPath = "/data/test.mp4.rename";
string result = cos_client.MoveFile(bucketName, srcPath, dstPath);
```
