## 1. 接口描述
  域名：wenzhi.api.qcloud.com
  接口名: LexicalAnalysis
	
提供智能分词（基本词和短语）、词性标注、命名实体识别功能。专业的团队对数据、模型、程序进行迭代更新以保证效果的不断提升。用户只需简单的调用相关API接口即可获取到所需结果，无需担心诸如新词发现、歧义消除、调用性能等词法分析难题。词法分析已经为应用宝搜索、微信公共账号搜索等业务提供支持，均取得了良好的效果。

## 2. 输入参数

<table class="t">
<tr>
<th width="80"> <b>参数名称</b>
</th><th width="30"> <b>必选</b>
</th><th width="80"> <b>类型</b>
</th><th width="450"> <b>描述</b>
</th></tr>
<tr>
<td> text </td><td> 是 </td><td> String </td><td> 待词法分析的文本
</td></tr>
<tr>
<td> code </td><td> 是 </td><td> Int</td><td> text的编码(0x00200000=utf-8) 目前文智统一输入为utf-8
</td></tr>
<tr>
<td> type </td><td> 否 </td><td> Int </td><td>	取值0或1，默认为0。
0为基础粒度版分词，倾向于将句子切分的更细，在搜索场景使用为佳。
1为混合粒度版分词，倾向于保留更多基本短语不被切分开。
</td></tr>
</table>


## 3. 输出参数
<table class="t">
<tr>
<th width="100"> <b>参数名称</b>
</th><th width="100"> <b>类型</b>
</th><th colspan="4"> <b>描述</b>
</th></tr>
<tr>
<td> code
</td><td> Int
</td><td colspan="4">错误码。0: 成功，其他值: 失败
</td></tr>
<tr>
<td> message
</td><td> String
</td><td colspan="4">错误信息
</td></tr>
<tr>
<td rowspan="5"> tokens
</td><td rowspan="5"> Array
</td><td colspan="4">分词结果 其中Array元素包含以下字段
</td></tr>
<tr>
<td> word
</td><td> String
</td><td colspan="2">切分出来的基础词
</td></tr>
<tr>
<td> pos
</td><td> UInt32
</td><td colspan="2">该基础词在文本中的起始位置
</td></tr>
<tr>
<td> wtype
</td><td> String
</td><td colspan="2">基础词的词性
</td></tr>
<tr>
<td> wlen
</td><td> Uint64
</td><td colspan="2">该基础词的长度
</td></tr>
<tr>
<td rowspan="10"> combtokens
</td><td rowspan="10"> Array
</td><td colspan="4"> 命名实体识别结果 其中Array元素包含以下字段
</td></tr>
<tr>
<td> word
</td><td> String
</td><td colspan="2">实体词
</td></tr>
<tr>
<td> pos
</td><td> UInt32
</td><td colspan="2">该实体在文本中的起始位置
</td></tr>
<tr>
<td> wlen
</td><td> UInt64
</td><td colspan="2">该实体词的长度基础词的词性
</td></tr>
<tr>
<td rowspan="6">cls
</td><td rowspan="6">Int32
</td><td> 人名
</td><td> 100000010/100000011
</td></tr>
<tr>
<td> 地名
</td><td> 100000012
</td></tr>
<tr>
<td> 机构名
</td><td> 100000013
</td></tr>
</table>

## 4. 示例
输入

```
https://wenzhi.api.qcloud.com/v2/index.php?
	Action=LexicalAnalysis
	&Nonce=345122
	&Region=sz
	&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
	&Timestamp=1408704141
	&Signature=HgIYOPcx5lN6gz8JsCFBNAWp2oQ
	&text=我爱洗澡
	&code=2097152
```

 
输出

```
 {
        "code": 0,
        "message": "",
        "combtokens": [
            {
                "cls": "短语",
                "pos": 0,
                "wlen": "8",
                "word": "我爱洗澡"
            }
        ],
        "tokens": [
            {
                "pos": 0,
                "wlen": "2",
                "word": "我",
                "wtype": "代词",
                "wtype_pos": 27
            },
            {
                "pos": 2,
                "wlen": "2",
                "word": "爱",
                "wtype": "动词",
                "wtype_pos": 31
            },
            {
                "pos": 4,
                "wlen": "4",
                "word": "洗澡",
                "wtype": "动词",
                "wtype_pos": 31
            }
        ]
    }	
```
