## 互动直播录制开发
录制的文件将存储在腾讯云提供的点播服务上，用户可通过点播的管理控制台、API进行管理、转码、分发等操作。<br/><br/>
**使用录制功能前，请先在控制台开通腾讯云点播服务，否则将无法使用**。

### 1 客户端SDK接口
#### Android
##### 开始录制
######1. 设置录制参数

```
ILiveRecordOption option = new ILiveRecordOption();
option.fileName(filename);
option.addTag(tag);
option.classId(Integer.parseInt(classId))
    .transCode(trancodeCheckBox.isChecked())
    .screenShot(screenshotCheckBox.isChecked())
    .waterMark(watermarkCheckBox.isChecked());
```

* 录制参数：ILiveRecordOption

字段名|字段类型|默认值|说明
:--:|:--:|:--:|:--:
fileName|String|必填| 录制生成的文件名
classId|int|必填|视频分类ID
transCode|boolean|NO|是否转码
screenShot|boolean|NO|是否截图
waterMark|boolean|NO|是否打水印
sdkType|TIMAvManager.SDKType|必填|SDK对应的业务类型
recordType|AVRecordType|AV_RECORD_TYPE_VIDEO|录制类型

方法名|参数|说明
:--:|:--:|:--:
addTag|String|添加视频标签

######2. 开始录制

```
ILiveRoomManager.getInstance().startRecordVideo(option, new ILiveCallBack() {
        @Override
        public void onSuccess(Object data) {
            //开始录制成功
        }

        @Override
        public void onError(String module, int errCode, String errMsg) {
            //开始录制失败
        }
    });
```

##### 结束录制

```
ILiveRoomManager.getInstance().stopRecordVideo(new ILiveCallBack<List<String>>() {
        @Override
        public void onSuccess(List<String> data) {
            //停止录制成功
            for (String url : data){
                //文件id
            }
        }

        @Override
        public void onError(String module, int errCode, String errMsg) {
            //停止录制失败
        }
    });
```

Android录制功能的详细实现见[新随心播](https://github.com/zhaoyang21cn/ILiveSDK_Android_Demos)

#### ios
##### 开始录制
######1. 设置录制参数

```
ILiveRecordOption *option = [[ILiveRecordOption alloc] init];
option.fileName = @"新随心播录制文件";
option.tags = tags;
option.classId = [tag intValue];
option.isTransCode = NO;
option.isScreenShot = NO;
option.isWaterMark = NO;
option.isScreenShot = NO;
option.avSdkType = sdkType;
option.recordType = recordType;
```

* 录制参数：ILiveRecordOption

字段名|字段类型|默认值|说明
:--:|:--:|:--:|:--:
fileName|NSString|必填| 录制生成的文件名
tags|NSArray|必填|视频标签列表
classId|UInt32|必填|视频分类ID
isTransCode|BOOL|NO|是否转码
isScreenShot|BOOL|NO|是否截图
isWaterMark|BOOL|NO|是否打水印
sdkType|AVSDKType|必填|SDK对应的业务类型
recordType|AVRecordType|AV_RECORD_TYPE_VIDEO|录制类型

######2. 开始录制

```
[[ILiveRoomManager getInstance] startRecordVideo:option succ:^{
        NSLog(@"已开始录制");
    } failed:^(NSString *module, int errId, NSString *errMsg) {
        NSLog(@"开始录制失败");
    }];
```

##### 结束录制

```
[[ILiveRoomManager getInstance] stopRecordVideo:^(id selfPtr) {
            NSArray *fileIds = (NSArray *)selfPtr;
            NSLog(@"已停止录制");
        } failed:^(NSString *module, int errId, NSString *errMsg) {
            NSLog(@"停止录制失败");
        }];
```

* 回调结果：NSArray（返回NSString类型的文件Id列表）

IOS录制功能的详细实现见[新随心播](https://github.com/zhaoyang21cn/ILiveSDK_iOS_Demos)

### 2 视频管理

通过音视频通信SDK录制的视频将存储在点播服务中

1. 用户访问点播的[管理控制台](http://console.qcloud.com/video)可以对录制的文件进行相应的管理操作<br/>
2. 用户也可以通过点播提供的API进行管理操作，[API手册](https://www.qcloud.com/doc/api/257/API%E6%A6%82%E8%A7%88)<br/>
3. DescribeVodPlayInfo能根据文件名（开始录制Api中，录制参数所填文件名）获取到录制
文件下载地址。详见[参考文档](https://www.qcloud.com/doc/api/257/%E8%8E%B7%E5%8F%96%E8%A7%86%E9%A2%91%E6%92%AD%E6%94%BE%E4%BF%A1%E6%81%AF%E5%88%97%E8%A1%A8)

### 3 价格和计费说明

录制功能本身是不收费的，但由于使用的是点播服务的能力，在云点播中会产生存储、流量的费用。[计费规则](https://www.qcloud.com/doc/product/268/5129#2..E5.BD.95.E5.88.B6.E7.9B.B8.E5.85.B3.E8.AE.A1.E8.B4.B9)：


需要说明的是，如果你已开通点播服务，并选定套餐或后付费中的一种计费模式，将沿用你已选定的计费模式，如果你未开通点播服务，将默认选择后付费按流量的计费模式。

### 4 注意事项

1. 双人音视频房间不支持录制功能
2. 录制文件格式默认为MP4
3. 录制每隔90分钟或录制结束时不足90分钟会生成一个MP4录制文件，超过90分钟则会生成多个文件
4. APP运行过程中crash或异常退出，1分钟没收到数据会自动关闭录制，后端会录制用户异常退出前音视频
5. 现版本不支持多路上行视频合并和混音处理

### 5 错误码


| 错误码| 错误说明| 处理建议|
|---------|---------|---------|
|1|用户没有录制权限||
|2|用户点播余额不足||
|30000000|SDK请求解析失败|【录制请求字段填写是否完整】|
|30000001|SDK请求解析失败-没有录制请求包体|【录制请求字段填写是否完整】
|30000002|SDK请求解析失败-没有录制文件名字段|【录制请求字段填写是否完整】
|30000003|SDK请求解析失败-没有录制请求操作字段|【录制请求字段填写是否完整】
|30000004|SDK请求解析失败-视频源类型错误（摄像头/桌面等）|【录制请求字段填写是否完整】
|30000201|请求服务器内部数据打包错误|【反馈腾讯客服】
|30000202|请求服务器内部数据打包错误|【反馈腾讯客服】
|30000203|请求服务器内部数据打包错误|【反馈腾讯客服】
|30000207|请求录制服务器通讯错误-拉取录制服务器地址失败|【反馈腾讯客服】
|30000208|请求录制服务器通讯错误-请求录制服务器超时|【可能是网络问题，重试处理，重试失败反馈腾讯客服】
|30000301|解析录制服务器回包错误-数据包解析失败|【反馈腾讯客服】
|30000302|解析录制服务器回包错误-数据包解析失败|【反馈腾讯客服】
|30000303|解析录制服务器回包错误-没有返回IP|【反馈腾讯客服】
|30000304|解析录制服务器回包错误-没有返回端口|【反馈腾讯客服】
|30000305|解析录制服务器回包错误-没有返回结果|【反馈腾讯客服】
|30000401|查询房间获取grocery服务IP错误|【可能是网络问题，重试处理，重试失败反馈腾讯客服】
|30000402|查询房间拉取grocery数据错误|【可能是网络问题，重试处理，重试失败反馈腾讯客服】
|30000403|查询房间拉取grocery不存在（房间不存在）|【检查是否成功开房，录制的用户ID，groupid是否填写正确】
|30000404|查询房间流控服务器超时|【可能是网络问题，重试处理，重试失败反馈腾讯客服】
|30000405|查询房间回包错误-数据包解析失败|【反馈腾讯客服】
|30000406|查询房间回包错误-数据包解析失败|【反馈腾讯客服】
|30000407|查询房间回包错误-数据包解析失败|【反馈腾讯客服】
|30000408|查询房间回包错误-没有返回结果|【反馈腾讯客服】
|30000409|查询房间回包错误-数据包解析失败|【反馈腾讯客服】
|30000410|录制的房间不存在|【检查是否成功开房，录制的用户ID，groupid是否填写正确,或者用户是否已经退出房间】
|30000411|录制的房间不存在，或发起录制的用户不存在|【检查是否成功开房，录制的用户ID，groupid是否填写正确,或者用户是否已经退出房间】
|30000412|停止录制重复发送，用户已经停止录制	|【如果是录制停止操作说明已经停止，检查是否多次发送停止操作，无需处理】
|30000413|停止录制重复发送，用户已经停止录制	|【如果是录制停止操作说明已经停止，检查是否多次发送停止操作，无需处理】
|30000414|查询房间-服务器内部操作类型错误|【反馈腾讯客服】
|30000415|启动录制重复发送，用户正在录制；或者发起录制的用户不存在|【检查是否成功开房，录制的用户ID，groupid是否填写正确】


