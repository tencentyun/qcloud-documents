## Role

## What is a Role
The Role introduced in ILVB is used to configure different parameters in a single platform. It is considered as a configuration set for a terminal to join a room.

### How to Configure Roles
Users can configure roles at Tencent Cloud backend.
![](https://zhaoyang21cn.github.io/iLiveSDK_Help/readme_img/role_config.png)

### How to Customize Roles
Users can customize their own roles based on their needs.
![](https://zhaoyang21cn.github.io/iLiveSDK_Help/readme_img/role_detail.png)

### How to Use Roles
Users can configure roles to be used in the option when they join a room.

Android:
```
ILVLiveRoomOption hostOption = new ILVLiveRoomOption(hostId)
                .controlRole("LiveMaster");     // Use the LiveMaster role
```

iOS
```
//TILLiveSDK(LVB SDK)
TILLiveRoomOption *hostOption = [TILLiveRoomOption defaultHostLiveOption];
hostOption.controlRole = @"LiveMaster";   // Use the LiveMaster role
```
    
```
//TILCallSDK(Call SDK)
TILCallSponsorConfig *sponsorConfig = [[TILCallSponsorConfig alloc] init];
sponsorConfig.controlRole = @"LiveMaster";   // Use the LiveMaster role
```

MacOS
```
ILiveRoomOption *option = [ILiveRoomOption defaultHostLiveOption];
option.controlRole = @"LiveMaster";//Role strings are from the spear configuration of Tencent Cloud console
[[ILiveRoomManager getInstance] createRoom:(int)_item.info.roomnum option:option succ:^{
    NSLog(@"create room succ");
} failed:^(NSString *module, int errId, NSString *errMsg) {
    NSLog(@"createRoom fail,module=%@,code=%d,msg=%@",module,errId,errMsg);
}];
```

PC
```c++
iLiveRoomOption roomOption;
roomOption.controlRole = "LiveMaster"; // Use the LiveMaster role
```

IE
```js
sdk.createRoom(roomid, "LiveMaster", // Use the LiveMaster role
    function () {
    }, function (errMsg) {
    }, false);
```

### How to Change Roles
After joining a room, users can still adjust their roles according to their needs.

Android:
```
// Change the role to LiveGuest
ILiveRoomManager.getInstance().changeRole("LiveGuest", new ILiveCallBack() {
    @Override
    public void onSuccess(Object data) {
        //...
    }

    @Override
    public void onError(String module, int errCode, String errMsg) {
        //...
    }
});
```


IOS:
```
// Change the role to LiveGuest
ILiveRoomManager *manager = [ILiveRoomManager getInstance];
[manager changeRole:@"LiveGuest" succ:^ {
    NSLog(@"Role changed successfully");
} failed:^(NSString *module, int errId, NSString *errMsg) {
    NSLog(@"Failed to change the role");
}];
```

MacOS
```
// Change the role to LiveGuest
NSString *role = @"LiveGuest";
[[ILiveRoomAVManager getInstance] changeRole:role succ:^{
    NSLog(@"change role succ");
} failed:^(NSString *module, int errId, NSString *errMsg) {
    NSLog(@"change role fail");
}];
```

PC
```c++
// Change the role to LiveGuest
void Live::OnChangeRoleSuc( void* data )
{
//Role changed successfully
}

void Live::OnChangeRoleErr( int code, const char *desc, void* data )
{
//Failed to change the role
}
GetILive()->changeRole("LiveGuest", OnChangeRoleSuc, OnChangeRoleErr, NULL);
```

IE
```js
// Change the role to LiveGuest
sdk.changeRole("LiveGuest", function() {
//Role changed successfully
},
function(err){
//Failed to change the role
}
);
```

### Advanced Application of Roles
Dynamically adjust the current video quality based on the network status:

Users can configure multiple roles (HD, SD, and fluent) for VJ and viewers on Tencent Cloud. Users can detect the current network status and dynamically adjust the roles used for now to modify the video quality in a dynamic manner.

*For more information, please see [FreeShow](https://github.com/zhaoyang21cn/iLiveSDK_Android_Suixinbo)*

