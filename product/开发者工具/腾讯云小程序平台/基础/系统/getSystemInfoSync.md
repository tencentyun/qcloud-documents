# getSystemInfoSync

#### 功能描述

[wx.getSystemInfo](./getSystemInfo.md) 的同步版本

#### 返回值

##### Object res

属性                          | 类型      | 说明                                                                                  | 最低版本                                                                                                              
--------------------------- | ------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------
brand                       | string  | 设备品牌                                                                                | 
model                       | string  | 设备型号                                                                                |                                                                                                                   
pixelRatio                  | number  | 设备像素比                                                                               |                                                                                                                   
screenWidth                 | number  | 屏幕宽度，单位px                                                                           | 
screenHeight                | number  | 屏幕高度，单位px                                                                           | 
windowWidth                 | number  | 可使用窗口宽度，单位px                                                                        |                                                                                                                   
windowHeight                | number  | 可使用窗口高度，单位px                                                                        |                                                                                                                   
statusBarHeight             | number  | 状态栏的高度，单位px                                                                         |
language                    | string  | 语言                                                                             |                                                                                                                   
version                     | string  | 版本号                                                                               |                                                                                                                   
system                      | string  | 操作系统及版本                                                                             |                                                                                                                   
platform                    | string  | 客户端平台                                                                               |                                                                                                                   
SDKVersion                  | string  | 客户端基础库版本                                                                            | 
AppPlatform                 | string  | App平台                                   |
safeArea                    | Object  | 在竖屏正方向下的安全区域                                                                            | 
theme                       | string  | 系统当前主题，取值为light或dark，全局配置"darkmode":true时才能获取，否则为undefined |


**res.safeArea 的结构**

属性                         | 类型     | 说明                                                                                                                                                                                             
--------------------------- | -------- | ----------------------------------------------------------------------------------- |
left                        | number  | 安全区域左上角横坐标 
right                       | number  | 安全区域右下角横坐标  
top                         | number  | 安全区域左上角纵坐标
bottom                      | number  | 安全区域右下角纵坐标
width                       | number  | 安全区域的宽度，单位逻辑像素
height                      | number  | 安全区域的高度，单位逻辑像素      



#### 示例代码

```js
wx.getSystemInfo({
  success(res) {
    console.log(res.model)
    console.log(res.pixelRatio)
    console.log(res.windowWidth)
    console.log(res.windowHeight)
    console.log(res.language)
    console.log(res.version)
    console.log(res.platform)
  }
})
```

```js
try {
  const res = wx.getSystemInfoSync()
  console.log(res.model)
  console.log(res.pixelRatio)
  console.log(res.windowWidth)
  console.log(res.windowHeight)
  console.log(res.language)
  console.log(res.version)
  console.log(res.platform)
} catch (e) {
  // Do something when catch error
}
```