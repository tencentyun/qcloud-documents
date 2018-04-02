## Preparations for Development

### Related Resources

* [GitHub](https://github.com/tencentyun/cos-python-sdk-v4) GitHub project address. Welcome to share codes and report problems.
* [PyPi](https://pypi.python.org/pypi/qcloud_cos_v4) PyPi project address 


### Environment Dependency

Python 2.7

How to get python version:

- Linux Shell

```shell
$ python -V
Python 2.7.11
```

- Windows cmd

```shell
D:\>python -V
Python 2.7.11
```

If prompted that it is not an internal or external command, please add the absolute path of python to the windows environment variable PATH first

### Installing SDK

- pip installation

```shell
pip install qcloud_cos_v4
```

- Source code installation

Download SDK on github, decompress it and perform the following operations (if prompted "permission deny", you need to have administrator permissions)

```shell
python setup.py install
```

### Uninstalling SDK

```shell
pip uninstall qcloud_cos_v4
```


## Generating Client Object

### Initializing the Client


```python
	appid = 100000                  # Replaced with user's appid
    secret_id = u'xxxxxxxx'         # Replaced with user's secret_id
    secret_key = u'xxxxxxx'         # Replaced with user's secret_key
    region_info = "sh"             # Replaced with user's region. For example, sh refers to East China region, gz refers to South China region, and tj refers to North China region
    cos_client = CosClient(appid, secret_id, secret_key, region=region_info)
```



### Customizing Connection Point

If you need to use a customized connected domain, you can set it as follows
```python
	conf = CosConfig(hostname='', download_hostname='')
	cos_client.set_config(conf)
```

## File-related Operations

### Uploading a File

#### Method Prototype

```python
def upload_file(self, request)
```

#### Parameter Description

|   Parameter Name   |        Type         | Default Value  |   Description   |
| :-----: | :---------------: | :--: | :------: |
| request | UploadFileRequest |  None   | Uploading file request |

|  request Member  |      Type      | Default Value  |    Setting Method   |                    Description                    |
| :---------: | :----------: | :--: | :--------: | :--------------------------------------: |
| bucket_name |   unicode    |  None   | Constructor or set method |                 bucket name                 |
|  cos_path   |   unicode    |  None   |  Constructor or set method | cos path, which must start with the root / under the bucket. File path cannot end with /. For example, /mytest/demo.txt |
| local_path  |   unicode    |  None  | Constructor or set method |              The absolute path of the local file to be uploaded               |
|  biz_attr   |   unicode    |  Null   | Constructor or set method |           Note for file, mainly the description of the use of the file            |
| insert_only | int     (enumeration) |  1   | Constructor or set method | Indicate whether to insert only and not overwrite the existing file. 1 means inserting only and not overwriting the existing file; when the file exists, an error will be returned. 0 means overwriting the existing file |

#### Returned Value

| Type of Returned Value |                  Description of Returned Value                   |
| :---: | :--------------------------------------: |
| dict  | {'code':\$code,  'message':$mess, 'data':\$data}. If "code" is 0, it means success. "message" indicates SUCCESS or failure reason. "data" contains related attributes. For details, refer to the Returned Value module |

#### Example

```python
    request = UploadFileRequest(bucket, u'/sample_file.txt', u'local_file_1.txt')
    upload_file_ret = cos_client.upload_file(request)
```

### Getting File Attributes

#### Method Prototype

```python
def stat_file(self, request)
```

#### Parameter Description

|   Parameter Name   |      Type       | Default Value  |   Description   |
| :-----: | :-------------: | :--: | :------: |
| request | StatFileRequest | None | Getting file attribute request |

|  request Member  |   Type    | Default Value  |    Setting Method    |                    Description                    |
| :---------: | :-----: | :--: | :--------: | :--------------------------------------: |
| bucket_name | unicode |  None   | Constructor or set method |                 bucket name                 |
|  cos_path   | unicode |  None   | Constructor or set method | cos path, which must start with the root / under the bucket. File path cannot end with /. For example, /mytest/demo.txt |

#### Returned Value

| Type of Returned Value |                  Description of Returned Value                   |
| :---: | :--------------------------------------: |
| dict  | {'code':\$code,  'message':$mess, 'data':\$data}. If "code" is 0, it means success. "message" indicates SUCCESS or failure reason. "data" contains related attributes. For details, refer to the Returned Value module |

#### Example

```python
    request = StatFileRequest(bucket, u'/sample_file.txt')
    stat_file_ret = cos_client.stat_file(request)
```

### Updating File Attributes

#### Method Prototype

```python
def update_file(self, request)
```

#### Parameter Description

|   Parameter Name   |       Type        | Default Value  |   Description   |
| :-----: | :---------------: | :--: | :------: |
| request | UpdateFileRequest |  None   | Updating file attribute request |

|      request Member      |      Type      | Default Value  |    Setting Method    |                    Description                    |
| :-----------------: | :----------: | :--: | :--------: | :--------------------------------------: |
|     bucket_name     |   unicode    |  None   | Constructor or set method |                 bucket name                 |
|      cos_path       |   unicode    |  None   |  Constructor or set method | cos path, which must start with the root / under the bucket. File path cannot end with /. For example, /mytest/demo.txt |
|      biz_attr       |   unicode    |  None   |   set method    |           Note for file, mainly the description of the use of the file            |
|      authority      | unicode (enumeration) |  None   |   set method | File permissions. The valid values of bucket permissions will be inherited by default: eInvalid (inherit bucket), eWRPrivate (private), eWPrivateRPublic (public-read) |
|    cache_control    |   unicode    |  None   |   set method    |           Refer to the Cache-Control in HTTP header           |
|    content_type     |   unicode    |  None   |   set method    |           Refer to the Content-Type in HTTP header            |
|  content_language   |   unicode    |  None   |   set method    |         Refer to the Content-Language in HTTP header          |
| content_disposition |   unicode    |  None   |   set method    |        Refer to the Content-Disposition in HTTP header        |
|     x-cos-meta-     |   unicode    |  None   |   set method    | Customized HTTP header. Parameters must start with x-cos-meta-, and the value is defined by the user. Multiple values are allowed |

**Tips:** You can update only some of the attributes. For the HTTP headers cache_control, content_type, content_disposition and x-cos-meta-, if you just update some, other headers will be erased. That is, these four attributes are updated as a whole.

#### Returned Value

| Type of Returned Value |                  Description of Returned Value                   |
| :---: | :--------------------------------------: |
| dict  | {'code':\$code,  'message':$mess}. If "code" is 0, it means success. "message" indicates SUCCESS or failure reason. For details, refer to the Returned Value module |

#### Example

```python
    request = UpdateFileRequest(bucket, u'/sample_file.txt')

    request.set_biz_attr(u'This is a demo file')            # Set biz_attr attribute
    request.set_authority(u'eWRPrivate')              # Set file permissions
    request.set_cache_control(u'cache_xxx')           # Set Cache-Control
    request.set_content_type(u'application/text')     # Set Content-Type
    request.set_content_disposition(u'ccccxxx.txt')   # Set Content-Disposition
    request.set_content_language(u'english')          # Set Content-Language
    request.set_x_cos_meta(u'x-cos-meta-xxx', u'xxx') # Set the customized x-cos-meta- attribute
    request.set_x_cos_meta(u'x-cos-meta-yyy', u'yyy') # Set the customized x-cos-meta- attribute

    update_file_ret = cos_client.update_file(request)
```

### Deleting a File

#### Method Prototype

```python
def del_file(self, request)
```

#### Parameter Description

|   Parameter Name   |      Type      | Default Value  |  Description  |
| :-----: | :------------: | :--: | :----: |
| request | DelFileRequest | None | Deleting file request |

|  request Member  |   Type    | Default Value  |    Setting Method    |                    Description                    |
| :---------: | :-----: | :--: | :--------: | :--------------------------------------: |
| bucket_name | unicode |  None   | Constructor or set method |                 bucket name                 |
|  cos_path   | unicode |  None   | Constructor or set method | cos path, which must start with the root / under the bucket. File path cannot end with /. For example, /mytest/demo.txt |

#### Returned Value

| Type of Returned Value |                  Description of Returned Value                   |
| :---: | :--------------------------------------: |
| dict  | {'code':\$code,  'message':$mess}. If "code" is 0, it means success. "message" indicates SUCCESS or failure reason. For details, refer to the Returned Value module |

#### Example

```python
    request = DelFileRequest(bucket, u'/sample_file_move.txt')
    del_ret = cos_client.del_file(request)
```

## Directory-related Operations

### Creating a Directory

#### Method Prototype

```python
def create_folder(self, request)
```

#### Parameter Description

|   Parameter Name   |        Type         | Default Value  |  Description  |
| :-----: | :-----------------: | :--: | :----: |
| request | CreateFolderRequest |  None   | Creating directory request |

|  request Member  |   Type    | Default Value  |    Setting Method    |                    Description                    |
| :---------: | :-----: | :--: | :--------: | :--------------------------------------: |
| bucket_name | unicode |  None   | Constructor or set method |                 bucket name                 |
|  cos_path   | unicode |  None   | Constructor or set method | cos path, which must start with the root / under the bucket. Directory path must end with /. For example, /mytest/dir/ |
|  biz_attr   | unicode |  Null   |   set method    |            Note for directory, mainly the description of the use of the directory            |

#### Returned Value

| Type of Returned Value |                  Description of Returned Value                   |
| :---: | :--------------------------------------: |
| dict  | {'code':\$code,  'message':$mess}. If "code" is 0, it means success. "message" indicates SUCCESS or failure reason. For details, refer to the Returned Value module |

#### Example

```python
    request = CreateFolderRequest(bucket, u'/sample_folder/')
    create_folder_ret = cos_client.create_folder(request)
```

### Getting Directory Attributes

#### Method Prototype

```python
def stat_folder(self, request)
```

#### Parameter Description

|   Parameter Name   |       Type        | Default Value  |   Description   |
| :-----: | :---------------: | :--: | :------: |
| request | StatFolderRequest |  None   | Getting directory attribute request |

|  request Member  |   Type    | Default Value  |    Setting Method    |                    Description                    |
| :---------: | :-----: | :--: | :--------: | :--------------------------------------: |
| bucket_name | unicode |  None   | Constructor or set method |                 bucket name                 |
|  cos_path   | unicode |  None   | Constructor or set method | cos path, which must start with the root / under the bucket. Directory path must end with /. For example, /mytest/dir/ |

#### Returned Value

| Type of Returned Value |                  Description of Returned Value                   |
| :---: | :--------------------------------------: |
| dict  | {'code':\$code,  'message':$mess, 'data':\$data}. If "code" is 0, it means success. "message" indicates SUCCESS or failure reason. "data" contains related attributes. For details, refer to the Returned Value module |

#### Example

```python
    request = StatFolderRequest(bucket, u'/sample_folder/')
    stat_folder_ret = cos_client.stat_folder(request)
```



### Updating Directory Attributes

#### Method Prototype

```python
def update_folder(self, request)
```

#### Parameter Description

|   Parameter Name   |        Type         | Default Value  |   Description   |
| :-----: | :-----------------: | :--: | :------: |
| request | UpdateFolderRequest |  None   | Updating directory attribute request |

|  request Member  |   Type    | Default Value  |    Setting Method    |                    Description                    |
| :---------: | :-----: | :--: | :--------: | :--------------------------------------: |
| bucket_name | unicode |  None   | Constructor or set method |                 bucket name                 |
|  cos_path   | unicode |  None   | Constructor or set method | cos path, which must start with the root / under the bucket. Directory path must end with /. For example, /mytest/dir/ |
|  biz_attr   | unicode |  Null   |   set method    |            Note for directory, mainly the description of the use of the directory            |

#### Returned Value

| Type of Returned Value |                  Description of Returned Value                   |
| :---: | :--------------------------------------: |
| dict  | {'code':\$code,  'message':$mess}. If "code" is 0, it means success. "message" indicates SUCCESS or failure reason. For details, refer to the Returned Value module |

#### Example

```python
    request = UpdateFolderRequest(bucket, u'/sample_folder/')
    request.set_biz_attr(u'This is a test directory')
    update_folder_ret = cos_client.update_folder(request)
```

### Getting List of Directories

#### Method Prototype

```python
def list_folder(self, request)
```

#### Parameter Description

|   Parameter Name   |       Type        | Default Value  |   Description   |
| :-----: | :---------------: | :--: | :------: |
| request | ListFolderRequest |  None   | Getting directory member request |

|  request Member  |   Type    | Default Value  |    Setting Method    |                    Description                    |
| :---------: | :-----: | :--: | :--------: | :--------------------------------------: |
| bucket_name | unicode |  None   | Constructor or set method |                 bucket name                 |
|  cos_path   | unicode |  None   | Constructor or set method | cos path, which must start with the root / under the bucket. Directory path must end with /. For example, /mytest/dir/ |
|     num     |   int   | 199  | Constructor or set method |             Number of members in the list obtained. The maximum is 199             |
|   prefix    | unicode |  Null   | Constructor or set method | Prefix of members for search. For example, if the prefix is test, it means only searching files or directories that start with test |
|   context   | unicode |  Null   | Constructor or set method |  Transparently transmitted field, which is obtained from the response content. If you want to query the first page, an empty string should be passed as context. To turn pages, the context in the returned content of the previous page should be transparently transmitted to the parameter |

#### Returned Value

| Type of Returned Value |                  Description of Returned Value                   |
| :---: | :--------------------------------------: |
| dict  | {'code':\$code,  'message':$mess, 'data':\$data}. If "code" is 0, it means success. "message" indicates SUCCESS or failure reason. "data" contains the member list. For details, refer to the Returned Value module |

#### Example

```python
    request = ListFolderRequest(bucket, u'/sample_folder/')
    list_folder_ret = cos_client.list_folder(request)
```

### Deleting a Directory

#### Method Prototype

```python
def del_folder(self, request)
```

#### Parameter Description

|   Parameter Name   |       Type       | Default Value  |  Description  |
| :-----: | :--------------: | :--: | :----: |
| request | DelFolderRequest | None | Deleting directory request |

|  request Member  |   Type    | Default Value  |    Setting Method    |                    Description                    |
| :---------: | :-----: | :--: | :--------: | :--------------------------------------: |
| bucket_name | unicode |  None   | Constructor or set method |                 bucket name                 |
|  cos_path   | unicode |  None   | Constructor or set method | cos path, which must start with the root / under the bucket. Directory path must end with /. For example, /mytest/dir/ |

#### Returned Value

| Type of Returned Value |                  Description of Returned Value                   |
| :---: | :--------------------------------------: |
| dict  | {'code':\$code,  'message':$mess}. If "code" is 0, it means success. "message" indicates SUCCESS or failure reason. For details, refer to the Returned Value module |

#### Example

```python
    request = DelFolderRequest(bucket, u'/sample_folder/')
    delete_folder_ret = cos_client.del_folder(request)
```

## Signature Management

The signature module provides APIs for generating multiple-time signature, one-time signature, and download signature. The multiple-time signature and one-time signature are used within the apis of file-related and directory-related operations, so users do not need to care about them. The download signature is used to help users generate the signature for downloading the private bucket file.

### Multiple-time Signature

```python
def sign_more(self, bucket, cos_path, expired)
```

#### Usage Scenarios

Uploading files, renaming files, creating directories, getting file and directory attributes, and pulling lists of directories

#### Parameter Description

| Parameter Name      |  Type   | Default Value  |      Description       |
| -------- | :-----: | :--: | :-------------: |
| bucket   | unicode |  None   |    bucket name     |
| cos_path | unicode |  None   |    The cos path that needs a signature     |
| expired  |   int   |  None   | Expiration time of the signature, Unix timestamp |

#### Returned Value

String encoded with base64

#### Example

```python
cred = CredInfo(100000, u'xxxxxxx', u'xxxxxxxx') # appid, secret_id, secret_key  
auth_obj = Auth(cred)                                                           
sign_str = auth_obj.sign_more(u'mybucket', u'/pic/1.jpg',  int(time.time()) + 600)
```

### One-time Signature

```python
def sign_once(self, bucket, cos_path)
```

#### Usage Scenarios

Deleting and updating files and directories

#### Parameter Description

|   Parameter Name    |  Type   | Default Value  |   Description    |
| :------: | :-----: | :--: | :-------: |
|  bucket  | unicode |  None   | bucket name  |
| cos_path | unicode |  None   | The cos path that needs a signature |

#### Returned Value

String encoded with base64

#### Example

```python
cred = CredInfo(100000, u'xxxxxxx', u'xxxxxxxx') # appid, secret_id, secret_key  
auth_obj = Auth(cred)                                                           
sign_str = auth_obj.sign_once(u'mybucket', u'/pic/1.jpg')
```

### Download Signature

```python
def sign_download(self, bucket, cos_path, expired)
```

#### Usage Scenarios

Generating download signature of file for downloading private bucket files

#### Parameter Description

|   Parameter Name    |  Type   | Default Value  |      Description       |
| :------: | :-----: | :--: | :-------------: |
|  bucket  | unicode |  None   |    bucket name     |
| cos_path | unicode |  None   |    The cos path that needs a signature     |
| expired  |   int   |  None   | Expiration time of the signature, Unix timestamp |

#### Returned Value

String encoded with base64

#### Example

```python
cred = CredInfo(100000, u'xxxxxxx', u'xxxxxxxx') # appid, secret_id, secret_key  
auth_obj = Auth(cred)                                                           
sign_str = auth_obj.sign_download(u'mybucket', u'/pic/1.jpg',  int(time.time()) + 600)
```

## Error Codes

| Code |                  Meaning                  |
| :--: | :----------------------------------: |
|  0   |                 Operation succeeded                 |
|  -1  | Incorrect input parameter. For example, the local file path entered does not exist; cos file path does not conform to standards |
|  -2  |             Network error, such as 404              |
|  -3  |           An exception occurs while trying to connect cos, such as connection timeout           |
| -71  |           Too many attempts have been made, which triggers cos attack            |

