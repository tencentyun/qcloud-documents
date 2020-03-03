TCB-router 是基于 koa 风格的小程序·云开发云函数轻量级类路由库，主要用于优化服务端函数处理逻辑。
## 云函数端
### 安装 TCB-router
```
npm install --save tcb-router
```

```
// 云函数的 index.js
const TcbRouter = require('./router');

exports.main = (event, context) => {
    const app = new TcbRouter({ event });
  
    // app.use 表示该中间件会适用于所有的路由
    app.use(async (ctx, next) => {
        ctx.data = {};
        await next(); // 执行下一中间件
    });

    // 路由为数组表示，该中间件适用于 user 和 timer 两个路由
    app.router(['user', 'timer'], async (ctx, next) => {
        ctx.data.company = 'Tencent';
        await next(); // 执行下一中间件
    });

    // 路由为字符串，该中间件只适用于 user 路由
    app.router('user', async (ctx, next) => {
        ctx.data.name = 'heyli';
        await next(); // 执行下一中间件
    }, async (ctx, next) => {
        ctx.data.sex = 'male';
        await next(); // 执行下一中间件
    }, async (ctx) => {
        ctx.data.city = 'Foshan';
        // ctx.body 返回数据到小程序端
        ctx.body = { code: 0, data: ctx.data};
    });

    // 路由为字符串，该中间件只适用于 timer 路由
    app.router('timer', async (ctx, next) => {
        ctx.data.name = 'flytam';
        await next(); // 执行下一中间件
    }, async (ctx, next) => {
        ctx.data.sex = await new Promise(resolve => {
        // 等待500ms，再执行下一中间件
        setTimeout(() => {
            resolve('male');
        }, 500);
        });
        await next(); // 执行下一中间件
    }, async (ctx)=>  {
        ctx.data.city = 'Taishan';

        // ctx.body 返回数据到小程序端
        ctx.body = { code: 0, data: ctx.data };
    });

    return app.serve();

}
```

>?小程序云函数的 node 环境默认支持 async/await 语法，推荐涉及到的异步操作时，同 demo 使用方法一致。

## 小程序端
```
// 调用名为 router 的云函数，路由名为 user
wx.cloud.callFunction({
    // 要调用的云函数名称
    name: "router",
    // 传递给云函数的参数
    data: {
        $url: "user", // 要调用的路由的路径，传入准确路径或者通配符*
        other: "xxx"
    }
});
```

## 接口
### 构造函数
#### 参数
Object，存入云函数的 event 参数
#### 示例
```
const TcbRouter = require('./router');
exports.main = (event, context) => {
    const app = new TcbRouter({ event });
};
```

### app.use
#### 参数
Function，应用于所有路由的中间件
#### 示例
```
app.router(['user', 'timer'], async (ctx, next) => {
    ctx.data = {}；
    ctx.data.company = 'Tencent';
    await next(); // 执行下一中间件
});

// 路由为字符串，该中间件只适用于 user 路由
app.router('user', async (ctx, next) => {
    ctx.data.name = 'heyli';
    ctx.body = {code: 0, data: ctx.data}; // 将数据返回给云函数，用ctx.body
});
```

### app.router
#### 参数
- Array|String，路由或路由数组
- Function，应用于对应路由的中间件


#### 示例
```
app.router(['user', 'timer'], async (ctx, next) => {
    ctx.data = {}；
    ctx.data.company = 'Tencent';
    await next(); // 执行下一中间件
});

// 路由为字符串，该中间件只适用于 user 路由
app.router('user', async (ctx, next) => {
    ctx.data.name = 'heyli';
    ctx.body = {code: 0, data: ctx.data}; // 将数据返回给云函数，用ctx.body
});
```



### 测试
```
npm run test
```


