## 主要特性

### 视频通信

支持最高720P高清视频，云端流控策略优化，保证高质量视频通信。

### 音频通信

支持最高同时收取6路语音，支持窄带、宽带语音链接，保证高质量音频通信。

### 跨平台互通

支持Android、iOS、PC、Web主流平台开播、观看及互通；支持一对多，多对多的互动直播，满足视频社交、在线教育、远程医疗等多种应用场景。

### 旁路直播(即旁观者模式)

支持旁路直播，结合腾讯云直播服务可实现HLS、RTMP的直播下发。

### PC桌面分享

支持全屏及选定区域的桌面分享，支持清晰（1920×1200）、流畅（960×720）2种分享模式

### SPEAR云端配置

用户可根据业务场景，分平台、分角色配置音频、视频、网络参数，灵活定制属于自己的流控策略，也可方便快速地使用我们提供的实时通讯，互动直播等默认策略。

### 云端录制

支持云端录制，结合腾讯云点播服务及其完善的API可实现存储、转码、分发等功能。


## 基本功能

### 互动直播Winows C++/iOS/Android SDK

<table style="display:table;width:100%;">
	<tbody>
		<tr>
			<th rowspan="2">模块</th>
			<th colspan="2" rowspan="2" style="width: 123px;">子功能</th>
			<th rowspan="2" style="width: 200px;">详细描述/注意事项</th>
			<th colspan="3" style="width: 180px;">是否支持</th>
		</tr>
		<tr>
			<th style="width: 25px;">PC</th>
			<th style="width: 25px;">iOS</th>
			<th style="width: 150px;">Android</th>
		</tr>
		<tr>
			<td rowspan="13" style="text-align:center">房间</td>
			<td rowspan="8" style="text-align: center; width: 56px;">房间操作</td>
			<td colspan="2" style="text-align: center; width: 300px;">说明：业务侧房间与音视频SDK侧房间：业务侧房间是业务侧自己维护的具有唯一性的房间，如常见的有业务侧自己维护的房间号、讨论组号、群号、游戏座号等。音视频SDK侧房间是音视频SDK侧这边自己维护的房间，也一样具有唯一性，每次进入房间时动态分配。在进入音视频SDK侧房间时，需要带入业务侧的房间号，以让两侧的房间建立映射关系。另外，需要注意的是，对于业务侧来说，音视频SDK侧的房间号是透明的，不需要关心它。</td>
			<td colspan="3" style="text-align: center; width: 263px;">　</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">创建房间</td>
			<td style="text-align: center; width: 382px;">第一个成员要进入房间时，音视频后台会自动创建房间，后续成员加入时，就不会再创建。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">进入房间</td>
			<td style="text-align: center; width: 382px;">进入房间。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">退出房间</td>
			<td style="text-align: center; width: 382px;">退出房间。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">销毁房间</td>
			<td style="text-align: center; width: 382px;">最后一个成员退出房间后，音视频后台会自动销毁房间。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">最大房间成员人数</td>
			<td style="text-align: center; width: 382px;">5万人。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">获取正在发语音/视频的成员列表</td>
			<td style="text-align: center; width: 382px;">1.2版本：支持。<br />
			1.3及以后版本：支持。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">获取所有房间成员列表</td>
			<td style="text-align: center; width: 382px;">1.2版本：不支持。<br />
			1.3及以后版本：房间成员人数少于50个时，支持；成员人数超过50个时，只能获取前50个成员的列表。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td rowspan="5" style="text-align: center; width: 56px;">事件通知</td>
			<td style="text-align: center; width: 65px;">自己进入房间事件通知</td>
			<td style="text-align: center; width: 382px;">支持。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">别人进入房间事件通知</td>
			<td style="text-align: center; width: 382px;">1.2版本：不支持。<br />
			1.3及以后版本：房间成员人数少于50个时，支持；成员人数超过50个时，只做前50个成员的进入房间事件通知。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">自己退出房间事件通知</td>
			<td style="text-align: center; width: 382px;">支持。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">别人退出房间事件通知</td>
			<td style="text-align: center; width: 382px;">1.2版本：不支持。<br />
			1.3及以后版本：房间成员人数少于50个时，支持；成员人数超过50个时，只做前50个成员的退出房间事件通知。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">成员是否发语音/视频状态变更事件通知</td>
			<td style="text-align: center; width: 382px;">支持。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td rowspan="8" style="text-align:center">房间成员</td>
			<td colspan="2" style="text-align: center; width: 123px;">发语音</td>
			<td style="text-align: center; width: 382px;">支持。最多支持同时6个成员发语音。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">发视频</td>
			<td style="text-align: center; width: 382px;">支持。最多支持同时4个成员发摄像头/外部捕获设备的视频。如果是Windows平台，还支持1个成员发屏幕视频，这个发送屏幕视频的成员可以是前面的4个成员之一，也可以不是；所以，对于Windows平台，最多支持同时发4个摄像头/外部捕获设备的视频+1个屏幕视频。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">请求画面</td>
			<td style="text-align: center; width: 382px;">请求某个人/某些人的摄像头/外部捕获设备/屏幕视频画面。<br />
			注意事项：<br />
			. 最多支持同时请求4个摄像头/外部捕获设备的视频画面+1个屏幕视频画面；如果自己上了视频，则这时候可以上的其他成员的视频画面个数也就相应减少，自己可以请求的视频画面个数也一样减少。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">取消画面</td>
			<td style="text-align: center; width: 382px;">取消已请求的某个成员或所有成员的画面。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">接听语音</td>
			<td style="text-align: center; width: 382px;">如果想听某个人的语音(前提是他有发送语音)，则可以设置接听他的语音。默认是接听所有人的声音。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">不接听语音</td>
			<td style="text-align: center; width: 382px;">如果不想听某个人或某些人的语音，则可以选择不听。<br />
			注意事项：<br />
			. 自己设置不听某个人的语音，只会影响自己，那个人的语音还是可以照样发，别人还是可以照样接听他的语音。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 56px;">　</td>
			<td style="text-align: center; width: 65px;">动态修改自身权限</td>
			<td style="text-align: center; width: 382px;">通话中动态修改自己的音视频上下行权限，用于第三方实现权限控制和管理</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">获取成员状态</td>
			<td style="text-align: center; width: 382px;">获取成员状态。现在的状态有：是否发语音、是否发视频等。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td rowspan="7" style="text-align:center">语音质量控制</td>
			<td colspan="2" style="text-align: center; width: 123px;">音频流控参数</td>
			<td style="text-align: center; width: 382px;">参数包括编解码器类型、采样率、通道数、包长和码率。<br />
			注意事项：<br />
			. 通过Web流控配置系统来配置这些参数。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" rowspan="6" style="text-align: center; width: 123px;">音频数据输入和输出</td>
			<td style="text-align: center; width: 382px;">获取本地麦克风采集的音频数据。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 382px;">发送方最终发送出去的音频数据。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 382px;">获取本地扬声器播放音频数据。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 382px;">接收方收到的音频数据。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 382px;">输入额外的音频数据，与本地播放音频数据混音后给扬声器播放出来。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 382px;">输入额外的音频数据，与本地发送音频数据混音后发送出去。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align:center">视频质量控制</td>
			<td colspan="2" style="text-align: center; width: 123px;">视频流控参数</td>
			<td style="text-align: center; width: 382px;">参数包括编解码器类型、图像宽高、帧率、码率、最大QP、最小QP、GOP、清晰化开关、清晰化度和FEC开关。<br />
			注意事项：<br />
			. 通过Web流控配置系统来配置这些参数，参数支持详见WEB流控配置系统页面。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td rowspan="11" style="text-align:center">基本音频设备</td>
			<td rowspan="6" style="text-align: center; width: 56px;">麦克风</td>
			<td style="text-align: center; width: 65px;">打开</td>
			<td style="text-align: center; width: 382px;">打开设备。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">关闭</td>
			<td style="text-align: center; width: 382px;">关闭设备。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">获取设备信息</td>
			<td style="text-align: center; width: 382px;">获取设备的信息，包括ID、名称、类型、是否打开等。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">获取/设置数字音量</td>
			<td style="text-align: center; width: 382px;">数字音量就是指应用程序自身的音频数据数字信号值。通俗地讲，数字音量就是应用的音量，区别于系统的音量。调节数字音量，就是对数字信号值进行缩放。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">获取动态音量</td>
			<td style="text-align: center; width: 382px;">动态音量就是指每一帧音频数据中所有时刻的音频信号值中的最大值(峰值)。业务侧可以获取这个动态音量去画音量动态波形图。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">热插拔检测</td>
			<td style="text-align: center; width: 382px;">热插拔检测。在通话过程中，设备热插拔检测并处理。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td rowspan="6" style="text-align: center; width: 56px;">扬声器</td>
			<td style="text-align: center; width: 65px;">打开</td>
			<td style="text-align: center; width: 382px;">打开设备。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">关闭</td>
			<td style="text-align: center; width: 382px;">关闭设备。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">获取设备信息</td>
			<td style="text-align: center; width: 382px;">获取设备的信息，包括ID、名称、类型、是否打开等。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">获取/设置音量</td>
			<td style="text-align: center; width: 382px;">获取/设置音量。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">获取动态音量</td>
			<td style="text-align: center; width: 382px;">获取动态音量。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align:center">　</td>
			<td style="text-align: center; width: 65px;">热插拔检测</td>
			<td style="text-align: center; width: 382px;">热插拔检测。在通话过程中，设备热插拔检测并处理。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td rowspan="3" style="text-align:center">高级音频设备</td>
			<td rowspan="3" style="text-align: center; width: 56px;">远端房间成员语音设备(虚拟设备)</td>
			<td style="text-align: center; width: 65px;">打开</td>
			<td style="text-align: center; width: 382px;">打开设备。<br />
			注意事项：<br />
			. 后台最多支持发送6路语音，如果超过6路语音，则会根据某种策略选择其中6路，并转发给接收成员。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">关闭</td>
			<td style="text-align: center; width: 382px;">关闭设备。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">获取设备信息</td>
			<td style="text-align: center; width: 382px;">获取设备的信息，包括ID、名称、类型、是否打开等。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td rowspan="6" style="text-align:center">基本视频设备</td>
			<td rowspan="6" style="text-align: center; width: 56px;">摄像头</td>
			<td style="text-align: center; width: 65px;">打开</td>
			<td style="text-align: center; width: 382px;">打开设备。如果同类型的设备存在多个，是不允许同时打开的；打开其中一个设备时，如果之前已经有其他同类型的设备打开了，SDK会默认关闭那些设备。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">关闭</td>
			<td style="text-align: center; width: 382px;">关闭设备。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">获取设备信息</td>
			<td style="text-align: center; width: 382px;">获取设备的信息，包括ID、名称、类型、是否打开等。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">渲染</td>
			<td style="text-align: center; width: 382px;">渲染视频画面。<br />
			注意事项：<br />
			. 目前，SDK内部提供的渲染模块的功能比较简单，对于渲染画面大小、位置等不能任意设置。如果这样不能满足业务需求的话，建议业务侧自己实现渲染。</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">获取系统摄像头对象</td>
			<td style="text-align: center; width: 382px;">业务方可以通过该对象实现变焦功能。</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">图像预处理</td>
			<td style="text-align: center; width: 382px;">可以对摄像头视频图像进行预处理。<br />
			注意事项：<br />
			. 自己和房间成员是可以看到预处理后的效果。自己如果发视频，是发这个预处理后的视频，房间成员看到的也是预处理后的视频。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td rowspan="21" style="text-align:center">高级视频设备</td>
			<td rowspan="5" style="text-align: center; width: 56px;">外部视频捕获设备(虚拟设备)</td>
			<td colspan="2" style="text-align: center; width: 448px;">说明：外部视频捕获设备是一种虚拟设备，用于让用户输入自己的视频，并由SDK发送给房间其他成员。这边的视频源可以任意，比如来自用户自己的摄像头的、来自某个视频文件的。目前只支持一个外部视频捕获设备。</td>
			<td colspan="3" style="text-align: center; width: 263px;">　</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">打开</td>
			<td style="text-align: center; width: 382px;">打开设备。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">关闭</td>
			<td style="text-align: center; width: 382px;">关闭设备。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">获取设备信息</td>
			<td style="text-align: center; width: 382px;">获取设备的信息，包括ID、名称、类型、是否打开等。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">输入视频流</td>
			<td style="text-align: center; width: 382px;">根据业务需求，输入自己的视频流，并由SDK发送给房间其他成员。这边的视频源可以任意，比如来自用户自己的摄像头的、来自某个视频文件的。<br />
			注意事项：<br />
			. 输入的视频流必须遵循SDK接口所约定的要求。具体要求是：视频必须转成一帧帧图像传进来，图像的颜色格式目前只支持I420，图像大小最大支持640&times;480，并且图像的宽高必须是4的倍数，视频帧率最好在10-15帧左右。另外，SDK不负责对所输入的视频流做图像预处理、渲染等。<br />
			. 外部图像捕获设备跟摄像头设备是互斥的，也就是同一个时刻只能有一个起作用。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td rowspan="6" style="text-align: center; width: 56px;">远端房间成员视频设备(虚拟设备)</td>
			<td colspan="2" style="text-align: center; width: 448px;">说明：远程房间成员视频设备，是一种虚拟设备，用于操作远程成员的视频流。目前只支持一个远程房间成员视频设备，所有远程房间成员共用。</td>
			<td colspan="3" style="text-align: center; width: 263px;">　</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">打开</td>
			<td style="text-align: center; width: 382px;">打开设备。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">关闭</td>
			<td style="text-align: center; width: 382px;">关闭设备。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">获取设备信息</td>
			<td style="text-align: center; width: 382px;">获取设备的信息，包括ID、名称、类型、是否打开等。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">渲染</td>
			<td style="text-align: center; width: 382px;">渲染远程成员的视频画面。<br />
			注意事项：<br />
			. 目前，SDK内部提供的渲染模块的功能比较简单，对于渲染画面大小、位置等不能任意设置。如果这样不能满足业务需求的话，建议业务侧自己实现渲。IOS和Android SDK提供的渲染模块当前已支持多路渲染（Windows平台需要业务方拿到视频流后自行进行渲染）。</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">获取视频流</td>
			<td style="text-align: center; width: 382px;">获取房间成员的视频流。可以获取所有有发送视频的成员的视频流。如果业务侧根据自己业务需要，要实现自己的渲染，可以通过该功能获取视频流后去渲染。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td rowspan="5" style="text-align: center; width: 56px;">本地屏幕视频设备(虚拟设备)</td>
			<td style="text-align: center; width: 65px;">打开</td>
			<td style="text-align: center; width: 382px;">打开设备。<br />
			注意事项：<br />
			. 同一时刻，同一个房间内，只允许一个成员打开本地屏幕视频设备和发送屏幕视频。如果其他人要打开本地屏幕视频设备，必须等到别人关闭了本地屏幕视频设备后才行。<br />
			. 屏幕视频画面编码分辨率最大支持1920*1200。<br />
			. 更多屏幕视频设备使用的注意事项请参考API文档。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">关闭</td>
			<td style="text-align: center; width: 382px;">关闭设备。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">获取设备信息</td>
			<td style="text-align: center; width: 382px;">获取设备的信息，包括ID、名称、类型、是否打开等。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">渲染</td>
			<td style="text-align: center; width: 382px;">渲染视频画面。<br />
			注意事项：<br />
			. 目前，SDK内部提供的渲染模块的功能比较简单，对于渲染画面大小、位置等不能任意设置。如果这样不能满足业务需求的话，建议业务侧自己实现渲染。</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">图像预处理</td>
			<td style="text-align: center; width: 382px;">可以对本地屏幕采集图像进行预处理。<br />
			注意事项：<br />
			. 自己和房间成员是可以看到预处理后的效果。自己如果发视频，是发这个预处理后的视频，房间成员看到的也是预处理后的视频。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td rowspan="5" style="text-align: center; width: 56px;">远端屏幕视频设备(虚拟设备)</td>
			<td style="text-align: center; width: 65px;">打开</td>
			<td style="text-align: center; width: 382px;">打开设备。<br />
			注意事项：<br />
			. 由于屏幕视频画面分辨率往往比较高，如1920*1200，对于终端，特别是一些硬件配置比较差的终端，接收、解码和渲染这么大的画面，是对用户体验有所影响的；所以在实际使用过程中，最好对此做好评估。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">关闭</td>
			<td style="text-align: center; width: 382px;">关闭设备。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">获取设备信息</td>
			<td style="text-align: center; width: 382px;">获取设备的信息，包括ID、名称、类型、是否打开等。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">渲染</td>
			<td style="text-align: center; width: 382px;">渲染视频画面。<br />
			注意事项：<br />
			. 目前，SDK内部提供的渲染模块的功能比较简单，对于渲染画面大小、位置等不能任意设置。如果这样不能满足业务需求的话，建议业务侧自己实现渲染。</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">获取视频流</td>
			<td style="text-align: center; width: 382px;">获取房间成员的视频流。可以获取所有有发送视频的成员的视频流。如果业务侧根据自己业务需要，要实现自己的渲染，可以通过该功能获取视频流后去渲染。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td rowspan="8" style="text-align:center">设备管理</td>
			<td colspan="2" style="text-align: center; width: 123px;">获取输入和输出设备个数</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">获取输入和输出设备列表</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">获取已经打开的设备个数</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">获取已经打开的设备列表</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">根据设备id获取某个设备</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">获取某种类型的设备列表</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">&nbsp;&nbsp;&nbsp; 通话前麦克风、扬声器和摄像<br />
			头等设备的可用性检测</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">获取语音/视频设备列表</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&times;</td>
			<td style="text-align: center; width: 206px;">&times;</td>
		</tr>
		<tr>
			<td rowspan="8" style="text-align:center">其他</td>
			<td colspan="2" style="text-align: center; width: 123px;">录制</td>
			<td style="text-align: center; width: 382px;">支持云端录制，结合腾讯云点播服务及其完善的API可实现存储、转码、分发等功能。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">旁路直播</td>
			<td style="text-align: center; width: 382px;">支持旁路直播，结合腾讯云直播服务可实现HLS、RTMP的直播下发。</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">自有账号体系</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">第三方开放帐号体系</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td rowspan="3" style="text-align: center; width: 56px;">日志</td>
			<td style="text-align: center; width: 65px;">日志打印</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">设置日志存放目录</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 65px;">日志上报</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 123px;">crash上报</td>
			<td style="text-align: center; width: 382px;">　</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 25px;">&radic;</td>
			<td style="text-align: center; width: 206px;">&radic;</td>
		</tr>
	</tbody>
</table>


### 互动直播Web SDK

<table style="display:table;width:100%;">
	<tbody>
		<tr>
			<th rowspan="2" style="width: 18px;">模块</th>
			<th colspan="2" rowspan="2" style="width: 116px;">子功能</th>
			<th rowspan="2" style="width: 307px;">详细描述/注意事项</th>
			<th colspan="3" style="width: 146px;">是否支持</th>
		</tr>
		<tr>
			<th style="width: 42px;">PC</th>
			<th style="width: 49px;">iOS</th>
			<th style="width: 58px;">Android</th>
		</tr>
		<tr>
			<td rowspan="13" style="text-align: center; width: 18px;">房间</td>
			<td rowspan="8" style="text-align: center; width: 49px;">房间操作</td>
			<td colspan="2" style="text-align: center; width: 376px;">说明：业务侧房间与音视频SDK侧房间：业务侧房间是业务侧自己维护的具有唯一性的房间，如常见的有业务侧自己维护的房间号、讨论组号、群号、游戏座号等。音视频SDK侧房间是音视频SDK侧这边自己维护的房间，也一样具有唯一性，每次进入房间时动态分配。在进入音视频SDK侧房间时，需要带入业务侧的房间号，以让两侧的房间建立映射关系。另外，需要注意的是，对于业务侧来说，音视频SDK侧的房间号是透明的，不需要关心它。</td>
			<td colspan="3" style="text-align: center; width: 146px;">　</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">创建房间</td>
			<td style="text-align: center; width: 307px;">第一个成员要进入房间时，音视频后台会自动创建房间，后续成员加入时，就不会再创建。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">进入房间</td>
			<td style="text-align: center; width: 307px;">进入房间。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">退出房间</td>
			<td style="text-align: center; width: 307px;">退出房间。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">销毁房间</td>
			<td style="text-align: center; width: 307px;">最后一个成员退出房间后，音视频后台会自动销毁房间。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">最大房间成员人数</td>
			<td style="text-align: center; width: 307px;">5万人。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">获取正在发语音/视频的成员列表</td>
			<td style="text-align: center; width: 307px;">1.2版本：支持。<br />
			1.3及以后版本：支持。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">获取所有房间成员列表</td>
			<td style="text-align: center; width: 307px;">1.2版本：不支持。<br />
			1.3及以后版本：房间成员人数少于50个时，支持；成员人数超过50个时，只能获取前50个成员的列表。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td rowspan="5" style="text-align: center; width: 49px;">事件通知</td>
			<td style="text-align: center; width: 67px;">自己进入房间事件通知</td>
			<td style="text-align: center; width: 307px;">支持。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">别人进入房间事件通知</td>
			<td style="text-align: center; width: 307px;">1.2版本：不支持。<br />
			1.3及以后版本：房间成员人数少于50个时，支持；成员人数超过50个时，只做前50个成员的进入房间事件通知。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">自己退出房间事件通知</td>
			<td style="text-align: center; width: 307px;">支持。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">别人退出房间事件通知</td>
			<td style="text-align: center; width: 307px;">1.2版本：不支持。<br />
			1.3及以后版本：房间成员人数少于50个时，支持；成员人数超过50个时，只做前50个成员的退出房间事件通知。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">成员是否发语音/视频状态变更事件通知</td>
			<td style="text-align: center; width: 307px;">支持。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td rowspan="8" style="text-align: center; width: 18px;">房间成员</td>
			<td colspan="2" style="text-align: center; width: 116px;">发语音</td>
			<td style="text-align: center; width: 307px;">支持。最多支持同时6个成员发语音。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">发视频</td>
			<td style="text-align: center; width: 307px;">支持。最多支持同时4个成员发摄像头/外部捕获设备的视频。如果是Windows平台，还支持1个成员发屏幕视频，这个发送屏幕视频的成员可以是前面的4个成员之一，也可以不是；所以，对于Windows平台，最多支持同时发4个摄像头/外部捕获设备的视频+1个屏幕视频。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">请求画面</td>
			<td style="text-align: center; width: 307px;">请求某个人/某些人的摄像头/外部捕获设备/屏幕视频画面。<br />
			注意事项：<br />
			. 最多支持同时请求4个摄像头/外部捕获设备的视频画面+1个屏幕视频画面；如果自己上了视频，则这时候可以上的其他成员的视频画面个数也就相应减少，自己可以请求的视频画面个数也一样减少。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">取消画面</td>
			<td style="text-align: center; width: 307px;">取消已请求的某个成员或所有成员的画面。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">接听语音</td>
			<td style="text-align: center; width: 307px;">如果想听某个人的语音(前提是他有发送语音)，则可以设置接听他的语音。默认是接听所有人的声音。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">不接听语音</td>
			<td style="text-align: center; width: 307px;">如果不想听某个人或某些人的语音，则可以选择不听。<br />
			注意事项：<br />
			. 自己设置不听某个人的语音，只会影响自己，那个人的语音还是可以照样发，别人还是可以照样接听他的语音。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 49px;">　</td>
			<td style="text-align: center; width: 67px;">动态修改自身权限</td>
			<td style="text-align: center; width: 307px;">通话中动态修改自己的音视频上下行权限，用于第三方实现权限控制和管理</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">获取成员状态</td>
			<td style="text-align: center; width: 307px;">获取成员状态。现在的状态有：是否发语音、是否发视频等。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td rowspan="7" style="text-align: center; width: 18px;">语音质量控制</td>
			<td colspan="2" style="text-align: center; width: 116px;">音频流控参数</td>
			<td style="text-align: center; width: 307px;">参数包括编解码器类型、采样率、通道数、包长和码率。<br />
			注意事项：<br />
			. 通过Web流控配置系统来配置这些参数。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" rowspan="6" style="text-align: center; width: 116px;">音频数据输入和输出</td>
			<td style="text-align: center; width: 307px;">获取本地麦克风采集的音频数据。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 307px;">发送方最终发送出去的音频数据。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 307px;">获取本地扬声器播放音频数据。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 307px;">接收方收到的音频数据。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 307px;">输入额外的音频数据，与本地播放音频数据混音后给扬声器播放出来。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 307px;">输入额外的音频数据，与本地发送音频数据混音后发送出去。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 18px;">视频质量控制</td>
			<td colspan="2" style="text-align: center; width: 116px;">视频流控参数</td>
			<td style="text-align: center; width: 307px;">参数包括编解码器类型、图像宽高、帧率、码率、最大QP、最小QP、GOP、清晰化开关、清晰化度和FEC开关。<br />
			注意事项：<br />
			. 通过Web流控配置系统来配置这些参数，参数支持详见WEB流控配置系统页面。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td rowspan="11" style="text-align: center; width: 18px;">基本音频设备</td>
			<td rowspan="6" style="text-align: center; width: 49px;">麦克风</td>
			<td style="text-align: center; width: 67px;">打开</td>
			<td style="text-align: center; width: 307px;">打开设备。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">关闭</td>
			<td style="text-align: center; width: 307px;">关闭设备。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">获取设备信息</td>
			<td style="text-align: center; width: 307px;">获取设备的信息，包括ID、名称、类型、是否打开等。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">获取/设置数字音量</td>
			<td style="text-align: center; width: 307px;">数字音量就是指应用程序自身的音频数据数字信号值。通俗地讲，数字音量就是应用的音量，区别于系统的音量。调节数字音量，就是对数字信号值进行缩放。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">获取动态音量</td>
			<td style="text-align: center; width: 307px;">动态音量就是指每一帧音频数据中所有时刻的音频信号值中的最大值(峰值)。业务侧可以获取这个动态音量去画音量动态波形图。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">热插拔检测</td>
			<td style="text-align: center; width: 307px;">热插拔检测。在通话过程中，设备热插拔检测并处理。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td rowspan="6" style="text-align: center; width: 49px;">扬声器</td>
			<td style="text-align: center; width: 67px;">打开</td>
			<td style="text-align: center; width: 307px;">打开设备。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">关闭</td>
			<td style="text-align: center; width: 307px;">关闭设备。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">获取设备信息</td>
			<td style="text-align: center; width: 307px;">获取设备的信息，包括ID、名称、类型、是否打开等。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">获取/设置音量</td>
			<td style="text-align: center; width: 307px;">获取/设置音量。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">获取动态音量</td>
			<td style="text-align: center; width: 307px;">获取动态音量。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 18px;">　</td>
			<td style="text-align: center; width: 67px;">热插拔检测</td>
			<td style="text-align: center; width: 307px;">热插拔检测。在通话过程中，设备热插拔检测并处理。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td rowspan="3" style="text-align: center; width: 18px;">高级音频设备</td>
			<td rowspan="3" style="text-align: center; width: 49px;">远端房间成员语音设备(虚拟设备)</td>
			<td style="text-align: center; width: 67px;">打开</td>
			<td style="text-align: center; width: 307px;">打开设备。<br />
			注意事项：<br />
			. 后台最多支持发送6路语音，如果超过6路语音，则会根据某种策略选择其中6路，并转发给接收成员。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">关闭</td>
			<td style="text-align: center; width: 307px;">关闭设备。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">获取设备信息</td>
			<td style="text-align: center; width: 307px;">获取设备的信息，包括ID、名称、类型、是否打开等。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td rowspan="6" style="text-align: center; width: 18px;">基本视频设备</td>
			<td rowspan="6" style="text-align: center; width: 49px;">摄像头</td>
			<td style="text-align: center; width: 67px;">打开</td>
			<td style="text-align: center; width: 307px;">打开设备。如果同类型的设备存在多个，是不允许同时打开的；打开其中一个设备时，如果之前已经有其他同类型的设备打开了，SDK会默认关闭那些设备。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">关闭</td>
			<td style="text-align: center; width: 307px;">关闭设备。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">获取设备信息</td>
			<td style="text-align: center; width: 307px;">获取设备的信息，包括ID、名称、类型、是否打开等。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">渲染</td>
			<td style="text-align: center; width: 307px;">渲染视频画面。<br />
			注意事项：<br />
			. 目前，SDK内部提供的渲染模块的功能比较简单，对于渲染画面大小、位置等不能任意设置。如果这样不能满足业务需求的话，建议业务侧自己实现渲染。</td>
			<td style="text-align: center; width: 42px;">&times;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">获取系统摄像头对象</td>
			<td style="text-align: center; width: 307px;">业务方可以通过该对象实现变焦功能。</td>
			<td style="text-align: center; width: 42px;">&times;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">图像预处理</td>
			<td style="text-align: center; width: 307px;">可以对摄像头视频图像进行预处理。<br />
			注意事项：<br />
			. 自己和房间成员是可以看到预处理后的效果。自己如果发视频，是发这个预处理后的视频，房间成员看到的也是预处理后的视频。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td rowspan="21" style="text-align: center; width: 18px;">高级视频设备</td>
			<td rowspan="5" style="text-align: center; width: 49px;">外部视频捕获设备(虚拟设备)</td>
			<td colspan="2" style="text-align: center; width: 376px;">说明：外部视频捕获设备是一种虚拟设备，用于让用户输入自己的视频，并由SDK发送给房间其他成员。这边的视频源可以任意，比如来自用户自己的摄像头的、来自某个视频文件的。目前只支持一个外部视频捕获设备。</td>
			<td colspan="3" style="text-align: center; width: 146px;">　</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">打开</td>
			<td style="text-align: center; width: 307px;">打开设备。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">关闭</td>
			<td style="text-align: center; width: 307px;">关闭设备。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">获取设备信息</td>
			<td style="text-align: center; width: 307px;">获取设备的信息，包括ID、名称、类型、是否打开等。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">输入视频流</td>
			<td style="text-align: center; width: 307px;">根据业务需求，输入自己的视频流，并由SDK发送给房间其他成员。这边的视频源可以任意，比如来自用户自己的摄像头的、来自某个视频文件的。<br />
			注意事项：<br />
			. 输入的视频流必须遵循SDK接口所约定的要求。具体要求是：视频必须转成一帧帧图像传进来，图像的颜色格式目前只支持I420，图像大小最大支持640&times;480，并且图像的宽高必须是4的倍数，视频帧率最好在10-15帧左右。另外，SDK不负责对所输入的视频流做图像预处理、渲染等。<br />
			. 外部图像捕获设备跟摄像头设备是互斥的，也就是同一个时刻只能有一个起作用。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td rowspan="6" style="text-align: center; width: 49px;">远端房间成员视频设备(虚拟设备)</td>
			<td colspan="2" style="text-align: center; width: 376px;">说明：远程房间成员视频设备，是一种虚拟设备，用于操作远程成员的视频流。目前只支持一个远程房间成员视频设备，所有远程房间成员共用。</td>
			<td colspan="3" style="text-align: center; width: 146px;">　</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">打开</td>
			<td style="text-align: center; width: 307px;">打开设备。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">关闭</td>
			<td style="text-align: center; width: 307px;">关闭设备。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">获取设备信息</td>
			<td style="text-align: center; width: 307px;">获取设备的信息，包括ID、名称、类型、是否打开等。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">渲染</td>
			<td style="text-align: center; width: 307px;">渲染远程成员的视频画面。<br />
			注意事项：<br />
			. 目前，SDK内部提供的渲染模块的功能比较简单，对于渲染画面大小、位置等不能任意设置。如果这样不能满足业务需求的话，建议业务侧自己实现渲。IOS和Android SDK提供的渲染模块当前已支持多路渲染（Windows平台需要业务方拿到视频流后自行进行渲染）。</td>
			<td style="text-align: center; width: 42px;">&times;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">获取视频流</td>
			<td style="text-align: center; width: 307px;">获取房间成员的视频流。可以获取所有有发送视频的成员的视频流。如果业务侧根据自己业务需要，要实现自己的渲染，可以通过该功能获取视频流后去渲染。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td rowspan="5" style="text-align: center; width: 49px;">本地屏幕视频设备(虚拟设备)</td>
			<td style="text-align: center; width: 67px;">打开</td>
			<td style="text-align: center; width: 307px;">打开设备。<br />
			注意事项：<br />
			. 同一时刻，同一个房间内，只允许一个成员打开本地屏幕视频设备和发送屏幕视频。如果其他人要打开本地屏幕视频设备，必须等到别人关闭了本地屏幕视频设备后才行。<br />
			. 屏幕视频画面编码分辨率最大支持1920*1200。<br />
			. 更多屏幕视频设备使用的注意事项请参考API文档。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">关闭</td>
			<td style="text-align: center; width: 307px;">关闭设备。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">获取设备信息</td>
			<td style="text-align: center; width: 307px;">获取设备的信息，包括ID、名称、类型、是否打开等。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">渲染</td>
			<td style="text-align: center; width: 307px;">渲染视频画面。<br />
			注意事项：<br />
			. 目前，SDK内部提供的渲染模块的功能比较简单，对于渲染画面大小、位置等不能任意设置。如果这样不能满足业务需求的话，建议业务侧自己实现渲染。</td>
			<td style="text-align: center; width: 42px;">&times;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">图像预处理</td>
			<td style="text-align: center; width: 307px;">可以对本地屏幕采集图像进行预处理。<br />
			注意事项：<br />
			. 自己和房间成员是可以看到预处理后的效果。自己如果发视频，是发这个预处理后的视频，房间成员看到的也是预处理后的视频。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td rowspan="5" style="text-align: center; width: 49px;">远端屏幕视频设备(虚拟设备)</td>
			<td style="text-align: center; width: 67px;">打开</td>
			<td style="text-align: center; width: 307px;">打开设备。<br />
			注意事项：<br />
			. 由于屏幕视频画面分辨率往往比较高，如1920*1200，对于终端，特别是一些硬件配置比较差的终端，接收、解码和渲染这么大的画面，是对用户体验有所影响的；所以在实际使用过程中，最好对此做好评估。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">关闭</td>
			<td style="text-align: center; width: 307px;">关闭设备。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">获取设备信息</td>
			<td style="text-align: center; width: 307px;">获取设备的信息，包括ID、名称、类型、是否打开等。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">渲染</td>
			<td style="text-align: center; width: 307px;">渲染视频画面。<br />
			注意事项：<br />
			. 目前，SDK内部提供的渲染模块的功能比较简单，对于渲染画面大小、位置等不能任意设置。如果这样不能满足业务需求的话，建议业务侧自己实现渲染。</td>
			<td style="text-align: center; width: 42px;">&times;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">获取视频流</td>
			<td style="text-align: center; width: 307px;">获取房间成员的视频流。可以获取所有有发送视频的成员的视频流。如果业务侧根据自己业务需要，要实现自己的渲染，可以通过该功能获取视频流后去渲染。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td rowspan="8" style="text-align: center; width: 18px;">设备管理</td>
			<td colspan="2" style="text-align: center; width: 116px;">获取输入和输出设备个数</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">获取输入和输出设备列表</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">获取已经打开的设备个数</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">获取已经打开的设备列表</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">根据设备id获取某个设备</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">获取某种类型的设备列表</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">&nbsp;&nbsp;&nbsp; 通话前麦克风、扬声器和摄像<br />
			头等设备的可用性检测</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">获取语音/视频设备列表</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&times;</td>
			<td style="text-align: center; width: 58px;">&times;</td>
		</tr>
		<tr>
			<td rowspan="8" style="text-align: center; width: 18px;">其他</td>
			<td colspan="2" style="text-align: center; width: 116px;">录制</td>
			<td style="text-align: center; width: 307px;">支持云端录制，结合腾讯云点播服务及其完善的API可实现存储、转码、分发等功能。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">旁路直播</td>
			<td style="text-align: center; width: 307px;">支持旁路直播，结合腾讯云直播服务可实现HLS、RTMP的直播下发。</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">自有账号体系</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">第三方开放帐号体系</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td rowspan="3" style="text-align: center; width: 49px;">日志</td>
			<td style="text-align: center; width: 67px;">日志打印</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">设置日志存放目录</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 67px;">日志上报</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center; width: 116px;">crash上报</td>
			<td style="text-align: center; width: 307px;">　</td>
			<td style="text-align: center; width: 42px;">&radic;</td>
			<td style="text-align: center; width: 49px;">&radic;</td>
			<td style="text-align: center; width: 58px;">&radic;</td>
		</tr>
	</tbody>
</table>


