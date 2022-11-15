## 命名空间
Namespace=QCE/TSF


## 监控指标
| 指标英文名    | 指标中文名                         | 单位 | 维度          | 统计粒度（period） |
| ------------- | ---------------------------------- | ---- | ------------- | ------------------ |
| ReqCount      | 请求数(按粒度求和)                 | 个   | applicationId | 60s、300s、3600s   |
| SuccCount     | 请求的成功数(按粒度求和)           | 个   | applicationId | 60s、300s、3600s   |
| FailCount     | 请求服务的失败数(按粒度求和)       | %    | applicationId | 60s、300s、3600s   |
| AvgDurationMs | 请求服务的平均延迟(按粒度求平均值) | 个   | applicationId | 60s、300s、3600s   |

## 各维度对应参数总览

| 参数名称                       | 维度名称   | 维度解释                   | 格式                                 |
| ------------------------------ | ---------- | -------------------------- | ------------------------------------ |
| Instances.N.Dimensions.0.Name  | applicationId | 应用 ID 的维度名称 | 输入 String 类型维度名称：applicationId |
| Instances.N.Dimensions.0.Value |applicationId | 应用 具体 ID      | 输入具体应用 ID，例如：application-abe7e123  |

## 入参说明

**查询云服务器监控数据，入参取值如下：**
&Namespace=QCE/TSF
&Instances.N.Dimensions.0.Name=applicationId 
&Instances.N.Dimensions.0.Value=具体应用 ID
