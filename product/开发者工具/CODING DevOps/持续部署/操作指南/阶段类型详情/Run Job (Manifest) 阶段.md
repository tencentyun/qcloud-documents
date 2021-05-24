本文为您详细介绍 CODING 持续部署中部署流程中的 Run Job (Manifest) 阶段。

## 前提条件

使用 CODING 持续部署的前提是，您的腾讯云账号需要开通 CODING DevOps 服务，详情请参见 [开通服务](https://cloud.tencent.com/document/product/1159/44859)。 

## 进入项目

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击团队域名进入 CODING 使用页面。
2. 单击工作台首页左侧的 <img src ="https://main.qcloudimg.com/raw/12230547b45d5eae85ad1c4fa86fba68.png" style ="margin:0" data-nonescope="true">，进入持续部署控制台。

Run Job(Manifest) 阶段将运行一个 Kubernetes Job 作为部署流程的一部分。

### 查看执行日志

对于 `job` 类型的 Kubernetes 对象，日志显得尤其重要。考虑到 CODING 持续部署的用户对 Kubernetes 的理解程度有所不同，我们提供了两种获取和查看日志的方式。

### 将日志链接到外部系统

大多数 Kubernetes 部署过程都支持将日志从容器转发到外部系统以方便做日志分析。如果您也使用了这类日志平台，可以给`Job`配置注解 `job.spinnaker.io/logs`以及日志系统的模板化 URL，注解的值将在 UI 界面中渲染成链接地址。

为了让查找`Job`更简单，注解值支持模板变量。模板变量在注解中以`{{ templateKey }}`格式使用，`templateKey`根据不同的资源类型有不同的取值范围。已部署的 manifest 将会以 JSON 格式传入模板。

例如，假设您部署了名为 `myjob-12345` 的 `Job`，并使用了注解：

```shell
job.spinnaker.io/logs: 'https://internal-logging/jobs/{{ manifest.metadata.name }}'
```

注解内容将会被解析为：

```URL
https://internal-logging/jobs/myjob-12345
```

### 在 CODING 部署控制台查看日志

除了将日志发送给外部系统，您也可以在 CODING 部署控制台中查看`Job`日志。CODING 部署控制台可以直接获取`Job`信息和日志并在 UI 界面展示。这些日志只在`Job`部署完成后保留一小段时间，因为 Kubernetes 针对对象的事件也只会保留一小段时间。如果需要将日志保留更长的时间，推荐您使用类似 [Fluentd](https://www.fluentd.org) 这样的工具将日志转发至持久化平台（如 [Elasticsearch](https://www.elastic.co/cn/elasticsearch) 或 [Datado](https://www.datadoghq.com)）。

### 抓取 Job 的输出日志

在大多数场景中，`Job`用于完成一些特定的工作并在结构化的输出（如`JSON`）中记录了执行信息。这些输出可以通过部署流程表达式（SpEL）影响到下游阶段，您也可以使用日志或制品达到相同的目的。

### 日志

一些`Jobs`可能会输出大量的数据，处理起来很复杂。如果`Job`输出`megabytes`或`gigabytes`量级的日志数据，我们推荐您使用制品的方式。最简单和最容易理解的方式是将`Job`日志写到标准输出（stdout）。当`Job`执行完毕后，日志数据将会被两个不同的`markers`抓取和分析。

### SPINNAKER_PROPERTY_* 文件

`SPINNAKER_PROPERTY_*=*`可以用来提供单独的键值对，类似 Jenkins 的`build.properties`文件。跟随在`SPINNAKER_PROPERTY_*=*`后面的内容都会被作为键值对解析。例如有如下输出日志：

```log
Checkout spinnaker/spinnaker source code...
Latest tag is: 1.1.0.
Tag spinnaker/spinnaker with next minor version...
Uploading release...
Release uploaded.

SPINNAKER_PROPERTY_RELEASE=1.1.1
SPINNAKER_PROPERTY_URL=https://github.com/spinnaker/spinnaker/releases/tag/1.1.1
```

最终将会被解析为如下内容：

```json
{
    "RELEASE": "1.1.1",
    "URL": "https://github.com/spinnaker/spinnaker/releases/tag/1.1.1"
}
```

### SPINNAKER_CONFIG_JSON

`SPINNAKER_CONFIG_JSON`用于提供复杂的或结构化的数据。在以下案例中，`SPINNAKER_CONFIG_JSON`后面的内容被解析为 JSON。

```json
Checkout spinnaker/spinnaker source code...
Latest tag is: 1.1.0.
Tag spinnaker/spinnaker with next minor version...
Uploading release...
Release uploaded.

SPINNAKER_CONFIG_JSON={"RELEASE": "1.1.1", "URL": "https://github.com/spinnaker/spinnaker/releases/tag/1.1.1"}
```

最终将会被解析为如下内容：

```json
{
    "RELEASE": "1.1.1",
    "URL": "https://github.com/spinnaker/spinnaker/releases/tag/1.1.1"
}
```

如果在输出日志中多次出现`SPINNAKER_CONFIG_JSON`，那么每一个`SPINNAKER_CONFIG_JSON`对应的内容都会被解析并添加到 JSON 内容。如果出现了多个相同的`key`，例如 key foo 同时出现在多个`SPINNAKER_CONFIG_JSON`中，将会使用最后出现的`key`所对应的`value`值。

如果`SPINNAKER_CONFIG_JSON`指向的是`json`文件，如`SPINNAKER_CONFIG_JSON=$(cat file.json）`。请确保文件中没有换行符，因为在日志文件中`SPINNAKER_CONFIG_JSON`会被当做一整行解析。

### 制品

CODING 持续部署中的制品机制使得部署流程可以引用存储在外部系统的资源。制品可以使任何数据类型，例如 Docker 镜像、Kubernetes manifests 以及本案例将演示的`Run Job`阶段生成的数据。正如上述提到的，如果`job`产生的数据量很大导致处理成本太高，那么使用制品是最佳的解决方案。

您必须使用 CODING 持续部署支持的制品格式才能使用制品捕获`job`输出的数据。在`job`执行完成后，其输出数据被作为制品注入到部署流程上下文，下游阶段可以使用`SpEL`表达式引用制品。`job`的输出必须是 json 格式才能将其作为制品。

假设`job`执行完成后将输出数据推送到`S3 bucket`。

```log
...
Operation completed successfully.
Publishing output to S3.
Output published to s3://my-bucket/my-job/output.json
```

在`Run Jon(manifest)`阶段中配置使用制品捕获输出数据。

![](https://main.qcloudimg.com/raw/724d7905bfab31ea5394a6bb96809a9f.png)

### 清理旧的 Jobs

CODING 部署控制台（Spinnaker）不会回收`Run Job(Manifest)`阶段部署的`Jobs`。Kubernetes 在 1.12 版本中针对`Job`发布了`alpha`版本的垃圾回收功能。如果需要用到垃圾回收，请联系您的 Kubernetes 集群管理员确认是否支持此特性。
