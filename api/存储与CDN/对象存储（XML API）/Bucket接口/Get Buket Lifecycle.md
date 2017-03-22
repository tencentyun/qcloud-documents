## 功能描述
Get Bucket Lifecycle请求实现读取生命周期管理的配置。当配置不存在时，返回404 Not Found。

（目前只支持华南园区）

## 请求

### 请求语法

```HTTP
GET /?lifecycle HTTP 1.1
Host:<Bucketname>-<AppID>.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### 请求参数

无特殊请求参数

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

| 名称                             | 描述                                       | 类型        |
| ------------------------------ | ---------------------------------------- | --------- |
| LifecycleConfiguration         | 描述此生命周期管理的所有配置信息，最大支持1000条规则。            | Container |
| Rule                           | 描述单条规则的具体信息，最大支持1000条规则<Br/>父节点：LifecycleConfiguration | Container |
| Prefix                         | 前缀匹配策略，根目录则填空；多个Rule不能同时指定相同前缀路径；父目录指定某条Rule时，子目录不能指定相同类型的Rule<Br/>父节点：LifecycleConfiguration | String    |
| Status                         | 是否生效此条策略，枚举值：Enabled, Disabled<Br/>父节点：LifecycleConfiguration | String    |
| ID                             | 标示策略名称<Br/>父节点：LifecycleConfiguration    | String    |
| Transition                     | 配置文件的生命周期管理配置<Br/>父节点：Rule                 | Container |
| Expiration                     | 配置文件的定期删除规则，过期时间必须大于转换时间<Br/>父节点：Rule    | Container |
| Days                           | 在文件创建指定天数以后执行操作。Transition操作请用自然数，Expiration操作请用正整数，不同的Rule下可使用不同的时间格式，相同Rule下冲突<Br/>父节点：Transition，Expiration | Integer    |
| Date                           | 在指定时间点执行操作，时间格式为ISO 8601格式，须指定东八区触发当天午夜零点零分，可以指定历史时间，例如2016-10-31T00:00:00+08:00；当前时间大于等于Date便执行操作，长期有效；不同的Rule下可使用不同的时间格式，相同Rule下冲突<Br/>父节点：Transition，Expiration | Integer    |
| StorageClass                   | 指定存储级别，枚举值：Standard，Standard_IA，Nearline<Br/>父节点：Transition | String    |
| AbortIncompleteMultipartUpload | 配置未完成分块上传的定期删除规则<Br/>父节点：Rule            | Container |
| DaysAfterInitiation            | 在初始化分块上传之后指定天数以后Abort操作                  | 正整数       |

配置文件的冷热沉降规则

```XML
<LifecycleConfiguration>
  <Rule>
    <ID></ID>
    <Prefix></Prefix>
    <Status></Status>
    <Transition>
      <Date></Date>
      <StorageClass></StorageClass>
    </Transition>
  </Rule>
  <Rule>
    <ID></ID>
    <Prefix></Prefix>
    <Status></Status>
    <Transition>
      <Days></Days>
      <StorageClass></StorageClass>
    </Transition>
  </Rule>
</LifecycleConfiguration>
```

配置文件的定期删除规则

```XML
<LifecycleConfiguration>
  <Rule>
    <ID></ID>
    <Prefix></Prefix>
    <Status></Status>
    <Expiration>
      <Date></Date>
    </Expiration>
  </Rule>
  <Rule>
    <ID></ID>
    <Prefix></Prefix>
    <Status></Status>
    <Expiration>
      <Days></Days>
    </Expiration>
  </Rule>
</LifecycleConfiguration>
```

配置未完成分块上传的定期删除规则

```XML
<LifecycleConfiguration>
  <Rule>
    <ID></ID>
    <Prefix></Prefix>
    <Status></Status>
    <AbortIncompleteMultipartUpload>
      <DaysAfterInititation></DaysAfterInititation>
    </AbortIncompleteMultipartUpload>
  </Rule>
</LifecycleConfiguration>
```
