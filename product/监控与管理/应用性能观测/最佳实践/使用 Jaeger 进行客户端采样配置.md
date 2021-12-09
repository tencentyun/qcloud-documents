本文将为您介绍如何使用 Jaeger 进行客户端采样配置。


## 操作背景

在访问量较大时，全链路数据上报可能会导致使用应用性能观测的成本较高。在访问量级较大的情况下，往往会进行数据采样。
<dx-alert infotype="explain" title="">
采样指从全量采集的所有链路数据中，采集部分数据进行分析，减少上报数量和链路存储费用，降低使用应用性能观测的成本。
</dx-alert>

## 采样解析
以一个简单的调用关系为例：A > B > C（ A 服务调用 B 服务，同时，B 服务调用 C 服务）。如果 A 服务被调用的时候没有收到任何追踪信息，A 服务的 Jaeger 库就会创建一个新的追踪(Trace)，分配一个 Trace ID，并根据采样配置决策是否需要保存这次追踪。采样配置决策与请求一起传递到 B 服务和 C 服务，因此我们只需要在 A 服务进行采样配置即可。

## 操作步骤

### 采样策略

Jaeger客户端支持4种采样策略，分别是：

- **Constant (sampler.type=const) ：**采样率的可设置的值为 0 和 1，分别表示关闭采样和全部采样
- **Probabilistic (sampler.type=probabilistic) ：**按照概率采样，取值可在 0 至 1 之间，例如：设置为 0.5 ，表示对 50% 的请求采样。
- **Rate Limiting (sampler.type=ratelimiting)：**设置每秒的采样次数上限 。 例如当 `sampler.param = 2.0` 时，它将以每秒 2条链路对请求进行采样。
- **Remote (sampler.type=remote)：** 默认策略。 采样遵循远程设置，取值的含义和  probabilistic 相同，都意为采样的概率，但是设置为 remote 后，Client 会从 Jaeger Agent 中动态获取采样率设置。 为了最大程度地减少开销，**Jaeger 默认采用 0.1% 的采样策略采集数据 (1000次里面采集1次)**。


### Java 示例

1. 将 Jaeger 库添加到依赖项中。
<dx-codeblock>
::: java
<dependency>
  <groupId>io.jaegertracing</groupId>
  <artifactId>jaeger-client</artifactId>
  <version>0.32.0</version>
</dependency>
:::
</dx-codeblock>

2. 代码示例如下。
<dx-codeblock>
::: java
import io.jaegertracing.Configuration;
import io.jaegertracing.Configuration.ReporterConfiguration;
import io.jaegertracing.Configuration.SamplerConfiguration;
import io.jaegertracing.internal.JaegerTracer;
import io.jaegertracing.internal.samplers.ConstSampler;
import io.opentracing.Span;
import io.opentracing.util.GlobalTracer;

...

SamplerConfiguration samplerConfig = SamplerConfiguration.fromEnv()
  .withType(ConstSampler.TYPE)
  .withParam(1);

ReporterConfiguration reporterConfig = ReporterConfiguration.fromEnv()
  .withLogSpans(true);

Configuration config = new Configuration("helloWorld")
  .withSampler(samplerConfig)
  .withReporter(reporterConfig);

GlobalTracer.register(config.getTracer());

...
Span parent = GlobalTracer.get().buildSpan("hello").start();
try (Scope scope = GlobalTracer.get().scopeManager()
      .activate(parent)) {
    Span child = GlobalTracer.get().buildSpan("world")
            .asChildOf(parent).start();
    try (Scope scope = GlobalTracer.get().scopeManager()
       .activate(child)) {
    }
}
:::
</dx-codeblock>

### GO 示例

<dx-codeblock>
::: java
import (
    "github.com/opentracing/opentracing-go"
    "github.com/uber/jaeger-client-go"
    "github.com/uber/jaeger-client-go/config"
)

...

func main() {
    ...
    cfg := config.Configuration{
	Sampler: &config.SamplerConfig{
	    Type:  "const",
	    Param: 1,
	},
	Reporter: &config.ReporterConfig{
	    LogSpans:            true,
	    BufferFlushInterval: 1 * time.Second,
	},
    }
    tracer, closer, err := cfg.New(
        "your_service_name",
        config.Logger(jaeger.StdLogger),
    )
    opentracing.SetGlobalTracer(tracer)
    defer closer.Close()

    someFunction()
    ...
}

...

func someFunction() {
    parent := opentracing.GlobalTracer().StartSpan("hello")
    defer parent.Finish()
    child := opentracing.GlobalTracer().StartSpan(
	"world", opentracing.ChildOf(parent.Context()))
    defer child.Finish()
}
:::
</dx-codeblock>

<dx-alert infotype="explain" title="">
更多语言采样说明请参见 [Client Library Features](https://www.jaegertracing.io/docs/1.27/client-features)。
</dx-alert>



