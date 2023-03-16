由于访问控制接口变更，以下接口将逐步切换为最新版本。如果您最近正在使用相关接口，请尽快替换为最新版本：

<table>
<thead>
<tr>
<th rowspan=2 >归属模块</th>
<th colspan=2 >原接口</th>
<th colspan=2 >新接口</th>
</tr>
<tr>
<th>接口名称</th>
<th>接口功能</th>
<th>接口名称</th>
<th>接口功能</th>
</tr>
</thead>
<tbody>
<tr>
<td>互联网访问控制规则</td>
<td><a href="https://cloud.tencent.com/document/product/1132/49070">CreateAcRules</a></td>
<td>创建访问控制规则</td>
<td><a href="https://cloud.tencent.com/document/product/1132/61922">AddAcRule</a></td>
<td>添加互联网边界规则</td>
</tr>
<tr>
<td>NAT 访问控制规则</td>
<td><a href="https://cloud.tencent.com/document/product/1132/49070">CreateAcRules</a></td>
<td>创建访问控制规则</td>
<td><a href="https://cloud.tencent.com/document/product/1132/86861">AddNatAcRule</a></td>
<td>添加 NAT 访问控制规则</td>
</tr>
<tr>
<td>NAT 访问控制规则</td>
<td><a href="https://cloud.tencent.com/document/product/1132/49064">ModifyAcRule</a></td>
<td>修改规则</td>
<td><a href="https://cloud.tencent.com/document/product/1132/86859">ModifyNatAcRule</a></td>
<td>修改 NAT 访问控制规则</td>
</tr>
<tr>
<td>NAT 访问控制规则</td>
<td><a href="https://cloud.tencent.com/document/product/1132/49069">DescribeAcLists</a></td>
<td>访问控制列表</td>
<td><a href="https://cloud.tencent.com/document/product/1132/86860">DescribeNatAcRule</a></td>
<td>查询 NAT 访问控制列表</td>
</tr>
<tr>
<td>NAT 访问控制规则</td>
<td><a href="https://cloud.tencent.com/document/product/1132/49062">ModifySequenceRules</a></td>
<td>修改规则执行顺序</td>
<td><a href="https://cloud.tencent.com/document/product/1132/86970">ModifyNatSequenceRules</a></td>
<td>NAT 防火墙规则快速排序</td>
</tr>
<tr>
<td>NAT 访问控制规则</td>
<td><a href="https://cloud.tencent.com/document/product/1132/49063">ModifyAllRuleStatus</a></td>
<td>启用停用全部规则</td>
<td>无变化</td>
<td>-</td>
</tr>
<tr>
<td>NAT 访问控制规则</td>
<td><a href="https://cloud.tencent.com/document/product/1132/49058">DeleteAllAccessControlRule</a></td>
<td>全部删除规则</td>
<td><a href="https://cloud.tencent.com/document/product/1132/86858">RemoveNatAcRule</a></td>
<td>删除 NAT 访问控制规则</td>
</tr>
<tr>
<td>NAT 访问控制规则</td>
<td><a href="https://cloud.tencent.com/document/product/1132/49059">DeleteAcRule</a></td>
<td>删除规则</td>
<td><a href="https://cloud.tencent.com/document/product/1132/86858">RemoveNatAcRule</a></td>
<td>删除 NAT 访问控制规则</td>
</tr>
</tbody></table>
