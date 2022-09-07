## API 概览
|接口名称         | 接口功能|
|-------------    | -------------|
|[CreateApp](#CreateApp)        | 开发者创建自己的一个 App，接入白板房间是以 App 为维度区分|
|[DescribeAppList](#DescribeAppList)  | 查询所创建的App信息列表|
|[ModifyApp](#ModifyApp)      | 修改 App 的信息|
|[CreateRoom](#CreateRoom)     | 创建房间，一个房间对应一个白板|
|[DescribeRooms](#DescribeRooms)    | 查询指定房间信息列表|
|[ModifyRoom](#ModifyRoom)       | 修改房间信息|
|[DeleteRoom](#DeleteRoom)       | 删除房间|
|[ModifyUserRole](#ModifyUserRole)   | 修改房间中用户的角色|
|[ModifyRole](#ModifyRole)       | 修改角色对应的权限范围|

## 接口鉴权方式
所有接口仅支持 HTTPS 方式调用。请求需用 SecretKey 进行签名，并携带以下请求头：
**请求头 header 参数**

|参数名称  |  类型 | 描述|
|----------| ---  |----------|
|Content-Type    |string|内容格式 application/json|
|Accept    |string|Accept 格式 application/json|
|Authorization       |string|签名校验信息|
|X-Date       |string|GMT 格式的时间戳|


>? `auth` 替换为签名后的内容。

### 签名示例

```go
func GetSignedHeader(path string) http.Header {
   secretID := "xxx"
   secretKey := "xxx"
   requestLine := fmt.Sprintf("POST %s HTTP/1.1", path)
   //获取当前GMT格式的时间戳
   xDate := time.Now().UTC().Format(http.TimeFormat)

   //拼接用于生成加密签名的字符串
   signingString := fmt.Sprintf("%s\nx-date: %s", requestLine, xDate)

   //生成签名串
   h := hmac.New(sha256.New, []byte(secretKey))
   h.Write([]byte(signingString))
   base64Digest := base64.StdEncoding.EncodeToString(h.Sum(nil))

   //组装Authorization header
   auth := fmt.Sprintf(
      `hmac username="%s", algorithm="hmac-sha256", headers="request-line x-date", signature="%s"`,
      secretID, base64Digest,
   )
   return http.Header{
      "Content-Type":  []string{"application/json"},
      "Authorization": []string{auth},
      "Accept":        []string{"application/json"},
      "X-Date":        []string{xDate},
   }
}
```
入参 path 为接口 route，如：/xxx/xxx。
secreateID/secretKey 为开发者注册成功后获得的密钥对。

### header 示例
```markdown
{
   "Content-Type":  "application/json",
   "Accept": "application/json",
   "Authorization":  "<auth>",
   "X-Date":        "<x-date>",
}
```

## <a id="CreateApp"></a>创建 App
### 接口描述
接口请求域名： coop-public.qcloudtiw.com
请求路径: /trpc.tiwdeveloper.main/CreateApp
在申请为开发者后，使用接入指引中的调用方式创建自己的一个的 App，供后续接入白板房间使用。
### 输入参数
以下请求参数列表仅列出了接口请求参数，其他公共参数请参见 [公共请求参数](#CommonSign)。

|参数名称  | 是否必选 | 类型 | 描述|
|----------| ---      | ---  |----------|
|IconUrl   |否        |string|白板房间中展示的 App 的 logo 图片地址|
|HomeUrl   |否        |string|白板房间中点击 App 的 logo 跳转地址|

### 输出参数

|参数名称  |  类型 | 描述|
|----------| ---  |----------|
|Error    |Object|参见 [公共参数](#CommonSign)|
|RequestID       |string|唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId|
|App |AppInfo| App 信息|

**AppInfo**

|参数名称  |  类型 | 描述|
|----------| ---  |----------|
|AppID    |string| App 唯一标识|
|SecretKey       |string|App 密钥，用于签发接入白板房间 token|
|DeveloperID |string| 开发者的 ID|
|IconUrl |string| App 的 logo 图片地址|
|HomeUrl |string| 点击 App 的 logo 跳转地址|

## <a id="DescribeAppList"></a>查询 App 列表
### 接口描述
接口请求域名： coop-public.qcloudtiw.com
请求路径: /trpc.tiwdeveloper.main/DescribeAppList
开发者可使用该接口查询自己创建的所有 App 列表。
### 输入参数
以下请求参数列表仅列出了接口请求参数，其他公共参数请参见 [公共请求参数](#CommonSign)。

参数名称  | 是否必选 | 类型 | 描述
----------| ---      | ---  |----------
Offset   |是        |int64|查询 App 在列表中的便宜位置，0为第一个
Limit   |是       |int64|分页拉取，一页返回 App 个数

### 输出参数

参数名称  |  类型 | 描述
----------| ---  |----------
Error    |Object|参见 [公共参数](#CommonSign)
RequestID       |string|唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId
App |AppInfo| App 信息

**AppInfo**

参数名称  |  类型 | 描述
----------| ---  |----------
AppID    |string|App 唯一标识
DeveloperID |string| 开发者的 ID
IconUrl |string| App 的 logo 图片地址
HomeUrl |string| 点击 App 的 logo 跳转地址

## <a id="ModifyApp"></a>修改 App 信息
###  接口描述
接口请求域名： coop-public.qcloudtiw.com
请求路径: /trpc.tiwdeveloper.main/ModifyApp
该接口可用于修改 App 的 logo 地址，跳转地址。
### 输入参数
以下请求参数列表仅列出了接口请求参数，其他公共参数请参见 [公共请求参数](#CommonSign)。

参数名称  | 是否必选 | 类型 | 描述
----------| ---      | ---  |----------
AppID    |是|string|修改的 App 唯一标识
IconUrl   |否        |string|白板房间中展示的 App 的 logo 图片地址
HomeUrl   |否        |string|白板房间中点击 App 的 logo 跳转地址

### 输出参数

参数名称  |  类型 | 描述
----------| ---  |----------
Error    |Object|参见 [公共参数](#CommonSign)
RequestID       |string|唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId


## <a id="CreateRoom"></a>创建房间
### 接口描述
接口请求域名： coop-public.qcloudtiw.com
请求路径: /trpc.tiwdeveloper.main/CreateRoom
在进入白板房间前需要先创建房间，不存在的房间无法进入，创建成功会返回房间的跳转地址拼上 room、user、token 就可以正常跳转到房间页。
### 输入参数
以下请求参数列表仅列出了接口请求参数，其他公共参数请参见 [公共请求参数](#CommonSign)。

参数名称  | 是否必选 | 类型 | 描述
----------| ---      | ---  |----------
AppID    |是|string|App 唯一标识
RoomID   |是        |string|创建的房间 ID，需要保证 APP 内唯一，否则会创建失败
UserID   |是        |string|房间创建者的用户唯一标识 ID
RoomTitle   |否        |string|创建房间的名称，不传则是默认名称

### 输出参数

参数名称  |  类型 | 描述
----------| ---  |----------
Error    |Object|参见 [公共参数](#CommonSign)
RequestID       |string|唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId
RoomID    |string|参加公共参数
RoomTitle    |string|房间名称
JumpURL       |string|房间跳转地址

## <a id="DescribeRooms"></a>查询指定房间列表
### 接口描述
接口请求域名： coop-public.qcloudtiw.com
请求路径: /trpc.tiwdeveloper.main/DescribeRooms
用户批量获取房间信息，给定多个房间 ID，返回房间信息列表。
### 输入参数
以下请求参数列表仅列出了接口请求参数，其他公共参数请参见 [公共请求参数](#CommonSign)。

参数名称  | 是否必选 | 类型 | 描述
----------| ---      | ---  |----------
AppID    |是|string|App 唯一标识
RoomList   |是        |Array string|房间 ID 数组


### 输出参数

参数名称  |  类型 | 描述
----------| ---  |----------
Error    |Object|参见 [公共参数](#CommonSign)
RequestID       |string|唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId
Rooms    |Array DevRoomInfo|房间信息数组

**DevRoomInfo**

参数名称  |  类型 | 描述
----------| ---  |----------
RoomID    |string|房间 ID
RoomTitle       |string|房间名称
JumpURL    |string|房间跳转地址

## <a id="ModifyRoom"></a>修改房间信息
### 接口描述
接口请求域名： coop-public.qcloudtiw.com
请求路径: /trpc.tiwdeveloper.main/ModifyRoom
可用于修改指定房间的信息，房间的名称等。
### 输入参数 
以下请求参数列表仅列出了接口请求参数，其他公共参数请参见 [公共请求参数](#CommonSign)。

参数名称  | 是否必选 | 类型 | 描述
----------| ---      | ---  |----------
AppID    |是|string|App 唯一标识
RoomID   |是        |string|房间 ID
RoomTitle   |是        |string|房间名称


### 输出参数

参数名称  |  类型 | 描述
----------| ---  |----------
Error    |Object|参见 [公共参数](#CommonSign)
RequestID       |string|唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId

## <a id="DeleteRoom"></a>删除房间
### 接口描述
接口请求域名： coop-public.qcloudtiw.com
请求路径: /trpc.tiwdeveloper.main/DeleteRoom
删除指定的房间，删除接口会将房间的所以信息删除，请谨慎使用。

### 输入参数
以下请求参数列表仅列出了接口请求参数，其他公共参数参见 [公共请求参数](#CommonSign)。

参数名称  | 是否必选 | 类型 | 描述
----------| ---      | ---  |----------
AppID    |是|string|App 唯一标识
RoomID   |是        |string|房间 ID


### 输出参数

参数名称  |  类型 | 描述
----------| ---  |----------
Error    |Object|参见 [公共参数](#CommonSign)
RequestID       |string|唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId

## <a id="ModifyUserRole"></a>修改房间内用户的角色
### 接口描述
接口请求域名： coop-public.qcloudtiw.com
请求路径: /trpc.tiwdeveloper.main/ModifyUserRole
对房间内的用户可修改其角色来改变用户对该房间的权限。

### 输入参数
以下请求参数列表仅列出了接口请求参数，其他公共参数参见 [公共请求参数](#CommonSign)。

参数名称  | 是否必选 | 类型 | 描述
----------| ---      | ---  |----------
UserID    |是|string|用户唯一标识，指定要修改的用户 ID
Role   |是        |string|角色，由用户自定义
RoomID   |是        |string|用户所在房间 ID
AppID   |是        |string|App 唯一标识


### 输出参数

参数名称  |  类型 | 描述
----------| ---  |----------
Error    |Object|参见 [公共参数](#CommonSign)
RequestID       |string|唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId

## <a id="ModifyRole"></a>修改角色对应的权限
### 接口描述
接口请求域名： coop-public.qcloudtiw.com
请求路径: /trpc.tiwdeveloper.main/ModifyRole
对房间内的用户可修改其角色来改变用户对该房间的权限。
### 输入参数
以下请求参数列表仅列出了接口请求参数，其他公共参数参见 [公共请求参数](#CommonSign)。

参数名称  | 是否必选 | 类型 | 描述
----------| ---      | ---  |----------
AppID    |是|string|App 唯一标识
Role   |是        |string|角色
Permission   |是        |int64|权限范围，权限说明参见 [公共参数](#CommonSign)。


### 输出参数

参数名称  |  类型 | 描述
----------| ---  |----------
Error    |Object|参见 [公共参数](#CommonSign)
RequestID       |string|唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId

## 公共参数 [](id:CommonSign)
**Error**

参数名称  |  类型 | 描述
----------| ---  |----------
Code    |string|错误码，OK 为成功，其他值为错误
Message       |string|错误信息

**请求头 header 参数**

参数名称  |  类型 | 描述
----------| ---  |----------
Content-Type    |string|内容格式 application/json
Authorization       |string|签名校验信息
X-Date       |string|GMT 格式的时间戳

**权限说明**

名称  |  值 | 描述
----------| ---  |----------
select    |1|可读权限
modify      |2|可写权限
delete       |4|删除权限
create       |8|创建权限

以上权限可搭配使用，例如给定某个角色拥有可读可写权限则 role 对应的 permission 值为1+2=3。
