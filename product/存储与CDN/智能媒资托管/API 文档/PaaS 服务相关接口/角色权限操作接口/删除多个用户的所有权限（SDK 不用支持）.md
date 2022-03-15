#### 删除多个用户的所有权限（SDK 不用支持）

##### 功能描述

用于删除多个用户的所有权限

##### 请求

###### 请求示例

DELETE /api/v1/authority/`{LibraryId}`/user-authority?user_id_list=`{UserId1,UserId2,UserId3}`&access_token=`{AccessToken}`

- 请求参数：
  - LibraryId: 媒体库 ID，必选参数；
  - UserId1: 用户 ID，必填参数；
  - AccessToken: 访问令牌，必选参数；

###### 请求体

空

##### 响应

###### 响应码

删除成功，返回 HTTP 200 OK

###### 响应体

无
