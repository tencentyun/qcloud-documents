## 1. 接口描述
本接口(DescribeTaskInfo)用于查询任务结果
接口请求域名：<font style='color:red'>redis.api.qcloud.com </font>

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href='https://cloud.tencent.com/document/api/239/7200' title='公共请求参数'>公共请求参数</a>页面。其中，此接口的Action字段为DescribeTaskInfo。

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>是否必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> requestId<td> 是 <td> UInt <td> 任务ID
</tbody></table>

## 3. 输出参数
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code <td> Int <td>公共错误码, 0表示成功，其他值表示失败。详见错误码页面的<a href='https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81' title='公共错误码'>公共错误码</a>
<tr>
<td> message <td> String <td> 错误信息
<tr>
<td> codeDesc <td> String <td> 业务侧错误码英文描述。成功时返回Success，错误时返回具体业务错误原因
<tr>
<td> data <td> Array <td> 返回的数据数组
</tbody></table>

**data数组结构：**

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> data.status <td> Int <td> 任务状态0:待执行，1：执行中，2：成功，3：失败，-1 执行出错
</tbody></table>

## 4. 错误码
以下错误码表列出了该接口的业务逻辑错误码。

| 错误代码 | 英文提示 | 错误描述 |
|---------|---------|---------|
|11201|InvalidParameter|业务参数错误|

 
## 5. 示例
<pre>
https://redis.api.qcloud.com/v2/index.php?Action=DescribeTaskInfo
&<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>
&requestId=11963
</pre>
返回示例如下：
```
{
    "code": 0,
	"message": "",
	"codeDesc": "Success",
    "data": {
        "status": 2
    }
}
```
