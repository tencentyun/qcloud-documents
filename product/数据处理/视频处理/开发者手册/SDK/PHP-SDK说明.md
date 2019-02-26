## 1	开发准备

<p>1、微视频服务的PHP SDK的下载地址： <a href="https://github.com/tencentyun/uvs-php-sdk.git" class="external free" title="https://github.com/tencentyun/uvs-php-sdk.git" target="_blank" rel="nofollow">https://github.com/tencentyun/uvs-php-sdk.git</a> <br>
2、composer项目名： tencentyun/uvs-php-sdk
</p>

### 1.1	前期准备

<p><b>前期准备</b><br>
1.	sdk依赖php 5.3.0版本及以上， 推荐使用相同的版本。<br>
2.	获取项目ID(appid)，bucket，secret_id和secret_key；<br>
</p>

### 1.2	获取SDK

<p>1、直接下载github上提供的源代码，集成到您的开发环境。 <br>
2、composer安装：直接执行命令：php composer.phar require tencentyun/uvs-php-sdk <br>
在您使用sdk之前，加载include.php即可。
</p>

```
require('./include.php'); <br>
use Qcloud_video\Auth; <br>
use Qcloud_video\Video; <br>
```


### 1.3	https支持
<p>修改conf.php中API_VIDEO_END_POINT的值为：<code>https://web.video.myqcloud.com/files/v1/</code> <br>
</p>

## 2	API详细说明

### 2.1	生成签名
<p>1．	接口说明<br>
签名生成方法，可以在服务端生成签名，供移动端app使用。<br>
签名分为2种：<br>
		多次有效签名（有一定的有效时间）<br>
		单次有效签名（绑定资源url，只能生效一次）<br>
签名的详细描述及使用场景参见<a href="http://cloud.tencent.com/doc/product/314/%E9%89%B4%E6%9D%83%E5%8F%8A%E7%AD%BE%E5%90%8D%E6%96%87%E6%A1%A3" title="微视频鉴权及签名文档">鉴权服务技术方案</a><br>
2．	方法<br>
多次有效签名<br>
</p>
<pre> public static function appSign($expired, $bucketName)
</pre>
<p>单次有效签名<br>
</p>
<pre> public static function appSign_once($path, $bucketName)
</pre>
<p>3．	参数和返回值<br>
参数说明：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="60"><b>类型</b>
</th><th width="60"><b>必须</b>
</th><th width="60"><b>默认值</b>
</th><th width="150"><b>参数描述</b>
</th></tr>
<tr>
<td> expired
</td><td> long
</td><td> 否
</td><td> 无
</td><td> 过期时间，Unix时间戳
</td></tr>
<tr>
<td> bucketName
</td><td> String
</td><td> 否
</td><td> 无
</td><td> bucket名称，bucket创建参见<a href="http://console.cloud.tencent.com/uvs/vbucket" class="external text" title="http://console.cloud.tencent.com/uvs/vbucket" target="_blank" rel="nofollow">创建Bucket</a>
</td></tr>
<tr>
<td> path
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 视频唯一的标识，视频文件上传时会返回，格式/filepath/filename，文件在此bucketname下的全路径，
</td></tr></tbody></table><br><br>
<p>返回值：签名字符串<br>
示例代码：<br>
</p>

```
$expired = time() + 60;
$sign = Auth::appSign($expired, $bucketName);
$resourcePath= "/myFloder/myVideo.mp4";
$sign = Auth::appSign_once($path, $bucketName);
```

### 2.2	目录操作

#### 2.2.1	创建目录

<p>1．	接口说明<br>
用于目录的创建，调用者可以通过此接口在指定bucket下创建目录。<br>
2．	方法<br>
</p>
<pre> public static function createFolder($bucketName, $path,$bizAttr = null)<br>
</pre>
<p>3．	参数和返回值<br>
参数说明：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="60"><b>类型</b>
</th><th width="60"><b>必须</b>
</th><th width="60"><b>默认值</b>
</th><th width="150"><b>参数描述</b>
</th></tr>
<tr>
<td> bucketName
</td><td> String
</td><td> 是
</td><td> 无
</td><td> bucket名称，bucket创建参见<a href="http://console.cloud.tencent.com/uvs/vbucket" class="external text" title="http://console.cloud.tencent.com/uvs/vbucket" target="_blank" rel="nofollow">创建Bucket</a>
</td></tr>
<tr>
<td> path
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 需要创建目录的全路径，以"/"开头,以"/"结尾，api会补齐
</td></tr>
<tr>
<td> bizAttr
</td><td> String
</td><td> 否
</td><td> null
</td><td> 目录绑定的属性信息，业务自行维护
</td></tr></tbody></table><br><br>
<p>返回值,json格式：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
<tr>
<td> httpcode
</td><td> Int
</td><td> http响应码，请求正常时为200
</td></tr>
<tr>
<td> code
</td><td> Int
</td><td> 错误码，成功时为0
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> 错误信息
</td></tr>
<tr>
<td> data
</td><td> Array
</td><td> 返回数据
</td></tr>
<tr>
<td> data.ctime
</td><td> String
</td><td> 目录的创建时间，unix时间戳
</td></tr>
<tr>
<td> data.resource_path
</td><td> String
</td><td> 目录的资源路径
</td></tr></tbody></table><br><br>
<p>示例代码：<br>
</p>

```
$bucketName = "myBucket";
$path = "/myFolder/";
$bizAttr = "attr_folder";
$result  = Video::createFolder($bucketName, $path,$bizAttr)
```

#### 2.2.2	目录属性更新

<p>1．	接口说明<br>
用于目录业务自定义属性的更新，调用者可以通过此接口更新业务的自定义属性字段。<br>
2．	方法<br>
</p>
<pre> public static function updateFolder($bucketName, $path, $bizAttr) <br>
</pre>
<p>3．	参数和返回值<br>
参数说明：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="60"><b>类型</b>
</th><th width="60"><b>必须</b>
</th><th width="60"><b>默认值</b>
</th><th width="150"><b>参数描述</b>
</th></tr>
<tr>
<td> bucketName
</td><td> String
</td><td> 是
</td><td> 无
</td><td> bucket名称，bucket创建参见<a href="http://console.cloud.tencent.com/uvs/vbucket" class="external text" title="http://console.cloud.tencent.com/uvs/vbucket" target="_blank" rel="nofollow">创建Bucket</a>
</td></tr>
<tr>
<td> path
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 需要创建目录的全路径，以"/"开头,以"/"结尾，api会补齐
</td></tr>
<tr>
<td> bizAttr
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 新的目录绑定的属性信息
</td></tr></tbody></table><br><br>
<p>返回值,json格式：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
<tr>
<td> httpcode
</td><td> Int
</td><td> http响应码，请求正常时为200
</td></tr>
<tr>
<td> code
</td><td> Int
</td><td> 错误码，成功时为0
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> 错误信息
</td></tr></tbody></table><br><br>
<p>示例代码：<br>
</p>

```
$bucketName = "myBucket";
$path = "/myFolder/";
$bizAttr = "attr_folder_new";
$result  = Video::updateFolder($bucketName, $path,$bizAttr)
```

#### 2.2.3	目录查询

<p>1．	接口说明<br>
用于目录属性的查询，调用者可以通过此接口查询目录的属性。<br>
2．	方法<br>
</p>
<pre> public static function statFolder($bucketName, $path)  <br>
</pre>
<p>3．	参数和返回值<br>
参数说明：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="60"><b>类型</b>
</th><th width="60"><b>必须</b>
</th><th width="60"><b>默认值</b>
</th><th width="150"><b>参数描述</b>
</th></tr>
<tr>
<td> bucketName
</td><td> String
</td><td> 是
</td><td> 无
</td><td> bucket名称，bucket创建参见<a href="http://console.cloud.tencent.com/uvs/vbucket" class="external text" title="http://console.cloud.tencent.com/uvs/vbucket" target="_blank" rel="nofollow">创建Bucket</a>
</td></tr>
<tr>
<td> path
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 目录的全路径，以"/"开头,以"/"结尾，api会补齐
</td></tr></tbody></table><br><br>
<p>返回值,json格式：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
<tr>
<td> httpcode
</td><td> Int
</td><td> http响应码，请求正常时为200
</td></tr>
<tr>
<td> code
</td><td> Int
</td><td> 错误码，成功时为0
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> 错误信息
</td></tr>
<tr>
<td> data
</td><td> Array
</td><td> 目录属性数据
</td></tr>
<tr>
<td> data.biz_attr
</td><td> String
</td><td> 目录绑定的属性信息，业务自行维护
</td></tr>
<tr>
<td> data.video_cover
</td><td> String
</td><td> 视频封面的URL
</td></tr>
<tr>
<td> data.ctime
</td><td> String
</td><td> 目录的创建时间，unix时间戳
</td></tr>
<tr>
<td> data.mtime
</td><td> String
</td><td> 目录的修改时间，unix时间戳
</td></tr>
<tr>
<td> data.name
</td><td> String
</td><td> 目录的名称
</td></tr></tbody></table><br><br>
<p>示例代码：<br>
</p>

```
$bucketName = "myBucket";
$path = "/myFolder/";
$result = Video::statFolder($bucketName, $path);
```

#### 2.2.4	目录删除
<p>1．	接口说明<br>
用于目录的删除，调用者可以通过此接口删除空目录，如果目录中存在有效视频文件或目录，将不能删除。<br>
2．	方法<br>
</p>
<pre> public static function delFolder($bucketName, $path) <br>
</pre>
<p>3．	参数和返回值<br>
参数说明：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="60"><b>类型</b>
</th><th width="60"><b>必须</b>
</th><th width="60"><b>默认值</b>
</th><th width="150"><b>参数描述</b>
</th></tr>
<tr>
<td> bucketName
</td><td> String
</td><td> 是
</td><td> 无
</td><td> bucket名称，bucket创建参见<a href="http://console.cloud.tencent.com/uvs/vbucket" class="external text" title="http://console.cloud.tencent.com/uvs/vbucket" target="_blank" rel="nofollow">创建Bucket</a>
</td></tr>
<tr>
<td> path
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 目录的全路径，以"/"开头,以"/"结尾，api会补齐
</td></tr></tbody></table><br><br>
<p>返回值,json格式：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
<tr>
<td> httpcode
</td><td> Int
</td><td> http响应码，请求正常时为200
</td></tr>
<tr>
<td> code
</td><td> Int
</td><td> 错误码，成功时为0
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> 错误信息
</td></tr></tbody></table><br><br>
<p>示例代码：<br>
</p>

```
$bucketName = "myBucket";
$path = "/myFolder/";
$result = Video::delFolder($bucketName, $path);
```

#### 2.2.5	列举目录下视频&amp;目录
<p>1．	接口说明<br>
用于列举目录下文件和目录，调用者可以通过此接口查询目录下的文件和目录属性。<br>
2．	方法<br>
</p>
<pre> public static function listFolder($bucketName, $path, $num = 20, $pattern = 'eListBoth', $order = 0, $context = null)<br>
</pre>
<p>3．	参数和返回值<br>
参数说明：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="60"><b>类型</b>
</th><th width="60"><b>必须</b>
</th><th width="60"><b>默认值</b>
</th><th width="150"><b>参数描述</b>
</th></tr>
<tr>
<td> bucketName
</td><td> String
</td><td> 是
</td><td> 无
</td><td> bucket名称，bucket创建参见<a href="http://console.cloud.tencent.com/uvs/vbucket" class="external text" title="http://console.cloud.tencent.com/uvs/vbucket" target="_blank" rel="nofollow">创建Bucket</a>
</td></tr>
<tr>
<td> path
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 目录的全路径，以"/"开头,以"/"结尾，api会补齐
</td></tr>
<tr>
<td> num
</td><td> int
</td><td> 否
</td><td> 20
</td><td> 要查询的目录/视频文件数量
</td></tr>
<tr>
<td> context
</td><td> String
</td><td> 否
</td><td> null
</td><td> 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页
</td></tr>
<tr>
<td> order
</td><td> int
</td><td> 否
</td><td> 0
</td><td> 默认正序(=0), 填1为反序
</td></tr>
<tr>
<td> pattern
</td><td> String
</td><td> 否
</td><td> eListBoth
</td><td> eListBoth,eListDirOnly,eListFileOnly  默认eListBoth
</td></tr></tbody></table><br><br>
<p>返回值,json格式：<br>
</p>
<table class="t">
<tbody><tr>
<th width="120"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="80"><b>必然返回</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
<tr>
<td> httpcode
</td><td> Int
</td><td> 是
</td><td> http响应码，请求正常时为200
</td></tr>
<tr>
<td> code
</td><td> Int
</td><td> 是
</td><td> API 错误码，成功时为0
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> 是
</td><td> 错误信息
</td></tr>
<tr>
<td> data
</td><td> Array
</td><td> 是
</td><td> 返回数据
</td></tr>
<tr>
<td> data.has_more
</td><td> Bool
</td><td> 是
</td><td> 是否有内容可以继续往前/往后翻页
</td></tr>
<tr>
<td> data.context
</td><td> String
</td><td> 是
</td><td> 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页
</td></tr>
<tr>
<td> data.dircount
</td><td> String
</td><td> 是
</td><td> 子目录数量(总)
</td></tr>
<tr>
<td> data.filecount
</td><td> String
</td><td> 是
</td><td> 子视频文件数量(总)
</td></tr>
<tr>
<td> data.infos
</td><td> Array
</td><td> 是
</td><td> 视频文件、目录集合，可以为空
</td></tr>
<tr>
<td> data.infos.name
</td><td> String
</td><td> 是
</td><td> 视频文件或目录名
</td></tr>
<tr>
<td> data.infos.biz_attr
</td><td> String
</td><td> 是
</td><td> 目录或文件属性，业务端维护
</td></tr>
<tr>
<td> data.infos.video_cover
</td><td> String
</td><td> 是
</td><td> 视频封面的URL
</td></tr>
<tr>
<td> data.infos.ctime
</td><td> String
</td><td> 是
</td><td> 目录或文件的创建时间，unix时间戳
</td></tr>
<tr>
<td> data.infos.mtime
</td><td> String
</td><td> 是
</td><td> 目录或文件的修改时间，unix时间戳
</td></tr>
<tr>
<td> data.infos.filesize
</td><td> Int
</td><td> 否(当类型为视频文件时返回)
</td><td> 视频文件大小
</td></tr>
<tr>
<td> data.infos.filelen
</td><td> Int
</td><td> 否(当类型为视频文件时返回)
</td><td> 文件已传输大小(通过与filesize对比可知文件传输进度)
</td></tr>
<tr>
<td> data.infos.sha
</td><td> String
</td><td> 否(当类型为视频文件时返回)
</td><td> 文件sha
</td></tr>
<tr>
<td> data.infos.access_url
</td><td> String
</td><td> 否(当类型为视频文件时返回)
</td><td> 生成的视频下载url
</td></tr>
<tr>
<td> data.infos.trans_status
</td><td> Array
</td><td> 否(当类型为文件时返回)
</td><td> 转码状态,如: {“f10”: 0, “f20”: 1} 等<br>f10:低清，f20:标清，f30:高清<br>状态码：0,初始化中，1，转码中;2，转码成功;3，转码失败;
</td></tr>
<tr>
<td> data.infos.video_status
</td><td> Int
</td><td> 否(当类型为视频时返回)
</td><td> 视频状态码 <br>0,初始化中，1，视频入库中;2，上传成功;
</td></tr>
<tr>
<td> data.infos.video_play_time
</td><td> Int
</td><td> 否(当类型为视频时返回)
</td><td> 视频播放时长,	只有使用视频转码的业务才有
</td></tr>
<tr>
<td> data.infos.video_title
</td><td> String
</td><td> 否(当类型为文件时返回)
</td><td> 视频标题
</td></tr>
<tr>
<td> data.infos.video_desc
</td><td> String
</td><td> 否(当类型为视频时返回)
</td><td> 视频描述
</td></tr>
<tr>
<td> data.infos.video_play_url
</td><td> Array
</td><td> 否(当类型为视频时返回)
</td><td> 各码率的播放url, 如:["f10":url1,"f20":url2,"f30":url3] 等
</td></tr></tbody></table><br><br>
<p>示例代码：<br>
</p>

```
$bucketName = "myBucket";
$path = "/myFolder/";
$result = Video::listFolder($bucketName, $path, 20, 'eListBoth',0);
```

#### 2.2.6	列举目录下指定前缀视频&amp;目录
<p>1．	接口说明<br>
用于列举目录下指定前缀的文件和目录，调用者可以通过此接口查询目录下的指定前缀的文件和目录信息。<br>
2．	方法<br>
</p>
<pre> public static function prefixSearch($bucketName, $prefix, $num = 20, $pattern = 'eListBoth', $order = 0, $context = null) <br>
</pre>
<p>3．	参数和返回值<br>
参数说明：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="60"><b>类型</b>
</th><th width="60"><b>必须</b>
</th><th width="60"><b>默认值</b>
</th><th width="150"><b>参数描述</b>
</th></tr>
<tr>
<td> bucketName
</td><td> String
</td><td> 是
</td><td> 无
</td><td> bucket名称，bucket创建参见<a href="http://console.cloud.tencent.com/uvs/vbucket" class="external text" title="http://console.cloud.tencent.com/uvs/vbucket" target="_blank" rel="nofollow">创建Bucket</a>
</td></tr>
<tr>
<td> prefix
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 列出含此前缀的所有视频文件(带全路径)
</td></tr>
<tr>
<td> num
</td><td> int
</td><td> 否
</td><td> 20
</td><td> 要查询的目录/视频文件数量
</td></tr>
<tr>
<td> context
</td><td> String
</td><td> 否
</td><td> null
</td><td> 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页
</td></tr>
<tr>
<td> order
</td><td> int
</td><td> 否
</td><td> 0
</td><td> 默认正序(=0), 填1为反序
</td></tr>
<tr>
<td> pattern
</td><td> String
</td><td> 否
</td><td> eListBoth
</td><td> eListBoth,eListDirOnly,eListFileOnly 默认eListBoth
</td></tr></tbody></table><br><br>
<p>返回值,json格式：<br>
</p>
<table class="t">
<tbody><tr>
<th width="120"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="80"><b>必然返回</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
<tr>
<td> httpcode
</td><td> Int
</td><td> 是
</td><td> http响应码，请求正常时为200
</td></tr>
<tr>
<td> code
</td><td> Int
</td><td> 是
</td><td> 错误码，成功时为0
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> 是
</td><td> API 错误信息
</td></tr>
<tr>
<td> data
</td><td> Array
</td><td> 是
</td><td> 返回数据
</td></tr>
<tr>
<td> data.has_more
</td><td> Bool
</td><td> 是
</td><td> 是否有内容可以继续往前/往后翻页
</td></tr>
<tr>
<td> data.context
</td><td> String
</td><td> 是
</td><td> 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页
</td></tr>
<tr>
<td> data.dircount
</td><td> String
</td><td> 是
</td><td> 子目录数量(总)
</td></tr>
<tr>
<td> data.filecount
</td><td> String
</td><td> 是
</td><td> 子视频文件数量(总)
</td></tr>
<tr>
<td> data.infos
</td><td> Array
</td><td> 是
</td><td> 视频文件、目录集合，可以为空
</td></tr>
<tr>
<td> data.infos.name
</td><td> String
</td><td> 是
</td><td> 视频文件或目录名
</td></tr>
<tr>
<td> data.infos.biz_attr
</td><td> String
</td><td> 是
</td><td> 目录或视频文件属性，业务端维护
</td></tr>
<tr>
<td> data.infos.video_cover
</td><td> String
</td><td> 是
</td><td> 视频封面的URL
</td></tr>
<tr>
<td> data.infos.ctime
</td><td> String
</td><td> 是
</td><td> 目录或文件的创建时间，unix时间戳
</td></tr>
<tr>
<td> data.infos.mtime
</td><td> String
</td><td> 是
</td><td> 目录或文件的修改时间，unix时间戳
</td></tr>
<tr>
<td> data.infos.filesize
</td><td> Int
</td><td> 否(当类型为视频文件时返回)
</td><td> 视频文件大小
</td></tr>
<tr>
<td> data.infos.filelen
</td><td> Int
</td><td> 否(当类型为视频文件时返回)
</td><td> 文件已传输大小(通过与filesize对比可知文件传输进度)
</td></tr>
<tr>
<td> data.infos.sha
</td><td> String
</td><td> 否(当类型为文件时返回)
</td><td> 文件sha
</td></tr>
<tr>
<td> data.infos.access_url
</td><td> String
</td><td> 否(当类型为视频文件时返回)
</td><td> 生成的视频下载url
</td></tr>
<tr>
<td> data.infos.trans_status
</td><td> Array
</td><td> 否(当类型为视频文件时返回)
</td><td> 转码状态,如: {“f10”: 0, “f20”: 1} 等<br>f10:低清，f20:标清，f30:高清<br>状态码：0,初始化中，1，转码中;2，转码成功;3，转码失败;
</td></tr>
<tr>
<td> data.infos.video_status
</td><td> Int
</td><td> 否(当类型为文件时返回)
</td><td> 视频状态码 <br>0,初始化中，1，视频入库中;2，上传成功;
</td></tr>
<tr>
<td> data.infos.video_play_time
</td><td> Int
</td><td> 否(当类型为视频时返回)
</td><td> 视频播放时长,	只有使用视频转码的业务才有
</td></tr>
<tr>
<td> data.infos.video_title
</td><td> String
</td><td> 否(当类型为视频时返回)
</td><td> 视频标题
</td></tr>
<tr>
<td> data.infos.video_desc
</td><td> String
</td><td> 否(当类型为视频时返回)
</td><td> 视频描述
</td></tr>
<tr>
<td> data.infos.video_play_url
</td><td> Array
</td><td> 否(当类型为视频时返回)
</td><td> 各码率的播放url, 如:["f10":url1,"f20":url2,"f30":url3] 等
</td></tr></tbody></table><br><br>
<p>示例代码：<br>
</p>


```
$bucketName = "myBucket";
$prefix= "/myFolder/2015-";
$result = Video::listFolder($bucketName, $path, 20, 'eListBoth',0);
```

### 2.3	视频文件

#### 2.3.1	视频上传

<p>1．	接口说明<br>
用于较小视频(一般小于8MB)的上传，调用者可以通过此接口上传较小的视频并获得视频的url，较大的视频请使用分片上传接口。<br>
2．	方法<br>
</p>
<pre>public static function upload($srcPath, $bucketName, $dstPath, $videoCover = null, $bizAttr = null, $title = null, $desc = null, $magicContext = null)<br>
</pre>
<p>3．	参数和返回值<br>
参数说明：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="60"><b>类型</b>
</th><th width="60"><b>必须</b>
</th><th width="60"><b>默认值</b>
</th><th width="150"><b>参数描述</b>
</th></tr>
<tr>
<td> srcPath
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 本地要上传视频文件的全路径
</td></tr>
<tr>
<td> bucketName
</td><td> String
</td><td> 是
</td><td> 无
</td><td> bucket名称，bucket创建参见<a href="http://console.cloud.tencent.com/uvs/vbucket" class="external text" title="http://console.cloud.tencent.com/uvs/vbucket" target="_blank" rel="nofollow">创建Bucket</a>
</td></tr>
<tr>
<td> dstPath
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 文件在微视频服务端的全路径，不包括/appid/bucketname
</td></tr>
<tr>
<td> videoCover
</td><td> String
</td><td> 否
</td><td> null
</td><td> 视频封面的URL
</td></tr>
<tr>
<td> bizAttr
</td><td> String
</td><td> 否
</td><td> null
</td><td> 视频文件属性，业务端维护
</td></tr>
<tr>
<td> title
</td><td> String
</td><td> 否
</td><td> null
</td><td> 视频的标题
</td></tr>
<tr>
<td> desc
</td><td> String
</td><td> 否
</td><td> null
</td><td> 视频的描述
</td></tr>
<tr>
<td> magicContext
</td><td> String
</td><td> 否
</td><td> null
</td><td> 透传字段，微视频会将此字段信息透传给业务设定的回调url，具体参见<a href="http://cloud.tencent.com/doc/product/314/%E6%8E%A7%E5%88%B6%E5%8F%B0%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97" title="微视频控制台操作指南">回调设置</a>
</td></tr></tbody></table><br><br>
<p>返回值,json格式：<br>
</p>
<table class="t">
<tbody><tr>
<th width="120"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="80"><b>必然返回</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
<tr>
<td> httpcode
</td><td> Int
</td><td> 是
</td><td> http响应码，请求正常时为200
</td></tr>
<tr>
<td> code
</td><td> Int
</td><td> 是
</td><td> 错误码，成功时为0
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> 是
</td><td> 错误信息
</td></tr>
<tr>
<td> data
</td><td> Array
</td><td> 是
</td><td> 返回数据
</td></tr>
<tr>
<td> data.access_url
</td><td> Bool
</td><td> 是
</td><td> 生成的文件下载url
</td></tr>
<tr>
<td> data.url
</td><td> String
</td><td> 是
</td><td> 操作文件的url
</td></tr>
<tr>
<td> data.resource_path
</td><td> String
</td><td> 是
</td><td> 资源路径. 格式:/appid/bucket/xxx
</td></tr></tbody></table><br><br>
<p>示例代码：<br>
</p>

```
$srcPath= "/data/test.mp4";
$bucketName = "myBucket";
$dstPath = "/myFolder/";
$result = Video::upload($srcPath,$bucketName,dstPath , "http://cover-url.jpg", "biz_attr","title","desc","magic_context");
```

#### 2.3.2	视频分片上传
<p>1．	接口说明<br>
用于较大视频(一般大于8MB)的上传，调用者可以通过此接口上传较大视频并获得视频的url和唯一标识resource_path（用于调用其他api）。<br>
2．	方法<br>
</p>

```
public static function upload_slice(
            $srcPath, $bucketName, $dstPath, 
            $videoCover = null, $bizAttr = null, $title = null, $desc = null, 
            $magicContext = null, $sliceSize = self::DEFAULT_SLICE_SIZE, $session = null)
```

<p>3．	参数和返回值<br>
参数说明：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="60"><b>类型</b>
</th><th width="60"><b>必须</b>
</th><th width="60"><b>默认值</b>
</th><th width="150"><b>参数描述</b>
</th></tr>
<tr>
<td> srcPath
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 本地要上传视频文件的全路径
</td></tr>
<tr>
<td> bucketName
</td><td> String
</td><td> 是
</td><td> 无
</td><td> bucket名称，bucket创建参见<a href="http://console.cloud.tencent.com/uvs/vbucket" class="external text" title="http://console.cloud.tencent.com/uvs/vbucket" target="_blank" rel="nofollow">创建Bucket</a>
</td></tr>
<tr>
<td> dstPath
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 文件在微视频服务端的全路径，不包括/appid/bucketname
</td></tr>
<tr>
<td> videoCover
</td><td> String
</td><td> 否
</td><td> null
</td><td> 视频封面的URL
</td></tr>
<tr>
<td> bizAttr
</td><td> String
</td><td> 否
</td><td> null
</td><td> 视频文件属性，业务端维护
</td></tr>
<tr>
<td> title
</td><td> String
</td><td> 否
</td><td> null
</td><td> 视频的标题
</td></tr>
<tr>
<td> desc
</td><td> String
</td><td> 否
</td><td> null
</td><td> 视频的描述
</td></tr>
<tr>
<td> magicContext
</td><td> String
</td><td> 否
</td><td> null
</td><td> 透传字段，微视频会将此字段信息透传给业务设定的回调url，具体参见<a href="http://cloud.tencent.com/doc/product/314/%E6%8E%A7%E5%88%B6%E5%8F%B0%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97" title="微视频控制台操作指南">回调设置</a>
</td></tr>
<tr>
<td> sliceSize
</td><td> Int
</td><td> 否
</td><td> 512*1024字节
</td><td> 分片大小，用户可以根据网络状况自行设置
</td></tr>
<tr>
<td> session
</td><td> String
</td><td> 否
</td><td> null
</td><td> 如果是断点续传, 则带上(唯一标识此视频文件传输过程的id, 由后台下发, 调用方透传)
</td></tr></tbody></table><br><br>
<p>返回值,json格式：<br>
</p>
<table class="t">
<tbody><tr>
<th width="120"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="80"><b>必然返回</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
<tr>
<td> httpcode
</td><td> Int
</td><td> 是
</td><td> http响应码，请求正常时为200
</td></tr>
<tr>
<td> code
</td><td> Int
</td><td> 是
</td><td> 错误码，成功时为0
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> 是
</td><td> 错误信息
</td></tr>
<tr>
<td> data
</td><td> Array
</td><td> 是
</td><td> 返回数据
</td></tr>
<tr>
<td> data.access_url
</td><td> Bool
</td><td> 是
</td><td> 生成的文件下载url
</td></tr>
<tr>
<td> data.url
</td><td> String
</td><td> 是
</td><td> 操作文件的url
</td></tr>
<tr>
<td> data.resource_path
</td><td> String
</td><td> 是
</td><td> 资源路径. 格式:/appid/bucket/xxx
</td></tr></tbody></table><br><br>
<p>示例代码：<br>
</p>

```
$srcPath= "/data/test.mp4";
$bucketName = "myBucket";
$dstPath = "/myFolder/";
$result = Video::upload_slice($srcPath,$bucketName,dstPath ,"http://cover-url.jpg","biz_attr","title","desc","magic_context");
```

#### 2.3.3	视频属性更新

<p>1．	接口说明<br>
用于文件业务自定义属性的更新，调用者可以通过此接口更新业务的自定义属性字段。<br>
2．	方法<br>
</p>
<pre> public static function update($bucketName, $path, $videoCover = null, $bizAttr = null,$title = null, $desc = null)
</pre>
<p>3．	参数和返回值<br>
参数说明：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="60"><b>类型</b>
</th><th width="60"><b>必须</b>
</th><th width="60"><b>默认值</b>
</th><th width="150"><b>参数描述</b>
</th></tr>
<tr>
<td> bucketName
</td><td> String
</td><td> 是
</td><td> 无
</td><td> bucket名称，bucket创建参见<a href="http://console.cloud.tencent.com/uvs/vbucket" class="external text" title="http://console.cloud.tencent.com/uvs/vbucket" target="_blank" rel="nofollow">创建Bucket</a>
</td></tr>
<tr>
<td> path
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 文件在微视频服务端的全路径，不包括/appid/bucketname
</td></tr>
<tr>
<td> videoCover
</td><td> String
</td><td> 否
</td><td> null
</td><td> 视频封面的URL
</td></tr>
<tr>
<td> bizAttr
</td><td> String
</td><td> 否
</td><td> null
</td><td> 待更新的视频文件属性信息
</td></tr>
<tr>
<td> title
</td><td> String
</td><td> 否
</td><td> null
</td><td> 视频的标题
</td></tr>
<tr>
<td> desc
</td><td> String
</td><td> 否
</td><td> null
</td><td> 视频的描述
</td></tr></tbody></table><br><br>
<p>返回值,json格式：<br>
</p>
<table class="t">
<tbody><tr>
<th width="120"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="80"><b>必然返回</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
<tr>
<td> httpcode
</td><td> Int
</td><td> 是
</td><td> http响应码，请求正常时为200
</td></tr>
<tr>
<td> code
</td><td> Int
</td><td> 是
</td><td> 错误码，成功时为0
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> 是
</td><td> 错误信息
</td></tr></tbody></table><br><br>
<p>示例代码：<br>
</p>

```
$bucketName = "myBucket";
$path = "/myFolder/test.mp4";
$result = Video::update($bucketName, $path,"http://cover-url.jpg","attr_file_new"，"title_new"，"desc_new");
```

#### 2.3.4	视频查询
<p>1．	接口说明<br>
用于视频的查询，调用者可以通过此接口查询视频的各项属性信息。<br>
2．	方法<br>
</p>
<pre> public static function stat($bucketName, $path)<br>
</pre>
<p>3．	参数和返回值<br>
参数说明：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="60"><b>类型</b>
</th><th width="60"><b>必须</b>
</th><th width="60"><b>默认值</b>
</th><th width="150"><b>参数描述</b>
</th></tr>
<tr>
<td> bucketName
</td><td> String
</td><td> 是
</td><td> 无
</td><td> bucket名称，bucket创建参见<a href="http://console.cloud.tencent.com/uvs/vbucket" class="external text" title="http://console.cloud.tencent.com/uvs/vbucket" target="_blank" rel="nofollow">创建Bucket</a>
</td></tr>
<tr>
<td> path
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 文件在微视频服务端的全路径，不包括/appid/bucketname
</td></tr></tbody></table><br><br>
<p>返回值,json格式：<br>
</p>
<table class="t">
<tbody><tr>
<th width="120"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="80"><b>必然返回</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
<tr>
<td> httpcode
</td><td> Int
</td><td> 是
</td><td> http响应码，请求正常时为200
</td></tr>
<tr>
<td> code
</td><td> Int
</td><td> 是
</td><td> 错误码，成功时为0
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> 是
</td><td> 错误信息
</td></tr>
<tr>
<td> data
</td><td> Array
</td><td> 是
</td><td> 视频属性数据
</td></tr>
<tr>
<td> data.name
</td><td> String
</td><td> 是
</td><td> 视频文件或目录名
</td></tr>
<tr>
<td> data.biz_attr
</td><td> String
</td><td> 是
</td><td> 视频属性，业务端维护
</td></tr>
<tr>
<td> data.video_cover
</td><td> String
</td><td> 是
</td><td> 视频封面的URL
</td></tr>
<tr>
<td> data.ctime
</td><td> String
</td><td> 是
</td><td> 视频的创建时间，unix时间戳
</td></tr>
<tr>
<td> data.mtime
</td><td> String
</td><td> 是
</td><td> 视频的修改时间，unix时间戳
</td></tr>
<tr>
<td> data.filesize
</td><td> Int
</td><td> 是
</td><td> 视频文件大小
</td></tr>
<tr>
<td> data.filelen
</td><td> Int
</td><td> 是
</td><td> 视频文件已传输大小(通过与filesize对比可知文件传输进度)
</td></tr>
<tr>
<td> data.sha
</td><td> String
</td><td> 是
</td><td> 视频文件sha
</td></tr>
<tr>
<td> data.access_url
</td><td> String
</td><td> 是
</td><td> 生成的视频下载url
</td></tr>
<tr>
<td> data.trans_status
</td><td> Array
</td><td> 是
</td><td> 转码状态,如: ["f10":0,"f20":1,"f30":0] 等
</td></tr>
<tr>
<td> data.video_status
</td><td> Int
</td><td> 是
</td><td> 视频状态码
</td></tr>
<tr>
<td> data.video_play_time
</td><td> Int
</td><td> 是
</td><td> 视频播放时长,	只有使用视频转码的业务才有
</td></tr>
<tr>
<td> data.video_title
</td><td> String
</td><td> 是
</td><td> 视频标题
</td></tr>
<tr>
<td> data.video_desc
</td><td> String
</td><td> 是
</td><td> 视频描述
</td></tr>
<tr>
<td> data.video_play_url
</td><td> Array
</td><td> 是
</td><td> 各码率的播放url, 如:["f10":url1,"f20":url2,"f30":url3] 等
</td></tr></tbody></table><br><br>
<p>示例代码：<br>
</p>

```
$bucketName = "myBucket";
$path = "/myFolder/test.mp4";
$result = Video::stat($bucketName, $path);
```

#### 2.3.5	视频删除
<p>1．	接口说明<br>
用于视频的删除，调用者可以通过此接口删除已经上传的视频。<br>
2．	方法<br>
</p>
<pre> public static function del($bucketName, $path) <br>
</pre>
<p>3．	参数和返回值<br>
参数说明：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="60"><b>类型</b>
</th><th width="60"><b>必须</b>
</th><th width="60"><b>默认值</b>
</th><th width="150"><b>参数描述</b>
</th></tr>
<tr>
<td> bucketName
</td><td> String
</td><td> 是
</td><td> 无
</td><td> bucket名称，bucket创建参见<a href="http://console.cloud.tencent.com/uvs/vbucket" class="external text" title="http://console.cloud.tencent.com/uvs/vbucket" target="_blank" rel="nofollow">创建Bucket</a>
</td></tr>
<tr>
<td> path
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 文件在微视频服务端的全路径，不包括/appid/bucketname
</td></tr></tbody></table><br><br>
<p>返回值,json格式：<br>
</p>
<table class="t">
<tbody><tr>
<th width="120"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="80"><b>必然返回</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
<tr>
<td> httpcode
</td><td> Int
</td><td> 是
</td><td> http响应码，请求正常时为200
</td></tr>
<tr>
<td> code
</td><td> Int
</td><td> 是
</td><td> 错误码，成功时为0
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> 是
</td><td> 错误信息
</td></tr></tbody></table><br><br>
<p>示例代码：<br>
</p>

```
$bucketName = "myBucket";
$path = "/myFolder/test.mp4";
$result = Video::del($bucketName, $path);
```

<!-- 
NewPP limit report
Preprocessor node count: 73/1000000
Post-expand include size: 0/2097152 bytes
Template argument size: 0/2097152 bytes
Expensive parser function count: 0/100
-->

<!-- Saved in parser cache with key tencentwiki_db:pcache:idhash:1092-0!1!0!!zh-cn!2!edit=0 and timestamp 20160316224514 -->
