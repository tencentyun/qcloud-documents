# wx.updateShareMenu(Object object)
更新转发属性

#### 参数

##### Object object

属性                 | 类型       | 默认值   | 必填 | 说明                                                                                                                                                                                       | 最低版本                                                                                                          
------------------ | -------- | ----- | -- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------
withShareTicket    | boolean  | false | 否  | 是否使用带 shareTicket 的转发 |                                                                                                           
success            | function |       | 否  | 接口调用成功的回调函数                                                                                                                                                                              |                                                                                                                
fail               | function |       | 否  | 接口调用失败的回调函数                                                                                                                                                                              |                                                                                                                
complete           | function |       | 否  | 接口调用结束的回调函数（调用成功、失败都会执行）                                                                                                                                                                 |                       

<!--isUpdatableMessage | boolean  | false | 否  | 是否是动态消息，详见[动态消息](/develop/game/frame/open-ability/share.html#动态消息)                                                                       | -->
<!--activityId         | string   |       | 否  | 动态消息的 activityId。通过 [createActivityId](/develop/game/server/open-port//dynamic-message.html) 接口获取                                                             | -->
<!--templateInfo       | Object   |       | 否  | 动态消息的模板信息                                                                                                                                                                                | -->

<!--**object.templateInfo 的结构**-->

<!--属性            | 类型             | 默认值 | 必填 | 说明  -->
<!--------------- | -------------- | --- | -- | ------>
<!--parameterList | Array.\<Object\> |     | 是  | 参数列表-->

<!--**parameterList 的结构**-->

<!--属性    | 类型     | 默认值 | 必填 | 说明 -->
<!------- | ------ | --- | -- | ----->
<!--name  | string |     | 是  | 参数名-->
<!--value | string |     | 是  | 参数值-->

#### 示例代码

```js
wx.updateShareMenu({
  withShareTicket: true
})
```