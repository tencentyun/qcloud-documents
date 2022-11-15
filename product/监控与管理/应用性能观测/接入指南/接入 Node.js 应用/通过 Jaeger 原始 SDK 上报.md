本文将为您介绍如何使用 Jaeger 原始 SDK 上报 Node.js 应用数据。

## 操作步骤

### 步骤1：获取接入点和 Token

进入 [应用性能观测控制台](https://console.cloud.tencent.com/apm)，进入**应用监控 > 应用列表**页面，单击**接入应用**，在接入应用时选择 Node.js 语言与 Jaeger 的数据采集方式。在选择接入方式步骤获取您的接入点和 Token，如下图所示：           

![img](https://main.qcloudimg.com/raw/d7d94913947d31edf70e85c6462c6bac.png)

### 步骤2：安装依赖
使用  npm 安装依赖
```
$ npm i jaeger-client
```

### 步骤3：引入 SDK 并且进行数据上报
1. 引入SDK，示例如下：
```
const initTracer = require('jaeger-client').initTracer;

// jaeger 配置
const config = {
    serviceName: 'service-name', // 服务名称，根据业务自行修改
    sampler: {
        type: 'const',
        param: 1,
    },
    reporter: {
        logSpans: true,
        collectorEndpoint: 'http://ap-guangzhou.apm.tencentcs.com:14268/api/traces', // 接入点，比前在应用性能监控获取的接入点多了 api/traces
    },
};

const options = {
    tags: {
        token: 'Vds************CrKck' // 业务申请的 token
    },
};
```

>? Node 使用 API 直接进行数据上报，因此不需要启动 Jaeger agent。接入点选择自己对应的网络环境，并且在后面加入 `/api/traces`  后缀即可。

2. 进行数据上报 ，示例如下：
```
// 初始化 tracer 实例对象
const tracer = initTracer(config, options);

// 初始化 span 实例对象
const span = tracer.startSpan('spanStart');

// 当前服务为 server
span.setTag('span.kind', 'server');

// 设置标签（可选，支持多个）
span.setTag('tagName', 'tagValue');

// 设置事件（可选，支持多个）
span.log({ event: 'timestamp', value: Date.now() });

// 标记Span结束
span.finish();
```
