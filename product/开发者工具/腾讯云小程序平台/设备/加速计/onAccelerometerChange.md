# wx.onAccelerometerChange
### wx.onAccelerometerChange(function callback)

监听加速度数据事件。频率根据 [wx.startAccelerometer()](./startAccelerometer.md) 的 interval 参数。可使用 [wx.stopAccelerometer()](./stopAccelerometer.md) 停止监听。

#### 参数

##### function callback

加速度数据事件的回调函数

###### 参数

**Object res**

属性 | 类型     | 说明 
-- | ------ | ---
x  | number | X 轴
y  | number | Y 轴
z  | number | Z 轴

#### 示例代码

```js
wx.onAccelerometerChange(function (res) {
  console.log(res.x)
  console.log(res.y)
  console.log(res.z)
})
```