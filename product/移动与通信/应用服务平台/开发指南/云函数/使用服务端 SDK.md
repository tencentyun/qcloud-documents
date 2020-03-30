在云函数中访问云开发的服务是以管理员的身份进行的，拥有不受限的数据库读写权限和云文件读写权限。

## Node.js云函数
### 安装 SDK
腾讯云入口环境创建的云函数：
```
npm install --save tcb-admin-node@latest
```
微信小程序入口环境创建的云函数：
```
npm install --save wx-server-sdk@latest
```
### 初始化 SDK
在调用 SDK 的各个方法前，需要先初始化：

**腾讯云入口**
```
   const tcb = require('tcb-admin-node')
    tcb.init({
        env: tcb.getCurrentEnv() //示例使用客户端所使用的环境ID，可以自由指定
    })

```


**微信小程序入口**
```
     const cloud = require('wx-server-sdk')
    cloud.init({
        env: cloud.DYNAMIC_CURRENT_ENV // 给定 DYNAMIC_CURRENT_ENV 常量：接下来的 API 调用都将请求到与该云函数当前所在环境相同的环境
    })
```


### 访问数据库服务
假设在数据库中已有一个 todos 集合，我们可以如下方式取得 todos 集合的数据： collection 上的 get 方法会返回一个 Promise，因此云函数会在数据库异步取完数据后返回结果

**腾讯云入口**
```
    const tcb = require('tcb-admin-node')
    tcb.init({
        env: tcb.getCurrentEnv() //示例使用客户端所使用的环境ID，可以手动指定
    })
    const db = tcb.database()
    exports.main = async (event, context) => {
        return db.collection('todos').get()
    }

```


**微信小程序入口**
```
	const cloud = require('wx-server-sdk')

    cloud.init({
    env: cloud.DYNAMIC_CURRENT_ENV
    })

    const db = cloud.database()
    exports.main = async (event, context) => {
        return db.collection('todos').get()
    }
```


### 访问文件存储服务
上传在云函数目录中包含的一个图片文件（demo.jpg）

**腾讯云入口**
```
    const tcb = require('tcb-admin-node')
    const fs = require('fs')
    const path = require('path')

    tcb.init({
        env: tcb.getCurrentEnv()
    })

    exports.main = async (event, context) => {
        const fileStream = fs.createReadStream(path.join(__dirname, 'demo.jpg'))
        return await tcb.uploadFile({
            cloudPath: 'demo.jpg',
            fileContent: fileStream,
        })
    }
```


**微信小程序入口**
```
    const cloud = require('wx-server-sdk')
    const fs = require('fs')
    const path = require('path')

    cloud.init({
        env: cloud.DYNAMIC_CURRENT_ENV
    })

    exports.main = async (event, context) => {
        const fileStream = fs.createReadStream(path.join(__dirname, 'demo.jpg'))
        return await cloud.uploadFile({
            cloudPath: 'demo.jpg',
            fileContent: fileStream,
        })
    }
```


### 调用其它云函数

**腾讯云入口**
```
    const tdb = require('tcb-admin-node')

    tcb.init({
        env: tcb.getCurrentEnv()
    })

    exports.main = async (event, context) => {
        return await tcb.callFunction({
            name: 'sum',
            data: {
                x: 1,
                y: 2,
            }
        })
    }
```


**微信小程序入口**
```
    const cloud = require('wx-server-sdk')

    cloud.init({
        env: cloud.DYNAMIC_CURRENT_ENV
    })

    exports.main = async (event, context) => {
        return await cloud.callFunction({
            name: 'sum',
            data: {
                x: 1,
                y: 2,
            }
        })
    }
```
