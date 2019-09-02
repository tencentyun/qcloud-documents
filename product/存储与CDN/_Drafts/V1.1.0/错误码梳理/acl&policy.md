## Put Bucket Acl
---
### 功能描述
#### 细节分析
1. 既可以通过头部设置，也可以通过xml body设置，建议只使用一种方法。
2. 私有bucket可以下可以给某个文件夹设置成公有，那么该文件夹下的文件都是公有；但是把文件夹设置成私有后，在该文件夹中设置的公有属性，不会生效。

### Response

#### Special Errors
在该请求下经常会发生的一些错误如下：
错误码|描述|HTTP状态码
--|--|--
InvalidDigest|用户带的Content-MD5和COS计算body的Content-MD5不一致|400 Bad Request
MalformedXM|传入的xml格式有误,请跟restful api文档仔细比对|400 Bad Request
InvalidArgument|参数错误，具体可以参考错误信息|400 Bad Request
## Put Object Acl
---
### 功能描述
#### 细节分析
1. 既可以通过头部设置，也可以通过xml body设置，建议只使用一种方法。
2. ACL策略数上限1000，建议用户不要每个上传文件都设置ACL。
3. 把文件夹设置成私有后，给该文件夹下的文件及文件夹设置公有属性，不会生效。


### Response

#### Special Errors

在该请求下经常会发生的一些错误如下：

错误码|描述|HTTP状态码
--|--|--
InvalidDigest|用户带的Content-MD5和COS计算body的Content-MD5不一致|400 Bad Request
MalformedXML|传入的xml格式有误,请跟restful api文档仔细比对|400 Bad Request
InvalidArgument|参数错误，具体可以参考错误信息|400 Bad Request
NoSuchKey|object不存在|404 Not Found


## Put Policy
---
### 功能描述
#### 细节分析
1. Sid可以不设置，默认生成，如果要设置，不能名字重复，且值不能为空。
2. Resource字段里面的region、appid、bucket，需要和请求的host匹配。



###Response

####Special Errors
在该请求下经常会发生的一些错误如下：
错误码|描述|HTTP状态码
--|--|--
InvalidDigest|用户带的Content-MD5和COS计算body的Content-MD5不一致|400 Bad Request
InvalidArgument|参数错误，具体可以参考错误信息|400 Bad Request






