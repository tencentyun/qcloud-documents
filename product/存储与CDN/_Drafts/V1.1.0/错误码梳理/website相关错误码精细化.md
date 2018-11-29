## put bucket website

### 功能描述
开启静态网站功能，用户可以配置首页IndexDocument以及错误页面ErrorDocuemnt，还可以设置条件重定向以及错误码重定向等功能，通过设置XML来配置静态网站配置。
### 细节分析

|错误码|描述|HTTP状态码|
|:--|:--|:--|
| InvalidArgument |当上传的XML配置为空时会发生错误|400 Bad Request|
| XMLSizeLimit |当上传的XML配置大小超过64KB或者RoutingRules超过1000条时|400 Bad Request|
| MalformedXML |1.当上传的XML配置的格式不正确时会返回错误 <br> 2.如果设置IndexDocument非法,会提示静态网站必须开启index的错误<br> 3.如果设置HttpErrorCodeReturnedEquals为5XX错误，会提示只允许设置4XX错误码<br> 其它不符合静态网站规则的错误详见返回的Message字段。|400 Bad Request|

## get bucket website

### 功能描述
获取当前bucket开启的静态网站配置，如果没有开启静态网站，则会返回错误。
### 细节分析
|错误码|描述|HTTP状态码|
|:--|:--|:--|
| NoSuchWebsiteConfiguration |当没有设置静态网站配置时|404 Not Found|

## delete bucket website
### 功能描述
删除当前bucket的静态网站配置，删除成功后返回204.

## ActionS3WebsiteFileGet 

### 功能描述
当用户开启了静态网站功能后，则可以通过静态网站域名来访问COS的资源，通过静态网站域名下载资源将直接在浏览器端预览，通过静态网站域名的访问只允许GET和HEAD方法，并且URL中不允许带参数，否则会返回错误。

### 细节分析
|错误码|描述|HTTP状态码|
|:--|:--|:--|
| NoSuchWebsiteConfiguration |当没有开启静态网站的情况下，试图通过静态网站域名访问资源|404 Not Found|
| MethodNotAllowed |当使用非法的Method或者URL中带参数来访问静态网站域名|405 Method Not Allowed|
| |当访问的资源命中错误码重定向或者前缀重定向时|301 Moved Permanently|
| |当访问的资源resource不存在，而resource/Index存在时|302 Moved Temporarily|

## ActionS3WebsiteObjectAttrQuery 

### 功能描述
当用户开启了静态网站功能后，则可以通过静态网站域名来访问COS的资源，通过静态网站域名访问资源的元信息，通过静态网站域名的访问只允许GET和HEAD方法，并且URL中不允许带参数，否则会返回错误。

### 细节分析

|错误码|描述|HTTP状态码|
|:--|:--|:--|
| NoSuchWebsiteConfiguration |当没有开启静态网站的情况下，试图通过静态网站域名访问资源|404 Not Found|
| MethodNotAllowed |当使用非法的Method或者URL中带参数来访问静态网站域名|405 Method Not Allowed|
| |当访问的资源命中错误码重定向或者前缀重定向时|301 Moved Permanently|
| |当访问的资源resource不存在，而resource/Index存在时|302 Moved Temporarily|

## ActionS3GetBucketObjectVersioning 

### 功能描述
当Bucket开启了版本控制之后，通过该接口可以获取当前bucket中所有的带版本信息的objects信息，访问该接口必须拥有存储桶的读权限。

### 细节分析

|错误码|描述|HTTP状态码|
|:--|:--|:--|
| NoSuchBucket |当访问的Bucket不存在 |404 Not Found|
| InvalidBucketName |当访问一个命名不规范的Bucket时|400 Bad Request|
| InvalidArgument|1.当max-keys大于1000或者小于0<br>2.当max-keys不是一个数字时|400 Bad Request|
| InvalidURI |当prefix、marker或者delimiter参数不符合长度要求（必须小于1024）|400 Bad Request|
