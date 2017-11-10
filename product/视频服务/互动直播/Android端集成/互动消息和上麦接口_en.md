## Messaging and Interactively Joining Broadcasting

### 1. Send a Message

#### 1.1 Send Plain Text Messages
| API |  Description  |
|---------|---------|
| **sendText** | Send text messages. You can send broadcast messages and C2C messages through various types of message bodies |


| Parameter | Description |
|---------|---------|
| ILVText | Text message class. You can specify message types (broadcast messages or C2C message), message content and message receiver (group ID or user ID) |
| ILiveCallBack | API for message sending callback |

* Example of sending text

```java          
            //Send message
            ILVText iliveText = new ILVText("ss", "", ILVLiveConstants.GROUP_TYPE);
            iliveText.setText("" + textInput.getText());
            //Send message
            ILVLiveManager.getInstance().sendText(iliveText, new ILiveCallBack() {
                @Override
                public void onSuccess(Object data) {
                    Toast.makeText(LiveActivity.this, "send succ!", Toast.LENGTH_SHORT).show();
                }

                @Override
                public void onError(String module, int errCode, String errMsg) {

                }

            });
```


#### 1.2 Send Signaling Messages
| API |  Description  |
|---------|---------|
| **sendCustomCmd** | Send signaling messages. You can send broadcast messages and C2C messages through various types of message bodies |


| Parameter | Description |
|---------|---------|
| ILVCustomCmd | Signaling message class. You can specify message types (broadcast messages or C2C message), message content, message receiver (group ID or user ID), and String type parameter |
| ILiveCallBack | API for message sending callback |

* Example of inviting to join broadcasting

```java 
            //Invite to join broadcasting
            ILVCustomCmd cmd = new ILVCustomCmd();
            cmd.setCmd(ILVLiveConstants.ILVLIVE_CMD_INVITE);
            cmd.setType(ILVLiveConstants.C2C_TYPE);
            cmd.setDestid("" + memId.getText());
            cmd.setParam("");
            ILVLiveManager.getInstance().sendCustomCmd(cmd, new ILiveCallBack<TIMMessage>() {
                @Override
                public void onSuccess(TIMMessage data) {
                    Toast.makeText(LiveActivity.this, "invite send succ!", Toast.LENGTH_SHORT).show();
                }

                @Override
                public void onError(String module, int errCode, String errMsg) {

                }

            });            
```        

*  **Note: To help users to customize signaling messages, iLiveSDk retains a custom zone**<br/>
```java    
    public static final int ILVLIVE_CMD_CUSTOM_LOW_LIMIT = 0x800;          //Custom message segment lower limit
    public static final int ILVLIVE_CMD_CUSTOM_UP_LIMIT = 0x900;          //Custom message segment upper limit
```




         
### 2. Resolve Messages

> ILVLiveConfig is global LVB configuration where a message callback ILVLiveConfig.ILVLiveMsgListener can be configured. You can get corresponding message type using this message callback, and place it back to ILVLiveManager for configuration.
 
| Parameter | Description |
|---------|---------|
| onNewCmdMsg | Pre-defined iLiveSDK signalling callback, for example, joining broadcasting and quitting broadcasting |
| onNewCustomMsg | User-defined signaling callback |
| onNewTextMsg | Plain text reception callback |

* Example

```java
        ILVLiveConfig liveConfig = new ILVLiveConfig();

        liveConfig.setLiveMsgListener(new ILVLiveConfig.ILVLiveMsgListener() {
            @Override
            public void onNewTextMsg(String text, String id) {
                Toast.makeText(LiveActivity.this, "onNewTextMsg : " + text, Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onNewCmdMsg(int cmd, String param, String id) {
                switch (cmd) {
                    case ILVLiveConstants.ILVLIVE_CMD_INVITE:
                        Toast.makeText(LiveActivity.this, "onNewCmdMsg : received a invitation! ", Toast.LENGTH_SHORT).show();
                        ILiveLog.d(TAG, "ILVB-LiveApp|received ");
                        ILVLiveManager.getInstance().upToVideoMember(ILVLiveConstants.VIDEO_MEMBER_AUTH, ILVLiveConstants.VIDEO_MEMBER_ROLE, new ILiveCallBack() {
                            @Override
                            public void onSuccess(Object data) {

                            }

                            @Override
                            public void onError(String module, int errCode, String errMsg) {

                            }
                        });
                        break;
                    case  ILVLiveConstants.ILVLIVE_CMD_INVITE_CANCEL:

                        break;
                    case ILVLiveConstants.ILVLIVE_CMD_INVITE_CLOSE:
                        ILVLiveManager.getInstance().downToNorMember(ILVLiveConstants.NORMAL_MEMBER_AUTH, ILVLiveConstants.NORMAL_MEMBER_ROLE, new ILiveCallBack() {
                            @Override
                            public void onSuccess(Object data) {

                            }

                            @Override
                            public void onError(String module, int errCode, String errMsg) {

                            }
                        });
                        break;
                    case ILVLiveConstants.ILVLIVE_CMD_INTERACT_AGREE:
                        break;
                    case  ILVLiveConstants.ILVLIVE_CMD_INTERACT_REJECT:
                        break;
                }

            }

            @Override
            public void onNewCustomMsg(int cmd, String param, String id) {
                Toast.makeText(LiveActivity.this, "cmd "+ cmd, Toast.LENGTH_SHORT).show();

            }
        });
```                               
            
            
  
### 3. Join Broadcasting for Interaction
            
#### 3.1 Action of Joining Broadcasting  
>  "Switch Role" -> "Enable Camera" -> "Render Image" (if auto rendering is enabled, this step can be skipped)

| API | Description |
|---------|---------|
| upToVideoMember | Integrate role switchover, permission, scenario, enabling camera into one step |


* Example     

```java
ILVLiveManager.getInstance().upToVideoMember(ILVLiveConstants.VIDEO_MEMBER_AUTH, ILVLiveConstants.VIDEO_MEMBER_ROLE, new ILiveCallBack() {
                            @Override
                            public void onSuccess(Object data) {

                            }

                            @Override
                            public void onError(String module, int errCode, String errMsg) {

                            }
                        });
```


#### 3.2 Action of Quitting Broadcasting  
>  "Switch Role" -> "Disable Camera" -> "Finish Rendering"

| API | Description |
|---------|---------|
| downToNorMember | Integrate role switchover, permission, scenario, closing camera into one step |


* Example     

```java
ILVLiveManager.getInstance().downToNorMember(ILVLiveConstants.NORMAL_MEMBER_AUTH, ILVLiveConstants.NORMAL_MEMBER_ROLE, new ILiveCallBack() {
                            @Override
                            public void onSuccess(Object data) {

                            }

                            @Override
                            public void onError(String module, int errCode, String errMsg) {

                            }
                        });
```

