## 1、相关概念说明
- DC（Data Center）：核心机房，用于互动直播业务中需要上行音视频数据或实时交互的用户角色（如主播、讲师、参与实时互动的角色等）接入
- OC（Outer Center）：边缘节点，用于互动直播业务中不需要上行音视频数据、仅观看的用户角色（如普通观众、不需要与老师互动的学生等）接入

二者的计费价格是不同的的，详情请见(https://cloud.tencent.com/doc/product/268/5128#2..E5.9F.BA.E7.A1.80.E7.BD.91.E7.BB.9C.E8.B4.B9.E7.94.A8.E8.AE.A1.E7.AE.97.E5.85.AC.E5.BC.8F)。

## 2、关于DC和OC的分配原则
对于一个App的终端实例来说，什么情况下会接入DC、什么情况下会接入OC呢？分配原则简单来说只有一句话：“有上行音视频数据权限的实例会分配DC、没有上行音视频数据权限的实例分配OC”。具体地，在调用SDK进入房间接口EnterRoom()的时候，其参数EnterRoomParam.auth_bits和
EnterRoomParam.auth_buffer用于设置该实例在房间内的权限，具体权限字段如下图所示：

![用户权限位说明](//mccdn.qcloud.com/img56cdd6a958dff.png)

EnterRoomParam.auth_bits是权限位的明文形式，EnterRoomParam.auth_buffer是权限位的密文形式。可以只使用权限位的明文形式；而一旦申请开启了加密密钥，则权限位密文必填，且后台会校验明文和密文的内容是否对应以及密文的有效期等，业务的逻辑后台也要及时更新App中的密文避免过期。需要注意的是，密文形式由于应用场景过少所有暂时没有开放使用，请尽量使用明文形式。

如果EnterRoomParam.auth_bits/EnterRoomParam.auth_buffer将AUTH_BITS_SEND_AUDIO/AUTH_BITS_SEND_VEDIO/AUTH_BITS_SEND_SUB中的任意一个置为1，则实例会被分配接入DC；反之则该实例被分配接入OC。

PS：后台对单个房间接入DC的用户数量有一个上限保护。例如，如果某个业务设置每个用户都有上行权限，那么后台对于每一个房间前1000个用户分配DC，其他用户分配OC。该限制为后台保护策略，后面可以根据需要进行调整。

## 3、关于DC/OC之间的切换策略
当用户通过进入房间的EnterRoom流程被分配到DC/OC之后，有时也会有需要在DC/OC之间进行切换的需求。例如，教育场景下，一个原本没有上行权限的学生（被分配接入OC）被老师点中回答问题时，需要从不能上行音视频数据OC切换到DC。DC/OC的切换依然是以权限变化为依据的，相对应的接口为tencent::av::AVRoomMuti::ChangeAuthority(string auth_buffer)。其中auth_buffer为权限位的密文形式（暂未启用）。下面将分几种情况来分别讨论：
- 用户位于DC，权限从有到无（将AUTH_BITS_SEND_AUDIO/AUTH_BITS_SEND_VEDIO/AUTH_BITS_SEND_SUB全设置为0）
在此情况下，音视频后台会下发重定向指令，将终端实例重定向到OC。典型的场景是，老师叫一个学生回答问题，回答结束之后取消了该学生上行音视频的权限，学生此时会被重定向到OC（该重定向操作对App和用户是透明的，切换过程通常很快）

	![权限从有到无的变更导致切换示意图](//mccdn.qcloud.com/img56cdd763b0628.png)

- 用户位于DC，权限从无到有：不存在这种情况
- 用户位于OC，权限从有到无：在此情况下SDK不会有任何动作
- 用户位于OC，权限从无到有（将AUTH_BITS_SEND_AUDIO/AUTH_BITS_SEND_VEDIO/AUTH_BITS_SEND_SUB其中一个置为非0），在此情况下，音视频后台会下发重定向指令，将终端实例重定向到DC

	![权限从无到有的变更导致切换示意图](//mccdn.qcloud.com/img56cdd789c7ee8.png)
