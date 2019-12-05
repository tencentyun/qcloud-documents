## Data Structure and Function Description
### class ToaFetcher
A subject class which is used to manage the obtainment and release of TOA.

### InitUpToaFetcher
#### Function description
This function is used to initialize TOA fetcher.

bool InitUpToaFetcher(char *ncard_ip_str, char *svr_ip_str, u_short svr_port[], u_short svr_port_num, u_short cache_secs=TIMER_CACHE_SECS)

#### Input parameter description
ncard_ip_str is used to identify the IP address string of network interface, for example, "10.75.132.39". The ENI is the one for communicating with the client, as shown in the following figure:
![](https://main.qcloudimg.com/raw/b9af3663b55b043d5891dfc2baa42877.png)
vr_ip_str: IP address string of the server, for example, "10.75.132.39" for filtering TCP streams.
svr_port: Port list of the server for filtering TCP streams. You can enter up to three ports and at least one port.
svr_port_num: Number of ports of the server.
cache_secs: The length of cache in seconds. 15 seconds by default. For details, see toa_fetcher.h: TIMER_CACHE_SECS. The TOA will no longer be saved after the cache has expired.

#### Returned value
TRUE: Indicates that the creation of TOA for obtaining bypass thread is successful.
FALSE: Indicates that the creation of TOA for obtaining bypass thread is failed.

### FetchToaValue
#### Function description
This function is used to obtain the TOA value. If the tcp-syn packet is interacted, the TOA can be obtained after waiting for up to 1 ms. Normally, the three-way handshake consumes more than 1 ms.

bool FetchToaValue(u_long fake_client_ip_addr, u_short fake_client_port, u_long &real_client_ip_addr, u_short &real_client_port)

#### Input parameter description
fake_client_ip_addr: The dummy client IP address which is stored in network order and obtained from the peer address returned by accept function of the server.
fake_client_port: The dummy client port number which is stored in network order and obtained from the peer address returned by accept function of the server.
real_client_ip_addr: The real client IP address which is stored in network order and obtained from TOA.
real_client_port: The real client port number which is stored in network order and obtained from TOA.

#### Returned value
TRUE: TOA is successfully obtained
FALSE: If the TOA is not obtained, it is generally that the cache time is exceeded, which causes the TOA to be cleared.


### StopToaFetcher
#### Function description
This function is used to stop TOA fetcher.

void StopToaFetcher()

#### Input parameter description
None.
#### Returned value
None.

### GetFetcherStatus
#### Function description
This function is used to obtain the Fetcher status.

int GetFetcherStatus()

#### Input parameter description
None.
#### Returned value
0: Indicates the initial status. After the instance is created, it is the initial status. In Fetcher initialization, the initial status remains unchanged. When an error occurs, -1 is returned, and when it runs successfully, 1 is returned.
-1: Indicates exceptional status.
1: Indicates normal running.

### FetchThreadHandler
#### Function description
This function is used to obtain the TOA bypass thread handle.

HANDLE FetchThreadHandler()

 #### Input parameter description
None.
#### Returned value
The TOA bypass thread handle, which is actively closed when the ToaFetcher instance is terminated.

### FetchErrorInfo
#### Function description
This function is used to obtain the error code.

bool FetchErrorInfo(int* err_code_ptr, char* err_msg_ptr)

#### Input parameter description
err_code_ptr: An integer pointer which points to the error code and is used to return the error code.
err_msg_ptr: A character pointer which points to a string buffer of at least 50 bytes and is used to return an error message.

#### Returned value
TRUE: Obtained successfully.
FALSE: Failed to obtain.

## Error Codes
| Error Code | Error Message | Description |
|---------|---------|---------|
| 0 | Ok | Normal |
| -1001 | Exceed max server port number | The maximum number of ports is exceeded, please check CreateToaFetecherThread: svr_port_num |
| -1002 | Invalid IP address | Invalid IPv4 address. |
| -1003 | No suitable network interface | No suitable network interface is found. |
| -1004 | System Error: find dev error | System error: dev is not found. Please contact the lib developer. |
| -1005 | System Error: start timer error | System error: Timer startup error. Please contact the lib developer. |
| -1006 | System Error: compile filter error | System error: Filter rule compilation error. Please contact the lib developer. |
| -1007 | System Error: set filter error | System error: Filter rule setting error. Please contact the lib developer. |
| -1008 | System Error: open pcap error | System error: dev enabling error. Please contact the lib developer. |
| -1009 | System Error: start pcap error | System error: Listening enabling error. Please contact the lib developer. |
| -1010 | System Error: begin thread error | System error: Thread enabling error. Please contact the lib developer. |
| -1999 | Unknown error | Unknown error. Please contact the lib developer. |


## Example
Initialize ToaFetcher:
```
char ncard_ip_str[] = "1.1.1.1";
char svr_ip_str[] = "1.1.1.1";
u_short svr_port_list[3] = {1111, 2222, 3333};
ToaFetcher inst = ToaFetcher();
inst.InitUpToaFetecher((char*)ncard_ip_str, (char*)svr_ip_str, svr_port_list, 3);
```

Obtain TOA:
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
    	//fpp: Custom print function
		fpp("real_client_ip_addr", &real_client_ip_addr, 4);	
　　fpp("real_client_port", &real_client_port, 2);
	}
}
```














