# ILVB API

The audio/video messaging capabilities of iLiveSDK are abstracted as a "room". A member can watch the videos of other members within the same room, and a maximum of 4 parallel video streams are allowed in a room. iLiveSDK (IE) provides room management, audio and video device management and other features to allow users to set up interactive videos. The business process of ILVB is as follows:

![Business Process]http://mc.qcloudimg.com/static/img/e6632b362fbc90745505823b1dc295bd/image.png)

## Create Object
Create an iLiveSDK object for later use.

```
//iLiveSDK is the ID of cab component.
var sdk = new ILiveSDK(sdkappid, accounttype, "iLiveSDK");
```

## Initialization
iLiveSDK must be initialized before you use other features.

```
sdk.init(function () {
    alert("init succ");
}, function (errMsg) {
    alert("error code:" + errMsg.code + " error message:" + errMsg.desc);
});
```

## Login
You can use messaging, interactive video and other features only after login. User ID and signature are required for login. Signature is provided by [Tencent Login Service]https://cloud.tencent.com/document/product/269/1507).

```
sdk.login(id, sig, function () {
    alert("login succ");
}, function (errMsg) {
    alert("error code:" + errMsg.code + " error message:" + errMsg.desc);
});
```

## Audio/Video Permission Management

**At business layer, the focus is placed on the audio and video permissions of room members**.  Only VJs or the viewers who need to join the broadcasting are granted the permission to send upstream audio and video. Before joining or creating a room, you need to enter the correct permissions (see "Join/Create a Room" below). Members are allowed to change their permissions in the room.   
You can go to Tencent Cloud [console to configure](https://github.com/zhaoyang21cn/suixinbo_doc/blob/master/SPEARConfig.md) the roles and relevant permissions to meet your business needs. Tencent CVMs assign different [access machines](https://cloud.tencent.com/document/product/268/7651) based on the permissions of room members. Incorrectly configured permissions can cause unnecessary bandwidth costs and abnormal upstream data at viewer end.



## Join/Create a Room
When creating a room, you can set role permissions and room number, which must be unique.

```js
sdk.createRoom(roomid, "LiveMaster", function () {
    alert("create room succ");
}, function (errMsg) {
    alert("error code:" + errMsg.code + " error message:" + errMsg.desc);
});
```
When joining a room, you can enter role permissions and room number.

```js
sdk.joinRoom(roomid, "Guest", function () {
    alert("join room succ");
}, function (errMsg) {
    alert("error code:" + errMsg.code + " error message:" + errMsg.desc);
});
```

## Device Management

### Enable camera
When the member who has upstream permission in the room enables the camera, other room members can access the video data. The upstream data of members without permission will be discarded by the server. Before enabling the camera, you can call the API to get the current camera list.

```js
var szRet = sdk.getCameraList();
if (szRet.code != 0) {
    alert("Error while obtaining the camera list; error code:" + szRet.code);
    return;
}
var nRet = sdk.openCamera(szRet.cameras[0].id);
if (nRet != 0) {
    alert("Failed to enable the camera; error code:" + nRet);
}
```
### Disable camera
When you need to stop the video, disable the camera.

```js
var nRet = sdk.closeCamera();
```
### Enable microphone

```js
var nRet = sdk.openMic();
```
### Disable microphone

```js
var nRet = sdk.closeMic();
```
## Video Rendering
After receiving the video data of each user, you need to use the rendering control to render the received videos.

```js
render.setIdentifer( userid ); //After you have set a user ID for the rendering control, the control will render the received data of the user automatically.
```
When the user's video data is stopped, the rendering control needs to be released.

```js
render.freeRender();
```

##  Beauty Filter
Set the beautifying level 0-10

```JS
sdk.setBeauty(beauty);
```

Set the whitening level 0-10

```JS
sdk.setWhite(white);
```

 Terminate the beauty filter resources; if beauty filter feature is enabled, when the camera is disabled, you just need to call the beauty filter.

```JS
sdk.destroyFilter();
```

Notes:
 1. By default, beauty filter is disabled on SDK.
 2. When beautifying and whitening levels are all set to 0, beauty filter is automatically disabled on SDK. If either of the levels is not 0, the beauty filter is enabled.
 3. It is recommended not to call API sdk.destroyFilter until the camera is disabled.





## Exit the Room
Exit the room and reclaim resources

```js
sdk.quitRoom(function () {
    alert("quit room succ");
}, function (errMsg) {
    alert("error code:" + errMsg.code + " error message:" + errMsg.desc);
});
```




## Logout
The reverse operation of login

```
sdk.logout(function () {
    alert("logout succ");
}, function (errMsg) {
    alert("error code:" + errMsg.code + " error message:" + errMsg.desc);
});
```

## Online Status
A logged user has an online status, and each account can only log in to one terminal at a time. If someone logs in to another terminal with the same user ID, the currently logged user will be kicked off the line and receive an notification on the current terminal.   
SDK allows you to configure listening for kick-off-line notification. When receiving the notification, business layer can process the change of login status at a higher level.
```
sdk.setForceOfflineListener(function() {
    alert ("You have been kicked off line, please re-log in");
});
```

