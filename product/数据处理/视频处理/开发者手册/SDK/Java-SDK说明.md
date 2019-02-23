## 1	开发准备

<p>微视频服务的java sdk的下载地址： <a href="https://github.com/tencentyun/mvs-java-sdk.git" class="external free" title="https://github.com/tencentyun/mvs-java-sdk.git" target="_blank" rel="nofollow">https://github.com/tencentyun/mvs-java-sdk.git</a>
</p>

### 1.1	前期准备
1.	sdk采用1.8版本的jdk开发， 推荐使用相同的版本。如果使用其他版本，建议不要直接导入jar包，自行编译为佳；
2.	通过项目设置获取appid，secret_id和secret_key；
3.	Sdk开发采用netbeans，本文档以netbeans为例，其他IDE请适当调整。


### 1.2	导入SDK

<p>1.	下载java sdk<br>
如果安装了git命令行，执行git clone <a href="https://github.com/tencentyun/mvs-java-sdk.git" class="external free" title="https://github.com/tencentyun/mvs-java-sdk.git" target="_blank" rel="nofollow">https://github.com/tencentyun/mvs-java-sdk.git</a><br>
或者直接在github下载zip包。<br>
2.	导入项目<br>
在IDE中导入jar包（如果代码不支持，可以直接复制代码文件）<br>
<img src="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/jieruwanxiang-22.jpg" alt="jieruwanxiang-22.jpg"><br><br>
3.	参照api说明和sdk中提供的demo，开发代码。<br>
</p>

### 1.3	https支持

<p>修改VideoCloud.java中VIDEO_CGI_URL的值为：<code>https://web.video.myqcloud.com/files/v1</code> <br>
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
String appSign(int appId, String secretId, String secretKey, long expired, String bucketName)<br>
单次有效签名<br>
String appSignOnce(int appId, String secretId, String secretKey, String resourcePath, String bucketName)<br>
3．	参数和返回值<br>
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
<td> appId
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 开发者的授权appid
</td></tr>
<tr>
<td> secret_id
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 开发者的授权secret_id
</td></tr>
<tr>
<td> secret_key
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 开发者的授权secret_key，以上三项获取参见<a href="http://console.cloud.tencent.com/uvs/vproject" class="external text" title="http://console.cloud.tencent.com/uvs/vproject" target="_blank" rel="nofollow">项目设置</a>
</td></tr>
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
<td> resourcePath
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 视频文件唯一的标识，视频上传时会返回，格式/appid/bucketname/filepath/filename，其中/filepath/filename为视频文件在此bucketname下的全路径，
</td></tr></tbody></table><br><br>
<p>返回值：签名字符串<br>
示例代码：<br>
</p>

```
long expired = System.currentTimeMillis() / 1000 + 2592000;
String sign = Sign.appSign(m_appid, m_secret_id, m_secret_key, expired, "myBucketName");
String resourcePath= "/myFloder/myVideo.mp4";
String sign = Sign.appSignOnce(m_appid, m_secret_id, m_secret_key, resourcePath, "myBucketName");
```

### 2.2	目录操作
#### 2.2.1	创建目录
<p>1．	接口说明<br>
用于目录的创建，调用者可以通过此接口在指定bucket下创建目录。<br>
2．	方法<br>
String createFolder(String bucketName,String remotePath, String bizAttribute)<br>
3．	参数和返回值<br>
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
<td> remotePath
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 需要创建目录的全路径，以"/"开头,以"/"结尾，api会补齐
</td></tr>
<tr>
<td> bizAttribute
</td><td> String
</td><td> 否
</td><td> 无
</td><td> 目录绑定的属性信息，业务自行维护
</td></tr></tbody></table><br><br>
<p>返回值,json格式字符串：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
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
VideoCloud video = new VideoCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/";
String result = video.createFolder("bucketname", remotePath,"bizAttribute");
```

#### 2.2.2	目录属性更新
<p>1．	接口说明<br>
用于目录业务自定义属性的更新，调用者可以通过此接口更新业务的自定义属性字段。<br>
2．	方法<br>
String updateFolder(String bucketName, String remotePath, String bizAttribute) <br>
3．	参数和返回值<br>
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
<td> remotePath
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 需要创建目录的全路径，以"/"开头,以"/"结尾，api会补齐
</td></tr>
<tr>
<td> bizAttribute
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 新的目录绑定的属性信息
</td></tr></tbody></table><br><br>
<p>返回值,json格式字符串：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
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
VideoCloud video = new VideoCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/";
String result = video.updateFolder("bucketname", remotePath,"bizAttribute_new");
```

#### 2.2.3	目录查询
<p>1．	接口说明<br>
用于目录属性的查询，调用者可以通过此接口查询目录的属性。<br>
2．	方法<br>
String getFolderStat(String bucketName, String remotePath) <br>
3．	参数和返回值<br>
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
<td> remotePath
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 目录的全路径，以"/"开头,以"/"结尾，api会补齐
</td></tr></tbody></table><br><br>
<p>返回值,json格式字符串：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
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
VideoCloud video = new VideoCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/";
String result = video.getFolderStat("bucketname", remotePath);
```

#### 2.2.4	目录删除
<p>1．	接口说明<br>
用于目录的删除，调用者可以通过此接口删除空目录，如果目录中存在有效视频文件或目录，将不能删除。<br>
2．	方法<br>
String deleteFolder(String bucketName, String remotePath) <br>
3．	参数和返回值<br>
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
<td> remotePath
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 目录的全路径，以"/"开头,以"/"结尾，api会补齐
</td></tr></tbody></table><br><br>
<p>返回值,json格式字符串：<br>
</p>
<table class="t">
<tbody><tr>
<th width="80"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
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
VideoCloud video = new VideoCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/";
String result = video.deleteFolder("bucketname", remotePath);
```

#### 2.2.5	列举目录下视频&amp;目录
<p>1．	接口说明<br>
用于列举目录下视频和目录，调用者可以通过此接口查询目录下的视频和目录属性。<br>
2．	方法<br>
String getFolderList(String bucketName, String remotePath, int num, String context, int order, FolderPattern pattern) <br>
3．	参数和返回值<br>
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
<td> remotePath
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 目录的全路径，以"/"开头,以"/"结尾，api会补齐
</td></tr>
<tr>
<td> num
</td><td> int
</td><td> 是
</td><td> 无
</td><td> 要查询的目录/视频文件数量
</td></tr>
<tr>
<td> context
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页
</td></tr>
<tr>
<td> order
</td><td> int
</td><td> 是
</td><td> 无
</td><td> 默认正序(=0), 填1为反序
</td></tr>
<tr>
<td> pattern
</td><td> FolderPattern
</td><td> 是
</td><td> 无
</td><td> pattern File:只是视频文件，Folder:只是视频文件夹，Both:全部
</td></tr></tbody></table><br><br>
<p>返回值,json格式字符串：<br>
</p>
<table class="t">
<tbody><tr>
<th width="120"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="80"><b>必然返回</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
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
</td><td> 子视频数量(总)
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
</td><td> 视频文件名或目录名
</td></tr>
<tr>
<td> data.infos.biz_attr
</td><td> String
</td><td> 是
</td><td> 目录或视频属性，业务端维护
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
</td><td> 目录或视频文件的创建时间，unix时间戳
</td></tr>
<tr>
<td> data.infos.mtime
</td><td> String
</td><td> 是
</td><td> 目录或视频文件的修改时间，unix时间戳
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
</td><td> 视频文件已传输大小(通过与filesize对比可知视频文件传输进度)
</td></tr>
<tr>
<td> data.infos.sha
</td><td> String
</td><td> 否(当类型为视频文件时返回)
</td><td> 视频文件sha
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
</td><td> 否(当类型为视频文件时返回)
</td><td> 视频状态码 <br>0,初始化中，1，视频入库中;2，上传成功;
</td></tr>
<tr>
<td> data.infos.video_play_time
</td><td> Int
</td><td> 否(当类型为视频文件时返回)
</td><td> 视频播放时长,	只有使用视频转码的业务才有
</td></tr>
<tr>
<td> data.infos.video_title
</td><td> String
</td><td> 否(当类型为视频文件时返回)
</td><td> 视频标题
</td></tr>
<tr>
<td> data.infos.video_desc
</td><td> String
</td><td> 否(当类型为视频文件时返回)
</td><td> 视频描述
</td></tr>
<tr>
<td> data.infos.video_play_url
</td><td> Array
</td><td> 否(当类型为视频文件时返回)
</td><td> 各码率的播放url, 如:["f10":url1,"f20":url2,"f30":url3] 等
</td></tr></tbody></table><br><br>
<p>示例代码：<br>
</p>


```

VideoCloud video = new VideoCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/";
String result = video.getFolderList("bucketname",remotePath,100,"",0,FolderPattern.Both);

```

#### 2.2.6	列举目录下指定前缀视频&amp;目录
<p>1．	接口说明<br>
用于列举目录下指定前缀的视频和目录，调用者可以通过此接口查询目录下的指定前缀的视频和目录信息。<br>
2．	方法<br>
String getFolderList(String bucketName, String remotePath, String prefix, int num, String context, int order, FolderPattern pattern) <br>
3．	参数和返回值<br>
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
<td> remotePath
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 需要创建目录的全路径，以"/"开头,以"/"结尾，api会补齐
</td></tr>
<tr>
<td> prefix
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 读取视频文件/目录前缀
</td></tr>
<tr>
<td> num
</td><td> int
</td><td> 是
</td><td> 无
</td><td> 要查询的目录/视频文件数量
</td></tr>
<tr>
<td> context
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 透传字段，查看第一页，则传空字符串。若需要翻页，需要将前一页返回值中的context透传到参数中。order用于指定翻页顺序。若order填0，则从当前页正序/往下翻页；若order填1，则从当前页倒序/往上翻页
</td></tr>
<tr>
<td> order
</td><td> int
</td><td> 是
</td><td> 无
</td><td> 默认正序(=0), 填1为反序
</td></tr>
<tr>
<td> pattern
</td><td> FolderPattern
</td><td> 是
</td><td> 无
</td><td> pattern File:只是视频文件，Folder:只是视频文件夹，Both:全部
</td></tr></tbody></table><br><br>
<p>返回值,json格式字符串：<br>
</p>
<table class="t">
<tbody><tr>
<th width="120"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="80"><b>必然返回</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
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
</td><td> 目录或视频文件的创建时间，unix时间戳
</td></tr>
<tr>
<td> data.infos.mtime
</td><td> String
</td><td> 是
</td><td> 目录或视频文件的修改时间，unix时间戳
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
</td><td> 视频文件已传输大小(通过与filesize对比可知视频文件传输进度)
</td></tr>
<tr>
<td> data.infos.sha
</td><td> String
</td><td> 否(当类型为视频文件时返回)
</td><td> 视频文件sha
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
</td><td> 否(当类型为视频文件时返回)
</td><td> 视频状态码<br>0,初始化中，1，视频入库中;2，上传成功;
</td></tr>
<tr>
<td> data.infos.video_play_time
</td><td> Int
</td><td> 否(当类型为视频文件时返回)
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

VideoCloud video = new VideoCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/";
String result = video.getFolderList("bucketname", remotePath,"20150701_", 100, "", 0, FolderPattern.Both);

```

### 2.3	视频文件
#### 2.3.1	视频上传
<p>1．	接口说明<br>
用于较小视频(一般小于8MB)的上传，调用者可以通过此接口上传较小的视频并获得视频的url，较大的视频请使用分片上传接口。<br>
2．	方法<br>
String uploadFile(String bucketName, String remotePath,String localPath)<br>
String uploadFile(String bucketName, String remotePath,String localPath,String videoCover,String bizAttribute,String title,String desc,String magicContext) <br>
3．	参数和返回值<br>
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
<td> remotePath
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 视频在微视频服务端的全路径，不包括/appid/bucketname
</td></tr>
<tr>
<td> localPath
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 本地要上传视频的全路径
</td></tr>
<tr>
<td> videoCover
</td><td> String
</td><td> 否
</td><td> 无
</td><td> 视频封面的URL
</td></tr>
<tr>
<td> bizAttribute
</td><td> String
</td><td> 否
</td><td> 无
</td><td> 视频属性，业务端维护
</td></tr>
<tr>
<td> title
</td><td> String
</td><td> 否
</td><td> 无
</td><td> 视频的标题
</td></tr>
<tr>
<td> desc
</td><td> String
</td><td> 否
</td><td> 无
</td><td> 视频的描述
</td></tr>
<tr>
<td> magicContext
</td><td> String
</td><td> 否
</td><td> 无
</td><td> 透传字段，微视频会将此字段信息透传给业务设定的回调url，具体参见<a href="http://cloud.tencent.com/doc/product/314/%E6%8E%A7%E5%88%B6%E5%8F%B0%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97" title="微视频控制台操作指南">回调设置</a>
</td></tr></tbody></table><br><br>
<p>返回值,json格式字符串：<br>
</p>
<table class="t">
<tbody><tr>
<th width="120"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="80"><b>必然返回</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
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
</td><td> 生成的视频下载url
</td></tr>
<tr>
<td> data.url
</td><td> String
</td><td> 是
</td><td> 操作视频的url
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

VideoCloud video = new VideoCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/myVideo.mp4";
String result = video.upload(bucketname, remotePath,localPath,"http://video_cover.jpg","biz_attr","title","desc","magic_context");

```

#### 2.3.2	视频分片上传
<p>1．	接口说明<br>
用于较大视频(一般大于8MB)的上传，调用者可以通过此接口上传较大视频并获得视频的url和唯一标识resource_path（用于调用其他api）。<br>
2．	方法<br>
String sliceUpload(String bucketName,String remotePath,String localPath) <br>
String sliceUpload(String bucketName,String remotePath,String localPath,String videoCover,String bizAttribute,String title,String desc,String magicContext,int sliceSize) <br>
3．	参数和返回值<br>
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
<td> remotePath
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 视频在微视频服务端的全路径，不包括/appid/bucketname
</td></tr>
<tr>
<td> localPath
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 本地要上传视频的全路径
</td></tr>
<tr>
<td> videoCover
</td><td> String
</td><td> 否
</td><td> 无
</td><td> 视频封面的URL
</td></tr>
<tr>
<td> bizAttribute
</td><td> String
</td><td> 否
</td><td> 无
</td><td> 视频属性，业务端维护
</td></tr>
<tr>
<td> title
</td><td> String
</td><td> 否
</td><td> 无
</td><td> 视频的标题
</td></tr>
<tr>
<td> desc
</td><td> String
</td><td> 否
</td><td> 无
</td><td> 视频的描述
</td></tr>
<tr>
<td> magicContext
</td><td> String
</td><td> 否
</td><td> 无
</td><td> 透传字段，微视频会将此字段信息透传给业务设定的回调url，具体参见<a href="http://cloud.tencent.com/doc/product/314/%E6%8E%A7%E5%88%B6%E5%8F%B0%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97" title="微视频控制台操作指南">回调设置</a>
</td></tr>
<tr>
<td> sliceSize
</td><td> Int
</td><td> 否
</td><td> 512*1024字节
</td><td> 分片大小，用户可以根据网络状况自行设置
</td></tr></tbody></table><br><br>
<p>返回值,json格式字符串：<br>
</p>
<table class="t">
<tbody><tr>
<th width="120"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="80"><b>必然返回</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
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
</td><td> 生成的视频下载url
</td></tr>
<tr>
<td> data.url
</td><td> String
</td><td> 是
</td><td> 操作视频的url
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
VideoCloud video = new VideoCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/myVideo.mp4";
String result = video.sliceUpload(bucketname, remotePath,localPath,"http://video_cover.jpg","biz_attr","title","desc","magic_context",1024*1024);

```

#### 2.3.3	视频属性更新
<p>1．	接口说明<br>
用于目录业务自定义属性的更新，调用者可以通过此接口更新业务的自定义属性字段。<br>
2．	方法<br>
String updateFile(String bucketName, String remotePath, String videoCover, String bizAttribute,String title,String desc,String magicContext);<br>
3．	参数和返回值<br>
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
<td> remotePath
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 视频在微视频服务端的全路径，不包括/appid/bucketname
</td></tr>
<tr>
<td> videoCover
</td><td> String
</td><td> 否
</td><td> 无
</td><td> 视频封面的URL
</td></tr>
<tr>
<td> bizAttribute
</td><td> String
</td><td> 否
</td><td> 无
</td><td> 待更新的视频属性信息
</td></tr>
<tr>
<td> title
</td><td> String
</td><td> 否
</td><td> 无
</td><td> 视频的标题
</td></tr>
<tr>
<td> desc
</td><td> String
</td><td> 否
</td><td> 无
</td><td> 视频的描述
</td></tr></tbody></table><br><br>
<p>返回值,json格式字符串：<br>
</p>
<table class="t">
<tbody><tr>
<th width="120"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="80"><b>必然返回</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
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
>>VideoCloud video = new VideoCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/myVideo.mp4";
String result = video.updateFile(bucketname, remotePath,"http://video_cover.jpg","biz_attr_new","title_new","desc_new");

```

#### 2.3.4	视频查询
<p>1．	接口说明<br>
用于视频的查询，调用者可以通过此接口查询视频的各项属性信息。<br>
2．	方法<br>
String getFileStat(String bucketName, String remotePath) <br>
3．	参数和返回值<br>
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
<td> remotePath
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 视频在微视频服务端的全路径，不包括/appid/bucketname
</td></tr></tbody></table><br><br>
<p>返回值,json格式字符串：<br>
</p>
<table class="t">
<tbody><tr>
<th width="120"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="80"><b>必然返回</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
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
</td><td> 视频文件名或目录名
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
</td><td> 转码状态,如: {“f10”: 0, “f20”: 1} 等<br>f10:低清，f20:标清，f30:高清<br>状态码：0,初始化中，1，转码中;2，转码成功;3，转码失败;
</td></tr>
<tr>
<td> data.video_status
</td><td> Int
</td><td> 是
</td><td> 视频状态码 <br>0,初始化中，1，视频入库中;2，上传成功;
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
VideoCloud video = new VideoCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/myVideo.mp4";
String result = video.getFileStat("bucketname", remotePath);
```

#### 2.3.5	视频删除
<p>1．	接口说明<br>
用于视频的删除，调用者可以通过此接口删除已经上传的视频。<br>
2．	方法<br>
String deleteFile(String bucketName, String remotePath)<br>
3．	参数和返回值<br>
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
<td> remotePath
</td><td> String
</td><td> 是
</td><td> 无
</td><td> 视频在微视频服务端的全路径，不包括/appid/bucketname
</td></tr></tbody></table><br><br>
<p>返回值,json格式字符串：<br>
</p>
<table class="t">
<tbody><tr>
<th width="120"><b>参数名</b>
</th><th width="80"><b>类型</b>
</th><th width="80"><b>必然返回</b>
</th><th width="220"><b>参数描述</b>
</th></tr>
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
VideoCloud video = new VideoCloud(APP_ID, SECRET_ID, SECRET_KEY);
String remotePath = "/myFolder/myVideo.mp4";
String result = video.deleteFile("bucketname", remotePath);
```


<!-- 
NewPP limit report
Preprocessor node count: 68/1000000
Post-expand include size: 0/2097152 bytes
Template argument size: 0/2097152 bytes
Expensive parser function count: 0/100
-->

<!-- Saved in parser cache with key tencentwiki_db:pcache:idhash:1091-0!1!0!!zh-cn!2!edit=0 and timestamp 20160315222827 -->
