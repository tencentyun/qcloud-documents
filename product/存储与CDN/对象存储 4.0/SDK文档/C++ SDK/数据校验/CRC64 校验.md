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

## SDK 校验方式

目前C++ SDK对于不同接口默认校验方式不同：

- 简单上传接口
  - [PUT Object](https://cloud.tencent.com/document/product/436/7749) ：默认使用MD5校验，暂不支持CRC64校验。
- 分块上传接口
  - [Upload Part](https://cloud.tencent.com/document/product/436/7750)：默认使用MD5校验，暂不支持CRC64校验。
  - [Complete Multipart Upload](https://cloud.tencent.com/document/product/436/7742)：默认使用CRC64校验，暂不支持MD5校验。

用于在对象上传和下载的时候对对象数据做 crc64 一致性校验。


#### 请求示例
```cpp
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
options->config = cos_config_create(options->pool);
cos_str_set(&options->config->endpoint, TEST_COS_ENDPOINT);   
cos_str_set(&options->config->access_key_id, TEST_ACCESS_KEY_ID);
cos_str_set(&options->config->access_key_secret, TEST_ACCESS_KEY_SECRET);
cos_str_set(&options->config->appid, TEST_APPID);
options->config->is_cname = is_cname;
options->ctl = cos_http_controller_create(options->pool, 0);
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
```
