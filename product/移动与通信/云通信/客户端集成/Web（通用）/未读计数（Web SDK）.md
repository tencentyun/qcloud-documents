## 获取当前会话未读消息数 

可以根据 `Session` 对象定义的 `unread()` 方法获取未读消息数。**示例：**

```
//获取全局的 sessMap
var sessMap = webim.MsgStore.sessMap();
//这里的 GROUPID 为"GROUP"+群 id
//C2CID 为"C2C"+identifier
sessMap["GROUPID"].unread();
sessMap["C2CID"].unread();
```

**示例： **

```
//更新其他聊天对象的未读消息数
updateSessDiv(sess.id(), sess.unread());
```

## 设置会话自动已读标记 

当用户阅读某个会话的数据后，需要进行会话消息的已读上报，SDK 根据会话中最后一条阅读的消息，设置会话中之前所有消息为已读。 **函数名：**

```
/* function setAutoRead
 *   //设置会设置会话自动已读标记话自动已读上报标志
 * params:
 *   selSess	- webim.Session类型, 当前会话
 *   isOn	- boolean, 将selSess的自动已读消息标志改为isOn，同时是否上报当前会话已读消息
 *   isResetAll	- boolean，是否重置所有会话的自动已读标志
 * return:
 *   (无)
 */
setAutoRead: function(selSess, isOn, isResetAll) {},
```

**示例： **

```
//消息已读上报，以及设置会话自动已读标记
webim.setAutoRead(selSess, true, true);
```