## 接口描述
- **描述：**
 - 对网络研讨会进行 Webinar 进行暖场设置。
 - 支持 JWT 鉴权、OAuth2.0 鉴权，权限为：管理会议。
 - 可订阅网络研讨会暖场上传结果事件用于获得上传结果，请参见 [网络研讨会（Webinar）暖场上传结果](https://cloud.tencent.com/document/product/1095/79826) 。
- **调用方式：**POST
- **接口请求域名：**
```plaintext
https://api.meeting.qq.com/v1/webinars/{meeting_id}/warm-up
```

## 输入参数
<table>
   <tr>
      <th width="20%" >参数</td>
      <th width="20%" >是否必须</td>
      <th width="20%" >参数类型</td>
      <th width="40%" >参数描述</td>
   </tr>
   <tr>
      <td>operator_id	</td>
      <td>是</td>
      <td>String</td>
      <td>操作者 ID。会议创建者可以修改会议配置。
<br>operator_id 必须与 operator_id_type 配合使用。根据 operator_id_type 的值，operator_id 代表不同类型。
<br>operator_id_type=2，operator_id 必须和公共参数的 openid 一致。
<br>使用 OAuth 公参鉴权后不能使用 userid 为入参。</td>
   </tr>
   <tr>
      <td>operator_id_type</td>
      <td>是</td>
      <td>Integer</td>
      <td>操作者 ID 的类型：<br>1：userid<br>2：open_id</td>
   </tr>
   <tr>
      <td>instanceid</td>
      <td>是</td>
      <td>Integer</td>
      <td>用户的终端设备类型：<br>0：PSTN<br>1：PC<br>2：Mac<br>3：Android<br>4：iOS<br>5：Web<br>6：iPad<br>7：Android Pad<br>8：小程序<br>9：voip、sip 设备<br>10：linux<br>20：Rooms for Touch Windows<br>21：Rooms for Touch MacOS<br>22：Rooms for Touch Android<br>30：Controller for Touch Windows<br>32：Controller for Touch Android<br>33：Controller for Touch iOS</td>
   </tr>
   <tr>
      <td>warm_up_picture</td>
      <td>否</td>
      <td>String</td>
      <td>暖场图片地址，推荐使用腾讯云对象存储。
<br>暖场图片与暖场视频只能选择一个，如果同时传入图片和视频，以图片为准。
<br>图片推荐 1280*720 尺寸，支持 png/jpg 格式，大小不超过 5M。
<br>会议开始前 15 分钟进入的观众可观看暖场，仅支持 3.3.0 及以上版本客户端观看。</td>
   </tr>
   <tr>
      <td>warm_up_video</td>
      <td>否</td>
      <td>String</td>
      <td>暖场视频地址，推荐使用腾讯云对象存储。
<br>暖场图片与暖场视频只能选择一个，如果同时传入图片和视频，以图片为准。
<br>推荐 1280*720 尺寸，支持 mp4 格式，大小不超过 1G。
<br>会议开始前 15 分钟进入的观众可观看暖场，仅支持 3.3.0 及以上版本客户端观看。</td>
   </tr>
   <tr>
      <td>allow_participants_invite_others</td>
      <td>否</td>
      <td>Boolean</td>
      <td>	允许参会者在暖场中邀请成员。<br>true：允许，默认允许。<br>false：不允许。</td>
   </tr>
</table>

## 输出参数
成功则返回为空


## 示例
#### 输入示例
```plaintext
POST
https://api.meeting.qq.com/v1/webinars/7976035087704477330/warm-up
{
    "operator_id":"user",
    "operator_id_type":1,
    "instanceid":1,
    "warm_up_picture":"https://xxxxxx.cos.myqcloud.com/flower.png",
    "warm_up_video":"https://xxxxxx.cos.myqcloud.com/cat.mp4",
    "allow_participants_invite_others":true
}
```

#### 输出示例
```plaintext
{}
```
