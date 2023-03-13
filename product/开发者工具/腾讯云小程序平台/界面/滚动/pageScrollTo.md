# wx.pageScrollTo
### wx.pageScrollTo(Object object)

将页面滚动到目标位置

#### 参数

##### Object object

属性        | 类型       | 默认值 | 必填 | 说明                      
--------- | -------- | --- | -- | ------------------------
scrollTop | number   |     | 是  | 滚动到页面的目标位置，单位 px        
duration  | number   | 300 | 否  | 滚动动画的时长，单位 ms           
success   | function |     | 否  | 接口调用成功的回调函数             
fail      | function |     | 否  | 接口调用失败的回调函数             
complete  | function |     | 否  | 接口调用结束的回调函数（调用成功、失败都会执行）

#### 示例代码

```js
wx.pageScrollTo({
  scrollTop: 0,
  duration: 300
})
```