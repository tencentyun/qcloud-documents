# wx.onCompassChange
### wx.onCompassChange(function callback)

监听罗盘数据变化事件。频率：5 次/秒，接口调用后会自动开始监听，可使用 wx.stopCompass 停止监听。

#### 参数

##### function callback

罗盘数据变化事件的回调函数

###### 参数

**Object res**

属性        | 类型            | 说明      | 最低版本                                                                                                              
--------- | ------------- | ------- | ------------------------------------------------------------------------------------------------------------------
direction | number        | 面对的方向度数 |                                                                                                                   
accuracy  | number/string | 精度      | 

#### 示例代码

```javascript
wx.onCompassChange(function (res) {
  console.log(res.direction)
})
```

#### accuracy 在 iOS/Android 的差异

由于平台差异，accuracy 在 iOS/Android 的值不同。

* iOS：accuracy 是一个 number 类型的值，表示相对于磁北极的偏差。0 表示设备指向磁北，90 表示指向东，180 表示指向南，依此类推。
* Android：accuracy 是一个 string 类型的枚举值。

值               | 说明                                                 
--------------- | ---------------------------------------------------
high            | 高精度                                                
medium          | 中等精度                                               
low             | 低精度                                                
no-contact      | 不可信，传感器失去连接                                        
unreliable      | 不可信，原因未知                                           
unknow ${value} | 未知的精度枚举值，即该 Android 系统此时返回的表示精度的 value 不是一个标准的精度枚举值