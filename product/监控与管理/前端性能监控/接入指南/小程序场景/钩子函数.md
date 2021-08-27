您可以使用钩子函数对某些资源的测速上报进行自定义配置，系统将会为您计算、统计函数执行时间等。您可以在 [自定义测速](https://console.cloud.tencent.com/rum/web/custom) 多维度分析函数执行耗时。

## beforeReport

1. 该钩子将会在日志上报（对应上报接口为 `/collect?`）前执行，例如：
<dx-codeblock>
:::  js
const aegis = new Aegis({
  id: 'pGUVFTCZyewxxxxx',
  beforeReport(log) {
  // 监听到下面抛出的错误
    console.log(log); // {level: "4", msg: "发生错误啦！！！！"}
    return log;
  }
});

throw new Error('发生错误啦！！！！');
:::
</dx-codeblock>
<dx-alert infotype="explain" title="">
上述 `log` 将会有以下几个字段：  
1. `level`: 日志等级，例如：当 level 为 `'4'` 时代表错误日志；  
2. msg`: 日志内容；
3. 全部日志等级如下：
- `{ level: '1', name: '接口请求日志（白名单日志）' }`
- `{ level: '2', name: '一般日志' }`
- `{ level: '4', name: 'JS 执行错误' }`
- `{ level: '8', name: 'Promise 错误' }`
- `{ level: '16', name: 'Ajax 请求异常' }`
- `{ level: '32', name: 'JS 加载异常' }`
- `{ level: '64', name: '图片加载异常' }`
- `{ level: '128', name: 'css 加载异常' }`
- `{ level: '256', name: 'console.error (未启用)' }`
- `{ level: '512', name: '音视频资源异常' }`
- `{ level: '1024', name: 'retcode 异常' }`
- `{ level: '2048', name: 'aegis report' `
</dx-alert>
2. 当该钩子返回 `false` 时，本条日志将不会进行上报，该功能可用来过滤某些不需要上报的错误，例如：
<dx-codeblock>
:::  js
const aegis = new Aegis({
  id: 'pGUVFTCZyewxxxxx',
  beforeReport(log) {
    if (log.level === '4' && log.msg && log.msg.indexOf('碍眼的错误') !== -1) {
      return false
    }
  }
});
throw new Error('碍眼的错误'); // 该错误将不会被上报
:::
</dx-codeblock>
上面例子中，当上报的错误内容包含 `碍眼的错误` 几个关键字时，将不会上报至 RUM 后台中。

## onReport

该钩子将在日志上报成功之后执行，用法类似 `beforeReport` 钩子，唯一不同点在于，该钩子接收到的所有参数都是已经上报完成的日志，而 `beforeReport` 钩子接收的参数是即将上报的日志。

## beforeReportSpeed

1. 该钩子将会在测速数据上报前被执行，例如：
<dx-codeblock>
:::  js
const aegis = new Aegis({
  id: 'pGUVFTCZyewxxxxx',
  reportApiSpeed: true,
  reportAssetSpeed: true,
  beforeReportSpeed(msg) {
    console.log(msg); // {url: "https://localhost:3001/example.e31bb0bc.js", method: "get", duration: 7.4, status: 200, type: "static"}
    return msg
  }
});
:::
</dx-codeblock>
<dx-alert infotype="explain" title="">
上述 `msg` 将会有以下几个字段：  
1. `url`: 该资源的请求地址；  
2. `type`: 该资源的类型，目前有 `fetch` 、 `static` 两种，当为 `fetch` 时，Aegis 将会把该资源当成 API 请求进行上报，`static` 时则视为静态资源；  
3. `duration`: 该资源请求耗时；  
4. `method`: 请求该资源时使用的 `http method`；  
5. `status`: 服务器返回状态码；  
</dx-alert>
上面的例子中，每当 Aegis 收集到一个资源的加载详情时，将会以该资源的加载情况（上面的返回的 <code>msg</code>）作为参数调用 <code>beforeReportSpeed</code> 钩子。  
2. 如果您配置了该钩子，**Aegis 最终的上报内容将以钩子的执行结果为准**。例如：
<dx-codeblock>
:::  js
const aegis = new Aegis({
  id: 'pGUVFTCZyewxxxxx',
  reportApiSpeed: true,
  reportAssetSpeed: true,
  beforeReportSpeed(msg) {
    msg.type = 'static';
  }
});
:::
</dx-codeblock>
上述代码中，将所有的 <code>msg.type</code> 设置为 <code>static</code>，这意味着所有的资源都将被当成静态资源进行上报，API 请求也将被报至静态资源中。  
3. 使用该钩子，您可以校准 Aegis 类型判断错误的请求。  
#### 示例
假如您有一条接口 `https://example.com/api`，该接口的响应头 `Content-Type` 为 `text/html`。正常情况下，RUM 会将该资源当成静态资源进行上报。但在您的业务中，该接口就必须视为 API 请求进行上报，您可以给 Aegis 配置如下钩子进行校正：
<dx-codeblock>
:::  js
const aegis = new Aegis({
  id: 'pGUVFTCZyewxxxxx',
  reportApiSpeed: true,
  reportAssetSpeed: true,
  beforeReportSpeed(msg) {
    if (msg.url === 'https://example.com/api') {
      msg.type = 'fetch';
    }
  }
});
:::
</dx-codeblock>
4. 您还可以屏蔽某些资源的测速上报，例如：
<dx-codeblock>
:::  js
const aegis = new Aegis({
  id: 'pGUVFTCZyewxxxxx',
  reportApiSpeed: true,
  reportAssetSpeed: true,
  beforeReportSpeed(msg) {
    // 地址中包含‘https://example.com/api’的都不上报
    if (msg.url.indexOf('https://example.com/api') !== -1) {
      // 返回 ‘false’ 将阻止本条测速日志的上报
      return false
    }
  }
});
:::
</dx-codeblock>

## beforeRequest

该钩子将会在日志上报前执行，例如：
<dx-alert infotype="notice" title="">
SDK 版本应大于等于 1.24.44。
</dx-alert>
<dx-codeblock>
:::  js
const aegis = new Aegis({
  id: 'pGUVFTCZyewxxxxx',
  beforeRequest: function(msg) {
    if (msg.logs && msg.logs.level === '4' && msg.logs.msg && msg.logs.msg.indexOf('碍眼的错误') !== -1) {
      return false
    }
    return msg;
  }
});
:::
</dx-codeblock>

其中，msg 将会有以下几个字段：

1. logType：日志类型，有以下值：
 - custom：自定义测速
 - event：自定义事件
 - log：日志
 - performance：页面测速
 - pv：页面PV
 - speed：接口和静态资源测速
 - vitals：web vitals
2. logs：上报的日志内容：
 - 当 logType 为 'custom' 时，logs 数据类型为 `{name: "白屏时间", duration: 3015.7000000178814, ext1: '', ext2: '', ext3: ''}`。
 - 当 logType 为 'event' 时，logs 数据类型为 `{name: "ios", ext1: "", ext2: "", ext3: ""}`。
 - 当 logType 为 'performance' 时，logs 数据类型为 `{contentDownload: 2, dnsLookup: 0, domParse: 501, firstScreenTiming: 2315, resourceDownload: 260, ssl: 4, tcp: 4, ttfb: 5}`。
 - 当 logType 为 'speed' 时，logs 数据类型为 `{connectTime: 0, domainLookup: 0, duration: 508.2, isHttps: true, method: "get", status: 200, type: "tatic", url: "https://xxxxxx", urlQuery: "max_age=1296000"}`。
 - 当 logType 为 'vitals' 时，logs 数据类型为 `{delta: 1100, entries: [PerformancePaintTiming], id: "v1-1629344653118-4916457684758", name: "CP", value: 1100}`。
 - 当 logType 为 'log' 时，logs 数据类型为 `{msg: "日志详情", level: '4', ext1: '', ext2: '', ext3: '', trace: ''}`。
<dx-alert infotype="explain" title="">
其中 level 枚举值如下

- `{ level: '1', name: '接口请求日志（白名单日志）' }`,
- `{ level: '2', name: '一般日志' }`,
- `{ level: '4', name: 'JS 执行错误' }`,
- `{ level: '8', name: 'Promise 错误' }`,
- `{ level: '16', name: 'Ajax 请求异常' }`,
- `{ level: '32', name: 'JS 加载异常' }`,
- `{ level: '64', name: '图片加载异常' }`,
- `{ level: '128', name: 'css 加载异常' }`,
- `{ level: '256', name: 'console.error (未启用)' }`,
- `{ level: '512', name: '音视频资源异常' }`,
- `{ level: '1024', name: 'retcode 异常' }`,
- `{ level: '2048', name: 'aegis report' `}


该钩子返回 false 时，本条日志将不会进行上报，该功能可用来过滤某些不需要上报的错误，可以用来过滤不希望上报的日志。
</dx-alert>

## afterRequest

该勾子将会在测速数据上报后被执行，例如：

<dx-alert infotype="notice" title="">
SDK 版本应大于等于 1.24.44。
</dx-alert>


<dx-codeblock>
:::  js
const aegis = new Aegis({
  id: "pGUVFTCZyewxxxxx",
  afterRequest: function(msg) {
    // {isErr: false, result: Array(1), logType: "log", logs: Array(4)}
    console.log(msg);
  }
});
:::
</dx-codeblock>

其中，msg 将会有以下几个字段：
1. isErr：请求上报接口是否错误。
2. result：上报接口的返回结果。
3. logs：上报的日志内容。
4. logType：日志类型，同 beforeRequest 中的 logType。
