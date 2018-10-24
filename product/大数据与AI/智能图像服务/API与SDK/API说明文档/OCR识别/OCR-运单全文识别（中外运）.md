## 接口概述

### 服务简介
中外运单据OCR识别，根据用户提供的中外运单据图片，返回识别出的字段信息。

### url 说明
支持 http 和 https 两种协议：

`http://recognition.image.myqcloud.com/ocr/waybill`

`https://recognition.image.myqcloud.com/ocr/waybill`

## 请求方式

### 请求头 header
所有请求都要求含有以下头部信息：

| 参数名          | 值                             | 描述                     |
| -------------- | ------------------------------ | ------------------------ |
| host           | recognition.image.myqcloud.com | 腾讯云文字识别服务器域名      |
| content-length | 包体总长度                      | 整个请求包体内容的总长度，单位：字节（Byte）|
| content-type	 | Multipart/form-data            | 支持上传本地图片的方式                   |
| authorization	 | 鉴权签名	                      | 多次有效签名，用于鉴权， 具体生成方式详见 [鉴权签名方法](/document/product/641/12409) |


### 请求参数

| 参数名          | 必选	     | 类型	       | 参数说明      |
| -------------- | ------------- | ----------- | ------------ |
| appid	         | 是	         | string      | 开发商应用ID |
| type	         | 是	         | int	       | 0:fapiao  <br> 3:bill_chinese  <br> 4:bill_english |
| image	         | 是	         | binary	   | 图片内容      |

## 返回内容

| 字段           | 类型                    | 说明               |
| ------------- | ----------------------- | ------------------ |
| data	        | array(itemcontent)	  | 识别出的所有字段信息 |
| code        	| int	                  | 返回码             |
| message	    | string	              | 返回错误消息        |

ItemContent 说明：

| 字段           | 类型                    | 说明               |
| ------------- | ----------------------- | ------------------ |
| item	        | string	              | 字段名称            |
| item_type     | int	                  | 字段类型            |
| item_text	    | string	              | 字段内容            |
| item_coord	| coordinate	          | 文本行坐标          |
| candwords	    | array(CandiateWord)	  | 候选字符集          |

coordinate 说明：

| 字段           | 类型                    | 说明               |
| ------------- | ----------------------- | ------------------ |
| x	            | int	                  | item框左上角x       |
| y	            | int	                  | item框左上角y       |
| width	        | int	                  | item框宽度          |
| height	    | int	                  | item框高度          |

candiateword说明:

| 字段           | 类型                    | 说明               |
| ------------- | ----------------------- | ------------------ |
| words	        | array(Word)	          | 候选词列表          |

word说明:

| 字段           | 类型                    | 说明                |
| ------------- | ----------------------- | ------------------ |
| character	    | string	              | 字符内容            |
| Confidence	| float	                  | 置信度              |

### 请求示例

```
POST /ocr/waybill HTTP/1.1
Authorization: FCHXdPTEwMDAwMzc5Jms9QUtJRGVRZDBrRU1yM2J4ZjhRckJi==
Host: recognition.image.myqcloud.com
Content-Length: 735
Content-Type: multipart/form-data;boundary=--------------acebdf13572468

----------------acebdf13572468
Content-Disposition: form-data; name="appid";

123456
----------------acebdf13572468
Content-Disposition: form-data; name="type";

0
----------------acebdf13572468
Content-Disposition: form-data; name="image"; filename="test.jpg"
Content-Type: image/jpeg

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
----------------acebdf13572468--
```

### 返回示例

```
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 4044
Content-Type: application/json

{
    "data": [
        {
            "item": "123",
            "item_type": 1,
            "item_text": "abcdef",
            "item_coord": {...},
            "candwords": [...]
        },
        {...}
    ],
    "code": 0,
    "message": "OK"
}
```
## 错误码

| 错误码	               | 含义                 |
| -------------------- | ------------------- |
| 0	                   | 成功                 |
| 3	                   | 错误的请求；其中 message:account abnormal,errorno is:2 为账号欠费停服             |
| 4	                   | 签名为空              |
| 5                    | 签名串错误            |
| 9	                   | 签名过期              |
| 10	               | appid不存在          |
| 11	               | secretid不存在        |
| 12	               | appid和secretid不匹配 |
| 13                   | 重放攻击              |
| 14	               | 签名校验失败          |
| 15	               | 操作太频繁，触发频控   |
| 16	               | Bucket不存在         |
| 21	               | 无效参数             |
| 23	               | 请求包体过大          |
| 24	               | 没有权限             |
| 25	               | 您购买的资源已用完    |
| 107                  | 鉴权服务不可用        |
| 108	               | 鉴权服务不可用        |
| 213	               | 内部错误             |	
| 其他	               | 图片识别失败         |

 更多其他 API 错误码请看[**错误码说明**](/document/product/641/12410)。










