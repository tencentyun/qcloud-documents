### 实例管理相关接口
<table>
<thead>
<tr>
<th align="left" style="width:15%">API 名称及描述</th>
<th align="left" style="width:10%">资源类型</th>
<th align="left">资源六段式示例</th>
</tr>
</thead>
<tbody><tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/41572">CreateInstance</a><br>创建实例</td>
<td align="left">instance</td>
<td align="left"><code>qcs::tcr:$region:$account:instance/$instanceid</code></td>
</tr>
<tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/41569">DescribeInstances</a><br>查询实例信息</td>
<td align="left">instance</td>
<td align="left"><code>qcs::tcr:$region:$account:instance/*</code>  <code>qcs::tcr:$region:$account:instance/$instanceid</code></td>
</tr>
<tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/41570">DescribeInstanceStatus</a><br>查询实例状态</td>
<td align="left">instance</td>
<td align="left"><code>qcs::tcr:$region:$account:instance/$instanceid</code></td>
</tr>
<tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/41571">CreateInstanceToken</a><br>获取临时登录密码</td>
<td align="left">instance</td>
<td align="left"><code>qcs::tcr:$region:$account:instance/$instanceid</code></td>
</tr>
</tbody></table>
