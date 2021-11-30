>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
本接口（DeleteSecurityGroup）用于删除新的安全组。
接口请求域名：<font style="color:red">dfw.api.qcloud.com</font>
1)安全组可以通过系统生成的唯一ID（前缀为sg的字符串）为索引来进行删除。只有当前账号下的安全组允许被删除。
2)安全组ID如果在其他安全组的规则中被引用，则无法直接删除。这种情况下，需要调用DescribeAssociateSecurityGroups查询出这些安全组，进行规则修改，再删除原来的安全组。
删除的安全组无法再找回，请谨慎调用。

 

## 2. 输入参数
 
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见公共请求参数页面。其中，此接口的Action字段为DeleteSecurityGroup。
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> sgId <td> 是 <td> String <td> 安全组唯一ID，可能来自DescribeSecurityGroups或者CreateSecurityGroup
</tbody></table>

 

## 3. 输出参数
 

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code <td> Int <td> 错误码, 0: 成功, 其他值: 失败
<tr>
<td> message <td> String <td> 错误信息
</tbody></table>

 ## 4. 错误码表
 <table class="t"><tbody><tr>
<th><b>错误码数值</b></th>
<th><b>原因</b></th>
<tr>

<td> 7000 <td> 安全组后台异常
<tr>
<td> 7001 <td> 安全组不存在
<tr>
<td> 7006 <td> 系统默认安全组禁止删除
</tbody></table>


## 5. 示例
 
输入
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=DeleteSecurityGroup
  &sgId=sg-c3y9ak17
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>

</pre>

输出
```

{
    "code": 0,
    "message": ""
}

```

