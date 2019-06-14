## 简介
#### 腾讯云 TUIKit

TUIKit 是基于腾讯云 IMSDK 的一款 UI 组件库，里面提供了一些通用的 UI 组件，开发者可通过该组件库选取自己所需要的组件快速的搭建一个 IM 应用。
IM 软件都具备一些通用的 UI 界面，如会话列表，聊天界面等。TUIKit 提供了这一类的组件，并提供了灵活的 UI 和交互扩展接口，方便用户做个性化开发。

#### IMSDK 与 TUIKit 的结合
腾讯云 IMSDK 提供了 IM 通信所需的各种基础能力，如通信网络，消息收发、存储，好友关系链，用户资料等。 TUIKit 中的组件在实现 UI 功能的同时调用 IMSDK 相应的接口实现了 IM 相关逻辑和数据的处理，因而开发者在使用 TUIKit 时只需关注自身业务或做一些个性化的扩展即可。
下面我们将指导您如何快速的接入和使用 TUIKit。

## 帐号相关的基本概念

这里我们先来了解帐号相关的几个概念。

- **用户标识（userId）**:
userId（用户标识）用于在一个 IM 应用中唯一标识一个用户，即我们通常所说的帐号。这个一般由开发者自己的服务生成，即用户信息的生成（注册）需由开发者实现。

- **用户签名（userSig）**:
userSig（用户签名）是用于对一个用户进行鉴权认证，确认用户是否真实的。即用户在开发者的服务里注册一个帐号后，开发者的服务需要给该帐号配置一个 usersig，后续用户登录 IM 的时候需要带上 usersig 让 IM 服务器进行校验。用户签名生成方法可参考 [生成签名](https://cloud.tencent.com/document/product/647/17275) 文档。

了解了前面的概念后，您可以通过下图了解集成了 IMSDK 应用的注册/登录流程。

![](http://dldir1.qq.com/hudongzhibo/im/regist&login.jpg)

首先用户的终端需要向您的服务器注册帐号(userid)，您的服务器在进行注册业务处理时，按照用户签名文档中的方法生成一个该用户的 usersig，并返回给客户端。客户端再通过该 userid 和 usersig 到 IMSDK 进行登录操作。
为方便开发者接入开发测试，我们在腾讯云控制台提供了快速生成 usersig 的工具（在这之前您需要先在腾讯云创建自己的 IM 应用，可参考 [云通信 IM 入门](https://cloud.tencent.com/product/im/getting-started)）。登录控制台后选择-【云通信】-【应用列表】（选择您当前在使用的应用）-【应用配置】-【开发辅助工具】，参考上面说明即可生成 usersig。

## TUIKit效果图


<div align="center">
<img src="https://cdn.nlark.com/yuque/0/2019/gif/367185/1560518740493-e5a89223-4cb4-44df-a9a5-665e78b67983.gif#align=left&display=inline&height=674&name=%E4%BC%9A%E8%AF%9D%E5%88%97%E8%A1%A8.gif&originHeight=674&originWidth=380&size=319844&status=done&width=380" width="300" height="535">
</div>

<div align="center">
<img src="https://cdn.nlark.com/yuque/0/2019/gif/367185/1560519391978-f7dbd5fa-8ee7-4b4c-9e71-c7e8d6c5b01b.gif#align=left&display=inline&height=674&name=%E8%81%8A%E5%A4%A9%E6%BC%94%E7%A4%BA.gif&originHeight=674&originWidth=380&size=918355&status=done&width=380" width="300" height="535">
</div>

<div align="center">
<img src="https://cdn.nlark.com/yuque/0/2019/gif/366128/1559825875054-fdfb0919-1f59-4382-924a-b2197f813ab4.gif#align=left&display=inline&height=533&name=add.gif&originHeight=1920&originWidth=1080&size=547272&status=done&width=300" width="300" height="535">
</div>


<div align="center">
<img src="https://cdn.nlark.com/yuque/0/2019/gif/366128/1559825509248-ebb52b9b-8fee-421f-ad32-f2a12192167c.gif#align=left&display=inline&height=533&name=replace%2B.gif&originHeight=1920&originWidth=1080&size=177751&status=done&width=300" width="300">
</div>

<div align="center">
<img src="https://cdn.nlark.com/yuque/0/2019/gif/366128/1559826601807-394ea189-6188-47e7-bfe8-bb19c67b9dbb.gif#align=left&display=inline&height=587&name=new.gif&originHeight=1920&originWidth=1080&size=508813&status=done&width=330" width="300" height="535">
</div>

## TUIKit文档

<table >
  <tr>
    <th width="180px" style="text-align:center">功能模块</th>
    <th width="180px" style="text-align:center">平台</th>
    <th width="500px" style="text-align:center">文档链接</th>
  </tr>

  <tr >
    <td rowspan='2' style="text-align:center">快速集成</td>
    <td style="text-align:center">iOS</td>
    <td style="text-align:center"><a href="https://github.com/tencentyun/TIMSDK/wiki/TUIKit-iOS%E5%BF%AB%E9%80%9F%E9%9B%86%E6%88%90">TUIKit-iOS快速集成</a></td>
  </tr>

  <tr>
    <td style="text-align:center">Android</td>
    <td style="text-align:center"><a href="https://github.com/tencentyun/TIMSDK/wiki/TUIKit-Android%E5%BF%AB%E9%80%9F%E9%9B%86%E6%88%90">TUIKit-Android快速集成</a></td>
  </tr>

  <tr>
    <td rowspan='2' style="text-align:center">快速搭建</td>
    <td style="text-align:center">iOS</td>
    <td style="text-align:center"><a href="https://github.com/tencentyun/TIMSDK/wiki/TUIKit-iOS%E5%BF%AB%E9%80%9F%E6%90%AD%E5%BB%BA">TUIKit-iOS快速搭建</a></td>
  </tr>

  <tr>
    <td style="text-align:center">Android</td>
    <td style="text-align:center"><a href="https://github.com/tencentyun/TIMSDK/wiki/TUIKit-Android%E5%BF%AB%E9%80%9F%E6%90%AD%E5%BB%BA">TUIKit-Android快速搭建</a></td>
  </tr>

  <tr>
    <td rowspan='6' style="text-align:center">修改界面样式</td>
    <td style="text-align:center">iOS</td>
    <td style="text-align:center"><a href="https://github.com/tencentyun/TIMSDK/wiki/TUIKit-iOS%E4%BF%AE%E6%94%B9%E7%95%8C%E9%9D%A2%E6%A0%B7%E5%BC%8F">TUIKit-iOS修改界面样式</a></td>

  </tr>

  <tr>
    <td rowspan='5' style="text-align:center">Android</td>
    <td style="text-align:center"><a href="https://github.com/tencentyun/TIMSDK/wiki/TUIKit-Android%E4%BF%AE%E6%94%B9%E7%95%8C%E9%9D%A2%E6%A0%B7%E5%BC%8F-%E4%BC%9A%E8%AF%9D%E5%88%97%E8%A1%A8">TUIKit-Android修改界面样式-会话列表</a></td>
  </tr>

  <tr>
    <td style="text-align:center"><a href="https://github.com/tencentyun/TIMSDK/wiki/TUIKit-Android%E4%BF%AE%E6%94%B9%E7%95%8C%E9%9D%A2%E6%A0%B7%E5%BC%8F-%E8%81%8A%E5%A4%A9%E7%95%8C%E9%9D%A2">TUIKit-Android修改界面样式-聊天界面</a></td>
  </tr>

  <tr>
    <td style="text-align:center"><a href="https://github.com/tencentyun/TIMSDK/wiki/TUIKit-Android%E4%BF%AE%E6%94%B9%E7%95%8C%E9%9D%A2%E6%A0%B7%E5%BC%8F-%E8%81%8A%E5%A4%A9%E7%95%8C%E9%9D%A2-%E9%80%9A%E7%9F%A5%E5%8C%BA%E5%9F%9F">TUIKit-Android修改界面样式-聊天界面-通知区域</a></td>
  </tr>

  <tr>
    <td style="text-align:center"><a href="https://github.com/tencentyun/TIMSDK/wiki/TUIKit-Android%E4%BF%AE%E6%94%B9%E7%95%8C%E9%9D%A2%E6%A0%B7%E5%BC%8F-%E8%81%8A%E5%A4%A9%E7%95%8C%E9%9D%A2-%E6%B6%88%E6%81%AF%E5%8C%BA%E5%9F%9F">TUIKit-Android修改界面样式-聊天界面-消息区域</a></td>
  </tr>

  <tr>
    <td style="text-align:center"><a href="https://github.com/tencentyun/TIMSDK/wiki/TUIKit-Android%E4%BF%AE%E6%94%B9%E7%95%8C%E9%9D%A2%E6%A0%B7%E5%BC%8F-%E8%81%8A%E5%A4%A9%E7%95%8C%E9%9D%A2-%E8%BE%93%E5%85%A5%E5%8C%BA%E5%9F%9F">TUIKit-Android修改界面样式-聊天界面-输入区域</a></td>
  </tr>

  <tr>
    <td rowspan='2' style="text-align:center">自定义消息</td>
    <td style="text-align:center">iOS</td>
    <td style="text-align:center"><a href="https://github.com/tencentyun/TIMSDK/wiki/TUIKit-iOS%E8%87%AA%E5%AE%9A%E4%B9%89%E6%B6%88%E6%81%AF">TUIKit-iOS自定义消息</a></td>
  </tr>

  <tr>
    <td style="text-align:center">Android</td>
    <td style="text-align:center"><a href="https://github.com/tencentyun/TIMSDK/wiki/TUIKit-Android%E8%87%AA%E5%AE%9A%E4%B9%89%E6%B6%88%E6%81%AF">TUIKit-Android自定义消息</a></td>
  </tr>
  
</table>




## 快速体验

欢迎扫码体验我们的 DEMO，后续会继续完善。更多最新资讯请关注 [这里](https://github.com/zhaoyang21cn/IMTUIkit_android)。

![](https://main.qcloudimg.com/raw/fe3ef4a58c3efa5388e57a653133f392.png)

