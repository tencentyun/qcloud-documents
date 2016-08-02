## 1. 接口描述
 
域名：cdn.api.qcloud.com
接口名: GetCdnMiddleSourceList

获取实时的CDN中间源IP列表信息，每小时更新。

 

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
<td> 错误码, 0: 成功, 其他值: 失败
<tr>
<td> message
<td> String
<td> 错误信息
<tr>
<td> data
<td> Array
<td> 中间源列表
</tbody></table>

 

## 4. 示例
 
输入
```
  https://domain/v2/index.php?Action=GetCdnMiddleSourceList
```

输出
```
  {
      "code":0,
      "message": "",
      "data" : {}
  }

```


