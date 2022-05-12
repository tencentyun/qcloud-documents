### WHOIS 中域名状态的解释说明
查看域名 [WHOIS 信息](https://whois.cloud.tencent.com/) 时，都有一项**域名状态**栏，每一个域名都有当前的状态，可能只有一个状态，也可能有多个状态。了解各种域名状态的含义，有助于您了解域名处于不同状态下的原因，可及时采取相应解决措施。

以下视频将为您介绍 WHOIS 中的域名状态：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2534-43061?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

分别有以下几种情况：
<table>
<tr>
<th style="width:25%">主要状态</th>
<th>说明</th>
</tr>
<tr>
<td>以 client 开头</td>
<td>由注册商发起。</td>
</tr>
<tr>
<td>以 server 开头</td>
<td>由注册局发起。</td>
</tr>
<tr>
<td>ACTIVE（OK）</td>
<td>普通状态（正常，没有需要立即进行的操作，也没有设置任何保护措施，当有其他状态时 OK 状态不显示，但并不代表不正常）。</td>
</tr>
<tr>
<td>addPeriod</td>
<td>注册局设置的域名新注册期。域名新注册后5天内会出现该状态，不影响域名使用，5天后将自动解除该状态。</td>
</tr>
<tr>
<td>INACTIVE</td>
<td>非激活状态（注册时未设置域名服务器，无法进行解析）。</td>
</tr>
</table>

**域名注册信息的保护，域名在进行某些安全锁定后，会出现以下状态：**
- 以 client 开头的状态：
<table>
<tr>
<th style="width:25%">client 开头</th>
<th>说明</th>
</tr>
<tr>
<td>clientDeleteProhibited</td>
<td>注册商设置禁止删除。</td>
</tr>
<tr>
<td>clientUpdateProhibited</td>
<td>注册商设置禁止修改（不允许修改域名信息，可以设置或修改解析记录）。</td>
</tr>
<tr>
<td>clientTransferProhibited</td>
<td>注册商设置禁止转移（注册商处设置不允许转出）。</td>
</tr>
</table>
- 以 server 开头的状态：
<table>
<tr>
<th style="width:25%">server 开头</th>
<th>说明</th>
</tr>
<tr>
<td>serverDeleteProhibited</td>
<td>注册局设置禁止删除。</td>
</tr>
<tr>
<td>serverUpdateProhibited</td>
<td>注册局设置禁止修改（不允许修改域名信息，可以设置或修改解析记录）。</td>
</tr>
<tr>
<td>serverTransferProhibited</td>
<td>注册局设置禁止转移（有的域名新注册及转移注册商在60天内会被注册局设置该状态，60天后自动解除；有的则是域名涉及仲裁或诉讼案被注册局设置，仲裁或诉讼案结束会被解除）。</td>
</tr>
</table>

**还有一些禁止解析、禁止续费的状态：**
<table>
<tr>
<th style="width:25%">部分禁止状态</th>
<th>说明</th>
</tr>
<tr>
<td>clientRenewProhibited</td>
<td>注册商设置禁止续费（域名不能被续费，通常处于该状态表示该域名处于仲裁或法院争议期，需联系注册商确认原因）。</td>
</tr>
<tr>
<td>clientHold</td>
<td>注册商设置暂停解析，联系注册商解除该状态。</td>
</tr>
<tr>
<td>serverRenewProhibited</td>
<td>注册局设置禁止续费（域名不能被续费，通常处于该状态表示该域名处于仲裁或法院争议期，需联系注册商确认原因）。</td>
</tr>
<tr>
<td>serverHold</td>
<td>注册局设置暂停解析（大多原因是.com、.cn、.net 等域名未进行实名认证，完成实名审核后自动解除该状态，更多原因可参考 <a href='https://cloud.tencent.com/document/product/242/54080'>域名注册局设置停止解析（serverHold）状态</a>）。</td>
</tr>
<tr>
<td>pendingTransfer</td>
<td>注册局设置转移过程中。</td>
</tr>
<tr>
<td>pendingVerification</td>
<td>注册信息确认中（域名未完成实名审核，或实名审核未通过，期间会影响解析。如域名注册后 5 天内仍未完成实名，则将进入 serverHold 状态，无法正常解析）。</td>
</tr>
</table>

### 域名过期的状态
域名过期状态有以下几种情况：
<table>
<tr>
<th style="width:35%">域名过期状态</th>
<th>说明</th>
</tr>
<tr>
<td>REGISTRAR HOLD（注册商保留）</td>
<td>表示域名过期后30天左右，即俗称的 “域名续费期”。</td>
</tr>
<tr>
<td>REDEMPTION PERIOD（赎回宽限期）</td>
<td>表示域名续费期结束后进入30天左右的 “域名赎回期”。</td>
</tr>
<tr>
<td>AUTORENEWPERIOD（自动续费宽限期）</td>
<td>表示域名过期后30天左右，可以被续费。</td>
</tr>
<tr>
<td>PENDING DELETE</td>
<td>表示国际域名在赎回期结束之后域名将进入5天的待删除期，5天期满后域名被删除。</td>
</tr>
</tr>
<tr>
<td>REGISTRAR/REGISTRY LOCK</td>
<td>表示注册商/局域名锁定状态，过期后防止被转移注册商。</td>
</tr>
</table>

>?
>- 具体可前往 [腾讯云 DNS 解析 DNSPod](https://cloud.tencent.com/document/product/302) 和 [域名实名认证](https://cloud.tencent.com/document/product/242/6707) 了解。
- 如果问题还未解决，请加入 [DNSPod 官方用户群](https://cloud.tencent.com/document/product/242/57608#DNSPod) 并联系技术客服协助您解决。





