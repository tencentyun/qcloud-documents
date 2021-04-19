
文本为您介绍 P2P 通道分别通过 so 库调用方法和 aar 库调用方法进行传输数据的操作步骤。

## so 库调用方法

### 步骤1：P2P 通道初始化

 -  函数声明：
```
int startServiceWithXp2pInfo(const char* xp2p_info)
```
 - 代码示例：
```
const char* xp2p_info = getXP2PInfo(...); // 从自建后台获取xp2p info
   //设置回调函数
  startServiceWithXp2pInfo(xp2p_info);
```

### 步骤2：P2P 通道传输音视频流

#### 1. 接收裸数据
  - 函数声明：
```
void *startAvRecvService(const char *params); //启动接收数据服务, 使用该方法首先需调用  setUserCallbackToXp2p()注册回调
void _av_data_recv(uint8_t *data, size_t len);  //裸数据回调接口(具体以自己设置的为准)
```
  - 代码示例：
```
setUserCallbackToXp2p(_av_data_recv, _msg_notify);
startAvRecvService("action=live");
void _av_data_recv(uint8_t *data, size_t len) {
	//具体数据处理
}
stopAvRecvService(NULL);
```
	
#### 2. 接收 FLV 音视频流，使用 ijkplayer 播放
  - 函数声明：
  ```
	const char *delegateHttpFlv(); // 获取本地请求数据的标准http url,可使用该url请求设备端数据
	```
  - 播放器调用示例：
```
char url[128] = { 0 };
/* 组合请求url */
snprintf(url, sizeof(url), "%s%s", delegateHttpFlv($id), "ipc.flv?action=live");
/* 设置url到播放器 */
setUrl2Player(url);
```

### 步骤3：发送语音对讲数据

  - 函数声明：
	```
	void *runSendService(); //启动p2p数据发送服务
  int dataSend(uint8_t *data, size_t len);  //语音数据发送接口
	```
  - 代码示例：
  ```
	runSendService();
  while (1) {
					dataSend(audio_data, data_len);
					usleep(100 * 1000);
  }
  stopSendService(NULL);  //停止发送服务
	```
	
### 步骤4：P2P 通道传输自定义数据

#### 1. 发送自定义数据

- 函数声明：
	```
	int getCommandRequestWithSync(const char *params, char **buf, size_t *len, uint64_t timeout_us);  //同步发送
	int getCommandRequestWithAsync(const char *params);  //异步发送
	```
- 代码示例：
	- 异步方式：
		```
		setUserCallbackToXp2p(_av_data_recv, _msg_notify);  //设置回调
		getCommandRequestWithAsync("action=user_define&cmd=custom_cmd");
		```
	- 同步方式：
		```
		char *buf = NULL;
		int len = 0;
		getCommandRequestWithSync("action=user_define&cmd=custom_cmd", &buf, &len, 2*1000*1000);  //接收的数据填充在buf中
		```
		
#### 2. 接收自定义数据
  - 函数声明：
 ```
  char* _msg_notify(int type, const char* msg);  //只有异步发送的才会在该回调返回接收的数据
	```
  - 代码示例：
  ```
	char* _msg_notify(int type, const char* msg) {
    	if (type == 2) {
    		// 处理返回结果
    	}
  }
```

### 步骤5：主动关闭 P2P 通道

  - 函数声明：
  ```
	void stopService();
	```
  - 代码示例：
 ```
  stopService();
	```
	
### 步骤6：P2P 通道关闭回调

- 函数声明：
```
char* _msg_notify(int type, const char* msg);
```
- 代码示例：
```
char* _msg_notify(int type, const char* msg) {
		if (type == 0) {
			//p2p通道正常关闭
		}
}
```

### 步骤7. P2P 通道错误断开回调
  - 函数声明：
  ```
  char* _msg_notify(int type, const char* msg);
	```
  - 代码示例：
  ```
  char* _msg_notify(int type, const char* msg) {
					if (type == 5) {
						//p2p通道错误断开
					}
  }
```

## aar 库调用方法


### 步骤1：P2P 通道初始化
  - 函数声明：
  ```
  public static void startServiceWithXp2pInfo(String xp2p_info)
	```
  - 代码示例：
  ```
  String xp2p_info = getXP2PInfo(...) // 从自建后台获取xp2p info
  XP2P.setCallback(this)
  XP2P.startServiceWithXp2pInfo(xp2p_info)
	```

	
### 步骤2：P2P 通道传输音视频流

#### 1. 接收裸数据
    
 - 函数声明：
```
public static void startAvRecvService(String cmd); // 启动接收数据服务, 使用该方法首先需调用setCallback()注册回调
override fun avDataRecvHandle(data: ByteArray?, len: Int); //裸数据回调接口
```  
 - 代码示例：
	```
	XP2P.setCallback(this)
	XP2P.startAvRecvService("action=live")  
	override fun avDataRecvHandle(data: ByteArray?, len: Int) {
		// 裸流数据处理操作可以放在这里
	}
	```
	
#### 2. 接收 FLV 音视频流，使用 ijkplayer 播放
   
- 函数声明：
```
String delegateHttpFlv() // 获取本地请求数据的标准http url,可使用该url请求设备端数据
```
- 播放器调用示例：
	```
	val url = XP2P.delegateHttpFlv() + "ipc.flv?action=live" //观看直播(action=live)，回放(action=playback)
	mPlayer.dataSource = url
	mPlayer.prepareAsync()
	mPlayer.start()
	```
 
### 步骤3：发送语音对讲数据
    
- 函数声明：
	```
	void runSendService() //启动p2p数据发送服务
	void dataSend(byte[] data, int len)
	```  
- 代码示例：
	```
	XP2P.runSendService()
	audioRecordUtil.start() // 采集音频并发送，内部调用了dataSend接口
	```
		
### 步骤4：P2P 通道传输自定义数据

#### 1. 发送自定义数据
- 函数声明：
```
void getCommandRequestWithAsync(String cmd) // 异步
String getComandRequestWithSync(String cmd, long timeout) //同步
```
- 代码示例：
```
 XP2P.getCommandRequestWithAsync("action=user_define&cmd=custom_cmd")
 ```
		 
#### 2. 接收自定义数据
- 函数声明：
```
override fun commandRequest(msg: String?) // 设备端回调App
```
- 代码示例：
```
override fun commandRequest(msg: String?) {
		Log.d(msg) //接收到的自定义数据后，添加业务逻辑
}
```
		
### 步骤5：主动关闭 P2P 通道

- 函数声明：
	```
	void stopService()
	```
- 代码示例：
	```
	override fun onDestroy() {
			super.onDestroy()
			mPlayer.release()
			XP2P.stopService()
	}
```

### 步骤6：P2P 通道关闭回调
  - 函数声明：
  ```
  override fun avDataCloseHandle(msg: String?, errorCode: Int)  //通道关闭后回调
	```
  - 代码示例：
  ```
  override fun avDataCloseHandle(msg: String?, errorCode: Int) {
  	//处理通道关闭后的事务
  }
```

### 步骤7：P2P 通道错误断开回调
  - 函数声明：
  ```
  override fun xp2pLinkError(msg: String?)  //通道错误断开后回调
	```
  - 代码示例：
 ```
 override fun xp2pLinkError(msg: String?) {
  	//处理通道错误断开后的事务
  }
```




