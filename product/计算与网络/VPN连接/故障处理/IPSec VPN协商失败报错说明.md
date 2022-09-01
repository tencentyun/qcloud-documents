<table>
<tr>
<td class="confluenceTd">协商阶段</td>
<td class="confluenceTd">错误提示信息</td>
<td class="confluenceTd">说明</td>
</tr>
<tr>
<td rowspan="5" >IKE 协商</td>
<td colspan="1" >no match proposal</td>
<td >云侧和客户侧配置的IKE策略一致，请检查。</td>
</tr>
<tr>
<td>DH group not supported</td>
<td>客户侧配置的DH组云侧不支持，请修改您本地配置。</td>
</tr>
<tr>
<td colspan="1" >responder no peer config found by ID payload</td>
<td>云侧配置的【本端标识】和【对端标识】与客户侧配置的不一致，致使响应方无应答。</td>
</tr>
<tr>
<td colspan="1" >initiator no peer config found by ID payload</td>
<td>云侧配置的【本端标识】和【对端标识】与客户侧配置的不一致，致使请求方无应答。</td>
</tr>
<tr>
<td>received xxx error notify</td>
<td>云侧收到客户侧协商失败的报文。</td>
</tr>
<tr>
<td colspan="1" rowspan="4">IPSec 协商</td>
<td colspan="1" >DH group xxx not supported</td>
<td >客户侧配置的DH组云侧不支持，请修改您本地的DH组。</td>
</tr>
<tr>
<td colspan="1" >reponder no matching CHILD_SA config for TS</td>
<td>云侧和客户侧配置的ts不一致，请检查。</td>
</tr>
<tr>
<td colspan="1" >no matching proposal, configured xxx, received xxx</td>
<td>云侧和客户侧配置的child不匹配。</td>
</tr>
<tr>
<td class="confluenceTd">received xxx error notify in the payload</td><td class="confluenceTd">云侧收到客户侧协商失败的报文。</td>
</tr>
</table>
