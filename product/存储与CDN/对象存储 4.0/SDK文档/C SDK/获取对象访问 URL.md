## 简介
本文档提供获取对象访问 URL 的代码示例。

## 获取对象访问 URL

#### 功能说明
获取对象访问 URL 用于匿名下载或分发。

#### 方法原型

```
const char *cos_gen_object_url(const cos_request_options_t *options, const cos_string_t *bucket, const cos_string_t *object)
```

#### 请求示例

[//]: # ".cssg-snippet-get-object-url-alias"
```go
cos_pool_t *p = NULL;
int is_cname = 0; 
cos_status_t *s = NULL;
cos_request_options_t *options = NULL;
cos_string_t bucket;
cos_string_t object;
cos_string_t filepath;
cos_resumable_clt_params_t *clt_params;
      
cos_pool_create(&p, NULL);
options = cos_request_options_create(p);
init_test_request_options(options, is_cname);
cos_str_set(&bucket, TEST_BUCKET_NAME);
cos_str_set(&object, "exampleobject");

printf("url:%s\n", cos_gen_object_url(options, &bucket, &object));

cos_pool_destroy(p);
```

#### 参数说明

| 参数名称   | 参数描述   |类型 | 是否必填 |
| -------------- | -------------- |---------- | ----------- |
| options | COS 请求选项 |Struct | 是 |
| bucket | 存储桶名称，Bucket 的命名规则为 BucketName-APPID ，此处填写的存储桶名称必须为此格式 |Struct | 是 |
| object | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg` 中，对象键为 doc/pic.jpg | String | 是 |

#### 返回结果说明

该方法返回值为对象访问的 URL。	
