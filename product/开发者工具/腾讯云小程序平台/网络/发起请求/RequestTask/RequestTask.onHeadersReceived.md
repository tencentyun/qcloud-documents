# RequestTask.onHeadersReceived(function listener)

## 功能描述

监听 HTTP Response Header 事件。会比请求完成事件更早

## 参数

### function listener

HTTP Response Header 事件的监听函数

#### 参数

##### Object res

| 属性   | 类型   | 说明                                    |
| :----- | :----- | :-------------------------------------- |
| header | Object | 开发者服务器返回的 HTTP Response Header |