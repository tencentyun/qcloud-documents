## 一. 音视频房间介绍
  定义：房间指的是用户进入了一个封闭空间，进入了这个封闭空间的成员就可以进行语音交流，视频交流。每个音视频房间都有一个房间号（roomID），处于不同房间号的成员互不影响。房间类为音视频房间的成员提供了很多获取房间和房间成员信息的方法。

## 二. 进房和退房
### 1.进入房间
进入房间（假如该房间没有成员则为创建房间）操作含有以下四个步骤：

- 1 在进入房间页面的.h文件里加入房间委托协议QAVRoomDelegate。

- 2 通过配置QAVMultiParam来设置房间号和音视频场景策略（如主播场景）等参数，来达到最好的音视频效果。

- 3 在进入房间页面的.m文件根据配置的参数进入房间并把delegate设置为self。

- 4 进入房间的是否成功，会回调回以下方法中，因此要在.m里实现协议中的方法:


```
-(void)OnEnterRoomComplete:(int)result;      

```

接口描述：

```
-(QAVResult)enterRoom:(QAVRoomParam*)param delegate:(id<QAVRoomDelegate>)dlg;

```
 示例代码：
 

```
    QAVMultiParam *info = [[QAVMultiParam alloc]init];
    info.roomID = 201678;  
    info.authBitMap = QAV_AUTH_BITS_DEFAULT;          //拥有所有的音视频权限

    QAVResult temp = [[AVUtil sharedContext] enterRoom:info delegate:self];
```


```
-(void)OnEnterRoomComplete:(int)result
{
    if(result)
    {
        NSLog(@"进入房间成功");
    }
}

```

### 2.退出房间 
退出房间的用法与进入房间的用法相同，接口描述：

```
-(QAVResult)exitRoom;
```

退出房间是否成功的异步回调 ：


```
-(void)OnExitRoomComplete:(int)result;

```
 示例代码：
 

```
[[AVUtil sharedContext]exitRoom];

```

```
-(void)OnExitRoomComplete:(int)result
{
    if(result)
    {
        NSLog(@"退出房间成功");
    }
}
```

## 三. 房间的监听回调 
除了进入房间和退出房间的回调，房间委托协议QAVRoomDelegate中还定义了3个通知回调接口：

### 1.房间成员状态更新通知

用户在进入房间后，每次成员更新（有人加入房间或者退出房间）或者房间里的某个用户的视频状态的改变（某一个人开启摄像头或者关闭摄像头），都会回调通知到这个方法（前提是这个类使用房间委托协议QAVRoomDelegate）：

接口描述：

```
-(void)OnEndpointsUpdateInfo:(QAVUpdateEvent)eventID endpointlist:(NSArray*)endpoints;

```

 示例代码：
 

```

- (void)OnEndpointsUpdateInfo:(QAVUpdateEvent)eventID endpointlist:(NSArray *)endpoints
{
    for(int i = 0; i < [endpoints count]; i++)
    {
        //获取房间内的用户信息
        QAVEndpoint *endpoint = [endpoints objectAtIndex:i];
        NSLog(@"%d %@ 是否开启摄像头:%@",i,endpoint.identifier,endpoint.isCameraVideo?@"YES":@"No");
    }
}

```
### 2.房间成员非法操作通知

房间里不同角色拥有不同权限。例如，在直播中，主播应该获得发送语音和视频等大部分权限，而普通观众则应该被授权接收语音和视频等权限，但一般不具备发送语音和视频的权限。如果不具备某项权限的成员进行相应操作，SDK回回调此通知。房间成员的权限通过进入房间时上带的配置参数EnterRoomParam中的authBit和authBuffer字段来指定。

接口描述：

```
@param privilege 当前SDK侧所记录的该房间成员的通话能力权限值
-(void)OnPrivilegeDiffNotify:(int)privilege;
```

 示例代码：
 

```
- (void)OnPrivilegeDiffNotify:(int)privilege
{
    NSLog(@"illegal operation!Your privilege is %d",privilege);
}
```
### 3.半自动接收房间视频的成员列表通知

进入房间上带的参数EnterRoomParam中有对接受视频方式进行配置的字段，当指定为自动接收视频时，成员进入房间后无需主动申请，可以自动接收房间中已经有数据上行的摄像头视频，屏幕分享除外，但是进入房间之后，若又有新增的上行摄像头视频，仍然需要手动申请并通过调用requestview()方法获取。SDK会通过回调OnSemiAutoRecvCameraVideo()来通知App房间里拥有上行数据的成员列表，以便App进行渲染设置。

接口描述：

```
@param identifierList 自动接收的摄像头视频所对应的成员id列表
-(void)OnSemiAutoRecvCameraVideo:(NSArray*)identifierList;
```
 示例代码：

```
- (void)OnSemiAutoRecvCameraVideo:(NSArray*)identifyList
{

    if(identifierList != NULL && [identifierList count] > 0)
    {
       for(NSString* identifier in identifierList)
       {
          NSLog(@"%@ has video upload",identifier);
       }
    }
}
```
## 四. 房间成员
首先通过QAVContext的实例的room属性获取房间并强制转换为QAVMultiRoom，并用它的GetEndPointList的方法获取所有房间成员对象。

接口描述：

```
-(NSArray*)GetEndpointList; 
```
示例代码：

```
QAVMultiRoom *multiRoom = (QAVMultiRoom *)[AVUtil sharedContext].room;
NSArray *endpointArray = [NSArray arrayWithArray:[multiRoom GetEndpointList]];
//     对用户数组endpointArray进行操作
```

## 五. 成员的权限
房间里不同的角色拥有不同的权限。例如，在直播中，主播应该获得发送语音，发送视频等大部分权限。而作为普通观众，则应该被授予接受语音，接受视频这些权限，但是不具备发送语音和视频这样的权限。

所有权限的定义在QAVCommon.h中：

```
QAV_AUTH_BITS_DEFAULT          // 缺省值。拥有所有权限。
QAV_AUTH_BITS_OPEN             // 权限全开
QAV_AUTH_BITS_CLOSE            // 权限全关
QAV_AUTH_BITS_CREATE_ROOM      // 创建房间权限。
QAV_AUTH_BITS_JOIN_ROOM        // 加入房间的权限。
QAV_AUTH_BITS_SEND_AUDIO       // 发送语音的权限。
QAV_AUTH_BITS_RECV_AUDIO       // 接收语音的权限。
QAV_AUTH_BITS_SEND_VIDEO       // 发送视频的权限。
QAV_AUTH_BITS_RECV_VIDEO       // 接收视频的权限。
QAV_AUTH_BITS_SEND_SUB         // 发送辅路视频的权限。
QAV_AUTH_BITS_RECV_SUB         // 接收辅路视频的权限。
```

假如要改变个人的权限，则可以通过以下步骤改变：

1. 在相应的ViewController.h文件里加入权限更改协议QAVChangeDelegate。

2. 通过调用改变个人权限的方法，第一个参数传入新赋予的权限，第二个参数传空，改变的结果通过回调函数返回，接口声明如下：

```
-(QAVResult)ChangeAuthoritybyBit:(uint64)auth_Bit orstring:(NSData *)buff delegate:(id<QAVChangeDelegate>)dlg;
```
 示例代码如下：

```
//赋予创建房间和进入房间的权限
authBitMap = QAV_AUTH_BITS_CREATE_ROOM | QAV_AUTH_BITS_JOIN_ROOM;   
QAVMultiRoom*multiRoom = (QAVMultiRoom*)[AVUtil sharedContext].room;
[multiRoom ChangeAuthoritybyBit: authBitMap orstring:nil delegate:self];
```
3.改变权限是否成功，会回调回以下方法中，因此要在相应的ViewController.m文件里实现协议中的方法:

```
-(void)OnChangeAuthority:(int)ret{
    if (ret == QAV_OK)
{
      //修改权限成功
}
}

```