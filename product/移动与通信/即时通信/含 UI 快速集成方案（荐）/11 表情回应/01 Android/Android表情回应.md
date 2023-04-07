## 功能描述
TUIKit 从 [6.3.2609](https://cloud.tencent.com/document/product/269/1606#6.3.2609-.402022.06.16---.E5.A2.9E.E5.BC.BA.E7.89.88) 版本开始 ，聊天消息支持表情回应功能。

“表情回应”功能使用 IMSDK [消息变更](https://cloud.tencent.com/document/product/269/75327) 能力实现。

## 效果展示

### 发送表情回应

开启表情回应能力后，长按消息菜单上方会多一条表情选择区。该区域支持点击右侧按钮扩大，展示更多表情。点击表情即可对该消息进行表情回应。如果已经使用该表情对该消息进行回应过，点击表情后会取消回应。


<table style="text-align:center;vertical-align:middle;width:600px">
  <tr>
    <th style="text-align:center;" width="300px">长按消息菜单<br></th>
    <th style="text-align:center;" width="300px">更多表情<br></th>
  </tr>
  <tr>
    <td style="text-align:center;"><img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/5850964be7a7714cc7670c7f665e142d/%E8%A1%A8%E6%83%85%E5%9B%9E%E5%BA%94%E9%95%BF%E6%8C%892.png"  />    </td>
    <td style="text-align:center;"><img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/c20688323e340222f0ab5b15951a0346/%E8%A1%A8%E6%83%85%E5%9B%9E%E5%BA%94%E6%9B%B4%E5%A4%9A2.png" />     </td>
	 </tr>
</table>


### 展示表情回应

一条消息收到的所有回应表情，都会展示在这条消息的下方，会话中所有成员均可看到。

在消息下方，会显示回应的表情和回应了该表情的聊天成员昵称，点击表情可以快速回应相同表情或者取消回应该表情。

<img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/ff3495b661378c83ac797b30df10d159/%E8%A1%A8%E6%83%85%E5%9B%9E%E5%BA%94%E6%A0%B7%E5%BC%8F2.png"  /> 


## 关闭表情回应

在 `TUIChat` 组件中的 [GeneralConfig.java](https://github.com/TencentCloud/TIMSDK/blob/master/Android/TUIKit/TUIChat/tuichat/src/main/java/com/tencent/qcloud/tuikit/tuichat/config/GeneralConfig.java) 文件里，提供了“表情回应”功能开关 **reactEnable** , 其类型为 boolean，默认为 `true` 。

```java
public class GeneralConfig {
    private boolean reactEnable = true;
    // ... 其他配置
}
```

如果不想开启表情回应，可以把 **reactEnable** 的默认值改为 `false`  ，或者在聊天页面初始化之前调用以下方法来关闭。
```java
TUIChatConfigs.getConfigs().getGeneralConfig().setReactEnable(false);
```

关闭之后消息长按弹窗的效果：

<img style="width:250px" src="https://qcloudimg.tencent-cloud.cn/raw/88d9732233d3422b5c91d1c593a980a2/%E8%A1%A8%E6%83%85%E5%9B%9E%E5%BA%94%E5%85%B3%E9%97%AD2.png" />

## 交流与反馈
欢迎加入 QQ 群进行技术交流和反馈问题。
<img src="https://im.sdk.qcloud.com/tools/resource/officialwebsite/pictures/doc_tuikit_qq_group.jpg" style="zoom:50%;"/> 
