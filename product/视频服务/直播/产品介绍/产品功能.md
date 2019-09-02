该页面提供直播产品支持功能简明一览表。具体功能描述和使用方法，请查询对应详细文档。

<div class="doc-table-wrap"><table>
   <tbody><tr>
      <th width="85px" align="center">功能模块</th>
      <th width="85px" align="center">功能名称</th>
      <th width="0px" align="center">功能简介</th>
   </tr>
   <tr>
      <td rowspan="3">直播推流</td>
      <td>推流协议</td>
      <td>支持 RTMP 协议进行推流。</td>
   </tr>
   <tr>   
      <td>推流方式</td>
      <td>支持集成腾讯云直播 iOS、Android、Web 等推流 SDK 的 App，以及常见的第三方推流软件，包括  OBS/XSplit/FMLE 等。</td>
   </tr>
   <tr>
      <td>推流设备</td>
      <td>支持常见的第三方 RTMP 推流硬件和编码器或盒子等设备。</td>
   </tr>


   <tr>
      <td rowspan="3">直播播放</td>
      <td>播放协议</td>
      <td>支持 RTMP、FLV 及 HLS 三种播放协议。</td>
      
   </tr>
   <tr>
      <td>播放方式</td>
      <td>支持腾讯云直播 iOS、Android、Web 等播放器 SDK，以及常见的第三方 FLV、RTMP、HLS 播放器。</td>
      
   </tr>
   <tr>
      <td>播放控制</td>
      <td>可播放与输入流规格一致的原始码流，或播放经过实时转码的码流。</td>
   
 
   <tr>
      <td rowspan="1">直播管理</td>
      <td>管理方式</td>
      <td>支持在直播管理控制台进行图形化管理，或调用直播云 API 进行管理。</td>
   
   </tr>
   <tr>
      <td rowspan="6">直播控制台</td>
      <td>概览</td>
      <td>可对直播资源包流量和直播实时带宽、流量等数据进行查看。</td>

   </tr>
   <tr>
      <td>域名管理</td>
      <td>可进行新增、修改、禁用、删除直播推流和播放域名，支持配置域名 CNAME、Https 证书和推流及播放鉴权等。</td>

   </tr>
   <tr>
      <td>直播流管理</td>
      <td>查询在线或历史的直播流信息。</td>

   </tr>
   <tr>
      <td>功能模块</td>
      <td>查询或修改直播录制、转码、截图、鉴黄、水印、回调等配置信息。</td>

   </tr>
   <tr>
      <td>统计分析</td>
      <td>查询直播服务带宽、流量、请求数、并发连接数、截图数量、频道数量、录制路数等用量统计信息。</td>
  
   </tr>
   <tr>
      <td>直播 SDK</td>
      <td>查询移动直播 SDK 质量监控数据，以及移动直播连麦分钟数信息。</td>


   </tr>
   <tr>
      <td rowspan="2">直播安全</td>
      <td>推流鉴权</td>
      <td>支持推流 URL 防盗链，可自定义鉴权 Key 及过期时间。</td>

   </tr>
   <tr>
      <td>播放鉴权</td>
      <td>支持黑白名单防盗链、 Referer 防盗链、播放 URL 防盗链以及播放远程鉴权。</td>
 
   </tr>

   <tr>
      <td rowspan="6">API 管理</td>
      <td>延播管理 API</td>
      <td>延迟播放、恢复延播。</td>
    
   </tr>
   <tr>
      <td>录制管理 API</td>
      <td>创建录制任务、删除录制任务、终止录制任务。</td>
     
   </tr>
   <tr>
      <td>水印管理 API</td>
      <td>添加水印、删除水印、查询水印列表、设置水印状态、更新水印。</td>
     
   </tr>
   <tr>
      <td>直播拉流 API</td>
      <td>添加拉流配置、删除拉流配置、查询拉流配置、更新拉流配置、修改拉流配置状态。</td>
   
   </tr>
   <tr>
      <td>直播流管理 API</td>
      <td>查询在线推流信息、查询直播中的流、查询历史推流信息、查询流状态、断开直播流、禁播直播流、恢复直播流。</td>
   
   </tr>
   <tr>
      <td>鉴权管理 API</td>
      <td>查询播放鉴权、查询推流鉴权、修改播放鉴权、修改推流鉴权。</td>
  
   </tr>

   <tr>
      <td rowspan="6">增值服务</td>
      <td>直播转码</td>
      <td>支持对直播流进行多种规格转码。</td>
  
   </tr>
  
   <tr>
      <td>直播截图</td>
      <td>支持通过 API 对直播过程截图并存储于腾讯云 COS 对象存储服务。</td>
      
   </tr>

   <tr>
      <td>直播审核</td>
      <td>支持对直播流进行鉴黄、暴恐、涉政等智能 AI 审核。</td>
      
   </tr>

   <tr>
      <td>直播录制</td>
      <td>支持通过 API 录制直播过程并存储于腾讯云 VOD 点播平台。</td>
      
   </tr>

   <tr>
      <td>直播时移</td>
      <td>支持用户在直播流进行中回放过去任意时间的直播内容。</td>
      
   </tr>

   <tr>
      <td>直播海外加速</td>
      <td>支持在海外地区使用腾讯云直播服务。</td>
      
   </tr>

   <tr>
      <td rowspan="3">直播 SDK</td>
      <td>直播 SDK</td>
      <td>提供集直播推流、基础美颜、滤镜、直播播放、直播时移回看一体化的直播 SDK。</td>
    
   </tr>
   <tr>
      <td>美颜特效 SDK</td>
      <td>由腾讯云与天天 P 图及优图实验室联合打造的高级视频处理方案，为直播视频拍摄提供了滤镜、美颜美型、贴纸、手势识别等多种实时特效功能，覆盖多种拍摄场景，满足用户多类拍摄需求。</td>

   </tr>
   <tr>
      <td>互动连麦 SDK</td>
      <td>提供多路实时连麦的互动直播解决方案。</td>

   </tr>



</tbody></table></div>

