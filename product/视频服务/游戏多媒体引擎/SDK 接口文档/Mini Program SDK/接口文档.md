## 操作场景
本文档指导您如何使用小程序SDK接口实现小程序开发者调试和接入腾讯云游戏多媒体引擎产品 API。


## 前提条件
已在腾讯云后台中申请 GME 相关服务，详细信息请参考 [SDK 接入指引](https://cloud.tencent.com/document/product/607/10782)。


## 操作步骤
### 申请云直播服务
>!申请云直播服务之前需要进行实名验证。在【账号信息】中申请实名认证。

1. 登录腾讯云控制台，选择【云直播】服务，进入 [云直播服务申请界面](https://console.cloud.tencent.com/live)。
2. 勾选【同意《腾讯云服务协议》】，并单击【申请开通】进行云直播服务开通。
3. 单击【确认】，云直播服务已申请成功。如下图所示：
![](https://main.qcloudimg.com/raw/53d626f2dea1eaecf459636db1481e4b.png)
4. 服务申请成功后，单击左侧菜单栏【域名管理】，进入域名管理界面。
5. 云直播服务会自动生成一个推流域名，单击【添加域名】，申请播放域名。
 >!请添加自有已备案域名进行直播推流和播放。域名管理使用方法参见 [域名管理](https://cloud.tencent.com/document/product/267/30559) 和 [CNAME配置](https://cloud.tencent.com/document/product/267/30010)。 

![](https://main.qcloudimg.com/raw/d24740621f990a6101ee031de1a78cc4.png)

申请播放地址成功后，界面会有两个域名，一个是推流域名，一个是播放域名。
![](https://main.qcloudimg.com/raw/df0850145ad53d12285e8e1b8f29cec5.png)


### rtmp 流地址生成
rtmp 流支持两种模式。
- 拉取房间内某个说话成员的 rtmp 流。模式一只能听到指定成员的说话声音。
- 拉取房间内所有说话成员合成的 rtmp 流。模式二可以听到所有成员的声音。

rtmp 流地址生成需要以下几个信息：

|参数|含义|获取方式|
|-----|-----|-----|
|AppID|GME 控制台所申请到的 AppID。 |腾讯云控制台，请参考  [SDK 接入指引](https://cloud.tencent.com/document/product/607/10782)。|
|RoomID|此用户需要收听的房间号 ID。 |此参数由开发者在应用中生成。|
|UserID|此用户需要收听的另一用户的 ID |此参数由开发者在应用中生成。|
|BizID|云直播服务控制台生成的标识码 |此参数获取方式见下文 [步骤1](#step1)。|
|StreamKey|云直播服务控制台生成的密钥|此参数获取方式见下文 [步骤1](#step1)。|
|StreamID|rtmp 流的一个唯一标识|此参数获取方式见下文 [步骤2](#step2)。|
|Timestamp|时间戳，单位为秒 |此参数由开发者在应用生成并填入。|


rtmp 流地址生成有以下几个步骤：
<span id="step1"></span>
#### 获取 BizID 和 StreamKey
1. 进入域名管理界面，在播放域名一栏，单击【管理】，进入播放域名管理界面。
 ![](https://main.qcloudimg.com/raw/df0850145ad53d12285e8e1b8f29cec5.png)
2. CNAME 一栏中，在 “.liveplay.myqcloud.com” 后缀前面的播放域名为 BizID 参数。例如下图中的 BizID 即为 38251。 API Key 为 StreamKey 参数。
 ![](https://main.qcloudimg.com/raw/6a0a8c119acd2d49b575a40aa7ededcc.png)

<span id="step2"></span>
#### 生成 StreamID

模式一：
```
{AppID}_{UserID}_{RoomID}_main
```
模式二：
```
mixer_{AppID}_{RoomID}
```

#### 生成最终地址
```
rtmp://{BizID}.liveplay.myqcloud.com/live/MD5({StreamID})?txSecret= MD5({StreamKey}{streamidMd5}{timestamp})&txTime={timestamp}
```

>!其中 MD5()；为计算 MD5 的函数。



示例所需要的信息为：

```
Bizid:38251
streamKey:4531cddc5bd6dc28a812bb87121a5853
AppID:1400089356
RoomID:20180301
Userid:123456
timestamp:1551438840
```

rtmp 地址如下：

```
模式一：
rtmp://38251.liveplay.myqcloud.com/live/38251_5a1d7c2f7e8fcb56942691035b49d960?txSecret=09fcc68fc320336c2b85071b11056bd6&txTime=5c7913f8

模式二：
rtmp://38251.liveplay.myqcloud.com/live/38251_fed2b77fb622dcbf978ed6041d9f52d9?txSecret=2d69cfbd346da4531d82624a0bed9368&txTime=5c7913f8
```










