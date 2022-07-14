### 命名空间相关接口
<table>
<thead>
<tr>
<th align="left"  style="width:39%">API 名称及描述</th>
<th align="left" style="width:1%">资源<br>类型</th>
<th align="left" style="width:58%">资源六段式示例</th>
</tr>
</thead>
<tbody><tr>
<td align="left">CreateNamespacePersonal<br>创建个人版命名空间</td>
<td align="left">repo</td>
<td align="left"><code>qcs::tcr:$region:$account:repo/$namespace</code></td>
</tr>
<tr>
<td align="left">DeleteNamespacePersonal<br>删除个人版命名空间</td>
<td align="left">repo</td>
<td align="left"><code>qcs::tcr:$region:$account:repo/$namespace</code></td>
</tr>
</tbody></table>

### 镜像仓库相关接口
<table>
<thead>
<tr>
<th align="left" style="width:49%">API 名称及描述</th>
<th align="left" style="width:1%">资源<br>类型</th>
<th align="left" style="width:49%">资源六段式示例</th>
</tr>
</thead>
<tbody><tr>
<td align="left">DescribeRepositoryOwnerPersonal<br>查询个人版所有仓库</td>
<td align="left">repo</td>
<td align="left"><code>qcs::tcr:$region:$account:repo/*</code></td>
</tr>
<tr>
<td align="left">CreateRepositoryPersonal<br>创建个人版镜像仓库</td>
<td align="left">repo</td>
<td align="left"><code>qcs::tcr:$region:$account:repo/$namespace/$repo</code></td>
</tr>
<tr>
<td align="left">DeleteRepositoryPersonal<br>删除个人版镜像仓库</td>
<td align="left">repo</td>
<td align="left"><code>qcs::tcr:$region:$account:repo/$namespace/$repo</code></td>
</tr>
<tr>
<td align="left">BatchDeleteRepositoryPersonal<br>批量删除个人版镜像仓库</td>
<td align="left">repo</td>
<td align="left"><code>qcs::tcr:$region:$account:repo/$namespace/*</code></td>
</tr>
<tr>
<td align="left">DeleteImagePersonal<br>删除个人版仓库 tag</td>
<td align="left">repo</td>
<td align="left"><code>qcs::tcr:$region:$account:repo/$namespace/$repo</code></td>
</tr>
<tr>
<td align="left">BatchDeleteImagePersonal<br>批量删除个人版仓库 tag</td>
<td align="left">repo</td>
<td align="left"><code>qcs::tcr:$region:$account:repo/$namespace/$repo</code></td>
</tr>
<tr>
<td align="left">PullRepositoryPersonal<br>拉取个人版镜像仓库内镜像</td>
<td align="left">repo</td>
<td align="left"><code>qcs::tcr:$region:$account:repo/$namespace/$repo</code></td>
</tr>
<tr>
<td align="left">PushRepositoryPersonal<br>推送个人版镜像仓库内镜像</td>
<td align="left">repo</td>
<td align="left"><code>qcs::tcr:$region:$account:repo/$namespace/$repo</code></td>
</tr>
</tbody></table>





