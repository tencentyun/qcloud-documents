腾讯实时音视频（Tencent Real-Time Communication，TRTC）将腾讯21年来在网络与音视频技术上的深度积累，以多人音视频通话和低延时互动直播两大场景化方案，通过腾讯云服务向开发者开放，致力于帮助开发者快速搭建低成本、低延时、高品质的音视频互动解决方案。

下表为云审计支持的实时音视频操作列表：

| 操作名称                         | 资源类型 | 事件名称                          |
|------------------------------|------|-------------------------------|
| 修改权限密钥状态                     | trtc | ChangeSecretKeyFlag           |
| trtcCreateMixConf            | trtc | CreateMixConf                 |
| 创建新版密钥                       | trtc | CreateSecret                  |
| 使用密钥生成签名                     | trtc | CreateSecretUserSig           |
| 增加 spear 配置                    | trtc | CreateSpearConf               |
| 创建异常信息                       | trtc | CreateTroubleInfo             |
| 注册一个实时音视频应用                  | trtc | CreateTrtcApp                 |
| 上传水印图片                       | trtc | CreateWatermark               |
| 删除 Spear 配置                    | trtc | DeleteSpearConf               |
| 删除水印图片                       | trtc | DeleteWatermark               |
| 查询异常体验事件                     | trtc | DescribeAbnormalEvent         |
| 获取用户名下的应用列表                  | trtc | DescribeAppStatList           |
| 获取时长套餐包列表                    | trtc | DescribeDurationPackages      |
| 查询历史房间和用户数                   | trtc | DescribeHistoryScale          |
| trtcDescribeLiveList         | trtc | DescribeLiveList              |
| trtcDescribeMixConf          | trtc | DescribeMixConf               |
| 批量获取应用的混流配置                  | trtc | DescribeMixConfs              |
| 查询实时网络状态                     | trtc | DescribeRealtimeNetwork       |
| 查询实时质量数据                     | trtc | DescribeRealtimeQuality       |
| 查询实时规模                       | trtc | DescribeRealtimeScale         |
| 查询房间列表                       | trtc | DescribeRoomInformation       |
| trtcDescribeRoomList         | trtc | DescribeRoomList              |
| 获取一个 SkdAppID 的信息              | trtc | DescribeSdkAppInfo            |
| 获取密钥                         | trtc | DescribeSecret                |
| 获取旧版 Sig                      | trtc | DescribeSig                   |
| 获取 Spear 配置                    | trtc | DescribeSpearConf             |
| 获取应用和账户信息                    | trtc | DescribeTrtcAppAndAccountInfo |
| trtcDescribeTrtcSdkAppIdList | trtc | DescribeTrtcSdkAppIdList      |
| 获取 Trtc 的时长统计数据                | trtc | DescribeTrtcStatistic         |
| 查询用户在房间中的状态                  | trtc | DescribeUserState             |
| 查询用户在房间中的状态                  | trtc | DescribeUserStateByStrRoomId  |
| 查找水印图片                       | trtc | DescribeWatermark             |
| 解散房间                         | trtc | DismissRoom                   |
| 解散房间                         | trtc | DismissRoomByStrRoomId        |
| 解散房间                         | trtc | DissolveRoom                  |
| 解散房间                         | trtc | DissolveRoomByStrRoomId       |
| 获取通话状态                       | trtc | GetCommState                  |
| 查询ES数据                       | trtc | GetElasticSearchData          |
| 获取房间列表                       | trtc | GetRoomList                   |
| 获取用户信息                       | trtc | GetUserInfo                   |
| 获取用户列表                       | trtc | GetUserList                   |
| 查询应用混流配置，如果不存在会自动创建          | trtc | HardDescribeMixConf           |
| 判断是否可以购买上行时长套餐包              | trtc | IfCanBuyOldPackage            |
| 判断用户是否是 AvSdk 用户               | trtc | IsAvSdkUser                   |
| 判断用户是不是新的 Trtc 用户              | trtc | IsNewTrtcUser                 |
| 判断 uin 是否为 Trtc 用户               | trtc | IsTrtcUser                    |
| 踢人                           | trtc | KickOutUser                   |
| 踢人                           | trtc | KickOutUserByStrRoomId        |
| 修改应用信息                       | trtc | ModifyAppInfo                 |
| 修改混流配置参数                     | trtc | ModifyMixConf                 |
| trtcModifyRecordMode         | trtc | ModifyRecordMode              |
| 修改 Spear 配置                    | trtc | ModifySpearConf               |
| 修改水印图片                       | trtc | ModifyWatermark               |
| 移出用户                         | trtc | RemoveUser                    |
| 移出用户                         | trtc | RemoveUserByStrRoomId         |
| 展示房间列表                       | trtc | ShowRoomList                  |
| 展示用户列表                       | trtc | ShowUserList                  |
| 启动云端混流                       | trtc | StartMCUMixTranscode          |
| 结束云端混流                       | trtc | StopMCUMixTranscode           |
| 切换密钥版本                       | trtc | ToggleSecretVersion           |
| 切换 Spear 场景                    | trtc | ToggleSpearScheme             |
| trtcUpdateNewUserStep        | trtc | UpdateNewUserStep             |
| 签名（UserSig）校验                | trtc | VerifySecretUserSig           |
| 旧版公私钥 Sig 校验                   | trtc | VerifySig                     |
