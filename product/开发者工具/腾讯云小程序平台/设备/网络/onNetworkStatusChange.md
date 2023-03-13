# wx.onNetworkStatusChange
### wx.onNetworkStatusChange(function callback)


监听网络状态变化事件

#### 参数

##### function callback

网络状态变化事件的回调函数

###### 参数

**Object res**

属性          | 类型      | 说明       
----------- | ------- | ---------
isConnected | boolean | 当前是否有网络连接
networkType | string  | 网络类型     

**networkType 的合法值**

值       | 说明               
------- | -----------------
wifi    | wifi 网络          
2g      | 2g 网络            
3g      | 3g 网络            
4g      | 4g 网络            
unknown | Android 下不常见的网络类型
none    | 无网络              

#### 示例代码

```js
wx.onNetworkStatusChange(function (res) {
  console.log(res.isConnected)
  console.log(res.networkType)
})
```