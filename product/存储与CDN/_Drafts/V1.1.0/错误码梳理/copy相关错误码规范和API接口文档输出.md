## Upload-Part Copy

1. 拷贝操作需要请求者对源object有读权限，如果没有读权限，会返回403 AccessDenied，错误信息：You have no authority to read the source file 

2. 如果在x-cos-copy-source中指定的 region不合法，会返回400 Bad Request，需要检查填写的源object或者请求的region是否符合COS的规范。

3. 如果对源object被封禁或者其它原因无法查询其属性，则会返回400-Base 错误码,具体的错误信息请参考API的响应体的Message字段。

4. 如果请求的前置条件不匹配，则会返回412 PreconditionFailed错误码，错误信息：PreconditionFailed， 需要检查前置条件是否满足需求

5. 如果x-cos-copy-source 格式不合法，会返回400 Bad Request，x-cos-copy-source 的参考格式如下

   ```x-cos-copy-source: bucekt-appid.cos.ap-shanghai.myqcloud.com/path/to/file```

6. 如果 x-cos-copy-source-range 格式不合法，会返回400 Bad Request，x-cos-copy-source-range 的参考格式如下

    ```x-cos-copy-source-range: bytes=1-10```

如若请求返回遇到其他公共错误码，请参见[通用错误码列表]()

## AppendObject
1. 如果对一个非appendable的文件进行append操作，那么会返回409 Confilct，错误信息：
The operation is not valid for the current state of the object.

2. 如果请求中未携带position参数，会返回400 Bad Request, 错误信息：InvalidArgument

3. 如果请求中缺失Content-Length头部，会返回411 Length Required，错误信息：
You must provide the Content-Length HTTP header.

如若请求返回遇到其他公共错误码，请参见[通用错误码列表]()


## Upload Copy

1. 拷贝操作需要请求者对源object有读权限，如果没有读权限，会返回403 AccessDenied.

2. 如果在x-cos-copy-source中指定的 region不合法，会返回400 Bad Request，错误信息：InvalidArgument。需要检查填写的源object或者请求的region是否符合COS的规范。

3. 如果源object被封禁或者其它原因无法查询其属性，则会返回400-Base的错误码，错误信息：Failed to query the state of source object

4. 如果请求的前置条件不匹配，则会返回412 PreconditionFailed错误码，错误信息：PreconditionFailed， 需要检查前置条件是否满足需求

5. 如果x-cos-copy-source 格式不合法，会返回400 Bad Request，错误信息：InvalidArgument, x-cos-copy-source 的参考格式如下

   ```x-cos-copy-source: bucekt-appid.cos.ap-shanghai.myqcloud.com/path/to/file```
   
   如若请求返回遇到其他公共错误码，请参见[通用错误码列表]()



## AbortUploadPart

 当请求中指定的UploadId不存在时，返回404 Not Found，对应的错误码NoSuchUpload。

 如若请求返回遇到其他公共错误码，请参见[通用错误码列表]()

## PostObject

1. 如果Post的表单不符合表单格式，会返回400 Bad Request，错误信息：
 The body of your request is not well-formed multipart/form-data

2. 如果Post表单里面的条件不匹配，如时间过期、条件表达式不匹配都会返回403 Forbidden。具体的错误信息
可以参考接口返回的Message字段。

如若请求返回遇到其他公共错误码，请参见[通用错误码列表]()
