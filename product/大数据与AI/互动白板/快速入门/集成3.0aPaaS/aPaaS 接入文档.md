# 快速接入

## 概念介绍

**开发者(Developer)**

​        一个开发者下可创建多个应用。开发者注册成功后，会分配一对SecretID/SecretKey，用作开发者调用apaas平台接口权限的凭证。

**应用(App)**

​        开发者实际以应用维度接入及管理白板房间、用户信息等相关数据。开发者创建应用成功后，会分配一对AppID/AppSecretKey，用于用户token 的签发。

## 接入总体流程

1. 注册开发者
2. 创建应用
3. 创建房间
4.  生成进房链接
5.  设置进房角色


具体说明参考如下

## 注册开发者
接入3.0aPaaS需要先申请注册开发者，目前为人工审核开通，可直接[申请工单](https://console.cloud.tencent.com/workorder/category)开通

**申请开通模板**

- 公司名：
- 账号 ID：
- AppID：
- 联系人姓名： 
- 联系电话：
- 行业类型：
- 预计用户规模：

账号 ID 和 AppID 可以在腾讯云控制台->[账号信息](https://console.cloud.tencent.com/developer) 中查询，申请通过后会获得secretID，secretKey信息

## 创建应用

平台为开发者提供了RestAPI，创建应用可调用RestAPI中的CreateApp接口实现，API目前仅支持https调用方式，需要在请求头中需要携带鉴权信息(Authorization、X-Date)，可使用注册开发者获得的secretID、secretKey签名获得，签名方法等详细说明可参见[RestAPI](https://whiteboard.qcloudtiw.com/docs/service/index.html)

[调用地址](https://whiteboard.qcloudtiw.com/docs/service/index.html#/%E5%BA%94%E7%94%A8/CreateApp)


**请求header**

```markdown
{
   "Content-Type":  "application/json",
   "Accept": "application/json",
   "Authorization":  <auth>,
   "X-Date":        <x-date>,
}
```
**请求body**

参数名称  | 是否必选 | 类型 | 描述| 输入值
----------| ---      | ---  |----------|----------
IconUrl   |否        |string|白板房间中展示的app的logo图片地址| ""
HomeUrl   |否        |string|白板房间中点击app的logo跳转地址| ""

**请求response**

参数名称  |  类型 | 描述
----------| ---  |----------
Error    |Object|参加公共参数
RequestID       |string|唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
App |AppInfo| app信息

***AppInfo***

参数名称  |  类型 | 描述
----------| ---  |----------
AppID    |string|App唯一标识
SecretKey       |string|App密钥，用于签发接入白板房间token
DeveloperID |string| 开发者的id
IconUrl |string| app的logo图片地址
HomeUrl |string| 点击app的lgogo跳转地址



## 创建房间

[调用地址](https://whiteboard.qcloudtiw.com/docs/service/index.html#/%E6%88%BF%E9%97%B4/CreateRoom)

**请求header**

```markdown
{
   "Content-Type":  "application/json",
   "Accept": "application/json",
   "Authorization":  <auth>,
   "X-Date":        <x-date>,
}
```
**请求body**

参数名称  | 是否必选 | 类型 | 描述 | 输入值
----------| ---      | ---  |----------|----------
AppID    |是|string|App唯一标识|""
RoomID   |是        |string|创建的房间ID，需要保证APP内唯一，否则会创建失败|""
UserID   |是        |string|房间创建者的用户唯一标识ID|""
RoomTitle   |否        |string|创建房间的名称，不传则是默认名称|""

**请求response**

参数名称  |  类型 | 描述
----------| ---  |----------
Error    |Object|参加公共参数
RequestID       |string|唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
RoomID    |string|参加公共参数
RoomTitle    |string|房间名称
JumpURL       |string|房间跳转地址

## 设置进房角色

用户在进入房间时需要先设置用户的角色，以获得进房的权限，设置用户角色可调用```ModifyUserRole```接口

[调用地址](https://whiteboard.qcloudtiw.com/docs/service/index.html#/rbac/ModifyUserRole)

**请求header**


```markdown
{
   "Content-Type":  "application/json",
   "Accept": "application/json",
   "Authorization":  <auth>,
   "X-Date":        <x-date>,
}
```

**请求body**

参数名称  | 是否必选 | 类型 | 描述 | 输入值
----------| ---      | ---  |---------- |----
UserID    |是|string|用户唯一标识，指定要修改的用户id |""
Role   |是        |string|角色，角色表用户可自定义，未定义可参见[默认角色表]()|""
RoomID   |是        |string|用户所在房间id|""
AppID   |是        |string|App唯一标识|""

**请求response**

参数名称  |  类型 | 描述
----------| ---  |----------
Error    |Object|参加公共参数
RequestID       |string|唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。

## 生成进房链接

### 生成token
用户进入房间需要携带鉴权token，鉴权采用的是JWT认证方式，使用创建应用返回的AppSecretKey签发token，JWT的payload需要包含以下内容：


```markdown
{
  "exp": 1646205506, // 过期时间
  "iat": 1646119106, // 签发时间
  "aid": "请输入应用id", // APPID
  "uid": "请输入用户id" // 用户名
}
SecretKey: "请输入应用SecretKey"
```
[点击生成]()(待实现)

```markdown
token:
```
**生成token代码示例**

```markdown
func (claims AuthTokenClaims) GenToken(secretKey string) (string, error) {
	signer, err := jwt.NewSignerHS(jwt.HS256, []byte(secretKey))
	if err != nil {
		return "", errors.Wrap(err, "cannot get signer")
	}
	builder := jwt.NewBuilder(signer)
	token, err := builder.Build(claims)
	if err != nil {
		return "", errors.Wrap(err, "generate token error")
	}
	return token.String(), err
}
```

### 进房链接说明

进房链接是由创建房间接口返回的跳转链接JumpURL拼接用户id、房间id、token信息生成

创建房间接口返回的跳转链接

```markdown
JumpURL:https://whiteboard.qcloudtiw.com/app/board/index.html
```

需携带的相关参数:

```markdown
user: "请输入进房用户id"
room_id: "请输入房间id"
token: "请输入生成的token"
```

**进房链接**:

```markdown
https://whiteboard.qcloudtiw.com/app/board/index.html?room=<room_id>&user=<user>&token=<token>
```





**至此，所有接入流程已完成，可以直接跳转链接进入白板房间**