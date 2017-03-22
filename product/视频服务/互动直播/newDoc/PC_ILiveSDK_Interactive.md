# 互动消息和上麦

## 1 发送消息

### 1.1 发送C2C消息

|接口名|接口描述|
|---|---|
|sendC2CMessage|发送C2C消息|

|参数类型|参数名|说明|
|---|---|---|
|string|dstUser|接收方id|
|TIMMessage|message|IM消息内容|
|SuccessCalllback|suc|发送消息成功回调|
|ErrorCallback|err|发送消息失败回调|
|void*|data|用户自定义数据的指针，在成功和失败的回调函数中原封不动地返回|

* 示例

```c++
void OnSendC2CMsgSuc( void* data )
{
  //发送C2C消息成功
}
void OnSendC2CMsgErr( int code, const std::string& desc, void* data )
{
  //发送C2C消息失败
}
TIMMessage message;
TIMTextElem textElem;
textElem.set_content( text );
message.AddElem(&textElem);
iLiveSDK::getInstance()->sendC2CMessage(  message, OnSendC2CMsgSuc, OnSendC2CMsgErr, NULL );
```

### 1.2 发送群消息
发送群消息是指发送消息到当前加入的房间内,所以必须要先加入房间;

|接口名|接口描述|
|---|---|
|sendGroupMessage|发送群消息|

|参数类型|参数名|说明|
|---|---|---|
|TIMMessage|message|消息内容|
|SuccessCalllback|suc|发送消息成功回调|
|ErrorCallback|err|发送消息失败回调|
|void*|data|用户自定义数据的指针，在成功和失败的回调函数中原封不动地返回|

* 示例

```c++
void OnSendGroupMsgSuc( void* data )
{
  //发送群消息成功
}
void OnSendGroupMsgErr( int code, const std::string& desc, void* data )
{
  //发送群消息失败
}
TIMMessage message;
TIMTextElem textElem;
textElem.set_content( text );
message.AddElem(&textElem);
iLiveSDK::getInstance()->sendGroupMessage(  message, OnSendGroupMsgSuc, OnSendGroupMsgErr, NULL );
```
## 2 解析消息
- 初始化时，设置接收消息的回调函数:
```c++
class MessageCallBack : public imcore::TIMMessageCallBack
{
public:
	virtual void OnNewMessage(const std::vector<TIMMessage> &msgs)
	{
 		//在这里解析收到的消息
 	}
};
MessageCallBack m_messageCallBack;
iLiveSDK::getInstance()->SetMessageCallBack(&m_messageCallBack);
```
- 解析收到消息:
```c++
void OnNewMessage(const std::vector<TIMMessage> &msgs)
{
	int nCount = msg.GetElemCount();
	for (int i = 0; i < nCount; ++i)
	{
		imcore::TIMElem* pElem = msg.GetElem(i);
		switch( pElem->type() )
		{
			case kElemText://文本消息
			{
				std::string textMsg = pElem->GetTextElem()->content();
			}
			case kElemCustom://自定义消息
			{
				std::string Date = pElem->GetCustomElem()->data();
			}
			//其他消息类型...
		}
	}
}
```

## 3 上麦

### 3.1 主播邀请上麦流程:
![邀请上麦](https://mc.qcloudimg.com/static/img/fba65e3aea7b724de6a378589ce5ea55/image.png)<br/>

### 3.2 主播断开连麦观众流程:
![断开连麦](https://mc.qcloudimg.com/static/img/c0f507d28e9fb94d21aa6d441ba49623/image.png)<br/>

### 3.3 接口
iLiveSDK未对上/下麦进行封装，用户可以参考随心播的sendC2CCustomCmd()和sendGroupCustomCmd()函数，发送自定义消息作为邀请上麦和接受邀请的信令;观众上麦和下麦，需要切换用户角色和修改用户权限;

- 切换角色

|接口名|接口描述|
|---|---|
|changeRole|更改角色|

|参数类型|参数名|说明|
|---|---|---|
|string|szControlRole|角色字符串(由用户App的控制台配置)|
|SuccessCalllback|suc|成功的回调函数|
|ErrorCallback|err|失败的回调函数|
|void* |data | 用户自定义数据的指针，在成功和失败的回调函数中原封不动地返回|

示例:
```c++
void OnChangeRoleSuc( void* data )
{
	//切换角色成功
}
void OnChangeRoleErr( int code, const std::string& desc, void* data )
{
	//切换角色失败
}
iLiveSDK::getInstance()->changeRole(Role, OnChangeRoleSuc, OnChangeRoleErr, NULL);
```

- 修改权限

|接口名|接口描述|
|---|---|
|iLiveChangeAuthority|修改权限|

|参数类型|参数名|说明|
|---|---|---|
|uint64|authBits|通话能力权限位|
|string|authBuffer|通话能力权限位的加密串|
|SuccessCalllback|suc|成功的回调函数|
|ErrorCallback|err|失败的回调函数|
|void* |data | 用户自定义数据的指针，在成功和失败的回调函数中原封不动地返回|

示例:
```c++
void Live::OnChangeAuthoritySuc( void* data )
{
	//修改权限成功
}
void Live::OnChangeAuthorityErr( int code, const std::string& desc, void* data )
{
	//修改权限失败
}
iLiveSDK::getInstance()->changeAuthority(authBits, authBuffer, OnChangeAuthoritySuc, OnChangeAuthorityErr, NULL);
```
