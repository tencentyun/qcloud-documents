### 策略语法
```
{     
      "version":"2.0", 
      "statement": 
      [ 
         { 
            "effect":"effect", 
            "action":["action"], 
            "resource":["resource"], 
             "condition": {"key":{"value"}} 
         } 
     ] 
} 
```

<table>
<tr>
<th width="25%">元素</th><th>说明</th>
</tr>
<tr>
<td>version（版本）</td><td>必填项，目前仅允许值为"2.0"。</td>
</tr>
<tr>
<td>statement（语句）</td><td>是用来描述一条或多条权限的详细信息。该元素包括 effect、action、resource，condition 等多个其他元素的权限或权限集合。一条策略有且仅有一个 statement 元素。</td>
</tr>
<tr>
<td>effect（影响）</td><td>必填项，描述声明产生的结果是“允许”还是“显式拒绝”。包括 allow（允许）和 deny（显式拒绝）两种情况。</td>
</tr>
<tr>
<td>action（操作）</td><td> 必填项，描述允许或拒绝的操作。操作可以是 API（以 name 前缀描述）或者功能集（一组特定的 API，以 permid 前缀描述）。</td>
</tr>
<tr>
<td>resource（资源）</td><td> 必填项，描述授权的具体数据。资源是用六段式描述。每款产品的资源定义详情会有所区别。有关如何指定资源的信息，请参阅您编写的资源声明所对应的产品文档。</td>
</tr>
<tr>
<td>condition（生效条件）</td><td> 非必填项，描述策略生效的约束条件。条件包括操作符、操作键和操作值组成。条件值可包括时间、IP 地址等信息。有些服务允许您在条件中指定其他值。</td>
</tr>
</table>


### 轻量应用服务器访问管理策略示例
以下策略授予查看轻量应用服务器实例列表权限，及禁止用户 xxxxxx 查看 `lhins-e31oxxxx` 实例详情。 
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "lighthouse:DescribeInstances"
            ],
            "resource": [
                "*"
            ]
        },
        {
            "effect": "deny",
            "action": [
                "lighthouse:DescribeInstances"
            ],
            "resource": [
                "qcs::lighthouse::uin/xxxxxx:instance/lhins-e31oxxxx"
            ]
        }
    ]
}
```

### 轻量应用服务器资源路径
每个轻量应用服务器策略语句都有适用于自己的资源。资源路径的一般形式如下：
```
qcs:project_id:service_type:region:account:resource
```
**project_id**：描述项目信息，仅为了兼容 CAM 早期逻辑，无需填写。
**service_type**：产品简称，如 lighthouse。
**region**：地域信息，如 ap-guangzhou。
**account**：资源拥有者的根帐号信息，如 uin/xxxxxx。
**resource**：各产品的具体资源详情，如 instance/instance_id1 或者 instance/*。

