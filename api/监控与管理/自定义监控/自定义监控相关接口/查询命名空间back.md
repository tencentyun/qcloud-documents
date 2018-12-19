## 1. 接口描述
 
域名：monitor.api.qcloud.com
接口名: DescribeNamespace

查询所有自定义命名空间。

 

## 2. 输入参数
 
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<th><b>来源</b></th>
<tr>
<td> Action
<td> 是
<td> String
<td>操作接口名
<td>系统规定参数，此处取值：DescribeNamespace
</tbody></table>

## 3. 输出参数
 
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code
<td> Int
<td> 错误码, 0: 成功, 其他值: 失败
<tr>
<td> message
<td> String
<td> 错误信息
<tr>
<td> data
<td> Array
<td> 返回的命名空间数组
</tbody></table>

## 4. 示例
 
输入

<pre>
 https://monitor.api.qcloud.com/v2/index.php?Action=DescribeNamespace&<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>

输出
```
｛
'code': 0,
'message': ''
'data': [“name1”,”name2”]
｝
```

## 5. 错误码

| 返回值 | 说明 |
|---------|---------|
| -503 | 参数错误 | 
|-513 | DB操作失败 | 