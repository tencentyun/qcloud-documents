## 场景描述
广电 OTT 主要基于电视终端提供流媒体服务。该场景一般有下列核心诉求：
<table>
    <tr>
        <th>
            核心诉求              
        </th>
				<th>
           说明
        </th>
    </tr>
		<tr>
        <td>
            高分辨率视频
        </td>
				<td>
			广电 OTT 用户一般通过智能电视等大屏终端进行播放，首要需求就是细腻真实的视频体验，因此超高清分辨率视频是其最基本的诉求。
        </td>
	</tr>
	<tr>
        <td>
            多清晰度智能切换
        </td>
				<td>
			 广电 OTT 用户基数庞大，各家网络情况千差万别，为适应多种网络环境，视频资源一般需要准备多种分辨率，终端播放时根据网络情况自动选择合适码率的媒体流进行播放。
        </td>
	</tr>
	<tr>
        <td>
            版权保护
        </td>
				<td>
			 广电 OTT 媒体资源内容包罗万象，例如电影外、体育赛事、儿童动画、综艺等不一而足，在大屏消费不断攀升的现在，极易被不法分子盯上，制作盗版并传播，因此需要借助有效的版本保护手段，最大限度降低媒体资源泄露。
        </td>
	</tr>
	<tr>
        <td>
            媒体智能审核
        </td>
				<td>
			广电 OTT 用户群体广泛，媒体内容违规会造成相当恶劣的影响，给平台带来巨大损失，平台一般长视频资源较多，人工审核周期长、效率低且易出错，如果能通过机器智能审核，可先过滤掉大量的合规视频，极大降低人工审核的成本。
        </td>
	</tr>
	<tr>
        <td>
            媒体禁播
        </td>
				<td>
				最新录制的节目，由于审核疏漏等原因，包含不适宜向公众展示的内容，需要尽快禁播。
        </td>
	</tr>
		<tr>
        <td>
            点播转直播
        </td>
				<td>
				广电 OTT 广泛存在伪直播（即通过技术手段使已存在的视频文件达成类似直播的播放效果）的场景。如电视台播放电影电视剧，又如定期更新的综艺节目、人物访谈，提前录制剪辑好，在预告页面提前放置，观众可提前收藏页面、链接，既定播放时间到来时才可播放。
        </td>
	</tr>
	<tr>
        <td>
            高效广电编目
        </td>
				<td>
				广电行业有大量视频，一般以长视频居多，传统人工编目效率低下。
        </td>
	</tr>
</table>




## 解决方案
<table>
    <tr>
        <th>
            核心诉求              
        </th>
				<th>
           云点播推荐功能
        </th>
    </tr>
	<tr>
        <td>
            高分辨率视频
        </td>
				<td>
					<li><a href="https://cloud.tencent.com/document/product/266/78289" title="音视频转码" target="_blank">音视频转码</a></br>云点播支持 2K、4K、8K 等高分辨率转码，也支持 HDR 画质转码，满足 OTT 电视等大屏设备对于超高清、高画质内容的使用需求。</li>
        </td>
	</tr>
	<tr>
        <td>
            多清晰度智能切换
        </td>
				<td>
					<li><a href="https://cloud.tencent.com/document/product/266/78296" title="多码率智能切换" target="_blank">多码率智能切换</a></br>一进多出生成多路码流，满足终端设备在复杂的家庭网络环境下的播放需求。</li>
        </td>
	</tr>
	 <tr>
        <td>
            版权保护
        </td>
				<td>
				<li>
					<a href="https://cloud.tencent.com/document/product/266/78306" title="防盗链" target="_blank">防盗链</a></br>支持 Referer 防盗链和 Key 防盗链两种形式，防范非法盗链行为。
				</li>
				<li>
					<a href="https://cloud.tencent.com/document/product/266/78307" title="加密与 DRM" target="_blank">加密与 DRM</a></br>支持 HLS 私有加密和商业级 DRM，均能有效防范各类破解行为，为媒体版权保驾护航。
				</li>
        </td>
	</tr>
	<tr>
        <td>
            媒体智能审核
        </td>
				<td>
				<li>
					<a href="https://cloud.tencent.com/document/product/266/78304" title="智能审核" target="_blank">智能审核</a></br>云点播智能审核持续对海量的违规数据进行训练建模，识别的准确率和召回率均达到业界领先水准，全面有效保障广电 OTT 平台媒体内容安全。
				</li>
        </td>
	</tr>
	<tr>
        <td>
            媒体禁播
        </td>
				<td>
					<li><a href="https://cloud.tencent.com/document/product/266/78305" title="媒体禁播" target="_blank">媒体禁播</a></br>通过媒体禁播，广电 OTT 平台可以第一时间阻断违规媒体内容进一步传播，降低平台安全风险和品牌伤害。</li>
        </td>
	</tr>
	<tr>
        <td>
            点播转直播
        </td>
				<td>
					<li><a href="https://cloud.tencent.com/document/product/266/78312" title="点播转直播" target="_blank">点播转直播</a></br>基于云点播访问控制的功能，使点播文件达成类直播效果，广电 OTT 可以低成本快速实现点播文件的类直播分发，充分利用高价值录播内容为平台吸引更多流量。</li>
        </td>
	</tr>
	<tr>
        <td>
            高效广电编目
        </td>
				<td>
					<li><a href="https://cloud.tencent.com/document/product/266/78302" title="标签分类" target="_blank">标签分类</a></br>通过云点播标签分类功能可以高效理解海量视频内容信息，改变以往人工编目效率低下的情况，借助识别出来的标签分类信息，可以快速地对视频进行归档和标签检索。</li>
        </td>
	</tr>
</table>
