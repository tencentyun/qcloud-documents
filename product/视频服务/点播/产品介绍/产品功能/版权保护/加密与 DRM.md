## 简介

媒体的破解，是指媒体本身未经加密保护，或媒体经加密后被攻击者破解得到原始内容，传播给第三方播放的盗版行为。云点播的 HLS 私有加密和商业级 DRM，均能有效防范各类破解行为，为媒体版权保驾护航。

<table ><thead ><tr>
<th style="width:150px" >功能</th><th >说明</th><th >安全级别</th><th >播放端兼容度</th></tr>

</thead><tbody ><tr>
<td>HLS 私有加密</td>
<td>云点播独创的媒体内容加密方案，内容密钥使用腾讯云的私有协议保护。</td>
<td>高：可有效防范多种浏览器插件和灰产工具的破解。</td>
<td>高：支持几乎所有主流设备的播放。</td>
</tr>

<tr>
<td>商业级 DRM</td>
<td>苹果（Fairplay）和谷歌（Widevine）主推的版权保护系统，内容密钥使用 DRM 系统中设计的协议保护。</td>
<td>极高：硬件级的加解密方案，满足海外影视内容提供商的要求。</td>
<td>一般：iOS 兼容度较好，但部分 Android 终端不支持。</td>
</tr>

</tbody>
</table>



## 适用场景

<table ><thead ><tr>
<th style="width:150px">场景</th><th >说明</th></tr>

</thead><tbody ><tr>
<td>在线教育</td>
<td>教培类课程，需要极高的制作成本，对防破解防盗有很高的诉求。<li>如果课程对播放终端兼容性要求高，建议优先使用 HLS 私有加密；</li>
<li>如果对安全性要求极高，且愿意牺牲一部分终端播放，可以考虑使用商业级 DRM。</li>
</td>
</tr>

<tr>
<td>版权影视剧</td>
<td>影视剧来源于专业版权方的提供，通常需要做版权保护。<li>对于国内制作的影视剧，建议优先使用 HLS 私有加密；</li>
<li>如果海外版权方（如好莱坞）要求商业级 DRM，则考虑使用商业级 DRM。</li>
</td>
</tr>

</tbody>
</table>

 

## 使用方式

* 关于 HLS 私有加密，使用方式参考 [链接](https://cloud.tencent.com/document/product/266/73073)。
* 关于商业级 DRM，使用方式参考 [链接](https://cloud.tencent.com/document/product/266/76203)。
