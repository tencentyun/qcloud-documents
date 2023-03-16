# request

- 功能描述

发起 HTTPS 网络请求。使用前请注意阅读[相关说明](/develop/frame/basic_ability/basic_network.md)。

#### 参数

##### Object object

属性           | 类型                        | 默认值  | 必填 | 说明                                                                         | 最低版本                                                                                                              
------------ | ------------------------- | ---- | -- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------
url          | string                    |      | 是  | 开发者服务器接口地址                                                                 |                                                                                                                   
data         | string/object/ArrayBuffer |      | 否  | 请求的参数                                                                      |                                                                                                                   
header       | Object                    |      | 否  | 设置请求的 header，header 中不能设置 Referer。  
`content-type` 默认为 `application/json` |                             |      |        |       |                                                                                  
method       | string                    | GET  | 否  | HTTP 请求方法                                                                  |                                                                                                                   
dataType     | string                    | json | 否  | 返回的数据格式                                                                    |                                                                                                                   
responseType | string                    | text | 否  | 响应的数据类型                                                                    | 
success      | function                  |      | 否  | 接口调用成功的回调函数                                                                |                                                                                                                   
fail         | function                  |      | 否  | 接口调用失败的回调函数                                                                |                                                                                                                   
complete     | function                  |      | 否  | 接口调用结束的回调函数（调用成功、失败都会执行）                                                   |                                                                                                                   

**object.method 的合法值**

值       | 说明             
------- | ---------------
OPTIONS | HTTP 请求 OPTIONS
GET     | HTTP 请求 GET    
HEAD    | HTTP 请求 HEAD   
POST    | HTTP 请求 POST   
PUT     | HTTP 请求 PUT    
DELETE  | HTTP 请求 DELETE 
TRACE   | HTTP 请求 TRACE  
CONNECT | HTTP 请求 CONNECT

**object.dataType 的合法值**

值    | 说明                                   
---- | -------------------------------------
json | 返回的数据为 JSON，返回后会对返回的数据进行一次 JSON.parse
其他   | 不对返回的内容进行 JSON.parse                 

**object.responseType 的合法值**

值           | 说明                
----------- | ------------------
text        | 响应的数据为文本          
arraybuffer | 响应的数据为 ArrayBuffer

###### object.success 回调函数

**参数**

**Object res**

属性         | 类型                        | 说明                             | 最低版本                                                                                                              
---------- | ------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------
data       | string/Object/Arraybuffer | 开发者服务器返回的数据                    |                                                                                                                   
statusCode | number                    | 开发者服务器返回的 HTTP 状态码             |                                                                                                                   
header     | Object                    | 开发者服务器返回的 HTTP Response Header | 

#### 返回值

##### [RequestTask](./RequestTask.md)


请求任务对象

#### data 参数说明

最终发送给服务器的数据是 String 类型，如果传入的 data 不是 String 类型，会被转换成 String 。转换规则如下：

* 对于 `GET` 方法的数据，会将数据转换成 query string（`encodeURIComponent(k)=encodeURIComponent(v)&encodeURIComponent(k)=encodeURIComponent(v)...`）
* 对于 `POST` 方法且 `header['content-type']` 为 `application/json` 的数据，会对数据进行 JSON 序列化
* 对于 `POST` 方法且 `header['content-type']` 为 `application/x-www-form-urlencoded` 的数据，会将数据转换成 query string `（encodeURIComponent(k)=encodeURIComponent(v)&encodeURIComponent(k)=encodeURIComponent(v)...）`

#### 示例代码

```js
wx.request({
  url: 'test.php', // 仅为示例，并非真实的接口地址
  data: {
    x: '',
    y: ''
  },
  header: {
    'content-type': 'application/json' // 默认值
  },
  success(res) {
    console.log(res.data)
  }
})
```