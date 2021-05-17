
告警规则允许我们基于 Prometheus 的表达式设定告警条件, 实时监控服务的状态，及时通知触达服务异常情况.

## 如何定义一个告警规则

在 Prometheus 中，告警规则和聚合规则的定义非常类似，一个告警规则的示例可能如下：

```
groups:
- name: example
  rules:
  - alert: HighRequestLatency
    expr: job:request_latency_seconds:mean5m{job="myjob"} > 0.5
    for: 10m
    labels:
      severity: page
    annotations:
      summary: High request latency
```

在告警规则文件中，我们可以将一组相关的规则设置定义在一个 group 下。在每一个 group 中我们可以定义多个告警规则 rule。一条告警规则主要由以下几部分组成：

* alert：告警规则的名称。
* expr：基于 PromQL 的表达式告警触发条件，用于计算是否有时间序列满足该条件。
* for：评估等待时间，可选参数。用于表示只有当触发条件持续一段时间后才发送告警。在等待期间新产生告警的状态为 pending。
* labels：自定义标签，允许用户指定要附加到告警上的一组附加标签。
* annotations：用于指定一组附加信息，例如用于描述告警详细信息的文字等，annotations 的内容在告警产生时会一同作为参数发送到 Alertmanager。

## 模板

通常情况，在告警规则文件的 annotations 中使用 summary 描述告警的概要信息，description 用于描述告警的详细信息。同时 Alertmanager 的 UI 也会根据这两个标签值，显示告警信息。为使告警信息具有更好的可读性，Prometheus 支持模板化 label 和 annotations 的中标签的值。

通过 $labels.&lt;labelname> 变量可以访问当前告警实例中指定标签的值。$value 则可以获取当前 PromQL 表达式计算的样本值。

```
# To insert a firing element's label values:
{{ $labels.<labelname> }}
# To insert the numeric expression value of the firing element:
{{ $value }}
```

例如，可以通过模板化优化 summary 以及 description 的内容的可读性：

```
groups:
- name: example
  rules:

  # Alert for any instance that is unreachable for >5 minutes.
  - alert: InstanceDown
    expr: up == 0
    for: 5m
    labels:
      severity: page
    annotations:
      summary: "Instance {{ $labels.instance }} down"
      description: "{{ $labels.instance }} of job {{ $labels.job }} has been down for more than 5 minutes."

  # Alert for any instance that has a median request latency >1s.
  - alert: APIHighRequestLatency
    expr: api_http_request_latencies_second{quantile="0.5"} > 1
    for: 10m
    annotations:
      summary: "High request latency on {{ $labels.instance }}"
      description: "{{ $labels.instance }} has a median request latency above 1s (current value: {{ $value }}s)"
```
