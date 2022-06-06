## 前提条件
1. 已完成 [快速入门（使用方式：SDK 集成）](https://cloud.tencent.com/document/product/679/73495)。
2. 已完成 [电话号码购买](https://cloud.tencent.com/document/product/679/73526) 或 [自携电话号码对接](https://cloud.tencent.com/document/product/679/73527)。

## 集成效果
腾讯云呼叫中心已经提供默认通话工具条 UI 样式，集成后坐席可直接使用。企业也可隐藏默认样式并调用相关接口自定义 UI 开发。
![](https://qcloudimg.tencent-cloud.cn/raw/65af020fb8181a5b7e4190fb43db5812.png)

## 集成方法 
1. 集成腾讯云呼叫中心 SDK，具体接入步骤参考 [集成座席端工作台](https://cloud.tencent.com/document/product/679/72042)。
2. 调用[ SDK API Call（电话呼出）](https://cloud.tencent.com/document/product/679/72044#.E7.94.B5.E8.AF.9D.E5.91.BC.E5.87.BA)。

## 自定义 UI 样式
1. 隐藏 SDK UI，详情参考 [SDK API UI（用户界面相关接口函数）](https://cloud.tencent.com/document/product/679/72044#ui.EF.BC.88.E7.94.A8.E6.88.B7.E7.95.8C.E9.9D.A2.E7.9B.B8.E5.85.B3.E6.8E.A5.E5.8F.A3.E5.87.BD.E6.95.B0.EF.BC.89) 。
2. 根据业务需要调用相应的 SDK API（如：挂断、静音、通话保持等）完成通话工具条样式开发，详情参考 [SDK API](https://cloud.tencent.com/document/product/679/72044)。

## 事件通知
SDK 提供了外呼事件、外呼接听事件，企业可通过事件监听及时获取电话呼出事件信息，便于在业务系统弹屏展示对应客户信息。详情参考 [SDK API Events（事件）](https://cloud.tencent.com/document/product/679/72044#events.EF.BC.88.E4.BA.8B.E4.BB.B6.EF.BC.89)。
