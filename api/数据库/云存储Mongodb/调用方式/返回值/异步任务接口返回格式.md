## 普通异步任务接口返回格式
一次请求只能操作一个资源的异步任务接口，例如创建负载均衡，重置主机操作系统等。
<table class="t">
<tbody><tr>
<th> <b>名称</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th><th> <b>必选</b>
</th></tr>
<tr>
<td> code
</td><td> Int
</td><td> 返回结果的错误码，0表示成功，其它值表示失败
</td><td> Yes
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> 返回结果的错误信息
</td><td> No
</td></tr>
<tr>
<td> requestId
</td><td> String
</td><td> 任务编号
</td><td> Yes
</td></tr></tbody></table>

## 批量异步任务接口返回格式
一次请求能操作多个资源的异步任务接口，例如修改密码，启动机器，停止机器等。
<table class="t">
<tbody><tr>
<th> <b>名称</b>
</th><th> <b>类型</b>
</th><th> <b>描述</b>
</th><th> <b>必选</b>
</th></tr>
<tr>
<td> code
</td><td> Int
</td><td> 返回结果的错误码，0表示成功，其它值表示失败
</td><td> Yes
</td></tr>
<tr>
<td> message
</td><td> String
</td><td> 返回结果的错误信息
</td><td> No
</td></tr>
<tr>
<td> detail
</td><td> Array
</td><td> 以资源 ID 为 key，返回对该资源操作的 code，message，requestId
</td><td> Yes
</td></tr></tbody></table>

例如：

```
{
	"code": 0,
	"message": "success",
	"detail": {
		"qcvm6a456b0d8f01d4b2b1f5073d3fb8ccc0": {
			"code": 0,
			"message": "",
			"requestId": "1231231231231"
		},
		"qcvm6a456b0d8f01d4b2b1f5073d3fb8ccc0": {
			"code": 0,
			"message": "",
			"requestId": "1231231231232"
		}
	}
}
```
>!
>- 资源全部操作成功，则最外层 code 为0。
>- 资源全部操作失败，则最外层 code 会返回5100。
>- 资源部分操作失败，则最外层 code 会返回5400。
>- 在第3种情况下，终端可以通过 detail 得到失败部分的操作信息。
