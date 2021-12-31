### 实例管理相关接口
<table>
<thead>
<tr>
<th align="left" style="width:15%">API 名称及描述</th>
<th align="left" style="width:10%">资源类型</th>
<th align="left">资源六段式示例</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/41572">CreateInstance</a><br>创建实例</td>
<td align="left">instance</td>
<td align="left"><code>qcs::tcr:$region:$account:instance/$instanceid</code></td>
</tr>
<tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/41570">DescribeInstanceStatus</a><br>查询实例状态</td>
<td align="left">instance</td>
<td align="left"><code>qcs::tcr:$region:$account:instance/*</code>  <code>qcs::tcr:$region:$account:instance/$instanceid</code></td>
</tr>
<tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/41569">DescribeInstances</a><br>查询实例信息</td>
<td align="left">instance</td>
<td align="left"><code>qcs::tcr:$region:$account:instance/*</code>  <code>qcs::tcr:$region:$account:instance/$instanceid</code></td>
</tr>
<tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/41571">CreateInstanceToken</a><br>创建实例访问凭证</td>
<td align="left">instance</td>
<td align="left"><code>qcs::tcr:$region:$account:instance/$instanceid</code></td>
</tr>
<tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/42912">DeleteInstanceToken</a><br>删除长期访问凭证</td>
<td align="left">instance</td>
<td align="left"><code>qcs::tcr:$region:$account:instance/$instanceid</code></td>
</tr>
<tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/42910">ModifyInstanceToken</a><br>更新实例长期访问凭证</td>
<td align="left">instance</td>
<td align="left"><code>qcs::tcr:$region:$account:instance/$instanceid</code></td>
</tr>
<tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/42911">DescribeInstanceToken</a><br>查询长期访问凭证信息</td>
<td align="left">instance</td>
<td align="left"><code>qcs::tcr:$region:$account:instance/$instanceid</code></td>
</tr>
</tbody></table>


### 命名空间相关接口
<table>
<tr>
<th align="left" style="width:15%">API 名称及描述</th>
<th align="left" style="width:10%">资源类型</th>
<th align="left">资源六段式示例</th>
</tr>
<tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/42729">CreateNamespace</a><br>创建命名空间</td>
<td align="left">repository</td>
<td align="left"><code>qcs::tcr:$region:$account:repository/$instanceId/$namespaceName</code></td>
</tr>
<tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/42728">DeleteNamespace</a><br>删除命名空间</td>
<td align="left">repository</td>
<td align="left"><code>qcs::tcr:$region:$account:repository/$instanceId/$namespaceName</code></td>
</tr>
<tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/42727">ModifyNamespace</a><br>更新命名空间信息</td>
<td align="left">repository</td>
<td align="left"><code>qcs::tcr:$region:$account:repository/$instanceId/$namespaceName</code></td>
</tr>
<tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/42765">DescribeNamespaces</a><br>查询命名空间信息</td>
<td align="left">repository</td>
<td align="left">
<code>qcs::tcr:$region:$account:repository/$instanceId/*</code><br><code>qcs::tcr:$region:$account:repository/$instanceId/$namespaceName</code></td>
</tr>
</table>

### 镜像仓库相关接口
<table>
<tr>
<th align="left" style="width:15%">API 名称及描述</th>
<th align="left" style="width:10%">资源类型</th>
<th align="left">资源六段式示例</th>
</tr>
<tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/42725">CreateRepository</a><br>创建镜像仓库</td>
<td align="left">repository</td>
<td align="left">
<code>qcs::tcr:$region:$account:repository/$instanceId/$namespaceName/$repositoryName</code></td>
</tr>
<tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/42724">DeleteRepository</a><br>删除镜像仓库</td>
<td align="left">repository</td>
<td align="left">
<code>qcs::tcr:$region:$account:repository/$instanceId/$namespaceName/$repositoryName</code></td>
</tr>
<tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/42721">ModifyRepository</a><br>更新镜像仓库信息</td>
<td align="left">repository</td>
<td align="left">
<code>qcs::tcr:$region:$account:repository/$instanceId/$namespaceName/$repositoryName</code></td>
</tr>
<tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/42723">DescribeImages</a><br>查询容器镜像信息</td>
<td align="left">repository</td>
<td align="left">
<code>qcs::tcr:$region:$account:repository/$instanceId/$namespaceName/$repositoryName/*</code></td>
</tr>
<tr>
<td align="left"><a href="https://cloud.tencent.com/document/product/1141/42722">DescribeImages</a><br>查询镜像仓库信息</td>
<td align="left">repository</td>
<td align="left">
<code>qcs::tcr:$region:$account:repository/$instanceId/$namespaceName/*</code><br>
<code>qcs::tcr:$region:$account:repository/$instanceId/$namespaceName/$repositoryName</code></td>
</tr>
</table>





