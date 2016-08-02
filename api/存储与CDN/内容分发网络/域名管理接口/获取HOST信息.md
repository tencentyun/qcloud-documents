## 1. 接口描述
 
域名：cdn.api.qcloud.com
接口名: DescribeCdnHosts

获取对应账户下Host信息记录。

 

## 2. 输入参数
 
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>是否必填</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td>offset
<td> 否
<td> int
<td> 偏移量，默认为0
<tr>
<td> limit
<td> 否
<td> int
<td>返回数量，默认全部返回
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
  https://domain/v2/index.php?Action=DescribeCdnHosts&offset=0&limit=40
```

输出
```
  {
      "code":0,
      "message": "",
      "data":{}
  }

```


