## 开发准备
### 相关资源
对象存储的 XML C SDK 资源下载地址：
- [GitHub 项目（to be updated）](https://github.com/tencentyun/cos-c-sdk-v5)
- [本地下载（to be updated）](https://mc.qcloudimg.com/static/archive/2549fea204187b28d05fb1ac470f49d4/cos-c-sdk-v5-master.zip)

演示示例 Demo 下载地址：
- [XML C SDK Demo（to be updated）](https://github.com/tencentyun/cos-c-sdk-v5/cos_c_sdk_test/cos_demo.c)

### 开发环境
1. 安装 CMake 工具（建议 2.6.0 及以上版本），点击 [这里](http://www.cmake.org/download/) 下载，典型安装方式如下：
```bash
./configure
make
make install
```
2. 安装 libcurl（建议 7.32.0 及以上版本），点击 [这里](http://curl.haxx.se/download.html?spm=5176.doc32132.2.7.23MmBq) 下载，典型安装方式如下：
```bash
./configure
make
make install
```
3. 安装 apr（建议 1.5.2 及以上版本），点击 [这里](https://apr.apache.org/download.cgi?spm=5176.doc32132.2.9.23MmBq&file=download.cgi) 下载，典型安装方式如下：
```bash
./configure
make
make install
```
4. 安装 apr-util（建议 1.5.4 及以上版本），点击 [这里](https://apr.apache.org/download.cgi?spm=5176.doc32132.2.10.23MmBq&file=download.cgi) 下载，安装时需要指定— with-apr 选项，典型安装方式如下：
```bash
./configure --with-apr=/your/apr/install/path
make
make install
```
5. 安装 minixml（建议 2.8 及以上版本），点击 [这里](http://www.msweet.org/downloads.php?spm=5176.doc32132.2.11.23MmBq&L+Z3) 下载，典型安装方式如下：
```bash
./configure
make
sudo make install
```

### 安装 SDK
源码安装。从 [GitHub](https://github.com/tencentyun/cos-c-sdk-v5) 下载源码，典型编译命令如下：
```bash
cmake .
make
make install
```

## SDK 初始化
### 初始化 SDK 运行环境
```cpp
int main(int argc, char *argv[])
{
    /* 程序入口处调用 cos_http_io_initialize 方法，这个方法内部会做一些全局资源的初始化，涉及网络，内存等部分 */
    if (cos_http_io_initialize(NULL, 0) != AOSE_OK) {
        exit(1);
    }

    /* 调用 COS SDK 的接口上传或下载文件 */
    /* ... 用户逻辑代码，这里省略 */

    /* 程序结束前，调用 cos_http_io_deinitialize 方法释放之前分配的全局资源 */
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

##  SDK 一般使用流程
1. 初始化 SDK。
2. 设置请求选项参数。
关于 APPID、SecretId、SecretKey、Bucket 等名称的含义和获取方式请参考 [COS 术语信息](/document/product/436/7751)。
  *  APPID 是申请腾讯云账户后，系统分配的账户标识之一。
  * access_key_id 与 access_key_secret 是账户 API 密钥。
  * endpoint 是 COS 访问域名信息，可以通过腾讯云[【COS 可用地域】](/document/product/436/6224) 页面查看。
  例如，广州地区 endpoint 为 cos.ap-guangzhou.myqcloud.com。
3. 设置 API 接口必需的参数。
4. 调用 SDK API 发起请求并获得请求响应结果。

### 创建 Bucket
```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_acl_e cos_acl = COS_ACL_PRIVATE;
    cos_string_t bucket;
    cos_table_t *resp_headers = NULL;
    
    /* 重新创建一个新的内存池，第二个参数是NULL，表示没有继承自其它内存池 */
    cos_pool_create(&p, NULL);
    
    /* 创建并初始化options，这个参数内部主要包括endpoint,access_key_id,acces_key_secret，is_cname, curl参数等全局配置信息
     * options的内存是由pool分配的，后续释放掉pool后，options的内存也相当于释放掉了，不再需要单独释放内存
     */
    options = cos_request_options_create(p);
    options->config = cos_config_create(options->pool);
    init_test_config(options->config, is_cname);
    
    /* 设置appid，endpoint，access_key_id，acces_key_secret，is_cname, curl参数等配置信息 */
    cos_str_set(&options->config->endpoint, TEST_COS_ENDPOINT);
    cos_str_set(&options->config->access_key_id, TEST_ACCESS_KEY_ID);
    cos_str_set(&options->config->access_key_secret, TEST_ACCESS_KEY_SECRET);
    cos_str_set(&options->config->appid, TEST_APPID);
    options->config->is_cname = is_cname;
    options->ctl = cos_http_controller_create(options->pool, 0);
    cos_str_set(&bucket, TEST_BUCKET_NAME);

    /* 调用api创建bucket */
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
```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
    cos_string_t file;
    cos_table_t *resp_headers = NULL;
    
    /* 重新创建一个新的内存池，第二个参数是NULL，表示没有继承自其它内存池 */
    cos_pool_create(&p, NULL);
    
    /* 创建并初始化options，这个参数内部主要包括endpoint,access_key_id,acces_key_secret，is_cname, curl参数等全局配置信息
     * options的内存是由pool分配的，后续释放掉pool后，options的内存也相当于释放掉了，不再需要单独释放内存
     */
    options = cos_request_options_create(p);
    options->config = cos_config_create(options->pool);
    init_test_config(options->config, is_cname);

    /* 设置appid，endpoint，access_key_id，acces_key_secret，is_cname, curl参数等配置信息 */
    cos_str_set(&options->config->endpoint, TEST_COS_ENDPOINT);
    cos_str_set(&options->config->access_key_id, TEST_ACCESS_KEY_ID);
    cos_str_set(&options->config->access_key_secret, TEST_ACCESS_KEY_SECRET);
    cos_str_set(&options->config->appid, TEST_APPID);
    options->config->is_cname = is_cname;
    options->ctl = cos_http_controller_create(options->pool, 0);
    cos_str_set(&bucket, TEST_BUCKET_NAME);

    /* 调用api上传文件 */
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
    
    /* 重新创建一个新的内存池，第二个参数是NULL，表示没有继承自其它内存池 */
    cos_pool_create(&p, NULL);
    
    /* 创建并初始化options，这个参数内部主要包括endpoint,access_key_id,acces_key_secret，is_cname, curl参数等全局配置信息
     * options的内存是由pool分配的，后续释放掉pool后，options的内存也相当于释放掉了，不再需要单独释放内存
     */
    options = cos_request_options_create(p);
    options->config = cos_config_create(options->pool);
    init_test_config(options->config, is_cname);

    /* 设置appid，endpoint，access_key_id，acces_key_secret，is_cname, curl参数等配置信息 */
    cos_str_set(&options->config->endpoint, TEST_COS_ENDPOINT);
    cos_str_set(&options->config->access_key_id, TEST_ACCESS_KEY_ID);
    cos_str_set(&options->config->access_key_secret, TEST_ACCESS_KEY_SECRET);
    cos_str_set(&options->config->appid, TEST_APPID);
    options->config->is_cname = is_cname;
    options->ctl = cos_http_controller_create(options->pool, 0);
    cos_str_set(&bucket, TEST_BUCKET_NAME);

    /* 调用api下载文件 */
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
