## 1	基本概念

| 概念 | 解释 |
|---------|---------|
| appid | 接入微视频时,生成为唯一id, 用于唯一标识接入业务, 获取地址: 密钥配置 |
| Authorization | 签名，具体生成参见[鉴权签名方法](http://www.qcloud.com/doc/product/314/%E9%89%B4%E6%9D%83%E5%8F%8A%E7%AD%BE%E5%90%8D%E6%96%87%E6%A1%A3). |
| bucket_name | bucket名称，bucket创建参见[创建Bucket](http://console.qcloud.com/uvs/vbucket) |

## 2	鉴权
腾讯云•微视频通过签名来验证请求的合法性。开发者通过将签名授权给客户端，使其具备上传下载及管理指定资源的能力。

签名分为单次签名和多次签名, 区别为: 如果针对资源进行写操作(资源删除), 那么这个签名必须是单次有效的.重复使用该签名则会返回签名失败.如果是上传或下载资源,签名必须是多次有效的.有效时长最多为三个月。

开发者可以通过[服务器SDK文档](http://www.qcloud.com/wiki/%E5%BE%AE%E8%A7%86%E9%A2%91SDK%E6%96%87%E6%A1%A3)生成签名，也可以参考我们的签名函数自行生成签名，具体生成方式详见[鉴权签名方法](http://www.qcloud.com/doc/product/314/SDK%E4%B8%8B%E8%BD%BD)。

## 3	目录操作
### 3.1	创建目录
功能: 在指定路径下创建目录。 接口:web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[dirName]/ <font color="red"><- 有文件夹斜杠 /</font>
要求: 父目录存在
方法: POST
请求参数HTTP头部信息:

| 参数名称 | 必选 | 类型 | 描述 | 
|---------|---------|---------|---------|
| Host | 是 | String | 微视频服务器域名，固定为web.video.myqcloud.com | 
| Content-Type | 是 | String | application/json | 
| Authorization | 是 | String | 多次有效签名,用于鉴权， 具体生成方式详见[鉴权签名方法](http://www.qcloud.com/wiki/%E5%BE%AE%E8%A7%86%E9%A2%91%E9%89%B4%E6%9D%83%E5%8F%8A%E7%AD%BE%E5%90%8D%E6%96%87%E6%A1%A3) | 

请求包体 (json):

| 参数名称 | 必选 | 类型 | 描述 | 
|---------|---------|---------|---------|
| op | 是 | String | 操作类型.固定填”create” | 
| biz_attr | 否 | String | 目录属性，业务端维护 | 

返回包体(json):
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
			<td>资源路径. 不包含/[appid]/[bucket_name]</td>
		</tr>
	</tbody>
</table>

### 3.2	创建视频:(完整上传)
功能: 在指定路径下创建视频。 接口:web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[DirName]/[file_name] <font color="red"> <- 没有文件夹斜杠 / </font>
方法: POST
请求参数HTTP头部信息:

| 参数名称 | 必选 | 类型 | 描述 | 
|---------|---------|---------|---------|
| Content-Length | 是 | Int | 整个multipart/form-data内容的总长度，单位：字节（Byte） | 
| Content-Type | 是 | String | 固定为multipart/form-data | 
| Authorization | 是 | String | 多次有效签名,用于鉴权， 具体生成方式详见[鉴权签名方法](http://www.qcloud.com/doc/product/314/%E9%89%B4%E6%9D%83%E5%8F%8A%E7%AD%BE%E5%90%8D%E6%96%87%E6%A1%A3) | 

请求包体信息 (multipart/form-data):

| 参数名称 | 必选 | 类型 | 描述 | 
|---------|---------|---------|---------|
| op | 是 | String | 固定填upload | 
| filecontent | 是 | Binary | 视频文件内容 | 
| sha | 否 | String | 视频文件的sha值 | 
| biz_attr | 否 | String | 文件属性，业务端维护 | 
| video_cover | 否 | String | 视频封面的URL | 
| video_title | 否 | String | 视频标题 | 
| video_desc | 否 | String | 视频描述 | 
| magicContext | 否 | String | 转码成功后,用于透传回调用者的业务后台 | 

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
			<td>资源路径. 不包含/[appid]/[bucket_name]</td>
		</tr>
	</tbody>
</table>

### 3.3	创建视频:(分片上传, 第一片)
功能: 在指定路径下创建视频。 接口:web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[DirName]/[file_name] <font color="red"> <- 没有文件夹斜杠 / </font>
方法: POST
请求参数HTTP头部信息:

| 参数名称 | 必选 | 类型 | 描述 | 
|---------|---------|---------|---------|
| Content-Length | 是 | Int | 整个multipart/form-data内容的总长度，单位：字节（Byte） | 
| Content-Type | 是 | String | 固定为multipart/form-data | 
| Authorization | 是 | String | 多次有效签名,用于鉴权， 具体生成方式详见[鉴权签名方法](http://www.qcloud.com/doc/product/314/%E9%89%B4%E6%9D%83%E5%8F%8A%E7%AD%BE%E5%90%8D%E6%96%87%E6%A1%A3) | 

请求包体信息 (multipart/form-data):

| 参数名称 | 必选 | 类型 | 描述 | 
|---------|---------|---------|---------|
| op | 是 | String | 固定填upload_slice | 
| filesize | 是 | Int 64 | 视频文件总大小 | 
| sha | 否 | String | 文件的sha值,必须提供 | 
| biz_attr | 否 | String | 视频属性，业务端维护 | 
| video_cover | 否 | String | 视频封面的URL | 
| session | 否 | String | 如果想要断点续传,则带上上一次的session id | 
| video_title | 否 | String | 视频标题 | 
| video_desc | 否 | String | 视频描述 | 
| magicContext | 否 | String | 转码成功后,用于透传回调用者的业务后台 | 

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
			<td>资源路径. 不包含/[appid]/[bucket_name]</td>
		</tr>
	</tbody>
</table>

### 3.4	创建视频:(分片上传, 后续分片)
功能: 在指定路径下创建视频。 接口:web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[DirName]/[file_name] <font color="red"><- 有文件夹斜杠 /</font>
方法: POST
请求参数HTTP头部信息:

| 参数名称 | 必选 | 类型 | 描述 | 
|---------|---------|---------|---------|
| Content-Length | 是 | Int | 整个multipart/form-data内容的总长度，单位：字节（Byte） | 
| Content-Type | 是 | String | 固定为multipart/form-data | 
| Authorization | 是 | String | 多次有效签名,用于鉴权， 具体生成方式详见[鉴权签名方法](http://www.qcloud.com/doc/product/314/%E9%89%B4%E6%9D%83%E5%8F%8A%E7%AD%BE%E5%90%8D%E6%96%87%E6%A1%A3) | 

请求包体信息 (multipart/form-data):

| 参数名称 | 必选 | 类型 | 描述 | 
|---------|---------|---------|---------|
| op | 是 | String | 固定填upload_slice | 
| filecontent | 是 | Binary | 视频文件内容 | 
| sha | 否 | String | 本次文件分片的sha值,可以提供用于校验(暂时未启用) | 
| session | 是 | String | 唯一标识此视频文件传输过程的id, 由后台下发, 调用方透传 | 
| offset | 是| Int 64 | 本次分片位移 | 


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
			<td>请求包体里的传输的位移,调用方如果用多线程等方式传输,可以用来唯一确定本次分片结果</td>
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
			<td>资源路径. 不包含/[appid]/[bucket_name]</td>
		</tr>
	</tbody>
</table>

### 3.5	目录列表,前缀搜索
功能: 在指定路径下搜索视频或目录。 接口: web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/
web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[DirName]/
web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[DirName]/[prefix] <font color="red"> <- 如果填写prefix, 则列出含此前缀的所有文件</font>
方法: GET
Request Param(query string):

| 参数名称 | 必选 | 类型 | 描述 | 
|---------|---------|---------|---------|
| op | 否 | String | 操作类型.可以不填,如果要填,固定填”list” | 
| num | 是 | Int | 拉取的总数 | 
| pattern | 否 | String | eListBoth, eListDirOnly, eListFileOnly (默认eListBoth) | 
| order | 否 | Int | 默认正序(=0), 填1为反序, | 
| context | 否 | String | 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页。 | 
| Authorization | 是 | String | 多次有效签名,用于鉴权， 具体生成方式详见[鉴权签名方法](http://www.qcloud.com/doc/product/314/%E9%89%B4%E6%9D%83%E5%8F%8A%E7%AD%BE%E5%90%8D%E6%96%87%E6%A1%A3) | 

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
			<td>透传字段,用于翻页,前端不需理解,需要往前/往后翻页则透传回来</td>
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
			<td>转码状态,如:</br> {“f10”: 0, “f20”: 1} 等;</br> f10:低清，f20:标清，f30:高清; </br></br>状态码：</br>0，初始化中，</br>1，转码中;</br>2，转码成功;</br>3，转码失败;</td>
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
			<td>视频播放时长,只有转码成功后才有，单位：秒</td>
		</tr>
		<tr>
			<td>video_play_url</td>
			<td>否，视频才有，目录没有</td>
			<td>Array</td>
			<td>各码率的播放url,</br> 如:[“f10”: url1, “f20’: url2] 等;</br> f10:低清，f20:标清，f30:高清</td>
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
功能: 在指定路径下更新目录或视频。 接口: web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[DirName]/
web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[DirName]/[filename]
方法: POST
Request Body (json):

| 参数名称 | 必选 | 类型 | 描述 | 
|---------|---------|---------|---------|
| op | 否 | String | 	操作类型.可以不填,如果要填,固定填”update” | 
| biz_attr | 否 | String | 目录/视频文件属性，业务端维护 | 
| video_cover | 否 | String | 视频封面的URL | 
| video_title | 否 | String | 视频才有，目录没有此属性 | 
| video_desc | 否 | String | 视频才有，目录没有此属性 | 
| Authorization | 是 | String | 单次有效签名,用于鉴权， 具体生成方式详见[鉴权签名方法](http://www.qcloud.com/doc/product/314/%E9%89%B4%E6%9D%83%E5%8F%8A%E7%AD%BE%E5%90%8D%E6%96%87%E6%A1%A3) | 

Response (json):

| 参数名称 | 必选 | 类型 | 描述 | 
|---------|---------|---------|---------|
| code | 是 | Int| 	服务端返回码 | 
| message | 是 | String | 服务端提示内容 | 

### 3.7	查询目录/视频属性信息
功能: 查询目录、视频的属性。 接口: web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[DirName]/
web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[DirName]/[filename]
方法: GET
Request Body (query string):

| 参数名称 | 必选 | 类型 | 描述 | 
|---------|---------|---------|---------|
| op | 是 | String | 操作类型.固定填”stat” | 
| Authorization | 是 | String | 多次有效签名,用于鉴权， 具体生成方式详见[鉴权签名方法](http://www.qcloud.com/doc/product/314/%E9%89%B4%E6%9D%83%E5%8F%8A%E7%AD%BE%E5%90%8D%E6%96%87%E6%A1%A3) | 

Response (json):
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
			<td>转码状态,如:</br> {“f10”: 0, “f20”: 1} 等;</br> f10:低清，f20:标清，f30:高清; </br></br>状态码：</br>0，初始化中，</br>1，转码中;</br>2，转码成功;</br>3，转码失败;</td>
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
			<td>视频播放时长,只有转码成功后才有，单位：秒</td>
		</tr>
		<tr>
			<td>video_play_url</td>
			<td>否，视频才有，目录没有</td>
			<td>Array</td>
			<td>各码率的播放url,</br> 如:[“f10”: url1, “f20’: url2] 等;</br> f10:低清，f20:标清，f30:高清</td>
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
功能: 删除目录或视频，只有空目录才能被删除。 接口: web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[dir_name]/[dir_name]/
web.video.myqcloud.com/files/v1/[appid]/[bucket_name]/[dir_name]/[dir_name]/[file_name]
方法: POST
Request Body (json):

| 参数名称 | 必选 | 类型 | 描述 | 
|---------|---------|---------|---------|
| op | 是 | String | 操作类型.固定填”delete” | 
| Authorization | 是 | String | 单次有效签名,用于鉴权， 具体生成方式详见[鉴权签名方法](http://www.qcloud.com/doc/product/314/%E9%89%B4%E6%9D%83%E5%8F%8A%E7%AD%BE%E5%90%8D%E6%96%87%E6%A1%A3) | 

Response (json):

| 参数名称 | 必选 | 类型 | 描述 | 
|---------|---------|---------|---------|
| code | 是 | Int| 	服务端返回码 | 
| message | 是 | String | 服务端提示内容 | 

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

若开启了token防盗链（如何开启，详见[token防盗链](http://www.qcloud.com/doc/product/314/%E6%8E%A7%E5%88%B6%E5%8F%B0%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97)）。
视频下载只能是私密下载，即必须access_url +?sign=[签名]。转码后的视频防盗链规则一样。
示例:

```

http://bucketname-10000379.video.myqcloud.com/q.mp4?sign=
GonmF5K4ehldbFpHASHbZo+DC6xhPTI5OTIwMSZrPUFLSURBc3FqSDM1QW9KTm16akIzbGZWVUlITERNQjE4Y1hHOCZlPT
E0MzMxNDU2MDAmdD0xNDI4NTcwMDMxJnI9MjkzODI3MTE2JnU9JmY9

```







