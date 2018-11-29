## 开发准备

### 相关资源

[cos c sdk v5 github项目(to be updated)](https://github.com/tencentyun/cos-c-sdk-v5)

[C SDK本地下载(to be updated)](https://mc.qcloudimg.com/static/archive/2549fea204187b28d05fb1ac470f49d4/cos-c-sdk-v5-master.zip)


> <font size=4 color=red>  把Demo的地址附上来，可以引导用户去demo里面查看</font>
> by stongdong


### 开发环境

1. 安装cmake工具（建议2.6.0及以上版本），点击[这里](http://www.cmake.org/download/)下载，典型安装方式如下：
```bash
./configure
make
make install
```
2. libcurl（建议 7.32.0 及以上版本），点击[这里](http://curl.haxx.se/download.html?spm=5176.doc32132.2.7.23MmBq)下载，典型安装方式如下：
```bash
./configure
make
make install
```
3. apr（建议 1.5.2 及以上版本），点击[这里](https://apr.apache.org/download.cgi?spm=5176.doc32132.2.9.23MmBq&file=download.cgi)下载，典型安装方式如下：
```bash
./configure
make
make install
```
4. apr-util（建议 1.5.4 及以上版本），点击[这里](https://apr.apache.org/download.cgi?spm=5176.doc32132.2.10.23MmBq&file=download.cgi)下载，安装时需要指定—with-apr选项，典型安装方式如下：
```bash
./configure --with-apr=/your/apr/install/path
make
make install
```
5. minixml（建议 2.8 及以上版本），点击[这里](http://www.msweet.org/downloads.php?spm=5176.doc32132.2.11.23MmBq&L+Z3)下载，典型安装方式如下：
```bash
./configure
make
sudo make install
```

### 安装SDK

- 源码安装

从[cos c sdk v5 github项目(to be updated)](https://github.com/tencentyun/cos-c-sdk-v5)下载源码，典型编译命令如下：
```bash
cmake .
make
make install
```

## SDK初始化

### 初始化SDK运行环境

```cpp
int main(int argc, char *argv[])
{
    /* 程序入口处调用cos_http_io_initialize方法，这个方法内部会做一些全局资源的初始化，涉及网络，内存等部分 */
    if (cos_http_io_initialize(NULL, 0) != AOSE_OK) {
        exit(1);
    }

    /* 调用COS SDK的接口上传或下载文件 */
    /* ... 用户逻辑代码，这里省略 */

    /* 程序结束前，调用cos_http_io_deinitialize方法释放之前分配的全局资源 */
    cos_http_io_deinitialize();
    return 0;
}
```

### 初始化请求选项

```cpp
    /* 等价于apr_pool_t，用于内存管理的内存池，实现代码在apr库中 */
    cos_pool_t *pool;
    cos_request_options_t *options;

    /* 重新创建一个新的内存池，第二个参数是NULL，表示没有继承自其它内存池 */
    cos_pool_create(&pool, NULL);

    /* 创建并初始化options，这个参数内部主要包括endpoint,access_key_id,acces_key_secret，is_cname, curl参数等全局配置信息
     * options的内存是由pool分配的，后续释放掉pool后，options的内存也相当于释放掉了，不再需要单独释放内存
     */
    options = cos_request_options_create(pool);
    options->config = cos_config_create(options->pool);

    /* cos_str_set是用char*类型的字符串初始化cos_string_t类型*/
    cos_str_set(&options->config->endpoint, "<用户的Endpoint>");              //Endpoint依据用户所在园区的COS服务域名填写
    cos_str_set(&options->config->access_key_id, "<用户的SecretId>");         //用户注册COS服务后所获得的SecretId
    cos_str_set(&options->config->access_key_secret, "<用户的SecretKey>");    //用户注册COS服务后所获得的SecretKey
    cos_str_set(&options->config->appid, "<用户的AppId>");                    //用户注册COS服务后所获得的AppId

    /* 是否使用了CNAME */
    options->config->is_cname = 0;

    /* 用于设置网络相关参数，比如超时时间等*/
    options->ctl = cos_http_controller_create(options->pool, 0);
```

## 快速入门

> <font size=4 color=red> 这个标题和目录的位置是不是放错了？</font>
> by stongdong

###  SDK一般使用流程

1. 初始化SDK
2. 设置请求选项参数
3. 设置API接口必需的参数
4. 调用SDK API发起请求并获得请求响应结果

> <font size=4 color=red> 关键的数据appid region secretId 和 secretKey从哪里获取，要写出来，并给出链接</font>
> by stongdong


> <font size=4 color=red> 最好是把每一步 加上简单的注释，说明一下用途。这样能够更直接明白。</font>
> by stongdong


### 创建Bucket

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_acl_e cos_acl = COS_ACL_PRIVATE;
    cos_string_t bucket;
    cos_table_t *resp_headers = NULL;

    //create memory pool
    cos_pool_create(&p, NULL);

    //init request options
    options = cos_request_options_create(p);
    options->config = cos_config_create(options->pool);
    init_test_config(options->config, is_cname);
    cos_str_set(&options->config->endpoint, TEST_COS_ENDPOINT);
    cos_str_set(&options->config->access_key_id, TEST_ACCESS_KEY_ID);
    cos_str_set(&options->config->access_key_secret, TEST_ACCESS_KEY_SECRET);
    cos_str_set(&options->config->appid, TEST_APPID);
    options->config->is_cname = is_cname;
    options->ctl = cos_http_controller_create(options->pool, 0);
    cos_str_set(&bucket, TEST_BUCKET_NAME);

    //create bucket
    s = cos_create_bucket(options, &bucket, cos_acl, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("create bucket succeeded\n");
    } else {
        printf("create bucket failed\n");
    }

    //destroy memory pool
    cos_pool_destroy(p);
```

### 上传文件


> <font size=4 color=red> 得到结果怎么使用，中间进度怎么监控需要说明一下。</font>
> by stongdong

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
    cos_string_t file;
    cos_table_t *resp_headers = NULL;

    //create memory pool
    cos_pool_create(&p, NULL);

    //init request options
    options = cos_request_options_create(p);
    options->config = cos_config_create(options->pool);
    init_test_config(options->config, is_cname);
    cos_str_set(&options->config->endpoint, TEST_COS_ENDPOINT);
    cos_str_set(&options->config->access_key_id, TEST_ACCESS_KEY_ID);
    cos_str_set(&options->config->access_key_secret, TEST_ACCESS_KEY_SECRET);
    cos_str_set(&options->config->appid, TEST_APPID);
    options->config->is_cname = is_cname;
    options->ctl = cos_http_controller_create(options->pool, 0);
    cos_str_set(&bucket, TEST_BUCKET_NAME);

    //put object
    cos_str_set(&file, TEST_DOWNLOAD_NAME);
    cos_str_set(&object, TEST_OBJECT_NAME);
    s = cos_put_object_from_file(options, &bucket, &object, &file, NULL, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("put object succeeded\n");
    } else {
        printf("put object failed\n");
    }

    //destroy memory pool
    cos_pool_destroy(p);
```

### 下载文件

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
    cos_string_t file;
    cos_table_t *resp_headers = NULL;

    //create memory pool
    cos_pool_create(&p, NULL);

    //init request options
    options = cos_request_options_create(p);
    options->config = cos_config_create(options->pool);
    init_test_config(options->config, is_cname);
    cos_str_set(&options->config->endpoint, TEST_COS_ENDPOINT);
    cos_str_set(&options->config->access_key_id, TEST_ACCESS_KEY_ID);
    cos_str_set(&options->config->access_key_secret, TEST_ACCESS_KEY_SECRET);
    cos_str_set(&options->config->appid, TEST_APPID);
    options->config->is_cname = is_cname;
    options->ctl = cos_http_controller_create(options->pool, 0);
    cos_str_set(&bucket, TEST_BUCKET_NAME);

    //get object
    cos_str_set(&file, TEST_DOWNLOAD_NAME);
    cos_str_set(&object, TEST_OBJECT_NAME);
    s = cos_get_object_to_file(options, &bucket, &object, NULL, NULL, &file, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("get object succeeded\n");
    } else {
        printf("get object failed\n");
    }

    //destroy memory pool
    cos_pool_destroy(p);
```
