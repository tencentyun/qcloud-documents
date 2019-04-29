# Interactive Messaging

iLiveSDK (IE) provides messaging feature that  allows sending broadcast messages to room members and C2C messages between users (adding friend is not needed). Currently, the SDK only supports text and custom messages.

## Send broadcast message
Currently, sending broadcast messages is only allowed in the same room. When a member send a broadcast message, other members in the same room can receive the message.

```JS
//For more information about ILiveMessageElem and ILiveMessage, please see API documentation.
var elem = new ILiveMessageElem(0, "message content");
var elems = [];
elems.push(elem);
var message = new ILiveMessage(elems);
sdk.sendGroupMessage(message, function () {
    alert("send message succ");
}, function (errMsg) {
    alert("error code:" + errMsg.code + " error message:" + errMsg.desc);
});
```

## Receive broadcast message
After listening for broadcast message is configured, broadcast messages can be received. Broadcast message can be configured after being initialized.

```JS
sdk.setMessageListener(function (msg) {
    //The definition of msg is described in the API documentation.
})
```

## Send C2C message
C2C messages refer to peer-to-peer messages between two users. You can use C2C custom messages at business layer to invite other room members to join the broadcasting. Please see the demo for the implementation.

```JS
//For more information about ILiveMessageElem and ILiveMessage, please see API documentation.
var elem = new ILiveMessageElem(0, "message content");
var elems = [];
elems.push(elem);
var message = new ILiveMessage(elems);
sdk.sendC2CMessage("somebody", message, function () {
    alert("send message succ");
}, function (errMsg) {
    alert("error code:" + errMsg.code + " error message:" + errMsg.desc);
});
```

## Receive C2C message
After listening for C2C message is configured, C2C messages can be received. C2C message can be configured after being initialized.

```JS
sdk.setMessageListener(function (msg) {
    //The definition of msg is described in the API documentation.
})
```


## Joint Broadcasting
Joining broadcasting is achieved by modifying the audio and video permissions. The process for joining broadcasting is:

> Switch Role -> Enable Camera -> Render Video

The process for quitting broadcasting is:

> Switch Role -> Disable Camera -> Finish Rendering

You can go to console to [configure scenario and roles](https://cloud.tencent.com/document/product/268/7599), and then call the API to switch role.

```js
//liveMaster is the role configured in the console.
sdk.changeRole("LiveMaster");
```

