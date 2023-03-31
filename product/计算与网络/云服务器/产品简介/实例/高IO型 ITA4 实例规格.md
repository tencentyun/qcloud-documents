<div class="sect1">
	<h2 id="INSTANCETYPE">实例类型</h2>
	<div class="sectionbody">
		<div class="paragraph">
		</div>
		<div class="dlist">
<table>
<tr>
<th style="width: 18%;">类型</th>
<th style="width: 25%;">子类型</th>
<th>描述</th>
</tr>
<tr>
<td><a href="#S">高IO型实例族</a></td>
<td>
<ul style="margin-bottom: 0;">
 <li><a href="#S6">高IO型ITA4</a> </li>
</ul>
</td>
<td>具有高随机 IOPS、高吞吐量、低访问延时等特点，适合对硬盘读写和时延要求高的高性能数据库等 I/O 密集型应用</td>
</tr>
</table>
</div>
<blockquote class="doc-tip"><p class="doc-tip-tit"><i class="doc-icon-tip"></i>说明：</p><p>该实例规格族正在邀测中，欢迎您的建议与反馈 。</p>
</blockquote>
</div>
</div>

<div class="sect1">
	<h2 id="S">高IO型实例族</h2>
		<div class="sectionbody">
			<div class="paragraph">
</div>


<table class="tableblock frame-none grid-all spread custom-style">
				<colgroup>
					<col style="width: 100%;">
				</colgroup>
				<tbody>
					<tr>
						<td class="tableblock halign-left valign-top">
							<div>
								<div class="sect2">
									<h3 id="S6">高IO型实例族</h3>
									<div class="paragraph">
									<p>高 IO 型 ITA4 实例是专为 I/O 密集型工作负载设计的最新一代高 IO 型实例。基于 NVMe SSD 实例存储，以较低的成本提供低延迟、超高的 IOPS、高吞吐量的存储资源。适合高性能关系型数据库、Elasticsearch 等 IO 密集型业务。</p>
									</div>
									<div class="sect3">
										<h4 id="_实例特点">实例特点</h4>
										<div class="ulist">
											<ul>
												<li>
												<p>新一代腾讯云自研星星海双路服务器，搭配AMD EPYC™ Milan处理器</p>
												</li>
												<li>
												<p>采用 AMD EPYC™ Milan 处理器，睿频3.5GHz</p>
												</li>
												<li>
													<p>实例网络性能与规格对应，规格越高网络转发性能越强，内网带宽上限越高</p>
												</li>
												<li>
													<p>采用 NVMe SSD 的实例存储，提供低延迟、超高的 IOPS</p>
												</li>
											</ul>
										</div>
									</div>
									<div class="sect3">
										<h4 id="_使用场景">使用场景</h4>
										<div class="paragraph">
										</div>
										<div class="ulist">
											<ul>
												<li>
													<p>高性能数据库、NoSQL 数据库（例如 MongoDB）、群集化数据库</p>
												</li>
												<li>
													<p>联机事务处理（OLTP）系统、Elastic Search 搜索等需要低时延的 I/O 密集型应用</p>
												</li>
											</ul>
										</div>
									</div>
									<div class="sect3">
										<h4 id="_实例要求">实例要求</h4>
										<div class="ulist">
											<ul>
												<li>
													<p>若本地硬盘损坏，我们支持在线换盘操作。</p>
												</li>
												<li>
													<p>若云服务器实例已经宕机，我们会告知您并进行维修操作。</p>
												</li>
												<li>
													<p>ITA4 实例未安装监控组件会导致平台无法对实例进行更细致的监控，若实例发生故障则将无法正常通知，可能存在高危风险,请参考 <a 
href="https://cloud.tencent.com/document/product/248/6211">安装云服务器监控组件 </a>完成监控组件安装。</p>
												</li>
												<li>
													<p>ITA4实例可以用作包年包月实例和按量计费实例。</p>
												</li>
												<li>
													<p>仅支持在私有网络中启动 ITA4实例。</a></p>
												</li>
<li>
													<p>ITA4 实例不支持调整配置及关机不计费功能。</a></p>
												</li>
<li>
													<p>ITA4 实例支持购买配置，请参阅下方实例规格。</a></p>
												</li>
		</li>
<li>
													<p>实例最高100G的网络带宽，依赖实例操作系统内核版本及运行环境的支持。当 pps 超过1000万，带宽大于50Gbps时，内核协议栈对网络性能损耗较大，此时 netperf 测试的带宽值可能不符合预期，可以用 DPDK 的方法屏蔽云服务器内核协议栈的差异，获取实例的真实网络性能。测试方法请参见<a 
href="https://cloud.tencent.com/document/product/213/56297"> 高吞吐网络性能测试 </a> </p>
												</li>
											</ul>
										</div>
									</div>
									<div class="sect3">
										<h4 id="__a_href_instancetype_回到顶部_a">&nbsp; &nbsp;<a href="#INSTANCETYPE">回到顶部</a></h4>
									</div>
								</div>
							</div>
						</td>
					</tr>
					<tr>
						<td class="tableblock halign-left valign-top">
							<div>
	<table>
<colgroup>
										<col style="width: 20%;">
										<col style="width: 10%;">
										<col style="width: 10%;">
										<col style="width: 10%;">
										<col style="width: 10%;">
										<col style="width: 10%;">
										<col style="width: 10%;">
										<col style="width: 10%;">
									</colgroup>
    <tr>
        <td>规格</td>
        <td>vCPU</td>
        <td>内存（GB）</td>
        <td>网络收发包（pps）（出+入）</td>
        <td>连接数</td>
        <td>队列数</td>
        <td>内网带宽能力（Gbps）（出+入）</td>
        <td>备注</td>
    </tr>
    <tr>
        <td>ITA4.4XLARGE64</td>
        <td>16</td>
        <td>64</td>
        <td>170万</td>
        <td>100万</td>
        <td>16</td>
        <td>6</td>
        <td>	1 × 7140GB 本地 NVMe SSD 硬盘</td>
    </tr>
    <tr>
        <td>ITA4.8XLARGE128</td>
        <td>32</td>
        <td>128</td>
        <td>350万</td>
        <td>200万</td>
        <td>32</td>
        <td>13</td>
        <td>	2 × 7140GB 本地 NVMe SSD 硬盘</td>
    </tr>
    <tr>
        <td>ITA4.16XLARGE256</td>
        <td>64</td>
        <td>256</td>
        <td>700万</td>
        <td>400万</td>
        <td>48</td>
        <td>25</td>
        <td>4 × 7140GB 本地 NVMe SSD 硬盘</td>
    </tr>
    <tr>
        <td>ITA4.32XLARGE512</td>
        <td>128</td>
        <td>512</td>
        <td>1400万</td>
        <td>800万</td>
        <td>48</td>
        <td>50</td>
        <td>8 × 7140GB 本地 NVMe SSD 硬盘</td>
    </tr>
</table></div></td>
</tr>
</tbody>
</table>
