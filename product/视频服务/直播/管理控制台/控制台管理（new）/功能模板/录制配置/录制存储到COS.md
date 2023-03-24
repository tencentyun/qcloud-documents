
云直播提供将直播画面进行录制并将文件存储到云点播或者对象存储中的功能，本文将为您介绍如何将录制文件存储至 COS 中。

## 注意事项

- 录制的视频存储至对象存储控制台，建议提前开通对象存储服务，并可提前选购存储容量包，避免存储业务欠费停用，详细请参见 [对象存储快速入门](https://cloud.tencent.com/document/product/436/38484)。
- 开启录制功能后请确保对象存储服务处于正常使用状态。对象存储服务未开通或账号欠费导致对象存储服务停服等情况将影响直播无法进行录制，期间不会产生录制文件和录制费用。
- 直播过程中预计在录制结束5分钟左右可获取对应文件。例如，某直播从12:00开始录制，12:30结束录制，则12:35左右可获取12:00 - 12:30的对应片段，以此类推。
- 录制模板创建成功后，可与推流域名进行关联，相关文档可参见 录制配置，关联成功后约5分钟 - 10分钟生效。
- 混流录制不支持中国内地（大陆）和国际/港澳台的直播混流，会导致录制文件错误，影响正常观看回放。
- 录制后的存储功能依赖对象存储的API权限，请确保使用前已完成对云直播服务的授权，避免录制存储失败。因授权取消导致存储失败时，视频无法找回。相关授权可查看COS授权给直播实现录制存储。
- 当发起录制任务时，没有选择相应的录制模板，录制文件默认存储至云点播。
- 根据国家《网络表演经营活动管理办法》及《网络交易监督管理办法》的最新规定，经营单位需记录网络直播视频内容并进行存储备份，保存时长根据直播类型建议存储60日至3年，详情请参见 [直播录制国家相关规定](https://cloud.tencent.com/document/product/267/80341)。


## 前提条件

- 已开通腾讯云直播服务，并添加 [推流域名](https://cloud.tencent.com/document/product/267/20381)。
- 已开通 [对象存储服务](https://cloud.tencent.com/document/product/436/38484)。


## 创建录制模板

1. 登录云直播控制台，进入 **功能配置** > [**直播录制**](https://console.cloud.tencent.com/live/config/record)。
2. 在直播录制中选择录制存储至 COS。
3. 单击**创建模板** 设置模板信息，进行如下配置：
   ![](https://qcloudimg.tencent-cloud.cn/raw/6330b07b1247185083ed191ff7231f7c.png)
<table>
   <thead><tr><th width="20%" colspan=2>配置项</th><th>配置描述</th></tr></thead>
   <tbody><tr>
   <tr>
   <td colspan=2>模板名称</td>
   <td>直播录制模板名称，可自定义（仅支持中文、英文、数字、_、-）。</td>
   </tr><tr>
   <td colspan=2>模板描述</td>
   <td>直播录制模板介绍描述，可自定义（仅支持中文、英文、数字、_、-）。</td>
   </tr><tr>   
   <td rowspan=3 width="10%">录制内容</td>
   <td width="30%">录制原始流</td> 
   <td>录制视频针对直播原始码率录制，默认录制原始流。选择该配置会在直播流转码（包括转码、加水印及混流）前进行录制，录制的视频不带转码、水印及混流效果。对 WebRTC 推流录制原始流可能出现音频播放不兼容的情况，建议选择“带水印录制”或“指定转码流录制”。</ul></td>
   </tr><tr>
   <td>带水印录制</td>
   <td>选择该配置会在直播流加水印模板配置的水印后进行录制，若未配置水印模板则录制原始流。</td>
   </tr><tr>
   <td>指定转码流录制</td>
   <td>单击指定转码流录制，可选择已配置的转码模板，或点击模板名称前往修改转码模板配置。选择该配置会在推流后自动根据转码模板id发起转码进行录制，若转码模板被误删，则效果等同于录制内容"按带水印录制"
。</td>
   </tr><tr>
   <td colspan=2>录制格式</td>
   <td>录制视频输出格式有  HLS、FLV、MP4 和 AAC 四种，其中 AAC 为纯音频录制。</td>
   </tr>
</tbody></table>
> ! 
> - WebRTC 推流录制原始流会丢失音频，建议选择其它录制内容。
> - 录制转码流功能暂不支持时移场景使用，若录制模板已关联时移配置，会按照原始流进行录制。
> - 若指定转码流录制中选择纯音频转码模板时，录制格式中只可选择音频格式。
> - 录制转码流需要先发起转码任务，会额外产生转码费用，若使用相同转码模板进行播放，不会重复计费。
3. 选择录制内容，勾选需要录制格式后，弹出相关格式的设置界面，可选择一个或多个录制格式同时进行设置。请进行如下设置：
<img src="https://qcloudimg.tencent-cloud.cn/raw/ef25f0451d1625570046b88c7a7eba55.png" width=900>
<table>
 <thead><tr><th width="27%" colspan=2>配置项</th><th>配置描述</th></tr></thead>
 <tbody><tr>
<tr>
<td colspan=2>单个录制文件时长（分钟）</td>
<td><ul style="margin-bottom:0px">
			<li>录制 HLS 格式最长单个文件时长无限制，如果超出续录等待时长则新建文件继续录制。</li>
			<li>录制 FLV 格式单个文件时长限制为1分钟 - 720分钟。</li>
			<li>录制 MP4 或 AAC 格式单个文件时长限制为1分钟 - 120分钟。</li>
</ul></td>
</tr><tr>
<td colspan=2>续录等待时长（秒）</td>
<td>仅  HLS 格式支持文件推流中断续录，续录等待时长可设置为1s - 1800s。</td>
</tr><tr>
<td colspan=2>保存时长（天）</td>
<td>可选择 <b>永久存储</b> 或 <b>指定时间</b>。单个录制文件保存最大时长均为1500天，文件保存时长0为永久。</td>
</tr><tr>
<td colspan=2>存储路径</td>
<td><ul style="margin-bottom:0px">
				<li>可在 Bucket 中选择您已在 <b>对象存储</b> 中创建并完成授权的 COS bucket。</li>
				<li>Region 为上述 Bucket 所属地域信息，不可修改。</li>
</ul></td>
</tr><tr>      
<td colspan=2>容灾存储路径</td>      
<td>可开启容灾存储路径，当网络抖动导致录制文件不能存储到主存储路径时，系统会自动将文件存储至容灾路径下，以防止文件丢失。当主存储路径恢复后，容灾路径下的录制文件会自动同步到主存储路径下。主备region不能相同。</td>
</tr><tr>      
<td colspan=2>存储文件夹</td>      
<td><ul style="margin-bottom:0px"><li>录制存储文件夹默认按照 <code>{RecordSource}/{Domain}/{AppName}/{StreamID}/{RecordId}/{StartYear}-{StartMonth}-{StartDay}-{StartHour}-{StartMinute}-{StartSecond}</code> 进行存储。其中变量包含：</li>
<li>{RecordSource}：录制内容，原始流则为origin，转码流则为转码模板id</li>  
<li>{StartYear}：开始时间-年</li> 
<li>{StartMonth}：开始时间-月</li>
<li>{StartDay}：开始时间-日</li>
<li>{StartMinute}：开始时间-分钟</li>
<li>{StartSecond}：开始时间-秒</li>
<li>{Domain}：推流域名</li>
<li>{AppName}：推流路径</li>
<li>{StreamID}：流ID</li>
<li>{RecordId}：录制id，区别录制规则or录制任务，录制任务则展示任务id（即CreateRecord创建返回ID）</li>
<li>「/」为层级关系，「-」为普通字符</li>
</ul></td>
</tr>
</tbody></table>
4. 单击 **保存** 即可。
> ? 由于录制文件是边录边传，导致无法在上传前获取到结束时间，无法在文件名中添加结束时间。

[](id:conect)
## 关联域名

1. 登录云直播控制台，进入 **功能配置** > [**直播录制**](https://console.cloud.tencent.com/live/config/record)>录制存储至COS。
   - **直接关联域名：**单击左上方的 **绑定域名**。
     ![](https://qcloudimg.tencent-cloud.cn/raw/7c0525f583d65b27adf82ff89f0a3ef8.png)
   - **新录制模板创建成功后关联域名：**录制模板创建成功后，单击提醒框中的 **去绑定域名**。
     ![](https://main.qcloudimg.com/raw/4de2cb134a48920fc5527217704e7f76.png)
2. 在域名绑定窗口中，选择您需绑定的**录制模板**及**推流域名**，单击 **确定** 即可绑定成功。
   ![](https://qcloudimg.tencent-cloud.cn/raw/ed874330b279d76e3fe80de2310b12b5.png)
> ? 支持通过单击 **添加** 为当前模板绑定多个推流域名。

[](id:unite)
## 解除绑定
1. 登录云直播控制台，进入 **功能配置** > [**直播录制**](https://console.cloud.tencent.com/live/config/record)>录制存储至COS。
2. 选择已关联域名的录制模板，选择需要解绑的域名，单击右侧的 **解绑**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/440c2bc8eaa91b9e0648cce5ce57d4e4.png)
3. 确认是否解绑当前关联域名，单击 **确定** 即可解绑。
   ![](https://main.qcloudimg.com/raw/690daf43f9b1d5f57b6033720c19860a.png)

> ? 
> - 录制模板解除绑定后，不影响正在直播中的流。
> - 若需解绑生效，解绑后请断流并重新推流直播，新的直播将不会生成录制文件。


## 修改模板

1. 进入 **功能配置** > [**直播录制**](https://console.cloud.tencent.com/live/config/record)>录制存储至COS。
2. 选择您已创建成功的录制模板，并单击右侧的 **编辑**，即可进入修改模板信息。
3. 单击 **保存** 即可。
![](https://qcloudimg.tencent-cloud.cn/raw/0059445110bafcfbc8c4a985eea53930.png)


## 删除模板
1. 登录云直播控制台，进入 **功能配置** > [**直播录制**](https://console.cloud.tencent.com/live/config/record)>录制存储至COS。
2. 选择您已创建成功的录制模板，单击右上方 **删除**。
3. 确认是否删除当前录制模板，单击 **确定** 即可成功删除。
![](https://qcloudimg.tencent-cloud.cn/raw/45006e452f7418e894e534d23b0ebc78.png)

> ! 
> - 若模板已被关联，需要先 [解除绑定](#unite)，才可以进行删除操作。
> - 控制台的录制模板管理为域名维度，暂时无法取消关联接口创建的规则，如果是通过录制管理接口关联指定流的，则需要通过调用 [删除录制规则](https://cloud.tencent.com/document/product/267/32613) 解除关联。 


## 相关操作
**域名维度绑定**和**解绑**录制模板的具体操作及相关说明，请参见 录制配置。
