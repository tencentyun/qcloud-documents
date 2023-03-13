# wx.getNetworkType
### wx.getNetworkType(Object object)

获取网络类型

#### 参数

##### Object object

属性       | 类型       | 默认值 | 必填 | 说明                      
-------- | -------- | --- | -- | ------------------------
success  | function |     | 否  | 接口调用成功的回调函数             
fail     | function |     | 否  | 接口调用失败的回调函数             
complete | function |     | 否  | 接口调用结束的回调函数（调用成功、失败都会执行）

###### object.success 回调函数

**参数**

**Object res**

属性          | 类型     | 说明  
----------- | ------ | ----
networkType | string | 网络类型

**res.networkType 的合法值**

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
wx.getNetworkType({
  success(res) {
    const networkType = res.networkType
  }
})
```