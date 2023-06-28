<table>
<tr>
<th class="confluenceTd">协商阶段</th>
<th class="confluenceTd">错误提示信息</th>
<th class="confluenceTd">说明</th>
</tr>
<tr>
<td rowspan="5" >IKE 协商</td>
<td colspan="1" >no match proposal</td>
<td >云侧和客户侧配置的 IKE 策略不一致，请检查。</td>
</tr>
<tr>
<td>DH group not supported</td>
<td>客户侧配置的 DH 组云侧不支持，请修改您本地配置。</td>
</tr>
<tr>
<td colspan="1" >responder no peer config found by ID payload</td>
<td>云侧配置的<b>本端标识</b>和<b>对端标识</b>与客户侧配置的不一致，致使响应方无应答。</td>
</tr>
<tr>
<td colspan="1" >initiator no peer config found by ID payload</td>
<td>云侧配置的<b>本端标识</b>和<b>对端标识</b>与客户侧配置的不一致，致使请求方无应答。</td>
</tr>
<tr>
<td>received xxx error notify</td>
<td>云侧收到客户侧协商失败的报文。</td>
</tr>
<tr>
<td colspan="1" rowspan="4">IPSec 协商</td>
<td colspan="1" >DH group xxx not supported</td>
<td >客户侧配置的 DH 组云侧不支持，请修改您本地的 DH 组。</td>
</tr>
<tr>
<td colspan="1" >reponder no matching CHILD_SA config for TS</td>
<td>云侧和客户侧配置的 ts 不一致，请检查。</td>
</tr>
<tr>
<td colspan="1" >no matching proposal, configured xxx, received xxx</td>
<td>云侧和客户侧配置的 child 不匹配。</td>
</tr>
<tr>
<td class="confluenceTd">received xxx error notify in the payload</td><td class="confluenceTd">云侧收到客户侧协商失败的报文。</td>
</tr>
</table>
