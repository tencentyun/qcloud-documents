腾讯云提供了全套技术文档和源码来帮助您快速构建一个音视频小程序，但是再好的源码和文档也有学习成本，为了尽快的能调试起来，我们还提供了一个快速一键部署服务（开发环境免费部署）：您只需轻点几下鼠标，就可以在自己的账号下获得一个音视频小程序，同时附送一台拥有独立域名的测试服务器，让您可以在 5 分钟内快速构建出自己的测试环境。
>注意：
测试中产生的云服务费将正常收取。
>相关云服务费详细介绍情参考 [购买指导](/document/product/454/13649)

## 准备工作
### step1 通过微信公众平台授权登录腾讯云
打开 [微信公众平台](https://mp.weixin.qq.com) 注册并登录小程序，保存小程序的 WX_APPID 和 WX_APPSECRET 供后面使用，按如下步骤操作：

1. 单击左侧菜单栏中的【设置】。
2. 单击右侧 Tab 栏中的【开发者工具】。
3. 单击【腾讯云】，进入腾讯云工具页面，单击【开通】。
4. 使用小程序绑定的微信扫码即可将小程序授权给腾讯云，开通之后会自动进去腾讯云微信小程序控制台，显示开发环境已开通，此时可以进行后续操作。

> **注意：**
> 此时通过小程序开发者工具查看腾讯云状态并不会显示已开通，已开通状态会在第一次部署开发环境之后才会同步到微信开发者工具上。

![进入微信公众平台后台](https://mc.qcloudimg.com/static/img/a3ca2891b23cfce7d3678cd05a4e14fe/13.jpg)

![开通腾讯云](https://mc.qcloudimg.com/static/img/53e34b52e098ee3a0a02ecc8fbb68a54/14.jpg)

![腾讯云微信小程序控制台](https://mc.qcloudimg.com/static/img/032d0b2b99dfcfdf4234db911e93b60f/15.png)

### step2 开通小程序类目与推拉流标签【重要】
出于政策和合规的考虑，微信暂时没有放开所有小程序对 &lt;live-pusher&gt; 和 &lt;live-player&gt; 标签的支持：

- 个人账号和企业账号的小程序暂时只开放如下表格中的类目：
<table>
<tr align="center">
<th width="200px">主类目</th>
<th width="700px">子类目</th>
</tr>
<tr align="center">
<td>【社交】</td>
<td>直播</td>
</tr>
<tr align="center">
<td>【教育】</td>
<td>在线教育</td>
</tr>
<tr align="center">
<td>【医疗】</td>
<td>互联网医院，公立医院</td>
</tr>
<tr align="center">
<td>【政务民生】</td>
<td>所有二级类目</td>
</tr>
<tr align="center">
<td>【金融】</td>
<td>基金、信托、保险、银行、证券/期货、非金融机构自营小额贷款、征信业务、消费金融</td>
</tr>
</table>

- 符合类目要求的小程序，需要在小程序管理后台的<font color='red'> “设置 - 接口设置” </font>中自助开通该组件权限，如下图所示：
![](https://mc.qcloudimg.com/static/img/a34df5e3e86c9b0fcdfba86f8576e06a/weixinset.png)

>注意：如果以上设置都正确，但小程序依然不能正常工作，可能是微信内部的缓存没更新，请删除小程序并重启微信后，再进行尝试。

### step3 开通腾讯云服务
小程序跟 WebRTC 的互通是基于实时音视频（[TRTC](https://cloud.tencent.com/product/trtc)）服务实现的，需要开通该服务。

- 进入实时音视频 [管理控制台](https://console.cloud.tencent.com/rav)，如果服务还没有开通，点击申请开通，之后会进入腾讯云人工审核阶段，审核通过后即可开通。
- 服务开通后，进入 [管理控制台](https://console.cloud.tencent.com/rav) 创建实时音视频应用，点击【确定】按钮即可。
![](https://main.qcloudimg.com/raw/20d0adeadf23251f857571a65a8dd569.png)
- 从实时音视频控制台获取`sdkAppID、accountType、privateKey`：
![](https://main.qcloudimg.com/raw/0f99232db6d55ce846ffde6e19456eba.png)

从验证方式中下载公私钥，解压出来将 private_key 用文本编辑器打开，如：

```bash
-----BEGIN PRIVATE KEY-----
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
-----END PRIVATE KEY-----
```

将其转换成字符串形式如下所示，后面在 server 配置文件中使用，<font color='red'>请注意每行后面要加入\r\n</font>：

```bash
"-----BEGIN PRIVATE KEY-----\r\n"+
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\n"+
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\n"+
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\r\n"+
"-----END PRIVATE KEY-----\r\n"
```
public_key 也采用同样的方式编辑，供后续使用。

## 小程序demo部署
### step1 安装微信小程序开发工具
下载并安装最新版本的 [微信开发者工具](https://mp.weixin.qq.com/debug/wxadoc/dev/devtools/download.html)，使用小程序绑定的微信号扫码登录开发者工具。
![微信开发者工具](https://mc.qcloudimg.com/static/img/4fd45bb5c74eed92b031fbebf8600bd2/1.png)

### step2 下载小程序 Demo
访问 [SDK+Demo](https://cloud.tencent.com/document/product/454/7873#XiaoChengXu)，获取小程序 Demo 和后台源码。

### step3 上传和部署代码

1. 打开第四步安装的微信开发者工具，点击【小程序项目】按钮。
2. 输入小程序 AppID，项目目录选择上一步下载下来的代码目录，点击确定创建小程序项目。
3. 再次点击【确定】进入开发者工具。
> **注意：**
> 目录请选择 `RTMPRoom` 根目录。包含有 `project.config.json`，请不要只选择 `wxlite` 目录。
 
 ![上传代码](https://mc.qcloudimg.com/static/img/fd7074730e5b37af8a4d86dc8125d120/xiaochengxustart.png)

4. 打开 Demo 代码中 `server` 目录下的 `config.js` 文件，将其中的 `IM_SDKAPPID`、`IM_ACCOUNTTYPE`、`PRIVATEKEY`、配置成上述云通信服务里生成的值，同时将小程序的`WX_APPID`、`WX_APPSECRET`配置进去，并**保存**。
![serverconfig](	https://main.qcloudimg.com/raw/c33de87d0142cf0bd7357b3c624fb98e.png)

5. 点击界面右上角的【腾讯云】图标，在下拉的菜单栏中选择【上传测试代码】。
![上传按钮](https://mc.qcloudimg.com/static/img/8480bbc02b097bac0d511c334b731e12/5.png)

6. 选择【模块上传】并勾选全部选项，然后勾选【部署后自动安装依赖】，点击【确定】开始上传代码。
![选择模块](https://mc.qcloudimg.com/static/img/d7ff3775c77a662e9c18807916ab8045/6.png)
![上传成功](https://mc.qcloudimg.com/static/img/a78431b42d0edf0bddae0b85ef00d40f/7.png)

7. 上传代码完成之后，点击右上角的【详情】按钮，接着选择【腾讯云状态】即可看到腾讯云自动分配给你的开发环境域名，完整复制（包括 `https://`）开发环境 request 域名，然后在编辑器中打开 `wxlite/config.js` 文件，将复制的域名填入 `url` 中并保存，保存之后编辑器会自动编译小程序，左边的模拟器窗口即可实时显示出客户端的 Demo：
![查看开发域名](https://main.qcloudimg.com/raw/c5ed016e213cac0be7cb623dd0c96895.png)

8. 在模拟器中编译运行点击多人音视频进入，在右侧的 console 里面可以看到登录成功的 log 表示配置成功。
![登录测试](https://main.qcloudimg.com/raw/ee916ccef75ca8a3821d0e0e5a76df21.png)

9. 请使用手机进行测试，直接扫描开发者工具预览生成的二维码进入，<font color='red'> 这里部署的后台是开发测试环境，一定要开启调试: </font>
![开启调试](https://mc.qcloudimg.com/static/img/1abfe50750f669ca4e625ec3cdfbd411/xiaochengxutiaoshi.png)

<font color='red'> 注意：后台服务器部署的测试环境有效期为七天，如果还需要测试体验请重新部署后台。小程序访问域名有白名单限制，小程序开启调试就不会检查白名单，测试期间建议开启白名单，最后要发布的时候将域名配置到白名单里面，请参考常见问题里面如何部署正式环境？</font>

## Web 端 Demo部署

### Demo 体验 
用 Chrome 浏览器打开 [体验地址](https://sxb.qcloud.com/miniApp/)，即可体验 Chrome（WebRTC） + 微信（小程序）的视频通话功能，如下图所示：
![](https://main.qcloudimg.com/raw/81edf044e0a40ccfd4794b91185f1f82.jpg)

### step1  源码调试
#### Client
[github地址](https://github.com/TencentVideoCloudMLVBDev/webrtc_pc)。
> 该demo只能运行于支持 WebRTC 的浏览器中：
  
| 目录 | 说明 | 
|:-------:|---------|
| index.html | Demo 主页面 | 
| vue| vue 框架代码 | 
| third | 第三方 js 文件 | 
| component | Demo 页面的主要业务逻辑位于该文件夹下的各个 js 文件中 | 

#### Server
[github地址](https://github.com/TencentVideoCloudMLVBDev/webrtc_server_java) 

这份代码的主要作用是实现了一个简单的（无鉴权的）房间列表，可以支持创建通话房间，关闭通话房间等功能。如果您只是希望打通视频通话（在 Chrome 和 小程序端 写死一个 roomid），则不太需要这部分代码的帮助。 

| 目录 | 说明 | 
|:-------:|---------|
|README.pdf | 介绍了如何使用这份后台代码 | 
|后台接口表.pdf| 介绍了这份后台代码的内部实现细节 | 
| src | java 版本的后台房间列表源代码 | 


### 对接原理
下面这幅图简单介绍了如何将 WebRTC 方案整合到您的现有的业务系统中：
![](https://main.qcloudimg.com/raw/6670541d971f3a133027342b29265aaf.png)

#### step1: 搭建业务服务器
业务服务器的作用主要是向PC端网页和微信小程序派发 userid、usersig、roomid、 privateMapKey 这些进行视频通话所必须的信息。其中roomid 和 userid 都可以由您的业务后台自由决定，只要确保不会出现 id重叠 就可以。usersig 和 privateMapKey 的计算则需要参考示例源码[（java | PHP）](https://cloud.tencent.com/document/product/454/7873#Server)。
 
#### step2: 对接 Chrome
虽然谷歌给出了很多的文档和教程介绍如何使用使用 WebRTC，但是官方文档过于追求灵活性，所以理解成本很高，腾讯云推出了一个简化版的封装接口，阅读腾讯云 [WebRTC API](https://cloud.tencent.com/document/product/647/16865) 了解如何通过几个函数的调用就能完成 WebRTC 的 Chrome 端对接。

#### step3: 对接小程序端代码
微信 6.6.6 版本中开始支持 WebRTC 互通，参考 [**&lt;webrtc-room&gt;**](https://cloud.tencent.com/document/product/454/16914) 了解如何快速实现一个支持 WebRTC 视频通话的小程序。



## 常见问题 FAQ
#### 1. 运行出错如何排查？
- 请修改`wxlite/config.js`中的url，使用默认的官方demo后台：`https://room.qcloud.com` ，直接运行小程序
- 请重新解压下载的demo直接运行小程序，默认就是官方demo后台
- 请返回第二步检查开通的小程序类目是否正确，推拉流标签在小程序控制台是否开启
- 使用官方demo后台运行可以，请参考此文档再重新部署一遍
- 依然不行可以提工单或客服电话（400-9100-100）联系我们

#### 2. 运行小程序进入多人音视频看不到画面?
- 请确认使用手机来运行，微信开发者工具内部的模拟器目前还不支持直接运行
- 请确认小程序基础库版本 wx.getSystemInfo 可以查询到该信息，1.7.0 以上的基础库才支持音视频能力。
- 请确认小程序所属的类目，由于监管要求，并非所有类目的小程序都开发了音视频能力，已支持的类目请参考 [DOC](https://cloud.tencent.com/document/product/454/13037)。
- 如有更多需求，或希望深度合作，可以提工单或客服电话（400-9100-100）联系我们。

#### 3. live-pusher、live-player标签使用及错误码参考
- [live-pusher&错误码](https://mp.weixin.qq.com/debug/wxadoc/dev/component/live-pusher.html)
- [live-player&错误码](https://mp.weixin.qq.com/debug/wxadoc/dev/component/live-player.html)
- [livePusherContext](https://mp.weixin.qq.com/debug/wxadoc/dev/api/api-live-pusher.html)
- [livePlayerContext](https://mp.weixin.qq.com/debug/wxadoc/dev/api/api-live-player.html)

#### 4. 如果需要上线或者部署正式环境怎么办？
- 请申请域名并做备案
- 请将服务端代码部署到申请的服务器上
- 请将业务server域名、RoomService域名及IM域名配置到小程序控制台request合法域名里面，其中IM域名为：`https://webim.tim.qq.com` ，RoomService域名为：`https://room.qcloud.com`
 
