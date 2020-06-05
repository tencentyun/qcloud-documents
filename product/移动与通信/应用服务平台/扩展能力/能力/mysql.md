# MySQL

支持在云函数用使用MySQL。

## 前置要求
已经开通云开发。

## 功能特性

提供基于开源数据库 MySQL 专业打造的高性能分布式数据存储服务，让用户能够在云中更轻松地设置、操作和扩展关系数据库。

### 适用场景

云开发的数据库满足不了业务的需求，需要使用到MySQL。

已有的业务使用了MySQL，业务迁移到云开发中，希望继续使用MySQL。

## 安装程序
>! 微信小程序开发者请使用【其他登录方式】-【微信公众号登录】登录，再选择关联的小程序账户登录；QQ小程序开发者可直接通过QQ小程序开发者IDE【云开发】按钮登录，也可以通过关联的腾讯云账户登录。

您可以通过 [云开发控制台](https://console.cloud.tencent.com/tcb/add)，来安装和管理该能力。

## 使用程序

如果你的原有业务代码中使用了MySQL连接池，在云函数中可能就不需要连接池了，每个请求都会分发到不同的云函数实例中，通常情况下，一个云函数有一个MySQL连接就可以。

根据用户的实际情况，推荐使用[mysql](https://www.npmjs.com/package/mysql)和[serverless-mysql](https://www.npmjs.com/package/serverless-mysql)。

默认情况下，serverless-mysql是mysql的一个封装，它添加连接管理相关的功能，与MySQL Server只有一个连接；如果在云函数中需要使用连接池，推荐使用mysql。

使用serverless-mysql的时候，注意MySQL的max_user_connections和max_connections的配置。

**调用示例**

云函数中使用：

```javascript
'use strict';
const mysql = require('serverless-mysql')({
    config: {
        host: process.env.HOST,
        port: process.env.PORT,
        database: process.env.DATABASE,
        // 需要填写真实的用户名与密码
        user: 'xxx',
        password: 'xxx'
    }
})
exports.main = async (event, context, callback) => {
    let res
    try {
        res = await mysql.query('SELECT * FROM mysql_test')
    } catch (e) {
        console.error(e)
    }
    return {
        res,
        code: 200
    }
}
```


## 其它


###    云函数的运行机制

[深入理解云函数-云函数的运行机制](/cloud-function/deep-priciple.md)

###    私有网络VPC

在云函数中，开发者如果需要访问腾讯云的云数据库等资源，推荐使用私有网络来确保数据安全及连接安全。关于私有网络、以及如果建立私有网络和云函数加入私有网络，可以参考[为云数据库MySQL创建私有网络](https://cloud.tencent.com/document/product/236/8468)中的相关章节。


###    云函数并发数 & MySQL连接数

在[云开发控制台-环境总览](https://console.cloud.tencent.com/tcb/env/overview)中可以看到当前环境所允许的云函数并发数的最大值，最大并发数也是云函数的最大实例。

关于MySQL连接，推荐阅读MySQL官方博客的博文[MySQL Connection Handling and Scaling](https://mysqlserverteam.com/mysql-connection-handling-and-scaling/)。

MySQL连接数的相关参数配置，可以在[云数据库TencentDB](https://console.cloud.tencent.com/cdb)控制台 -> MySQL -> 数据库管理 -> 参数设置中配置。

云函数中使用MySQL，每个云函数实例与MySQL Server都会有连接，那么此云函数与MySQL的最大连接数是，单个实例的最大连接数*实际运行的最大并发数；在配置MySQL的max_connections的时候，此参数应该大于，使用此数据库的所有云函数的最大连接数之和。

因此，在云函数中使用MySQL，建议您将使用到同一个数据库，不仅仅是同一张表，的所有读写MySQL的代码集中到一个云函数中，这样做有两个好处

-   云函数出现冷启动的概率比较低
-   MySQL的最大连接数较小