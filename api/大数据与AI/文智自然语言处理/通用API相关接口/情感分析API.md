## 1. 接口描述
接口请求域名：wenzhi.api.qcloud.com
本接口（TextSentiment）用于舆情监控、话题监督、口碑分析等商业分析领域，具有非常重要的应用价值。

## 2. 输入参数
<table class="t">
<tr>
<th width="80"> <b>参数名称</b>
</th><th width="50"> <b>必选</b>
</th><th width="80"> <b>类型</b>
</th><th width="500"> <b>描述</b>
</th></tr>
<tr>
<td> content </td><td> 是 </td><td> String </td><td> 待分析的文本（只能为 utf8编码）
</td></tr><tr>
<td> type</td><td> 否 </td><td>Int </td><td> （可选参数，默认为4）
1：电商；2：APP；3：美食；4：酒店和其他。
</td></tr></table>

## 3. 输出参数
<table class="t">
<tr>
<th width="80"> <b>参数名称</b>
</th><th width="80"> <b>类型</b>
</th><th width="350"> <b>描述</b>
</th></tr>
<tr>
<td> code </td><td> Int32 </td><td> 错误码。0：成功，其他值：失败
</td></tr>
<tr>
<td> message</td><td> String </td><td> 错误信息</a>
</td></tr>
<tr>
<td> positive </td><td> Double </td><td> 正面情感概率
</td></tr>
<tr>
<td> negative </td><td> Double </td><td> 负面情感概率
</td></tr></table>




## 4. 示例
输入：
```
https://wenzhi.api.qcloud.com/v2/index.php?
	Action=TextSentiment
	&Nonce=345122
	&Region=sz
	&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
	&Timestamp=1408704141
	&Signature=HgIYOPcx5lN6gz8JsCFBNAWp2oQ
	&content=双万兆服务器就是好，只是内存小点	
```

输出：
```
{
   "code": 0,
   "message": "",
   "negative": 0.138263002038002,
   "positive": 0.8617370128631592
}
```
