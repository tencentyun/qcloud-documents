TUIKit 默认实现了文本、图片、语音、视频、文件等基本消息类型的发送和展示，如果这些消息类型满足不了您的需求，您可以新增自定义消息类型。

## 基本消息类型
<table>
     <tr>
         <th width="20%" style="text-align:center">消息类型</th>  
         <th style="text-align:center">显示效果图</th>  
     </tr>
     <tr>      
         <td style="text-align:center">文本类消息</td>   
     <td style="text-align:center"><img src="https://qcloudimg.tencent-cloud.cn/raw/9cb4ed8a616242ef1af2c95deede7d41.png" width="320"/></td>   
     </tr> 
     <tr>      
         <td style="text-align:center">图片类消息</td>   
     <td style="text-align:center"><img src="https://qcloudimg.tencent-cloud.cn/raw/f55d26506d6d5a00e0155a682d55379b.png" width="320"/></td>   
     </tr> 
     <tr>      
         <td style="text-align:center">语音类消息</td>   
     <td style="text-align:center"><img src="https://qcloudimg.tencent-cloud.cn/raw/c391f8425e3274abc13ef22e7ab1b0bf.png" width="320"/></td>   
     </tr> 
     <tr>      
         <td style="text-align:center">视频类消息</td>   
     <td style="text-align:center"><img src="https://qcloudimg.tencent-cloud.cn/raw/5778254c16b8bbe925e1c5f2a72c22ea.png" width="320"/></td>   
     </tr> 
     <tr>      
         <td style="text-align:center">文件类消息</td>   
     <td style="text-align:center"><img src="https://qcloudimg.tencent-cloud.cn/raw/3b2bfdd4135840a07359c08b4c10aaea.png" width="320"/></td>   
     </tr> 
</table>

## 自定义消息
如果基本消息类型不能满足您的需求，您可以根据实际业务需求自定义消息。
TUIKit 中内置了几种自定义消息样式，如下图所示：
<table>
     <tr>
         <th width="20%" style="text-align:center">自定义消息预设样式</th>  
         <th style="text-align:center">显示效果图</th>  
     </tr>
     <tr>      
         <td style="text-align:center">超文本类消息</td>   
     <td style="text-align:center"><img src="https://qcloudimg.tencent-cloud.cn/raw/ba0942914ab685b2f787c2eb9562a071.png" width="320"/></td>   
     </tr> 
     <tr>      
         <td style="text-align:center">评价类消息</td>   
     <td style="text-align:center"><img src="https://qcloudimg.tencent-cloud.cn/raw/7a48e2fcc4b8480f7c41ff2bfbdf47a5.png" width="320"/></td>   
     </tr> 
     <tr>      
         <td style="text-align:center">订单类消息</td>   
     <td style="text-align:center"><img src="https://qcloudimg.tencent-cloud.cn/raw/2ab2d710f7b5d1fe94099942992678c6.png" width="320"/></td>   
     </tr> 
</table>
下文以发送一条可跳转至浏览器的超文本作为自定义消息为例，帮助您快速了解实现流程。


## 展示自定义消息
TUIKit 内置的自定义消息 cell 元素如下图所示：
<img src="https://qcloudimg.tencent-cloud.cn/raw/d199be3f5a4ff5693d4f80b62afb262f.png" width = "500"/>
自定义类消息和其他普通类型消息接收方式一致，所有类型消息都通过监听`TIM.EVENT.MESSAGE_RECEIVED`事件来获取。
收到的自定义消息根据相应的具体类型字段以不同的形式展示在消息列表中 。
下面我们讲解下如何展示自定义消息。

### 创建自定义消息展示结构
自定义消息的展示主要通过在 `messageBubble` 的内容区渲染 `messgaeCustom `实现。
您可以在路径 `src/TUIKit/TUIComponents/container/TUIChat/components/message-custom.vue` 文件下新增您需要的自定义消息展示结构样式。
以超文本类型消息展示结构为例，示例代码如下：
<dx-codeblock>
:::  html
<!-- 判断自定义消息展示类型 -->
<template v-else-if="isCustom.businessID === constant.typeTextLink">
	<div class="textLink">
		<!-- 展示文本 -->
		<p>{{isCustom.text}}</p>
		<!-- 展示超链接 -->
		<a :href="isCustom.link" target="view_window">{{$t('message.custom.查看详情>>')}}</a>
	</div>
</template>
:::
</dx-codeblock>

## 发送自定义消息
您可以通过调用路径 `src/TUIKit/TUIComponents/container/TUIChat/server.ts` 文件中的 `sendCustomMessage` 方法来发送一条自定义消息。 `sendCustomMessage` 接收一个参数 `data` ， `data` 会被作为消息 `Message` 的 `payload` 字段发送，其中参数 `data`  数据里面自定义一个 `businessID` 字段来唯一标识这条自定义消息类型。您可以通过构建不同的 data 数据项来实现发送不同类型的自定义消息。
发送超文本类自定义消息示例代码如下：
<dx-codeblock>
:::  js
const custom = {
	data: {
		// 自定义消息类型的标识字段
		businessID: constant.typeTextLink,
		// 超文本类自定义消息文字说明部分
		text: '欢迎加入腾讯云IM大家庭',
		// 超文本类自定义消息超链接部分
		link: 'https://buy.cloud.tencent.com/avc',
	},
	description: '欢迎加入腾讯云IM大家庭',
	extension: '欢迎加入腾讯云IM大家庭',
};
sendCustomMessage(custom);// 调用 sendCustomMessage 方法发送自定义消息
:::
</dx-codeblock>

