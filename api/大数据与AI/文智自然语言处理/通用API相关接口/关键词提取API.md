## 1. 接口描述
接口请求域名：wenzhi.api.qcloud.com
本接口（TextKeywords）基于关键词抽取平台，为用户实现诸如新闻内容关键词自动提取、评论关键词提取等提供基础服务。目前已经接入的业务包括腾讯新闻客户端、手机腾讯网等。

## 2. 输入参数
<table class="t">
<tr>
<th width="80"> <b>参数名称</b>
</th><th width="50"> <b>必选</b>
</th><th width="80"> <b>类型</b>
</th><th colspan="2"> <b>描述</b>
</th></tr>
<tr>
<td> title </td><td> 是 </td><td> String </td><td colspan="2">新闻标题
</td></tr>
<tr>
<td rowspan="15">channel </td><td rowspan="15">否 </td><td rowspan="15">String </td><td colspan="2"> 新闻频道(选填 不填默认是科技)
</td></tr>
<tr>
<td> CHnews_news_sports </td><td> 体育新闻
</td></tr>
<tr>
<td> CHnews_news_ent </td><td> 娱乐新闻
</td></tr>
<tr>
<td> CHnews_news_astro </td><td> 星座新闻
</td></tr>
<tr>
<td> CHnews_news_auto </td><td> 汽车新闻
</td></tr>
<tr>
<td> CHnews_news_cul </td><td> 文化新闻
</td></tr>
<tr>
<td> CHnews_news_digi </td><td> 数码新闻
</td></tr>
<tr>
<td> CHnews_news_finance </td><td> 财经新闻
</td></tr>
<tr>
<td> CHnews_news_game </td><td> 游戏新闻
</td></tr>
<tr>
<td> CHnews_news_house </td><td> 房产新闻
</td></tr>
<tr>
<td> CHnews_news_lad </td><td> 时尚新闻
</td></tr>
<tr>
<td> CHnews_news_mil </td><td> 军事新闻
</td></tr>
<tr>
<td> CHnews_news_ssh </td><td> 社会新闻
</td></tr>
<tr>
<td> CHnews_news_tech </td><td> 科技新闻
</td></tr>
<tr>
<td> CHnews_news_others </td><td> 其它
</td></tr>
<tr>
<td> content </td><td> 是 </td><td> String </td><td colspan="2">新闻正文
</td></tr></table>


## 3. 输出参数
<table class="t">
<tr>
<th width="80"> <b>参数名称</b>
</th><th width="100"> <b>类型</b>
</th><th colspan="4"> <b>参数描述</b>
</th></tr>
<tr>
<td> code
</td><td>Int32
</td><td colspan="4">错误码，0：成功, 其他值：失败
</td></tr>
<tr>
<td> message
</td><td> String
</td><td colspan="4">错误信息
</td></tr>
<tr>
<td rowspan="5">keywords
</td><td rowspan="5">Array
</td><td colspan="4">关键词提取结果，其中 Array 元素包含以下字段
</td></tr>
<tr>
<td> score
</td><td> Double
</td><td colspan="2">关键词权重
</td></tr>
<tr>
<td> keyword
</td><td> String
</td><td colspan="2"> 关键词提取服务对文本标记的标签
</td></tr>
<tr>
<td rowspan="2">type
</td><td rowspan="2">String
</td><td> keyword
</td><td> 文本中出现的关键词
</td></tr>
<tr>
<td> topic
</td><td> 话题
</td></tr></table>


  关键词提取 API 错误码详细信息如下：
<table class="t">
<tr>
<th width="50"> <b>错误码</b>
</th><th width="100"> <b>含义说明</b>
</th></tr>
<tr>
<td> 400 </td><td> HTTP Method 不正确
</td></tr>
<tr>
<td> 401 </td><td> HTTP 请求参数不符合要求
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
<th width="100"> <br />
</th><th width="80"> <b>参数名称</b>
</th><th width="100"> <b>参数描述</b>
</th><th width="50"> <b>必选</b>
</th><th width="150"> <b>参数值示例</b>
</th></tr>
<tr>
<td rowspan="4">腾讯云公共参数 </td><td> Action </td><td> 方法名 </td><td> 是 </td><td> TextKeywords
</td></tr>
<tr>
<td> SecretId  </td><td> Secret 的 ID </td><td> 是 </td><td> AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
</td></tr>
<tr>
<td> Timestamp </td><td> 当前时间戳 </td><td> 是 </td><td> 1408704141
</td></tr>
<tr>
<td> Nonce </td><td> 随机正整数 </td><td> 是 </td><td> 345122
</td></tr>
<tr>
<td rowspan="3">业务参数 </td><td> title </td><td> 新闻标题 </td><td> 是 </td><td> Dior 新款，秋冬新款娃娃款甜美圆领配毛领毛呢大衣外套、码数：SM、P330
</td></tr>
<tr>
<td> channel </td><td> 新闻频道(选填 不填默认是科技) </td><td> 否 </td><td> <br />
</td></tr>
<tr>
<td> content </td><td> 新闻正文 </td><td> 是 </td><td> Dior 新款，秋冬新款娃娃款甜美圆领配毛领毛呢大衣外套、码数：SM、P330
</td></tr></table>


  下面以上述业务为例，详细说明“关键词提取API”接口的使用方法。
	
### 4.1 接口鉴权
  示例要调用服务的数据为：{"title":"Dior新款，秋冬新款娃娃款甜美圆领配毛领毛呢大衣外套、码数：SM、P330","content":"Dior新款，秋冬新款娃娃款甜美圆领配毛领毛呢大衣外套、码数：SM、P330"}
  则上述业务的参数列表如下：
	
  <div class="code">
 <pre>{
        'Action' : 'TextKeywords',
        'Nonce' : 345122,
        'Region' : 'sz',
        'SecretId' : 'AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA',
        'Timestamp' : 1408704141,
        'title': 'Dior新款，秋冬新款娃娃款甜美圆领配毛领毛呢大衣外套、码数：SM、P330',
        'content': 'Dior新款，秋冬新款娃娃款甜美圆领配毛领毛呢大衣外套、码数：SM、P330'
    }</pre>
</div>

根据上述参数列表进行签名，得出的数字签名为：HgIYOPcx5lN6gz8JsCFBNAWp2oQ（示例），详细的数字签名的生成方法请参照 [接口鉴权](https://cloud.tencent.com/document/product/271/2053)。
>!
- 在生成签名的过程中，需要将加密字符串中包含的“_”改写成“.”，从而加密产生签名。
- 鉴权时，需要将参数列表按 key 进行排序：字典序，同时大写在前。

### 4.2 API 调用
根据上一步中得到的数字签名，以 POST 请求为例构造请求 URL，将数字签名加入到参数 Signature 中。
	
<div class="code">
<pre>https://wenzhi.api.qcloud.com/v2/index.php?
	Action=TextKeywords
	&Nonce=345122
	&Region=sz
	&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
	&Timestamp=1408704141
	&Signature=HgIYOPcx5lN6gz8JsCFBNAWp2oQ
	&title=Dior新款，秋冬新款娃娃款甜美圆领配毛领毛呢大衣外套、码数：SM、P330
	&content=Dior新款，秋冬新款娃娃款甜美圆领配毛领毛呢大衣外套、码数：SM、P330</pre>
</div>

  执行上述操作之后，会将数据{"title":"Dior新款，秋冬新款娃娃款甜美圆领配毛领毛呢大衣外套、码数：SM、P330","content":"Dior新款，秋冬新款娃娃款甜美圆领配毛领毛呢大衣外套、码数：SM、P330"}发送给API接口，进行相应分析。
>!在发送请求过程中，不能将参数字符串中包含的“_”改写成“.”。
 
上述指令返回的数据结构如下：
<div class="code">
<pre> {
        "code": 0,
        "message": "",
        "keywords": [
            {
                "keyword": "p330",
                "score": 0.2800000011920929,
                "type": "keyword"
            },
            {
                "keyword": "dior",
                "score": 0.2784992158412933,
                "type": "keyword"
            },
            {
                "keyword": "毛领",
                "score": 0.2746416926383972,
                "type": "keyword"
            }
        ]
    }</pre>
</div>
