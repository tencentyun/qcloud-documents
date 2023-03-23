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
<td><a href="#S">标准型实例族</a></td>
<td>
<ul style="margin-bottom: 0;">
 <li><a href="#S6">标准型 SA4</a> </li>
</ul>
</td>
<td>均衡的计算、内存和网络资源，可满足大多数场景下的应用资源需求</td>
</tr>
</table>
</div>
<blockquote class="doc-tip"><p class="doc-tip-tit"><i class="doc-icon-tip"></i>说明：</p><p>该实例规格族正在邀测中，欢迎您的建议与反馈 <a href="https://cloud.tencent.com/apply/p/jxftjls5x3">（SA4实例测试使用调查问卷）</a>。</p>
</blockquote>
</div>
</div>

<div class="sect1">
	<h2 id="S">标准型实例族</h2>
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
									<h3 id="S6">标准型 SA4</h3>
									<div class="paragraph">
									<p>标准型 SA4 实例是最新一代的标准型实例，基于全新优化虚拟化平台，提供了平衡、稳定的计算、内存和网络资源，是众多应用程序的最佳选择。</p>
									<p>标准型 SA4 实例采用的AMD EPYC™ Genoa全新处理器，内存采用最新 DDR5，默认网络优化，最高内网收发能力达4500万pps，最高内网带宽可支持100Gbps。
</p>
									</div>
									<div class="sect3">
										<h4 id="_实例特点">实例特点</h4>
										<div class="ulist">
											<ul>
												<li>
												<p>新一代腾讯云自研星星海双路服务器，搭配AMD EPYC™ Genoa处理器</p>
												</li>
												<li>
												<p>采用 AMD EPYC™ Genoa 处理器，主频2.6GHz，睿频3.6GHz</p>
												</li>
												<li>
													<p>提供1：2和1：4等多种处理器和内存的配比</p>
												</li>
												<li>
													<p>最高可支持100G内网带宽、4500万PPS，超高网络收发包能力，满足超高的内网传输需求</p>
												</li>
												<li>
													<p>实例网络性能与规格对应，规格越高网络转发性能越强，内网带宽上限越高</p>
												</li>
												<li>
													<p>支持关闭或开启超线程配置</p>
												</li>
											</ul>
										</div>
									</div>
									<div class="sect3">
										<h4 id="_使用场景">使用场景</h4>
										<div class="paragraph">
											<p>标准型 SA4 实例可应用于以下场景：：</p>
										</div>
										<div class="ulist">
											<ul>
												<li>
													<p>各种类型和规模的企业级应用</p>
												</li>
												<li>
													<p>中小型数据库系统、缓存、搜索集群</p>
												</li>
												<li>
													<p>计算集群、依赖内存的数据处理</p>
												</li>
												<li>
													<p>高网络包收发场景，如视频弹幕、直播、游戏等</p>
												</li>
											</ul>
										</div>
									</div>
									<div class="sect3">
										<h4 id="_实例要求">实例要求</h4>
										<div class="ulist">
											<ul>
												<li>
													<p>SA4 实例可以用作包年包月实例和按量计费实例。</p>
												</li>
												<li>
													<p>仅支持在私有网络中启动 SA4 实例。</p>
												</li>
												<li>
													<p>推荐搭配 TencentOS Server 操作系统，以发挥出实例的最优应用表现。</p>
												</li>
												<li>
													<p>SA4 实例支持购买配置，请参阅下侧实例规格。确保您选择的 SA4 实例大小达到您的操作系统和应用程序的最低 CPU 内存要求。在许多使用案例中，带有消耗大量内存和 CPU 资源的图形用户界面的操作系统（例如 Windows）可能需要更大的实例大小。随着您的工作负载对内存和 CPU 的需求随着时间增加，您可以扩展到更高的配置或选用其他类型实例。</p>
												</li>
												<li>
													<p>实例最高100G的网络带宽，依赖实例操作系统内核版本及运行环境的支持。当 pps 超过1000万，带宽大于50Gbps时，内核协议栈对网络性能损耗较大，此时 netperf 测试的带宽值可能不符合预期，可以用 DPDK 的方法屏蔽云服务器内核协议栈的差异，获取实例的真实网络性能。测试方法请参见 <a href="https://cloud.tencent.com/document/product/213/56297">高吞吐网络性能测试 。</a></p>
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
        <td>SA4.2XLARGE16</td>
        <td>8</td>
        <td>16</td>
        <td>90万</td>
        <td>30万</td>
        <td>8</td>
        <td>2</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SA4.2XLARGE32</td>
        <td>8</td>
        <td>32</td>
        <td>90万</td>
        <td>30万</td>
        <td>8</td>
        <td>2</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SA4.4XLARGE32</td>
        <td>16</td>
        <td>32</td>
        <td>180万</td>
        <td>60万</td>
        <td>16</td>
        <td> 4</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SA4.4XLARGE64</td>
        <td>16</td>
        <td>64</td>
        <td>180万</td>
        <td>60万</td>
        <td>16</td>
        <td>4</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SA4.8XLARGE64</td>
        <td>32</td>
        <td>64</td>
        <td>370万</td>
        <td>130万</td>
        <td>32</td>
        <td>8</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SA4.8XLARGE128</td>
        <td>32</td>
        <td>128</td>
        <td>270万</td>
        <td>130万</td>
        <td>32</td>
        <td>8</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SA4.16XLARGE128</td>
        <td>64</td>
        <td>128</td>
        <td>750万</td>
        <td>260万</td>
        <td>48</td>
        <td>17</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SA4.16XLARGE256</td>
        <td>64</td>
        <td>256</td>
        <td>750万</td>
        <td>260万</td>
        <td>48</td>
        <td>17</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SA4.24XLARGE192</td>
        <td>96</td>
        <td>192</td>
        <td>1120万</td>
        <td>400万</td>
        <td>48</td>
        <td>25</td>
        <td>-</td>
    </tr>
    <tr>
        <td>SA4.48XLARGE384</td>
        <td>192</td>
        <td>384</td>
        <td>2250万</td>
        <td>800万</td>
        <td>48</td>
        <td>50</td>
        <td>-</td>
    </tr>
</table></div></td>
</tr>
</tbody>
</table>
