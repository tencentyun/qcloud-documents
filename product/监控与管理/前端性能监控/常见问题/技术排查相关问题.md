[](id:que1)
### 代码中 `throw new Error` Aegis SDK 没有捕获到，如何处理？
在 VUE 框架中，Vue.config.errorHandler 会主动捕获错误，可以通过主动捕获再调用 aegis.error() 进行上报


### 接口请求报错 403 要怎么处理？

接口403一般是因为页面域名校验失败导致的，可以检查项目创建时候设置的域名跟实际上报的域名是否一致。如果项目不需要校验，域名可以填 `*`。
![](https://main.qcloudimg.com/raw/2f0d5075339146c01cf4e6a5571211bb.png)

>?如果不确定您的上报域名是什么的话，可以在浏览器控制台输入 `location.host` 查看。对于非 web 项目，默认填了 `*` 表示不需要校验。

用户在 RUM 上创建项目后，会得到一个长度为 18 位的字符串，这个字符串为上报 ID，new Aegis 的时候传入的 ID 就是这个上报 ID。如果这个 ID 不正确，也会报403。

**Aegis 初始化**

```
new` `Aegis({`` ``id: ``'pGUVFTCZyewhxxxxxx'``})
```

>? 如果项目刚刚创建，RUM 数据同步需要一定的时间，大概在1-2min。



[](id:que3)
### 日志里面的“图片加载失败”、“JS 加载失败”、“CSS 加载失败” 的问题如何查？

1. 自行访问一下这个资源看是否有异常情况。
2. 若访问正常，但是日志里面还是有比较多的异常情况。
3. 再查看一下这些异常是否有聚集的情况，例如区域聚集，运营商聚集等等。
4. 若没有发现有聚集的情况，那大概率是因为用户的网络问题导致的资源加载异常，可以尝试项目中接入 PWA 或者离线包来减少这类情况。本质上，前端没有办法完全避免这种情况。


[](id:que4)
### 项目接入 SDK 后，为什么会有一个 `aegis.qq.com/speed/webvitals` 的接口在页面刷新的时候 cancel ？
![](https://main.qcloudimg.com/raw/860c80768620582bbfd1b293c7732d05.png)

webvitals 中 CLS 的值必须是页面可见性改变的时候才计算的，用户刷新页面的时候，如果选中了 Preserve log，就会有一条请求处理发送中，但恰好被页面刷新给 cancel 掉，就出现这种情况。对用户和数据没有影响，可以忽略。

[](id:que5)
### 有不少错误日志是 “Script error. @ (:0:0) 没啥信息” 这种是第三方 JS 异常吗？可以通过配置过滤掉吗？
Script error. 也被称为跨域错误，当网站请求并且执行一个非本域名下的脚本的时候，如果跨域脚本发生错误，就有可能抛出这个错误。由于项目中，我们的脚本都是放在 CDN 上的，因此这种错误最为常见。

其实这并不是一个 JavaScript Bug。但出于安全考虑，浏览器会刻意隐藏其他域的 JS 文件抛出的具体错误信息，这样做可以有效避免敏感信息无意中被不受控制的第三方脚本捕获。因此浏览器只允许同域下的脚本捕获具体错误信息，而其他脚本只知道发生了一个错误，但无法获知错误的具体内容。更多信息，请参见 [Webkit源码](https://trac.webkit.org/browser/branches/chromium/648/Source/WebCore/dom/ScriptExecutionContext.cpp?spm=a2c63.p38356.879954.4.35155db7eUvHNi&file=ScriptExecutionContext.cpp#L294)。

![](https://main.qcloudimg.com/raw/4fc7d1569532435658dd6c5f07038073.png)

**具体解决方式：**
#### 解决办法1：CORS
步骤1：资源添加 crossorigin 属性
<dx-codeblock>
:::  js
<script src="http://another-domain.com/app.js" crossorigin="anonymous"></script>
:::
</dx-codeblock>

步骤2：CDN 添加 cors 响应头，这个基本是 cdn 默认的，所以实际上我们并不需要做什么。
```
Access-Control-Allow-Origin: *
```


#### 解决办法2: try catch
window.onerror 中只能捕获 `Script error.`，但是 try catch 中却能打印详细的错误栈。
```HTML
<!doctype html>
<html>
<body>
    <script src="http://another-domain.com/app.js"></script>
    <script>
        window.onerror = function (message, url, line, column, error) {
            console.log(message, url, line, column, error);
        }
        try {
            foo(); // 调用app.js中定义的foo方法
        } catch (e) {
            console.log(e);
            throw e; // 主动抛出的错误捕获后不是 Script error
        }
    </script>
</body>
</html>
```
如果不想解决，只想直接屏蔽，可以参考下一个问题，不上报特殊日志。

[](id:que6)
### 对于一些特殊的日志，不想上报到 RUM，可以怎处理？

SDK 提供一个 hook 来帮助用户在日志上报前对日志进行操作和限制，可以使用 `beforeReport`，返回 false 或者空值就可以不上报该条日志。

**beforeReport**
<dx-codeblock>
:::  JS
new Aegis({  id: 'pGUVFTCZyewhxxxxxx',
  beforeReport(log) {
    if (log.msg && log.msg.indexOf('Script error') !== -1) {
      return false
    }
    return log;
  }
})
:::
</dx-codeblock>

[](id:que7)
### SDK 如何获取网络类型？为什么我的网络类型不正确？

若 UA 里面有 NetType ，则 UA 是从 NetType 获取的。若没有，您用的是 `navigator.connection.effectiveType || navigator.connection.type`，`effectiveType`，则会根据您的网速推算出的一个类型，并不是实际类型。


[](id:que8)
### 为什么 SDK 上报的接口请求耗时跟 network 里面的时间不一致？

SDK 通过劫持 fetch 和 xhr 的方式实现对接口的测速，在请求前和请求后分别进行打点测速，因为 JS 计算时间差的逻辑依赖 js 主线程执行，如果 end 时间执行的时候有线程阻塞，会导致实际计算的时长要大于浏览器 network 时长。


[](id:que9)
### 为什么上报的网络类型跟实际网络类型不符合，例如当前用户使用的是 wifi，上报的却是 4G？

我们目前通过 UA 里面的 NetType 和 `navigator.connection.effectiveType` 获取网络类型，前者依赖浏览器注入网络信息到 UA，后者是浏览器提供的 “等效网络类型”，并不代表真实的网络类型。`navigator.connection.effectiveType` 这个 API 目前还存在兼容性问题，IOS 暂不支持，所以会被识别为未知。


[](id:que10)
### 我开启了 SPA 参数，但是页面之间跳转的时候，为什么没有上报页面性能呢？

SPA 页面之间的跳转，本质上只是一段 JS 代码的执行，首屏探测的是从用户浏览器发起请求到页面可见元素渲染完成的时间，因此没有办法计算首屏。


[](id:que11)
### 日志里面上报了非常多 AJAX 异常，状态码是 0 ，这个可能是什么原因导致的？
![](https://main.qcloudimg.com/raw/1665de72d9dc65ef469fe59d2da6c235.png)

HTTP 接口的 status 是 0，有以下几种可能：超时，abort，cancel，跨域。

#### 开发者本地调试可能没有发现这种错误，但是在用户侧却能经常发生，这个是什么原因呢？
因为用户侧可能随时离开页面，或者因为网络问题把某次 HTTP 请求中断了，这种情况就会发生 status 为 0 的情况。
虽然 status 为 0 有多种情况，但我们也可以根据日志里面的信息看出一些问题。例如上述截图里面的耗时都非常小，而且发生的用户比较集中，因此可以判断该接口是浏览器插件屏蔽掉了，这种情况常见于一些数据上报的接口。

如果看到 duration 非常长，那超时的可能性就比较大了，开发者也可以查看自己接口的超时时间来进行对比。至于跨域的情况，可以检查一下后台的业务逻辑是否正常，而 cancel 的情况，多半是前端业务控制的，也可以看下具体的业务逻辑。
