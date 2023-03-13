# wx.setBackgroundTextStyle
### wx.setBackgroundTextStyle(Object object)


动态设置下拉背景字体、loading 图的样式

#### 参数

##### Object object

属性        | 类型       | 默认值 | 必填 | 说明                      
--------- | -------- | --- | -- | ------------------------
textStyle | string   |     | 是  | 下拉背景字体、loading 图的样式。    
success   | function |     | 否  | 接口调用成功的回调函数             
fail      | function |     | 否  | 接口调用失败的回调函数             
complete  | function |     | 否  | 接口调用结束的回调函数（调用成功、失败都会执行）

**object.textStyle 的合法值**

值     | 说明      
----- | --------
dark  | dark 样式 
light | light 样式

#### 示例代码

```js
wx.setBackgroundTextStyle({
  textStyle: 'dark' // 下拉背景字体、loading 图的样式为dark
})
```