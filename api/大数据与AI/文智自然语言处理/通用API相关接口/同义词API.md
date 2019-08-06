## 1. 接口描述
  域名：wenzhi.api.qcloud.com
  接口名: LexicalSynonym
	
  为用户提供同义词查询服务，搜索团队通过全网数据挖掘出海量同义词，并持续对数据、模型等进行迭代更新，保证同义词的效果始终与时俱进。用户也可以通过提供产品专有的数据，与我们合作打造专属的同义词库。同义词服务作为搜索引擎检索串理解的基本功能，目前已经应用在视频、音乐、应用宝、群搜、商圈等数百个产品中。
## 2. 输入参数

| 参数名称 | 必选 | 类型 |描述 |
|---------|---------|---------|---------|
| text | 是 | 文本3 | 待分析的文本（目前文智统一输入为 utf-8） |



## 3. 输出参数
<table class="t">
<tr>
<th width="100"> <b>参数名称</b>
</th><th width="80"> <b>类型</b>
</th><th colspan="5"> <b>描述</b>
</th></tr>
<tr>
<td> code </td><td> Int32 </td><td colspan="5">错误码, 0: 成功, 其他值: 失败
</td></tr>
<tr>
<td> message </td><td> String </td><td colspan="5">错误信息
</td></tr>
<tr>
<td> query </td><td> String </td><td colspan="5">输入的原文本
</td></tr>
<tr>
<td rowspan="8"> syns </td><td rowspan="8"> Array </td><td colspan="5">同义词分析结果，其中Array元素包括以下字段
</td></tr>
<tr>
<td rowspan="4"> word_ori </td><td rowspan="4"> Object </td><td colspan="3">原词信息，包含以下字段
</td></tr>
<tr>
<td> idx_beg </td><td> Int32 </td><td> 起始位置
</td></tr>
<tr>
<td> idx_end </td><td> Int32 </td><td> 终止位置
</td></tr>
<tr>
<td> text </td><td> String </td><td>  提取的原词文本
</td></tr>
<tr>
<td rowspan="3">word_syns </td><td rowspan="3">Array </td><td colspan="3">原词对应的同义词列表，其中Array元素包含
</td></tr>
<tr>
<td> text </td><td> String </td><td> 同义词文本
</td></tr>
<tr>
<td> conf </td><td> Double </td><td> 同义词置信度
</td></tr></table>

同义词API错误码详细信息如下：<br />

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
<th width="100"> <br />
</th><th width="80"> <b>参数名称</b>
</th><th width="100"> <b>参数描述</b>
</th><th width="50"> <b>必选</b>
</th><th width="150"> <b>参数值示例</b>
</th></tr>
<tr>
<td rowspan="4">腾讯云公共参数 </td><td> Action </td><td> 方法名 </td><td> 是 </td><td> LexicalSynonym
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
<td> 业务参数 </td><td> text </td><td> 待分析的文本（目前文智统一输入为utf-8） </td><td> 是 </td><td> 张三结婚
</td></tr></table>


  下面以上述业务为例，详细说明“同义词API”接口的使用方法。
### 4.1 接口鉴权
  示例要调用服务的数据为：{"text":"张三结婚"}
  则上述业务的参数列表如下：
	
 <div class="code">
 <pre>{
        'Action' : 'LexicalSynonym',
        'Nonce' : 345122,
        'Region' : 'sz',
        'SecretId' : 'AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA',
        'Timestamp' : 1408704141,
        'text': '张三结婚'
    }</pre>
</div>

  根据上述参数列表进行签名，得出的数字签名为：HgIYOPcx5lN6gz8JsCFBNAWp2oQ（示例），详细的数字签名的生成方法请参照：《腾讯云接口鉴权》。
  <b>注意：</b>
  1）在生成签名的过程中，需要将加密字符串中包含的“_”改写成“.”，从而加密产生签名；
  2）鉴权时，需要将参数列表按key进行排序：字典序，同时大写在前。
### 4.2 API调用
  根据上一步（4.4.1）中得到的数字签名，以POST请求为例构造请求URL，将数字签名加入到参数Signature中。
  
<div class="code">
 <pre>https://wenzhi.api.qcloud.com/v2/index.php?
	Action=LexicalSynonym
	&Nonce=345122
	&Region=sz
	&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
	&Timestamp=1408704141
	&Signature=HgIYOPcx5lN6gz8JsCFBNAWp2oQ
	&text=张三结婚</pre>
</div>

  执行上述操作之后，会将数据{"text":"张三结婚"}发送给API接口，进行相应分析。
   <b>注意：</b>在发送请求过程中，不能将参数字符串中包含的“_”改写成“.”。
  上述指令返回的数据结构如下：
	
<div class="code">
 <pre>{
        "code": 0,
        "message": "",
        "syns": [
            {
                "word_ori": {
                    "idx_beg": 0,
                    "idx_end": 2,
                    "text": "张三"
                },
                "word_syns": [
                    {
                        "conf": 0.2000000029802322,
                        "text": "jay"
                    },
                    {
                        "conf": 0.2000000029802322,
                        "text": "张董"
                    }
                ]
            }
        ]
    }</pre>
</div>
