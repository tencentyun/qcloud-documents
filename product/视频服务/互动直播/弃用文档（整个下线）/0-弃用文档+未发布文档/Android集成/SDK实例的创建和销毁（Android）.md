## 一. AVContext 介绍
在启动AVSDK之前，需要创建一个AVContext（SDK上下文）对象。AVContext管理着SDK内部线程以及运行的上下文。可以认为， AVContext对象代表着一个SDK运行实例。在大多数情况下，应用程序只需要创建唯一一个 AVContext对象即可使用SDK的所有功能。
注意：创建的时候，必须保证AVContext实例的唯一性，同时创建多个AVContext实例可能会因为设备占用等方面的原因，出现无法预料的结果。
## 二. AVContext的创建和销毁
###  1. 创建AVContext
创建上下文有以下两个步骤：
(1)通过Config配置AVContext的参数
(2)根据参数创建AVContext

**接口描述：**
![接口描述](//mccdn.qcloud.com/static/img/fbd0e60943c197de706da2c622008df9/image.png)

**示例代码**（参数为模拟参数，真实的参数需要在Server端获取）：
![示例代码](//mccdn.qcloud.com/static/img/bf6b0411b3cccc11cb73e58604ac4237/image.png)
### 2. 销毁AVContext
(1)销毁目前的AVContext对象，必须要在调用createContext后才能使用，建议在stop()异步回调后调用。
(2)销毁后要把AVContext对象置为空。

**接口描述：**
![接口描述](//mccdn.qcloud.com/static/img/010cdc1f978fd55e19eb5e881fc4f1b5/image.png)

**示例代码：**
![](//mccdn.qcloud.com/static/img/f2a022be50f705449f8901ed19611ec6/image.png)
## 三. AVContext的启动和终止
### 1. 启动AVContext
启动上下文分为以下两个步骤：
#### （1）登录IMSDK
登录所需配置参数与创建AVContext时的一样。
 ![登录IMSDK](//mccdn.qcloud.com/static/img/eed1f82d0d94a751859b7ffed64577b7/image.png)
 
#### （2） 启动AVContext

**接口描述：**
 ![接口描述](//mccdn.qcloud.com/static/img/bcdb258a321f0a3cc76fda78f3c82660/image.png)
 
**示例代码：**
 ![示例代码](//mccdn.qcloud.com/static/img/6ae61b457e50813914adac4435190aab/image.png)
### 2. AVContext的终止
终止目前的AVContext对象后，必须要手动销毁AVContext对象，即调用destroy，并将该对象置为null。

**接口描述：**
 ![接口描述](//mccdn.qcloud.com/static/img/3fd19b52486e51581b2bf29152ae99b6/image.png) 

**示例代码：**
 ![示例代码](//mccdn.qcloud.com/static/img/19fdda74630245a84fbee33bc484fb42/image.png)
