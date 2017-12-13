## 概述
黑石弹性公网IP 支持细化到实例级别的权限管理，你可以为人员分配管理特定弹性公网IP 实例的权限；或者属于特定 VPC 的所有弹性公网IP的 管理权限。

## 预设策略
预设策略，能帮助你快速授权，而不需要编写策略，但授权粒度会粗些，以下是黑石弹性公网IP 的两个预设策略，分别为：
<table >
 <tr>
    <th>预设策略名</th>
    <th>授权范围描述</th>

 </tr>
<tr>
<td>QcloudBMEIPFullAccess</td>
<td>关联后，获得所有黑石弹性公网IP 实例的增、删、改、查等操作的权限</td>
</tr>

<tr>
<td>QcloudBMEIPReadOnlyAccess</td>
<td>关联后，只能获得查询黑石弹性公网IP列表及基本信息的权限</td>
</tr>

</table>


## Action 、Resource、Condtion 列表
以下表格，罗列了在配置 黑石弹性公网IP 的策略时，需要用到的 action 、 resource、condition。相关概念请参考《[访问管理](https://cloud.tencent.com/document/product/598/10603 "访问管理")》章节

Action ，即操作，对应的是 API 。编写策略时，你可以复制表格里内容并粘贴在 Action 字段中。关联该策略后，即可获得特定 API 的调用权限<br/>

Resource ，即云资源，当列表中 ACtion 的鉴权参数不为空时，则表示在调用 API 需要指定云资源，否则则不需要指定。编写策略时，你可以复制表格里内容并粘贴在策略生成器的 Resource 字段中，但请记得替换 $EipId、$InstanceId 为真实的实例 ID ；关联该策略后，即可获得特定资源的操作权限<br/>

注意：
>部份 API 鉴权时需要两种类型的实例 ID，例如绑定 EIP ，分别需要 被绑定的黑石服务器 以及 用于绑定的黑石弹性公网IP 的实例 ID，这时>
>需要把两种云产品的资源描述都写在 Resource 里*


Condition,即生效条件。换句话说 Action 和 Resource 需要在特定的生效条件下，才能鉴权通过。你可以灵活使用 condtion 以做到 VPC 或者 Subnet 粒度的权限管理，比如授权人员管理特定 VPC 内的所有黑石服务器

注意：
>特别说明：Describe* 或者 Get* 指查询操作，比如拉取多个实例详情等，查询操作鉴权通过后可能会把所有实例信息都返回，而无法区别哪些是有权限哪些是没有权限的实例。但再修改、删除实例时，会再次鉴权。
 
<table >
 <tr>
    <th>Action</th>
    <th>鉴权参数</th>
	<th>功能描述</th>
	<th>条件密钥</th>
 </tr>

  <tr>
    <td>bmeip:EipBmUnBindVpcIp</td>
    <td> qcs::bmeip:::eipId/$EipId</td>
	<td> 黑石EIP解绑VPCIP虚拟机或者托管</td>
	<td> bmvpc : unVpcId</td>
	
 </tr>
 
  <tr>
    <td>bmeip:EipBmBindVpcIp</td>
    <td> qcs::bmeip:::eipId/$EipId</td>
	<td>黑石EIP绑定VPCIP（虚拟机或者托管）</td>
	<td>  bmvpc : unVpcId</td>
	
 </tr>
 
 <tr>
    <td>bm:UnbindEip</td>
    <td> qcs::bmeip:::eipId/$EipId <br/> qcs::bm:::instance/$InstanceId</td>
	<td>解绑黑石EIP</td>
	<td>  bmvpc : unVpcId</td>
	
 </tr>
 
  <tr>
    <td>bm:BindEip</td>
    <td> qcs::bmeip:::eipId/$EipId <br/> qcs::bm:::instance/$InstanceId</td>
	<td>绑定黑石EIP</td>
	<td>  bmvpc : unVpcId</td>
	
 </tr>
 
   <tr>
    <td>bmeip:EipBmModifyCharge</td>
    <td> qcs::bmeip:::eipId/$EipId</td>
	<td>黑石EIP修改计费方式</td>
	<td>  bmvpc : unVpcId</td>
	
 </tr>
 
    <tr>
    <td>bmeip:ModifyEipAlias</td>
    <td> qcs::bmeip:::eipId/$EipId</td>
	<td>更新黑石EIP名称</td>
	<td>  bmvpc : unVpcId</td>
	
 </tr>
 

 
 <tr>
    <td>bmeip:EipBmDelete</td>
    <td>qcs::bmeip:::eipId/$EipId</td>
	<td>释放黑石EIP</td>
	<td> bmvpc : unVpcId</td>
	
 </tr>
 
  <tr>
    <td>bmeip:EipBmApply</td>
    <td>qcs::bmvpc:::unVpcId/vpc-xxx</td>
	<td>创建黑石EIP</td>
	<td> </td>	
 </tr>

   <tr>
    <td>bmeip:DescribeEipBm</td>
    <td></td>
	<td>黑石EIP查询接口</td>
	<td> </td>
	
 </tr>
 
 </table>


## Condition (生效条件）

灵活使用 Condtion，即可做到 Vpc  粒度的权限管理，比如授权管理特定 Vpc 内的黑石弹性公网 IP 实例

> 在使用 Condtion 时，做到 Vpc  粒度的授权，策略的 Resource 字段建议只需填写 " * "
 

## 书写规范

```
 "condition": 
{
"Option1": {"key1": ["value1","value2"]) , "key2": ["value1","value2"])},
"Option2": {"key1": ["value1","value2"]) , "key2": ["value1","value2"])}
}
```

Option 即 操作符，理解为传入的鉴权参数和 key 的运算规则  <br/>
Key 和 Value 是对应的，以下是对应关系。传入的鉴权参数经过运算后应该满足 key 和 value 的要求

<table>
<tr><th>key</th><th>value</th></tr>
<tr><td> bmvpc：unVpcId</td><td>vpc-yyyyyy (Vpc 的实例 Id)</td></tr>
</table>

### 操作符(Option)
黑石弹性公网 IP 只推荐使用 `for\_all\_value:string_equal\_if\_exist` </br>

for\_all\_value:string_equal\_if\_exist，用于condition 有一个 key 多个value的情况 key:value1,value2，可以做到多个 vpc 或者 subnet 的授权 


### 例子
策略如下：

```  
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "bmeip:EipBmModifyCharge"
            ],
            "resource": [
               "*"
            ],
            "condition": {
                "string_equal": {
                    "bmvpc:unVpcId": "vpc-34cxlz7z"
                }
            }
        }
    ]
}
``` 

场景： 调用 EipBmModifyCharge 修改 vpc-34cxlz7z 的任一 EIP实例的别名。<br/>

评估逻辑：
1. 鉴权逻辑关联了 effect:allow 的策略且 action : bm:EipBmModifyCharge 和 resource:*，即允许 修改任一实例的别名。<br/>
2. 但前提是，实例要在 vpc-34cxlz7z里才能鉴权通过<br/>



## 最佳实践
本章节，我们举例两个场景的 策略内容和评估逻辑，帮助你了解如何实现黑石服务器的权限分配

场景1： 授权 释放 eip-adt6pq7f
场景2： 授权 绑定 vpc-34cxlz7z 和 vpc-muinpf9p 里内所有的 物理服务器和EIP 

### 场景1
策略如下：
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "bmeip:EipBmDelete"
            ],
            "resource": [
                "qcs::bmeip:::eipId/eip-adt6pq7f"
            ]
        }
    ]
}
```

评估逻辑：

当调用 EipBmDelete 时，CAM 会判断传入的 EipId 是否为 eip-adt6pq7f，【是】则鉴权通过；【否】则鉴权失败

 
### 场景2
策略如下：
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "bm:BindEip",
                "bm:UnbindEip"
            ],
            "resource": [
                "*"
            ],
            "condition": {
                "for_all_value:string_equal_if_exist": {
                    "bmvpc:unVpcId": [
                        "vpc-34cxlz7z",
                        "vpc-muinpf9p"
                    ]
                }
            }
        }
    ]
}
```

评估逻辑：
当调用 BindEip 时，CAM 会对传入的 instanceId和EipID 做鉴权，发现满足 resource（*）的要求。
但要求 instanceId和EipID 在 vpc-34cxlz7z 或者 vpc-muinpf9p 里，【是】则鉴权通过；【否】则鉴权失败

