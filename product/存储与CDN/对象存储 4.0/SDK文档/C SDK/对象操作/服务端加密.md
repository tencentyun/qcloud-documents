## 简介

如果需要对上传的对象进行加密，我们支持以下加密方式。

## 使用 SSE-COS 加密保护数据

#### 功能说明

由腾讯云 COS 托管主密钥和管理数据。COS 会帮助您在数据写入数据中心时自动加密，并在您取用该数据时自动解密。目前支持使用 COS 主密钥对数据进行 AES-256 加密。

C SDK 通过设置`x-cos-server-side-encryption`头部来完成。

#### 示例

```cpp
int main(int argc, char *argv[])
{
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
    cos_table_t *resp_headers = NULL;
    cos_table_t *headers = NULL;
    cos_string_t file;
    cos_string_t download_file;
	// 初始化
    if (cos_http_io_initialize(NULL, 0) != COSE_OK) {
       exit(1);
    }
    cos_pool_create(&p, NULL);
    // 初始化请求选项
    options = cos_request_options_create(p);
    options->config = cos_config_create(options->pool);
    cos_str_set(&options->config->endpoint, "cos.ap-guangzhou.myqcloud.com"); // your endpoint
    cos_str_set(&options->config->access_key_id, "SECRETID");	// your SecretId 
    cos_str_set(&options->config->access_key_secret, "SECRETKEY"); // your SecretKey
    cos_str_set(&options->config->appid, "APPID");	//your appid
    options->config->is_cname = is_cname;
    options->ctl = cos_http_controller_create(options->pool, 0);
    cos_str_set(&bucket, "<BucketName-APPID>");	//your bucketname, <BucketName-APPID>

    // 设置服务端加密头部，SSE-COS
    headers = cos_table_make(p, 1);
    apr_table_add(headers, "x-cos-server-side-encryption", "AES256");

    cos_str_set(&file, "example1.txt");		// your filename
    cos_str_set(&object, "example_object");	// your object name

    // 上传对象
    s = cos_put_object_from_file(options, &bucket, &object, &file, headers, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("put object succeeded\n");
    } else {
        printf("put object failed\n");
    }
    
    // 下载对象
    cos_str_set(&download_file, "example2.txt");
    s = cos_get_object_to_file(options, &bucket, &object, NULL, NULL, &download_file, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("get object succeeded\n");
    } else {
        printf("get object failed\n");
    }
    
    cos_pool_destroy(p);

    cos_http_io_deinitialize();
    return 0;
}
```

## 使用 SSE-C 加密保护数据

加密密钥由用户自己提供，用户在上传对象时，COS 将使用用户提供的加密密钥对用户的数据进行 AES-256 加密。C SDK 通过设置 `x-cos-server-side-encryption-customer-*`头部来完成。

#### 功能说明

> !
>- 该加密所运行的服务需要使用 HTTPS 请求。
>- customerKey：用户提供的密钥，传入一个32字节的字符串，支持数字、字母、字符的组合，不支持中文。
>- 如果上传的源文件调用了该方法，那么在使用 GET（下载）、HEAD（查询）时对源对象操作的时候也要调用该方法。


#### 示例
```cpp
int main(int argc, char *argv[])
{
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
    cos_table_t *resp_headers = NULL;
    cos_table_t *headers = NULL;
    cos_string_t file;
    cos_string_t download_file;
	// 初始化
    if (cos_http_io_initialize(NULL, 0) != COSE_OK) {
       exit(1);
    }
    cos_pool_create(&p, NULL);
    // 初始化请求选项
    options = cos_request_options_create(p);
    options->config = cos_config_create(options->pool);
    cos_str_set(&options->config->endpoint, "https://cos.ap-guangzhou.myqcloud.com"); // your endpoint, 需要使用HTTPS请求
    cos_str_set(&options->config->access_key_id, "SECRETID");	// your SecretId 
    cos_str_set(&options->config->access_key_secret, "SECRETKEY"); // your SecretKey
    cos_str_set(&options->config->appid, "APPID");	//your appid
    options->config->is_cname = is_cname;
    options->ctl = cos_http_controller_create(options->pool, 0);
    cos_str_set(&bucket, "<BucketName-APPID>");	//your bucketname, <BucketName-APPID>

    // 设置服务端加密头部，SSE-C
    headers = cos_table_make(p, 3);
    apr_table_add(headers, "x-cos-server-side-encryption-customer-algorithm", "AES256");
    apr_table_add(headers, "x-cos-server-side-encryption-customer-key", "MDEyMzQ1Njc4OUFCQ0RFRjAxMjM0NTY3ODlBQkNERUY=");	//替换成您的服务端加密密钥的 Base64 编码
    apr_table_add(headers, "x-cos-server-side-encryption-customer-key-MD5", "U5L61r7jcwdNvT7frmUG8g==");	//	替换成您的服务端加密密钥 MD5 哈希值的 Base64 编码

    cos_str_set(&file, "example1.txt");		// your filename
    cos_str_set(&object, "example_object");	// your object name

    // 上传对象
    s = cos_put_object_from_file(options, &bucket, &object, &file, headers, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("put object succeeded\n");
    } else {
        printf("put object failed\n");
    }
    
    // 下载对象，下载对象也需要提供服务端加密头部
    cos_str_set(&download_file, "example2.txt");
    s = cos_get_object_to_file(options, &bucket, &object, headers, NULL, &download_file, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("get object succeeded\n");
    } else {
        printf("get object failed\n");
    }

    cos_pool_destroy(p);

    cos_http_io_deinitialize();
    return 0;
}
```
