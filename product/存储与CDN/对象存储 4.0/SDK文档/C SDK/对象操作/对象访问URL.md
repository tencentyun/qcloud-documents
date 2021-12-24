## 简介

本文档提供获取对象访问 URL 的代码示例。

## 获取对象访问 URL

#### 功能说明
获取对象访问 URL 用于匿名下载或分发。

#### 方法原型

```cpp
const char *cos_gen_object_url(const cos_request_options_t *options, 
                               const cos_string_t *bucket, 
                               const cos_string_t *object)
```

#### 参数说明

| 参数名称   | 参数描述   |类型 | 是否必填 |
| -------------- | -------------- |---------- | ----------- |
| options | COS 请求选项 |Struct | 是 |
| bucket | 存储桶名称，Bucket 的命名规则为 BucketName-APPID ，此处填写的存储桶名称必须为此格式 |Struct | 是 |
| object | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg` 中，对象键为 doc/pic.jpg | String | 是 |

#### 返回结果说明

该方法返回值为对象访问的 URL。


#### 请求示例

```cpp
#include "cos_http_io.h"
#include "cos_api.h"
#include "cos_log.h"

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

void test_gen_object_url()
{
    cos_pool_t *p = NULL;
    int is_cname = 0; 
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
        
    cos_pool_create(&p, NULL);
    options = cos_request_options_create(p);
    init_test_request_options(options, is_cname);
    cos_str_set(&bucket, TEST_BUCKET_NAME);
    cos_str_set(&object, TEST_OBJECT_NAME1);

    printf("url:%s\n", cos_gen_object_url(options, &bucket, &object));

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

    test_gen_object_url();

    cos_http_io_deinitialize();

    return 0;
}
```	