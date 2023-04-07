# wx.stopCompass
### wx.stopCompass(Object object)

停止监听罗盘数据

#### 参数

##### Object object

属性       | 类型       | 默认值 | 必填 | 说明                      
-------- | -------- | --- | -- | ------------------------
success  | function |     | 否  | 接口调用成功的回调函数             
fail     | function |     | 否  | 接口调用失败的回调函数             
complete | function |     | 否  | 接口调用结束的回调函数（调用成功、失败都会执行）

#### 示例代码

```js
wx.stopCompass()
```