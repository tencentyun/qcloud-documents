## 基本概念
### 标识符说明

| 标识符 | 说明 |
|---------|---------|
| id | 跟您帐号关联的id, 用于标识您接入的人脸识别的项目；您可以用它来区分帐号内不同的项目 |
| user_id | 业务自行定义的用户标识，标识一个唯一用户 |
| secret_id | 标识api鉴权调用者的密钥身份 |
| secret_key | 用于加密签名字符串和服务器端验证签名字符串的密钥，secret_key 必须严格保管避免泄露 |
| group_id | 个体(person)以组（group）的形式存储，一个组可以包含多个个体，一个个体也可以存在于多个组。group_id即用来标识group |
| person_id | 人脸以个体（person）的形式存储，一个个体下可以存储多张人脸。person_id即用来标识person |
| face_id | 标识每张人脸的id |
### 协议参数说明
1) 接入服务中传递的图片数据采用base64编码。
2) 一个id下建立的group_id数量限制为5000个。
3) 一个group_id下建立的person_id数量限制为1000个。
4) 一个person_id下建立的人脸数量限制为100个。
5) 每个请求的包体大小限制为2m。

## 鉴权
详见[鉴权签名文档](http://cloud.tencent.com/doc/product/277/%E7%AD%BE%E5%90%8D%E9%89%B4%E6%9D%83)

## 接口列表

| 名称 | API |
|---------|---------|
| 人脸检测 | /youtu/api/detectface |
| 五官定位 | /youtu/api/faceshape |
| 人脸比对 | /youtu/api/facecompare |
| 人脸验证 | /youtu/api/faceverify |
| 人脸识别 | /youtu/api/faceidentify |
| 个体创建 | /youtu/api/newperson |
| 删除个体 | /youtu/api/delperson |
| 增加人脸 | /youtu/api/addface |
| 删除人脸 | /youtu/api/delface |
| 设置信息 | /youtu/api/setinfo |
| 获取信息 | /youtu/api/getinfo |
| 获取组列表 | /youtu/api/getgroupids |
| 获取人列表 | /youtu/api/getpersonids |
| 获取脸列表 | /youtu/api/getfaceids |
| 获取脸信息 | /youtu/api/getfaceinfo |
| 身份证OCR | /youtu/api/idcardocr |

## 人脸检测与分析
### 人脸检测
1) 接口

```
https://youtu.api.qcloud.com/youtu/api/detectface
```
2) 描述：
检测给定图片(Image)中的所有人脸(Face)的位置和相应的面部属性。位置包括(x, y,w, h)，面部属性包括性别(gender), 年龄(age), 表情(expression), 眼镜(glass)和姿态(pitch，roll，yaw)。

3) 请使用POST方式调用

4) HTTP请求格式
#### 头部信息

| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| Host | 是 | String | 图片云服务器域名，固定为youtu.api.qcloud.com |
| ContentLength | 是 | Int | 整个请求包体内容的总长度，单位：字节（Byte） |
| ContentType | 是 | String | text/json表示json格式 |
| Signature | 是 | String | 多次有效签名,用于鉴权， 具体生成方式详见[鉴权签名文档](http://cloud.tencent.com/doc/product/277/%E7%AD%BE%E5%90%8D%E9%89%B4%E6%9D%83) |
#### 请求包体
| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| id | 是 | String | App的 API ID |
| image | 是 | String(Bytes) | 使用base64编码的二进制图片数据 |
| mode | 否 | Int | 检测模式 0/1 正常/大脸模式，大脸模式只检测最大的一张脸 |
| datatype | 否 | Int | 图片数据类型，url/二进制数据，目前只支持二进制数据 |

5) 请求示例

```
{
"id":"123456",
"image":"SALDKHKAFLASD"
}
```
6) 返回值

| 字段 | 类型 | 说明 |
|---------|---------|---------|
|session_id|string|相应请求的session标识符，可用于结果查询|
|image_width|int32|请求图片的宽度|
|image_height|int32|请求图片的高度|
|face|Array(FaceItem)|被检测出的人脸FaceItem的列表,FaceItem为存储人脸属性的Object|
|face_id|string|人脸标识|
|x|object|人脸框左上角x|
|y|object|人脸框左上角y|
|width|object|人脸框宽度|
|height|object|人脸框高度|
|gender|object|性别 [0/(female)~100(male)]|
|age|object|年龄 [0~100]|
|expression|object|微笑[0(normal)~50(smile)~100(laugh)]|
|glass|object|是否有眼镜 [true,false]|
|pitch|int32|上下偏移[30,30]|
|yaw|int32|左右偏移[30,30]|
|roll|int32|平面旋转[180,180]|
|errorcode|int|返回状态值|
|errormsg|String|返回错误消息|

7) 返回示例

```
{
"session_id":"xxxx",
"image_height":584,
"image_width":527,
"face":[
    {
        "face_id":"1001344647426015231",
        "x":145,
        "y":147,
        "height":305.0,
        "width":305.0,
        "pitch":3,
        "roll":0,
        "yaw":0,
        "age":34,
        "gender":99,
        "glass":true,
        "expression":27
     }
],
"errorcode":0,
"errormsg":"ok"
}
```

### 人脸比对
1) 接口
```
https://youtu.api.qcloud.com/youtu/api/facecompare
```
2) 描述
计算两个Face的相似性以及五官相似度。
3) 使用POST方式调用
4) HTTP请求格式
#### 头部信息
| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| Host | 是 | String | 图片云服务器域名，固定为youtu.api.qcloud.com |
| ContentLength | 是 | Int | 整个请求包体内容的总长度，单位：字节（Byte） |
| ContentType | 是 | String | text/json表示json格式 |
| Signature | 是 | String | 多次有效签名,用于鉴权， 具体生成方式详见[鉴权签名文档](http://cloud.tencent.com/doc/product/277/%E7%AD%BE%E5%90%8D%E9%89%B4%E6%9D%83) |

#### 请求包体
|字段|	类型	|说明|
|---------|---------|---------|
|id	|String	|App的 API ID|
|imageA|	String	|使用base64编码的二进制图片数据A|
|imageB	|String	|使用base64编码的二进制图片数据B|

#### 请求示例

```
{
     "id":"123456",
     "imageA":"ASLKDJFKLASD",
     "imageB":"ASLKDJFKLASD"
}
```

5) 返回值

|字段|	类型	|说明|
|---------|---------|---------|
|session_id|	int	|相应请求的session标识符，保留|
|similarity|	float|	两个face的相似性|
|errorcode|	int	|返回状态码|
|errormsg	|String	|返回错误消息|
|eyebrow_sim|	float	|眉毛相似度|
|eye_sim|	float	|眼睛相似度|
|nose_sim|	float	|鼻子相似度|
|mouth_sim|	float	|嘴巴相似度|

6) 返回示例

```
{
     "session_id":"sessionid",
     "eye_sim":50.5024,
     "mouth_sim":50.5024,
     "nose_sim":50.5024,
     "eyebrow_sim":50.5024,
     "similarity":50.5024,
     "errorcode":0,
     "errormsg":"ok"
}
```

### 人脸验证
1) 接口
```
https://youtu.api.qcloud.com/youtu/api/faceverify
```
2) 描述
给定一个Face和一个Person，返回是否是同一个人的判断以及置信度。
3) 使用POST方式调用
4) HTTP请求格式
#### 头部信息
| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| Host | 是 | String | 图片云服务器域名，固定为youtu.api.qcloud.com |
| ContentLength | 是 | Int | 整个请求包体内容的总长度，单位：字节（Byte） |
| ContentType | 是 | String | text/json表示json格式 |
| Signature | 是 | String | 多次有效签名,用于鉴权， 具体生成方式详见[鉴权签名文档](http://cloud.tencent.com/doc/product/277/%E7%AD%BE%E5%90%8D%E9%89%B4%E6%9D%83) |

#### 请求包体
|字段	|类型	|说明|
|---------|---------|---------|
|id	|String	|App的 API ID|
|image	|String	|使用base64编码的二进制图片数据|
|person_id|	String	|待验证的Person ID|

#### 请求示例

```
{
     "id":"123456",
     "person_id":"person0",
     "image":"ASLDGJKALSJDKG"
}
```

5) 返回值

|字段	|类型	|说明|
|---------|---------|---------|
|ismatch	|bool	|两个输入是否为同一人的判断|
|confidence|	float	|系统对这个判断的置信度|
|session_id|	string	|相应请求的session标识符，保留|
|errorcode|	int	|返回状态码|
|errormsg|	String	|返回错误消息|

6) 示例

```
{
     "confidence":50.502410888671878,
     "ismatch":false,
     "session_id":"xxxx",
     "errorcode":0,
     "errormsg":"ok"
}
```

### 个体创建
1) 接口

```
https://youtu.api.qcloud.com/youtu/api/newperson
```
2) 描述
创建一个Person，并将Person放置到group_ids指定的组当中。
3) 请使用 POST方式调用
4) HTTP请求格式
#### 头部信息
| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| Host | 是 | String | 图片云服务器域名，固定为youtu.api.qcloud.com |
| ContentLength | 是 | Int | 整个请求包体内容的总长度，单位：字节（Byte） |
| ContentType | 是 | String | text/json表示json格式 |
| Signature | 是 | String | 多次有效签名,用于鉴权， 具体生成方式详见[鉴权签名文档](http://cloud.tencent.com/doc/product/277/%E7%AD%BE%E5%90%8D%E9%89%B4%E6%9D%83) |

#### 请求包体
|参数名| 必选	|类型	|参数说明|
|---------|---------|---------|---------|
|id|是|	String	|App的 API ID|
|image|是|	String(Bytes)	|使用base64编码的二进制图片数据|
|group_ids|是|	Array(string)|	指定将个体加入到哪些组（注：指定的组会根据group_id自动创建，无须开发者手动创建）|
|person_id	|是|String	|指定的个体id|
|person_name|否|	String	|个体名称|
|tag|否|	String	|备注信息|

#### 请求示例

```
{
     "id":"123456",
     "person_id":"person7",
     "person_name":"johnson",
     "image":"ASLFKJAKLSJFLASF",
     "group_ids":["tencent"],
     "tag":"person tag"
}
```

5) 返回值

|字段|	类型	|说明|
|---------|---------|---------|
|suc_group|	int	|成功被加入的group数量|
|suc_face|	int	|成功加入的face数量|
|errorcode|	int|	返回码|
|person_id|	String|	相应person的id|
|face_id	|String	|创建所用图片生成的face_id|
|group_ids|	Array(String)	|加入成功的组id|
|加入成功的组id|	String	|相应请求的session标识符，保留返回错误消息|
|errormsg|	String	|返回错误消息|

6) 返回示例

```
{
"person_id":"person0",
"suc_group":1,
"suc_face":1,
"errorcode":0,
"session_id":"session_id",
"face_id":"1009550071676600319",
"group_ids":["tencent"],
"errormsg":"ok"
}
```

### 删除个体
1) 接口

```
https://youtu.api.qcloud.com/youtu/api/delperson
```

2) 描述
删除一个Person
3) 请使用POST方式调用
4) HTTP请求格式
#### 头部信息
| 参数名称 | 必选 | 类型 | 描述 |
|---------|---------|---------|---------|
| Host | 是 | String | 图片云服务器域名，固定为youtu.api.qcloud.com |
| ContentLength | 是 | Int | 整个请求包体内容的总长度，单位：字节（Byte） |
| ContentType | 是 | String | text/json表示json格式 |
| Signature | 是 | String | 多次有效签名,用于鉴权， 具体生成方式详见[鉴权签名文档](http://cloud.tencent.com/doc/product/277/%E7%AD%BE%E5%90%8D%E9%89%B4%E6%9D%83) |

#### 请求包体
|参数名|	类型	|参数说明|
|---------|---------|---------|
|id	|String	|App的 API ID|
|person_id|	String	|待删除个体ID|

#### 请求示例

```
{
“id”:”123456”,
“person_id”:”person3”
}
```

5) 返回值说明

|字段|	类型	|说明|
|---------|---------|---------|
|deleted|	int	|成功删除的Person数量|
|person_id|	String	|成功删除的person_id|
|errorcode|	int	|返回状态码|
|session_id|	String|	相应请求的session标识符，保留|
|errormsg|	String	|返回错误消息|

#### 返回示例

```
{
     "deleted":1,
     "person_id": "person0",
     "errorcode":0,
     "session_id":"session_id",
     "errormsg":"ok"
}
```
### 增加人脸
1)接口
```
https://youtu.api.qcloud.com/youtu/api/addface
```
2)描述
>将一组Face加入到一个Person中。注意，一个Face只能被加入到一个Person中。
一个Person最多允许包含100个Face。


3)请使用 POST方式调用

4)HTTP请求格式

**头部信息**
<table class="t">
<tbody><tr>
<th width="80"><b>参数名称</b>
</th><th width="50"><b>必选</b>
</th><th width="50"><b>类型</b>
</th><th width="150"><b>描述</b>
</th></tr>
<tr>
<td> Host
</td><td> 是
</td><td> String
</td><td> 图片云服务器域名，固定为youtu.api.qcloud.com
</td></tr>
<tr>
<td> Content-Length
</td><td> 是
</td><td> Int
</td><td> 整个请求包体内容的总长度，单位：字节（Byte）
</td></tr>
<tr>
<td> Content-Type
</td><td> 是
</td><td> String
</td><td> text/json表示json格式
</td></tr>
<tr>
<td> Signature
</td><td> 是
</td><td> String
</td><td> 多次有效签名,用于鉴权， 具体生成方式详见<a href="http://imgcache.qq.com/qcloud/tianyan/wiki/Authorization.pdf" target="_blank" rel="nofollow">鉴权签名文档</a>
</td></tr></tbody></table>

**请求包体**
<table class="t">
<tbody><tr>
<th width="80"><br>
</th><th width="80"><b>参数名</b>
</th><th width="100"><b>类型</b>
</th><th width="150"><b>参数说明</b>
</th></tr>
<tr>
<td> 必须
</td><td> id
</td><td> String
</td><td> App的 API ID
</td></tr>
<tr>
<td> <br>
</td><td> person_id
</td><td> String
</td><td> 待增加人脸的个体id
</td></tr>
<tr>
<td> <br>
</td><td> images
</td><td> Bytes
</td><td> 增加的人脸图片列表
</td></tr>
<tr>
<td> 可选
</td><td> tag
</td><td> String
</td><td> 备注信息
</td></tr></tbody></table>

**示例**
```
{
	"id":"123456",
	"person_id":"person0",
	"images":["AASFLJASLJFASFA"],
	"tag":"face tag"
}
```

5)返回值说明
<table class="t">
<tbody><tr>
<th width="80"><b>字段</b>
</th><th width="100"><b>类型</b>
</th><th width="150"><b>说明</b>
</th></tr>
<tr>
<td> added
</td><td> int
</td><td> 成功加入的face数量
</td></tr>
<tr>
<td> errorcode
</td><td> int
</td><td> 返回状态码
</td></tr>
<tr>
<td> face_ids
</td><td> Array(String)
</td><td> 增加的人脸ID，顺序与请求的images一致，若某张图片中检测人脸失败，则对应位置face_id为空值(占位)
</td></tr>
<tr>
<td> session_id
</td><td> String
</td><td> 相应请求的session标识符，保留
</td></tr>
<tr>
<td> errormsg
</td><td> String
</td><td> 返回错误消息
</td></tr></tbody></table>

**示例**
```
{
"added":1,
"face_ids":["1001331646826348543"],
"errorcode":0,
"session_id":"session_id",
"errormsg":"ok"
}
```

### 删除人脸
1)接口
```
https://youtu.api.qcloud.com/youtu/api/delface
```
2)描述
>删除一个person下的face，包括特征，属性和face_id

3)请使用 POST方式调用

4)HTTP请求格式

**头部信息**
<table class="t">
<tbody><tr>
<th width="80"><b>参数名称</b>
</th><th width="50"><b>必选</b>
</th><th width="50"><b>类型</b>
</th><th width="150"><b>描述</b>
</th></tr>
<tr>
<td> Host
</td><td> 是
</td><td> String
</td><td> 图片云服务器域名，固定为youtu.api.qcloud.com
</td></tr>
<tr>
<td> Content-Length
</td><td> 是
</td><td> Int
</td><td> 整个请求包体内容的总长度，单位：字节（Byte）
</td></tr>
<tr>
<td> Content-Type
</td><td> 是
</td><td> String
</td><td> text/json表示json格式
</td></tr>
<tr>
<td> Signature
</td><td> 是
</td><td> String
</td><td> 多次有效签名,用于鉴权， 具体生成方式详见<a href="http://imgcache.qq.com/qcloud/tianyan/wiki/Authorization.pdf" target="_blank" rel="nofollow">鉴权签名文档</a>
</td></tr></tbody></table>

**请求包体**
<table class="t">
<tbody><tr>
<th width="80"><br>
</th><th width="80"><b>参数名</b>
</th><th width="100"><b>类型</b>
</th><th width="150"><b>参数说明</b>
</th></tr>
<tr>
<td> 必须
</td><td> id
</td><td> String
</td><td> App的 API ID
</td></tr>
<tr>
<td> <br>
</td><td> person_id
</td><td> String
</td><td> 待删除人脸的person ID
</td></tr>
<tr>
<td> <br>
</td><td> face_ids
</td><td> Array(String)
</td><td> 删除人脸id列表
</td></tr></tbody></table>

**示例**
```
{
	"id":"123456",
	"person_id":"person0",
	"face_ids":["1006991173632458751"]
}
```

### 设置信息
1)接口
```
https://youtu.api.qcloud.com/youtu/api/setinfo
```
2)描述
>设置Person的name

3)请使用POST方式调用

4)HTTP请求格式

**头部信息**
<table class="t">
<tbody><tr>
<th width="80"><b>参数名称</b>
</th><th width="50"><b>必选</b>
</th><th width="50"><b>类型</b>
</th><th width="150"><b>描述</b>
</th></tr>
<tr>
<td> Host
</td><td> 是
</td><td> String
</td><td> 图片云服务器域名，固定为youtu.api.qcloud.com
</td></tr>
<tr>
<td> Content-Length
</td><td> 是
</td><td> Int
</td><td> 整个请求包体内容的总长度，单位：字节（Byte）
</td></tr>
<tr>
<td> Content-Type
</td><td> 是
</td><td> String
</td><td> text/json表示json格式
</td></tr>
<tr>
<td> Signature
</td><td> 是
</td><td> String
</td><td> 多次有效签名,用于鉴权， 具体生成方式详见<a href="http://imgcache.qq.com/qcloud/tianyan/wiki/Authorization.pdf" target="_blank" rel="nofollow">鉴权签名文档</a>
</td></tr></tbody></table>

**请求包体**
<table class="t">
<tbody><tr>
<th width="80"><br>
</th><th width="80"><b>参数名</b>
</th><th width="100"><b>类型</b>
</th><th width="150"><b>参数说明</b>
</th></tr>
<tr>
<td> 必须
</td><td> id
</td><td> String
</td><td> App的 API ID
</td></tr>
<tr>
<td> <br>
</td><td> person_id
</td><td> String
</td><td> 待设置个体ID
</td></tr>
<tr>
<td> 可选
</td><td> person_name
</td><td> String
</td><td> 个体姓名
</td></tr>
<tr>
<td> <br>
</td><td> tag
</td><td> String
</td><td> 备注信息
</td></tr></tbody></table>

**示例**
```
{
	"id":"123456",
	"person_id":"person0",
	"person_name":"johnson",
	"tag":"person tag"	
}
```

5)返回值说明

<table class="t">
<tbody><tr>
<th width="80"><b>字段</b>
</th><th width="100"><b>类型</b>
</th><th width="150"><b>说明</b>
</th></tr>
<tr>
<td> errorcode
</td><td> int
</td><td> 返回状态码
</td></tr>
<tr>
<td> session_id
</td><td> string
</td><td> 相应请求的session标识符，保留
</td></tr>
<tr>
<td> person_id
</td><td> string
</td><td> 相应person的id
</td></tr>
<tr>
<td> errormsg
</td><td> String
</td><td> 返回错误消息
</td></tr></tbody></table>

**示例**
```
{
    "person_id": "9eb44387923528f97f8545d8bef906db", 
    "errorcode": 0, 
	"session_id": "session_id",
	"errormsg":"ok"
}
```

### 获取信息
1)接口
```
https://youtu.api.qcloud.com/youtu/api/getinfo
```
2)描述
>获取一个Person的信息, 包括name, id, tag, 相关的face, 以及groups等信息

3)请使用 POST方式调用

4)HTTP请求格式

**头部信息**
<table class="t">
<tbody><tr>
<th width="80"><b>参数名称</b>
</th><th width="50"><b>必选</b>
</th><th width="50"><b>类型</b>
</th><th width="150"><b>描述</b>
</th></tr>
<tr>
<td> Host
</td><td> 是
</td><td> String
</td><td> 图片云服务器域名，固定为youtu.api.qcloud.com
</td></tr>
<tr>
<td> Content-Length
</td><td> 是
</td><td> Int
</td><td> 整个请求包体内容的总长度，单位：字节（Byte）
</td></tr>
<tr>
<td> Content-Type
</td><td> 是
</td><td> String
</td><td> text/json表示json格式
</td></tr>
<tr>
<td> Signature
</td><td> 是
</td><td> String
</td><td> 多次有效签名,用于鉴权， 具体生成方式详见<a href="http://imgcache.qq.com/qcloud/tianyan/wiki/Authorization.pdf" target="_blank" rel="nofollow">鉴权签名文档</a>
</td></tr></tbody></table>

**请求包体**
<table class="t">
<tbody><tr>
<th width="80"><br>
</th><th width="80"><b>参数名</b>
</th><th width="100"><b>类型</b>
</th><th width="150"><b>参数说明</b>
</th></tr>
<tr>
<td> 必须
</td><td> id
</td><td> String
</td><td> App的 API ID
</td></tr>
<tr>
<td> <br>
</td><td> person_id
</td><td> String
</td><td> 待查询个体ID
</td></tr></tbody></table>

**示例**
```
{
	"id":"123456",
	"person_id":"person0"
}
```

5)返回值说明
<table class="t">
<tbody><tr>
<th width="80"><b>字段</b>
</th><th width="100"><b>类型</b>
</th><th width="150"><b>说明</b>
</th></tr>
<tr>
<td> errorcode
</td><td> int
</td><td> 返回状态码
</td></tr>
<tr>
<td> person_name
</td><td> string
</td><td> 相应person的name
</td></tr>
<tr>
<td> person_id
</td><td> string
</td><td> 相应person的id
</td></tr>
<tr>
<td> face_ids
</td><td> Array(string)
</td><td> 包含的人脸列表
</td></tr>
<tr>
<td> group_ids
</td><td> Array(string)
</td><td> 包含此个体的组id
</td></tr>
<tr>
<td> session_id
</td><td> string
</td><td> 相应请求的session标识符，保留
</td></tr>
<tr>
<td> tag
</td><td> string
</td><td> 备注信息
</td></tr>
<tr>
<td> errormsg
</td><td> String
</td><td> 返回错误消息
</td></tr></tbody></table>

**示例**
```
{
    "person_id": "9eb44387923528f97f8545d8bef906db", 
    "person_name": "NicolasCage", 
    "face_ids": [
            "199d1efd19ce4ee67a7ec7655f859b1a", 
            
	], 
	"tag":"person tag",
	"errorcode": 0, 
	"session_id"："session_id",
	"errormsg":"ok"
}
```

## 信息查询

### 组列表
1)接口
```
https://youtu.api.qcloud.com/youtu/api/getgroupids
```
2)描述
>获取一个AppId下所有group列表
3)请使用 POST方式调用

4)HTTP请求格式

**头部信息**
<table class="t">
<tbody><tr>
<th width="80"><b>参数名称</b>
</th><th width="50"><b>必选</b>
</th><th width="50"><b>类型</b>
</th><th width="150"><b>描述</b>
</th></tr>
<tr>
<td> Host
</td><td> 是
</td><td> String
</td><td> 图片云服务器域名，固定为youtu.api.qcloud.com
</td></tr>
<tr>
<td> Content-Length
</td><td> 是
</td><td> Int
</td><td> 整个请求包体内容的总长度，单位：字节（Byte）
</td></tr>
<tr>
<td> Content-Type
</td><td> 是
</td><td> String
</td><td> text/json表示json格式
</td></tr>
<tr>
<td> Signature
</td><td> 是
</td><td> String
</td><td> 多次有效签名,用于鉴权， 具体生成方式详见<a href="http://imgcache.qq.com/qcloud/tianyan/wiki/Authorization.pdf" target="_blank" rel="nofollow">鉴权签名文档</a>
</td></tr></tbody></table>

**请求包体**
<table class="t">
<tbody><tr>
<th width="80"><b>字段</b>
</th><th width="100"><b>类型</b>
</th><th width="150"><b>参数说明</b>
</th></tr>
<tr>
<td> id
</td><td> String
</td><td> App的 API ID
</td></tr></tbody></table>

**示例**
```
{
	"id":"123456",
}
```

5)返回值说明
<table class="t">
<tbody><tr>
<th width="80"><b>字段</b>
</th><th width="100"><b>类型</b>
</th><th width="150"><b>说明</b>
</th></tr>
<tr>
<td> errorcode
</td><td> int
</td><td> 返回状态码
</td></tr>
<tr>
<td> group_ids
</td><td> Array(string)
</td><td> 相应id的id列表
</td></tr>
<tr>
<td> errormsg
</td><td> String
</td><td> 返回错误消息
</td></tr></tbody></table>

**示例**
```
{
	"group _ids":["tencent"],
	"errorcode":0,
	"errormsg":"ok"
}
```

## 个体列表
1)接口
```
https://youtu.api.qcloud.com/youtu/api/getpersonids
```
2)描述
>获取一个组Group中所有person列表

3)请使用 POST方式请求

4)HTTP请求格式


**头部信息**

<table class="t">
<tbody><tr>
<th width="80"><b>参数名称</b>
</th><th width="50"><b>必选</b>
</th><th width="50"><b>类型</b>
</th><th width="150"><b>描述</b>
</th></tr>
<tr>
<td> Host
</td><td> 是
</td><td> String
</td><td> 图片云服务器域名，固定为youtu.api.qcloud.com
</td></tr>
<tr>
<td> Content-Length
</td><td> 是
</td><td> Int
</td><td> 整个请求包体内容的总长度，单位：字节（Byte）
</td></tr>
<tr>
<td> Content-Type
</td><td> 是
</td><td> String
</td><td> text/json表示json格式
</td></tr>
<tr>
<td> Signature
</td><td> 是
</td><td> String
</td><td> 多次有效签名,用于鉴权， 具体生成方式详见<a href="http://imgcache.qq.com/qcloud/tianyan/wiki/Authorization.pdf" target="_blank" rel="nofollow">鉴权签名文档</a>
</td></tr></tbody></table>

**请求包体**
<table class="t">
<tbody><tr>
<th width="80"><b>字段</b>
</th><th width="100"><b>类型</b>
</th><th width="150"><b>参数说明</b>
</th></tr>
<tr>
<td> id
</td><td> String
</td><td> App的 API ID
</td></tr>
<tr>
<td> group_id
</td><td> String
</td><td> 组id
</td></tr></tbody></table>

**示例**
```
{
	"id":"123456",
	"group_id":"12345"
} 
```

5)返回值说明
<table class="t">
<tbody><tr>
<th width="80"><b>字段</b>
</th><th width="100"><b>类型</b>
</th><th width="150"><b>说明</b>
</th></tr>
<tr>
<td> errorcode
</td><td> int
</td><td> 返回状态码
</td></tr>
<tr>
<td> person_ids
</td><td> Array(string)
</td><td> 相应person的id列表
</td></tr>
<tr>
<td> errormsg
</td><td> String
</td><td> 返回错误消息
</td></tr></tbody></table>

**示例**
```
{
"person_ids": [
"person0", 
...
],
"errorcode": 0,
"errormsg":"ok"
}
```

### 人脸列表

1)接口
```
https://youtu.api.qcloud.com/youtu/api/getfaceids
```
2)描述
>获取一个组person中所有face列表

3)请使用 POST方式调用

4)HTTP请求格式

**头部信息**
<table class="t">
<tbody><tr>
<th width="80"><b>参数名称</b>
</th><th width="50"><b>必选</b>
</th><th width="50"><b>类型</b>
</th><th width="150"><b>描述</b>
</th></tr>
<tr>
<td> Host
</td><td> 是
</td><td> String
</td><td> 图片云服务器域名，固定为youtu.api.qcloud.com
</td></tr>
<tr>
<td> Content-Length
</td><td> 是
</td><td> Int
</td><td> 整个请求包体内容的总长度，单位：字节（Byte）
</td></tr>
<tr>
<td> Content-Type
</td><td> 是
</td><td> String
</td><td> text/json表示json格式
</td></tr>
<tr>
<td> Signature
</td><td> 是
</td><td> String
</td><td> 多次有效签名,用于鉴权， 具体生成方式详见<a href="http://imgcache.qq.com/qcloud/tianyan/wiki/Authorization.pdf" target="_blank" rel="nofollow">鉴权签名文档</a>
</td></tr></tbody></table>

**请求包体**
<table class="t">
<tbody><tr>
<th width="80"><b>字段</b>
</th><th width="100"><b>类型</b>
</th><th width="150"><b>参数说明</b>
</th></tr>
<tr>
<td> id
</td><td> String
</td><td> App的 API ID
</td></tr>
<tr>
<td> person_id
</td><td> String
</td><td> 个体id
</td></tr></tbody></table>

**示例**
```
{
"id":"123456",
"person_id":"12345"
}
```
5)返回值说明
<table class="t">
<tbody><tr>
<th width="80"><b>字段</b>
</th><th width="100"><b>类型</b>
</th><th width="150"><b>说明</b>
</th></tr>
<tr>
<td> errorcode
</td><td> int
</td><td> 返回状态码
</td></tr>
<tr>
<td> face_ids
</td><td> Array(string)
</td><td> 相应face的id列表
</td></tr>
<tr>
<td> errormsg
</td><td> String
</td><td> 返回错误消息
</td></tr></tbody></table>

示例
```
{
"face_ids": [
"1005338790489817087", 
...
],
"errorcode": 0,
"errormsg":"ok"
}
```

### 人脸信息
1)接口
```
https://youtu.api.qcloud.com/youtu/api/getfaceinfo
```
2)描述
>获取一个face的相关特征信息。
>
3)请使用POST方式调用

4)HTTP请求格式

**头部信息**
<table class="t">
<tbody><tr>
<th width="80"><b>参数名称</b>
</th><th width="50"><b>必选</b>
</th><th width="50"><b>类型</b>
</th><th width="150"><b>描述</b>
</th></tr>
<tr>
<td> Host
</td><td> 是
</td><td> String
</td><td> 图片云服务器域名，固定为youtu.api.qcloud.com
</td></tr>
<tr>
<td> Content-Length
</td><td> 是
</td><td> Int
</td><td> 整个请求包体内容的总长度，单位：字节（Byte）
</td></tr>
<tr>
<td> Content-Type
</td><td> 是
</td><td> String
</td><td> text/json表示json格式
</td></tr>
<tr>
<td> Signature
</td><td> 是
</td><td> String
</td><td> 多次有效签名,用于鉴权， 具体生成方式详见<a href="http://imgcache.qq.com/qcloud/tianyan/wiki/Authorization.pdf" target="_blank" rel="nofollow">鉴权签名文档</a>
</td></tr></tbody></table>

**请求包体**
<table class="t">
<tbody><tr>
<th width="80"><b>字段</b>
</th><th width="100"><b>类型</b>
</th><th width="150"><b>参数说明</b>
</th></tr>
<tr>
<td> id
</td><td> String
</td><td> App的 API ID
</td></tr>
<tr>
<td> face_id
</td><td> String
</td><td> 人脸id
</td></tr></tbody></table>

**示例**
```
{
"id":"123456",
"face_id ":"1005338790489817087"
} 
```

5)返回值说明

<table class="t">
<tbody><tr>
<th width="80"><b>字段</b>
</th><th width="100"><b>类型</b>
</th><th width="150"><b>说明</b>
</th></tr>
<tr>
<td> errorcode
</td><td> int
</td><td> 返回状态码
</td></tr>
<tr>
<td> face_info
</td><td> FaceItem
</td><td> 人脸信息
</td></tr>
<tr>
<td> errormsg
</td><td> String
</td><td> 返回错误消息
</td></tr></tbody></table>

**示例**
```
{
	"face_info": {
	"face_id": "1005338790489817087",
	  "x": 44,
	  "y": 33,
	  "height": 64,
	  "width": 64,
	  "pitch": 5,
	  "roll": 0,
	  "yaw": 6,
	  "age": 37,
	  "gender": 99,
	  "glass": true,
	  "expression": 6
	},
	"errorcode": 0,
	"errormsg":"ok"
}
```

## 错误码
### 8.1 HTTP返回码
>400  HTTP_BAD_REQUEST    请求不合法，包体格式错误
401  HTTP_UNAUTHORIZED    权限验证失败
403  HTTP_FORBIDDEN    鉴权信息不合法，禁止访问
500  HTTP_INTERNAL_SERVER_ERROR    服务内部错误
503  HTTP_SERVICE_UNAVAILABLE    服务不可用
504  HTTP_GATEWAY_TIME_OUT    后端服务超时
### 8.2 协议错误码
>-100    SDK_DISTANCE_ERROR    相似度错误
-101    SDK_IMAGE_FACEDETECT_FAILED    人脸检测失败
-102    SDK_IMAGE_DECODE_FAILED    图片解码失败
-103    SDK_FEAT_PROCESSFAILED    特征处理失败
-104    SDK_FACE_SHAPE_FAILED    提取轮廓错误
-105    SDK_FACE_GENDER_FAILED    提取性别错误
-106    SDK_FACE_EXPRESSION_FAILED    提取表情错误
-107    SDK_FACE_AGE_FAILED    提取年龄错误
-108    SDK_FACE_POSE_FAILED	    提取姿态错误
-109    SDK_FACE_GLASS_FAILED    提取眼镜错误
-200    STORAGE_ERROR    存储错误
-300    ERROR_IMAGE_EMPTY    图片为空
-301    ERROR_PARAMETER_EMPTY    参数为空
-302    ERROR_PERSON_EXISTED	    个体已存在
-303    ERROR_PERSON_NOT_EXISTED    个体不存在
-304    ERROR_PARAMETER_TOO_LONG    参数过长
