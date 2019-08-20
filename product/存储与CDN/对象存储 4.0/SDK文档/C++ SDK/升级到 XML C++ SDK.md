如果您细心对比过 JSON C++ SDK 和 XML C++ SDK 的文档，您会发现并不是一个简单的增量更新。XML C++ SDK 不仅在架构、可用性和安全性上有了非常大的提升，而且在易用性、健壮性和传输性能上也做了非常大的改进。如果您想升级到 XML C++ SDK，请参考下面的指引，完成 C++ SDK 的升级工作。

## 功能对比

XML C++ SDK 与 JSON C++ SDK 功能对比请查看下表：

| 功能           |                              XML C++ SDK                              |                              JSON C++ SDK                              |
| -------------- | :----------------------------------------------------------: | :----------------------------------------------------------: |
| 文件上传       | 支持本地文件、字节流、输入流上传<br>覆盖同名文件<br>简单上传最大支持5GB<br>分块上传最大支持48.82TB（50,000GB） | 支持本地文件上传，大于8M 的文件需将文件内容进行分片上传<br>需要手动设置同名文件是否覆盖<br>简单上传最大上传20MB<br>分片上传最大支持64GB |
| 存储桶基本操作 |            创建存储桶<br>获取存储桶<br>删除存储桶            |                            不支持                            |
| 存储桶 ACL 操作  |   设置存储桶 ACL<br>获取设置存储桶 ACL<br>删除设置存储桶 ACL    |                            不支持                            |
| 存储桶生命周期 | 创建存储桶生命周期<br>获取存储桶生命周期<br>删除存储桶生命周期 |                            不支持                            |
| 目录操作       |                            不单独提供接口                            |               创建目录<br>查询目录<br>删除目录               |

## 升级步骤

请按照下面4个步骤升级 C++ SDK。

**1. 更新 C++ SDK**

[XML C++ SDK ](https://github.com/tencentyun/cos-cpp-sdk-v5)使用了 Poco 库替换了 JSON C++ SDK 的 curl 库，从 [Poco官网](https://pocoproject.org/download.html) 下载 complete 版本的 Poco ，并执行以下命令安装 Poco 的库和头文件。

```
./configure --omit=Data/ODBC,Data/MySQL
make
make install
```
此外，您也可以参考 C++ SDK [快速入门](https://cloud.tencent.com/document/product/436/12301) 文档选择合适您的安装方式。

**2. 更改 SDK 配置文件**

XML C++ SDK 与 JSON C++ SDK 的初始化过程相同，但对应配置文件 "config.json" 内容不同。在 XML C++ SDK 配置文件中，请对应修改以下变化内容：

- 删除 JSON C++ SDK 中 "APPID" 配置项。
- `ConnectTimeoutInms` 代替了 `CurlConnectTimeoutInms`和`CurlGlobalConnectTimeoutInms`，新增`ReceiveTimeoutInms`，在 Request 基类中也实现对应设置接口，可针对不同操作进行修改。
- XML C++ SDK 的初始化默认参数在文件 "cos_sys_config.cpp" 中有详细说明。
- JSON C++ SDK 和 XML C++ SDK 对应 Region 描述不同，详细区别见下方“更改存储桶名称和可用域简称”。

**3. 更改存储桶名称和可用区域简称**

XML C++ SDK 的存储桶名称和可用区域简称与 JSON C++ SDK 的不同，需要您进行相应的更改。

**存储桶 Bucket**

XML C++ SDK 存储桶名称由两部分组成：用户自定义字符串 和 APPID，两者以中划线“-”相连。例如 `mybucket1-1250000000`，其中 `mybucket1` 为用户自定义字符串，`1250000000` 为 APPID。

>?APPID 是腾讯云账户的账户标识之一，用于关联云资源。在用户成功申请腾讯云账户后，系统自动为用户分配一个 APPID。可登录腾讯云控制台后，在 [账号信息](https://console.cloud.tencent.com/developer) 查看 APPID。

设置 Bucket，请参考下面的示例代码：

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);
// JSON C++ SDK 的 AppID 是写在配置文件中的，JSON C++ SDK 的 Bucket 定义如：string bucket = "mybucket1";
string bucket = "mybucket1-1250000000";
qcloud_cos::HeadBucketReq req(bucket_name);
qcloud_cos::HeadBucketResp resp;
qcloud_cos::CosResult result = cos.HeadBucket(req, &resp);
```

**存储桶可用区域简称 Region**

XML C++ SDK 的存储桶可用区域简称发生了变化，在初始化时，请将存储桶所在区域简称设置到配置文件的 `Region` 中。不同区域在 JSON C++ SDK 和 XML C++ SDK 中的对应关系请查看下表：

| 地域             | XML C++ SDK 地域简称      | JSON C++ SDK 地域简称 |
| ---------------- | ---------------- | ----------- |
| 北京一区（华北） | ap-beijing-1     | tj          |
| 北京             | ap-beijing       | bj          |
| 上海（华东）     | ap-shanghai      | sh          |
| 广州（华南）     | ap-guangzhou     | gz          |
| 成都（西南）     | ap-chengdu       | cd          |
| 重庆             | ap-chongqing     | 无          |
| 香港             | ap-hongkong      | hk          |
| 新加坡           | ap-singapore     | sgp         |
| 多伦多           | na-toronto       | ca          |
| 法兰克福         | eu-frankfurt     | ger         |
| 孟买             | ap-mumbai        | 无          |
| 首尔             | ap-seoul         | 无          |
| 硅谷             | na-siliconvalley | 无          |
| 弗吉尼亚         | na-ashburn       | 无          |
| 曼谷             | ap-bangkok       | 无          |
| 莫斯科           | eu-moscow        | 无          |

**4. 更改 API**

升级到 XML C++ SDK 之后，一些操作的 API 发生了变化，请您根据实际需求进行相应的更改。我们同时做了封装让 SDK 更加易用，具体请参考我们的示例和 [快速入门](https://cloud.tencent.com/document/product/436/12301) 文档。

API 主要有以下变化：

**1）没有单独的目录接口**

在 XML SDK 中，不再提供单独的目录接口。对象存储中本身是没有文件夹和目录的概念的，对象存储不会因为上传对象 project/a.txt 而创建一个 project 文件夹。
为了满足用户使用习惯，对象存储在控制台、COS browser 等图形化工具中模拟了「文件夹」或「目录」的展示方式，具体实现是通过创建一个键值为`project/`，内容为空的对象，展示方式上模拟了传统文件夹。

例如：上传对象`project/doc/a.txt `，分隔符`/`会模拟「文件夹」的展示方式，在控制台上可以看到「文件夹」project 和 doc，其中 doc 是 project 下一级「文件夹」，并包含了 a.txt 文件 。

因此，如果您的应用场景只是上传文件，可以直接上传即可，不需要先创建文件夹。如果使用场景里面有文件夹的概念，则需要提供创建文件夹的功能，您可以上传一个路径以 '/' 结尾的0KB 文件。这样在您调用 GetBucket 接口时，就可以将该文件当做文件夹。

**2）多线程上传下载操作**

在 XML C++ SDK 中，我们封装了多线程分块上传和下载操作，为`MultiUploadObjectReq`和`MultiGetObjectReq`接口，对 API 设计和传输性能都能做了优化。

主要特性有：

- 可设置分块大小进行多线程上传和下载
- `MultiUploadObjectReq`接口封装了分块上传的所有接口，包括 Init、Upload、Complete 和 Abort 操作。

使用`MultiUploadObjectReq`上传的示例代码：

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);
string bucket_name = "alangz-1253960400";
string object_name = "object_key";
string local_file = "/data/test";
qcloud_cos::MultiUploadObjectReq req(bucket_name,object_name, local_file);
req.SetRecvTimeoutInms(1000 * 60);
qcloud_cos::MultiUploadObjectResp resp;
qcloud_cos::CosResult result = cos.MultiUploadObject(req, &resp);
if (result.IsSucc()) {
    std::cout << "MultiUpload Succ." << std::endl;
    std::cout << resp.GetLocation() << std::endl;
    std::cout << resp.GetKey() << std::endl;
    std::cout << resp.GetBucket() << std::endl;
    std::cout << resp.GetEtag() << std::endl;
} else {
    std::cout << "MultiUpload Fail." << std::endl;
    // 获取具体失败在哪一步
    std::string resp_tag = resp.GetRespTag();
    if ("Init" == resp_tag) {
        // print result
    } else if ("Upload" == resp_tag) {
        // print result
    } else if ("Complete" == resp_tag) {
        // print result
    }
}
```

使用`MultiGetObjectReq`下载的示例代码：

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);
string bucket_name = "alangz-1253960400";
string object_name = "object_key";
string file_path = "/data/test";
qcloud_cos::MultiGetObjectReq req(bucket_name,object_name, file_path);
qcloud_cos::MultiGetObjectResp resp;
qcloud_cos::CosResult result = cos.GetObject(req, &resp);
```

**3）签名算法不同**

通常您不需要手动计算签名，但如果您将 SDK 的签名返回给前端使用，请注意我们的签名算法发生了改变。签名不再区分单次和多次签名，而是通过设置签名的有效期来保证安全性。具体的算法请参考 [XML 请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

**4）新增API**

XML C++ SDK 新增 API，您可根据需求进行调用。包括：

- 存储桶的操作，如 PutBucketReq、GetBucketReq 等。
- 存储桶 ACL 的操作，如 PutBucketACLReq、GetBucketACLReq 等。
- 存储桶生命周期的操作，如 PutBucketLifecycleReq、GetBucketLifecycleReq 等。

具体请参考我们的 C++ SDK [快速入门](https://cloud.tencent.com/document/product/436/12301) 文档。
