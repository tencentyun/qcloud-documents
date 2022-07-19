<style>.markdown-text-box table td, .markdown-text-box table th {text-align: center;}</style>

实时音视频（TRTC）SDK 移动端（Android & iOS）即将发布 10.1 版本，新版本 SDK 采用“腾讯视频”同款播放内核打造，视频播放能力获得全面优化升级，详见 [升级特性](#up)。

同时从该版本开始将增加对**视频播放**功能模块的授权校验，**如果您的 App 已经拥有直播 License （原直播推流 License）或短视频 License 授权，当您升级至 10.1 版本后仍可继续正常使用**，不受到此次变更影响。您可以登录 [腾讯云视立方控制台](https://console.cloud.tencent.com/vcube) 查看您当前的 License 信息。

如果您此前未获得过直播 License （原直播推流 License）或短视频 License 授权，**且需使用新版本 SDK 中的 [CDN 直播播放](https://cloud.tencent.com/document/product/647/16826) 或 [点播播放功能](https://cloud.tencent.com/document/product/647/16823#.E5.9B.9E.E6.94.BE.E5.BD.95.E5.88.B6.E6.96.87.E4.BB.B6)，则需购买指定 License 获得授权**，详情参见 [授权说明](#warrant)。
**若您无需使用视频播放功能或未升级至10.1及更高版本的 SDK，将不受到此次变更的影响。**

>! 10.1版本 SDK 预计在2022年05月底发布，您可在 [License 购买页](https://buy.cloud.tencent.com/vcube) 内购买包含视频播放功能的 License，并参考 [License 操作指引](https://cloud.tencent.com/document/product/1449/56981) 进行 License 的新增与续期操作。本次升级涉及的 TRTC 移动端（iOS & Android）SDK 包含精简版（TRTC）SDK 和全功能版 （Professional）SDK，您可持续关注官网通知以了解最新动态。

[](id:warrant)
## 授权说明
10.1 版本后，直播 License（原直播推流 License）、短视频 License 和视频播放 License **均可**授权解锁新版本 SDK 的**视频播放**功能模块，您只需购买其中的**任意一种** License，即可正常使用新版 SDK 中的直播和点播播放功能，相关 License 的购买、计费信息及操作指引如下：

- [购买直播 License](https://buy.cloud.tencent.com/vcube?type=live&pkg-type=10tb) 授权解锁**直播推流 + 视频播放**功能模块，相关计费详情请参见 [直播 SDK 价格总览](https://cloud.tencent.com/document/product/454/8008#.E7.9B.B4.E6.92.AD-license.EF.BC.88.E5.8E.9F.E7.A7.BB.E5.8A.A8.E7.9B.B4.E6.92.AD.E5.9F.BA.E7.A1.80.E7.89.88-license.EF.BC.89)，操作指引参见 [直播License新增与续期](https://cloud.tencent.com/document/product/454/34750)。
- [购买短视频 License](https://buy.cloud.tencent.com/vcube?type=video&pkg-type=10tb) 授权解锁**短视频制作 + 视频播放**功能模块，相关计费详情请参见 [短视频 SDK 价格总览](https://cloud.tencent.com/document/product/584/9368)，操作指引参见 [短视频 License 新增与续期](https://cloud.tencent.com/document/product/584/54333)。
- [购买视频播放 License](https://buy.cloud.tencent.com/vcube) 授权解锁**视频播放**功能模块，相关计费详情请参见 [视频播放 License 计费说明](#play_price)，操作指引参见 [视频播放 License 新增与续期](https://cloud.tencent.com/document/product/881/74588)。

<table>
<thead>
<tr>
<th rowspan="2" width="20%">License 类型</th>
<th colspan="3">解锁的功能模块授权</th>
<th rowspan="2">License 获取方式</th>
</tr><tr>
<th>直播推流</th>
<th>短视频制作</th>
<th>视频播放</th>
</tr>
</thead>
<tbody>
<tr>
<td>直播 License</td>
<td>&#10003;</td>
<td>-</td>
<td>&#10003;</td>
<td style="text-align: left;"><ul style="margin:0">
<li><a href="https://buy.cloud.tencent.com/vcube?type=live&amp;pkg-type=10tb" target="_blank">购买</a> 10TB、50TB、200TB、1PB 云直播流量资源包赠送直播 License 一年使用授权</li>
    <li><a href="https://buy.cloud.tencent.com/vcube?type=live&amp;pkg-type=10tb" target="_blank">购买</a> 独立直播 License 一年使用授权</li></ul></td>
</tr>
<tr>
<td>短视频 License</td>
<td>-</td>
<td>&#10003;</td>
<td>&#10003;</td>
<td style="text-align: left;"><ul style="margin:0">
<li><a href="https://buy.cloud.tencent.com/vcube?type=video&amp;pkg-type=10tb" target="_blank">购买</a> 10TB、50TB、200TB、1PB 云点播流量资源包赠送短视频精简版/基础版 License 一年使用授权</li>
    <li><a href="https://buy.cloud.tencent.com/vcube?type=video&amp;pkg-type=10tb" target="_blank">购买</a> 独立短视频 License 一年使用授权</li></ul></td>
</tr>
<tr>
<td>视频播放 License</td>
<td>-</td>
<td>-</td>
<td>&#10003;</td>
<td style="text-align: left;"><ul style="margin:0">
<li><a href="https://buy.cloud.tencent.com/vcube" target="_blank">购买</a> 100GB、500GB、1TB、5TB 直播/点播流量资源包赠送视频播放 License 一年使用授权</li>
    <li><a href="https://buy.cloud.tencent.com/vcube" target="_blank">购买</a> 独立视频播放 License 一年使用授权</li></ul></td>
</tr>
</tbody></table>



[](id:up)
## 升级特性

升级后的实时音视频（TRTC）SDK 中的卓越视频播放器的视频播放内核由腾讯内部完全自研，且经过长期优化和海量服务验证，对比系统播放器，性能提升 30% ~ 50%。 同时针对控制带宽成本、辅助运营增长、降低接入门槛等方面为企业用户进行了专门的优化升级，新增终端极速高清、版权保护、全链路数据洞察和场景化低代码等多种方案，打造业界独家、行业领先的企业级视频播放解决方案，全面满足企业级需求。

<table>
<thead>
<tr>
<th width=16% style="text-align: left;">特性</th>
<th style="text-align: left;">说明</th>
</tr>
</thead>
<tbody><tr>
<td style="text-align: left;">“腾讯视频”同款</td>
<td style="text-align: left;">首次将“腾讯视频”播放能力以 SDK 的形式开放给广大开发者，在具备“臻彩视听”、精准 Seek、清晰度切换、小窗播放、离线缓存等多项“腾讯视频”同款播放功能的同时，具备同等水平的视频播放稳定性和机型适配性。</td>
</tr><tr>
<td style="text-align: left;">新增格式支持</td>
<td style="text-align: left;">新增支持 QUIC、AV1、H.266 等格式，相比 H.264/H.265节省带宽 20%～55%，满足多样化的业务场景同时降低客户成本。</td>
</tr><tr>
<td style="text-align: left;">版权保护升级</td>
<td style="text-align: left;">在支持私有协议加密、本地加密、防盗链等方案前提下，新增支持商业 DRM 加密方案，具备完整视频安全方案矩阵，全方位保护视频版权。</td>
</tr><tr>
<td style="text-align: left;">画质提升解决方案</td>
<td style="text-align: left;">新增支持“腾讯视频-臻彩视听” HDR 10 视频播放能力；并提供终端极速高清方案，能够在几乎不降低视频主观画质的情况下，为企业节省传输带宽成本。</td>
</tr><tr>
<td style="text-align: left;">全链路数据洞察</td>
<td style="text-align: left;">提供播放数据统计、质量监控及可视化分析服务。针对点播、直播等各种不同场景，提供了细致到单个文件的近百项不同维度数据指标及数据对比、多维筛选、定向追查等能力，方便开发者进行运营决策，驱动业务快速增长。</td>
</tr><tr>
<td style="text-align: left;">场景化低代码</td>
<td style="text-align: left;">提供类似腾讯视频号（沉浸式短视频）、腾讯新闻（Feed 流视频）的场景化方案，可以快速搭建相关场景 App；并新增视频封面、动态水印、列表轮播等多种功能组件，适配多样业务场景，降低开发成本。</td>
</tr>
</tbody></table>



[](id:play_price)
## 视频播放 License 计费说明
2022年05月底起，新上线可用于解锁 10.1 版本实时音视频（TRTC）SDK 视频播放能力的视频播放 License，该 License 提供两种购买解锁方式：购买指定资源包赠送 License 或购买独立 License，计费说明见下表：
<table>
<thead>
<tr>
<th width=15%>视频播放 License 类型</th>
<th>有效期</th>
<th>对应云服务资源包</th>
<th>解锁的功能模块</th>
<th width=10%>价格<br>（元/年）</th>
<th>获取方式</th>
</tr>
</thead>
<tbody><tr>
<td>测试版</td>
<td>28天</td>
<td>-</td>
<td rowspan=10>视频播放</td>
<td>0</td>
<td><a href="https://console.cloud.tencent.com/vcube">免费申请</a></td>
</tr>
<tr>
<td rowspan=9>正式版</td>
<td rowspan=9>1年</td>
<td>购买独立视频播放 License 一年使用授权<br>（无资源包）</td>
<td>12</td>
<td><a href="https://buy.cloud.tencent.com/vcube?type=player&pkg-type=lic">直接购买</a></td>
</tr>
<tr>
<td>购买 100GB 直播流量资源包<br>赠送视频播放 License 一年使用授权</td>
<td>26</td>
<td rowspan=8><a href="https://buy.cloud.tencent.com/vcube?type=live&pkg-type=100GB">购买资源包免费赠送</a></td>
</tr>
<tr>
<td>购买 500GB 直播流量资源包<br>赠送视频播放 License 一年使用授权</td>
<td>128</td>
</tr>
<tr>
<td>购买 1TB 直播流量资源包<br>赠送视频播放 License 一年使用授权</td>
<td>248</td>
</tr>
<tr>
<td>购买 5TB 直播流量资源包<br>赠送视频播放 License 一年使用授权</td>
<td>1,200</td>
</tr>
<tr>
<td>购买 100GB 点播流量资源包<br>赠送视频播放 License 一年使用授权</td>
<td>19</td>
</tr>
<tr>
<td>购买 500GB 点播流量资源包<br>赠送视频播放 License 一年使用授权</td>
<td>88</td>
</tr>
<tr>
<td>购买 1TB 点播流量资源包<br>赠送视频播放 License 一年使用授权</td>
<td>175</td>
</tr>
<tr>
<td>购买 5TB 点播流量资源包<br>赠送视频播放 License 一年使用授权</td>
<td>869</td>
</tr>
</tbody></table>
