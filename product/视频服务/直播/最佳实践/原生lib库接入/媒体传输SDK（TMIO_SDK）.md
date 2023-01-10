## 简单介绍
TMIO SDK（Tencent Media IO SDK）是针对当前日益丰富的流媒体传输协议，对主流协议进行整合优化和扩展，为用户可以开发出稳定可用的媒体应用提供服务方便，摆脱繁重的多种协议的开发调试工作。
TMIO SDK 当前已对 SRT、QUIC 等主流媒体协议 进行了优化扩展，同时新增自研传输控制协议 ETC（全称：Elastic Transmission Control），后续将会持续增加其他主流协议的优化扩展。

### 能力优势
- **多平台支持**：包括 Android、iOS、Linux、Mac 和 windows。
- **灵活的选择接入方式**：
   - 零代码入侵的代理模式， 请参见 [接入简介](#choose)。
   - 依托简单的 API 设计，可实现快速接入替换原有传输协议，请参见 [接入简介](#internal)。
- **API 接口设计简单，兼容性灵活性强**：
   - 提供简单易用的接口设计。
   - 可根据业务需求场景选择合适的模式和策略。
   - 可扩展其他协议的定制优化。
- **整合多种传输协议扩展优化**：
   - SRT、QUIC 等新一代主流传输协议和自研传输控制协议 ETC 支持
   - 可适用于多种业务场景的不同需求选择
   - 基于 UDP 的低延时、安全可靠的传输设计
   - 多链路加速优势，保证传输更稳定、流畅

### 效果展示（以TMIO SRT 为例）
- **TMIO 支持 SRT 协议，可用于弱网、远距离传输场景中，提高上行稳定性和下行流畅度。**
  如下测试场景中，RTMP推流在10%丢包率时已播放卡顿，SRT推流在10%甚至30%丢包率时仍能保持稳定和低延迟。
  <video width="500px" height="auto" src="https://qcloudimg.tencent-cloud.cn/raw/8d165df8dec666b05a013a3def596e0b.mp4" controls  muted></video>
- **TMIO-SRT 支持多链路平滑迁移。网络不佳时，可流畅切换至备用链路，保持推流的稳定。**
  <video width="500px" height="auto" src="https://qcloudimg.tencent-cloud.cn/raw/12b687f741d3dac58700fbf55b565550.mp4" controls  muted></video>



### 功能介绍
- **基于 SRT 的流媒体传输功能**
  - **抗随机丢包能力强**。
  - **基于 ARQ 及超时策略的重传机制**
  - **基于 UDT 的低延时、安全可靠的传输设计**。
  - **多链路传输功能，在原基础上新增扩展链路聚合功能**：
  多链路传输功能可配置多条链路来实现数据的传输，特别是在当前4G/5G网络普遍的情况下，移动终端设备既可以使用 Wi-Fi，又可以使用数据网络来进行数据的传输，这样即使单一网络突然中断，只要有一条链路可用就可以保证链路的稳定性。
    <table>
    <thead><tr><th>功能模式</th><th>说明</th></tr></thead>
    <tbody><tr>
    <td>广播模式</td>
    <td>可配置多个链接实现冗余发送，保证数据的完整性和连接可靠性。</td>
    </tr><tr>
    <td>主备模式</td>
    <td>基于链路稳定性和可靠性做参考，同一时间只有一路链接的活跃，实时选择更优质的链路来实现数据传输。既保证了链路的稳定性和可靠性，又能够减少冗余数据带来的带宽消耗。</td>
    </tr><tr>
    <td>聚合模式</td>
    <td>对于高码率、带宽要求的场景，当单一链路带宽无法满足其需求时，聚合模式可将数据通过多链路来拆分发送，同时在接收侧重组，以达到增大带宽的目的。</td>
    </tr>
    </tbody></table>
- **基于 QUIC 的流媒体传输功能**
  - **自适应拥塞控制算法**
  - **支持网络连接迁移，平滑无感知**
  - **支持下一代HTTP3基础传输协议**
  - **带宽受限、抖动环境下，发送冗余数据更低，更加节约带宽成本，优势明显**
- **自研传输控制协议ETC**
  - **纯自研，轻量级，跨平台**
  - **支持IoT设备，适合端到端通信**
  - **快启动、低时延且高带宽利用率**
  - **迅速、准确地感知链路状态变化，并及时调整到最佳传输策略**
  - **与主流传输协议并存时，能更公平、更稳定地利用带宽**


## 接入方法
以 RTMP over SRT 协议为例：

[](id:choose)
### 选择代理模式
#### Tmio Proxy 模式接入方式
![](https://qcloudimg.tencent-cloud.cn/raw/137c7bccf3021ea66f3275ef3a058acc.jpeg)

#### 操作步骤
1. **创建 Tmio Proxy**：
```c++
std::unique_ptr<tmio::TmioProxy> proxy_ = tmio::TmioProxy::createUnique();
```
2. **设置监听**：
```c++
void setListener(TmioProxyListener *listener);
```
TmioProxyListener 监听接口如下：
<dx-tabs>
::: Tmio 配置回调
用户可在此回调内对 Tmio 做参数配置，**简单配置可使用 `tmio-preset.h` 提供的辅助方法**。
```c++
/*
void onTmioConfig(Tmio *tmio);
*/
void onTmioConfig(tmio::Tmio *tmio) override {
		auto protocol = tmio->getProtocol();
		if (protocol == tmio::Protocol::SRT) {
				tmio::SrtPreset::rtmp(tmio);
		} else if (protocol == tmio::Protocol::RIST) {
				tmio->setIntOption(tmio::base_options::RECV_SEND_FLAGS,
													 tmio::base_options::FLAG_SEND);
		}
}
```
:::
::: TmioProxy 启动回调
```c++
/*
void onStart(const char *local_addr, uint16_t local_port); 
*/
void onStart(const char *addr, uint16_t port) override {
		LOGFI("ip %s, port %" PRIu16, addr, port);
}
```
收到此回调代表连接远程服务器成功，并且 TCP 本地端口绑定成功，可以启动推流。
:::
::: 错误信息回调
```c++
/*
void onError(ErrorType type, const std::error_code &err);
*/
void onError(tmio::TmioProxyListener::ErrorType type,
						const std::error_code &err) override {
		LOGFE("error type %s, %s, %d", tmio::TmioProxyListener::errorType(type),
					err.message().c_str(), err.value());
}
```
用户可通过 ErrorType 来区分是本地 IO 错误还是远程 IO 错误。本地 IO 通常是 RTMP 推流主动触发的，如结束推流，一般可忽略，而远程 IO 错误一般不可忽略。
:::
</dx-tabs>
3. **启动代理**：
```c++
std::error_code start(const std::string &local_url, const std::string &remote_url, void * config=nullptr)
```
	- 接口参数
<table>
<thead>
<tr>
<th>参数</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>local_url</td>
<td>只支持 TCP Scheme，格式为 <code>tcp://${ip}:${port}</code>。port 可以为0，为0时会绑定到随机端口，然后通过 onStart() 回调把绑定成功后的端口号返回给应用。使用0端口可以避免端口被占用、无权限等导致的绑定失败问题</td>
</tr>
<tr>
<td>remote_url</td>
<td>远程服务器 URL</td>
</tr>
<tr>
<td>config</td>
<td>配置参数，此参数在 SRT bonding 功能和 QUIC H3 协议启用时使用，具体定义请依据 <code>tmio.h</code> 下 TmioFeatureConfig 结构体定义</td>
</tr>
</tbody></table>
	- 单链路（代码示例）
```C++
 proxy_->start(local_url, remote_url, NULL);
```
	- bonding 多链路（代码示例）
```C++
tmio::TmioFeatureConfig option;
option_.protocol = tmio::Protocol::SRT;
option_.trans_mode = static_cast<int>(tmio::SrtTransMode::SRT_TRANS_BACKUP);
/*-----------------------------------------------------------*/
{
	//根据当前需要建立的链路数可添加多个链路
	option_.addAvailableNet(net_name, local_addr, remote_url, 0, weight, -1);
}
/*-----------------------------------------------------------*/

 proxy_->start(local_url, remote_url, &option_);
```
1. **停止**：
```c++
/*
void stop();
*/
proxy_.stop();
```

[](id:internal)
### 内部集成
#### Tmio SDK 内部集成接入方式
![](https://qcloudimg.tencent-cloud.cn/raw/ffad74f4bebbc9cea6eb780a937dc0b9.jpeg)

#### 接入流程
1. **创建 Tmio&配置参数**（代码示例）：
```C++
tmio_ = tmio::TmioFactory::createUnique(tmio::Protocol::SRT);
tmio::SrtPreset::mpegTsLossless(tmio_.get());
tmio_->setIntOption(tmio::srt_options::CONNECT_TIMEOUT, 4000);
tmio_->setBoolOption(tmio::base_options::THREAD_SAFE_CHECK, true);
```
	- **创建 Tmio**：通过 `TmioFactory` 来创建。
	- **参数配置**：根据不同参数选择不同的接口来实现配置：
	<ul>
	<li><strong>参数名</strong>：请参见 <code>tmio-option.h</code>。</li>
	<li><strong>简单配置</strong>：请参见 <code>tmio-preset.h</code>。
	</ul>
```C++
//根据不同参数属性选择合适的配置
bool setBoolOption(const std::string &optname, bool value);
bool setIntOption(const std::string &optname, int64_t value);
bool setDoubleOption(const std::string &optname, double value);
bool setStrOption(const std::string &optname, const std::string &value);
...
```
2. **开始连接**（代码示例）：
```C++
/**
 * open the stream specified by url
 *
 * @param config protocol dependent
 */
virtual std::error_code open(const std::string &url,
							  void *config = nullptr) = 0;
```
	- 单链路（config 可为 NULL）
```C++
//默认单链路
auto err = tmio->open(TMIO_SRT_URL);
if (err) {
	LOGE("open failed, %d, %s", err.value(), err.message().c_str());
}
```
	- 多链路 bonding（当前仅支持 SRT 协议）
		- config 设置时 SRT bonding 配置参数可参见 `tmio.h` 文件结构中 TmioFeatureConfig 定义。
```C++
tmio::TmioFeatureConfig option_;
option_.protocol = tmio::Protocol::SRT;
option_.trans_mode = static_cast<int>(tmio::SrtTransMode::SRT_TRANS_BACKUP);
option_.addAvailableNet(net_name, local_addr, remote_url, 0, weight, -1);
```
```C++
//bonding 多链路
auto err = tmio_->open(TMIO_SRT_URL, &option_);
if (err) {
	LOGE("open failed, %d, %s", err.value(), err.message().c_str());
}
```
		-  多链路 bonding open 接口还可以用来对 group 组添加新的链路用于传输。
3. **发送数据**：
```C++
int ret = tmio_->send(buf.data(), datalen, err);
if (ret < 0) {
		LOGE("send failed, %d, %s", err.value(), err.message().c_str());
		break;
}
```
4. **接收数据**：
	- 如果是需要交互的协议（如 RTMP）， 此时需要启用接收接口来读取数据完成协议交互，这里提供两个接口调用：
```c++
/**
* receive data
*
* @param err return error details
* @return number of bytes which were received, or < 0 to indicate error
*/
virtual int recv(uint8_t *buf, int len, std::error_code &err) = 0;

using RecvCallback = std::function<bool(const uint8_t *buf, int len, const std::error_code &err)>;
/**
* receive data in event loop
*
* recvLoop() block current thread, receive data in a loop and pass the data to recvCallback
* @param recvCallback return true to continue the receive loop, false for break
*/
virtual void recvLoop(const RecvCallback &recvCallback) = 0;
```
	- 上层应用循环读取
```C++
while (true) {
	ret = tmio_->recv(buf.data(), buf.size(), err);
	if (ret < 0) {
		LOGE("recv error: %d, %s", err.value(), err.message().c_str());
		break;
	}
	...
}
```
	- 回调读取
```C++
FILE *file = fopen(output_path, "w");
tmio_->recvLoop([file](const uint8_t *buf, int len,
													const std::error_code &err) {
		if (len < 0) {
				fwrite(buf, 1, len, file);
		} else if (len < 0) {
				LOGE("recv error: %d, %s", err.value(), err.message().c_str());
		}
		return true;
});
```
5. **关闭 Tmio**：
```C++
tmio_->close();
```
6. **其他**：
获取当前链路状态（应用可根据此状态信息调整推流策略）。
```C++
tmio::PerfStats stats_;
tmio_->control(tmio::ControlCmd::GET_STATS, &stats_);
```

## 最新 API 接口及 Demo 详细说明
接入 TMIO SDK，可参考最新 API 接口和 Demo 说明， 详情请参见 [TMIO 接入详情](https://github.com/tencentyun/tmio)。


## 常见问题解答
### 是不是所有的设备都可以使用 SRT bonding 多链路功能？
多链路功能的前提是设备有多个可用的网络接口，同时针对 Android 设备其系统需要在6.0（api level >=23）以上才可使用。

### Android 手机在已连接 Wi-Fi 的情况下，如何启用4G/5G数据网络？
Android 手机在已连接 Wi-Fi 的情况下，是无法直接使用4G/5G网络来实现数据传输的，此时如果想启用数据网络则需要申请数据网络权限，代码如下：
```java
ConnectivityManager connectivityManager = (ConnectivityManager) context.getSystemService(Context.CONNECTIVITY_SERVICE);
NetworkRequest request = new NetworkRequest.Builder().addTransportType(NetworkCapabilities.TRANSPORT_CELLULAR)
										   .addCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET)
										   .build();

ConnectivityManager.NetworkCallback networkCallback = new ConnectivityManager.NetworkCallback(){
	@Override
	public void onAvailable(@NonNull Network network) {
                Log.d(TAG, "移动数据网络通道已开启.");
		super.onAvailable(network);
	}
}
```
