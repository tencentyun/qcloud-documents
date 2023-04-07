# wx.getLogManager
#### [LogManager](../debug/LogManager/LogManager.md) wx.getLogManager(Object object)

获取日志管理器对象。

#### 参数

##### Object object

属性    | 类型     | 默认值 | 必填 | 说明                                                                         | 最低版本                                                                                                              
----- | ------ | --- | -- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------
level | number | 0   | 否  | 取值为0/1，取值为0表示是否会把 `App`、`Page` 的生命周期函数和命名空间下的函数调用写入日志，取值为1则不会。默认值是 0 | 

#### 返回值

##### [LogManager](../debug/LogManager/LogManager.md)

#### 示例代码

```js
const logger = wx.getLogManager({level: 1})
logger.log({str: 'hello world'}, 'basic log', 100, [1, 2, 3])
logger.info({str: 'hello world'}, 'info log', 100, [1, 2, 3])
logger.debug({str: 'hello world'}, 'debug log', 100, [1, 2, 3])
logger.warn({str: 'hello world'}, 'warn log', 100, [1, 2, 3])
```