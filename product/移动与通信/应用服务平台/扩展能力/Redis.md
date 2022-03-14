云开发支持在云函数内使用 Redis。

## 前置要求

已经开通 [云开发](https://console.cloud.tencent.com/tcb/env/index)。

## 功能特性

提供兼容 Redis 协议的缓存数据库，具备高可用、高可靠、高弹性等特征。

#### 适用场景

- 云开发的数据库满足不了业务的需求，需要使用到 Redis。
- 已有的业务使用了 Redis，业务迁移到云开发中，希望继续使用 Redis。

## 安装程序

您可以通过 [云开发控制台](https://console.cloud.tencent.com/tcb/extensions)，来安装和管理该能力。

> ! 
>
> - 微信小程序开发者请使用**其他登录方式** > **微信公众号登录**登录，选择关联的小程序账户登录。
> - QQ 小程序开发者可直接通过 QQ 小程序开发者 IDE**云开发**登录，也可以通过关联的腾讯云账户登录。

## 使用程序

根据实际情况，推荐使用 [redis](https://www.npmjs.com/package/redis) 或 [ioredis](https://www.npmjs.com/package/ioredis)。

#### 调用示例

调用示例如下：

```javascript
'use strict';

const redis = require('redis')

let client = redis.createClient({
    host: process.env.HOST,
    port: process.env.PORT,
    // 需要填写真实的密码
    password: 'xxx'
})

exports.main = async (event, context, callback) => {

    let res = await new Promise((resolve, reject) => {
        client.get('test', function (err, reply) {
            if (err) {
                resolve({
                    err
                })
            }
            resolve({
                data: reply.toString()
            }）
        })
    })

    return {
        res
    }
}

```

## 其它

### 云函数的运行机制

云函数的运行机制，请参考 [深入理解云函数](https://cloud.tencent.com/document/product/876/41764)。

### 私有网络

在云函数中，开发者如果需要访问腾讯云的 Redis 等资源，推荐使用私有网络来确保数据及连接安全。关于私有网络、如何建立私有网络以及云函数加入私有网络的详细信息，请参考 [云数据库 Redis 配置网络](https://cloud.tencent.com/document/product/239/30910) 中的相关章节。

### 云函数并发数

在 [云开发控制台-环境总览](https://console.cloud.tencent.com/tcb/env/overview) 中可以看到当前环境所允许的云函数并发数的最大值，最大并发数也是云函数的最大实例数。

### Redis 连接数
Redis 连接数的配置参数`maxclients`，默认是10000，可前往 [Redis 控制台](https://console.cloud.tencent.com/redis) 修改。
>?关于 Redis 连接，推荐阅读 Redis 官方博客的博文 [Redis Clients Handling](https://redis.io/topics/clients)。

- 在云函数中使用 Redis 时，每个云函数实例与 Redis Server 都会有连接，那么此云函数与 Redis 的最大连接数是：`单个实例的最大连接数 \* 实际运行的最大并发数`。
- 在配置 Redis 的 `maxclients` 的时候，此参数应该大于使用此数据库的所有云函数的最大连接数之和。
- 在云函数中使用 Redis，建议您将使用到同一个 Redis 实例的所有读写 Redis 的代码集中到一个云函数中，这样做有两个好处：
 - 云函数出现冷启动的概率比较低。
 - Redis 的最大连接数较小，减少连接数多内存的占用。
