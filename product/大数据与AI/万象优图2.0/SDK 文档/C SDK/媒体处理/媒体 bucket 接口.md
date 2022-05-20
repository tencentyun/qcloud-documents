## 简介

本文档提供关于媒体 bucket 的 API 概览和 SDK 示例代码。

| API                        |             操作名                     | 操作描述                                               |
| ------------------------------------------------------------ | --------------------------|---------------------------- |
|  [DescribeMediaBuckets](https://cloud.tencent.com/document/product/436/48988)  |  查询媒体处理开通情况    |    用于查询已经开通媒体处理功能的存储桶         |


## 查询媒体处理开通情况

#### 功能说明

用于查询已经开通媒体处理功能的存储桶。

#### 方法原型

```cpp
cos_status_t *ci_describe_media_buckets(const cos_request_options_t *options,
                                        const ci_media_buckets_request_t *media_request,
                                        cos_table_t *headers, 
                                        cos_table_t **resp_headers,
                                        ci_media_buckets_result_t **media_result);
```

#### 参数说明

| 参数名称           | 参数描述                                                     | 类型    |
| ------------------ | ------------------------------------------------------------ | ------- |
| options            | COS 请求选项                                                 | Struct  |
| media_request      | 查询媒体桶的请求参数                                           | Struct  |
| regions            | 地域信息，例如 ap-shanghai、ap-beijing，若查询多个地域以“,”分隔字符串，支持中国大陆地域   | String  |
| bucket_names       | 存储桶名称，以“,”分隔，支持多个存储桶，精确搜索                    | String  |
| bucket_name        | 存储桶名称前缀，前缀搜索                                        | String  |
| page_number        | 第几页                                                       | String  |
| page_size          | 每页个数                                                     | String  |
| headers            | COS 请求附加头域                                              | Struct |
| resp_headers       | 返回 HTTP 响应消息的头域                                       | Struct  |
| media_result       | 返回 开通媒体处理功能的桶信息                                    | Struct  |
| total_count        | 媒体 Bucket 总数                                              | Int  |
| page_number        | 当前页数，同请求中的 pageNumber                                 | Int  |
| page_size          | 每页个数，同请求中的 pageSize                                   | Int  |
| media_bucket_list  | 媒体 Bucket 列表                                              | Struct  |
| bucket_id          | 存储桶 ID                                                     | String  |
| name               | 存储桶名称，同 BucketId                                        | String  |
| region             | 所在的地域                                                     | String  |
| create_time        | 创建时间                                                       | String  |

#### 返回结果说明

| 返回结果   | 描述        | 类型   |
| ---------- | ----------- | ------ |
| code       | 错误码      | Int    |
| error_code | 错误码内容  | String |
| error_msg  | 错误码描述  | String |
| req_id     | 请求消息 ID | String |

#### 示例
完整代码请参见cos_demo.c中test_ci_media_process_media_bucket()函数。

```cpp
#include "cos_http_io.h"
#include "cos_api.h"
#include "cos_log.h"

// 数据万象的访问域名，详情请参见 https://cloud.tencent.com/document/product/460/31066 文档
static char TEST_CI_ENDPOINT[] = "https://ci.ap-guangzhou.myqcloud.com";
// 开发者拥有的项目身份ID/密钥，可在 https://console.cloud.tencent.com/cam/capi 页面获取
static char *TEST_ACCESS_KEY_ID;                //your secret_id
static char *TEST_ACCESS_KEY_SECRET;            //your secret_key
// 开发者访问 COS 服务时拥有的用户维度唯一资源标识，用以标识资源，可在 https://console.cloud.tencent.com/cam/capi 页面获取
static char TEST_APPID[] = "<APPID>";    //your appid

void log_status(cos_status_t *s)
{
    cos_warn_log("status->code: %d", s->code);
    if (s->error_code) cos_warn_log("status->error_code: %s", s->error_code);
    if (s->error_msg) cos_warn_log("status->error_msg: %s", s->error_msg);
    if (s->req_id) cos_warn_log("status->req_id: %s", s->req_id);
}

static void log_media_buckets_result(ci_media_buckets_result_t *result)
{
    int index = 0;
    ci_media_bucket_list_t *media_bucket;

    cos_warn_log("total_count: %d", result->total_count);
    cos_warn_log("page_number: %d", result->page_number);
    cos_warn_log("page_size: %d", result->page_size);

    cos_list_for_each_entry(ci_media_bucket_list_t, media_bucket, &result->media_bucket_list, node) {
        cos_warn_log("media_bucket index:%d", ++index);
        cos_warn_log("media_bucket->bucket_id: %s", media_bucket->bucket_id.data);
        cos_warn_log("media_bucket->name: %s", media_bucket->name.data);
        cos_warn_log("media_bucket->region: %s", media_bucket->region.data);
        cos_warn_log("media_bucket->create_time: %s", media_bucket->create_time.data);
    }
}

void test_ci_media_process_media_bucket()
{
    cos_pool_t *p = NULL;
    int is_cname = 0; 
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_table_t *resp_headers;
    ci_media_buckets_request_t *media_buckets_request;
    ci_media_buckets_result_t *media_buckets_result;

    // 基本配置
    cos_pool_create(&p, NULL);
    options = cos_request_options_create(p);
    options->config = cos_config_create(options->pool);
    cos_str_set(&options->config->endpoint, TEST_CI_ENDPOINT);     // https://ci.<Region>.myqcloud.com
    cos_str_set(&options->config->access_key_id, TEST_ACCESS_KEY_ID);
    cos_str_set(&options->config->access_key_secret, TEST_ACCESS_KEY_SECRET);
    cos_str_set(&options->config->appid, TEST_APPID);
    options->config->is_cname = is_cname;
    options->ctl = cos_http_controller_create(options->pool, 0);

    // 替换为您的配置信息，可参见文档 https://cloud.tencent.com/document/product/436/48988
    media_buckets_request = ci_media_buckets_request_create(p);
    cos_str_set(&media_buckets_request->regions, "");
    cos_str_set(&media_buckets_request->bucket_names, "");
    cos_str_set(&media_buckets_request->bucket_name, "");
    cos_str_set(&media_buckets_request->page_number, "1");
    cos_str_set(&media_buckets_request->page_size, "10");
    s = ci_describe_media_buckets(options, media_buckets_request, NULL, &resp_headers, &media_buckets_result);
    log_status(s);
    if (s->code == 200) {
        log_media_buckets_result(media_buckets_result);
    }

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

    test_ci_media_process_media_bucket();

    cos_http_io_deinitialize();

    return 0;
}
```