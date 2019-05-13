## 1. 接口描述
域名：wenzhi.api.qcloud.com
接口名: TextSensitivity <br />
识别信息的色情、政治等敏感程度。可用于敏感信息过滤，舆情监控等。
>?敏感词库自动更新，暂不支持客户自定义。

## 2. 输入参数
<table class="t">
<tr>
<th width="80"> <b>参数名称</b>
</th><th width="50"> <b>必选</b>
</th><th width="80"> <b>类型</b>
</th><th width="300"> <b>描述</b>
</th></tr>
<tr>
<td> content </td><td> 是 </td><td> String </td><td> 待分析的文本（只能为utf8编码）
</td></tr><td> type </td><td> 是 </td><td> int </td><td> 区分敏感词类型:1表示色情，2表示政治
</td></table>

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
<td> message</td><td> String </td><td>	失败时候的错误信息，成功则无该字段</a>
</td></tr>
<tr>
<td>sensitive</td><td> Double </td><td> 敏感的概率
</td></tr>
<tr>
<td> nonsensitive </td><td> Double </td><td> 不敏感的概率
</td></tr></table>




## 4. 示例
输入

```
https://wenzhi.api.qcloud.com/v2/index.php?
	Action=TextSensitivity
	&Nonce=345122
	&Region=sz
	&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
	&Timestamp=1408704141
	&Signature=HgIYOPcx5lN6gz8JsCFBNAWp2oQ
	&content=***********
	&type=2
```

输出
	

```
{
   "code": 0,
   "message": "",
   "sensitive": 0.7310585786300049,
   "nonsensitive": 0.2689414213699951
}
```
