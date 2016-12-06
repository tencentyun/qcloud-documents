#ILiveSDK直播基础接口简介
##简单直播流程示例

![](http://mc.qcloudimg.com/static/img/e6632b362fbc90745505823b1dc295bd/image.png)


###1 ILiveSDK初始化

| 接口名|  接口描述  |
|---------|---------|
| **initSDK** | iLiveSDK的部分类的预初始化，是所有行为的第一步，告知身份appId|


| 参数类型| 说明 |
|---------|---------|
| Conext | 建议用AppcalicationContext |
| int | 传入业务方appid |
| int | 传入业务方 accounttype |

*示例
  
```java 
ILiveSDK.getInstance().initSdk(getApplicationContext(), appid, accoutype);
```  


###2 账号登录
| 接口名|  接口描述  |
|---------|---------|
| **iLiveLogin** | 使用托管方式或独立模式，在获取到用户的sig后，使用登录接口，告知后台音视频模块上线了（包括avsdk）|

| 参数类型| 说明 |
|---------|---------|
| String | 用户id,在直播过程中的唯一标识  |
| String | 鉴权的密钥Sig 如果是独立登录方式，是业务方后台计算生成后下发的|
| ILiveCallBack | 帐号登录回调接口。通知上线是否成功 |
<br/>
*示例
    
```java     
ILiveLoginManager.getInstance().iLiveLogin(ILiveSDK.getInstance().getMyUserId(), "123456", new ILiveCallBack() {
                @Override
                public void onSuccess(Object data) {
                    bLogin = true;
                    Toast.makeText(ContactActivity.this, "login success !", Toast.LENGTH_SHORT).show();
                }

                @Override
                public void onError(String module, int errCode, String errMsg) {
                    Toast.makeText(ContactActivity.this, module + "|login fail " + errCode + " " + errMsg, Toast.LENGTH_SHORT).show();
                }
            });
```      
###3 创建房间

| 接口名| 接口描述 |
|---------|---------|
| **createRoom** | 创建一个直播，只有在初始化和登录成功之后才能创建直播|

| 参数类型| 说明 |
|---------|---------|
| int | 房间id 房间唯一标识 建议由业务方后台统一分配  |
| ILiveRoomOption | 房间配置项 可以设置角色 权限 主播ID 摄像头参数等 具体参考类ILiveRoomOption |
| ILiveCallBack | 创建房间回调接口。通知创建房间是否成功 |

```java            
  //创建房间配置项
            ILiveRoomOption hostOption = new ILiveRoomOption(null).
                    controlRole("Host")//角色设置
                    .authBits(AVRoomMulti.AUTH_BITS_DEFAULT)//权限设置
                    .cameraId(ILiveConstants.FRONT_CAMERA)//摄像头前置后置
                    .videoRecvMode(AVRoomMulti.VIDEO_RECV_MODE_SEMI_AUTO_RECV_CAMERA_VIDEO);//是否开始半自动接收
            //创建房间
            ILiveRoomManager.getInstance().createRoom(room, hostOption, new ILiveCallBack() {
                @Override
                public void onSuccess(Object data) {
                    Toast.makeText(LiveActivity.this, "create room  ok", Toast.LENGTH_SHORT).show();
                }

                @Override
                public void onError(String module, int errCode, String errMsg) {
                    Toast.makeText(LiveActivity.this, module + "|create fail " + errMsg + " " + errMsg, Toast.LENGTH_SHORT).show();
                }
            });
```
###4 加入房间
| 接口名|  接口描述  |
|---------|---------|
| **joinRoom** | 观众角色调用加入房间接口|


| 参数类型| 说明 |
|---------|---------|
| int | 房间id 房间唯一标识 建议由业务方后台统一分配  |
| ILiveRoomOption | 房间配置项 可以设置角色 权限 主播ID 摄像头参数等 具体参考类ILiveRoomOption |
| ILiveCallBack | 加入房间回调接口。通知加入房间是否成功 |
<br/>

```java  



           //加入房间配置项
            ILiveRoomOption memberOption = new ILiveRoomOption(hostId)
                    .autoCamera(false) //是否自动打开摄像头
                    .controlRole("NormalMember") //角色设置
                    .authBits(AVRoomMulti.AUTH_BITS_JOIN_ROOM | AVRoomMulti.AUTH_BITS_RECV_AUDIO |              AVRoomMulti.AUTH_BITS_RECV_CAMERA_VIDEO | AVRoomMulti.AUTH_BITS_RECV_SCREEN_VIDEO) //权限设置
                    .videoRecvMode(AVRoomMulti.VIDEO_RECV_MODE_SEMI_AUTO_RECV_CAMERA_VIDEO) //是否开始半自动接收
                    .autoMic(false);//是否自动打开mic
            //加入房间
            ILVLiveManager.getInstance().joinRoom(room, memberOption, new ILiveCallBack() {
                @Override
                public void onSuccess(Object data) {
                    bEnterRoom = true;
                    Toast.makeText(LiveActivity.this, "join room  ok ", Toast.LENGTH_SHORT).show();
                    logoutBtn.setVisibility(View.INVISIBLE);
                    backBtn.setVisibility(View.VISIBLE);
                }

                @Override
                public void onError(String module, int errCode, String errMsg) {
                    Toast.makeText(LiveActivity.this, module + "|join fail " + errMsg + " " + errMsg, Toast.LENGTH_SHORT).show();
                }
            });
```            
            
            
###设置渲染层
> 渲染层级示例图 在界面层xml插入一个AVRootView,音视频数据最终是通过AVRootView渲染出来。考虑多屏互动情况，AVRootView实际上不是一层View而是多层AVVideoView的叠加。直播业务默认主播在第0层默认最大，其他互动观众分别在1，2，3层。每层大小都可以动态调节。
> 

![](http://mc.qcloudimg.com/static/img/d063a1980cc046cafa0444df0b609d02/image.png)
* 示例

```java
    <com.tencent.ilivesdk.view.AVRootView
        android:id="@+id/av_root_view"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:background="@color/white" />
        
        
        avRootView = (AVRootView) findViewById(R.id.av_root_view);
        ILVLiveManager.getInstance().setAvVideoView(avRootView);
```  
        
[信令及上麦参见](./ILVLiveSenior.md)        
