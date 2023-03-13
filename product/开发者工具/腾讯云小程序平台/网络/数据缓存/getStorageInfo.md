### wx.getStorageInfo(Object object)

异步获取当前storage的相关信息

#### 参数

##### Object object

属性       | 类型       | 默认值 | 必填 | 说明                      
-------- | -------- | --- | -- | ------------------------
success  | function |     | 否  | 接口调用成功的回调函数             
fail     | function |     | 否  | 接口调用失败的回调函数             
complete | function |     | 否  | 接口调用结束的回调函数（调用成功、失败都会执行）

###### object.success 回调函数

**参数**

**Object object**

属性          | 类型             | 说明                 
----------- | -------------- | -------------------
keys        | Array.\<string\> | 当前 storage 中所有的 key
currentSize | number         | 当前占用的空间大小, 单位 KB   
limitSize   | number         | 限制的空间大小，单位 KB      

#### 示例代码

```js
wx.getStorageInfo({
  success(res) {
    console.log(res.keys)
    console.log(res.currentSize)
    console.log(res.limitSize)
  }
})
```

```js
try {
  const res = wx.getStorageInfoSync()
  console.log(res.keys)
  console.log(res.currentSize)
  console.log(res.limitSize)
} catch (e) {
  // Do something when catch error
}
```