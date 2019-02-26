## Preparations for Development
### Related resources
Download XML C SDK resources of COS service from [XML C SDK GitHub ](https://github.com/tencentyun/cos-c-sdk-v5).
Download Demo from: [XML C SDK Demo](https://github.com/tencentyun/cos-c-sdk-v5/blob/master/cos_c_sdk_test/cos_demo.c).

### Development environment
1. Click [here](http://www.cmake.org/download/) to download and install CMake tool (version 2.6.0 or above is recommended). Typical setup is as follows:
```bash
./configure
make
make install
```
2. Click [here](http://curl.haxx.se/download.html?spm=5176.doc32132.2.7.23MmBq) to download and install libcurl (version 7.32.0 or above is recommended). Typical setup is as follows:
```bash
./configure
make
make install
```
3. Click [here](https://apr.apache.org/download.cgi?spm=5176.doc32132.2.9.23MmBq&file=download.cgi) to download and install apr (version 1.5.2 or above is recommended). Typical setup is as follows:
```bash
./configure
make
make install
```
4. Click [here](https://apr.apache.org/download.cgi?spm=5176.doc32132.2.10.23MmBq&file=download.cgi) to download and install apr-util (version 1.5.4 or above is recommended). Typical setup is as follows:
```bash
./configure --with-apr=/your/apr/install/path
make
make install
```
5. Click [here](https://www.msweet.org/mxml/) to download and install minixml (version 2.8 or above is recommended). Typical setup is as follows:
```bash
./configure
make
sudo make install
```

### Installing SDK
Install via source code. Download source code from [GitHub](https://github.com/tencentyun/cos-c-sdk-v5). Typical compiling command is as follows:
```bash
cmake .
make
make install
```

## SDK Initialization
### Initializing SDK Operating Environment
```cpp
int main(int argc, char *argv[])
{
    /*Call cos_http_io_initialize method at the program entry to initialize global resources internally, including network, memory, etc.*/
 ? ?if (cos_http_io_initialize(NULL, 0) != COSE_OK) {
        exit(1);
    }

    /* Call COS SDK API to upload/download file */
    /* ... User logic code is ignored here */

    /* Call cos_http_io_deinitialize method to release global resources assigned previously before the program ends */
    cos_http_io_deinitialize();
    return 0;
}
```

### Initializing Request Options
```cpp
    /*Equivalent to apr_pool_t, the memory pool for memory management. The implementation code can be found in apr library */
    cos_pool_t *pool;
    cos_request_options_t *options;

    /* Re-create a new memory pool. The second parameter is NULL, which indicates it is not inherited from other memory pools */
    cos_pool_create(&pool, NULL);

    /* Create and initialize options. This parameter contains global configuration information such as endpoint, access_key_id, acces_key_secret, is_cname, and curl parameters.
     * The memory of the options is assigned by the pool. After the pool is released, the memory of the options is also released. There is no need to release the memory separately.
     */ 
    options = cos_request_options_create(pool);
    options->config = cos_config_create(options->pool);

    /* cos_str_set initializes the cos_string_t type with a char* type string*/
    cos_str_set(&options->config->endpoint, "<user's Endpoint>");              //Enter Endpoint according to the COS service domain name of user's region
    cos_str_set(&options->config->access_key_id, "<user's SecretId>");         //SecretId obtained after the COS service is registered
    cos_str_set(&options->config->access_key_secret, "<user's SecretKey>");    //SecretKey obtained after the COS service is registered
    cos_str_set(&options->config->appid, "<user's AppId>");                    //AppId obtained after the COS service is registered

    /* Whether CNAME is used */
    options->config->is_cname = 0;

    /* Used to set network-related parameters, such as timeout*/
    options->ctl = cos_http_controller_create(options->pool, 0);
```

## How to Use SDK
1. Initialize the SDK.
2. Set the request options.
For more information on the definitions of SecretId, SecretKey, Bucket and other terms and how to obtain them, please see [COS Glossary](/document/product/436/7751).
  * APPID is an account ID assigned by the system after the application for a Tencent cloud account is submitted.
  * Both access_key_id and access_key_secret are account API keys.
  * endpoint is the COS access domain name, which can be viewed on the [**Available Regions for COS**](/document/product/436/6224) page of Tencent Cloud.
  For example, the endpoint of Guangzhou region is cos.ap-guangzhou.myqcloud.com.
3. Set the required parameters for the API.
4. Call the SDK API to initiate the request and obtain the response result.

### Creating Bucket
```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_acl_e cos_acl = COS_ACL_PRIVATE;
    cos_string_t bucket;
    cos_table_t *resp_headers = NULL;
    
    /* Re-create a new memory pool. The second parameter is NULL, which indicates it is not inherited from other memory pools */
    cos_pool_create(&p, NULL);
    
    /* Create and initialize options. This parameter contains global configuration information such as endpoint, access_key_id, acces_key_secret, is_cname, and curl parameters.
     * The memory of the options is assigned by the pool. After the pool is released, the memory of the options is also released. There is no need to release the memory separately.
     */
    options = cos_request_options_create(p);
    options->config = cos_config_create(options->pool);
    init_test_config(options->config, is_cname);
    
    /* Set appid, endpoint, access_key_id, acces_key_secret, is_cname, curl parameters and other configuration information */
    cos_str_set(&options->config->endpoint, TEST_COS_ENDPOINT);
    cos_str_set(&options->config->access_key_id, TEST_ACCESS_KEY_ID);
    cos_str_set(&options->config->access_key_secret, TEST_ACCESS_KEY_SECRET);
    cos_str_set(&options->config->appid, TEST_APPID);
    options->config->is_cname = is_cname;
    options->ctl = cos_http_controller_create(options->pool, 0);
    /* The bucket name entered must be in a format of {name}-{appid} */
    cos_str_set(&bucket, TEST_BUCKET_NAME);

    /* Call API to create a bucket*/
    s = cos_create_bucket(options, &bucket, cos_acl, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("create bucket succeeded\n");
    } else {
        printf("create bucket failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

### Uploading files
```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
    cos_string_t file;
    cos_table_t *resp_headers = NULL;
    
    /* Re-create a new memory pool. The second parameter is NULL, which indicates it is not inherited from other memory pools */
    cos_pool_create(&p, NULL);
    
    /* Create and initialize options. This parameter contains global configuration information such as endpoint, access_key_id, acces_key_secret, is_cname, and curl parameters.
     * The memory of the options is assigned by the pool. After the pool is released, the memory of the options is also released. There is no need to release the memory separately.
     */
    options = cos_request_options_create(p);
    options->config = cos_config_create(options->pool);
    init_test_config(options->config, is_cname);

    /*Set appid, endpoint, access_key_id, acces_key_secret, is_cname, curl parameters and other configuration information */
    cos_str_set(&options->config->endpoint, TEST_COS_ENDPOINT);
    cos_str_set(&options->config->access_key_id, TEST_ACCESS_KEY_ID);
    cos_str_set(&options->config->access_key_secret, TEST_ACCESS_KEY_SECRET);
    cos_str_set(&options->config->appid, TEST_APPID);
    options->config->is_cname = is_cname;
    options->ctl = cos_http_controller_create(options->pool, 0);
    /* The bucket name entered must be in a format of {name}-{appid} */
    cos_str_set(&bucket, TEST_BUCKET_NAME);

    /*Call API to upload file */
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

### Downloading files
```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
    cos_string_t file;
    cos_table_t *resp_headers = NULL;
    
    /* Re-create a new memory pool. The second parameter is NULL, which indicates it is not inherited from other memory pools */
    cos_pool_create(&p, NULL);
    
    /* Create and initialize options. This parameter contains global configuration information such as endpoint, access_key_id, acces_key_secret, is_cname, and curl parameters.
     * The memory of the options is assigned by the pool. After the pool is released, the memory of the options is also released. There is no need to release the memory separately.
     */
    options = cos_request_options_create(p);
    options->config = cos_config_create(options->pool);
    init_test_config(options->config, is_cname);

    /* Set appid, endpoint, access_key_id, acces_key_secret, is_cname, curl parameters and other configuration information */
    cos_str_set(&options->config->endpoint, TEST_COS_ENDPOINT);
    cos_str_set(&options->config->access_key_id, TEST_ACCESS_KEY_ID);
    cos_str_set(&options->config->access_key_secret, TEST_ACCESS_KEY_SECRET);
    cos_str_set(&options->config->appid, TEST_APPID);
    options->config->is_cname = is_cname;
    options->ctl = cos_http_controller_create(options->pool, 0);
    /*The bucket name entered must be in a format of {name}-{appid}*/
    cos_str_set(&bucket, TEST_BUCKET_NAME);

    /* Call API to download file */
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

