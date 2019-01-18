
##  添加游戏好友

```
QQApiAddFriendObject *object = [[QQApiAddFriendObject alloc] initWithOpenID:@"A57597D3BA6F31A0F5D0049A354756FC"];
 object.description = @"一起玩游戏吧";
 object.subID = @"1234";
 object.remark = @"备注这里填写";
 SendMessageToQQReq* req = [SendMessageToQQReq reqWithContent:object];
 QQApiSendResultCode sent = [QQApiInterface sendReq:req];
```

>**注意：**
>APPID 要有添加好友的权限。

## 游戏公会

**错误码定义：**

|GuildErrorCode| 说明| 
|---------|---------|
| GuildErrNone |  |
|GuildErrNet |  网络错误， 请求失败。|
| GuildErrLocalApi |调用本地接口错误， 具体错误码见回调 QQApiSendResultCode。 |
|GuildErrLocalParamsInvalid | 本地参数错误。 |
| GuildErrInvalidLogin | 无效的登录状态。 |
| GuildErrExistBind|已有绑定群，逻辑错误。  |
| GuildErrNonExistBind | 未绑定群，逻辑错误。 |
| GuildErrInvalidGrpOwner | 当前用户不是群主。|
| GuildErrParamsInvalid |参数无效。  |
| GuildErrInvalidRight |  该 APP 无接口调用权限。|
| GuildErrInvalidMember |  不是公会成员。|
| GuildErrOverGrpCout |  达到创建群上限。|
| GuildErrOverCreateGrp | 创建群频率过高。|
| GuildErrGrpDeleted |  群被删除了。|
| GuildErrOther |  其他错误。|

>**注意：**
>下面的 CGI 调用都需要有登录态！

## 绑定公会和 QQ 群

```
TCGuildBindGroupDic *info = [[TCGuildBindGroupDic alloc] init];
info.paramRoleId = @"角色id";
info.paramZoneId = @"分区id";
info.paramGuildId =@"公会id";
info.paramAppKey = @"appkey"; // appkey为申请appid时平台生成的
[_tencentOAuth sendGuildBindGroup:info callback:^(TCGuildRspBindGroupInfo *info) {

}];
```
其中，`_tencentOAuth` 为 `TencentOAuth` 类的实例。

## 查询公会和 QQ 群是否绑定

```
TCGuildQueryBindStateDic *info = [TCGuildQueryBindStateDic dictionary];
info.paramZoneId = @"分区id";
info.paramGuildId = @"公会id";
info.paramRoleId = @"角色id";
[_tencentOAuth sendGuildQueryBindState:info callback:^(TCGuildRspQueryBindStateInfo *info) {
   //处理回调结果
}];
```
其中，`_tencentOAuth` 为 `TencentOAuth` 类的实例。

## 解绑公会(群主校验)

```
TCGuildUnBindDic *info = [TCGuildUnBindDic dictionary];
info.paramZoneId = @"分区id";
info.paramGuildId = @"公会id";
info.paramRoleId = @"角色id";
[_tencentOAuth sendGuildUnbind:info callback:^(TCGuildRspUnBindInfo *info) {
   //处理回调结果
}];
```
其中，`_tencentOAuth` 为 `TencentOAuth` 类的实例。

## 一键加群

```
TCGuildJoinGroupDic *info = [TCGuildJoinGroupDic dictionary];
info.paramZoneId = @"分区id";
info.paramGuildId = @"公会id";
info.paramRoleId = @"角色id";
[_tencentOAuth sendGuildJoinGroup:info callback:^(TCGuildRspJoinGroupInfo *info) {
   //处理回调结果
   if (info.retCode == GuildErrNone) 
           // success
       else {
           if (info.retCode == GuildErrLocalApi) {
               // 处理info.apiSendResultCode
           }
       }
}];
```
其中，`_tencentOAuth` 为 `TencentOAuth` 类的实例。

## 查询用户是否加入公会

```
TCGuildQueryMemberRelationDic *info = [TCGuildQueryMemberRelationDic dictionary];
info.paramZoneId = @"分区id";
info.paramGuildId = @"公会id";
info.paramRoleId = @"角色id";
[_tencentOAuth sendGuildQueryMemberRelation:info callback:^(TCGuildRspQueryMemberRelationInfo *info){

}];
```

其中，`_tencentOAuth` 为 `TencentOAuth` 类的实例。

## 游戏社区
打开兴趣部落:
```
[TencentOAuth launchQQBuluoWithBid:@"15558"];
```
其中，`15558` 为部落 bid，游戏接入方需要自行提供。
