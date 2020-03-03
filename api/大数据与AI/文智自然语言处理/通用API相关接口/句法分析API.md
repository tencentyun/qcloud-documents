>!
- 腾讯文智自然语言处理已于2019年7月09日全新升级为 [新版](https://cloud.tencent.com/document/product/271/3317)，接口功能更全面，服务更加稳定，且公测期间免费使用。
- 老版本接口将不再继续维护，将于2019年11月16日零点下线，建议您使用 [新版 API ](https://cloud.tencent.com/document/product/271/35484)，体验更优服务。
- 接口切换过程中，若您有相关问题，可加入官方 QQ 群（330130409）详细咨询。

## 1.接口描述
域名：wenzhi.api.qcloud.com
接口名: TextDependency
	
句法分析出句子中词与词之间的关系，可用于提取句子主干，提取句子核心词等。句法分析可以更好的理解句子，从而在机器翻译、自动问答、知识抽取等领域都可以应用。

## 2. 输入参数

|参数名称 | 必选 |类型 |描述|
|---------|---------|---------|---------|
| content | 是 | String |待分析的文本（只能为 utf8 编码）|

### 3. 输出参数
<table class="t">
<tr>
<th width="80"> <b>参数名称</b>

</th><th width="80"> <b>类型</b>
</th><th colspan="2"> <b>描述</b>
</th></tr>
<tr>
<td>id</td><td>  Int  </td><td colspan="2">节点id
</td></tr>
<tr>
<td>father_id</td><td>  Int  </td><td colspan="2">父节点id
</td></tr>
<tr>
<td rowspan="15">dep_rel </td><td rowspan="15">String </td>
<tr>
<td>SBV  </td><td> 主谓关系
</td></tr>
<tr>
<td> VOB </td><td> 动宾关系
</td></tr>
<tr>
<td> IOB </td><td> 间宾关系
</td></tr>
<tr>
<td> FOB </td><td> 前置宾语
</td></tr>
<tr>
<td> DBL </td><td> 兼语
</td></tr>
<tr>
<td> ATT </td><td> 定中关系
</td></tr>
<tr>
<td> ADV </td><td> 状中结构
</td></tr>
<tr>
<td> CMP </td><td> 动补结构
</td></tr>
<tr>
<td> COO </td><td> 并列关系
</td></tr>
<tr>
<td> POB </td><td> 介宾关系
</td></tr>
<tr>
<td> LAD </td><td> 左附加关系
</td></tr>
<tr>
<td> RAD </td><td> 右附加关系
</td></tr>
<tr>
<td> IS </td><td> 独立结构
</td></tr>
<tr>
<td> HED </td><td> 核心关系
</td></tr>
<tr>
<td> postag </td><td> String </td><td colspan="2">词性
</td></tr>
<tr>
<td> word </td><td> String </td><td colspan="2">词
</td></tr>
<tr>
<td> code  </td><td> Int </td><td colspan="2">0表示成功，非0表示失败
</td></tr><tr>
<td> message  </td><td> String </td><td colspan="2">失败时候的错误信息，成功则无该字段
</td></tr></table>

句法分析 API 错误码详细信息如下：

| 错误码 | 含义说明 | 
|---------|---------|
| 400| HTTP Method 不正确 | 
| 401| 	HTTP 请求参数不符合要求| 
| 503|调用额度已超出限制 | 
| 504| 服务故障 | 

## 4. 详细示例
  示例业务详细信息如下表：
	<table class="t">
<tr>
<th width="100"> <br />
</th><th width="80"> <b>参数名称</b>
</th><th width="120"> <b>参数描述</b>
</th><th width="50"> <b>必选</b>
</th><th width="150"> <b>参数值示例</b>
</th></tr>
<tr>
<td rowspan="4">腾讯云公共参数 </td><td> Action </td><td> 方法名 </td><td> 是 </td><td> TextDependency
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
<td rowspan="3">业务参数 </td>

<tr>
<td> content </td><td>待分析的文本（只能为utf8编码） </td><td> 是 </td><td>双万兆服务器就是好，只是内存小点
</td></tr></table>

  下面以上述业务为例，详细说明“句法分析API”接口的使用方法。
### 4.1 接口鉴权
示例要调用服务的数据为：{"content":"双万兆服务器就是好，只是内存小点"}
  则上述业务的参数列表如下：
	
   <div class="code">
 <pre>{
        'Action' : 'TextDependency',
        'Nonce' : 345122,
        'Region' : 'sz',
        'SecretId' : 'AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA',
        'Timestamp' : 1408704141,
        'content': '双万兆服务器就是好，只是内存小点'
    }</pre>
</div>

根据上述参数列表进行签名，得出的数字签名为：HgIYOPcx5lN6gz8JsCFBNAWp2oQ（示例），详细的数字签名的生成方法请参照：《腾讯云接口鉴权》。
>!
1. 在生成签名的过程中，需要将加密字符串中包含的“_”改写成“.”，从而加密产生签名；
2. 鉴权时，需要将参数列表按key进行排序：字典序，同时大写在前。
  
### 4.2 API 调用
  根据上一步（1.4.1）中得到的数字签名，以 POST 请求为例构造请求 URL，将数字签名加入到参数Signature中。
  
<div class="code">
 <pre>https://wenzhi.api.qcloud.com/v2/index.php?
	Action=TextDependency
	&Nonce=345122
	&Region=sz
	&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
	&Timestamp=1408704141
	&Signature=HgIYOPcx5lN6gz8JsCFBNAWp2oQ
	&content=双万兆服务器就是好，只是内存小点</pre>
</div>

  执行上述操作之后，会将数据{"content":"双万兆服务器就是好，只是内存小点"}发送给API接口，进行相应分析。
  <b>注意：</b>在发送请求过程中，不能将参数字符串中包含的“_”改写成“.”。
  上述指令返回的数据结构如下：
<div class="code">
 <pre> {
    "code": 0,
    "message": "",
    "keywords": [
        [
            {
                "dep_rel": "ATT",
                "father_id": 2,
                "id": 1,
                "postag": "m",
                "word": "双"
            },
            {
                "dep_rel": "ATT",
                "father_id": 3,
                "id": 2,
                "postag": "n",
                "word": "万兆"
            },
            {
                "dep_rel": "SBV",
                "father_id": 4,
                "id": 3,
                "postag": "n",
                "word": "服务器"
            },
            {
                "dep_rel": "HED",
                "father_id": 0,
                "id": 4,
                "postag": "v",
                "word": "就是"
            },
            {
                "dep_rel": "CMP",
                "father_id": 4,
                "id": 5,
                "postag": "a",
                "word": "好"
            },
            {
                "dep_rel": "WP",
                "father_id": 4,
                "id": 6,
                "postag": "w",
                "word": ","
            },
            {
                "dep_rel": "COO",
                "father_id": 4,
                "id": 7,
                "postag": "c",
                "word": "只是"
            },
            {
                "dep_rel": "ATT",
                "father_id": 9,
                "id": 8,
                "postag": "n",
                "word": "内存"
            },
            {
                "dep_rel": "VOB",
                "father_id": 7,
                "id": 9,
                "postag": "n",
                "word": "小点"
            }
        ]
    ]
}</pre>
</div>
