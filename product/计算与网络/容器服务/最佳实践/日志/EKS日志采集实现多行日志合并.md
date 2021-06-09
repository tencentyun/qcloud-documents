
## 使用场景
使用环境变量去配置 EKS 日志采集时，默认使用单行提取模式。但当客户程序的日志数据跨占多行时（例如 Java 程序日志），不能以换行符 `\n` 作为日志的结束标识符。为了能让日志系统明确区分开每条日志，需要配置具有首行正则表达式的 configmap，当某行日志匹配了预先设置的正则表达式，则认为是一条日志的开头，而在下一个行首出现则作为该条日志的结束标识符。本文向您介绍使用环境变量的方式开启 EKS 日志采集时，如何实现多行日志合并。





## 操作步骤
### 原始日志示例
```
2020-09-24 16:09:07 ERROR System.out(4844) java.lang.NullPointerException
at com.temp.ttscancel.MainActivity.onCreate(MainActivity.java:43)
at android.app.Activity.performCreate(Activity.java:5248)
at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1110) at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2162) at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2257)
at android.app.ActivityThread.access$800(ActivityThread.java:139)
at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1210)
```





### 创建 Configmap[](id:Configmap)
针对原始日志文件示例，parser.conf 配置文件内容为：

```
apiVersion: v1 
data:
    parser.conf: |- 
      [PARSER]
      Name parser_name
      Format regex
      Regex ^(?<timestamp>[0-9]{2,4}\-[0-9]{1,2}\-[0-9]{1,2} [0-9]{1,2}\:[0-9]{1,2}\:[0-9]{1,2}) (?<message>.*) 
kind: ConfigMap
metadata:
    name: cm 
    namespace: default
```

其中 `parser_name` 需要在创建工作负载的时候设置在 annotation 中（spec.template.metadata.annotations），执行以下命令进行设置：

```
eks.tke.cloud.tencent.com/parser-name: parser_name
```

更多 `parser.conf` 配置文件相关内容可参见 [Regular Expression](https://docs.fluentbit.io/manual/pipeline/parsers/regular-expression)。

### 创建 Pod 时挂载 Configmap
在创建 Pod 时需要做以下操作：
1. 以 Volume 形式挂载已创建的 [Configmap](#Configmap)。
2. 通过环境变量的方式开启日志采集，详情可参见 [配置日志采集](https://cloud.tencent.com/document/product/457/47200#.E9.80.9A.E8.BF.87-yaml-.E9.85.8D.E7.BD.AE.E6.97.A5.E5.BF.97.E9.87.87.E9.9B.86-.3Ca-id.3D.22yaml.22.3E.3C.2Fa.3E)。
3. 指定两个 annotation。
```
eks.tke.cloud.tencent.com/parser-name: "parser_name"
eks.tke.cloud.tencent.com/volume-name-for-parser: "volume-name"
```
 - `eks.tke.cloud.tencent.com/parser-name` 是指已创建的 [Configmap](#Configmap) 的 name。
 - `eks.tke.cloud.tencent.com/volume-name-for-parser` 是指 Pod 中挂载的 Volume 名称，可自定义。

**Pod yaml 模版**

```
apiVersion: apps/v1 
kind: Deployment 
metadata:
    labels:
      k8s-app: multiline 
      qcloud-app: multiline
    name: multiline
    namespace: default 
spec:
    replicas: 1 
    selector:
      matchLabels:
        k8s-app: multiline
        qcloud-app: multiline 
    template:
      metadata: 
        annotations:
          eks.tke.cloud.tencent.com/parser-name: parser_name
          eks.tke.cloud.tencent.com/volume-name-for-parser: volume-name 
        labels:
          k8s-app: multiline
          qcloud-app: multiline 
      spec:
        containers: 
        - env:
          - name: EKS_LOGS_OUTPUT_TYPE 
            value: cls
          - name: EKS_LOGS_LOG_PATHS 
            value: stdout
          - name: EKS_LOGS_TOPIC_ID 
            value: topic-id
          - name: EKS_LOGS_LOGSET_NAME 
            value: eks
          - name: EKS_LOGS_SECRET_ID 
            valueFrom:
              secretKeyRef: 
                key: SecretId 
                name: cls 
                optional: false
          - name: EKS_LOGS_SECRET_KEY 
            valueFrom:
              secretKeyRef: 
                key: SecretKey 
                name: cls 
                optional: false
          image: nginx 
          imagePullPolicy: Always 
          name: ng
          resources:
            limits:
              cpu: 500m 
              memory: 1Gi
            requests:
              cpu: 250m 
              memory: 256Mi
          volumeMounts:
          - mountPath: /mnt
              name: volume-name 
              imagePullSecrets:
              - name: qcloudregistrykey 
              restartPolicy: Always 
          volumes:
          - configMap:
              defaultMode: 420
              name: cm
            name: volume-name
```




### 结构化处理后日志示例

```
2020-09-24 16:09:07 ERROR System.out(4844) java.lang.NullPointerException \at com.temp.ttscancel.MainActivity.onCreate(MainActivity.java:43) \at android.app.Activity.performCreate(Activity.java:5248) \at android.app.Instrumentation.callActivityOnCreate(Instrumentation.java:1110) \at android.app.ActivityThread.performLaunchActivity(ActivityThread.java:2162) \at android.app.ActivityThread.handleLaunchActivity(ActivityThread.java:2257) \at android.app.ActivityThread.access$800(ActivityThread.java:139) \at android.app.ActivityThread$H.handleMessage(ActivityThread.java:1210)
```
