## 简介

数据在客户端和服务器间传输时可能会出现错误，COS 除了可以通过 [MD5 和自定义属性](https://cloud.tencent.com/document/product/436/36427) 验证数据完整性外，还可以通过 CRC64 检验码来进行数据校验。

COS 会对新上传的对象进行 CRC64 计算，并将结果作为对象的属性进行存储，随后在返回的响应头部中携带 x-cos-hash-crc64ecma，该头部表示上传对象的 CRC64 值，根据 [ECMA-182标准]( https://www.ecma-international.org/publications/standards/Ecma-182.htm) 计算得到。对于 CRC64 特性上线前就已经存在于 COS 的对象，COS 不会对其计算 CRC64 值，所以获取此类对象时不会返回其 CRC64 值。

## 操作说明

目前支持 CRC64 的 API 如下：

- 简单上传接口
	- [PUT Object](https://cloud.tencent.com/document/product/436/7749) 和 [POST Object](https://cloud.tencent.com/document/product/436/14690)：用户可在返回的响应头中获得文件 CRC64 校验值。
- 分块上传接口
	- [Upload Part](https://cloud.tencent.com/document/product/436/7750)：用户可以根据 COS 返回的 CRC64 值与本地计算的数值进行比较验证。
	- [Complete Multipart Upload](https://cloud.tencent.com/document/product/436/7742)：如果每个分块都有 CRC64 属性，则会返回整个对象的 CRC64 值，如果某些分块不具备 CRC64 值，则不返回。
- 执行 [Upload Part - Copy](https://cloud.tencent.com/document/product/436/8287) 时，会返回对应的 CRC64 值。
- 执行 [PUT Object - Copy](https://cloud.tencent.com/document/product/436/10881) 时，如果源对象存在 CRC64 值，则返回 CRC64，否则不返回。
- 执行 [HEAD Object](https://cloud.tencent.com/document/product/436/7745) 和 [GET Object](https://cloud.tencent.com/document/product/436/7753) 时，如果对象存在 CRC64，则返回。用户可以根据 COS 返回的 CRC64 值和本地计算的 CRC64 进行比较验证。

## API 接口示例

#### 分块上传响应

下面为用户发出 Upload Part 请求后得到的响应示例。x-cos-hash-crc64ecma 头部表示分块的 CRC64 值，用户可以通过该值与本地计算的 CRC64 值进行比较，从而校验分块完整性。

```shell
HTTP/1.1 200 OK
content-length: 0
connection: close
date: Thu, 05 Dec 2019 01:58:03 GMT
etag: "358e8c8b1bfa35ee3bd44cb3d2cc416b"
server: tencent-cos
x-cos-hash-crc64ecma: 15060521397700495958
x-cos-request-id: NWRlODY0MmJfMjBiNDU4NjRfNjkyZl80ZjZi****
```

#### 完成分块上传响应

下面为用户发出 Complete Multipart Upload 请求后得到的响应示例。x-cos-hash-crc64ecma 头部表示整个对象的 CRC64 值，用户可以通过该值与本地计算的 CRC64 值进行比较，从而校验对象完整性。

```shell
HTTP/1.1 200 OK
content-type: application/xml
transfer-encoding: chunked
connection: close
date: Thu, 05 Dec 2019 02:01:17 GMT
server: tencent-cos
x-cos-hash-crc64ecma: 15060521397700495958
x-cos-request-id: NWRlODY0ZWRfMjNiMjU4NjRfOGQ4Ml81MDEw****

[Object Content]
```

## SDK 示例

#### 功能说明

用于在对象上传和下载的时候对对象数据做 crc64 一致性校验。

#### 方法原型

```cpp
cos_status_t *cos_upload_part_from_buffer(const cos_request_options_t *options,
                                          const cos_string_t *bucket, 
                                          const cos_string_t *object, 
                                          const cos_string_t *upload_id, 
                                          int part_num, 
                                          cos_list_t *buffer, 
                                          cos_table_t **resp_headers);

cos_status_t *cos_upload_part_from_file(const cos_request_options_t *options,
                                        const cos_string_t *bucket, 
                                        const cos_string_t *object,
                                        const cos_string_t *upload_id, 
                                        int part_num, 
                                        cos_upload_file_t *upload_file,
                                        cos_table_t **resp_headers);

cos_status_t *cos_download_part_to_file(const cos_request_options_t *options,
                                        const cos_string_t *bucket, 
                                        const cos_string_t *object,
                                        cos_upload_file_t *download_file,
                                        cos_table_t **resp_headers);

cos_status_t *cos_put_object_from_buffer(const cos_request_options_t *options,
                                         const cos_string_t *bucket, 
                                         const cos_string_t *object, 
                                         cos_list_t *buffer,
                                         cos_table_t *headers, 
                                         cos_table_t **resp_headers);

cos_status_t *cos_put_object_from_file(const cos_request_options_t *options,
                                       const cos_string_t *bucket, 
                                       const cos_string_t *object, 
                                       const cos_string_t *filename,
                                       cos_table_t *headers, 
                                       cos_table_t **resp_headers);

cos_status_t *cos_get_object_to_buffer(const cos_request_options_t *options, 
                                       const cos_string_t *bucket, 
                                       const cos_string_t *object,
                                       cos_table_t *headers, 
                                       cos_table_t *params,
                                       cos_list_t *buffer, 
                                       cos_table_t **resp_headers);

cos_status_t *cos_get_object_to_file(const cos_request_options_t *options,
                                     const cos_string_t *bucket, 
                                     const cos_string_t *object,
                                     cos_table_t *headers, 
                                     cos_table_t *params,
                                     cos_string_t *filename, 
                                     cos_table_t **resp_headers);

cos_status_t *cos_append_object_from_buffer(const cos_request_options_t *options,
                                            const cos_string_t *bucket, 
                                            const cos_string_t *object, 
                                            int64_t position,
                                            cos_list_t *buffer, 
                                            cos_table_t *headers, 
                                            cos_table_t **resp_headers);

cos_status_t *cos_append_object_from_file(const cos_request_options_t *options,
                                          const cos_string_t *bucket, 
                                          const cos_string_t *object, 
                                          int64_t position,
                                          const cos_string_t *append_file, 
                                          cos_table_t *headers, 
                                          cos_table_t **resp_headers);

cos_status_t *cos_resumable_download_file(cos_request_options_t *options,
                                            cos_string_t *bucket,
                                            cos_string_t *object,
                                            cos_string_t *filepath,
                                            cos_table_t *headers,
                                            cos_table_t *params,
                                            cos_resumable_clt_params_t *clt_params,
                                            cos_progress_callback progress_callback);
```

#### 参数说明

| 参数名称           | 参数描述                                                     | 类型    |
| ------------------ | ------------------------------------------------------------ | ------- |
| options            | COS 请求选项                                                 | Struct  |
| options.ctl.options.enable_crc  | crc 校验选项，默认开启 crc 校验                      | Int  |

>?其他参数说明则参见 [对象操作](https://cloud.tencent.com/document/product/436/35558)。

#### 返回结果说明

| 返回结果   | 描述        | 类型   |
| ---------- | ----------- | ------ |
| code       | 错误码（crc 校验不通过返回：COSE_CRC_INCONSISTENT_ERROR）      | Int    |
| error_code | 错误码内容  | String |
| error_msg  | 错误码描述  | String |
| req_id     | 请求消息 ID | String |


#### 示例
这里只用了简单上传和下载两个接口来举例，其它接口也是同样使用方式，只需要将 **options** > **ctl** > **options** > **enable_crc** 设置为 COS_TRUE 即可（默认值也是 COS_TRUE）。

```cpp
#include "cos_http_io.h"
#include "cos_api.h"
#include "cos_log.h"
#include <unistd.h>

// endpoint 是 COS 访问域名信息，详情请参见 https://cloud.tencent.com/document/product/436/6224 文档
static char TEST_COS_ENDPOINT[] = "cos.ap-guangzhou.myqcloud.com";
// 开发者拥有的项目身份ID/密钥，可在 https://console.cloud.tencent.com/cam/capi 页面获取
static char *TEST_ACCESS_KEY_ID;                //your secret_id
static char *TEST_ACCESS_KEY_SECRET;            //your secret_key
// 开发者访问 COS 服务时拥有的用户维度唯一资源标识，用以标识资源，可在 https://console.cloud.tencent.com/cam/capi 页面获取
static char TEST_APPID[] = "<APPID>";    //your appid
//the cos bucket name, syntax: [bucket]-[appid], for example: mybucket-1253666666，可在 https://console.cloud.tencent.com/cos5/bucket 查看
static char TEST_BUCKET_NAME[] = "<bucketname-appid>"; 
// 对象键，对象（Object）在存储桶（Bucket）中的唯一标识。有关对象与对象键的进一步说明，请参见 https://cloud.tencent.com/document/product/436/13324 文档
static char TEST_OBJECT_NAME1[] = "1.txt";

void log_status(cos_status_t *s)
{
    cos_warn_log("status->code: %d", s->code);
    if (s->error_code) cos_warn_log("status->error_code: %s", s->error_code);
    if (s->error_msg) cos_warn_log("status->error_msg: %s", s->error_msg);
    if (s->req_id) cos_warn_log("status->req_id: %s", s->req_id);
}

void init_test_config(cos_config_t *config, int is_cname)
{
    cos_str_set(&config->endpoint, TEST_COS_ENDPOINT);
    cos_str_set(&config->access_key_id, TEST_ACCESS_KEY_ID);
    cos_str_set(&config->access_key_secret, TEST_ACCESS_KEY_SECRET);
    cos_str_set(&config->appid, TEST_APPID);
    config->is_cname = is_cname;
}

void init_test_request_options(cos_request_options_t *options, int is_cname)
{
    options->config = cos_config_create(options->pool);
    init_test_config(options->config, is_cname);
    options->ctl = cos_http_controller_create(options->pool, 0);
}

void test_data_crc64()
{
    cos_pool_t *p = NULL;
    int is_cname = 0; 
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_table_t *resp_headers;
    cos_table_t *headers = NULL;
    cos_list_t buffer;
    cos_list_t download_buffer;
    cos_string_t object;
    cos_buf_t *content = NULL;
    char *str = "This is my test data.";

    // 基本配置
    cos_pool_create(&p, NULL);
    options = cos_request_options_create(p);
    init_test_request_options(options, is_cname);
    options->ctl->options->enable_crc = COS_TRUE;   // 开启crc校验，默认也是开启的
    cos_str_set(&bucket, TEST_BUCKET_NAME);
    cos_str_set(&object, TEST_OBJECT_NAME1);

    // 上传对象，开启crc校验
    cos_list_init(&buffer);
    content = cos_buf_pack(options->pool, str, strlen(str));
    cos_list_add_tail(&content->node, &buffer);
    s = cos_put_object_from_buffer(options, &bucket, &object, 
                    &buffer, headers, &resp_headers);
    log_status(s);

    // 下载对象，开启crc校验
    cos_list_init(&download_buffer);
    s = cos_get_object_to_buffer(options, &bucket, &object, 
                        headers, NULL, &download_buffer, &resp_headers);
    log_status(s);

    // 销毁内存池
    cos_pool_destroy(p);
}

int main(int argc, char *argv[])
{
    // 通过环境变量获取 SECRETID 和 SECRETKEY
    TEST_ACCESS_KEY_ID     = getenv("COS_SECRETID");
    TEST_ACCESS_KEY_SECRET = getenv("COS_SECRETKEY");
 
    if (cos_http_io_initialize(NULL, 0) != COSE_OK) {
       exit(1);
    }

    //set log level, default COS_LOG_WARN
    cos_log_set_level(COS_LOG_WARN);

    //set log output, default stderr
    cos_log_set_output(NULL);

    test_data_crc64();

    cos_http_io_deinitialize();

    return 0;
}
```
