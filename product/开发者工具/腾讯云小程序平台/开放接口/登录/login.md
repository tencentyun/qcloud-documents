# wx.login
### wx.login(Object object)

IDE暂不支持，该API需要和宿主App联调，返回的内容需要宿主App提供。

#### 参数

##### Object object

属性       | 类型       | 默认值 | 必填 | 说明                                                                                                                                          
-------- | -------- | --- | -- | --------------------------------------------------------------------------------------------------------------------------------------------
success  | function |     | 否  | 接口调用成功的回调函数                                                                                                                                 
fail     | function |     | 否  | 接口调用失败的回调函数                                                                                                                                 
complete | function |     | 否  | 接口调用结束的回调函数（调用成功、失败都会执行）                                                                                                                    

#### 示例代码

```js
wx.login({
  success(res) {
    console.log(res ,"---------------info, host app return");
  }
})
```
