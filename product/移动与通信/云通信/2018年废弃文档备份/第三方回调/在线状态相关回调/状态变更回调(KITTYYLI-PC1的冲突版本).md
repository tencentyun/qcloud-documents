## 1 功能说明 

App后台可以通过该回调实时监控用户上、下线的行为，包括：
1. 用户上线（TCP连接建立）；
2. 用户注销下线或者用户网络断开（TCP连接断开）；
3. App心跳超时（App异常杀后台或者Crash）。

## 2 注意事项 

1. 要启用回调，必须配置回调URL，并打开本条回调协议对应的开关，配置方法详见第三方回调配置；
2. 回调的方向是：云通讯后台向APP后台发起HTTP POST请求；
3. App后台在收到回调请求之后，**务必校验请求URL中的参数SdkAppid是否是自己的SdkAppid**；
4. 其他安全相关事宜请参考第三方回调：安全考虑；
5. **可能会有大量的心跳超时包（Crash、杀后台等），业务需注意回调响应服务器性能。**
 
## 3 可能触发该回调的场景 

1.用户通过客户端发起上线请求；
2.用户通过客户端发起退出的下线请求；
3.客户端杀后台进程，云服务检测到客户端网络断开后触发下线回调；
4.客户端心跳超时，包括客户端Crash、关闭网络400秒后，云服务检测到客户端的心跳超时触发下线回调。
 

## 4  回调发生时机 

IM云server收到客户端的**TCP连接建立、TCP连接断开、若干心跳包**无法收到后发生。 

## 5 接口说明 

### 5.1 请求URL 

`https://www.example.com/SdkAppid=$SdkAppid&CallbackCommand=$CallbackCommand&contenttype=json`
此处假定APP配置的回调URL为 `https://www.example.com` 。 

### 5.2 请求参数 

<table style="width:100%;" >
		<tbody>
			<tr>
				<td style="width:25%;background-color:#CCCCCC;">
					参数<br />
				</td>
				<td style="background-color:#CCCCCC;">
					含义<br />
				</td>
			</tr>
			<tr>
				<td>
					SdkAppid<br />
				</td>
				<td>
					APP在云通讯申请的Appid。
				</td>
			</tr>
			<tr>
				<td>
					CallbackCommand<br />
				</td>
				<td>
					固定为：State.StateChange 。<br />
				</td>
			</tr>
			<tr>
				<td>
					contenttype<br />
				</td>
				<td>
					固定为：json。<br />
				</td>
			</tr>
			<tr>
				<td>
					ClientIP<br />
				</td>
				<td>
					客户端IP，格式如:127.0.0.1。<br />
				</td>
			</tr>
			<tr>
				<td>
					OptPlatform<br />
				</td>
				<td>
					设备类型，分为Windows，Web，Android，iOS，Mac和Unknown。<br />
				</td>
			</tr>
		</tbody>
	</table>

### 5.3 HTTP请求方式 

POST 

### 5.4 HTTP请求包体格式 

JSON 

### 5.5 回调请求包示例 

```
{
    "CallbackCommand": "State.StateChange",
    "Info": {
        "Action": "Logout",
        "To_Account": "testuser316",
        "Reason": "Unregister"
    }
}

```

### 5.6 回调请求包字段说明 

<table style="width:100%;" >
		<tbody>
			<tr>
				<td style="width:25%;background-color:#CCCCCC;">
					字段
				</td>
				<td style="width:5%;background-color:#CCCCCC;">
					类型
				</td>
				<td style="background-color:#CCCCCC;">
					说明
				</td>
			</tr>
			<tr>
				<td>
					CallbackCommand<br />
				</td>
				<td>
					String
				</td>
				<td>
					回调命令。<br />
				</td>
			</tr>
			<tr>
				<td>
					Info<br />
				</td>
				<td>
					Object
				</td>
				<td>
					用户上下线的信息。
				</td>
			</tr>
			<tr>
				<td>
					To_Account<br />
				</td>
				<td>
					String
				</td>
				<td>
					用户的ID。
				</td>
			</tr>
			<tr>
				<td>
					Action<br />
				</td>
				<td>
					String
				</td>
				<td>
					App上线或者下线的动作， Login：上线（TCP建立），Logout下线（TCP断开）。
				</td>
			</tr>		
			<tr>
				<td>
					Reason<br />
				</td>
				<td>
					String
				</td>
				<td>
					App上下线触发的原因。上线的原因有Register:App TCP连接建立。下线的原因有Unregister:App用户注销账号导致TCP断开;
					LinkClose:云通信检测到App TCP连接断开;Timeout：云通信检测到App心跳包超时，认为TCP已断开（客户端杀后台或Crash）。
				</td>
			</tr>
		</tbody>
	</table>
	
### 5.7 回调应答包示例

```
{
    "ActionStatus": "OK", 
    "ErrorCode": 0,
    "ErrorInfo": ""
}
```

### 5.8 应答包字段说明 

<table style="width:100%;" >
		<tbody>
			<tr>
				<td style="width:25%;background-color:#CCCCCC;">
					字段
				</td>
				<td style="width:5%;background-color:#CCCCCC;">
					类型
				</td>
				<td style="width:5%;background-color:#CCCCCC;">
					属性
				</td>
				<td style="background-color:#CCCCCC;">
					说明
				</td>
			</tr>
			<tr>
				<td>
					ActionStatus<br />
				</td>
				<td>
					String
				</td>
				<td>
					必填
				</td>
				<td>
					请求处理的结果，OK表示处理成功，FAIL表示失败。
				</td>
			</tr>
			<tr>
				<td>
					ErrorCode<br />
				</td>
				<td>
					Integer
				</td>
				<td>
					必填
				</td>
				<td>
					错误码，0表示APP后台处理成功，1表示APP后台处理失败。
				</td>
			</tr>
			<tr>
				<td>
					ErrorInfo<br />
				</td>
				<td>
					String
				</td>
				<td>
					必填
				</td>
				<td>
					错误信息。
				</td>
			</tr>
		</tbody>
	</table>

## 6 参考 

[第三方回调简介](/doc/product/269/第三方回调简介)
[用户在线状态综述](/doc/product/269/用户在线状态综述)

