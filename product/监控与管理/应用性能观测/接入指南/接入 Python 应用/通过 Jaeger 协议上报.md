本文将为您介绍如何使用 Jaeger 协议上报 Python 应用数据。

## 操作步骤


### 步骤1：获取接入点和 Token

进入 [应用性能观测控制台](https://console.cloud.tencent.com/apm) **应用监控** > **应用列表**页面，单击**接入应用**，在接入应用时选择  Python  语言与 Jaeger 协议的数据采集方式。在选择接入方式步骤获取您的接入点和 Token，如下图所示：
![](https://main.qcloudimg.com/raw/d7d94913947d31edf70e85c6462c6bac.png)

### 步骤2：安装 Jaeger Agent

1. 下载官方 [Jaeger Agent](https://github.com/jaegertracing/jaeger/releases/tag/v1.22.0)。
2. 执行下列命令启动 Agent。
<dx-codeblock>
:::  sh
nohup ./jaeger-agent --reporter.grpc.host-port={{接入点}} --jaeger.tags=token={{token}}
:::
</dx-codeblock>

### 步骤3：通过  Jaeger 上报数据


1. 执行下列命令安装 jaeger_client 包。
<dx-codeblock>
:::  sh
pip install jaeger_client
:::
</dx-codeblock>
2. 创建如下 Python 文件和 Tracer 对象，跟踪所有的 Request。
<dx-codeblock>
::: Python
from jaeger_client import Config
import time
from os import getenv

# 配置jaeger代理的地址，默认本机localhost
JAEGER_HOST = getenv('JAEGER_HOST', 'localhost')
SERVICE_NAME = getenv('JAEGER_HOST', 'my_service_test')


def build_your_span(tracer):
    with tracer.start_span('yourTestSpan') as span:
        span.log_kv({'event': 'test your message', 'life': 42})
        span.set_tag("span.kind", "server")
        return span


def build_your_tracer():
    my_config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'local_agent': {
                'reporting_host': JAEGER_HOST,
                'reporting_port': 6831,
            },
            'logging': True,
        },
        service_name=SERVICE_NAME,
        validate=True
    )
    tracer = my_config.initialize_tracer()

    return tracer


if __name__ == "__main__":
    tracer = build_your_tracer()
    span = build_your_span(tracer)
    time.sleep(2)
    tracer.close()
:::
</dx-codeblock>
<dx-alert infotype="explain" title="">
目前 Jaeger 支持 Flask、Django 和 Grpc 等框架进行上报，更多请参见：
- [jaeger-client-python](https://github.com/jaegertracing/jaeger-client-python)
- [OpenTracing API Contributions](https://github.com/opentracing-contrib?q=python&type=&language=&sort=)
</dx-alert>









