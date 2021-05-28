预聚合 (Recording Rule) 可以让我们对一些常用的指标或者计算相对复杂的指标进行提前计算，然后将这些数据存储到新的数据指标中，查询这些计算好的数据将比查询原始的数据更快更便捷。这对于 Dashboard 场景非常适用，可以解决用户配置以及查询慢的问题。

预聚合以规则组 (Rule Group) 的形式存在, 相同组中的规则以一定的间隔顺序执行。聚合规则的名字必须符合 [相应的 Prometheus 规范](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels)。

通常一个规则文件如下：

```plaintext
groups:
  [ - <rule_group> ]
```

以下为一个简单预聚合规则例子：

```plaintext
groups:
  - name: example
    rules:
    - record: job:http_inprogress_requests:sum
      expr: sum by (job) (http_inprogress_requests)
```


## 规则组

```plaintext
# 规则组名称, 在同一文件中必须唯一
name: <string>

# 规则探测周期.
[ interval: <duration> | default = global.evaluation_interval ]

rules:
  [ - <rule> ... ]
```

## 规则

预聚合的语法如下：

```plaintext
# 生成的新的指标名称, 必须是一个有效的指标名称
record: <string>

# PromQL 表达式, 每次计算的数据都会存储到新的指标名称 'record' 中
expr: <string>

# 在要存储的数据中所要添加或者覆盖的标签
labels:
  [ <labelname>: <labelvalue> ]
```

## 推荐命名格式

预聚合规则命名的推荐格式：`level:metric:operations`。

- level：表示聚合级别，以及规则的输出标签。
- metric：是指标名称。
- operations： 应用于指标的操作列表。

例如：
```plaintext
- record: instance_path:requests:rate5m
  expr: rate(requests_total{job="myjob"}[5m])

- record: path:requests:rate5m
  expr: sum without (instance)(instance_path:requests:rate5m{job="myjob"})
```
