本文将为您介绍如何使用 Jaeger 协议上报 C++ 应用数据。

## 操作步骤

### 步骤1：获取接入点和Token

进入 [应用性能观测控制台](https://console.cloud.tencent.com/apm) **应用监控** > **应用列表**页面，单击**接入应用**，在接入应用时选择 C++ 语言与 Jaeger 协议的数据采集方式。
在选择接入方式步骤获取您的接入点和 Token，如下图所示：
![](https://main.qcloudimg.com/raw/d7d94913947d31edf70e85c6462c6bac.png)

### 步骤2：下载 Jaeger Client

单击下载 [Jaeger Client](https://github.com/jaegertracing/jaeger-client-cpp?spm=a2c63.p38356.879954.9.4e9d6e24pPRWHz)。


###  步骤3：上报 C++ 应用数据
通过 Jaeger 协议上报 C++ 应用数据：
1. 配置 Jaeger，创建 Trace 对象，示例如下：
<dx-codeblock>
:::  c ++
void setUpTracer(const char* configFilePath)
{
  //导入配置文件
    auto configYAML = YAML::LoadFile(configFilePath);
    auto config = jaegertracing::Config::parse(configYAML);
  //设置trace的服务名
    auto tracer = jaegertracing::Tracer::make(
        "example-service", config, jaegertracing::logging::consoleLogger());
  //设置tracer为全局变量，之后会用到
    opentracing::Tracer::InitGlobal(
        std::static_pointer_cast<opentracing::Tracer>(tracer));
}
:::
</dx-codeblock>
YAML 配置参考：
<dx-codeblock>
:::  YAML
disabled: false
reporter:
    localAgentHostPort: 127.0.0.1:6831 //上报地址
    logSpans: true
sampler:	  	//采样策略
  type: const
  param: 1
:::
</dx-codeblock>
2. 开始一个 span 。开始一个 span 有多种方法，下面介绍常用的两种：
	- 方法一：
<dx-codeblock>
:::  c++
//开始一个 span，并设置设置 operationName
void tracedFunction()
{
    auto span = opentracing::Tracer::Global()->StartSpan("tracedFunction");
    tracedSubroutine(span);
}
:::
</dx-codeblock>
	- 方法二：
<dx-codeblock>
:::  c++
//设置 operationName，尝试在 ctx 中查找一个 span 作为父节点
void tracedSubroutine(const std::unique_ptr<opentracing::Span>& parentSpan)
{
    auto span = opentracing::Tracer::Global()->StartSpan(
        "tracedSubroutine", { opentracing::ChildOf(&parentSpan->context()) });
}
:::
</dx-codeblock>
完整代码：
<dx-codeblock>
:::  c++
int main(int argc, char* argv[])
{
  	//传入参数 config 的地址
    if (argc < 2) {
        std::cerr << "usage: " << argv[0] << " <config-yaml-path>\n";
        return 1;
    }
    setUpTracer(argv[1]);
    tracedFunction();
  	//关闭tracer
    opentracing::Tracer::Global()->Close();
    return 0;
}
:::
</dx-codeblock>

