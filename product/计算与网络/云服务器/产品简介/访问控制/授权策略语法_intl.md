
<span id = "celueyufa"></span>
### Policy Syntax
CAM policy:

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
- **version** is required. Now, the only available value is "2.0".
- **statement** describes details of one or multiple permissions. This element includes permission or permission set for other elements such as effect, action, resource, and condition. One policy can only have one statement element.
 1. **action** describes allowed or rejected actions. An action can be an API (described using the prefix "name") or a feature set (a set of specific APIs, described using the prefix "permid"). This element is required.
 2. **resource** describes the detailed data of authorization. Resource is described using 6-piece format. Detailed resource definition for each product is different. For more information on how to specify resource, please see the product documentation corresponding to your resource declaration. This element is required.
 3. **condition** describes the condition for the policy to take effect. Condition consists of operator, operational key and operate value. Condition value may include information such as time and IP address. Some services allow you to specify other values in the condition. This element is optional.
 4. **effect** describes whether the result produced by the declaration is "Allow" or "Explicitly Deny". This includes two situations: allow, deny. This element is required.

<span id = "caozuo"></span>
### CVM Operations

In CAM policy statements, you can specify any API operation from any service that supports CAM. For CVM, use API prefixed with name/cvm:. For example: name/cvm:RunInstances or name/cvm:ResetInstancesPassword.
To specify multiple operations in a single statement, separate them with commas as shown below:
```
"action":["name/cvm:action1","name/cvm:action2"]
```
You can also specify multiple operations with a wildcard. For example, you can specify all operations whose name starts with the word "Describe" as follows:
```
"action":["name/cvm:Describe*"]
```
To specify all operations in CVM, use the wildcard "*" as follows:
```
"action":["name/cvm:*"]
```

<span id = "ziyuanlujing"></span> 
### CVM Resource Path
Each CAM policy statement has its own resources.
The general form of resource path is as follows:
```
qcs:project_id:service_type:region:account:resource
```
**project_id** describes the project information, which is only used to be compatible with the earlier CAM logics and is not required.
**service_type**: the abbreviation of the product, for example, CVM.
**region**: region information, for example, bj.
**account**: the root account information of the resource owner, for example, uin/164256472.
**resource**: detailed resource information of each product, for example, instance/instance_id1 or instance/*.

For example, you can specify a specific instance (i-15931881scv4) in the statement as follows:
```
"resource":[ "qcs::cvm:bj:uin/164256472:instance/i-15931881scv4"]
```
You can also use the wildcard "*" to specify all instances that belong to a specific account as shown below:
```
"resource":[ "qcs::cvm:bj:uin/164256472:instance/*"]
```

If you want to specify all resources or if any API operation does not support resource-level permission, you can use the wildcard "*" in Resource element as shown below:
```
"resource": ["*"]
```
To specify multiple resources in one instruction, separate them with commas. In the following example, two resources are specified:
```
"resource":["resource1","resource2"]
```
The following table describes the resources CVM can use and the corresponding resource description methods.
<style>
table th:nth-of-type(1){
width:250px;
}
table th:nth-of-type(2){
width:500px;
}
</style>
In the following table, the words prefixed with $ are all alternative names.
- "project" represents project ID.
- "region" represents region.
- "account" represents account ID.

| Resource | Resource description method in authorization policy |
|-------|-------|
| Instance | qcs::cvm:$region:$account:instance/$instanceId |
| Key | qcs::cvm:$region:$account:keypair/$keyId |
|VPC|  qcs::vpc:$region:$account:vpc/$vpcId|
| Subnet | qcs::vpc:$region:$account:vpc/$vpcId |
| System disk | qcs::cvm:$region:$account:systemdisk/* |
| Image | qcs::cvm:$region:$account:image/* |
| Subnet | qcs::vpc:$region:$account:subnet/$subnetId |
| Data disk | qcs::cvm:$region:$account:datadisk/* |
| Security group | qcs::cvm:$region:$account:sg/$sgId |
|EIP|  qcs::cvm:$region:$account:eip/*|

 

<span id = "tiaojianmiyue"></span>
### CVM Condition Keys
In a policy statement, you can selectively specify conditions for controlling the effective time of the policy. Each condition includes one or multiple key value pairs. Condition keys are case insensitive.

- If you specify multiple conditions or specify multiple keys in one condition, we make an evaluation with logical operation "AND".
- If you specify a key with multiple values in one condition, we make an evaluation with logical operation "OR". All conditions must be met to grant a permission.
The following table describes CVM condition keys for specific services.
<table class="tableblock frame-all grid-all spread">
<colgroup>
<col style="width: 25%;">
<col style="width: 25%;">
<col style="width: 50%;">
</colgroup>
<thead>
<tr>
<th class="tableblock halign-left valign-top">Condition keys</th>
<th class="tableblock halign-left valign-top">Types for reference</th>
<th class="tableblock halign-left valign-top">Key value pairs</th>
</tr>
</thead>
<tbody>
<tr>
<td class="tableblock halign-left valign-top"><div><div class="paragraph">
<p>cvm:instance_type</p>
</div></div></td>
<td class="tableblock halign-left valign-top"><div><div class="paragraph">
<p>String</p>
</div></div></td>
<td class="tableblock halign-left valign-top"><div><div class="paragraph">
<p>cvm:instance_type=<code>instance_type</code></p>
</div>
<div class="ulist">
<ul>
<li>
<p><code>Instance_type</code> represents instance type (for example, S1.SMALL1).</p>
</li>
</ul>
</div></div></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><div><div class="paragraph">
<p>cvm:image_type</p>
</div></div></td>
<td class="tableblock halign-left valign-top"><div><div class="paragraph">
<p>String</p>
</div></div></td>
<td class="tableblock halign-left valign-top"><div><div class="paragraph">
<p>cvm:image_type=<code>image_type</code></p>
</div>
<div class="ulist">
<ul>
<li>
<p><code>Image_type</code> represents image type (for example, IMAGE_PUBLIC).</p>
</li>
</ul>
</div></div></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><div><div class="paragraph">
<p>vpc:region</p>
</div></div></td>
<td class="tableblock halign-left valign-top"><div><div class="paragraph">
<p>String</p>
</div></div></td>
<td class="tableblock halign-left valign-top"><div><div class="paragraph">
<p>vpc:region=<code>region</code></p>
</div>
<div class="ulist">
<ul>
<li>
<p><code>region</code> represents region (for example, ap-guangzhou).</p>
</li>
</ul>
</div></div></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><div><div class="paragraph">
<p>cvm:disk_size</p>
</div></div></td>
<td class="tableblock halign-left valign-top"><div><div class="paragraph">
<p>Integer</p>
</div></div></td>
<td class="tableblock halign-left valign-top"><div><div class="paragraph">
<p>cvm:disk_size=<code>disk_size</code></p>
</div>
<div class="ulist">
<ul>
<li>
<p><code>disk_size</code> represents disk size (for example, 500).</p>
</li>
</ul>
</div></div></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><div><div class="paragraph">
<p>cvm:disk_type</p>
</div></div></td>
<td class="tableblock halign-left valign-top"><div><div class="paragraph">
<p>String</p>
</div></div></td>
<td class="tableblock halign-left valign-top"><div><div class="paragraph">
<p>cvm_disk_type=<code>disk_type</code></p>
</div>
<div class="ulist">
<ul>
<li>
<p><code>disk_type</code> represents disk type (for example, CLOUD_BASIC).</p>
</li>
</ul>
</div></div></td>
</tr>
<tr>
<td class="tableblock halign-left valign-top"><div><div class="paragraph">
<p>cvm:region</p>
</div></div></td>
<td class="tableblock halign-left valign-top"><div><div class="paragraph">
<p>String</p>
</div></div></td>
<td class="tableblock halign-left valign-top"><div><div class="paragraph">
<p>cvm:region=<code>region</code></p>
</div>
<div class="ulist">
<ul>
<li>
<p><code>region</code> represents region (for example, ap-guangzhou).</p>
</li>
</ul>
</div></div></td>
</tr>
</tbody>
</table>
