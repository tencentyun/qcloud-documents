>!
- 腾讯文智自然语言处理已于2019年7月09日全新升级为 [新版](https://cloud.tencent.com/document/product/271/3317)，接口功能更全面，服务更加稳定，且公测期间免费使用。
- 老版本接口将不再继续维护，将于2019年11月16日零点下线，建议您使用 [新版 API ](https://cloud.tencent.com/document/product/271/35484)，体验更优服务。
- 接口切换过程中，若您有相关问题，可加入官方 QQ 群（330130409）详细咨询。

## 1. 接口描述
  域名：wenzhi.api.qcloud.com
  接口名: LexicalCheck
  能够实现对短文本的自动纠错功能，长文本的自动纠错也即将推出。用户只需要提供业务数据和日志, 无需关注技术细节和更新流程, 就可以享受到业务自身定制的纠错服务, 甚至不提供业务数据，享受通用的纠错服务。目前已经接入的业务包括音乐、视频、应用宝、云搜等，评测效果均好于竞品。
## 2. 输入参数
<table class="t">
<tr>
<th width="50"> <b>参数名称</b>
</th><th width="50"> <b>必选</b>
</th><th width="50"> <b>类型</b>
</th><th width="180"> <b>描述</b>
</th></tr>
<tr>
<td> text </td><td> 是 </td><td> String </td><td> 待纠错的文本（utf-8）
</td></tr></table>

## 3. 输出参数
<table class="t">
<tr>
<th width="100"> <b>参数名称</b>
</th><th width="80"> <b>类型</b>
</th><th width="200"> <b>描述</b>
</th></tr>
<tr>
<td> code </td><td> Int32 </td><td> 错误码, 0: 成功, 其他值: 失败
</td></tr>
<tr>
<td> message </td><td> String </td><td> 错误信息
</td></tr>
<tr>
<td> text </td><td> String </td><td> 纠错后词
</td></tr>
<tr>
<td> text_annotate </td><td> String </td><td> 标红的纠错后词
</td></tr>
<tr>
<td> conf </td><td> Double </td><td> 纠错置信度
</td></tr></table>
纠错API错误码详细信息如下：<br />
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

## 4. 详细示例
  示例业务详细信息如下表：
<table class="t">
<tr>
<th width="50"> <br />
</th><th width="50"> <b>参数名称</b>
</th><th width="50"> <b>参数描述</b>
</th><th width="50"> <b>必选</b>
</th><th width="150"> <b>参数值示例</b>
</th></tr>
<tr>
<td rowspan="4">腾讯云公共参数 </td><td> Action </td><td> 方法名 </td><td> 是 </td><td> LexicalCheck
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
<td> 业务参数 </td><td> text </td><td> 待纠错的文本（utf-8） </td><td> 是 </td><td> 睡交吃饭
</td></tr></table>


  下面以上述业务为例，详细说明“纠错API”接口的使用方法。
### 4.1 接口鉴权
  示例要调用服务的数据为：{"text":"睡交吃饭"}
  则上述业务的参数列表如下：
	
<div class="code">
 <pre>{
        'Action' : 'LexicalCheck',
        'Nonce' : 345122,
        'Region' : 'sz',
        'SecretId' : 'AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA',
        'Timestamp' : 1408704141,
        'text': '睡交吃饭'
    }</pre>
</div>

  根据上述参数列表进行签名，得出的数字签名为：HgIYOPcx5lN6gz8JsCFBNAWp2oQ（示例），详细的数字签名的生成方法请参照：《腾讯云接口鉴权》。
>!
1. 在生成签名的过程中，需要将加密字符串中包含的“_”改写成“.”，从而加密产生签名；
2. 鉴权时，需要将参数列表按 key 进行排序：字典序，同时大写在前。

### 4.2 API 调用
  根据上一步（3.4.1）中得到的数字签名，以POST请求为例构造请求URL，将数字签名加入到参数Signature中。
	
  <div class="code">
 <pre>https://wenzhi.api.qcloud.com/v2/index.php?
	Action=LexicalCheck
	&Nonce=345122
	&Region=sz
	&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
	&Timestamp=1408704141
	&Signature=HgIYOPcx5lN6gz8JsCFBNAWp2oQ
	&text=睡交吃饭</pre>
</div>

  执行上述操作之后，会将数据{"text":"睡交吃饭"}发送给API接口，进行相应分析。
  <b>注意：</b>在发送请求过程中，不能将参数字符串中包含的“_”改写成“.”。
  上述指令返回的数据结构如下：
	
<div class="code">
 <pre>{
        "code": 0,
        "message": "",
        "conf": 1.3,
        "text": "睡觉吃饭",
        "text_annotate": "<em>睡觉</em>吃饭"
    }</pre>
</div>
