## 1. 接口描述
 
域名：trade.api.qcloud.com
接口名: DescribeAccountBalance

获取云账户信息。

 

## 2. 输入参数
 
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> 空
<td> --
<td> --
<td> --
</tbody></table>

 

## 3. 输出参数
 
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code
<td> Int
<td> 错误码，0：成功，其他值：失败
<tr>
<td> message
<td> String
<td> 错误信息
<tr>
<td> balanceInfo
<td> Int 
<td> 云账户信息中的”展示可用余额”字段，单位为"分"
</tbody></table>

 

## 4. 示例
 
输入

<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=DescribeAccountBalance
  &<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>


输出
```

  {
      "code":0,
      "message": "success",
      "balanceInfo":12345
  }

```

