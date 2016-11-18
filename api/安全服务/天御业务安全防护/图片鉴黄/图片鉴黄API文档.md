## 1.接口描述
识别图片是否为色情、性感图片。
<br> 协议：HTTPS
<br> 域名：csec.api.qcloud.com
<br> 接口名：FileDetection

## 2.输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数](https://www.qcloud.com/doc/api/254/1778)页面。其中，此接口的Action字段为FileDetection。
<table class="t">
<tbody><tr>
<th> <b>参数名称</b>
</th><th> <b>是否必须</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> fileName
</td><td><font color=red> 必选 </font color=red>
</td><td> String
</td><td> 文件名
</td></tr>
<tr>
<td> fileUrl
</td><td> 可选
</td><td> String
</td><td> 文件的URL地址
</td></tr>
<tr>
<td> fileMd5
</td><td> 可选
</td><td> String
</td><td> 图片MD5值
</td></tr>
<tr>
<td> fileSha1
</td><td> 可选
</td><td> String
</td><td> 图片sha值
</td></tr>
</td></tr></tbody></table>

## 3.输出参数
<table class="t">
<tbody><tr>
<th> <b>参数名称</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th></tr>
<tr>
<td> level
</td><td> Int
</td><td> 0：表示无恶意
<br> 1：文件名恶意
<br> 2：文件内容恶意
<br> 3：文件名和内容恶意
</td></tr>
<tr>
<td> contentType
</td><td> Int
</td><td> 文件内容恶意类型：
<br> 0：未知
<br> 1：安全
<br> 2：风险
<br> 3：病毒
</td></tr>
<td> code
</td><td> Int
</td><td> 公共错误码，0表示成功，其他值表示失败。详见错误码页面的<a href="https://www.qcloud.com/doc/api/254/1781"target="black">公共错误码</a>
</td></tr>
<tr>
<td> confidence
</td><td> Double
</td><td> 识别为黄图的置信度，范围0-100；
是normalScore,hotScore,pornScore的综合评分,confidence大于83定为疑似图片
</td></tr>
<tr>
<td> normalScore
</td><td> Double
</td><td> 图片为正常图片的评分
</td></tr>
<tr>
<td> hotScore
</td><td> Double
</td><td> 图片为性感图片的评分
</td></tr>
<tr>
<td> pornScore
</td><td> Double
</td><td> 图片为色情图片的评分
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> 模块错误信息描述，与接口相关
</td></tr>
</tbody></table>

## 4.示例代码
代码下载：  [Python示例](https://mc.qcloudimg.com/static/archive/c8aa3de8d147ae873b9645c1b84eaac4/FileDetection.py.zip) [PHP示例](https://mc.qcloudimg.com/static/archive/df6e1d58b1a853e9af459e034661feb9/FileDetection.php.zip) [Java示例](https://mc.qcloudimg.com/static/archive/6ad6797367a37e8cd7d09f94b008b76e/FileDetection.java.zip) [.Net示例](https://mc.qcloudimg.com/static/archive/5314a5e2171556d17cc197cf1cc7e14d/FileDetection.cs.zip)
<br> 一个完整的请求需要两类请求参数：公共请求参数和接口请求参数。这里只列出了接口请求参数，并未列出公共请求参数，有关公共请求参数的说明可见[公共请求参数](https://www.qcloud.com/doc/api/254/1778)小节。
```
请求示例 ：
https://csec.api.qcloud.com/v2/index.php?Action=FileDetection
&<公共请求参数>
&fileName=helloworld.avi
&fileUrl=http%3A%2F%2Fimg4.duitang.com%2Fuploads%2Fitem%2F201212%2F18%2F20121218162327_WMCC3.thumb.466_0.jpeg
&fileMd5=v%2B2%2B45OP78U0cYlB8g%2BBpLrF%2BsE%3D
```

## 5.响应示例
```
{
"code": 0,
"confidence": 0,
"contentType": 0,
"hotScore": 0,
"level": 0,
"message": "No Error",
"normalScore": 99,
"pornScore": 0
}
```