# wx.hideShareMenu(Object object)

点击右上角菜单时隐藏"分享给好友"、"分享到空间"按钮

#### 参数

##### Object object

属性       | 类型       | 默认值 | 必填 | 说明                      
-------- | -------- | --- | -- | ------------------------
hideShareItems  | Array.&lt;string&gt; | ['qq', 'qzone', 'wechatFriends', 'wechatMoment'] | 否  | 'qq'控制是否隐藏"转发"，'qzone'控制是否隐藏"分享到空间"，'wechatFriends'控制是否隐藏"分享到微信朋友"，'wechatMoment'控制是否控制隐藏"分享到微信朋友圈"，不带hideShareItems参数默认"转发"、"分享到空间"、"分享到微信朋友"、"控制是否控制隐藏"全隐藏。
success  | function |     | 否  | 接口调用成功的回调函数             
fail     | function |     | 否  | 接口调用失败的回调函数             
complete | function |     | 否  | 接口调用结束的回调函数（调用成功、失败都会执行）

#### 示例代码

```js
wx.hideShareMenu({
    hideShareItems: ['qq', 'qzone', 'wechatFriends', 'wechatMoment']
})
```