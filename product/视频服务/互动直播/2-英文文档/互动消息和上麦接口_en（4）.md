
## Interactive Messaging

iLiveSDK (Windows) provides messaging feature that allows sending broadcast messages to room members and C2C messages between users (adding friend is not needed). Currently, the SDK only supports text and custom messages.

### Send C2C message

C2C messages refer to peer-to-peer messages between two users. You can use C2C custom messages at business layer to invite other room members to join the broadcasting or to give likes, etc. Please see the demo for the implementation.

| API | Description |
|---|---|
| sendC2CMessage | Send C2C message |

| Parameter Type | Parameter Name | Description |
|---|---|---|
| const char * | dstUser |ID of receiver |
| const Message	& | message | IM message content |
| iLiveSuccCallback | suc | "Message sent successfully" callback |
| iLiveErrCallback | err | "Failed to send message" callback |
| void* | data | A pointer for user's custom data, which is returned intact in the callback function indicating success or failure |

* Example

```c++
void OnSendC2CMsgSuc( void* data )
{
  //C2C message sent successfully
}
void OnSendC2CMsgErr( int code, const char *desc, void* data )
{
  //Failed to send C2C message
}
Message message;
MessageTextElem *elem = new MessageTextElem("hello");
message.elems.push_back(elem);
GetILive()->sendC2CMessage(  message, OnSendC2CMsgSuc, OnSendC2CMsgErr, NULL );
```

### Send broadcast message
Currently, sending broadcast message is only allowed in the same room. When a member sends a broadcast message, other members in the same room can receive the message.

| API | Description |
|---|---|
| sendGroupMessage | Send broadcast message |

| Parameter Type | Parameter Name | Description |
|---|---|---|
| const message & | message | Message content |
| iLiveSuccCallback | suc | "Message sent successfully" callback |
| iLiveErrCallback | err | "Failed to send message" callback |
| void* | data | A pointer for user's custom data, which is returned intact in the callback function indicating success or failure |

* Example

```c++
void OnSendGroupMsgSuc( void* data )
{
  //Broadcast message sent successfully
}
void OnSendGroupMsgErr( int code, const char *desc, void* data )
{
  //Failed to send broadcast message
}
Message message;
MessageTextElem *elem = new MessageTextElem("hello");
message.elems.push_back(elem);
GetILive()->sendGroupMessage(  message, OnSendGroupMsgSuc, OnSendGroupMsgErr, NULL );
```
## Receive Message

After setting the message listening callback, SDK notifies the upper layer every time it receives a message.

```c++
void OnMessage(const Message& message)
{
	std::string szSender = message.sender.c_str();	
	for (size_t i = 0; i < message.elems.size(); ++i)
	{
		MessageElem *pElem = message.elems[i];
		switch( pElem->type )
		{
		case TEXT:
			{				
				MessageTextElem *elem = static_cast<MessageTextElem*>(pElem);
				std::cout << elem->content.c_str() << std::endl;
				break;
			}
		case CUSTOM:
			{
				MessageCustomElem *elem = static_cast<MessageCustomElem*>(pElem);
				std::string szDate = elem->data.c_str();
				break;
			}
		default:
			break;
		}
	}
}
GetILive()->setMessageCallBack(OnMessage, NULL);
```

## Joint Broadcasting

### VJ invites viewer to join broadcasting:
![Invitation to join broadcasting](https://mc.qcloudimg.com/static/img/fba65e3aea7b724de6a378589ce5ea55/image.png)<br/>

### VJ disconnects the viewer from the joint broadcasting:
![Disconnect from Joint Broadcasting](https://mc.qcloudimg.com/static/img/c0f507d28e9fb94d21aa6d441ba49623/image.png)<br/>

### APIs
Wrappers for joining/quitting broadcasting are not available in iLiveSDK. Please refer to sendC2CCustomCmd() and sendGroupCustomCmd() functions and send custom messages as the invitation to joint broadcasting and acceptance of the invitation. To join or quit a broadcasting, a viewer needs to change his or her role and permission.

- Change the role

| API | Description |
|---|---|
| changeRole | Change role |

| Parameter Type | Parameter Name | Description |
|---|---|---|
| const char * | szControlRole | Role string (configured by user App's console)
| iLiveSuccCallback | suc | Callback function indicating a success |
| iLiveErrCallback | err | Callback function indicating a failure |
| void* | data | A pointer for user's custom data, which is returned intact in the callback function indicating success or failure |

Example:
```c++
void OnChangeRoleSuc( void* data )
{
	//Role changed successfully
}
void OnChangeRoleErr( int code, const char *desc, void* data )
{
	//Failed to change the role
}
GetILive()->changeRole(Role, OnChangeRoleSuc, OnChangeRoleErr, NULL);
```


