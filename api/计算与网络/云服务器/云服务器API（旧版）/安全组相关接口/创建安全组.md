>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
 
本接口（CreateSecurityGroup）用于创建新的安全组。
接口请求域名：<font style="color:red">dfw.api.qcloud.com</font>
1)每个账户下每个地域的每个项目的安全组[数量限制](https://cloud.tencent.com/doc/product/213/500#2.-.E5.AE.89.E5.85.A8.E7.BB.84.E7.9A.84.E9.99.90.E5.88.B6)。
2)安全组的唯一ID由系统自动生成；安全组名（输入的sgName字段）由您指定，最多25个UTF-8字符；安全组备注（输入的sgRemark字段）也由您指定，最多100个UTF-8字符，允许重复；如果您有多个项目，可以在创建安全组时选择项目ID（输入的projectId字段），不选择时即在您的默认项目中创建。
新建的安全组的入站和出站规则默认都是全部拒绝，在创建后通常您需要再调用ModifySecurityGroupPolicys将安全组的规则设置为需要的规则。

 

## 2. 输入参数
 
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见公共请求参数页面。其中，此接口的Action字段为CreateSecurityGroup。
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> sgName <td> 否 <td> String <td> 安全组名称，同项目下不可重名，可任意命名，但不得超过60个字符
<tr>
<td> sgRemark <td> 否 <td> String <td> 安全组备注，最多100个字符
<tr>
<td> projectId <td> 否 <td> Int <td> 项目id，默认0。可在用户中心->项目管理页面查询到
</tbody></table>

 

## 3. 输出参数
 | 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败 |
| message |   String | 错误信息 |
| data |   Object | 返回的数据结构|

<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>

<td> data.sgId <td> String <td> 安全组Id
<tr>
<td> data.sgName <td> String <td> 安全组名称
<tr>
<td> data.sgRemark <td> String <td> 安全组备注
</tbody></table>

## 4. 错误码表
 <table class="t"><tbody><tr>
<th><b>错误码数值</b></th>
<th><b>原因</b></th>
<tr>

<td> 7000 <td> 安全组后台异常
<tr>
<td> 7002 <td> 安全组个数已达上限
<tr>
<td> 7005 <td> 安全组名已存在
<tr>
<td> 9003 <td> 安全组名称/备注超长或包含非法字符
</tbody></table>

## 5. 示例
 
输入
<pre>

  https://dfw.api.qcloud.com/v2/index.php?Action=CreateSecurityGroup
  &projectId=1000379
  &sgName=组1
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>>

</pre>

输出
```

{
    "code": 0,
    "message": "",
    "data": {
        "sgId": "sg-c3y9ak17",
        "sgName": "组1",
        "sgRemark": ""
    }
}

```

