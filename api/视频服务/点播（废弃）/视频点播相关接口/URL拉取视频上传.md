<font color=RED>本页面的 API 已经失效，请参考</font>[新版本服务端 API](/document/product/266/7788)

## 1. 接口描述
 
域名：vod.api.qcloud.com
接口名: MultiPullVodFile

通过用户传递的URL，从已有的资源库批量拉取视频文件到腾讯云。此接口可以批量拉取多个视频文件，通过输入参数中的 n 值区分是第几个视频。

 

## 2. 输入参数
 
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> pullset.n.url
<td> 是
<td> String
<td> 需要拉取的视频URL，n为一个整数，第一个视频 n填1， 第二个视频 n填2， 依次递增；下同
<tr>
<td> pullset.n.fileName
<td> 是
<td> String
<td> 视频文件的名称
<tr>
<td> pullset.n.fileMd5
<td> 否
<td> string
<td> 视频文件的MD5
<tr>
<td> pullset.n.isTranscode
<td> 否
<td> Int
<td> 是否转码，0：否，1：是，默认为0；如果不执行转码，可在上传后，在管理控制台视频文件管理进行转码；
<tr>
<td> pullset.n.isScreenshot
<td> 否
<td> Int
<td> 是否截图，0：否，1：是，默认为0
<tr>
<td> pullset.n.isWatermark
<td> 否
<td> Int
<td> 是否打水印，0：否，1：是，默认为0；如果选择打水印，请务必在管理控制台提前完成水印文件选择和位置设定，否则可能导致上传失败；
<tr>
<td> pullset.n.notifyUrl
<td> 否
<td> String
<td> 腾讯云通过回调该URL地址通知；调用方该视频已经拉取完毕。
<tr>
<td> pullset.n.classId
<td> 否
<td> Int
<td> 视频的分类ID
<tr>
<td> pullset.n.tags
<td> 否
<td> String
<td> 视频的标签，有多个标签的话采用逗号分隔
<tr>
<td> pullset.n.priority
<td> 否
<td> Int
<td> 优先级0:中 1：高 2：低
<tr>
<td> pullset.n.isReport
<td> 否
<td> Int
<td> 回调开关，是否需要回包给开发商，0：否，1：是，默认为0
</tbody></table>

 

## 3. 输出参数
 
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code
<td> Int
<td> 错误码, 0: 成功, 其他值: 失败
<tr>
<td> message
<td> String
<td> 错误信息
<tr>
<td> data
<td> array
<td> 提交上传的file列表
</tbody></table>

其中data部分是一个数组，每一项格式如下
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> source_url
<td> string
<td> 源站地址
<tr>
<td> file_id
<td> uint
<td> file_id
<tr>
<td> file_name
<td> string
<td> 文件名称
</tbody></table>

 

## 4. 示例
 
输入1
<pre>
 https://domain/v2/index.php?Action=MultiPullVodFile
 &pullset.1.url=http%3A%2F%2Fv.qq.com%2Fcover%2Ft%2Ftofg0ynqvcjac58.mp4 //url必须指向可下载的视频地址
 &pullset.1.fileName=test
 &pullset.1.isTranscode=1
 &pullset.1.priority=1
 &pullset.1.isScreenshot=1
 &pullset.1.isWatermark=1
 &pullset.1.notifyUrl=http%3A%2F%2Ftest.com%2Ftest
 &pullset.1.classId=0
 &pullset.1.isReport=1
 &<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>

输出1
```

{
    "code" : 0,
    "message" : "",
}

```

## 5.回调说明
通用部分
● 调用关系
	视频云——>开发商
	请求方式
	HTTP POST
● 数据格式
	json
● 输入参数说明
	POST的path部分为开发商传入的notify_url（包含开放商拟定的参数），在调用api时传入
	POST的data部分为json，必要字段如下：
 
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> task
<td> 是
<td> string
<td> transcode：转码file_upload：上传
<tr>
<td> status
<td> 是
<td> int
<td> 0为成功
<tr>
<td> message
<td> 是
<td> string
<td>错误描述
<tr>
<td> data
<td> 否
<td> object
<td>扩展部分，各接口的详细数据
</tbody></table>

注：如果开发商调用api时，指定了需要转码，则回调会包括两次，一次是上传成功，一次是转码成功，[转码结果回调说明](http://cloud.tencent.com/wiki/v2/MultipartUploadVodFile#8..E8.AE.BE.E7.BD.AE.E8.BD.AC.E7.A0.81.E5.9B.9E.E8.B0.83)

● 输出参数说明
回调接口需要按json格式返回数据，必要字段如下：
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code
<td> Int
<td> 错误码, 0: 成功, 其他值: 失败
<tr>
<td> message
<td> String
<td> 错误信息
</tbody></table>


status定义
<table class="t"><tbody><tr>
<th><b>参数</b></th>
<th><b>描述</b></th>
<tr>
<td> 0 
<td> 成功
<tr>
<td> 10001
<td> 源站拉取文件失败
</tbody></table>


接口说明
各接口所需要的回调参数如下，数据填充在http post的data部分。

data部分的结构如下
<table class="t"><tbody><tr>
<th><b>参数</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td>image_video
<td>object
<td>视频信息
<tr>
<td> ret
<td> int
<td> 0表示成功 其他表示失败（用户可不用关心次字段)
<tr>
<td> message
<td> string
<td> 获取视频信息接口错误信息
<tr>
<td> file_id
<td> string
<td> 视频id
<tr>
<td> source_url
<td> string
<td> 拉取url
</tbody></table>

image_video字段如下：
<table class="t"><tbody><tr>
<th><b>参数</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td>code
<td>int
<td>1表示成功，（内部返回码，不用关心)
<tr>
<td> duration
<td> int
<td> 视频时长
<tr>
<td> imgUrls
<td> array
<td> 视频封面列表
id:截图id
url:截图地址
vheight:截图高度
vwidth:截图宽度
<tr>
<td> message
<td> string
<td> 接口返回信息
<tr>
<td> vid
<td> string
<td> vid
<tr>
<td> videoUrls
<td> array
<td> 视频基本信息和播放信息列表
accessperm:0 不用关心
definition:int 分辨率
filename:string 转码后文件名
md5:转码后文件md5
sha:转码后文件sha
size:转码后文件大小
update_time:文件更新时间
url:文件播放地址
vbitrate:视频码率   不转码是为0
vheight:视频高度   不转码是为0
vwidth:视频宽度    不转码是为0
</tbody></table>

示例：URL拉取文件接口
```
“image_video” > array(
      code>int
      duration>int
      imgUrls>array(   // 视频截图信息
         array(
            id>int
            url>’string’
            vheight>int
            vwidth>int
         )
     )
     message>’string’
     vid>’string’
     videoUrls>array(   // 视频播放信息
        array(
            url>’string’
            md5>’string’
            sha>’string’
            size>’string’
            update_time>’string’
            vbitrate>int
            vheight>int
						vwidth>int
        )
			)
   )
),
“ret”>’int’,获取视频信息的错误码
“message”>’string’,获取视频信息的错误描述，
“file_id”>int,文件id
“player_code”>array(
“h5”>’string’,h5播放器代码
“flash”>’string’，flash播放器代码
“iframe”>’string’，iframe代码
)

```

