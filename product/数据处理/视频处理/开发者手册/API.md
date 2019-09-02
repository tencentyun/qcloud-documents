**注意** ：本文1、2、3部分内容，仅适用于COS V3及以下版本，使用COS V4及以上版本的用户，请参见[COS  API产品手册](https://cloud.tencent.com/document/product/436/7751) 

## 1	基本概念

| 概念            | 解释                                       |
| ------------- | ---------------------------------------- |
| appid         | 接入视频处理时，生成为唯一id， 用于唯一标识接入业务， 获取地址: 密钥配置  |
| Authorization | 签名，具体生成参见[鉴权签名方法](https://cloud.tencent.com/document/product/314/2290)。 |
| bucket_name   | bucket名称，bucket创建参见[创建Bucket](https://console.cloud.tencent.com/media/bucket) |

## 2	鉴权
腾讯云•视频处理通过签名来验证请求的合法性。开发者通过将签名授权给客户端，使其具备上传下载及管理指定资源的能力。

签名分为单次签名和多次签名，区别为: 如果针对资源进行写操作(资源删除)，那么这个签名必须是单次有效的。重复使用该签名则会返回签名失败。如果是上传或下载资源，签名必须是多次有效的，有效时长最多为三个月。

开发者可以通过服务器SDK生成签名，也可以参考我们的签名函数自行生成签名，具体生成方式详见[鉴权签名方法](https://cloud.tencent.com/document/product/314/2290)。

## 3	目录操作

### 3.1	创建目录

功能：在指定路径下创建目录。 接口：web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[dirName]/ <font color="red"><- 有文件夹斜杠 /</font>

要求：父目录存在
方法：POST
请求参数HTTP头部信息：

| 参数名称          | 必选   | 类型     | 描述                                       |
| ------------- | ---- | ------ | ---------------------------------------- |
| Host          | 是    | String | 视频处理服务器域名，固定为web.video.myqcloud.com      |
| Content-Type  | 是    | String | application/json                         |
| Authorization | 是    | String | 多次有效签名，用于鉴权， 具体生成方式详见[鉴权签名方法](https://cloud.tencent.com/document/product/314/2290) |

请求包体 (json)：

| 参数名称     | 必选   | 类型     | 描述               |
| -------- | ---- | ------ | ---------------- |
| op       | 是    | String | 操作类型。固定填"create" |
| biz_attr | 否    | String | 目录属性，业务端维护       |

返回包体(json)：
<table style="display:table;width:80%;">
	<tbody>
		<tr>
			<th><strong>参数名称</strong></th>
			<th><strong>子属性</strong></th>
			<th><strong>必选</strong></th>
			<th><strong>类型</strong></th>
			<th><strong>描述</strong></th>
		</tr>
		<tr>
			<td>code</td>
			<td>-</td>
			<td>是</td>
			<td>Int</td>
			<td>服务端返回码</td>
		</tr>
		<tr>
			<td>message</td>
			<td>-</td>
			<td>是</td>
			<td>String</td>
			<td>服务端提示内容</td>
		</tr>
		<tr>
			<td rowspan="3">data</td>
			<td>-</td>
			<td>是</td>
			<td>集合</td>
			<td>服务器返回的应答数据</td>
		</tr>
		<tr>
			<td>ctime</td>
			<td>是</td>
			<td>Unix时间戳</td>
			<td>创建时间</td>
		</tr>
		<tr>
			<td>resource_path</td>
			<td>是</td>
			<td>String</td>
			<td>资源路径。 不包含/[appid]/[bucket_name]</td>
		</tr>
	</tbody>
</table>

### 3.2	创建视频：(完整上传)
功能：在指定路径下创建视频。 接口：web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[DirName]/[file_name] <font color="red"> <- 没有文件夹斜杠 / </font>
方法：POST
请求参数HTTP头部信息：

| 参数名称           | 必选   | 类型     | 描述                                       |
| -------------- | ---- | ------ | ---------------------------------------- |
| Content-Length | 是    | Int    | 整个multipart/form-data内容的总长度，单位：字节（Byte）  |
| Content-Type   | 是    | String | 固定为multipart/form-data                   |
| Authorization  | 是    | String | 多次有效签名，用于鉴权， 具体生成方式详见[鉴权签名方法](https://cloud.tencent.com/document/product/314/2290) |

请求包体信息 (multipart/form-data)：

| 参数名称         | 必选   | 类型     | 描述                  |
| ------------ | ---- | ------ | ------------------- |
| op           | 是    | String | 固定填upload           |
| filecontent  | 是    | Binary | 视频文件内容              |
| sha          | 否    | String | 视频文件的sha值           |
| biz_attr     | 否    | String | 文件属性，业务端维护          |
| video_cover  | 否    | String | 视频封面的URL            |
| video_title  | 否    | String | 视频标题                |
| video_desc   | 否    | String | 视频描述                |
| magicContext | 否    | String | 转码成功后，用于透传回调用者的业务后台 |

返回包体信息(json):
<table style="display:table;width:80%;">
	<tbody>
		<tr>
			<th><strong>参数名称</strong></th>
			<th><strong>子属性</strong></th>
			<th><strong>必选</strong></th>
			<th><strong>类型</strong></th>
			<th><strong>描述</strong></th>
		</tr>
		<tr>
			<td>code</td>
			<td>-</td>
			<td>是</td>
			<td>Int</td>
			<td>服务端返回码</td>
		</tr>
		<tr>
			<td>message</td>
			<td>-</td>
			<td>是</td>
			<td>String</td>
			<td>服务端提示内容</td>
		</tr>
		<tr>
			<td rowspan="4">data</td>
			<td>-</td>
			<td>是</td>
			<td>集合</td>
			<td>服务器返回的应答数据</td>
		</tr>
		<tr>
			<td>access_url</td>
			<td>是</td>
			<td>String</td>
			<td>生成的文件下载url</td>
		</tr>
		<tr>
			<td>url</td>
			<td>是</td>
			<td>String</td>
			<td>操作文件的url</td>
		</tr>
		<tr>
			<td>resource_path</td>
			<td>是</td>
			<td>String</td>
			<td>资源路径。 不包含/[appid]/[bucket_name]</td>
		</tr>
	</tbody>
</table>

### 3.3	创建视频：(分片上传， 第一片)
功能：在指定路径下创建视频。 接口：web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[DirName]/[file_name] <font color="red"> <- 没有文件夹斜杠 / </font>
方法： POST
请求参数HTTP头部信息：

| 参数名称           | 必选   | 类型     | 描述                                       |
| -------------- | ---- | ------ | ---------------------------------------- |
| Content-Length | 是    | Int    | 整个multipart/form-data内容的总长度，单位：字节（Byte）  |
| Content-Type   | 是    | String | 固定为multipart/form-data                   |
| Authorization  | 是    | String | 多次有效签名，用于鉴权， 具体生成方式详见[鉴权签名方法](https://cloud.tencent.com/document/product/314/2290) |

请求包体信息 (multipart/form-data)：

| 参数名称         | 必选   | 类型     | 描述                         |
| ------------ | ---- | ------ | -------------------------- |
| op           | 是    | String | 固定填upload_slice            |
| filesize     | 是    | Int 64 | 视频文件总大小                    |
| sha          | 否    | String | 文件的sha值，必须提供               |
| biz_attr     | 否    | String | 视频属性，业务端维护                 |
| video_cover  | 否    | String | 视频封面的URL                   |
| session      | 否    | String | 如果想要断点续传，则带上上一次的session id |
| video_title  | 否    | String | 视频标题                       |
| video_desc   | 否    | String | 视频描述                       |
| magicContext | 否    | String | 转码成功后，用于透传回调用者的业务后台        |

返回包体信息(json)：
<table style="display:table;width:80%;">
	<tbody>
		<tr>
			<th><strong>参数名称</strong></th>
			<th><strong>子属性</strong></th>
			<th><strong>必选</strong></th>
			<th><strong>类型</strong></th>
			<th><strong>描述</strong></th>
		</tr>
		<tr>
			<td>code</td>
			<td>-</td>
			<td>是</td>
			<td>Int</td>
			<td>服务端返回码</td>
		</tr>
		<tr>
			<td>message</td>
			<td>-</td>
			<td>是</td>
			<td>String</td>
			<td>服务端提示内容</td>
		</tr>
		<tr>
			<td rowspan="7">data</td>
			<td>-</td>
			<td>是</td>
			<td>集合</td>
			<td>服务器返回的应答数据</td>
		</tr>
		<tr>
			<td>session</td>
			<td>否(非秒传的大部分情况会有)</td>
			<td>String</td>
			<td>唯一标识此视频文件传输过程的id</td>
		</tr>
		<tr>
			<td>offset</td>
			<td>否(非秒传的大部分情况会有)</td>
			<td>Int 64</td>
			<td>开始传输的位移</td>
		</tr>
		<tr>
			<td>slice_size</td>
			<td>否(非秒传的大部分情况会有)</td>
			<td>Int</td>
			<td>分片大小</td>
		</tr>
		<tr>
			<td>access_url</td>
			<td>否(上一次已传完/秒传成功)</td>
			<td>String</td>
			<td>生成的文件下载url</td>
		</tr>
		<tr>
			<td>url</td>
			<td>否(上一次已传完/秒传成功)</td>
			<td>String</td>
			<td>操作文件的url</td>
		</tr>
		<tr>
			<td>resource_path</td>
			<td>否(上一次已传完/秒传成功)</td>
			<td>String</td>
			<td>资源路径。 不包含/[appid]/[bucket_name]</td>
		</tr>
	</tbody>
</table>

### 3.4	创建视频：(分片上传， 后续分片)
功能：在指定路径下创建视频。 接口：web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[DirName]/[file_name] <font color="red"><- 有文件夹斜杠 /</font>
方法：POST
请求参数HTTP头部信息：

| 参数名称           | 必选   | 类型     | 描述                                       |
| -------------- | ---- | ------ | ---------------------------------------- |
| Content-Length | 是    | Int    | 整个multipart/form-data内容的总长度，单位：字节（Byte）  |
| Content-Type   | 是    | String | 固定为multipart/form-data                   |
| Authorization  | 是    | String | 多次有效签名，用于鉴权， 具体生成方式详见[鉴权签名方法](https://cloud.tencent.com/document/product/314/2290) |

请求包体信息 (multipart/form-data):

| 参数名称        | 必选   | 类型     | 描述                             |
| ----------- | ---- | ------ | ------------------------------ |
| op          | 是    | String | 固定填upload_slice                |
| filecontent | 是    | Binary | 视频文件内容                         |
| sha         | 否    | String | 本次文件分片的sha值，可以提供用于校验(暂时未启用)    |
| session     | 是    | String | 唯一标识此视频文件传输过程的id， 由后台下发， 调用方透传 |
| offset      | 是    | Int 64 | 本次分片位移                         |


返回包体信息(json):
<table style="display:table;width:80%;">
	<tbody>
		<tr>
			<th><strong>参数名称</strong></th>
			<th><strong>子属性</strong></th>
			<th><strong>必选</strong></th>
			<th><strong>类型</strong></th>
			<th><strong>描述</strong></th>
		</tr>
		<tr>
			<td>code</td>
			<td>-</td>
			<td>是</td>
			<td>Int</td>
			<td>服务端返回码</td>
		</tr>
		<tr>
			<td>message</td>
			<td>-</td>
			<td>是</td>
			<td>String</td>
			<td>服务端提示内容</td>
		</tr>
		<tr>
			<td rowspan="7">data</td>
			<td>-</td>
			<td>是</td>
			<td>集合</td>
			<td>服务器返回的应答数据</td>
		</tr>
		<tr>
			<td>session</td>
			<td>否(非秒传的大部分情况)	</td>
			<td>String</td>
			<td>唯一标识此视频文件传输过程的id</td>
		</tr>
		<tr>
			<td>offset</td>
			<td>否(非秒传的大部分情况)	</td>
			<td>Int 64</td>
			<td>请求包体里的传输的位移，调用方如果用多线程等方式传输，可以用来唯一确定本次分片结果</td>
		</tr>
		<tr>
			<td>access_url</td>
			<td>否(上一次已传完/秒传成功)</td>
			<td>String</td>
			<td>生成的文件下载url</td>
		</tr>
		<tr>
			<td>url</td>
			<td>否(上一次已传完/秒传成功)</td>
			<td>String</td>
			<td>操作文件的url</td>
		</tr>
		<tr>
			<td>resource_path</td>
			<td>否(上一次已传完/秒传成功)</td>
			<td>String</td>
			<td>资源路径。 不包含/[appid]/[bucket_name]</td>
		</tr>
	</tbody>
</table>

### 3.5	目录列表，前缀搜索
功能：在指定路径下搜索视频或目录。 接口：web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/
web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[DirName]/
web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[DirName]/[prefix] <font color="red"> <- 如果填写prefix， 则列出含此前缀的所有文件</font>
方法：GET
Request Param(query string)：

| 参数名称          | 必选   | 类型     | 描述                                       |
| ------------- | ---- | ------ | ---------------------------------------- |
| op            | 否    | String | 操作类型。可以不填，如果要填，固定填”list“                 |
| num           | 是    | Int    | 拉取的总数                                    |
| pattern       | 否    | String | eListBoth， eListDirOnly， eListFileOnly (默认eListBoth) |
| order         | 否    | Int    | 默认正序(=0)， 填1为反序，                         |
| context       | 否    | String | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页。 |
| Authorization | 是    | String | 多次有效签名，用于鉴权， 具体生成方式详见[鉴权签名方法](https://cloud.tencent.com/document/product/314/2290) |

Response (json):
<table style="display:table;width:80%;">
	<tbody>
		<tr>
			<th><strong>参数名称</strong></th>
			<th><strong>子属性</strong></th>
			<th><strong>其他属性</strong></th>
			<th><strong>必选</strong></th>
			<th><strong>类型</strong></th>
			<th><strong>描述</strong></th>
		</tr>
		<tr>
			<td>code</td>
			<td>-</td>
			<td>-</td>
			<td>是</td>
			<td>Int</td>
			<td>服务端返回码</td>
		</tr>
		<tr>
			<td>message</td>
			<td>-</td>
			<td>-</td>
			<td>是</td>
			<td>String</td>
			<td>服务端提示内容</td>
		</tr>
		<tr>
			<td rowspan="21">data</td>
			<td>-</td>
			<td>-</td>
			<td>是</td>
			<td>集合</td>
			<td>服务器返回的应答数据</td>
		</tr>
		<tr>
			<td>context</td>
			<td>-</td>
			<td>是</td>
			<td>String</td>
			<td>透传字段，用于翻页，前端不需理解，需要往前/往后翻页则透传回来</td>
		</tr>
		<tr>
			<td>has_more</td>
			<td>-</td>
			<td>是</td>
			<td>Bool</td>
			<td>是否有内容可以继续往前/往后翻页</td>
		</tr>
		<tr>
			<td>dircount</td>
			<td>-</td>
			<td>是</td>
			<td>Int</td>
			<td>子目录数量(总)</td>
		</tr>
		<tr>
			<td>filecount</td>
			<td>-</td>
			<td>是</td>
			<td>Int</td>
			<td>子视频文件数量(总)</td>
		</tr>
		<tr>
			<td rowspan="16">infos</td>
			<td>-</td>
			<td>是</td>
			<td>Array</td>
			<td>可以为空</td>
		</tr>
		<tr>
			<td>name</td>
			<td>是</td>
			<td>String</td>
			<td>视频文件名</td>
		</tr>
		<tr>
			<td>biz_attr</td>
			<td>否</td>
			<td>String</td>
			<td>目录/视频文件属性，业务端维护</td>
		</tr>
		<tr>
			<td>video_cover</td>
			<td>否(当类型为视频文件时返回)</td>
			<td>String</td>
			<td>视频封面的URL</td>
		</tr>
		<tr>
			<td>filesize</td>
			<td>否(当类型为视频文件时返回)</td>
			<td>Int</td>
			<td>视频文件大小</td>
		</tr>
		<tr>
			<td>filelen</td>
			<td>否(当类型为视频文件时返回)</td>
			<td>Int</td>
			<td>文件已传输大小(通过与filesize对比可知文件传输进度)</td>
		</tr>
		<tr>
			<td>sha</td>
			<td>否(当类型为视频文件时返回)</td>
			<td>String</td>
			<td>文件sha</td>
		</tr>
		<tr>
			<td>ctime</td>
			<td>是</td>
			<td>Unix时间戳</td>
			<td>创建时间</td>
		</tr>
		<tr>
			<td>mtime</td>
			<td>是</td>
			<td>Unix时间戳</td>
			<td>修改时间</td>
		</tr>
		<tr>
			<td>access_url</td>
			<td>否(当类型为视频文件时返回)</td>
			<td>String</td>
			<td>生成的资源可访问的url</td>
		</tr>
		<tr>
			<td>trans_status</td>
			<td>否，视频才有，目录没有</td>
			<td>Json</td>
			<td>转码状态，如:</br> {“f10”: 0， “f20”: 1} 等;</br> f10:低清，f20:标清，f30:高清; </br></br>状态码：</br>0，初始化中，</br>1，转码中;</br>2，转码成功;</br>3，转码失败;</td>
		</tr>
		<tr>
			<td>video_status</td>
			<td>否，视频才有，目录没有</td>
			<td>Int</td>
			<td>视频状态码: </br> 0，初始化中，</br>1，视频入库中;</br>2，上传成功;</td>
		</tr>
		<tr>
			<td>video_play_time</td>
			<td>否，视频才有，目录没有</td>
			<td>Int</td>
			<td>视频播放时长，只有转码成功后才有，单位：秒</td>
		</tr>
		<tr>
			<td>video_play_url</td>
			<td>否，视频才有，目录没有</td>
			<td>Array</td>
			<td>各码率的播放url，</br> 如:[“f10”: url1， “f20’: url2] 等;</br> f10:低清，f20:标清，f30:高清</td>
		</tr>
		<tr>
			<td>video_title</td>
			<td>否，视频才有，目录没有</td>
			<td>String</td>
			<td>视频标题</td>
		</tr>		
		<tr>
			<td>video_desc</td>
			<td>否，视频才有，目录没有</td>
			<td>String</td>
			<td>视频描述</td>
		</tr>
	</tbody>
</table>

### 3.6	更新目录/视频信息
功能：在指定路径下更新目录或视频。 接口：web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[DirName]/
web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[DirName]/[filename]
方法： POST
Request Body (json)：

| 参数名称          | 必选   | 类型     | 描述                                       |
| ------------- | ---- | ------ | ---------------------------------------- |
| op            | 否    | String | 操作类型。可以不填，如果要填，固定填”update”               |
| biz_attr      | 否    | String | 目录/视频文件属性，业务端维护                          |
| video_cover   | 否    | String | 视频封面的URL                                 |
| video_title   | 否    | String | 视频才有，目录没有此属性                             |
| video_desc    | 否    | String | 视频才有，目录没有此属性                             |
| Authorization | 是    | String | 单次有效签名，用于鉴权， 具体生成方式详见[鉴权签名方法](https://cloud.tencent.com/document/product/314/2290) |

Response (json)：

| 参数名称    | 必选   | 类型     | 描述      |
| ------- | ---- | ------ | ------- |
| code    | 是    | Int    | 服务端返回码  |
| message | 是    | String | 服务端提示内容 |

### 3.7	查询目录/视频属性信息
功能：查询目录、视频的属性。 接口：web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[DirName]/
web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[DirName]/[filename]
方法：GET
Request Body (query string)：

| 参数名称          | 必选   | 类型     | 描述                                       |
| ------------- | ---- | ------ | ---------------------------------------- |
| op            | 是    | String | 操作类型。固定填”stat”                           |
| Authorization | 是    | String | 多次有效签名，用于鉴权， 具体生成方式详见[鉴权签名方法](https://cloud.tencent.com/document/product/314/2290) |

Response (json)：
<table style="display:table;width:80%;">
	<tbody>
		<tr>
			<th><strong>参数名称</strong></th>
			<th><strong>子属性</strong></th>
			<th><strong>必选</strong></th>
			<th><strong>类型</strong></th>
			<th><strong>描述</strong></th>
		</tr>
		<tr>
			<td>code</td>
			<td>-</td>
			<td>是</td>
			<td>Int</td>
			<td>服务端返回码</td>
		</tr>
		<tr>
			<td>message</td>
			<td>-</td>
			<td>是</td>
			<td>String</td>
			<td>服务端提示内容</td>
		</tr>
		<tr>
			<td rowspan="16">data</td>
			<td>-</td>
			<td>是</td>
			<td>集合</td>
			<td>服务器返回的应答数据</td>
		</tr>
		<tr>
			<td>name</td>
			<td>是</td>
			<td>String</td>
			<td>视频文件名</td>
		</tr>
		<tr>
			<td>biz_attr</td>
			<td>是</td>
			<td>Int</td>
			<td>目录/视频文件属性，业务端维护</td>
		</tr>
		<tr>
			<td>video_cover</td>
			<td>否(当类型为视频文件时返回)</td>
			<td>String</td>
			<td>视频封面的URL</td>
		</tr>
		<tr>
			<td>filesize</td>
			<td>否(当类型为视频文件时返回)</td>
			<td>Int</td>
			<td>视频文件大小</td>
		</tr>
		<tr>
			<td>sha</td>
			<td>否(当类型为视频文件时返回)</td>
			<td>String</td>
			<td>文件sha</td>
		</tr>		
		<tr>
			<td>ctime</td>
			<td>是</td>
			<td>Unix时间戳</td>
			<td>创建时间</td>
		</tr>
		<tr>
			<td>mtime</td>
			<td>是</td>
			<td>Unix时间戳</td>
			<td>修改时间</td>
		</tr>		
		<tr>
		<tr>
			<td>access_url</td>
			<td>否(当类型为视频文件时返回)</td>
			<td>String</td>
			<td>生成的资源可访问的url</td>
		</tr>
		<tr>
			<td>trans_status</td>
			<td>否，视频才有，目录没有</td>
			<td>Json</td>
			<td>转码状态，如:</br> {“f10”: 0， “f20”: 1} 等;</br> f10:低清，f20:标清，f30:高清; </br></br>状态码：</br>0，初始化中，</br>1，转码中;</br>2，转码成功;</br>3，转码失败;</td>
		</tr>
		<tr>
			<td>video_status</td>
			<td>否，视频才有，目录没有</td>
			<td>Int</td>
			<td>视频状态码: </br> 0，初始化中，</br>1，视频入库中;</br>2，上传成功;</td>
		</tr>
		<tr>
			<td>video_play_time</td>
			<td>否，视频才有，目录没有</td>
			<td>Int</td>
			<td>视频播放时长，只有转码成功后才有，单位：秒</td>
		</tr>
		<tr>
			<td>video_play_url</td>
			<td>否，视频才有，目录没有</td>
			<td>Array</td>
			<td>各码率的播放url，</br> 如:[“f10”: url1， “f20’: url2] 等;</br> f10:低清，f20:标清，f30:高清</td>
		</tr>
		<tr>
			<td>video_title</td>
			<td>否，视频才有，目录没有</td>
			<td>String</td>
			<td>视频标题</td>
		</tr>		
		<tr>
			<td>video_desc</td>
			<td>否，视频才有，目录没有</td>
			<td>String</td>
			<td>视频描述</td>
		</tr>
	</tbody>
</table>

### 3.8	删除目录/视频
功能：删除目录或视频，只有空目录才能被删除。 接口：web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[dir_name]/[dir_name]/
web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[dir_name]/[dir_name]/[file_name]
方法：POST
Request Body (json)：

| 参数名称          | 必选   | 类型     | 描述                                       |
| ------------- | ---- | ------ | ---------------------------------------- |
| op            | 是    | String | 操作类型。固定填”delete”                         |
| Authorization | 是    | String | 单次有效签名，用于鉴权， 具体生成方式详见[鉴权签名方法](https://cloud.tencent.com/document/product/314/2290) |

Response (json)：

| 参数名称    | 必选   | 类型     | 描述      |
| ------- | ---- | ------ | ------- |
| code    | 是    | Int    | 服务端返回码  |
| message | 是    | String | 服务端提示内容 |

### 3.9	视频下载
视频下载可以是公开下载，即使用视频的access_url 直接访问即可。
示例：

```

原视频：http://bucketname-10000379.video.myqcloud.com/q.mp4
如果三种规格转码都设置了，URL分别为：
低清：http://bucketname-10000379.video.myqcloud.com/q.mp4.f10.mp4
标清：http://bucketname-10000379.video.myqcloud.com/q.mp4.f20.mp4
高清：http://bucketname-10000379.video.myqcloud.com/q.mp4.f30.mp4
```

若开启了token防盗链（如何开启，详见[token防盗链](https://cloud.tencent.com/document/product/314/3496)）。
视频下载只能是私密下载，即必须access_url +?sign=[签名]。转码后的视频防盗链规则一样。
示例：

```
http://bucketname-10000379.video.myqcloud.com/q.mp4?sign=
GonmF5K4ehldbFpHASHbZo+DC6xhPTI5OTIwMSZrPUFLSURBc3FqSDM1QW9KTm16akIzbGZWVUlITERNQjE4Y1hHOCZlPT
E0MzMxNDU2MDAmdD0xNDI4NTcwMDMxJnI9MjkzODI3MTE2JnU9JmY9
```

## 4	音视频转码相关

## 描述

- 本文档用于腾讯云CDN转码服务结果查询和回调

- 请求域名：cdn.api.cloud.tencent.com

- 请求方式：POST 或者GET

- 签名方法：https://cloud.tencent.com/document/product/228/1725

- SDK： https://github.com/QCloudCDN/CDN_API_SDK/tree/master/Qcloud_CDN_API

- secretKey和secretId：https://console.cloud.tencent.com/capi


## 4.1	视频转码结果查询接口(GetCtsInfo)

### 功能描述

本接口用于查询视频转码任务结果

### 请求参数

| 参数名称 | 必选   | 类型     | 说明    |
| ---- | ---- | ------ | ----- |
| vid  | 否    | String | 视频的ID，vid获取规则参见4.6内容说明 |
| url  | 否    | String | 转码URL |

### 输出参数

| 名称      | 类型     | 说明              |
| ------- | ------ | --------------- |
| code    | Int    | 错误码，0：成功；其他值：失败 |
| message | String | 错误信息            |
| data    | 对象    | 结果数据，详细说明见下文    |

#### data字段说明

| 名称          | 类型     | 说明                |
| ----------- | ------ | ----------------- |
| vid         | String | 视频ID              |
| app_id      | Int    | 用户app_id          |
| bucket_name | String | cos bucket名       |
| name        | String | 视频名               |
| size        | Int    | 视频大小              |
| duration    | Int    | 视频时长              |
| height      | Int    | 视频高度              |
| width       | Int    | 视频宽度              |
| bitrate     | Int    | 视频码率              |
| create_time | String | 转码任务创建时间          |
| update_time | String | 转码任务更新时间          |
| url         | String | 视频文件的原始URL        |
| url_f0      | String | 视频文件的原始路径         |
| v_type      | String | 视频文件类型            |
| bucket_region     | String | 存储地区              |
| status      | Int    | 1：待处理， 2：已获取视频基本信息 ，3：转码中 ，4：转码失败 ，5：转码成功 |
| error_code  | Int    | 转码错误码             |
| error_msg   | String | 转码错误描述            |
| deleted     | String | yes表示任务删除，no表示未删除 |
| result      | Array  | 转码成功后的文件信息,详细说明见下文  |

#### result 字段说明 

| 名称    | 类型    | 说明                      |
| ----- | ----- | ----------------------- |
| video | Array | 转码后视频的相关信息,包含dst和info字段 |
| gif   | Array | gif的相关信息,包含dst和info字段   |
| cover | Array | 截图相关信息，包含dst和info字段     |
| dst   | Array | 转码后的存储信息                |

#### video 中info字段说明

| 名称         | 类型     | 说明               |
| ---------- | ------ | ---------------- |
| width      | Int    | 转码后视频宽度          |
| name       | Array  | 规格名称             |
| fps        | Array  | 帧率               |
| path       | String | 转码后的存储路径         |
| bitrate    | Array  | 转码后的码率           |
| height     | Array  | 转码后视频高度          |
| trans_size | Int    | 转码后的视频大小(m3u8为0) |

#### gif 中info字段说明

| 名称     | 类型     | 说明       |
| ------ | ------ | -------- |
| width  | Int    | 截图宽度     |
| path   | String | 转码后的存储路径 |
| name   | Array  | 规格名称     |
| height | Array  | 转码后视频高度  |

#### cover 中info字段说明

| 名称     | 类型    | 说明      |
| ------ | ----- | ------- |
| width  | Int   | 截图宽度    |
| path   | Array | 截图的存储路径 |
| count  | Array | 截图数     |
| name   | Array | 规格名称    |
| height | Array | 转码后视频高度 |

#### 备注说明

- 当同一个文件重复提交时，会将之前提交的任务标记为删除。
- 转码结果字段result与具体的配置有关，其中gif和cover可能不存在。
- dst 字段为转码后的存储信息，可配置，默认为原视频的信息。

#### 转码及截图规格说明

| 规格   | 类型   | 说明                                |
| ---- | ---- | --------------------------------- |
| f10  | 视频   | 流畅 270p                           |
| f20  | 视频   | 标清 480p                           |
| f30  | 视频   | 高清 720p                           |
| f40  | 视频   | 超清 1080p                          |
| s_x  | 截图   | 短边配置，x表示短边大小,例如s_270              |
| l_x  | 截图   | 长边配置，x表示长边大小,例如l_1920             |
| w_x  | 截图   | 指定宽度，x表示宽度,实际高度根据原尺寸等比缩放，例如w_1920 |
| h_x  | 截图   | 指定高度，x表示高度,实际宽度根据原尺寸等比缩放，例如h_1080 |
| 0_0  | 截图   | 视频原尺寸,例如1920_1080                 |
| x_y  | 截图   | 指定宽度和高度,例如400_200                 |

### 请求示例

```shell
https://cdn.api.cloud.tencent.com/v2/index.php?Action=GetCtsInfo&SecretId=AKIDxUCsd01oB7BxxxxxxFihD8hlRhftKmXr&Nonce=44207&Timestamp=1480384094&Region=gz&vid=000628c22a4cfa9daac321c31d496393&Signature=njTouxSxxxxxxPjeGKr0ZG%2Fi%2FE%3D
```

### 回包示例

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "vid": "963f1d40dfdfadfdd9b94e922d5696",
        "app_id": 1233444,
        "bucket_name": "cts",
        "bucket_region": "sh",
        "name": "/1233444/cts/test/w.mp4",
        "url": "http://cts-1233444.cossh.myqcloud.com/test/w.mp4",
        "url_f0": "/test/w.mp4",
        "size": 322960391,
        "duration": 600,
        "bitrate": 4205,
        "width": 1920,
        "height": 1080,
        "v_type": "mov,mp4,m4a,3gp,3g2,mj2",
        "create_time": "2016-12-23 21:11:42",
        "update_time": "2016-12-26 10:12:56",
        "status": 5,
        "error_code": null,
        "error_msg": null,
        "deleted": "no",
        "result": {
            "video": {
                "info": [
                    {
                        "bitrate": 300,
                        "width": 480,
                        "height": 270,
                        "fps": 25,
                        "path": "/test/w.mp4.f10.mp4",
                        "name": "f10",
                        "trans_size":100000
                        
                    },
                    {
                        "bitrate": 600,
                        "width": 852,
                        "height": 480,
                        "fps": 25,
                        "path": "/test/w.mp4.f20.mp4",
                        "name": "f20",
                        "trans_size":200000,
                    },
                    {
                        "bitrate": 1200,
                        "width": 1280,
                        "height": 720,
                        "fps": 25,
                        "path": "/test/w.mp4.f30.mp4",
                        "name": "f30",
                        "trans_size":100000
                    },
                    {
                        "bitrate": 2400,
                        "width": 1920,
                        "height": 1080,
                        "fps": 25,
                        "path": "/test/w.mp4.f40.mp4",
                        "name": "f40",
                        "trans_size":100000
                    }
                ],
                "dst": {
                    "app_id": 10033619,
                    "bucket_name": "cts",
                    "bucket_region": "sh"
                }
            },
            "gif": {
                "info": [
                    {
                        "height": 1080,
                        "width": 1920,
                        "path": "/test/w.mp4.0_0.gif",
                        "name": "0_0"
                    },
                    {
                        "height": 200,
                        "width": 400,
                        "path": "/test/w.mp4.400_200.gif",
                        "name": "400_200"
                    }
                ],
                "dst": {
                    "app_id": 10033619,
                    "bucket_name": "cts",
                    "bucket_region": "sh"
                }
            },
            "cover": {
                "info": [
                    {
                        "height": 1080,
                        "width": 1920,
                        "count": 5,
                        "path": [
                            "/test/w.mp4.0_0.p0.png",
                            "/test/w.mp4.0_0.p1.png",
                            "/test/w.mp4.0_0.p2.png",
                            "/test/w.mp4.0_0.p3.png",
                            "/test/w.mp4.0_0.p4.png"
                        ],
                        "name": "0_0"
                    },
                    {
                        "height": 200,
                        "width": 400,
                        "count": 2,
                        "path": [
                            "/test/w.mp4.400_200.p0.png",
                            "/test/w.mp4.400_200.p1.png"
                        ],
                        "name": "400_200"
                    }
                ],
                "dst": {
                    "app_id": 10033619,
                    "bucket_name": "cts",
                    "bucket_region": "sh"
                }
            }
        }
    }
}
```

### 4.2	视频转码回调

### 功能描述

回调接口实时将转码的结果详情回传给用户，需要用户配置回调地址。

### 回调方式

回调域名：需用户提供

回调方式：HTTP POST 请求

### 回调格式说明

#### 4.2.1 转码开始时基本信息回调

- 参数说明

| 名称            | 类型     | 说明 |
| ------------- | ------ | ------------------------- |
| status        | String  |  success：成功，fail：失败 |
| vid           | String | 视频ID                      |
| app_id        | Int    | 用户app_id      |
| bucket_name   | String | cos bucket名               |
| bucket_region | String | cos地区                     |
| create_time   | String | 转码任务创建时间                  |
| url           | String | 视频文件的原始URL                |
| v_type        | String | 视频文件类型                    |
| size     | Int   | 视频大小                 |
| duration | Int   | 视频时长                 |
| height   | Int   | 视频高度                 |
| width    | Int   | 视频宽度                 |
| bitrate  | Int   | 视频码率                 |
| fps  | Int   | 视频帧率                 |
| rotation | Int   | 视频方向，horizon ：水平 vertical：垂直|
|HasVideoStream | Int |是否有视频流，1：有；0：没有     |
|HasAudioStream | Int |是否有音频流，1：有；0：没有     |
|callback_type |String | 回调类型，需配置；trans_basic：转码开始时基本信息回调；trans_result：转码完成结果回调 |
|fail_msg | String  | 失败信息描述 |

- 回调成功示例
```
{
    "vid":"4e4d4cb91b14be1faca76aecad5cd28c1519806353",
    "app_id":12xxxxxxxx,
    "bucket_name":"test",
    "bucket_region":"sh",
    "url":"http://test-12xxxxxxxx.cossh.myqcloud.com/dragons.mp4",
    "size":39909209,
    "duration":31,
    "width":3840,
    "height":2032,
    "v_type":"mov,mp4,m4a,3gp,3g2,mj2",
    "create_time":"2018-02-28 16:25:54",
    "bitrate":10260,
    "fps":24,
    "rotation":"horizon",
    "HasVideoStream":1,
    "HasAudioStream":1,
    "status":"success",
    "callback_type":"trans_basic",
    "fail_msg":""
}
```
- 回调失败示例

```
{
    "vid":"7d6cec782335ff8c9d332daf7c0fda1f1519803613",
    "app_id":12xxxxxxxx,
    "bucket_name":"test",
    "bucket_region":"sh",
    "url":"http://tesdfdfd-12xxxxxxxx.cossh.myqcloud.com/x.mov",
    "size":0,
    "duration":0,
    "width":0,
    "height":0,
    "v_type":"",
    "create_time":"2018-02-28 15:40:14",
    "bitrate":0,
    "fps":0,
    "rotation":"",
    "HasVideoStream":0,
    "HasAudioStream":0,
    "status":"fail",
    "fail_msg":"AVC文件不存在或者文件内容有误，无法识别和处理"
}
```

####  4.2.2 转码成功完成时回调

- 参数说明

| 名称            | 类型     | 说明                        |
| ------------- | ------ | ------------------------- |
| status        | String | success：转码成功，fail：转码失败 |
| vid           | String | 视频ID                      |
| detail        | Array  | 详情，见下文详细说明                        |
| bucket_name   | String | cos bucket名               |
| bucket_region | String | cos地区                     |
| create_time   | String | 转码任务创建时间                  |
| app_id        | Int    | 用户app_id                  |
| url           | String | 视频文件的原始URL                |
| url_f0        | String | 视频文件的原始路径                 |
| v_type        | String | 视频文件类型                    |
|callback_type |String | 回调类型，需配置；trans_basic：转码开始时基本信息回调；trans_result：转码完成结果回调 |

- detail 说明

| 名称       | 类型    | 说明                   |
| -------- | ----- | -------------------- |
| size     | Int   | 视频大小                 |
| duration | Int   | 视频时长                 |
| height   | Int   | 视频高度                 |
| width    | Int   | 视频宽度                 |
| bitrate  | Int   | 视频码率                 |
| result   | Array | 转码后的结果，详情见GetCtsInfo |

- 示例

```
{
    "status":"success",
    "url_f0":"/test/w.mp4",
    "v_type":"mov,mp4,m4a,3gp,3g2,mj2",
    "name":"/123456/cts/test/w.mp4",
    "vid":"963f1d4048dfdfad362d9b94e922d5696",
    "url":"http://cts-123456.cossh.myqcloud.com/test/w.mp4",
    "callback_type":"trans_result"
    "detail":{
        "height":1080,
        "width":1920,
        "result":{
            "gif":{
                "info":[
                    {
                        "path":"/test/w.mp4.0_0.gif",
                        "width":1920,
                        "name":"0_0",
                        "height":1080
                    },
                    {
                        "path":"/test/w.mp4.400_200.gif",
                        "width":400,
                        "name":"400_200",
                        "height":200
                    }
                ],
                "dst":{
                    "bucket_name":"cts",
                    "bucket_region":"sh",
                    "app_id":123456
                }
            },
            "video":{
                "info":[
                    {
                        "width":480,
                        "name":"f10",
                        "fps":25,
                        "path":"/test/w.mp4.f10.mp4",
                        "bitrate":300,
                        "height":270,
                        "trans_size":100000
                    },
                    {
                        "width":852,
                        "name":"f20",
                        "fps":25,
                        "path":"/test/w.mp4.f20.mp4",
                        "bitrate":600,
                        "height":480,
                        "trans_size":100000
                    },
                    {
                        "width":1280,
                        "name":"f30",
                        "fps":25,
                        "path":"/test/w.mp4.f30.mp4",
                        "bitrate":1200,
                        "height":720,
                        "trans_size":100000
                    },
                    {
                        "width":1920,
                        "name":"f40",
                        "fps":25,
                        "path":"/test/w.mp4.f40.mp4",
                        "bitrate":2400,
                        "height":1080,
                        "trans_size":100000
                    }
                ],
                "dst":{
                    "bucket_name":"cts",
                    "bucket_region":"sh",
                    "app_id":123456
                }
            },
            "cover":{
                "info":[
                    {
                        "count":5,
                        "path":[
                            "/test/w.mp4.0_0.p0.png",
                            "/test/w.mp4.0_0.p1.png",
                            "/test/w.mp4.0_0.p2.png",
                            "/test/w.mp4.0_0.p3.png",
                            "/test/w.mp4.0_0.p4.png"
                        ],
                        "width":1920,
                        "name":"0_0",
                        "height":1080
                    },
                    {
                        "count":2,
                        "path":[
                            "/test/w.mp4.400_200.p0.png",
                            "/test/w.mp4.400_200.p1.png"
                        ],
                        "width":400,
                        "name":"400_200",
                        "height":200
                    }
                ],
                "dst":{
                    "bucket_name":"cts",
                    "bucket_region":"sh",
                    "app_id":123456
                }
            }
        },
        "duration":600,
        "bitrate":4205,
        "size":322960391
    },
    "app_id":123456,
    "create_time":"2016-12-23 21:11:42",
    "bucket_name":"cts",
    "bucket_region":"sh"
}
```

#### 4.2.3 转码失败时回调

- 参数说明

| 名称            | 类型     | 说明                        |
| ------------- | ------ | ------------------------- |
| status        | String | success：转码成功，fail：转码失败 |
| vid           | String | 视频ID                      |
| detail        | Array  | 详情，见下文详细说明                        |
| bucket_name   | String | cos bucket名               |
| bucket_region | String | cos地区                     |
| create_time   | String | 转码任务创建时间                  |
| app_id        | Int    | 用户app_id                  |
| url           | String | 视频文件的原始URL                |
| url_f0        | String | 视频文件的原始路径                 |
| v_type        | String | 视频文件类型                    |


- detail说明

| 名称       | 类型    | 说明                   |
| -------- | ----- | -------------------- |
| error_code    | Array   | 转码错误码   |
| error_msg | Array    | 错误码描述，与error_code一一对应  |


- 示例

```
{
    "status":"fail",   			 		   
  "url_f0":"/flash/mp4video56/TMS/2016/12/13/27a33649a97b4c3481b609f2be925b7d_h264418000nero_aac32-4.mp4",
  "name":"/10032344/cts/flash/mp4video56/TMS/2016/12/13/27a33649a97b4c3481b609f2be925b7d_h264418000nero_aac32-4.mp4",
    "vid":"7d70b89fdf72ee6b98dcc0b0211",
    "url":"http://cts-10032344.cossh.myqcloud.com/flash/mp4video56/TMS/2016/12/13/27a33649a97b4c3481b609f2be925b7d_h264418000nero_aac32-4.mp4",
    "detail":{
        "error_code":[
            122,
        ],
        "error_msg":[
            "回调Gif提交接口调用失败",
        ]
    },
    "app_id":123456,
    "create_time":"2016-12-15 14:31:46",
    "bucket_name":"cts",
    "bucket_region":"sh"
}
```

### 4.3	音频转码结果查询接口(GetCtsaudioInfo)

### 功能描述

查询音频转码任务结果

### 请求参数

| 参数名称 | 必选   | 类型     | 说明    |
| ---- | ---- | ------ | ----- |
| vid  | 否    | String | 音频的ID |

### 输出参数

| 名称      | 类型     | 说明              |
| ------- | ------ | --------------- |
| code    | Int    | 错误码，0：成功，其他值：失败 |
| message | String | 错误信息            |
| data    | 对象     | 结果数据，详细说明见下文    |

#### data字段说明

| 名称          | 类型     | 说明                |
| ----------- | ------ | ----------------- |
| vid         | String | 音频ID              |
| app_id      | Int    | 用户app_id          |
| bucket_name | String | cos bucket名       |
| name        | String | 音频名               |
| size        | Int    | 音频大小              |
| duration    | Int    | 音频时长              |
| format      | String | 音频格式              |
| sample_rate | 采样率    | 采样率               |
| bitrate     | Int    | 音频bitrate（kbps）   |
| create_time | String | 转码任务创建时间          |
| update_time | String | 转码任务更新时间          |
| url         | String | 音频文件的原始URL        |
| url_f0      | String | 音频文件的原始路径         |
| v_type      | String | 音频文件类型            |
| bucket_region   | String | 存储地区              |
| status      | Int    | 详细说明见备注           |
| error_code  | Int    | 转码错误码             |
| error_msg   | String | 转码错误描述            |
| deleted     | String | yes表示任务删除，no表示未删除 |
| result      | Array  | 转码成功后的信息,详细说明见下文  |

#### result 字段说明

| 名称    | 类型    | 说明                      |
| ----- | ----- | ----------------------- |
| audio | Array | 转码后音频的相关信息,包含dst和info字段 |
| dst   | Array | 转码后的存储信息                |

#### video 中info字段说明

| 名称          | 类型     | 说明                 |
| ----------- | ------ | ------------------ |
| bitrate     | Int    | 比特率,其中ape flac格式为0 |
| name        | Array  | 规格名称               |
| sample_rate | Array  | 采样率                |
| path        | String | 转码后的存储路径           |
| format      | String | 格式                 |
| encoder     | String | 编码器                |
| trans_size  | Int    | 转码后的音频大小           |

#### 备注

- status 状态：1.待处理 2.已获取音频基本信息 3.转码中 4.转码失败 5.转码成功
- 当同一个文件重复提交时，会将之前提交的任务标记为删除。
- 转码结果字段result与具体的配置有关，其中gif和cover可能不存在。
- dst 字段为转码后的存储信息，可配置，默认为原音频的信息。

#### 转码规格说明

| 规格   | 类型   | 说明            |
| ---- | ---- | ------------- |
| x_y  | 音频   | 其中x表示码率，y表示格式 |

###  请求示例

```shell
https://cdn.api.cloud.tencent.com/v2/index.php?Action=GetCtsaudioInfo&SecretId=AKIDxUCsd01oB7BxxxxxxFihD8hlRhftKmXr&Nonce=44207&Timestamp=1480384094&Region=gz&vid=000628c22a4cfa9daac321c31d496393&Signature=njTouxSxxxxxxPjeGKr0ZG%2Fi%2FE%3D
```

###  回包示例

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "vid": "6e50fd43c6f20d56c88d1c1d8f6db2641503390019",
        "app_id": 1253125191,
        "bucket_name": "onlinemusic",
        "bucket_region": "gz",
        "name": "/1253125191/onlinemusic/20170717/Maid.mp3",
        "url": "http://onlinemusic-1253125191.cosgz.myqcloud.com/20170717/Maid.mp3",
        "url_f0": "/20170717/Maid.mp3",
        "size": 4113874,
        "duration": 170,
        "bitrate": 187,
        "format": "mp3",
        "sample_rate": 44100,
        "encoder": "mp3",
        "create_time": "2017-08-22 16:20:19",
        "update_time": "2017-08-22 16:21:02",
        "status": 5,
        "error_code": null,
        "error_msg": null,
        "deleted": "no",
        "result": {
            "audio": {
                "info": [
                    {
                        "bitrate": 191488,
                        "sample_rate": 44100,
                        "format": "mp3",
                        "encoder": "lame",
                        "path": "/20170717/Maid.mp3.191488_mp3.mp3",
                        "name": "191488_mp3",
                        "trans_size": 4264747
                    }
                ],
                "dst": {
                    "app_id": 1253125191,
                    "bucket_name": "onlinemusic",
                    "bucket_region": "gz"
                }
            }
        }
    }
}
```

### 4.4	音频转码完成回调

### 功能描述

回调用户实时将完成的转码结果详情回传给用户，需要用户配置回调地址。

### 回调方式

回调域名：需用户提供
回调方式：HTTP POST 请求

### 回调格式说明

#### 转码成功

- 参数说明

| 名称            | 类型     | 说明                        |
| ------------- | ------ | ------------------------- |
| status        | String | success 表示转码成功，fail表示转码失败 |
| vid           | String | 音频ID                      |
| detail        | Array  | 详情                        |
| bucket_name   | String | cos bucket名               |
| bucket_region | String | cos地区                     |
| create_time   | String | 转码任务创建时间                  |
| app_id        | Int    | 用户app_id                  |
| url           | String | 音频文件的原始URL                |
| url_f0        | String | 音频文件的原始路径                 |



- detail 说明

| 名称          | 类型     | 说明                        |
| ----------- | ------ | ------------------------- |
| encoder     | String | 编码器                       |
| duration    | Int    | 音频时长                      |
| sample_rate | Int    | 采样率                       |
| bitrate     | Int    | 音频大小                      |
| result      | Array  | 转码后的结果，详情见GetCtsaudioInfo |

- 示例

```
    
{
    "status":"success",
    "url_f0":"/20170428/strength.mp3",
    "name":"/1253125191/onlinemusic/20170428/strength.mp3",
    "vid":"e5fea7f66851b7176b8c89c254d0a11b1493379478",
    "url":"http://onlinemusic-1253125191.cosgz.myqcloud.com/20170428/strength.mp3",
    "detail":{
        "encoder":"mp3",
        "sample_rate":48000,
        "result":{
            "audio":{
                "info":[
                    {
                        "sample_rate":44100,
                        "format":"ape",
                        "trans_size":16889420,
                        "path":"/20170428/strength.mp3.0_ape.ape",
                        "bitrate":0,
                        "trans_name":"0_ape",
                        "encoder":"ape"
                    },
                    {
                        "sample_rate":44100,
                        "format":"flac",
                        "trans_size":16843751,
                        "path":"/20170428/strength.mp3.0_flac.flac",
                        "bitrate":0,
                        "trans_name":"0_flac",
                        "encoder":"flac"
                    },
                    {
                        "sample_rate":44100,
                        "format":"mp3",
                        "trans_size":2664306,
                        "path":"/20170428/strength.mp3.128000_mp3.mp3",
                        "bitrate":128000,
                        "trans_name":"128000_mp3",
                        "encoder":"libmp3lame"
                    },
                    {
                        "sample_rate":44100,
                        "format":"m4a",
                        "trans_size":453401,
                        "path":"/20170428/strength.mp3.24000_m4a.m4a",
                        "bitrate":24000,
                        "trans_name":"24000_m4a",
                        "encoder":"fdk_aac"
                    },
                    {
                        "sample_rate":44100,
                        "format":"mp3",
                        "trans_size":984842,
                        "path":"/20170428/strength.mp3.24000_mp3.mp3",
                        "bitrate":24000,
                        "trans_name":"24000_mp3",
                        "encoder":"libmp3lame"
                    },
                    {
                        "sample_rate":44100,
                        "format":"m4a",
                        "trans_size":872852,
                        "path":"/20170428/strength.mp3.48000_m4a.m4a",
                        "bitrate":48000,
                        "trans_name":"48000_m4a",
                        "encoder":"fdk_aac"
                    },
                    {
                        "sample_rate":44100,
                        "format":"mp3",
                        "trans_size":1264718,
                        "path":"/20170428/strength.mp3.48000_mp3.mp3",
                        "bitrate":48000,
                        "trans_name":"48000_mp3",
                        "encoder":"libmp3lame"
                    }
                ],
                "dst":{
                    "bucket_name":"onlinemusic",
                    "bucket_region":"gz",
                    "app_id":1253125191
                }
            }
        },
        "duration":140,
        "bitrate":312,
        "size":5641493
    },
    "app_id":1253125191,
    "create_time":"2017-04-28 19:37:58",
    "bucket_name":"onlinemusic",
    "bucket_region":"gz"
}
```

#### 转码失败

- 参数说明

| 名称            | 类型     | 说明                        |
| ------------- | ------ | ------------------------- |
| status        | String | success 表示转码成功，fail表示转码失败 |
| vid           | String | 音频ID                      |
| detail        | Array  | 详情                        |
| bucket_name   | String | cos bucket名               |
| bucket_region | String | cos地区                     |
| create_time   | String | 转码任务创建时间                  |
| app_id        | Int    | 用户app_id                  |
| url           | String | 音频文件的原始URL                |
| url_f0        | String | 音频文件的原始路径                 |

- detail 说明

| 名称         | 类型    | 说明                   |
| ---------- | ----- | -------------------- |
| error_code | Array | 转码错误码                |
| error_msg  | Array | 错误码描述与error_code一一对应 |

### 4.5	增加音频转码任务(AddCtsAudioTask)

### 功能描述

增加音频转码任务

### 请求参数

| 参数名称         | 必选   | 类型     | 说明          |
| ------------ | ---- | ------ | ----------- |
| bucketRegion | 是    | String | 地域          |
| url          | 是    | String | 转码音频完整cos路径 |
| bucketName   | 是    | String | bucket名     |

### 输出参数

| 名称      | 类型     | 说明              |
| ------- | ------ | --------------- |
| code    | Int    | 错误码，0：成功，其他值：失败 |
| message | String | 错误信息            |
| data    | 对象     | 结果数据，详细说明见下文    |

#### data字段说明

| 名称   | 类型     | 说明     |
| ---- | ------ | ------ |
| vid  | String | 音频唯一ID |

### 请求示例

```
https://cdn.api.cloud.tencent.com/v2/index.php?Action=AddCtsAudioTask&SecretId=1&Nonce=47825&Timestamp=1503372336&Region=sh&Uin=2418826573&AppId=1253125191&url=http%3A%2F%2Fonlinemusic-1253125191.cosgz.myqcloud.com%2F20170717%2FMaid.mp3&bucketName=onlinemusic&bucketRegion=gz&Signature=LXe8bGz%2BSULUuCo1XF8PjzxT1fI%3D
```

### 回包示例

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "vid": "5ba52a3a31688f83571c34de9dd44f6c1503372336"
    }
}
```


### 4.6	vid获取规则说明

#### 情况一：使用cos v4 API进行视频文件上传

使用cos v4 API进行视频文件上传的用户，在上传文件后的回包中，直接包含有vid信息，用户可直接记录该vid与源文件映射关系即可。

- cos v4 API 上传文件后回包示例：

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: 321
Connection: keep-alive
Date: Tue, 12 Sep 2017 07:36:45 GMT
Server: tencent-cos
x-cos-request-id: NTliNzhlOGRfMTliMjk0MGFfNDg0N18xMTdiY2E=

{
"code":0,
"message":"SUCCESS",
"request_id":"NTllOWQ2YjVfYzlhMzNiMGFfMTY0OV9jMzYwZTU=",
"data":
     {
    "access_url":"http://xy2-124566667.file.myqcloud.com/uploader1500000000",
    "resource_path":"/124566667/xy2/uploader1508497108630",
    "source_url":"http://xy2-124566667.cosgz.myqcloud.com/uploader1500000000",
    "url":"http://gz.file.myqcloud.com/files/v2/124566667/xy2/uploader1500000000",
    "vid":"4396314caa204d61f5d070d45248d9981508497077"
     }
}
```


#### 情况二、使用cos v5 API进行视频文件上传

由于cos v5 API升级改版，用户使用新版cos v5 API进行视频文件上传后，回包中将不再包含vid信息，用户需要根据v5回包中的```x-cos-request-id```及```date```信息进行计算后，记录vid信息与源文件的映射关系，具体映射规则如下：

- cos v5 API 上传文件后回包示例：

```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Mon, 26 Feb 2018 08:25:37 GMT 
ETag: "15c7565b15676b5f35ef85615c04dc19"
Server: tencent-cos
x-cos-request-id: NWE5M2M0N2ZfZDBhMDY4NjRfMWNhZmZfODE4OTEy
```
- 则：

vid= md5(x-cos-request-id) + strtotime(Date)

其中，strtotime 表示把回包中的Date 在东八区下转换成时间戳格式。
**注意**：vid中不包含+符号，如上示例中vid最终计算结果为：vid=421e6d34756e53814c99939ffeec49861519633537

#### 备注说明：

- cos中的bucket不区分v4、v5版本，即cos v4版本创建的bucket，也可使用v5版本API进行上传；同理，cos v5版本创建的bucket，也可使用v4版本API进行上传。
- 更多cos API详细信息，请参见[cos API产品手册](https://cloud.tencent.com/document/product/436/7751) 




