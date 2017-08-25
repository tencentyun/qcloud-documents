## 功能描述
<!-- 描述该 API 的功能、背景、条件等-->
List Multipart Uploads 用来查询正在进行中的分块上传。单次请求操作最多列出 1000 个正在进行中的分块上传。
## 请求
<!-- 完整结构的请求语法示例，包括请求行、请求头、请求体。请求行中要有必选参数，非必选的不用写-->
语法示例：
```
GET /?uploads&delimiter=Delimiter HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```
<!-- 代码块中注意：
       1. HTTP 是全大写；
       2. 每一个冒号后面都有一个空格；
       3. Dete 格式是 GMT Date；
       4. Authorization 统一为 Auth String -->
> Authorization: Auth String (详细参见 [请求签名](https://www.qcloud.com/document/product/436/7778) 章节)

### 请求行
<!-- 将以上完整结构的请求语法示例中的请求行单独描述说明-->
```
GET /?uploads&delimiter=Delimiter HTTP/1.1
```
该 API 接口接受 GET 请求。

#### 请求参数 <!-- 如果实际 API 中没有请求参数，可以不用出现 -->

包含所有请求参数的请求行示例：
<!-- 请求行示例中列出该 API 请求所有必选和非必选参数 -->

```
GET /?uploads&delimiter=Delimiter&encoding-type=EncodingType&prefix=Prefix&max-uploads=MaxUploads&key-marker=KeyMarker&upload-id-marker=UploadIdMarker HTTP/1.1
```
<style  rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style> 
<!-- 这行代码要放在所有表格之上，目的是为了统一将本页所有的表格第一列宽度都为 200px -->
具体内容如下：
<!-- 用表格形式列出所有必选和非必选参数，必要的时候给出示例。注意：参数名称全小写-->

| 参数名称               | 描述                                       | 类型     | 必选   |
| ---------------- | ---------------------------------------- | ------ | ---- |
| delimiter        | 定界符为一个符号 | String | 是    |
| encoding-type    | 规定返回值的编码格式，合法值：url   | String | 否    |
| prefix           | 限定返回的 Object key 必须以 Prefix 作为前缀| String | 否    |
| max-uploads      | 设置最大返回的 multipart 数量，合法取值从1到1000，默认1000   | String | 否    |
| key-marker       | 与 upload-id-marker 一起使用 | String | 否    |
| upload-id-marker | 与 key-marker 一起使用 | String | 否    |

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://www.qcloud.com/document/product/436/7728) 章节。

#### 非公共头部
<!-- 如果实际 API 中没有非公共头部内容，表述的语句为：该请求操作无特殊的请求头部信息。
并且以下“必选头部”、“推荐头部”和“权限相关头部”都不用说明。-->
**必选头部**<!-- 如果实际 API 中没有，可以不用出现 -->
该请求操作的实现使用如下必选头部：

| 名称               | 描述      | 类型     | 必选   |
| ---------------- | ----------- | ------ | ---- |
| abc       | 与 upload一起使用 | String | 否    |
| defg | 与 key一起使用 | String | 否    |

**推荐头部**<!-- 如果实际 API 中没有，可以不用出现 -->
该请求操作的实现使用如下推荐请求头部信息：

| 名称               | 描述      | 类型     | 必选   |
| ---------------- | ----------- | ------ | ---- |
| abc       | 与 upload一起使用 | String | 否    |
| defg | 与 key一起使用 | String | 否    |

**权限相关头部**<!-- 如果实际 API 中没有，可以不用出现 -->
该请求操作的实现可以用 PUT 请求中的 x-cos-acl 头来设置 Object 访问权限。

| 名称               | 描述      | 类型     | 必选   |
| ---------------- | ----------- | ------ | ---- |
| abc       | 与 upload一起使用 | String | 否    |
| defg | 与 key一起使用 | String | 否    |

### 请求体
<!-- 如果实际 API 中没有请求体,表述的语句为：该请求的请求体为空。-->
该 API 接口请求的请求体具体节点内容为：
```
<Delete>
  <Object>
    <Key></Key>
  </Object>
  ...
</Delete>
```
具体内容描述如下：

|节点名称（关键字）|	父节点|	描述	|类型|	必选|
|---|---|---|---|---|
|Delete	|无	|说明本次删除的返回结果方式和目标 Object	|Container	|是|
|Object|	Delete	|说明每个将要删除的目标 Object 信息	|Container|	是|
|Key	|Delete.Object|	目标 Object 文件名称	|String	|是|

## 响应

### 响应头
#### 公共响应头 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://www.qcloud.com/document/product/436/7729) 章节。
#### 特有响应头
<!-- 如果实际 API 中没有特有响应头，表述的语句为：该响应无特殊的响应头。-->
该请求操作的响应头具体数据为：

|名称	|描述|	类型|
|---	|---|	---|
|x-cos-meta- * |用户自定义的 meta	|String|
|x-cos-object-type	|用来表示 Object 是否可以被追加上传，枚举值：normal 或者 appendable|	String|
|x-cos-storage-class	|Object 的存储级别，枚举值：Standard, Standard_IA, Nearline	|String|

### 响应体
<!-- 如果实际 API 中没有请求体,表述的语句为：该响应体返回为空。-->
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：
```
<ListMultipartUploadsResult>
  <Bucket></Bucket>
  <Encoding-Type></Encoding-Type>
  <KeyMarker></KeyMarker>
  <Upload>
    <Key></Key>
    <UploadID></UploadID>
    <StorageClass></StorageClass>
    <Initiator>
      <UIN></UIN>
    </Initiator>
    <Owner>
      <UID></UID>
    </Owner>
    <Initiated></Initiated>
  </Upload>
  <CommonPrefixs>
    <Prefix></Prefix>
  </CommonPrefixs>
</ListMultipartUploadsResult>
```
具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| ListMultipartUploadsResult |无| 用来表述所有分块上传的信息 | Container |

Container 节点 ListMultipartUploadsResult 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Bucket | ListMultipartUploadsResult | 分块上传的目标 Bucket |  String |
| Encoding-Type | ListMultipartUploadsResult | 规定返回值的编码格式，合法值：url |  String |
| KeyMarker | ListMultipartUploadsResult| 列出条目从该 key 值开始 |  String |
| Upload | ListMultipartUploadsResult  | 每个 Upload 的信息 |  Container |
| CommonPrefixs | ListMultipartUploadsResult | 将 prefix 到 delimiter 之间的相同路径归为一类，定义为 Common Prefix |  Container |

Container 节点 Upload 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Key | ListMultipartUploadsResult.Upload |  Object 的名称 |  String |
| UploadID | ListMultipartUploadsResult.Upload |  标示本次分块上传的 ID | String |
| StorageClass | ListMultipartUploadsResult.Upload |  用来表示分块的存储级别，枚举值：STANDARD，STANDARD_IA，NEARLINE  |  String |
| Initiator | ListMultipartUploadsResult.Upload |  用来表示本次上传发起者的信息 |  Container |
| Owner | ListMultipartUploadsResult.Upload | 用来表示这些分块所有者的信息 |  Container |
| Initiated | ListMultipartUploadsResult.Upload |  分块上传的起始时间 |  Date |

Container 节点 Initiator 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| UIN | ListMultipartUploadsResult.Upload.Initiator | 开发商 APPID | String  |

Container 节点 Owner 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| UID | ListMultipartUploadsResult.Upload.Owner | Object 的持有者 ID  | String    |

Container 节点 CommonPrefixs 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| Prefix | ListMultipartUploadsResult.CommonPrefixs | 显示具体的CommonPrefixs | String    |

## 实际案例

### 请求
```
GET /?uploads HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Date: Wed, 18 Jan 2015 21:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484727508;32557623508&q-key-time=1484727508;32557623508&q-header-list=host&q-url-param-list=uploads&q-signature=5bd4759a7309f7da9a0550c224d8c61589c9dbbf

```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1203
Date: Wed, 18 Jan 2015 21:32:00 GMT
Server: tencent-cos
x-cos-request-id: NTg3ZjI0ZGRfNDQyMDRlXzNhZmRfMjRl

<ListMultipartUploadsResult>
    <Bucket>arlenhuangtestsgnoversion</Bucket>
    <Encoding-Type/>
    <KeyMarker/>
    <IsTruncated>false</IsTruncated>
    <Upload>
        <Key>Object</Key>
        <UploadID>1484726657932bcb5b17f7a98a8cad9fc36a340ff204c79bd2f51e7dddf0b6d1da6220520c</UploadID>
        <Initiator>
           <UIN>14847266009/14847266009<UIN/>
        </Initiator>
        <Owner>
            <UID>1251668577</UID>
        </Owner>
        <StorageClass>Standard</StorageClass>
        <Initiated>Wed Jan 18 16:04:17 2017</Initiated>
    </Upload>
</ListMultipartUploadsResult>
```


==============================华丽丽的分割线==============================================
以上仅作文章结构示例，不做实际文档使用。接下来我们来说说其他细节部分：

## 格式细节部分

1. `HTTP/1.1`  是正规写法， HTTP 全大写，不要漏写反斜杠 “/” 。
2. 官网概念、专有名词统一大小写：APPID，SecretId，SecretKey，Bucket，Object，String 等
3. 中英文之间要空格。如：该响应体返回为 application/xml 数据。
4.  链接与正文间要空格。如：了解公共请求头详细请参见 [公共请求头部](https://www.qcloud.com/document/product/436/7728) 章节。
5.  阿拉伯数字与中文间要空格，如：列出 1000 个正在进行中的分块。
5.  变量名词用尖括号 &lt;abc&gt; 表示，左右尖括号用转义字符 `&lt;`,`&gt;` 表示。
6.  可选参数用英文方括号 [abc] 表示。
7.  不帯超链接的域名仅做示例的，要用内敛代码标识 `www.qcloud.com`。
8.  “通配符 * ”正确写法：“ * ”前后带空格。
9.  文中的“注意”有强调作用 ，所以“注意”要加粗换行，但注意的内容不加粗。如：

><font color="#0000cc">**注意：** </font>
- 默认下载域名在创建好存储桶后，可通过 [对象存储控制台](https://console.qcloud.com/cos4) 的存储桶【域名管理】查看。
- bucketname 是在创建存储桶时为存储桶命名的名称，可通过 [对象存储控制台](https://console.qcloud.com/cos4) 的存储桶【基础配置】查看。

11.表格描述中不带符号结尾。如：

| 节点名称（关键字） |父节点 | 描述  | 类型   |
| ------------ | ---------- | --------- |:--|
| Prefix |CommonPrefixs | 显示具体的CommonPrefixs | String    |






