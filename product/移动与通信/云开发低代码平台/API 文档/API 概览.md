通过 API ，您可以拿到当前应用的数据和常见的工具库、可以调用云函数、可以直接在低码编辑器中直接使用 API 等，增加编写程序的扩展性、便利性。

## 界面交互相关接口

| 接口名称   | 接口功能   |
| -------- | -------- |
| [showToast](https://cloud.tencent.com/document/product/1301/56701#showToast)    | 显示提示框   |
| [showLoading](https://cloud.tencent.com/document/product/1301/56701#showLoading)    | 显示 loading 提示框  |
| [hideLoading](https://cloud.tencent.com/document/product/1301/56701#hideLoading)   | 隐藏 loading 提示框   |
| [showModal](https://cloud.tencent.com/document/product/1301/56701#showModal) | 显示模态对话框   |

## 工具相关接口
| 接口名称   | 接口功能   |
| -------- | -------- |
| [utils.get](https://cloud.tencent.com/document/product/1301/56702#get)    | 根据 object 对象的 path 路径获取值   |
| [utils.set](https://cloud.tencent.com/document/product/1301/56702#set)    | 设置 object 对象中对应 path 属性路径上的值  |
| [utils.formatDate](https://cloud.tencent.com/document/product/1301/56702#formatDate)   |格式化日期函数   |

## 路由相关接口
| 接口名称   | 接口功能   |
| -------- | -------- |
| [navigateTo](https://cloud.tencent.com/document/product/1301/56703#navigateTo)    | 保留当前页面，跳转到应用内的某个页面   |
| [redirectTo](https://cloud.tencent.com/document/product/1301/56703#redirectTo)    | 关闭当前页面，跳转到应用内的某个页面  |
| [reLaunch](https://cloud.tencent.com/document/product/1301/56703#reLaunch)   |关闭所有页面，打开到应用内的某个页面   |
| [navigateBack](https://cloud.tencent.com/document/product/1301/56703#navigateBack)   |关闭所有页面，打开到应用内的某个页面    |

## 数据源相关接口
| 接口名称   | 接口功能   |
| -------- | -------- |
| [cloud.dataSources](https://cloud.tencent.com/document/product/1301/56704#dataSources)    | 获取当前应用所绑定的所有数据源   |

## 平台相关接口
| 接口名称   | 接口功能   |
| -------- | -------- |
| [platform](https://cloud.tencent.com/document/product/1301/56705#platform)    | 获取当前平台   |
