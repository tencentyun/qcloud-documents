## 接口描述
 
- 域名：account.api.qcloud.com。
- 接口名：AddProject。
- 接口描述：添加项目。项目为一个虚拟概念，用户可以在一个账户下面建立多个项目，每个项目中管理不同的资源。一个账号下最多创建100个项目。

 

## 输入参数
 

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> projectName <td> 是 <td> String <td> 待添加的项目名称，名称只允许为“中文”、“英文”或者“数字” 三者组成
<tr>
<td> projectDesc <td> 否 <td> String <td> 待添加的项目描述
</tbody></table>

 

## 输出参数
 

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code <td> Int <td> 错误码，0：成功，其他值：失败
<tr>
<td> message <td> String <td> 错误信息
<tr>
<td> projectId <td> Int <td> 项目 ID
</tbody></table>

 

## 示例
 
### 输入
<pre>
  https://account.api.qcloud.com/v2/index.php?Action=AddProject
  &projectName=test
  &projectDesc=用于测试使用
  &<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>

### 输出
```

{
    "code": 0,
    "message": "",
    "projectId": 1002996
}

```
