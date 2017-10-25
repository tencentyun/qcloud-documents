## Bucket操作

###  Put Bucket

#### 功能说明

Put Bucket请求可以在指定账号下创建一个Bucket。

#### 方法原型

```cpp
cos_status_t *cos_create_bucket(const cos_request_options_t *options, 
                                const cos_string_t *bucket, 
                                cos_acl_e cos_acl, 
                                cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* cos_acl —— (Enum)  ： 允许用户自定义权限。有效值：COS_ACL_PRIVATE(0)，COS_ACL_PUBLIC_READ(1)，COS_ACL_PUBLIC_READ_WRITE(2)。默认值：COS_ACL_PRIVATE(0)。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

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

###  Delete Bucket

#### 功能说明

Delete Bucket 请求可以在指定账号下删除 Bucket，删除之前要求 Bucket为空。

#### 方法原型

```cpp
cos_status_t *cos_delete_bucket(const cos_request_options_t *options,
                                const cos_string_t *bucket, 
                                cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
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

    //delete bucket
    s = cos_delete_bucket(options, &bucket, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("create bucket succeeded\n");
    } else {
        printf("create bucket failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Get Bucket

#### 功能说明

Get Bucket请求等同于List Object请求，可以列出该Bucekt下部分或者所有Object，发起该请求需要拥有Read权限。

#### 方法原型

```cpp
cos_status_t *cos_list_object(const cos_request_options_t *options,
                              const cos_string_t *bucket, 
                              cos_list_object_params_t *params, 
                              cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* params —— (Struct) ： Get Bucket操作参数。
  * encoding_type  —— (String) ： 规定返回值的编码方式。
  * prefix —— (String) ： 前缀匹配，用来规定返回的文件前缀地址。
  * marker —— (String) ： 默认以UTF-8二进制顺序列出条目，所有列出条目从marker开始。
  * delimiter —— (String) ： Get Bucket操作参数。
  * max_ret —— (Struct) ： 单次返回最大的条目数量，默认1000。
  * truncated —— (Boolean) ： 返回条目是否被截断，'true' 或者 'false'。
  * next_marker —— (String) ： 假如返回条目被截断，则返回NextMarker就是下一个条目的起点。
  * object_list —— (Struct) ： Get Bucket操作返回的对象信息列表。
    * key —— (Struct) ： Get Bucket操作返回的Object名称。
    * last_modified —— (Struct) ： Get Bucket操作返回的Object最后修改时间。
    * etag —— (Struct) ： Get Bucket操作返回的对象的SHA-1算法校验值。
    * size —— (Struct) ： Get Bucket操作返回的对象大小，单位Byte。
    * owner_id —— (Struct) ： Get Bucket操作返回的对象拥有者UID信息。
    * storage_class —— (Struct) ： Get Bucket操作返回的对象存储级别。
  * common_prefix_list —— (Struct) ： 将Prefix到delimiter之间的相同路径归为一类，定义为Common Prefix。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
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

    //get bucket(list object)
    cos_list_object_params_t *list_params = NULL;
    cos_list_object_content_t *content = NULL;
    list_params = cos_create_list_object_params(p);
    s = cos_list_object(options, &bucket, list_params, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("list object succeeded\n");
        cos_list_for_each_entry(cos_list_object_content_t, content, &list_params->object_list, node) {
            key = printf("%.*s\n", content->key.len, content->key.data);
        }
    } else {
        printf("list object failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Put Bucket Acl

#### 功能说明

Put Bucket ACL接口用来写入Bucket的ACL表，您可以通过Header："x-cos-acl"，"x-cos-grant-read"，"x-cos-grant-write"，"x-cos-grant-full-control"传入ACL信息。

#### 方法原型

```cpp
cos_status_t *cos_put_bucket_acl(const cos_request_options_t *options, 
                                 const cos_string_t *bucket, 
                                 cos_acl_e cos_acl,
                                 const cos_string_t *grant_read,
                                 const cos_string_t *grant_write,
                                 const cos_string_t *grant_full_ctrl,
                                 cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* cos_acl —— (Enum)  ： 允许用户自定义权限。有效值：COS_ACL_PRIVATE(0)，COS_ACL_PUBLIC_READ(1)，COS_ACL_PUBLIC_READ_WRITE(2)。默认值：COS_ACL_PRIVATE(0)。
* grant_read —— (String) ： 读权限授予者。
* grant_write —— (String) ： 写权限授予者。
* grant_full_ctrl —— (String) ： 读写权限授予者。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
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

    //put bucket acl
    cos_string_t read;
    cos_str_set(&read, "id=\"qcs::cam::uin/12345:uin/12345\", id=\"qcs::cam::uin/45678:uin/45678\"");
    s = cos_put_bucket_acl(options, &bucket, cos_acl, &read, NULL, NULL, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("put bucket acl succeeded\n");
    } else {
        printf("put bucket acl failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Get Bucket Acl

#### 功能说明

Get Bucket ACL接口用来获取Bucket的ACL(access control list)， 即用户空间（Bucket）的访问权限控制列表。 此API接口只有Bucket的持有者有权限操作。

#### 方法原型

```cpp
cos_status_t *cos_get_bucket_acl(const cos_request_options_t *options, 
                                 const cos_string_t *bucket, 
                                 cos_acl_params_t *acl_param, 
                                 cos_table_t **resp_headers)
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* acl_param —— (Struct) ： Get Bucket Acl操作参数。
  * owner_id  —— (String) ： Get Bucket Acl操作返回的Bucket持有者ID。
  * owner_name —— (String) ： Get Bucket Acl操作返回的Bucket持有者的名称。
  * object_list —— (Struct) ： Get Bucket Acl操作返回的被授权者信息与权限信息。
    * type —— (String) ： Get Bucket Acl操作返回的被授权者账户类型。
    * id —— (String) ： Get Bucket Acl操作返回的被授权者用户ID。
    * name —— (String) ： Get Bucket Acl操作返回的被授权者用户名称。
    * permission —— (String) ： Get Bucket Acl操作返回的被授权者权限信息。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
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

    //get bucket acl
    cos_acl_params_t *acl_params = NULL;
    acl_params = cos_create_acl_params(p);
    s = cos_get_bucket_acl(options, &bucket, acl_params, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("get bucket acl succeeded\n");
        printf("acl owner id:%s, name:%s\n", acl_params->owner_id.data, acl_params->owner_name.data);
        cos_acl_grantee_content_t *acl_content = NULL;
        cos_list_for_each_entry(cos_acl_grantee_content_t, acl_content, &acl_params->grantee_list, node) {
            printf("acl grantee type:%s, id:%s, name:%s, permission:%s\n", acl_content->type.data, acl_content->id.data, acl_content->name.data, acl_content->permission.data);
        }
    } else {
        printf("get bucket acl failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Put Bucket Lifecycle

#### 功能说明

Put Bucket Lifecycle接口用来写入Bucket的生命周期规则。

#### 方法原型

```cpp
cos_status_t *cos_put_bucket_lifecycle(const cos_request_options_t *options,
                                       const cos_string_t *bucket, 
                                       cos_list_t *lifecycle_rule_list, 
                                       cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* lifecycle_rule_list —— (Struct) ： Put Bucket Lifecycle操作参数。
  * id  —— (String) ： 生命周期规则ID。
  * prefix —— (String) ： 指定规则所适用的前缀。
  * status —— (String) ： 指明规则是否启用，枚举值：Enabled，Disabled。
  * expire —— (Struct) ： 规则过期属性。
    * days —— (Int) ： 指明多少天后执行删除操作。
    * date —— (String) ： 指明在何时执行删除操作。
  * transition —— (Struct) ： 规则转换属性，对象何时转换被转换为Standard_IA或Nearline。
    * days —— (Int) ： 指明多少天后执行转换操作。
    * date —— (String) ： 指明在何时执行转换操作。
    * storage_class —— (String) ： 指定Object转储到的目标存储类型，枚举值：Standard_IA,Nearline。
  * abort —— (Struct) ： 设置允许分块上传保持运行的最长时间。
    * days —— (Int) ： 指明分块上传开始后多少天内必须完成上传。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
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

    //put bucket lifecycle
    cos_list_t rule_list;
    cos_list_init(&rule_list);
    cos_lifecycle_rule_content_t *rule_content = NULL;

    rule_content = cos_create_lifecycle_rule_content(p);
    cos_str_set(&rule_content->id, "testrule1");
    cos_str_set(&rule_content->prefix, "abc/");
    cos_str_set(&rule_content->status, "Enabled");
    rule_content->expire.days = 60;
    cos_list_add_tail(&rule_content->node, &rule_list);

    rule_content = cos_create_lifecycle_rule_content(p);
    cos_str_set(&rule_content->id, "testrule2");
    cos_str_set(&rule_content->prefix, "efg/");
    cos_str_set(&rule_content->status, "Disabled");
    cos_str_set(&rule_content->transition.storage_class, "Nearline");
    rule_content->transition.days = 30;
    cos_list_add_tail(&rule_content->node, &rule_list);

    rule_content = cos_create_lifecycle_rule_content(p);
    cos_str_set(&rule_content->id, "testrule3");
    cos_str_set(&rule_content->prefix, "xxx/");
    cos_str_set(&rule_content->status, "Enabled");
    rule_content->abort.days = 1;
    cos_list_add_tail(&rule_content->node, &rule_list);
    
    s = cos_put_bucket_lifecycle(options, &bucket, &rule_list, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("put bucket lifecycle succeeded\n");
    } else {
        printf("put bucket lifecycle failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Get Bucket Lifecycle

#### 功能说明

Get Bucket Lifecycle接口用来获取Bucket的生命周期规则。

#### 方法原型

```cpp
cos_status_t *cos_get_bucket_lifecycle(const cos_request_options_t *options,
                                       const cos_string_t *bucket, 
                                       cos_list_t *lifecycle_rule_list, 
                                       cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* lifecycle_rule_list —— (Struct) ： Get Bucket Lifecycle操作参数。
  * id  —— (String) ： 生命周期规则ID。
  * prefix —— (String) ： 规则所适用的前缀。
  * status —— (String) ： 规则是否启用，枚举值：Enabled，Disabled。
  * expire —— (Struct) ： 规则过期属性。
    * days —— (Int) ： 指明多少天后执行删除操作。
    * date —— (String) ： 指明在何时执行删除操作。
  * transition —— (Struct) ： 规则转换属性，对象何时转换被转换为Standard_IA或Nearline。
    * days —— (Int) ： 指明多少天后执行转换操作。
    * date —— (String) ： 指明在何时执行转换操作。
    * storage_class —— (String) ： 指定Object转储到的目标存储类型，枚举值：Standard_IA,Nearline。
  * abort —— (Struct) ： 设置允许分块上传保持运行的最长时间。
    * days —— (Int) ： 指明分块上传开始后多少天内必须完成上传。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
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

    //get bucket lifecycle
    cos_list_t rule_list_ret;
    cos_list_init(&rule_list_ret);
    s = cos_get_bucket_lifecycle(options, &bucket, &rule_list_ret, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("get bucket lifecycle succeeded\n");
    } else {
        printf("get bucket lifecycle failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Delete Bucket Lifecycle

#### 功能说明

Delete Bucket Lifecycle接口用来删除Bucket的生命周期规则。

#### 方法原型

```cpp
cos_status_t *cos_delete_bucket_lifecycle(const cos_request_options_t *options,
                                          const cos_string_t *bucket, 
                                          cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
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

    //delete bucket lifecycle
    s = cos_delete_bucket_lifecycle(options, &bucket, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("delete bucket lifecycle succeeded\n");
    } else {
        printf("delete bucket lifecycle failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Put Bucket CORS

#### 功能说明

Put Bucket CORS接口用来请求设置Bucket的跨域资源共享权限。

#### 方法原型

```cpp
cos_status_t *cos_put_bucket_cors(const cos_request_options_t *options,
                                  const cos_string_t *bucket, 
                                  cos_list_t *cors_rule_list, 
                                  cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* cors_rule_list —— (Struct) ： Put Bucket CORS操作参数。
  * id  —— (String) ： 配置规则ID。
  * allowed_origin —— (String) ： 允许的访问来源，支持通配符*。
  * allowed_method —— (String) ： 允许的 HTTP 操作，枚举值：GET，PUT，HEAD，POST，DELETE。
  * allowed_header —— (String) ： 在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持通配符*。
  * expose_header —— (String) ： 设置浏览器可以接收到的来自服务器端的自定义头部信息。
  * max_age_seconds —— (Int) ： 设置OPTIONS请求得到结果的有效期。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
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

    //put bucket cors
    cos_list_t rule_list;
    cos_list_init(&rule_list);
    cos_cors_rule_content_t *rule_content = NULL;

    rule_content = cos_create_cors_rule_content(p);
    cos_str_set(&rule_content->id, "testrule1");
    cos_str_set(&rule_content->allowed_origin, "http://www.qq1.com");
    cos_str_set(&rule_content->allowed_method, "GET");
    cos_str_set(&rule_content->allowed_header, "*");
    cos_str_set(&rule_content->expose_header, "xxx");
    rule_content->max_age_seconds = 3600;
    cos_list_add_tail(&rule_content->node, &rule_list);

    rule_content = cos_create_cors_rule_content(p);
    cos_str_set(&rule_content->id, "testrule2");
    cos_str_set(&rule_content->allowed_origin, "http://www.qq2.com");
    cos_str_set(&rule_content->allowed_method, "GET");
    cos_str_set(&rule_content->allowed_header, "*");
    cos_str_set(&rule_content->expose_header, "yyy");
    rule_content->max_age_seconds = 7200;
    cos_list_add_tail(&rule_content->node, &rule_list);

    rule_content = cos_create_cors_rule_content(p);
    cos_str_set(&rule_content->id, "testrule3");
    cos_str_set(&rule_content->allowed_origin, "http://www.qq3.com");
    cos_str_set(&rule_content->allowed_method, "GET");
    cos_str_set(&rule_content->allowed_header, "*");
    cos_str_set(&rule_content->expose_header, "zzz");
    rule_content->max_age_seconds = 60;
    cos_list_add_tail(&rule_content->node, &rule_list);

    //put cors
    s = cos_put_bucket_cors(options, &bucket, &rule_list, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("put bucket cors succeeded\n");
    } else {
        printf("put bucket cors failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Get Bucket CORS

#### 功能说明

Get Bucket CORS接口用来请求获取Bucket的跨域资源共享权限配置。

#### 方法原型

```cpp
cos_status_t *cos_get_bucket_cors(const cos_request_options_t *options,
                                  const cos_string_t *bucket, 
                                  cos_list_t *cors_rule_list, 
                                  cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* cors_rule_list —— (Struct) ： Get Bucket CORS操作参数。
  * id  —— (String) ： 配置规则ID。
  * allowed_origin —— (String) ： 允许的访问来源，支持通配符*。
  * allowed_method —— (String) ： 允许的 HTTP 操作，枚举值：GET，PUT，HEAD，POST，DELETE。
  * allowed_header —— (String) ： 在发送 OPTIONS 请求时告知服务端，接下来的请求可以使用哪些自定义的 HTTP 请求头部，支持通配符*。
  * expose_header —— (String) ： 设置浏览器可以接收到的来自服务器端的自定义头部信息。
  * max_age_seconds —— (Int) ： 设置OPTIONS请求得到结果的有效期。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
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

    //get bucket cors
    cos_list_t rule_list_ret;
    cos_list_init(&rule_list_ret);
    s = cos_get_bucket_cors(options, &bucket, &rule_list_ret, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("get bucket cors succeeded\n");
        cos_cors_rule_content_t *content = NULL;
        cos_list_for_each_entry(cos_cors_rule_content_t, content, &rule_list_ret, node) {
            printf("cors id:%s, allowed_origin:%s, allowed_method:%s, allowed_header:%s, expose_header:%s, max_age_seconds:%d\n",
                content->id.data, content->allowed_origin.data, content->allowed_method.data, content->allowed_header.data, content->expose_header.data, content->max_age_seconds);
        }
    } else {
        printf("get bucket cors failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Delete Bucket CORS

#### 功能说明

Delete Bucket CORS接口用来删除Bucket的跨域资源共享权限配置。

#### 方法原型

```cpp
cos_status_t *cos_delete_bucket_cors(const cos_request_options_t *options,
                                     const cos_string_t *bucket, 
                                     cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
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

    //delete bucket cors
    s = cos_delete_bucket_cors(options, &bucket, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("delete bucket cors succeeded\n");
    } else {
        printf("delete bucket cors failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Put Bucket Versioning

#### 功能说明

Put Bucket Versioning接口实现启用或者暂停存储桶的版本控制功能。

#### 方法原型

```cpp
cos_status_t *cos_put_bucket_versioning(const cos_request_options_t *options,
                                        const cos_string_t *bucket, 
                                        cos_versioning_content_t *versioning, 
                                        cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* versioning —— (Struct) ： Put Bucket Versioning操作参数。
  * status  —— (String) ： 版本是否开启，枚举值：Suspended\Enabled。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
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

    //put bucket versioning
    cos_versioning_content_t *versioning = NULL;
    versioning = cos_create_versioning_content(p);
    cos_str_set(&versioning->status, "Enabled");
    s = cos_put_bucket_versioning(options, &bucket, versioning, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("put bucket versioning succeeded\n");
    } else {
        printf("put bucket versioning failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Get Bucket Versioning

#### 功能说明

Get Bucket Versioning接口实现获得存储桶的版本控制信息。

#### 方法原型

```cpp
cos_status_t *cos_get_bucket_versioning(const cos_request_options_t *options,
                                        const cos_string_t *bucket, 
                                        cos_versioning_content_t *versioning, 
                                        cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* versioning —— (Struct) ： Get Bucket Versioning操作参数。
  * status  —— (String) ： 版本是否开启，枚举值：Suspended\Enabled。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
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

    //get bucket versioning
    cos_versioning_content_t *versioning = NULL;
    versioning = cos_create_versioning_content(p);
    s = cos_get_bucket_versioning(options, &bucket, versioning, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("put bucket versioning succeeded\n");
        printf("bucket versioning status: %s\n", versioning->status.data);
    } else {
        printf("put bucket versioning failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Put Bucket Replication

#### 功能说明

Put Bucket Replication请求用于向开启版本管理的存储桶添加replication配置。如果存储桶已经拥有replication配置，那么该请求会替换现有配置。

#### 方法原型

```cpp
cos_status_t *cos_put_bucket_replication(const cos_request_options_t *options,
                                         const cos_string_t *bucket, 
                                         cos_replication_params_t *replication_param, 
                                         cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* replication_param —— (Struct) ： Put Bucket Replication操作参数。
  * role —— (String) ： 操作者账户信息。
  * rule_list —— (Struct) ： replication配置信息。
    * id —— (String) ： 用来标注具体Rule的名称。
    * status —— (String) ： 标识规则是否生效，枚举值：Enabled, Disabled。
    * prefix —— (String) ： 匹配前缀，不可重叠，重叠返回错误。
    * dst_bucket —— (String) ： 目的存储桶标识，格式为资源标识符：qcs:id/0:cos:[region]:appid/[AppId]:[bucketname]。
    * storage_class —— (String) ： 存储级别，枚举值：Standard, Standard_IA, Nearline；默认值：原存储桶级别。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
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

    //put bucket replication
    cos_replication_params_t *replication_param = NULL;
    replication_param = cos_create_replication_params(p);
    cos_str_set(&replication_param->role, "qcs::cam::uin/100000616666:uin/100000616666");
    
    cos_replication_rule_content_t *rule = NULL;
    rule = cos_create_replication_rule_content(p);
    cos_str_set(&rule->id, "Rule_01");
    cos_str_set(&rule->status, "Enabled");
    cos_str_set(&rule->prefix, "test1");
    cos_str_set(&rule->dst_bucket, "qcs:id/0:cos:cn-east:appid/1253686666:replicationtest");
    cos_list_add_tail(&rule->node, &replication_param->rule_list);

    rule = cos_create_replication_rule_content(p);
    cos_str_set(&rule->id, "Rule_02");
    cos_str_set(&rule->status, "Disabled");
    cos_str_set(&rule->prefix, "test2");
    cos_str_set(&rule->storage_class, "Standard_IA");
    cos_str_set(&rule->dst_bucket, "qcs:id/0:cos:cn-east:appid/1253686666:replicationtest");
    cos_list_add_tail(&rule->node, &replication_param->rule_list);

    rule = cos_create_replication_rule_content(p);
    cos_str_set(&rule->id, "Rule_03");
    cos_str_set(&rule->status, "Enabled");
    cos_str_set(&rule->prefix, "test3");
    cos_str_set(&rule->storage_class, "Nearline");
    cos_str_set(&rule->dst_bucket, "qcs:id/0:cos:cn-east:appid/1253686666:replicationtest");
    cos_list_add_tail(&rule->node, &replication_param->rule_list);
    
    s = cos_put_bucket_replication(options, &bucket, replication_param, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("put bucket replication succeeded\n");
    } else {
        printf("put bucket replication failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Get Bucket Replication

#### 功能说明

Get Bucket Replication接口请求实现读取存储桶中用户跨区域复制配置信息。

#### 方法原型

```cpp
cos_status_t *cos_get_bucket_replication(const cos_request_options_t *options,
                                         const cos_string_t *bucket, 
                                         cos_replication_params_t *replication_param, 
                                         cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* replication_param —— (Struct) ： Get Bucket Replication操作参数。
  * role —— (String) ： 操作者账户信息。
  * rule_list —— (Struct) ： replication配置信息。
    * id —— (String) ： 用来标注具体Rule的名称。
    * status —— (String) ： 标识规则是否生效，枚举值：Enabled, Disabled。
    * prefix —— (String) ： 匹配前缀，不可重叠，重叠返回错误。
    * dst_bucket —— (String) ： 目的存储桶标识，格式为资源标识符：qcs:id/0:cos:[region]:appid/[AppId]:[bucketname]。
    * storage_class —— (String) ： 存储级别，枚举值：Standard, Standard_IA, Nearline；默认值：原存储桶级别。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
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

    //get bucket replication
    cos_replication_params_t *replication_param2 = NULL;
    replication_param2 = cos_create_replication_params(p);
    s = cos_get_bucket_replication(options, &bucket, replication_param2, &resp_headers);
    
    if (cos_status_is_ok(s)) {
        printf("get bucket replication succeeded\n");
        printf("ReplicationConfiguration role: %s\n", replication_param2->role.data);
    cos_replication_rule_content_t *content = NULL;
        cos_list_for_each_entry(cos_replication_rule_content_t, content, &replication_param2->rule_list, node) {
        printf("ReplicationConfiguration rule, id:%s, status:%s, prefix:%s, dst_bucket:%s, storage_class:%s\n",
                content->id.data, content->status.data, content->prefix.data, content->dst_bucket.data, content->storage_class.data);
        }
    } else {
        printf("get bucket replication failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Delete Bucket Replication

#### 功能说明

Delete Bucket Replication接口用来删除Bucket的跨区域复制配置。

#### 方法原型

```cpp
cos_status_t *cos_delete_bucket_replication(const cos_request_options_t *options,
                                            const cos_string_t *bucket, 
                                            cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
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

    //delete bucket cors
    s = cos_delete_bucket_replication(options, &bucket, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("delete bucket replication succeeded\n");
    } else {
        printf("delete bucket replication failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

## Object操作

###  Get Object

#### 功能说明

Get Object 请求可以将一个文件（Object）下载至本地。该操作需要对目标 Object 具有读权限或目标 Object 对所有人都开放了读权限（公有读）。

#### 方法原型

```cpp
cos_status_t *cos_get_object_to_file(const cos_request_options_t *options,
                                     const cos_string_t *bucket, 
                                     const cos_string_t *object,
                                     cos_table_t *headers, 
                                     cos_table_t *params,
                                     cos_string_t *filename, 
                                     cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* object —— (String) ： Object名称。
* headers —— (Struct) ： COS请求附加头域。
* params —— (Struct) ： COS请求操作参数。
* filename —— (String) ： Object本地保存文件名称。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

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

###  Head Object

#### 功能说明

Head Object 请求可以取回对应 Object 的元数据，Head的权限与 Get 的权限一致。

#### 方法原型

```cpp
cos_status_t *cos_head_object(const cos_request_options_t *options, 
                              const cos_string_t *bucket, 
                              const cos_string_t *object,
                              cos_table_t *headers, 
                              cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* object —— (String) ： Object名称。
* headers —— (Struct) ： COS请求附加头域。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
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

    //head object
    cos_str_set(&object, TEST_OBJECT_NAME);
    s = cos_head_object(options, &bucket, &object, NULL, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("head object succeeded\n");
    } else {
        printf("head object failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Put Object

#### 功能说明

Put Object请求可以将一个文件（Oject）上传至指定Bucket。

#### 方法原型

```cpp
cos_status_t *cos_put_object_from_file(const cos_request_options_t *options,
                                       const cos_string_t *bucket, 
                                       const cos_string_t *object, 
                                       const cos_string_t *filename,
                                       cos_table_t *headers, 
                                       cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* object —— (String) ： Object名称。
* filename —— (String) ： Object本地文件名称。
* headers —— (Struct) ： COS请求附加头域。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例
 
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

###  Delete Object

#### 功能说明

Delete Object请求可以将一个文件（Object）删除。

#### 方法原型

```cpp
cos_status_t *cos_delete_object(const cos_request_options_t *options,
                                const cos_string_t *bucket, 
                                const cos_string_t *object, 
                                cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* object —— (String) ： Object名称。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
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

    //delete object
    cos_str_set(&object, TEST_OBJECT_NAME);
    s = cos_delete_object(options, &bucket, &object, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("delete object succeeded\n");
    } else {
        printf("delete object failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Delete Multiple Object

#### 功能说明

Delete Multiple Object请求实现批量删除文件，最大支持单次删除1000个文件。对于返回结果，COS提供Verbose和Quiet两种结果模式。Verbose模式将返回每个Object的删除结果；Quiet模式只返回报错的Object信息。

#### 方法原型

```cpp
cos_status_t *cos_delete_objects(const cos_request_options_t *options,
                                 const cos_string_t *bucket, 
                                 cos_list_t *object_list, 
                                 int is_quiet,
                                 cos_table_t **resp_headers, 
                                 cos_list_t *deleted_object_list);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* object_list —— (Struct) ： Object待删除列表。
  * key —— (String) ： 待删除Object名称。
* is_quiet —— (Boolean) ： 决定了是否启动Quiet模式，True(1)启动Quiet模式，False(0)启动Verbose模式，默认False(0)。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。
* deleted_object_list —— (Struct) ： Object删除信息列表。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
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
    
    //init delete object list
    char *object_name1 = TEST_OBJECT_NAME1;
    char *object_name2 = TEST_OBJECT_NAME2;
    cos_object_key_t *content1 = NULL;
    cos_object_key_t *content2 = NULL;
    cos_list_t object_list;
    cos_list_t deleted_object_list;
    cos_list_init(&object_list);
    cos_list_init(&deleted_object_list);
    content1 = cos_create_cos_object_key(p);
    cos_str_set(&content1->key, object_name1);
    cos_list_add_tail(&content1->node, &object_list);
    content2 = cos_create_cos_object_key(p);
    cos_str_set(&content2->key, object_name2);
    cos_list_add_tail(&content2->node, &object_list);
    
    //delete objects
    int is_quiet = COS_TRUE;
    cos_str_set(&object, TEST_OBJECT_NAME);
    s = cos_delete_objects(options, &bucket, &object_list, is_quiet, &resp_headers, &deleted_object_list);
    if (cos_status_is_ok(s)) {
        printf("delete objects succeeded\n");
    } else {
        printf("delete objects failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Put Object Acl

#### 功能说明

Put Object ACL接口用来写入Bucket中某个Object的ACL配置，您可以通过Header："x-cos-acl"，"x-cos-grant-read"，"x-cos-grant-write"，"x-cos-grant-full-control"传入ACL信息。

#### 方法原型

```cpp
cos_status_t *cos_put_object_acl(const cos_request_options_t *options, 
                                 const cos_string_t *bucket,
                                 const cos_string_t *object,  
                                 cos_acl_e cos_acl,
                                 const cos_string_t *grant_read,
                                 const cos_string_t *grant_write,
                                 const cos_string_t *grant_full_ctrl,
                                 cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* object —— (String) ： Object名称。
* cos_acl —— (Enum)  ： 允许用户自定义权限。有效值：COS_ACL_PRIVATE(0)，COS_ACL_PUBLIC_READ(1)，COS_ACL_PUBLIC_READ_WRITE(2)。默认值：COS_ACL_PRIVATE(0)。
* grant_read —— (String) ： 读权限授予者。
* grant_write —— (String) ： 写权限授予者。
* grant_full_ctrl —— (String) ： 读写权限授予者。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
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

    //put object acl
    cos_str_set(&object, TEST_OBJECT_NAME);
    cos_string_t read;
    cos_str_set(&read, "id=\"qcs::cam::uin/12345:uin/12345\", id=\"qcs::cam::uin/45678:uin/45678\"");
    s = cos_put_object_acl(options, &bucket, &object, cos_acl, &read, NULL, NULL, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("put object acl succeeded\n");
    } else {
        printf("put object acl failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p);  
```

###  Get Object Acl

#### 功能说明

Get Object ACL接口用来获取Bucket中某个Object的访问权限。此API接口只有Bucket的持有者有权限操作。

#### 方法原型

```cpp
cos_status_t *cos_get_object_acl(const cos_request_options_t *options, 
                                 const cos_string_t *bucket,
                                 const cos_string_t *object,
                                 cos_acl_params_t *acl_param, 
                                 cos_table_t **resp_headers)
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* object —— (String) ： Object名称。
* acl_param —— (Struct) ： Get Object Acl操作参数。
  * owner_id  —— (String) ： Get Object Acl操作返回的Bucket持有者ID。
  * owner_name —— (String) ： Get Object Acl操作返回的Bucket持有者的名称。
  * object_list —— (Struct) ： Get Object Acl操作返回的被授权者信息与权限信息。
    * type —— (String) ： Get Object Acl操作返回的被授权者账户类型。
    * id —— (String) ： Get Object Acl操作返回的被授权者用户ID。
    * name —— (String) ： Get Object Acl操作返回的被授权者用户名称。
    * permission —— (String) ： Get Object Acl操作返回的被授权者权限信息。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
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

    //get object acl
    cos_acl_params_t *acl_params2 = NULL;
    acl_params2 = cos_create_acl_params(p);
    s = cos_get_object_acl(options, &bucket, &object, acl_params2, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("get object acl succeeded\n");
        printf("acl owner id:%s, name:%s\n", acl_params2->owner_id.data, acl_params2->owner_name.data);
        acl_content = NULL;
        cos_list_for_each_entry(cos_acl_grantee_content_t, acl_content, &acl_params2->grantee_list, node) {
            printf("acl grantee id:%s, name:%s, permission:%s\n", acl_content->id.data, acl_content->name.data, acl_content->permission.data);
        }
    } else {
        printf("get object acl failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Put Object Copy

#### 功能说明

Put Object Copy请求实现将一个文件从源路径复制到目标路径。

#### 方法原型

```cpp
cos_status_t *cos_copy_object(const cos_request_options_t *options,
                              const cos_string_t *copy_source, 
                              const cos_string_t *dest_bucket, 
                              const cos_string_t *dest_object,
                              cos_table_t *headers,
                              cos_copy_object_params_t *copy_object_param,
                              cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* copy_source —— (String) ： 源文件路径。
* dest_bucket —— (String) ： 目的Bucket名称。
* dest_object —— (String) ： 目的Object名称。
* headers —— (Struct) ： COS请求附加头域。
* copy_object_param —— (Struct)  ： Put Object Copy操作参数。
  * etag —— (String) ： 返回文件的MD5算法校验值
  * last_modify —— (String) ： 返回文件最后修改时间，GMT格式
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
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

    //put object copy
    cos_str_set(&object, TEST_OBJECT_NAME);
    cos_string_t copy_source;
    cos_str_set(&copy_source, TEST_COPY_SRC);
    cos_copy_object_params_t *params = NULL;
    params = cos_create_copy_object_params(p);
    s = cos_copy_object(options, &copy_source, &bucket, &object, NULL, params, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("put object copy succeeded\n");
    } else {
        printf("put object copy failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p);  
```

## 分块上传操作

###  Initiate Multipart Upload

#### 功能说明

Initiate Multipart Upload请求实现初始化分片上传，成功执行此请求以后会返回Upload ID用于后续的Upload Part请求。

#### 方法原型

```cpp
cos_status_t *cos_init_multipart_upload(const cos_request_options_t *options, 
                                        const cos_string_t *bucket, 
                                        const cos_string_t *object, 
                                        cos_string_t *upload_id, 
                                        cos_table_t *headers,
                                        cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* object —— (String) ： Object名称。
* upload_id —— (String) ： 操作返回的Upload ID。
* headers —— (Struct) ： COS请求附加头域。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

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

    //init mulitipart upload
    cos_str_set(&object, TEST_OBJECT_NAME);
    s = cos_init_multipart_upload(options, &bucket, &object, 
                                  &upload_id, headers, &resp_headers);
    if (cos_status_is_ok(s)) {
        printf("init multipart upload succeeded\n");
    } else {
        printf("init multipart upload failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Upload Part

#### 功能说明

Upload Part请求实现在初始化以后的分块上传，支持的块的数量为1到10000，块的大小为1 MB 到5 GB。在每次请求Upload Part时候，需要携带partNumber和uploadID，partNumber为块的编号，支持乱序上传。

#### 方法原型

```cpp
cos_status_t *cos_upload_part_from_file(const cos_request_options_t *options,
                                        const cos_string_t *bucket, 
                                        const cos_string_t *object,
                                        const cos_string_t *upload_id, 
                                        int part_num, 
                                        cos_upload_file_t *upload_file,
                                        cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* object —— (String) ： Object名称。
* upload_id —— (String) ： 上传任务编号。
* part_num —— (Int) ： 分块编号。
* upload_file —— (Struct) ： 待上传本地文件信息。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
    cos_string_t file;
    cos_table_t *resp_headers = NULL;
    int part_num = 1;
    int64_t pos = 0;
    int64_t file_length = 0;
    
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

    //upload part from file
    int res = COSE_OK;
    cos_upload_file_t *upload_file = NULL;
    cos_file_buf_t *fb = cos_create_file_buf(p);
    res = cos_open_file_for_all_read(p, TEST_MULTIPART_FILE, fb);
    if (res != COSE_OK) {
        cos_error_log("Open read file fail, filename:%s\n", TEST_MULTIPART_FILE);
        return;
    }
    file_length = fb->file_last;
    apr_file_close(fb->file);
    while(pos < file_length) {
        upload_file = cos_create_upload_file(p);
        cos_str_set(&upload_file->filename, TEST_MULTIPART_FILE);
        upload_file->file_pos = pos;
        pos += 2 * 1024 * 1024;
        upload_file->file_last = pos < file_length ? pos : file_length; //2MB
        s = cos_upload_part_from_file(options, &bucket, &object, &upload_id,
                part_num++, upload_file, &resp_headers);

        if (cos_status_is_ok(s)) {
            printf("upload part succeeded\n");
        } else {
            printf("upload part failed\n");
        }
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Complete Multipart Upload

#### 功能说明

Complete Multipart Upload用来实现完成整个分块上传。当您已经使用Upload Parts上传所有块以后，你可以用该API完成上传。在使用该API时，您必须在Body中给出每一个块的PartNumber和ETag，用来校验块的准确性。

#### 方法原型

```cpp
cos_status_t *cos_complete_multipart_upload(const cos_request_options_t *options,
                                            const cos_string_t *bucket, 
                                            const cos_string_t *object, 
                                            const cos_string_t *upload_id, 
                                            cos_list_t *part_list, 
                                            cos_table_t *headers,
                                            cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* object —— (String) ： Object名称。
* upload_id —— (String) ： 上传任务编号。
* part_list —— (Struct) ： 完成分块上传的参数。
  * part_number —— (String) ： 分块编号。
  * etag —— (String) ： 分块的ETag 值，为 sha1 校验值，需要在校验值前后加上双引号，如 "3a0f1fd698c235af9cf098cb74aa25bc"。
* headers —— (Struct) ： COS请求附加头域。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
    cos_string_t file;
    cos_table_t *resp_headers = NULL;
    cos_list_part_content_t *part_content = NULL;
    cos_complete_part_content_t *complete_part_content = NULL;
    int part_num = 1;
    int64_t pos = 0;
    int64_t file_length = 0;
    
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

    //list part
    params = cos_create_list_upload_part_params(p);
    params->max_ret = 1000;
    cos_list_init(&complete_part_list);
    s = cos_list_upload_part(options, &bucket, &object, &upload_id, 
                             params, &resp_headers);

    if (cos_status_is_ok(s)) {
        printf("List multipart succeeded\n");
    } else {
        printf("List multipart failed\n");
        cos_pool_destroy(p);
        return;
    }

    cos_list_for_each_entry(cos_list_part_content_t, part_content, &params->part_list, node) {
        complete_part_content = cos_create_complete_part_content(p);
        cos_str_set(&complete_part_content->part_number, part_content->part_number.data);
        cos_str_set(&complete_part_content->etag, part_content->etag.data);
        cos_list_add_tail(&complete_part_content->node, &complete_part_list);
    }

    //complete multipart
    s = cos_complete_multipart_upload(options, &bucket, &object, &upload_id,
            &complete_part_list, complete_headers, &resp_headers);

    if (cos_status_is_ok(s)) {
        printf("Complete multipart upload from file succeeded, upload_id:%.*s\n", 
               upload_id.len, upload_id.data);
    } else {
        printf("Complete multipart upload from file failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  List Parts

#### 功能说明

List Parts用来查询特定分块上传中的已上传的块。

#### 方法原型

```cpp
cos_status_t *cos_list_upload_part(const cos_request_options_t *options,
                                   const cos_string_t *bucket, 
                                   const cos_string_t *object, 
                                   const cos_string_t *upload_id, 
                                   cos_list_upload_part_params_t *params,
                                   cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* object —— (String) ： Object名称。
* upload_id —— (String) ： 上传任务编号。
* params —— (Struct) ： List Parts操作参数。
  * part_number_marker —— (String) ： 默认以UTF-8二进制顺序列出条目，所有列出条目从marker开始。
  * encoding_type  —— (String) ： 规定返回值的编码方式。
  * max_ret —— (String) ： 单次返回最大的条目数量，默认1000。
  * truncated —— (Boolean) ： 返回条目是否被截断，'true' 或者 'false'。
  * next_part_number_marker —— (String) ： 假如返回条目被截断，则返回NextMarker就是下一个条目的起点。
  * part_list —— (Struct) ： 完成分块的信息。
    * part_number —— (String) ： 分块编号。
    * size —— (String) ： 分块大小，单位Byte。
    * etag —— (String) ： 分块的 SHA-1 算法校验值。
    * last_modified —— (String) ： 分块最后修改时间。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    int is_cname = 0;
    cos_status_t *s = NULL;
    cos_request_options_t *options = NULL;
    cos_string_t bucket;
    cos_string_t object;
    cos_string_t file;
    cos_table_t *resp_headers = NULL;
    cos_list_part_content_t *part_content = NULL;
    cos_complete_part_content_t *complete_part_content = NULL;
    int part_num = 1;
    int64_t pos = 0;
    int64_t file_length = 0;
    
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

    //list part
    params = cos_create_list_upload_part_params(p);
    params->max_ret = 1000;
    cos_list_init(&complete_part_list);
    s = cos_list_upload_part(options, &bucket, &object, &upload_id, 
                             params, &resp_headers);

    if (cos_status_is_ok(s)) {
        printf("List multipart succeeded\n");
    } else {
        printf("List multipart failed\n");
        cos_pool_destroy(p);
        return;
    }

    cos_list_for_each_entry(cos_list_part_content_t, part_content, &params->part_list, node) {
        complete_part_content = cos_create_complete_part_content(p);
        cos_str_set(&complete_part_content->part_number, part_content->part_number.data);
        cos_str_set(&complete_part_content->etag, part_content->etag.data);
        cos_list_add_tail(&complete_part_content->node, &complete_part_list);
    }

    //complete multipart
    s = cos_complete_multipart_upload(options, &bucket, &object, &upload_id,
            &complete_part_list, complete_headers, &resp_headers);

    if (cos_status_is_ok(s)) {
        printf("Complete multipart upload from file succeeded, upload_id:%.*s\n", 
               upload_id.len, upload_id.data);
    } else {
        printf("Complete multipart upload from file failed\n");
    }
    
    //destroy memory pool
    cos_pool_destroy(p); 
```

###  Abort Multipart Upload

#### 功能说明

Abort Multipart Upload用来实现舍弃一个分块上传并删除已上传的块。当您调用Abort Multipart Upload时，如果有正在使用这个Upload Parts上传块的请求，则Upload Parts会返回失败。

#### 方法原型

```cpp
cos_status_t *cos_abort_multipart_upload(const cos_request_options_t *options,
                                         const cos_string_t *bucket, 
                                         const cos_string_t *object, 
                                         cos_string_t *upload_id, 
                                         cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* object —— (String) ： Object名称。
* upload_id —— (String) ： 上传任务编号。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    cos_string_t bucket;
    cos_string_t object;
    int is_cname = 0;
    cos_table_t *headers = NULL;
    cos_table_t *resp_headers = NULL;
    cos_request_options_t *options = NULL;
    cos_string_t upload_id;
    cos_status_t *s = NULL;

    //create memory pool & init request options
    cos_pool_create(&p, NULL);
    options = cos_request_options_create(p);
    init_test_request_options(options, is_cname);
    headers = cos_table_make(p, 1);
    cos_str_set(&bucket, TEST_BUCKET_NAME);
    cos_str_set(&object, TEST_MULTIPART_OBJECT);

    //init multipart upload
    s = cos_init_multipart_upload(options, &bucket, &object, 
                                  &upload_id, headers, &resp_headers);

    if (cos_status_is_ok(s)) {
        printf("Init multipart upload succeeded, upload_id:%.*s\n", 
               upload_id.len, upload_id.data);
    } else {
        printf("Init multipart upload failed\n"); 
        cos_pool_destroy(p);
        return;
    }
    
    //abort multipart upload
    s = cos_abort_multipart_upload(options, &bucket, &object, &upload_id, 
                                   &resp_headers);

    if (cos_status_is_ok(s)) {
        printf("Abort multipart upload succeeded, upload_id::%.*s\n", 
               upload_id.len, upload_id.data);
    } else {
        printf("Abort multipart upload failed\n"); 
    }    

    cos_pool_destroy(p);
```

###  List Multipart Uploads

#### 功能说明

List Multiparts Uploads用来查询正在进行中的分块上传。单次最多列出1000个正在进行中的分块上传。

#### 方法原型

```cpp
cos_status_t *cos_list_multipart_upload(const cos_request_options_t *options,
                                        const cos_string_t *bucket, 
                                        cos_list_multipart_upload_params_t *params, 
                                        cos_table_t **resp_headers);
```

#### 参数说明

* options —— (Struct) ： COS请求选项。
* bucket —— (String) ： Bucket名称。
* params —— (Struct) ： List Multipart Uploads操作参数。
  * encoding_type  —— (String) ： 规定返回值的编码方式。
  * prefix —— (String) ： 前缀匹配，用来规定返回的文件前缀地址。
  * upload_id_marker —— (String) ： 假如返回条目被截断，则返回NextMarker就是下一个条目的起点。
  * delimiter —— (String) ： 界符为一个符号，如果有Prefix，则将Prefix到delimiter之间的相同路径归为一类，定义为Common Prefix，然后列出所有Common Prefix。如果没有Prefix，则从路径起点开始。
  * max_ret —— (String) ： 单次返回最大的条目数量，默认1000。
  * key_marker —— (String) ： 与upload-id-marker一起使用
    当upload-id-marker未被指定时，ObjectName字母顺序大于key-marker的条目将被列出
    当upload-id-marker被指定时，ObjectName字母顺序大于key-marker的条目被列出，ObjectName字母顺序等于key-marker同时UploadID大于upload-id-marker的条目将被列出。
  * upload_id_marker —— (String) ： 与key-marker一起使用。
    当key-marker未被指定时，upload-id-marker将被忽略
    当key-marker被指定时，ObjectName字母顺序大于key-marker的条目被列出，ObjectName字母顺序等于key-marker同时UploadID大于upload-id-marker的条目将被列出。
  * truncated —— (Boolean) ： 返回条目是否被截断，'true' 或者 'false'。
  * next_key_marker —— (String) ： 假如返回条目被截断，则返回NextMarker就是下一个条目的起点。
  * next_upload_id_marker —— (String) ： 假如返回条目被截断，则返回NextMarker就是下一个条目的起点。
  * upload_list —— (Struct) ： 分块上传的信息。
    * key —— (String) ： Object的名称。
    * upload_id —— (String) ： 标示本次分块上传的ID。
    * initiated —— (String) ： 标示本次分块上传任务的启动时间。
* resp_headers —— (Struct) ： 返回HTTP响应消息的头域。

typedef struct {
    cos_list_t node;
    cos_string_t key;
    cos_string_t upload_id;
    cos_string_t initiated;
} cos_list_multipart_upload_content_t;

#### 返回结果说明

* code —— (Int) ： Bucket名称        
* error_code —— (String)  ： 错误码内容。
* error_msg —— (String)  ： 错误码描述。
* req_id —— (String)  ： 请求消息id。

#### 示例

```cpp
    cos_pool_t *p = NULL;
    cos_string_t bucket;
    int is_cname = 0;
    cos_table_t *resp_headers = NULL;
    cos_request_options_t *options = NULL;
    cos_status_t *s = NULL;
    cos_list_multipart_upload_params_t *list_multipart_params = NULL;
    
    //create memory pool & init request options
    cos_pool_create(&p, NULL);
    options = cos_request_options_create(p);
    init_test_request_options(options, is_cname);
    cos_str_set(&bucket, TEST_BUCKET_NAME);
    
    //list multipart upload
    list_multipart_params = cos_create_list_multipart_upload_params(p);
    list_multipart_params->max_ret = 999;
    s = cos_list_multipart_upload(options, &bucket, list_multipart_params, &resp_headers);
    log_status(s);

    cos_pool_destroy(p);
```
