# wx.showShareMenu(Object object)

点击右上角菜单时显示当前页面的"分享给好友"、"分享到空间"、"分享到微信好友"、"分享到微信朋友圈"按钮

#### 参数

##### Object object

属性             | 类型       | 默认值   | 必填 | 说明                                                                                                                                                                                    
--------------- | -------- | ----- | -- | -------
showShareItems  | Array.&lt;string&gt; | ['qq', 'qzone', 'wechatFriends', 'wechatMoment'] | 否  | 请查看下面`object.showShareItems`参数说明
withShareTicket | boolean  | false | 否  | 是否使用带 shareTicket 的转发，Android从基础库1.4.0版本、iOS从基础库1.4.0版本开始支持。
success         | function |       | 否  | 接口调用成功的回调函数                                             
fail            | function |       | 否  | 接口调用失败的回调函数                                            
complete        | function |       | 否  | 接口调用结束的回调函数（调用成功、失败都会执行）     

##### object.showShareItems参数

值      | 说明    | 最低版本
--------|--------|------------
'qq'    | 控制是否展示"转发" |  
'qzone' | 控制是否展示"分享到空间" | 
'wechatFriends' | 控制是否展示"微信好友" | 1.6.3
'wechatMoment'  | 控制是否展示"微信朋友圈" | 1.6.3

不带showShareItems参数默认"转发"、"分享到空间"、"微信好友"、"微信朋友圈"全展示。

#### 示例代码

```js
wx.showShareMenu({
  showShareItems: ['qq', 'qzone', 'wechatFriends', 'wechatMoment']
})
```

<!--```js-->
<!--wx.showShareMenu({-->
<!--  withShareTicket: true-->
<!--})-->
<!--```-->