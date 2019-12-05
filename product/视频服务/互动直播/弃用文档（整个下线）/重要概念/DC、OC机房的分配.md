## 相关概念说明

- **DC（Data Center）：**核心机房，用于互动直播业务中需要上行音视频数据或实时交互的用户角色（如主播、讲师、参与实时互动的角色等）接入。
- **OC（Outer Center）：**边缘节点，用于互动直播业务中不需要上行音视频数据、仅观看的用户角色（如普通观众、不需要与老师互动的学生等）接入。

二者的计费价格是不同的。关于价格详情和分配策略参见 [基础网络费用](https://cloud.tencent.com/doc/product/268/5128#.E5.9F.BA.E7.A1.80.E7.BD.91.E7.BB.9C.E8.B4.B9.E7.94.A8.E8.AE.A1.E7.AE.97.E5.85.AC.E5.BC.8F)。

## 关于 DC 和 OC 的分配原则

对于一个 App 的用户来说，什么情况下会接入 DC、什么情况下会接入 OC 呢？

代码层面需要关心的分配原则简单来说只有一句话：有上行音视频数据权限的实例会分配 DC、没有上行音视频数据权限的实例分配 OC。具体地，在调用 SDK 进入房间接口 `ILiveRoomManager.getInstance().createRoom()` 的时候，其参数 `ILiveRoomOption.authBits()` 用于设置该实例在房间内的权限，具体权限字段如下：

| 字段 | 值 | 说明 |
| --- | --- | --- |
| AUTH_BITS_DEFUALT | 0xFFFFFFFFFFFFFFFF | 缺省值。拥有所有权限。 |
| AUTH_BITS_CREATE_ROOM | 0x00000001 | 创建房间权限。 |
| AUTH_BITS_JOIN_ROOM | 0x00000002 | 加入房间的权限。 |
| AUTH_BITS_SEND_AUDIO | 0x00000004 | 发送语音的权限。 |
| AUTH_BITS_RECV_AUDIO | 0x00000008 | 接收语音的权限。 |
| AUTH_BITS_SEND_VIDEO | 0x00000010 | 发送视频的权限。 |
| AUTH_BITS_RECV_VIDEO | 0x00000020 | 接收视频的权限。 |
| AUTH_BITS_SEND_SUB | 0x00000040 | 发送辅路视频的权限，暂不支持辅路。 |
| AUTH_BITS_RECV_SUB | 0x00000080 | 接收辅路视频的权限，暂不支持辅路。 |

AVRoomMulti.auth_bits 成员变量是权限位的明文形式。AVRoomMulti.auth_bits 将 `AUTH_BITS_SEND_AUDIO`/ `AUTH_BITS_SEND_VEDIO`/ `AUTH_BITS_SEND_SUB` 中的任意一个置为 1，则实例会被分配接入 DC；反之则该实例被分配接入 OC。

>? 后台对单个房间接入 DC 的用户数量有一个上限保护。例如，如果某个业务设置每个用户都有上行权限，那么后台对于每一个房间前1000个用户分配 DC，其他用户分配 OC。该限制为后台保护策略，后面可以根据需要进行调整。

## 关于 DC/OC 之间的切换策略

当用户通过进入房间的 `ILiveRoomManager.getInstance().createRoom()` 流程被分配到 DC/OC 之后，有时也会有需要在 DC/OC 之间进行切换的需求。例如，教育场景下，一个原本没有上行权限的学生（被分配接入 OC）被老师点中回答问题时，需要从不能上行音视频数据 OC 切换到 DC。DC/OC 的切换依然是以权限变化为依据的，相对应的接口为 ILiveRoomManager 类中 changeAuthAndRole 接口。下面将分几种情况来分别讨论：

- 用户位于 DC，权限从有到无（将 `AUTH_BITS_SEND_AUDIO` / `AUTH_BITS_SEND_VEDIO`/ `AUTH_BITS_SEND_SUB` 全设置为0），在此情况下，因为 OC 比 DC 有时延，为了避免学生切回 OC 后看到之前的画面，学生依然会留在 DC 直到退出房间。
- 用户位于 DC，权限从无到有：不存在这种情况。
- 用户位于 OC，权限从有到无：在此情况下 SDK 不会有任何动作。
- 用户位于 OC，权限从无到有（将 `AUTH_BITS_SEND_AUDIO` / `AUTH_BITS_SEND_VEDIO`/ `AUTH_BITS_SEND_SUB` 其中一个置为非0），在此情况下，音视频后台会下发重定向指令，将终端实例重定向到 DC。

![权限从无到有的变更导致切换示意图](https://mccdn.qcloud.com/img56cdd789c7ee8.png)
