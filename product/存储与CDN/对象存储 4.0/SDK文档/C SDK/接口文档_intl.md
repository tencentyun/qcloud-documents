XML C SDK operations of COS service return the result corresponding to each API calling, including response code, error code, error description, etc. See the exception types at the end of the document.
> For more information on the definitions of SecretId, SecretKey, Bucket and other terms and how to obtain them, please see [COS Glossary](https://cloud.tencent.com/document/product/436/7751).

The following describes how to use each API in the SDK. For the sake of brevity, subsequent examples only illustrate how to use the API rather than how to handle exceptions.

```cpp
    cos_status_t *s = NULL;
    s = cos_put_object_from_file(options, &bucket, &object, &file, &headers, &resp_headers);
    if (!s && !cos_status_is_ok(s)) {
        // Output logs for exceptions and handle exceptions as needed
        cos_warn_log("failed to put object from file", buf);
        if (s->error_code) cos_warn_log("status->error_code: %s", s->error_code);
        if (s->error_msg) cos_warn_log("status->error_msg: %s", s->error_msg);
        if (s->req_id) cos_warn_log("status->req_id: %s", s->req_id);
    }
```

## Bucket Operations
###  Put Bucket
#### Feature description
This API (Put Bucket) is used to create a Bucket under the specified account.
#### Method prototype
```cpp
cos_status_t *cos_create_bucket(const cos_request_options_t *options, 
                                const cos_string_t *bucket, 
                                cos_acl_e cos_acl, 
                                cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option | Struct | 
| bucket | Bucket name, which must be in a format of {name}-{appid} | String  |
| cos_acl |Allows users to define permissions.<br> Valid values: COS_ACL_PRIVATE(0), COS_ACL_PUBLIC_READ(1) and COS_ACL_PUBLIC_READ_WRITE(2).<br> Default: COS_ACL_PRIVATE(0) | Enum  |
| resp_headers |Returns HTTP response header | Struct | 

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String|  

#### Example
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
#### Feature description
This API (Delete Bucket) is used to delete a Bucket under the specified account. The Bucket must be empty before it can be deleted.

#### Method prototype
```cpp
cos_status_t *cos_delete_bucket(const cos_request_options_t *options,
                                const cos_string_t *bucket, 
                                cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| resp_headers |Returns HTTP response header |Struct| 

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|          
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String| 

#### Example
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
#### Feature description
This API (Get Bucket) is equivalent to List Object. It is used to list some or all of the Objects under the Bucket. Read permission is required to initiate this request.

#### Method prototype
```cpp
cos_status_t *cos_list_object(const cos_request_options_t *options,
                              const cos_string_t *bucket, 
                              cos_list_object_params_t *params, 
                              cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| params | Parameter for the Get Bucket operation | Struct|  
| encoding_type  |The encoding method of the returned value |String|  
| prefix | Indicates the prefix match, which is used to specify the prefix address of the returned file |String|
| marker |Entries are listed using UTF-8 binary order by default, starting from the marker |String|  
| delimiter | Parameter for the Get Bucket operation |String|  
| max_ret |Maximum number of entries returned at a time. Default is 1,000 |Struct|  
| truncated |Indicates whether the returned entry is truncated. Value: 'true' or 'false' |Boolean|  
| next_marker |If the returned entry is truncated, NextMarker represents the starting point of the next entry |String|  
| object_list | Lists the object information returned through the Get Bucket operation |Struct|  
| key | The name of the Object returned through the Get Bucket operation |Struct|  
| last_modified | The time when the Object returned through the Get Bucket operation was last modified |Struct|  
| etag | The SHA-1 algorithm check value of the Object returned through the Get Bucket operation |Struct|  
| size | The size of the Object returned through the Get Bucket operation (in bytes) |Struct|  
| owner_id | The Object owner UID returned through the Get Bucket operation |Struct| 
| storage_class | The storage level of the Object returned through the Get Bucket operation |Struct|  
| common_prefix_list |The same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix |Struct|  
| resp_headers |Returns HTTP response header |Struct|  

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|          
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String|  

#### Example
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

###  Put Bucket ACL
#### Feature description
Put Bucket ACL is used to write the Bucket ACL. You can import ACL information by using Header: "x-cos-acl", "x-cos-grant-read", "x-cos-grant-write", "x-cos-grant-full-control".

#### Method prototype
```cpp
cos_status_t *cos_put_bucket_acl(const cos_request_options_t *options, 
                                 const cos_string_t *bucket, 
                                 cos_acl_e cos_acl,
                                 const cos_string_t *grant_read,
                                 const cos_string_t *grant_write,
                                 const cos_string_t *grant_full_ctrl,
                                 cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| cos_acl | Allows users to define permissions.<br> Valid values: COS_ACL_PRIVATE(0),COS_ACL_PUBLIC_READ(1),COS_ACL_PUBLIC_READ_WRITE(2).<br>Default: COS_ACL_PRIVATE(0)|Enum|   
| grant_read | Users to whom the read permission is granted |String|  
| grant_write | Users to whom the write permission is granted |String|  
| grant_full_ctrl | Users to whom both read and write permissions are granted |String|  
| resp_headers |Returns HTTP response header |Struct| 

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|         
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String|  

#### Example
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

###  Get Bucket ACL 
#### Feature description
This API (Get Bucket ACL) is used to obtain the ACL (Access Control List) of a Bucket. Only the Bucket owner has the access to this API.

#### Method prototype
```cpp
cos_status_t *cos_get_bucket_acl(const cos_request_options_t *options, 
                                 const cos_string_t *bucket, 
                                 cos_acl_params_t *acl_param, 
                                 cos_table_t **resp_headers)
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| acl_param | Parameter for the Get Bucket ACL operation |Struct|  
| owner_id | The Bucket owner ID returned through the Get Bucket ACL operation |String|   
| owner_name | The Bucket owner name returned through the Get Bucket ACL operation |String|  
| object_list | Information of authorized user and permissions returned through the Get Bucket ACL operation |Struct|  
| type | Authorized account type returned through the Get Bucket ACL operation |String|  
| id | Authorized user ID returned through the Get Bucket ACL operation |String|  
| name | Authorized user name returned through the Get Bucket ACL operation |String|  
| permission | Information of authorized user and permissions returned through the Get Bucket ACL operation |String|  
| resp_headers |Returns HTTP response header |Struct|  



#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|          
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String|   

#### Example
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
#### Feature description
This API (Put Bucket Lifecycle) is used to write Bucket lifecycle rules.

#### Method prototype
```cpp
cos_status_t *cos_put_bucket_lifecycle(const cos_request_options_t *options,
                                       const cos_string_t *bucket, 
                                       cos_list_t *lifecycle_rule_list, 
                                       cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| lifecycle_rule_list | Parameter for the Put Bucket Lifecycle operation |Struct|  
| id  | Lifecycle rule ID |String|  
| prefix | Specifies the prefix to which the rule applies. |String|  
| status | Indicates whether the rule is enabled. Enumerated values: Enabled, Disabled. |String|  
| expire | Rule expiration attribute |Struct|  
| days | Indicates the number of days before the deletion operation is performed. |Int|  
| date | Indicates when the deletion operation is performed. |String|  
| transition | Rule transition attribute, which indicates when the Object is transited to Standard_IA |Struct|  
| days | Indicates the number of days before the transition operation is performed. |Int|  
| date | Indicates when the transition operation is performed. |String|  
| storage_class | Specifies the target storage class to which the object is transited. Enumerated values: Standard_IA. |String|  
| abort | Sets the maximum length of time allowed for a multipart upload. |Struct|  
| days | Indicates the number of days within which the upload must be completed after the multipart upload starts. |Int|  
| resp_headers |Returns HTTP response header |Struct|

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|          
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String|

#### Example
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
    cos_str_set(&rule_content->transition.storage_class, "Standard_IA");
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
#### Feature description
This API (Get Bucket Lifecycle) is used to obtain Bucket lifecycle rules.

#### Method prototype
```cpp
cos_status_t *cos_get_bucket_lifecycle(const cos_request_options_t *options,
                                       const cos_string_t *bucket, 
                                       cos_list_t *lifecycle_rule_list, 
                                       cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| lifecycle_rule_list | Parameter for the Get Bucket Lifecycle operation |Struct|  
| id  | Lifecycle rule ID |String|  
| prefix | The prefix to which the rule applies |String|  
| status | Indicates whether the rule is enabled. Enumerated values: Enabled, Disabled. |String|  
| expire | Rule expiration attribute |Struct|  
| days | Indicates the number of days before the deletion operation is performed. |Int|  
| date | Indicates when the deletion operation is performed. |String|  
| transition | Rule transition attribute, which indicates when the Object is transited to Standard_IA |Struct|  
| days | Indicates the number of days before the transition operation is performed. |Int|  
| date | Indicates when the transition operation is performed. |String|  
| storage_class | Specifies the target storage class to which the object is transited. Enumerated values: Standard_IA. |String|  
| abort | Sets the maximum time length allowed for a multipart upload. |Struct|  
| days | Indicates the number of days within which the upload must be completed after the multipart upload starts. |Int|  
| resp_headers |Returns HTTP response header |Struct| 

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|         
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String|   

#### Example
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
#### Feature description
This API (Delete Bucket Lifecycle) is used to delete Bucket lifecycle rules.

#### Method prototype
```cpp
cos_status_t *cos_delete_bucket_lifecycle(const cos_request_options_t *options,
                                          const cos_string_t *bucket, 
                                          cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| resp_headers |Returns HTTP response header |Struct| 

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String| 

#### Example
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
#### Feature description
This API (Put Bucket CORS) is used to set the cross-origin resource sharing permission of the Bucket.

#### Method prototype
```cpp
cos_status_t *cos_put_bucket_cors(const cos_request_options_t *options,
                                  const cos_string_t *bucket, 
                                  cos_list_t *cors_rule_list, 
                                  cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| cors_rule_list | Parameter for the Put Bucket CORS operation |Struct|  
| id  | Sets rule ID |String|  
| allowed_origin | Allowed access sources. The wildcard `*` is supported |String|  
| allowed_method | Allowed HTTP operations. Enumerated values: GET, PUT, HEAD, POST, DELETE |String|  
| allowed_header | When an OPTIONS request is sent, notifies the server about which custom HTTP request headers are allowed for subsequent requests. Wildcard "*" is supported. |String|  
| expose_header |Sets the custom header information that can be received by the browser from the server end |String|  
| max_age_seconds |Sets the validity period of the results obtained by OPTIONS |Int|  
| resp_headers |Returns HTTP response header |Struct|  


#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String| 

#### Example
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
#### Feature description
This API (Get Bucket CORS) is used to obtain the cross-origin resource sharing permission configuration of the Bucket.
#### Method prototype
```cpp
cos_status_t *cos_get_bucket_cors(const cos_request_options_t *options,
                                  const cos_string_t *bucket, 
                                  cos_list_t *cors_rule_list, 
                                  cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| cors_rule_list | Parameter for the Get Bucket CORS operation |Struct| 
| id  | Sets rule ID |String|  
| allowed_origin | Allowed access sources. The wildcard `*` is supported |String| 
| allowed_method | Allowed HTTP operations. Enumerated values: GET, PUT, HEAD, POST, DELETE |String|  
| allowed_header | When an OPTIONS request is sent, notifies the server about which custom HTTP request headers are allowed for subsequent requests. Wildcard "*" is supported. |String|  
| expose_header |Sets the custom header information that can be received by the browser from the server end |String|  
| max_age_seconds |Sets the validity period of the results obtained by OPTIONS |Int|  
| resp_headers |Returns HTTP response header |Struct| 

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String| 

#### Example
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
#### Feature description
This API (Delete Bucket CORS) is used to delete the cross-origin resource sharing permission configuration of the Bucket.

#### Method prototype
```cpp
cos_status_t *cos_delete_bucket_cors(const cos_request_options_t *options,
                                     const cos_string_t *bucket, 
                                     cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| resp_headers |Returns HTTP response header |Struct| 

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String| 

#### Example
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
#### Feature description
This API (Put Bucket Versioning) is used to enable or suspend the version control of the Bucket.

#### Method prototype
```cpp
cos_status_t *cos_put_bucket_versioning(const cos_request_options_t *options,
                                        const cos_string_t *bucket, 
                                        cos_versioning_content_t *versioning, 
                                        cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| versioning | Parameter for the Put Bucket Versioning operation |Struct|  
| status  | Indicates whether version is enabled. Enumerated values: Suspended, Enabled. |String|  
| resp_headers |Returns HTTP response header |Struct|  

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String| 

#### Example
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
#### Feature description
This API (Get Bucket Versioning) is used to obtain the information on the version control of the Bucket.

#### Method prototype
```cpp
cos_status_t *cos_get_bucket_versioning(const cos_request_options_t *options,
                                        const cos_string_t *bucket, 
                                        cos_versioning_content_t *versioning, 
                                        cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| versioning | Parameter for the Get Bucket Versioning operation |Struct|  
| status  | Indicates whether version is enabled. Enumerated values: Suspended, Enabled. |String|  
| resp_headers |Returns HTTP response header |Struct|  

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String| 

#### Example
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
#### Feature description
This API (Put Bucket Replication) is used to add replication configuration to the bucket for which versioning is enabled. If the bucket already has a replication configuration, the request will replace the existing configuration.

#### Method prototype
```cpp
cos_status_t *cos_put_bucket_replication(const cos_request_options_t *options,
                                         const cos_string_t *bucket, 
                                         cos_replication_params_t *replication_param, 
                                         cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option | Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| replication_param | Parameter for the Put Bucket Replication operation |Struct|  
| role | Operator's account information |String|  
| rule_list | replication configuration information |Struct|  
| id | Indicates the name of a specific Rule. |String|  
| status | Indicates whether the rule is enabled. Enumerated values: Enabled, Disabled. |String|  
| prefix | Prefix match. Prefixes cannot overlap, otherwise an error is returned. |String|  
| dst_bucket | Destination bucket ID. Format: resource identifier qcs:id/0:cos:[Region]:appid/[APPID]:[Bucketname]. |String|  
| storage_class | The storage class of Object. Enumerated values: Standard, Standard_IA.<br> Default value: the original bucket class. |String|  
| resp_headers |Returns HTTP response header | Struct|  

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String| 

#### Example
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
    cos_str_set(&rule->storage_class, "Standard_IA");
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

#### Feature description
This API (Get Bucket Replication) is used to read the cross-origin replication configuration information in a bucket.

#### Method prototype
```cpp
cos_status_t *cos_get_bucket_replication(const cos_request_options_t *options,
                                         const cos_string_t *bucket, 
                                         cos_replication_params_t *replication_param, 
                                         cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| replication_param | Parameter for the Get Bucket Replication operation |Struct|  
| role | Operator's account information |String|  
| rule_list | replication configuration information |Struct|  
| id | Indicates the name of a specific Rule. |String|  
| status | Indicates whether the rule is enabled. Enumerated values: Enabled, Disabled. |String|  
| prefix | Prefix match. Prefixes cannot overlap, otherwise an error is returned. |String|  
| dst_bucket | Destination bucket ID. Format: resource identifier qcs:id/0:cos:[Region]:appid/[APPID]:[Bucketname]. |String|  
| storage_class | The storage class of Object. Enumerated values: Standard, Standard_IA.<br> Default value: the original bucket class. |String|  
| resp_headers | Returns HTTP response header |Struct|  

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String| 

#### Example
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
#### Feature description
This API (Delete Bucket Replication) is used to delete the cross-origin replication configuration in the Bucket.

#### Method prototype
```cpp
cos_status_t *cos_delete_bucket_replication(const cos_request_options_t *options,
                                            const cos_string_t *bucket, 
                                            cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| resp_headers |Returns HTTP response header |Struct|  

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String|

#### Example
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

## Object Operations
###  Get Object
#### Feature description
This API (Delete Object) is used to download a file (Object) locally. This operation requires that the user have the read permission for the target Object or the read permission for the target Object be available for everyone (public-read).

#### Method prototype
```cpp
cos_status_t *cos_get_object_to_file(const cos_request_options_t *options,
                                     const cos_string_t *bucket, 
                                     const cos_string_t *object,
                                     cos_table_t *headers, 
                                     cos_table_t *params,
                                     cos_string_t *filename, 
                                     cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| object | Object name |String|  
| headers | Additional COS request header |Struct|  
| params | Parameter for the COS request operation |Struct|  
| filename | The file name of an Object stored locally |String|  
| resp_headers |Returns HTTP response header |Struct|  

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String| 

#### Example
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
#### Feature description
This API (Head Object) is used to get the metadata of an Object. It has the same permissions as Get Object.

#### Method prototype
```cpp
cos_status_t *cos_head_object(const cos_request_options_t *options, 
                              const cos_string_t *bucket, 
                              const cos_string_t *object,
                              cos_table_t *headers, 
                              cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| object | Object name |String|  
| headers | Additional COS request header |Struct|  
| resp_headers |Returns HTTP response header |Struct|  

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String| 

#### Example
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
#### Feature description
This API (Put Object) is used to upload a file (Object) to the specified Bucket.

#### Method prototype
```cpp
cos_status_t *cos_put_object_from_file(const cos_request_options_t *options,
                                       const cos_string_t *bucket, 
                                       const cos_string_t *object, 
                                       const cos_string_t *filename,
                                       cos_table_t *headers, 
                                       cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| object | Object name |String|  
| filename | The file name of an Object stored locally |String|  
| headers | Additional COS request header |Struct|  
| resp_headers |Returns HTTP response header |Struct| 

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String| 

#### Example
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
#### Feature description
This API (Delete Object) is used to delete a file (Object).

#### Method prototype
```cpp
cos_status_t *cos_delete_object(const cos_request_options_t *options,
                                const cos_string_t *bucket, 
                                const cos_string_t *object, 
                                cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| object | Object name |String|  
| resp_headers |Returns HTTP response header |Struct| 

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String| 

#### Example
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
#### Feature description
This API (Delete Multiple Object) is used for batch deletion of files. A maximum of 1000 files are allowed to be deleted at a time. COS provides two modes for returned results: Verbose and Quiet. Verbose mode will return the result of deletion of each Object, while Quiet mode only returns the information of the Objects with an error.

#### Method prototype
```cpp
cos_status_t *cos_delete_objects(const cos_request_options_t *options,
                                 const cos_string_t *bucket, 
                                 cos_list_t *object_list, 
                                 int is_quiet,
                                 cos_table_t **resp_headers, 
                                 cos_list_t *deleted_object_list);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String| 
| object_list | List of objects to be deleted |Struct| 
  | key | Name of object to be deleted |String|  
| is_quiet | Indicates whether the Quiet mode is enabled.<br> True(1): Quiet mode is enabled; False(0): Verbose mode is enabled. Default is False(0). |Boolean|  
| resp_headers | Returns HTTP response header |Struct|  
| deleted_object_list | List of deleted objects |Struct|  

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String|

#### Example
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

###  Put Object ACL
#### Feature description
This API (Put Object ACL) is used to write the ACL configuration of an Object in the Bucket. You can import ACL information by using Header: "x-cos-acl", "x-cos-grant-read", "x-cos-grant-write", "x-cos-grant-full-control".

#### Method prototype
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

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| object | Object name | String|  
| cos_acl | Allow users to define permissions. Valid values: COS_ACL_PRIVATE(0), COS_ACL_PUBLIC_READ(1) and COS_ACL_PUBLIC_READ_WRITE(2). Default: COS_ACL_PRIVATE(0) |Enum|   
| grant_read | Users to whom the read permission is granted |String|  
| grant_write | Users to whom the write permission is granted |String|  
| grant_full_ctrl | Users to whom both read and write permissions are granted |String|  
| resp_headers |Returns HTTP response header |Struct|  

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String| 

#### Example
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

###  Get Object ACL
#### Feature description
This API (Get Object ACL) is used to obtain access permission of an Object under a Bucket. Only the Bucket owner has the access to this API.

#### Method prototype
```cpp
cos_status_t *cos_get_object_acl(const cos_request_options_t *options, 
                                 const cos_string_t *bucket,
                                 const cos_string_t *object,
                                 cos_acl_params_t *acl_param, 
                                 cos_table_t **resp_headers)
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| object | Object name |String|  
| acl_param | Parameter for the Get Object ACL operation |Struct|  
| owner_id  | The Bucket owner ID returned through the Get Object ACL operation |String|  
| owner_name | The Bucket owner name returned through the Get Object ACL operation |String|  
| object_list | Information of authorized user and permissions returned through the Get Object ACL operation |Struct|  
| type | Authorized account type returned through the Get Object ACL operation |String|  
| id | Authorized user ID returned through the Get Object ACL operation |String|  
| name | Authorized user name returned through the Get Object ACL operation |String|  
| permission | Information of authorized user and permissions returned through the Get Object ACL operation |String|  
| resp_headers | Returns HTTP response header |Struct|  

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String| 

#### Example
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
#### Feature description
This API (Put Object Copy) is used to copy a file from source path to the destination path.

#### Method prototype
```cpp
cos_status_t *cos_copy_object(const cos_request_options_t *options,
                              const cos_string_t *copy_source, 
                              const cos_string_t *dest_bucket, 
                              const cos_string_t *dest_object,
                              cos_table_t *headers,
                              cos_copy_object_params_t *copy_object_param,
                              cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| copy_source | Path of the source file |String|  
| dest_bucket | Destination bucket name, which must be in a format of {name}-{appid} |String|  
| dest_object | Destination object name |String|  
| headers | Additional COS request header |Struct|  
| copy_object_param | Parameter for the Put Object Copy operation |Struct|   
| etag | MD5 algorithm check value for the returned file |String|  
| last_modify | Returns the last modification time of the file in GMT format |String|  
| resp_headers |Returns HTTP response header |Struct| 

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String| 

#### Example
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

## Multipart Upload Operations
###  Initiate Multipart Upload
#### Feature description
This API (Initiate Multipart Upload) is used to initialize multipart upload. After the request is executed successfully, Upload ID is returned for the subsequent Upload Part requests.

#### Method prototype
```cpp
cos_status_t *cos_init_multipart_upload(const cos_request_options_t *options, 
                                        const cos_string_t *bucket, 
                                        const cos_string_t *object, 
                                        cos_string_t *upload_id, 
                                        cos_table_t *headers,
                                        cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| object | Object name |String|  
| upload_id | Upload ID returned through the operation |String|  
| headers | Additional COS request header |Struct|  
| resp_headers |Returns HTTP response header |Struct| 

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String| 

#### Example
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
#### Feature description
This API (Upload Part) is used to implement multipart upload after initialization. A file can be split into 10000 chunks at most (minimum is 1) for multipart upload, and the size of each file chunk should be between 1 MB and 5 GB. Parameters partNumber and uploadId are required for Upload Part (partNumber is the file chunk No. Out-of-order upload is supported).

#### Method prototype
```cpp
cos_status_t *cos_upload_part_from_file(const cos_request_options_t *options,
                                        const cos_string_t *bucket, 
                                        const cos_string_t *object,
                                        const cos_string_t *upload_id, 
                                        int part_num, 
                                        cos_upload_file_t *upload_file,
                                        cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| object | Object name |String|  
| upload_id |Upload task number |String|  
| part_num | Part number |Int|  
| upload_file | Information on the local file to be uploaded |Struct|  
| resp_headers |Returns HTTP response header |Struct|  

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String|

#### Example
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
#### Feature description
Complete Multipart Upload  is used to complete the entire multipart upload. After you have uploaded all the file chunks using Upload Parts, you can use this API to complete the upload. When using this API, you need to provide the PartNumber and ETag for every chunk in Body, to verify the accuracy of chunks.

#### Method prototype
```cpp
cos_status_t *cos_complete_multipart_upload(const cos_request_options_t *options,
                                            const cos_string_t *bucket, 
                                            const cos_string_t *object, 
                                            const cos_string_t *upload_id, 
                                            cos_list_t *part_list, 
                                            cos_table_t *headers,
                                            cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options |  COS request option ||Struct|  
| bucket | Bucket  name, which must be in a format of {name}-{appid} |String|  
| object |  Object name |String|  
| upload_id | Upload task number |String|  
| part_list | Parameter for the Complete Multipart Upload operation|Struct|  
| part_number | Part number |String|  
| etag | ETag value of a part, which is sha1 check value. It must be enclosed in double quotes, such as "3a0f1fd698c235af9cf098cb74aa25bc"|String|  
| headers |  Additional COS request header |Struct| 
| resp_headers | Returns HTTP response header |Struct|  

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error Codes  |Int|        
| error_code |  Error description |String|   
| error_msg | Error message  |String|   
| req_id |  Request message ID |String| 

#### Example
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
#### Feature description
This API (List Parts) is used to query the uploaded parts in a specific multipart upload process.

#### Method prototype
```cpp
cos_status_t *cos_list_upload_part(const cos_request_options_t *options,
                                   const cos_string_t *bucket, 
                                   const cos_string_t *object, 
                                   const cos_string_t *upload_id, 
                                   cos_list_upload_part_params_t *params,
                                   cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| object | Object name |String|  
| upload_id | Upload task number |String|  
| params | Parameter for the List Parts operation |Struct| 
| part_number_marker |Entries are listed using UTF-8 binary order by default, starting from the marker |String|  
| encoding_type  |The encoding method of the returned value |String|  
| max_ret | Maximum number of entries returned at a time. Default is 1,000 |String|  
| truncated |Indicates whether the returned entry is truncated. Value: 'true' or 'false' |Boolean|  
| next_part_number_marker | If the returned entry is truncated, NextMarker represents the starting point of the next entry |String|  
| part_list | Information on completed part |Struct|      
| part_number | Part number |String|  
| size |Part size (in bytes) |String|  
| etag | SHA-1 algorithm check value for the part |String|  
| last_modified | The time when the part was last modified |String|  
| resp_headers |Returns HTTP response header |Struct|  

#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String| 

#### Example
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
#### Feature description
This API (Abort Multipart Upload) is used to abort a multipart upload operation and delete uploaded file chunks. When Abort Multipart Upload is called, a failure is returned for any request that is using Upload Parts.

#### Method prototype
```cpp
cos_status_t *cos_abort_multipart_upload(const cos_request_options_t *options,
                                         const cos_string_t *bucket, 
                                         const cos_string_t *object, 
                                         cos_string_t *upload_id, 
                                         cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct| 
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| object | Object name |String|  
| upload_id | Upload task number |String| 
| resp_headers |Returns HTTP response header |Struct|  


#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String|

#### Example
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
#### Feature description
This API (List Multiparts Uploads) is used to query multipart upload operations that are still in process. Up to 1000 such operations can be listed each time.

#### Method prototype
```cpp
cos_status_t *cos_list_multipart_upload(const cos_request_options_t *options,
                                        const cos_string_t *bucket, 
                                        cos_list_multipart_upload_params_t *params, 
                                        cos_table_t **resp_headers);
```

#### Parameters
| Parameter Name | Description | Type | 
|---------|---------|---------|
| options | COS request option |Struct|  
| bucket | Bucket name, which must be in a format of {name}-{appid} |String|  
| params | Parameter for the List Multipart Uploads operation |Struct|  
| encoding_type  |The encoding method of the returned value |String|  
| prefix | Indicates the prefix match, which is used to specify the prefix address of the returned file |String| 
| upload_id_marker |If the returned entry is truncated, NextMarker represents the starting point of the next entry |String|
| delimiter | Delimiter is a sign.<br> If Prefix exists, the same paths between Prefix and delimiter are grouped as the same type and defined as Common Prefix, and then all Common Prefixes are listed.<br> If Prefix does not exist, the listing process starts from the beginning of the path. |String|  
| max_ret | Maximum number of entries returned at a time. Default is 1,000 |String|  
| key_marker | Used together with upload-id-marker.<br> If upload-id-marker is not specified, entries whose ObjectNames are in front of key-marker (according to alphabetical order) will be listed.<br> If upload-id-marker is specified, entries whose ObjectNames are in front of key-marker (according to alphabetical order) will be listed, and entries whose ObjectNames are equal to key-marker and UploadIDs are in front of upload-id-marker (according to alphabetical order) will also be listed. |String|  
| upload_id_marker | Used together with key-marker.<br> If key-marker is not specified, upload-id-marker will be ignored.<br> If key-marker is specified, entries whose ObjectNames are in front of key-marker (according to alphabetical order) will be listed, and entries whose ObjectNames are equal to key-marker and UploadIDs are in front of upload-id-marker (according to alphabetical order) will also be listed. |String| 
| truncated |Indicates whether the returned entry is truncated. Value: 'true' or 'false' |Boolean|  
| next_key_marker |If the returned entry is truncated, NextMarker represents the starting point of the next entry |String|  
| next_upload_id_marker |If the returned entry is truncated, NextMarker represents the starting point of the next entry |String|  
| upload_list | Provides information on multipart upload |Struct|  
| key |Object name |String|  
| upload_id |The ID of current multipart upload |String|  
| initiated | Indicates the start time of current multipart upload. |String|  
| resp_headers |Returns HTTP response header |Struct|  

```
typedef struct {
    cos_list_t node;
    cos_string_t key;
    cos_string_t upload_id;
    cos_string_t initiated;
} cos_list_multipart_upload_content_t;
```


#### Returned result
| Returned Result | Description | Type | 
|---------|---------|---------|
| code | Error code |Int|        
| error_code | Error description |String|   
| error_msg | Error message |String|   
| req_id | Request message ID |String|

#### Example
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

## Exception Description

If the SDK operation fails, the result information can be found in the cos_status_t structure returned by the API.

The cos_status_t structure comprises of the following:

| cos_status_t Member | Description | Type |
| ---------------- | ---------------------------------------- | --------- |
| code    | Status code of the response. 4xx represents the request failure caused by the client, and 5xx represents the failure caused by the server exception For more information, please see [COS Error Message](https://cloud.tencent.com/document/product/436/7730)               | Int    |
| error_code      | Error Code returned by body when request fails. For more information, please see [COS Error Message](https://cloud.tencent.com/document/product/436/7730)                              | String    |
| error_msg   | Error Message returned by body when request fails. For more information, please see [COS Error Message](https://cloud.tencent.com/document/product/436/7730) | String    |
| req_id | Request ID, which is used to identify the user's unique request | String    |

