>!
- 腾讯文智自然语言处理已于2019年7月09日全新升级为 [新版](https://cloud.tencent.com/document/product/271/3317)，接口功能更全面，服务更加稳定，且公测期间免费使用。
- 老版本接口将不再继续维护，将于2019年11月16日零点下线，建议您使用 [新版 API ](https://cloud.tencent.com/document/product/271/35484)，体验更优服务。
- 接口切换过程中，若您有相关问题，可加入官方 QQ 群（330130409）详细咨询。

## 1.接口描述
  域名：wenzhi.api.qcloud.com
  接口名: ContentTranscode
	
  转码分为两大类：网页转码和网页名片。网页转码将在PC机上展示的二维页面转换为适合在手机等移动端设备上展示的一维页面，方便用户在移动端阅读。网页名片将页面简化为主体图片、标题、摘要的组合，以“卡片”的形式展示给大众，适合做页面的分享、收藏、推广等。用户只需要提交网页的 url ，就能获取我们的转码服务，方便、快捷。当前，网页转码已为公司QQ、qzone、微云、微博、正文吧等平台提供服务。
## 2.输入参数
<table class="t">
<tr>
<th width="80"> <b>参数名称</b>
</th><th width="50"> <b>必选</b>
</th><th width="80"> <b>类型</b>
</th><th width="150"> <b>描述</b>
</th></tr>
<tr>
<td> url </td><td> 是 </td><td> String </td><td> 网页地址
</td></tr>
<tr>
<td> to_html </td><td> 是 </td><td> Int32 </td><td> 1&nbsp;: html 0&nbsp;: xml
</td></tr></table>


## 3.输出参数
<table class="t">
<tr>
<th width="80"> <b>参数名称</b>
</th><th width="80"> <b>类型</b>
</th><th width="250"> <b>描述</b>
</th></tr>
<tr>
<td> code </td><td> Int32 </td><td> 错误码, 0: 成功, 其他值: 失败
</td></tr>
<tr>
<td> message </td><td> String </td><td> 错误信息
</td></tr>
<tr>
<td> content </td><td> String </td><td> 转码结果
</td></tr></table>
<p>转码API错误码详细信息如下：<br />
</p>
<table class="t">
<tr>
<th width="50"> <b>错误码</b>
</th><th width="100"> <b>含义说明</b>
</th></tr>
<tr>
<td> 400 </td><td> HTTP Method不正确
</td></tr>
<tr>
<td> 401 </td><td> HTTP请求参数不符合要求
</td></tr>
<tr>
<td> 503 </td><td> 调用额度已超出限制
</td></tr>
<tr>
<td> 504 </td><td> 服务故障
</td></tr></table>


## 4.详细示例
  示例业务详细信息如下表：
<table class="t">
<tr>
<th width="100"> <br />
</th><th width="80"> <b>参数名称</b>
</th><th width="100"> <b>参数描述</b>
</th><th width="50"> <b>必选</b>
</th><th width="150"> <b>参数值示例</b>
</th></tr>
<tr>
<td rowspan="4">腾讯云公共参数 </td><td> Action </td><td> 方法名 </td><td> 是 </td><td> ContentTranscode
</td></tr>
<tr>
<td> SecretId </td><td> SecretId </td><td> 是 </td><td> AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
</td></tr>
<tr>
<td> Timestamp </td><td> 当前时间戳 </td><td> 是 </td><td> 1408704141
</td></tr>
<tr>
<td> Nonce </td><td> 随机正整数 </td><td> 是 </td><td> 345122
</td></tr>
<tr>
<td rowspan="2">业务参数 </td><td> url </td><td> 网页地址 </td><td> 是 </td><td> www.163.com
</td></tr>
<tr>
<td> to_html </td><td> 1&nbsp;: html 0&nbsp;: xml </td><td> 是 </td><td> 1
</td></tr></table>


  下面以上述业务为例，详细说明“转码API”接口的使用方法。
## 4.1 接口鉴权
  示例要调用服务的数据为：{"url":"www.163.com","to_html":1}
  则上述业务的参数列表如下：
	
  <div class="code">
 <pre> {
        'Action' : 'ContentTranscode',
        'Nonce' : 345122,
        'Region' : 'sz',
        'SecretId' : 'AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA',
        'Timestamp' : 1408704141,
        'url': 'www.163.com',
        'to_html': 1
    }</pre>
</div>

根据上述参数列表进行签名，得出的数字签名为：HgIYOPcx5lN6gz8JsCFBNAWp2oQ（示例），详细的数字签名的生成方法请参照：《腾讯云接口鉴权》。
>!
1. 在生成签名的过程中，需要将加密字符串中包含的“_”改写成“.”，从而加密产生签名；
2. 鉴权时，需要将参数列表按 key 进行排序：字典序，同时大写在前。

## 4.2 API 调用
  根据上一步（9.4.1）中得到的数字签名，以 POST 请求为例构造请求 URL，将数字签名加入到参数 Signature 中。
	
  <div class="code">
 <pre> https://wenzhi.api.qcloud.com/v2/index.php?
	Action=ContentTranscode
	&Nonce=345122
	&Region=sz
	&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
	&Timestamp=1408704141
	&Signature=HgIYOPcx5lN6gz8JsCFBNAWp2oQ
	&url=www.163.com
	&to_html=1</pre>
</div>

  执行上述操作之后，会将数据{"url":"www.163.com","to_html":1}发送给API接口，进行相应分析。
  <b>注意：</b>在发送请求过程中，不能将参数字符串中包含的“”改写成“.”。
