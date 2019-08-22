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
<td> code </td><td> 是 </td><td> Int</td><td> text 的编码(0x00200000=utf-8) 目前文智统一输入为 utf-8
</td></tr>
<tr>
<td> type </td><td> 否 </td><td> Int </td><td>	取值 0 或 1，默认为 0。
0 为基础粒度版分词，倾向于将句子切分的更细，在搜索场景使用为佳。
1 为混合粒度版分词，倾向于保留更多基本短语不被切分开。
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
<td rowspan="7"> tokens
</td><td rowspan="7"> Array
</td><td colspan="4">分词结果 其中 Array 元素包含以下字段
</td></tr>
<tr>
<td> word
</td><td> String
</td><td colspan="2">切分出来的基础词
</td></tr>
<tr>
<td> pos
</td><td> UInt32
</td><td colspan="2">该基础词在文本中的起始位置，单位为字节数
</td></tr>
<tr>
<td> wtype
</td><td> String
</td><td colspan="2">基础词的词性，详细内容参照文末词性对照表
</td></tr>
<tr>
<td> wtype_pos
</td><td> UInt32
</td><td colspan="2">基础词的词性的 ID，与“ wtype ”对应，同参照文末词性对照表
</td></tr>
<tr>
<tr>
<td> wlen
</td><td> UInt64
</td><td colspan="2">该基础词的长度，单位为字节数，如：“我”为 2 个字节，该值为 2
</td></tr>
<tr>
<td rowspan="10"> combtokens
</td><td rowspan="10"> Array
</td><td colspan="4"> 命名实体识别结果 其中 Array 元素包含以下字段
</td></tr>
<tr>
<td> word
</td><td> String
</td><td colspan="2">实体词
</td></tr>
<tr>
<td> pos
</td><td> UInt32
</td><td colspan="2">该实体在文本中的起始位置，单位为字节数
</td></tr>
<tr>
<td> wlen
</td><td> UInt64
</td><td colspan="2">该实体词的长度，单位为字节数
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
<span id="postable"></span>
## 5. 词性对照表

| ID | 英文简写 | 含义 | 示例 |
|---------|---------|---------|---------|
|1 |	A	| 形容词	| 悲惨、宝贵啊、安恬 |
|	2	|	AD |	副形词	|	保障、不便、诚挚 |	
|	3	 |	AN	 |	名形词	 |	便捷、惨烈、产业化 |	
|	4 |		B	 |	区别词	 |	报复性、壁式、便民、半旧 |	
|	5 |	C	|	连词	|	比如、而、还有 |	
|	6	|	D	|	副词	|	不过、不管、必然|	
|	7	|	E	|	叹词	|	咦、呀、呀儿哟|	
|	8	|	F	|	方位词	|	顶端、侧后方、东南方|	
|	9	|	G	|	语素词	|	|	
|	10|		H	|	前接成分|		非、亚、前|	
|	11|		I	|	成语|		安于现状、哀鸿遍野、八仙过海|	
|	12	|	J	|	简称略语|		爱委会、奥申委、巴控区|	
|	13	|	K|		后接成分	|	级、期、症|	
|	14	|	L	|	习用语	|	安于现状、按需分配、八旗子弟|	
|	15 |	M |	数词	|	八旬、百儿八十、半拉|	
|	16	|	N	|	名词	|	电视、小说、程序|	
|	17	|	NR	|	人名	|	阿布穆萨、陈宏子、王雪|	
|	18	|	NRF	|	姓|		赵、张、李|	
|	19	|	NRG |		名	|	|	
|	20	|	NS	|	地名	|	阿根廷、北京、李家屯|	
|	21	|	NT	|	机构团体	|	公牛队、澳联社、财政部|	
|	22	|	NZ	|	其他专名	|	阿贾克斯、阿里朗、阿波罗|	
|	23	|	NX	|	字母词	|	B2C、 .net、 3D|	
|	24	|	O	|	拟声词	|	叮咣、叭哒、丁丁当当|	
|	25	|	P	|	介词	|	除了、对于、经|	
|	26	|	Q	|	量词	|	盎司、便士、帕|	
|	27	|	R	|	代词	|	鄙人、别国、俺|	
|	28	|	S	|	处所词	|	场外、村口、杯中|	
|	29	|	T	|	时间词	|	春秋、半夜、北汉|	
|	30	|	U	|	助词	|	着、的、地|	
|	31	|	V	|	动词	|	安排、暸望、哀悼|	
|	32	|	VD	|	副动词	|	标准化、濒临、鼎力|	
|	33	|	VN	|	名动词	|	罢免、拜年、败北|	
|	34	|	W	|	标点符号|		， ； 。 ...|	
|	35	|	X	|	非语素字	|	鸳、枇、蚣|	
|	36	|	Y	|	语气词	|	嘛、呢、呀|	
|	37	|	Z	|	状态词	|	本本分分、不羁、半死|	
|	38	|	AG	|	形语素	|	地、鼎、瘆|	
|	39	|	BG	|	区别语素|		赝、雄、当|	
|	40	|	DG|		副语素|		陡、务、劲|	
|	41|		MG	|	数词性语素|		丁、戊、辰|	
|	42	|	NG	|	名语素	|	餐、采、旙|	
|	43	|	QG	|	量语素	|	票、闾、仞|	
|	44	|	RG	|	代语素|		伊、或、汝|	
|	45	|	TG	|	动语素	|	雍、今、金|	
|	46	|	VG	|	量语素	|	朘、崇、僈|	
|	47	|	YG	|	语气词语素	|	咧、耳、尔|	
|	48	|	ZG	|	状态词语素	|	         ||	

