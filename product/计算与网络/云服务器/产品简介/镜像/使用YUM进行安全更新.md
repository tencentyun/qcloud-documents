## 操作场景
本文介绍如何使用 yum 查询、检查以及安装 TencentOS Server 操作系统的安全更新。

## 操作步骤
### 查询安全更新命令及参数
- 命令格式
```
yum updateinfo <command> [option]
```
- 参数及取值说明
<table>
<tr>
<th>参数</th>
<th>取值说明</th>
</tr>
<tr>
<td>command</td>
<td>
<ul class="params">
<li><code>list</code>：查询可用的安全更新列表。</li>
<li><code>info &lt;update_id&gt;</code>：查询指定的安全更新详情。</li>
</ul>
</td>
</tr>
<tr>
<td>option</td>
<td>
<ul class="params">
<li><code>--sec-severity=&lt;SEVS&gt; 或 --secseverity=&lt;SEVS&gt;</code>：指定安全更新级别，参数 &lt;SEVS&gt; 为指定的安全更新级别。</li>
<li><code>--cve=&lt;CVES&gt;</code>：指定 CVE ID。</li>
</ul>
</td>
</tr>
</table>
- 使用示例
执行以下命令，获取当前全部可用的安全更新信息。
```
yum updateinfo
```
返回类似如下结果：
```
Loaded plugins: fastestmirror
Determining fastest mirrors
tlinux                                                                                           | 3.6 kB  00:00:00     
tlinux-extras                                                                                    | 3.6 kB  00:00:00     
tlinux-os                                                                                        | 3.6 kB  00:00:00     
tlinux-updates                                                                                   | 3.6 kB  00:00:00     
(1/8): tlinux/2.4/x86_64/group_gz                                                                | 156 kB  00:00:00     
(2/8): tlinux-extras/2.4/x86_64/primary_db                                                       | 181 kB  00:00:00     
(3/8): tlinux-os/2.4/x86_64/group_gz                                                             | 156 kB  00:00:00     
(4/8): tlinux-extras/2.4/x86_64/group_gz                                                         | 156 kB  00:00:00     
(5/8): tlinux-updates/2.4/x86_64/group_gz                                                        | 156 kB  00:00:00     
(6/8): tlinux-updates/2.4/x86_64/primary_db                                                      | 1.9 MB  00:00:00     
(7/8): tlinux-os/2.4/x86_64/primary_db                                                           | 5.7 MB  00:00:00     
(8/8): tlinux/2.4/x86_64/primary_db                                                              |  11 MB  00:00:00     
updateinfo summary done
```

### 检查安全更新
执行以下命令，检查系统当前可用的安全更新信息。示例如下：
```
yum check-update --security |grep available
```
返回类似如下结果信息：
```
No packages needed for security; 197 packages available
```

### 安装安全更新
您可执行以下命令，安装安全更新。
```
yum upgrade --security
```
