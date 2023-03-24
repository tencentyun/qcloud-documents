# wx.startGyroscope
### wx.startGyroscope(Object object)

开始监听陀螺仪数据。

#### 参数

##### Object object

属性       | 类型       | 默认值    | 必填 | 说明                      
-------- | -------- | ------ | -- | ------------------------
interval | string   | normal | 否  | 监听陀螺仪数据回调函数的执行频率        
success  | function |        | 否  | 接口调用成功的回调函数             
fail     | function |        | 否  | 接口调用失败的回调函数             
complete | function |        | 否  | 接口调用结束的回调函数（调用成功、失败都会执行）

**object.interval 的合法值**

值      | 说明                        
------ | --------------------------
game   | 适用于更新游戏的回调频率，在 20ms/次 左右  
ui     | 适用于更新 UI 的回调频率，在 60ms/次 左右
normal | 普通的回调频率，在 200ms/次 左右