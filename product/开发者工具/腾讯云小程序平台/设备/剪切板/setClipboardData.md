# wx.setClipboardData
### wx.setClipboardData(Object object)


设置系统剪贴板的内容，对单个用户而言，每秒调用不超过`1`次。

#### 参数

##### Object object

属性       | 类型       | 默认值 | 必填 | 说明                      
-------- | -------- | --- | -- | ------------------------
data     | string   |     | 是  | 剪贴板的内容                  
success  | function |     | 否  | 接口调用成功的回调函数             
fail     | function |     | 否  | 接口调用失败的回调函数             
complete | function |     | 否  | 接口调用结束的回调函数（调用成功、失败都会执行）

#### 示例代码

```js
wx.setClipboardData({
  data: 'data',
  success(res) {
    wx.getClipboardData({
      success(res) {
        console.log(res.data) // data
      }
    })
  }
})
```