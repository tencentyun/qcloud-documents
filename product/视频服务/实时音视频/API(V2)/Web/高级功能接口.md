高级开发人员可以通过以下高级功能接口和高级事件通知进行开发。详细接口描述如下：


## WebRTCAPI.updateStream
>?2.5.3以上版本开始支持

停止推流

| 参数                   | 类型       | 描述            |
| -------------------- | -------- | ------------- | 
| opt         | object | 参数      |
| succ         | function | 成功回调      |
| fail         | function | 失败回调      |

##### opt

| 参数                   | 类型       | 描述            |
| -------------------- | -------- | ------------- |
| stream         | MediaStream | 预留字段,传空对象      |
| role         | string | 非必须，更新流如果需要更新画面角色设置，需要带上此参数      |


#### 语法示例
```javascript
    var RTC = new WebRTCAPI({ ... });
    ...
    RTC.updateStream({
        role: "user",
        stream: stream
    }, function(){
        console.debug('updateStream succ')
    }, function(){
        console.debug('updateStream failed')
    });

```


## WebRTCAPI.closeAudio
不采集音频（静音）。
#### 语法示例
```javascript
    var RTC = new WebRTCAPI({ ... });
    ...

    RTC.closeAudio();
```

## WebRTCAPI.openAudio
采集音频标识（取消静音）。
#### 语法示例
```javascript
    var RTC = new WebRTCAPI({ ... });
    ...

    RTC.openAudio();
```

## WebRTCAPI.closeVideo
不采集视频。
#### 语法示例
```javascript
    var RTC = new WebRTCAPI({ ... });
    ...

    RTC.closeVideo();
```

## WebRTCAPI.openVideo
打开视频采集。
> 这里的openVideo是在已经进行音视频推流的时候，关闭了视频的情况下再打开采集。


#### 语法示例
```javascript
    var RTC = new WebRTCAPI({ ... });
    ...

    RTC.openVideo();
```

## WebRTCAPI.getLocalMediaStatus
获取当前视频采集配置。
#### 语法示例
```javascript
    var RTC = new WebRTCAPI({ ... });
    ...
    var status = RTC.getLocalMediaStatus();
```

## WebRTCAPI.changeSpearRole
切换画面设定的用户角色。
#### 语法示例
```javascript
    var RTC = new WebRTCAPI({ ... });
    ...
    RTC.changeSpearRole( "role_name" );
```

## WebRTCAPI.getVideoDevices
枚举摄像头。
#### 语法示例
```javascript
    var RTC = new WebRTCAPI({ ... });
    ...
    RTC.getVideoDevices( function(devices){
        //devices 是枚举当前设备的视频输入设备的数组(DeviceObject)
        // 例如 ：[device,device,device]
        // 这些device将在选择摄像头的时候使用
    })
```

## WebRTCAPI.chooseVideoDevice
选择摄像头。
#### 语法示例
```javascript
    var RTC = new WebRTCAPI({ ... });
    ...
    RTC.chooseVideoDevice( device );

```

## WebRTCAPI.getAudioDevices
枚举麦克风。
#### 语法示例
```javascript
    var RTC = new WebRTCAPI({ ... });
    ...
    RTC.getAudioDevices( function(devices){
        //devices 是枚举当前设备的音频输入设备的数组(DeviceObject)
        // 例如 ：[device,device,device]
        // 这些device将在选择麦克风的时候使用
    })
```

## WebRTCAPI.chooseAudioDevice
选择麦克风。
#### 语法示例
```javascript
    var RTC = new WebRTCAPI({ ... });
    ...
    RTC.chooseAudioDevice( device );

```


## WebRTCAPI.getSpeakerDevices

> 2.6 以上版本开始支持

枚举音频输出设备
#### 语法示例
```javascript
    var RTC = new WebRTCAPI({ ... });
    ...
    RTC.getSpeakerDevices( function(devices){
        // devices 是枚举当前设备的音频输出设备的数组(DeviceObject)
        // 例如 ：[device,device,device]
        //这些 device 将在选择音频输出设备的时候使用
    })
```

## WebRTCAPI.chooseSpeakerDevice

> 2.6 以上版本开始支持


| 参数                   | 类型       | 描述            |
| -------------------- | -------- | ------------- | 
| media         | HTMLMediaElement | Audio / Video      |
| device         | DeviceElement | Audio / Video      |
| succ         | function | 成功回调      |
| fail         | function | 失败回调      |

选择音频输出设备
#### 语法示例
```javascript
    var RTC = new WebRTCAPI({ ... });
    ...
    var speakerList = [];
    RTC.getSpeakerDevices( function(devices){
        speakerList = devices;
    })
    ....
    document.querySelectorAll("video").forEach( function(video){
        //把当前页面的video的输出设备都设置一遍
    	RTC.chooseSpeakerDevice( video, speakerList[1],function(){
            console.debug('change speaker succ ')
    	} ,function(error){
            console.error('change speaker error ', error)
    	} );
    });

```


## WebRTCAPI.getStats
获取统计数据 & 停止获取接口


| 参数                   | 类型       |是否必填       |  描述            |
| -------------------- | -------- | ------------- | ---- |
| opt         | object |  是     | -     |
| succ         | function |  是     |成功回调      |
| fail         | function |  否     |失败回调      |

#### opt参数 详解

| 参数                   | 类型       | 是否必填       | 描述            |
| -------------------- | -------- | ------------- | ---- |
| userId         | String | 否       |  需要获取的音视频流的统计数据的用户 ID ，为空则表示获取自己的统计数据 |
| interval         | integer | 否       | 定时器，单位毫秒，表示获取统计数据的时间间隔，不填则表示不定时获取。|


#### result 详解
```javascript
    //发送流
    {
        video:{
            ssrc        : "", //数据源id
            codec       : "", //编码协议
            packetsSent : "", //视频包发送数
            packetsLost : "", //视频包丢失数
            width       : "", //视频分辨率-宽
            height      : "", //视频分辨率-高
        }
        audio:{
            ssrc        : "", //数据源 ID
            codec       : "", //编码协议
            packetsSent : "", //音频包发送数
        }
    }

    //接收流
    {
        video:{
            ssrc            : "", //数据源 ID
            codec           : "", //编码协议
            packetsReceived : "", //视频包接收数
            packetsLost     : "", //视频包丢失数
            width           : "", //视频分辨率-宽
            height          : "", //视频分辨率-高
        }
        audio:{
            ssrc            : "", //数据源 ID
            codec           : "", //编码协议
            packetsReceived : "", //音频包接收数
            packetsLost     : "", //音频包丢失数
        }
    }


```

#### 语法示例

```javascript
    var RTC = new WebRTCAPI({ ... });
    ...
    RTC.getStats( {
        interval:2000 //每2秒获取一次
    },function( result ){
        console.debug( result );
        // test code
        setTimeout( function(){
            //不再采集统计数据
            result.nomore();
        },20000);
    } ,function( error ){
        console.error( error );
    } );

```


## WebRTCAPI.SoundMeter
声音音量检测
#### 语法示例

>?2.5.3以上版本支持

#### 语法示例
```javascript
    var soundMeter = WebRTCAPI.SoundMeter( opts )
```

#### opts

| 参数                   | 类型       | 是否必须       | 描述            |
| -------------------- | -------- | ------------- |  ------------- |
| stream         | object |是 | MediaStream     |
| onprocess         | function |是 | 音频流监控回调      |

#### onprocess 的回调参数

| 参数                   | 类型       | 描述            |
| -------------------- | -------- | ------------- |
| volume         | String | 音量大小(例如0.02 )     |
| status         | function | volume >= 0.01 ? "speaking" : "silence"      |
| event         | AudioProcessingEventObject |-   |


>?有声音和没有声音的判断标准是 volumn 的值。 >= 0.01 则认为有声音， < 0.01 则认为静音。


```javascript
    // 分析音频流
    var meter = WebRTCAPI.SoundMeter({
        stream: info.stream,
        onprocess: function( data ){
            $("#volume").val( data.volume)
            $("#volume_str").text( "volume: "+ data.volume)
            $("#status").text( data.status )
        }
    })

    // 停止分析音频流
    meter.stop();

```
