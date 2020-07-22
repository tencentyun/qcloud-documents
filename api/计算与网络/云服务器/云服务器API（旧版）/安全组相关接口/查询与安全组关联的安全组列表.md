>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
本接口（DescribeAssociateSecurityGroups）查询有哪些安全组的出站或入站规则中包含了输入的安全组 ID。
接口请求域名：<font style="color:red">dfw.api.qcloud.com</font>
1)如果某个安全组 ID 的查询结果非空，那么这个安全组不能被直接删除，需要先修改引用了这个 ID 的其他安全组规则。
安全组的规则如果包含了自身的 ID，不会在查询结果中出现。 

## 2. 输入参数
 
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见公共请求参数页面。其中，此接口的 Action 字段为DescribeAssociateSecurityGroups。
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> sgIds.n <td> 是 <td> String <td> 安全组 ID 列表
</tbody></table>

 

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码，0：成功，其他值：失败 |
| message |   String | 错误信息 |
| data |   Object | 返回的数据结构|

Data结构

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> data.key <td> String <td> key 为被关联安全组 ID
<tr>
<td> data.value <td> Array of String <td> value 为规则中包含了 data.key 安全组 ID 的安全组列表
</tbody></table>

 ## 4. 错误码表
 <table class="t"><tbody><tr>
<th><b>错误码数值</b></th>
<th><b>原因</b></th>
<tr>

<td> 7000 <td> 安全组后台异常
<tr>
<td> 9003 <td> 输入为空
</tbody></table>


## 5. 示例
 
输入
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=DescribeAssociateSecurityGroups
  &sgIds.0=sg-5ua9adfv
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>

</pre>

输出
```

{
	"code": 0,
	"message": "",
	"data": {
		"sg-5ua9adfv": ["sg-exnsygsn"]
	}
}

```

