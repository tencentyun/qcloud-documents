## 一. 音视频房间介绍
定义：音视频房间指的是用户通过登录进入一个封闭空间，进入了同一个封闭空间的成员就可以进行语音和视频交流。每个音视频房间都有一个房间号(roomID)，处于不同房间的成员互不影响。房间类为音视频房间的成员提供了很多获取房间和房间成员信息的方法。
## 二. 进房和退房
### 1.进入房间
进入房间操作含有以下两个步骤：
(1).通过配置AVMultiParam来设置房间号和音视频场景策略（如主播场景）等参数，以达到订制化的音视频效果。
   ![](//mccdn.qcloud.com/static/img/f20213fc76026ab7aa2f407eeb92dfa9/image.png)
	 
所有房间参数枚举值如下所示：
   ![](//mccdn.qcloud.com/static/img/0383ddf61f7477d11b8bc100daca4af4/image.png) 
	 ![](//mccdn.qcloud.com/static/img/923b8ddb63523817a265eae6b5edee03/image.png)
	 
(2).实现房间delegate定义的回调函数。多人房间delegate继承自房间类AVRoom的delegate类，需要新建一个AVRoomMulti.Delegate对象并在其中实现回调接口OnEnterRoomComplete()。
   ![](//mccdn.qcloud.com/static/img/a5fbf9b759be82267c7fe72f3c413f1c/image.png)
	 
(3).根据房间参数和代理调用enterRoom方法进入房间   
**接口描述：**
   ![](//mccdn.qcloud.com/static/img/ccec380f63155ba6262511fc8816da69/image.png)
	 ![](//mccdn.qcloud.com/static/img/923b8ddb63523817a265eae6b5edee03/image.png)
	 
**示例代码：**
   ![](//mccdn.qcloud.com/static/img/13e608b48c0bfd42234f992fb45148c1/image.png)
	 ![](//mccdn.qcloud.com/static/img/a76fb417bd48d9f5fa2bc3829bc57fc3/image.png)
 
### 2.退出房间 
(1)退出房间exitRoom()内部异步执行退出房间的流程，只有当房间退出异步完成之后，才能创建新的房间。
(2)异步返回结果通过调用enterRoom()方法时传递的roomDelegate中定义的onExitRoomComplete()返回。
(3)退出房间之后，不代表服务器上的房间被立即销毁，直到房间内所有人都退出房间，该房间才会被服务器销毁。目前SDK暂不提供显式销毁服务器房间的方法。

**接口描述：**
   ![](//mccdn.qcloud.com/static/img/01920c5f5517c13495773597a1d118eb/image.png)
	 
**示例代码：**
   ![](//mccdn.qcloud.com/static/img/99a145f4fb98ef6a709356f12e51a118/image.png)
## 三. 房间的监听回调 
除了进入房间和退出房间的回调，房间委托协议AVRoomDelegate中还定义了3个通知回调接口。
### 1.房间成员状态更新通知
用户在进入房间后，每次成员更新（有人加入房间或者退出房间）或者房间里的某个用户的视频状态的改变（某一个人开启摄像头或者关闭摄像头），都会回调通知到这个方法。
### 2.房间成员非法操作通知
房间里不同的角色拥有不同的权限。例如，在直播中，主播应该获得发送语音，发送视频等大部分权限。而作为普通观众，则应该被授予接受语音，接受视频这些权限，但是不具备发送语音和视频这样的权限。房间成员你的权限通过进入房间时上带的配置参数EnterRoomParam中的authBit和authBuffer字段来指定。如果不具备某项权限的成员进行相应操作，SDK就会回调此通知。
### 3.半自动接收视频的成员列表回调通知
进入房间所配置的参数EnterRoomParam中有对接收视频方式进行配置的字段，如2.1所述，当指定为自动接收视频时，成员进入房间后能自动接收房间中已经有数据上行的摄像头视频，屏幕分享数据不遵循这一逻辑，而且当进入房间以后，房间内又有新增的上行摄像头数据，也是无法自动接收的，仍然需要手动申请并通过调用requestview()方法获取。此时SDK会通过回调接口OnSemiAutoRecvCameraVideo()来通知App现在房间里拥有上行数据的成员列表，以便App进行渲染设置。
    ![](//mccdn.qcloud.com/static/img/076e1a77c35b07caee4eb03b712135d3/image.png)
		
**接口描述：**
    ![](//mccdn.qcloud.com/static/img/83ee3d1ac00f21fa07a770634a0da001/image.png)
		
**示例代码：**
    ![](//mccdn.qcloud.com/static/img/4070db894c4d9bc99b6ff3e0763adfde/image.png)
## 四. 房间成员
首先通过AVContext的实例的room属性获取房间并强制转换为AVMultiRoom，并用它的getEndpointCount和getEndPointbyId的方法获取当前所有房间成员对象。
			
**接口描述：**
		![](//mccdn.qcloud.com/static/img/cac69699ca13610d8190278bee335a8f/image.png)
		
**示例代码**：
    ![](//mccdn.qcloud.com/static/img/2ffa7d872ea9a7011f14c9debc520bd5/image.png)
## 五. 成员的权限
上文中已经对房间成员的权限进行了说明，对于权限的管理，除了对进入房间的EnterRoomParam中的authBit或authBuffer进行配置之外，还可以动态修改房间中成员的权限，所有权限的定义在QAVCommon.h中。
假如要改变个人的权限，则可以通过以下步骤改变：
(1)通过调用ChangeAuthority()方法改变房间成员权限的方法，第一个参数可以传入明文权限位，第二个参数传入权限位加密串，如果只填一个，则以其为准，两者都填则以密文为准。明文权限位类型在2.1中有详细描述，权限位加密串由腾讯云提供。
(2)修改权限操作的结果通过ChangeAuthorityCallback回调返回。

**接口描述：**
    ![](//mccdn.qcloud.com/static/img/b025bf0b6c79b0306394014a7beafe6b/image.png)
		
**示例代码：**
    ![](//mccdn.qcloud.com/static/img/59742460d425b1976c532f7c54ce4287/image.png)
