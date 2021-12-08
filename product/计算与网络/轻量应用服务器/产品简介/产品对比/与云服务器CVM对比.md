对比 [云服务器 CVM](https://cloud.tencent.com/document/product/213/495)，轻量应用服务器 TencentCloud Lighthouse 更聚焦于中小企业、开发者、云计算入门者、学生等用户群体。相比云服务器 CVM 更加简单易用，精简了云服务器 CVM 的高阶概念及功能，提供高带宽流量包并以高性价比的套餐形式整体售卖基础云资源，将热门开源软件融合打包实现一键构建应用，更适合于支撑中小型网站、Web 应用、博客、论坛、小程序/小游戏、电商、云盘/图床、云端开发测试和学习环境等轻量级、低负载且访问量适中的应用场景。

<dx-alert infotype="explain" title="">
- 创建轻量应用服务器时不支持指定底层物理服务器的 CPU 型号，腾讯云将随机分配满足套餐规格的物理 CPU 型号。
- 与同规格的 [标准型云服务器 CVM](https://cloud.tencent.com/document/product/213/11518#S) 相比，轻量应用服务器的 CPU、内存性能与其处于同一水准。
</dx-alert>



轻量应用服务器相比云服务器 CVM 的主要区别和优势请参考下表：
<table style="width:908px;">
<tr>
<th style="width:95px;height:45px;position:relative;font-weight:700;" valign="top" colspan="2"><div style="position:absolute;width:1px;height: 244px;top:0;left:0;background-color: #d9d9d9;transform: rotate(-76deg);transform-origin:top;"></div><div style="position:relative;left:150px">产品</div>优势</th>
<th style="font-weight:700;">轻量应用服务器 TencentCloud Lighthouse</th>
<th style="font-weight:700;">云服务器 CVM</th>
</tr>
<tr>
<th style="font-weight:700;" colspan=2>更聚焦的用户群体</th>
<td>中小企业、开发者、云计算入门者</td>
<td>更适用于熟悉云计算，业务场景相对复杂的企业级⽤户  </td>
</tr>
<tr>
<th style="font-weight:700;" colspan=2>更轻量的业务场景</th>
<td>轻量级、低负载且访问量适中的应用场景：
<ul style="margin:-3px 0px">
<li>企业官网、个人展示网站、博客、论坛、电商等各类网站和 Web 应用服务</li>
<li>个人云盘、图床服务</li>
<li>微信小程序、小游戏后端服务</li>
<li>云端开发测试环境、学习环境</li>
<li>跨境电商店铺管理、独立站搭建</li>
</ul>
</td>
<td>全业务场景</td>
</tr>
<tr>
<th style="font-weight:700;" rowspan=2>更优惠的计费模式</th>
<th style="font-weight:700;">售卖方式</th>
<td>高性价比套餐式售卖（计算/网络/存储资源组合）</td>
<td>灵活选配计算/存储/网络资源，独立叠加计费</td>
</tr>
<tr>
<th style="font-weight:700;">网络计费</th>
<td>高带宽流量包模式</td>
<td>固定带宽/流量用量</td>
</tr>
<tr>
<th style="font-weight:700;" rowspan=5>更简化的功能设计</th>
<th style="font-weight:700;">云能力入口</th>
<td>一站式整合，独立且简化的控制台</td>
<td>面向全业务场景的控制台</td>
</tr>
<tr>
<th style="font-weight:700;">应用部署</th>
<td>开箱即用，预置应用系统所需的软件栈最优组合，自动完成应用软件、依赖的运行环境安装和初始化配置</td>
<td>通常为创建实例后自行部署应用，或使用镜像市场</td>
</tr>
<tr>
<th style="font-weight:700;">镜像</th>
<td>精选优质的轻量应用服务器专有应用镜像</td>
<td>公共镜像、自定义镜像、共享镜像、镜像市场 </td>
</tr>
<tr>
<th style="font-weight:700;">网络</th>
<td>自动创建网络资源，无需手动管理 VPC 网络、子网及公网 IP 等</td>
<td>用户自行创建、配置、管理网络 </td>
</tr>
</table>



<dx-alert infotype="explain" title="">
- 轻量应用服务器相比云服务器 CVM 在功能层面的主要限制包括：
  - 实例创建完成后，不支持更换公网 IP 地址。
  - 实例支持以套餐为单位进行配置（计算、存储和网络）的整体升级，但不支持降级套餐。详情请参见 [升级实例套餐](https://cloud.tencent.com/document/product/1207/51730)。
  - 目前不支持生成备案授权码。
 轻量应用服务器具体使用限制说明，请参见 [使用限制](https://cloud.tencent.com/document/product/1207/44376)。
- 轻量应用服务器在内网连通性上也存在一定限制，详情请参见 [地域与网络连通性](https://cloud.tencent.com/document/product/1207/50103)。
- 轻量应用服务器的 [云硬盘](https://cloud.tencent.com/document/product/1207/63920) 和云服务器 CVM 的 [云硬盘](https://cloud.tencent.com/document/product/213/4953) 相互独立。轻量应用服务器的云硬盘仅支持挂载至轻量应用服务器实例，无法挂载至云服务器 CVM。
</dx-alert>




如果您需要使用更丰富的实例类型，如内存优化型、高 IO 型、大数据型、裸金属、GPU/FPGA 异构计算型等，支持高并发网站、视频编解码、大型游戏、复杂分布式集群应用等业务场景，请使用云服务器 CVM 产品，具体可以参考 [云服务器-实例规格](https://cloud.tencent.com/document/product/213/11518)。
