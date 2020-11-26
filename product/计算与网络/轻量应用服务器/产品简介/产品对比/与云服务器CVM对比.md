轻量应用服务器 Lighthouse 是新一代以中小企业及开发者为中心的云服务器产品，具备轻运维、开箱即用的特点，通常适用于支撑小型网站、Web 应用、博客、论坛、云端开发测试和学习环境等轻量级、低负载且访问量适中的应用场景。

对比 [云服务器 CVM](https://cloud.tencent.com/document/product/213/495)，轻量应用服务器更加简单易用，简化了传统云服务器的高阶概念及功能，一站式融合多种云服务，您可以便捷高效的部署、配置和管理应用，是使用腾讯云的最佳入门途径。
>?轻量应用服务器底层使用的物理硬件资源与云服务器 CVM 保持一致，同等 CPU、内存和云硬盘配置下二者性能在同一水准。
>

轻量应用服务器与云服务器 CVM 的主要区别请参考下表：
<table style="width:908px;">
<tr>
<th style="width:95px;height:45px;position:relative;font-weight:700;" valign="top" colspan="2"><div style="position:absolute;width:1px;height: 175px;top:0;left:0;background-color: #d9d9d9;transform: rotate(-71deg);transform-origin:top;"></div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;产品<br>对比项</th>
<th style="font-weight:700;">轻量应用服务器 Lighthouse</th>
<th style="font-weight:700;">云服务器 CVM</th>
</tr>
<tr>
<th style="font-weight:700;" colspan=2>面向用户</th>
<td>中小企业、开发者</td>
<td>所有用户</td>
</tr>
<tr>
<th style="font-weight:700;" colspan=2>应用场景</th>
<td>
适合轻量级、低负载且访问量适中的应用场景：
<ul style="margin:-3px 0px">
<li>企业官网、个人展示网站、博客、论坛、电商等各类网站和 Web 应用服务</li>
<li>个人云盘、图床服务</li>
<li>微信小程序、小游戏后端服务</li>
<li>云端开发测试环境、学习环境</li>
</ul>
</td>
<td>全业务场景</td>
</tr>
<tr>
<th style="font-weight:700;" rowspan=3>计费</th>
<th style="font-weight:700;">付费模式</th>
<td>包年包月预付费，详情请参见 <a href="https://cloud.tencent.com/document/product/1207/44368">计费概述</a></td>
<td>包含包年包月、按量付费、竞价实例多种付费方式，详情请参见 <a href="https://cloud.tencent.com/document/product/213/2180">计费模式</a> </td>
</tr>
<tr>
<th style="font-weight:700;">售卖方式</th>
<td>高性价比套餐（计算、网络、存储资源组合）形式售卖</td>
<td>各项资源灵活选配，独立叠加计费 </td>
</tr>
<tr>
<th style="font-weight:700;">网络计费</th>
<td>高带宽流量包模式</td>
<td>固定带宽/流量用量</td>
</tr>
<tr>
<th style="font-weight:700;" rowspan=4>主要功能</th>
<th style="font-weight:700;">控制台</th>
<td>一站式整合，独立且简化的控制台 </td>
<td>面向全业务场景的控制台</td>
</tr>
<tr>
<th style="font-weight:700;">应用部署</th>
<td>开箱即用，预置应用系统所需的软件栈最优组合（例如 LAMP），一键实现应用软件、依赖的运行环境安装以及相关初始化配置</td>
<td>通常为创建实例后自行部署应用，或使用镜像市场</td>
</tr>
<tr>
<th style="font-weight:700;">镜像</th>
<td>提供丰富且优质的轻量应用服务器专有应用镜像，以及常用的系统镜像 </td>
<td>公共镜像、自定义镜像、共享镜像、镜像市场 </td>
</tr>
<tr>
<th style="font-weight:700;">网络</th>
<td>自动创建网络资源，无需管理 VPC 网络、子网及 IP 地址等 </td>
<td>用户自行创建、配置、管理网络 </td>
</tr>
</table>

>?
>- 轻量应用服务器相比云服务器 CVM 存在一些功能层面的限制，主要包括：
>  - 实例创建完成后，不支持更换公网 IP 地址。
>  - 目前不支持挂载云硬盘作为实例的数据盘。
>  - 目前不支持变更已完成购买的实例的套餐配置。
>- 轻量应用服务器在内网连通性上也存在一定限制，详情请参见 [地域与网络连通性](https://cloud.tencent.com/document/product/1207/50103)。
>
