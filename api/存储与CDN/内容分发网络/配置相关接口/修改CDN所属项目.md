## 1. 接口描述
 
域名：cdn.api.qcloud.com
接口名:UpdateCdnProject

完成CDN接入后，需要修改HOST对应的所属项目。

 

## 2. 输入参数
 
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> projectId
<td> 是
<td> Int
<td> 需修改的对应项目的项目Id
<tr>
<td> hostId
<td> 是
<td> Int
<td> 需修改对应Host的HostId
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
  https://domain/v2/index.php?Action=UpdateCdnProject
  &hostId=1024
  &projectId=1234
```

输出
```
  {
      "code":0,
      "message": "",
  }

```


