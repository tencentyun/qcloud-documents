
## 功能描述
TUIKit 从 v1.3.1 版本开始，已支持表情回应功能。
“表情回应”功能采用消息变更实现，在开启“表情回应”功能前，需要将您的 IMSDK 升级至 v2.20.0 及以上版本以支持消息变更操作。
更多消息变更相关内容详见：[消息变更](https://cloud.tencent.com/document/product/269/75328)。
<table style="text-align:center;vertical-align:middle;width:1000px;overflow-x:auto;">
  <tr>
    <th style="text-align:center;" width="500px">开启“表情回应”<br></th>
    <th style="text-align:center;" width="500px">关闭“表情回应”<br></th>
  </tr>
  <tr>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/4d626fbe22b0ddb43dc427d4317cdf8e.png"  />    </td>
    <td><img style="width:500px" src="https://qcloudimg.tencent-cloud.cn/raw/8dc6a4ed7471ed577d69931b06f0ad25.png" /> </td>
</table>

## 开启表情回应
在 TUIChat 顶层提供了“表情回应”功能开关 **isNeedEmojiReact** , 其类型为 boolean，默认为 true 。
<dx-codeblock>
 :::  html
 // 开启表情回应
 // open emoji react
<TUIChat :isNeedEmojiReact="true" />
 // 关闭表情回应
 // close emoji react
<TUIChat :isNeedEmojiReact="false" />
:::
</dx-codeblock>

## 交流与反馈

欢迎加入 QQ 群进行技术交流和反馈问题。
<img src="https://qcloudimg.tencent-cloud.cn/raw/960ce9d76ea2cebffcb7629741279b90.png" alt="" style="zoom:50%;" />

