本章节将指导您如何让直播中不同房间内的主播进行互动，即所说的跨房音视频交流

## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。 
[点击下载]()

## 相关概念
### 跨房音视频交流

iLiveSDK中的每个用户都可以创建自己的直播间，直播间内可以允许多个用户上行音视频数据，同时还允许与其它正在直播中的主播进行互动，这种跨房能力，我们称为跨房音视频交流。

### 跨房密钥

跨房音视频交流需要知道对方所在房间号，对方的用户id，同里还需要以此计算出跨房密钥，作为鉴权。该密钥作为使用跨房音视频交流接口linkRoom的参数。
测试时跨房密钥的生成可参考[跨房秘钥生成](https://gitee.com/vqcloud/doc_demo/blob/master/android/%E9%9F%B3%E9%A2%91%E7%89%B9%E6%95%88.md)

## 具体实现


### 开启直播
创建房间，开启直播可参考[创建房间](创建房间.md)。


### 发起跨房操作
用户在创建房间成功后，调用跨房接口即可，在这之前需先参考上面的说明生成跨房密钥，即下面的sign参数。实际应用中客户端应向自己的业务服务器获取。
```Java
ILiveRoomManager.getInstance().linkRoom(int roomId, String accountId, String sign, ILiveCallBack callBack)
```

### 取消跨房音视频交流
需要取消跨房音视频交流时调用关闭接口即可
```Java
ILiveRoomManager.getInstance().unlinkRoom(ILiveCallBack callback)
```
## API说明

### linkRoom
ILiveRoomManager类封装的跨房音视频交流接口
参数说明

|名称|类型|描述|
|--|--|--|
|roomId|int|需要连接的房间号|
|accountId|String|需要连接房间对应的主播账户|
|sign|String|跨房密钥|
|callback|ILiveCallBack|结果回调|


### unlinkRoom
ILiveRoomManager类封装的取消跨房音视频交流接口
参数说明

|名称|类型|描述|
|--|--|--|
|callback|ILiveCallBack|取消跨房连接的结果回调|

## 联系邮箱
如果对上述文档有不明白的地方，请反馈到trtcfb@qq.com
