## 简介

C SDK 提供获取请求预签名 URL 接口，详细操作请查看本文说明和示例。

>?
> - 建议用户使用临时密钥生成预签名，通过临时授权的方式进一步提高预签名上传、下载等请求的安全性。申请临时密钥时，请遵循 [最小权限指引原则](https://cloud.tencent.com/document/product/436/38618)，防止泄漏目标存储桶或对象之外的资源。
> - 如果您一定要使用永久密钥来生成预签名，建议永久密钥的权限范围仅限于上传或下载操作，以规避风险。
> 


## 获取请求预签名 URL 

#### 生成请求预签名 URL

#### 功能说明

该接口用于生成请求预签名 URL。

#### 方法原型

```cpp
int cos_gen_presigned_url(const cos_request_options_t *options,
                          const cos_string_t *bucket, 
                          const cos_string_t *object,
                          const int64_t expire,
                          http_method_e method,
                          cos_string_t *presigned_url);
```

#### 参数说明

| 参数名称      | 参数描述                                                     | 类型   |
| ------------- | ------------------------------------------------------------ | ------ |
| options       | COS 请求选项                                                 | Struct |
| bucket        | 存储桶名称，存储桶的命名格式为 BucketName-APPID，此处填写的存储桶名称必须为此格式 | String |
| object        | Object 名称                                                  | String |
| expire        | 签名有效时间，单位为秒                                       | Int    |
| method        | HTTP 请求方法枚举类型，分别为 HTTP_GET、HTTP_HEAD、HTTP_PUT、HTTP_POST、HTTP_DELETE | Enum   |
| presigned_url | 生成的请求预签名 URL                                         | String |

#### 返回结果说明

| 返回结果 | 描述   | 类型 |
| -------- | ------ | ---- |
| code     | 错误码 | Int  |

#### 预签名请求示例

可在 options 参数中设置永久密钥或临时密钥来获取预签名 URL：

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

void test_presigned_url()
{
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
    cos_string_t presigned_url;
    
    cos_pool_create(&p, NULL);
    options = cos_request_options_create(p);
    init_test_request_options(options, is_cname);
    cos_str_set(&bucket, TEST_BUCKET_NAME);
    cos_str_set(&object, TEST_OBJECT_NAME1);

    cos_gen_presigned_url(options, &bucket, &object, 300, HTTP_GET, &presigned_url);
    printf("presigned_url: %s\n", presigned_url.data);

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

    test_presigned_url();

    cos_http_io_deinitialize();

    return 0;
}
```

## 安全获取请求预签名 URL 

#### 安全生成请求预签名 URL

#### 功能说明

该接口用于安全的生成请求预签名 URL。

#### 方法原型

```cpp
int cos_gen_presigned_url_safe(const cos_request_options_t *options,
                          const cos_string_t *bucket, 
                          const cos_string_t *object,
                          const int64_t expire,
                          http_method_e method,
                          cos_table_t *headers,
                          cos_table_t *params,
                          int sign_host,
                          cos_string_t *presigned_url);
```

#### 参数说明

| 参数名称      | 参数描述                                                     | 类型   |
| ------------- | ------------------------------------------------------------ | ------ |
| options       | COS 请求选项                                                 | Struct |
| bucket        | 存储桶名称，存储桶的命名格式为 BucketName-APPID，此处填写的存储桶名称必须为此格式 | String |
| object        | Object 名称                                                  | String |
| expire        | 签名有效时间，单位为秒                                       | Int    |
| method        | HTTP 请求方法枚举类型，分别为 HTTP_GET、HTTP_HEAD、HTTP_PUT、HTTP_POST、HTTP_DELETE | Enum   |
| headers       | COS 请求附加头域                                             | Struct |
| params        | COS 请求操作参数                                             | Struct |
| sign_host     | 是否对 host 头域进行签名，为了安全性强烈建议开启                    | Int    |
| presigned_url | 生成的请求预签名 URL                                         | String |

#### 返回结果说明

| 返回结果 | 描述   | 类型 |
| -------- | ------ | ---- |
| code     | 错误码 | Int  |

#### 请求示例1: 生成预签名URL，并在签名中携带host

可在 options 参数中设置永久密钥或临时密钥来获取预签名 URL：

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

void test_safe_presigned_url()
{
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
    cos_string_t presigned_url;
    cos_table_t *params = NULL;
    cos_table_t *headers = NULL;
    int sign_host = 1;
    
    cos_pool_create(&p, NULL);
    options = cos_request_options_create(p);
    init_test_request_options(options, is_cname);
    /* 可以通过设置 sts_token 来使用临时密钥，当使用临时密钥时，access_key_id 和 access_key_secret 均需要设置为对应临时密钥所配套的 SecretId 和 SecretKey */
    //cos_str_set(&options->config->sts_token, "MyTokenString");
    cos_str_set(&bucket, TEST_BUCKET_NAME);
    cos_str_set(&object, TEST_OBJECT_NAME1);

    // 强烈建议sign_host为1，这样强制把host头域加入签名列表，防止越权访问问题
    cos_gen_presigned_url_safe(options, &bucket, &object, 300, HTTP_GET, headers, params, sign_host, &presigned_url);
    printf("presigned_url_safe: %s\n", presigned_url.data);

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

    test_safe_presigned_url();

    cos_http_io_deinitialize();

    return 0;
}
```

#### 请求示例2: 生成预签名URL，并在签名中携带request param和request header

可在 options 参数中设置永久密钥或临时密钥来获取预签名 URL：

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

void test_safe_presigned_url()
{
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
    cos_string_t presigned_url;
    cos_table_t *params = NULL;
    cos_table_t *headers = NULL;
    int sign_host = 1;
    
    cos_pool_create(&p, NULL);
    options = cos_request_options_create(p);
    init_test_request_options(options, is_cname);
    /* 可以通过设置 sts_token 来使用临时密钥，当使用临时密钥时，access_key_id 和 access_key_secret 均需要设置为对应临时密钥所配套的 SecretId 和 SecretKey */
    //cos_str_set(&options->config->sts_token, "MyTokenString");
    cos_str_set(&bucket, TEST_BUCKET_NAME);
    cos_str_set(&object, TEST_OBJECT_NAME1);

    // 添加您自己的params和headers
    params = cos_table_make(options->pool, 0);
    //cos_table_add(params, "param1", "value");
    headers = cos_table_make(options->pool, 0);
    //cos_table_add(headers, "header1", "value");

    // 强烈建议sign_host为1，这样强制把host头域加入签名列表，防止越权访问问题
    cos_gen_presigned_url_safe(options, &bucket, &object, 300, HTTP_GET, headers, params, sign_host, &presigned_url);
    printf("presigned_url_safe: %s\n", presigned_url.data);

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

    test_safe_presigned_url();

    cos_http_io_deinitialize();

    return 0;
}
```
