## 数据结构和函数说明
### class ToaFetcher
主体类，用于管理 TOA 的获取和释放。

### InitUpToaFetcher
#### 函数说明
该函数用于初始化 TOA fetcher

bool InitUpToaFetcher(char *ncard_ip_str, char *svr_ip_str, u_short svr_port[], u_short svr_port_num, u_short cache_secs=TIMER_CACHE_SECS)

#### 入参说明
ncard_ip_str	用于识别网络接口的IP地址字符串，例如：”10.75.132.39”，该网卡为与客户端通信的网卡，如下图所示：
![](https://main.qcloudimg.com/raw/b9af3663b55b043d5891dfc2baa42877.png)
vr_ip_str：服务器的 IP 地址字符串，例如：”10.75.132.39”，用于过滤 TCP 流。
svr_port：服务器的端口列表，用于过滤TCP流，最多可以填三个端口，最少一个。
svr_port_num：服务器的端口个数。
cache_secs：缓存的时长，单位：秒，默认 15 秒，详见 toa_fetcher.h：TIMER_CACHE_SECS，缓存时间到期后，将不再保存该 TOA。

#### 返回值
TRUE：表示创建 TOA 获取旁路线程成功。
FALSE：表示创建 TOA 获取旁路线程失败。

### FetchToaValue
#### 函数说明
该函数用于获取 TOA 值，tcp-syn 包交互后，最长需要等待 1ms 后可以获取到 TOA，正常情况下三次握手需要消耗 1ms 以上。

bool FetchToaValue(u_long fake_client_ip_addr, u_short fake_client_port, u_long &real_client_ip_addr, u_short &real_client_port)

#### 入参说明
fake_client_ip_addr：客户端伪 IP 地址，采用网络序存储，从服务器 accept 函数返回的对端地址中获取。
fake_client_port：客户端伪端口号，采用网络序存储，从服务器 accept 函数返回的对端地址中获取。
real_client_ip_addr：客户端真实 IP 地址，采用网络序存储，从 TOA 中获取。
real_client_port：客户端真实端口号，采用网络序存储，从 TOA 中获取。

#### 返回值
TRUE：获取 TOA 成功
FALSE：未获取到 TOA，一般是超过缓存时间导致 TOA 被清掉。


### StopToaFetcher
#### 函数说明
该函数用于停止 TOA fetcher。

void StopToaFetcher()

#### 入参说明
无。
#### 返回值
无。

### GetFetcherStatus
#### 函数说明
该函数用于获取 Fetcher 状态。

int GetFetcherStatus()

#### 入参说明
无。
#### 返回值
0：表示初始状态。创建实例后，初始状态处于该状态，Fetcher 初始化中，该状态保持不变，当中间出现错误时，返回 -1，当成功运行时，返回 1。
-1：表示异常状态。
1：表示正常运行中。

### FetchThreadHandler
#### 函数说明
该函数用于获取 TOA 旁路线程句柄。

HANDLE FetchThreadHandler()

 #### 入参说明
无。
#### 返回值
TOA 旁路线程句柄，当 ToaFetcher 实例被销毁时，将主动关闭该句柄。

### FetchErrorInfo
#### 函数说明
该函数用于获取错误码。

bool FetchErrorInfo(int* err_code_ptr, char* err_msg_ptr)

#### 入参说明
err_code_ptr：一个整型指针指向错误码，用于返回错误码。
err_msg_ptr	：一个字符指针指向字符串缓冲区，至少 50 字节，用于返回错误信息。

#### 返回值
TRUE：获取正常。
FALSE：获取异常。

## 错误码
| 错误码 | 错误信息 | 说明 |
|---------|---------|---------|
| 0	       | Ok	| 正常 |
| -1001	|Exceed max server port number |	超过最大的端口数，请检查 CreateToaFetecherThread：svr_port_num |
| -1002	| Invalid IP address	| 非法的 IPv4 地址。 |
| -1003	| No suitable network interface	|未找到合适的网络接口。|
| -1004	| System Error: find dev error	| 系统错误：未找到 dev，请联系 lib 开发者。|
| -1005	| System Error: start timer error	|系统错误：定时器启动错误，请联系 lib 开发者。|
| -1006	| System Error: compile filter error	| 系统错误：过滤规则编译错误，请联系lib开发者。|
| -1007	| System Error: set filter error	| 系统错误：过滤规则设置错误，请联系 lib 开发者。|
| -1008	| System Error: open pcap error |	系统错误：打开 dev 错误，请联系 lib 开发者。|
| -1009	| System Error: start pcap error	|系统错误：启动监听错误，请联系 lib 开发者。|
| -1010	| System Error: begin thread error	| 系统错误：启动线程错误，请联系 lib 开发者。|
| -1999	| Unknown error	| 未知错误，请联系 lib 开发者。|


## 示例
初始化 ToaFetcher：
```
char ncard_ip_str[] = "1.1.1.1";
char svr_ip_str[] = "1.1.1.1";
u_short svr_port_list[3] = {1111, 2222, 3333};
ToaFetcher inst = ToaFetcher();
inst.InitUpToaFetecher((char*)ncard_ip_str, (char*)svr_ip_str, svr_port_list, 3);
```

获取 TOA：
```
void GetToa(SOCKADDR_IN client_addr, ToaFetcher * toa_fetcher_ptr)
{
	u_long fake_client_ip_addr = 0;
	u_short fake_client_port = 0;
	u_long real_client_ip_addr = 0;
	u_short real_client_port = 0;
	memcpy(&fake_client_ip_addr, &client_addr.sin_addr, 4);
	memcpy(&fake_client_port, &client_addr.sin_port, 2);
	bool ret = toa_fetcher_ptr->FetchToaValue(fake_client_ip_addr, fake_client_port, real_client_ip_addr, real_client_port);
	if(ret == FALSE){
		printf("No toa found\n");
	}else{
    	//fpp: 自定义的打印函数
		fpp("real_client_ip_addr", &real_client_ip_addr, 4);	
　　fpp("real_client_port", &real_client_port, 2);
	}
}
```













