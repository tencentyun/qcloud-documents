腾讯云云游戏提供 JS-SDK 用于 Web 接入，支持端游和手游。SDK 提供了丰富的接口，满足大部分接入需求。接入方法请参见 [快速入门](https://cloud.tencent.com/document/product/1162/46135) 及 [搭建示例](https://cloud.tencent.com/document/product/1162/56337)，并可通过 [SDK 接口](https://cloud.tencent.com/document/product/1162/46134)，获取更多功能指引。

## SDK 下载 
| SDK  | 下载地址                           | SDK 说明文档                         |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| JS SDK | [GitHub下载](https://github.com/tencentyun/cloudgame-js-sdk) | [DOC](https://cloud.tencent.com/document/product/1162/46134) |

## 安装说明

`import dist/tcg-sdk`，导出的为 umd 格式。

## 版本信息 
<table>
<tr><th>日期</th><th width="17%">版本</th><th>更新内容</th></tr>
<tr>
<td>2021.05.26 </td>
<td><a href="https://ex.cloud-gaming.myqcloud.com/cloud_gaming_web_sdk/tcg-sdk/1.0.3/index.js">JS SDK 1.0.3 版本</a></td>
<td>
<b>新增</b><ul style="margin:0">
init 新增参数 showLoading，用于是否显示 loading 画面。
</ul>
<b>更新</b><ul style="margin:0">
onLoadedMetaData 逻辑修改。
</ul>
<b>修复</b><ul style="margin:0">
keyboard event 切换窗口卡建问题修复。
</ul></td></tr>
<tr>
<td>2021.05.18</td>
<td><a href="https://ex.cloud-gaming.myqcloud.com/cloud_gaming_web_sdk/tcg-sdk/1.0.2/index.js">JS SDK 1.0.2 版本</a></td>
<td>
<b>新增</b><ul style="margin:0">
<li/>setVideoOrientation 设置 video 的旋转角度。
<li/>init params 新增 mobileGame 参数，用于接入手游。
</ul>
<b>更新</b><ul style="margin:0">
onTouchEvent 新增支持多点触控，返回 <code>object[]</code>，object 数据类型和同之前版本。
</ul>
<b>修复</b><ul style="margin:0">
<li/>心跳启动逻辑导致断连。
<li/>onConnectSuccess 确保在 ACK 数据通道创建成功后。
</ul></td></tr>
<tr>
<td>2021.04.06</td>
<td><a href="https://ex.cloud-gaming.myqcloud.com/cloud_gaming_web_sdk/tcg-sdk/1.0.0/index.js">JS-SDK 1.0.0 版本</a></td>
<td>重构 TCGSDK。
</ul></tr>
</tbody></table>



