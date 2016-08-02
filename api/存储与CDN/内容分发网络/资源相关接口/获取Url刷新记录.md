## 1. 接口描述
 
域名：cdn.api.qcloud.com
接口名: GetCdnRefreshLog

查询某段时间内的Url历史刷新记录。

 

## 2. 输入参数
 
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> startDate
<td> 是
<td> String
<td> 查询开始时间
<tr>
<td> endDate
<td> 是
<td> String
<td> 查询结束时间
<tr>
<td> url
<td> 否
<td> String
<td> 需要查询的Url（可为空）
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
</tbody></table>

 

## 4. 示例
 
输入
```
  https://domain/v2/index.php?Action=GetCdnRefreshLog
  &startDate=2015-04-20 00:00:00
  &endDate=2015-04-20 23:59:59 
  &url=www.gomezshuitest.com
```

输出
```
  {
      "code":0,
      "message": "",
  }

```


