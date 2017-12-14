Guestbook留言板是一个比较典型的web应用服务，由一个frontend前端服务和redis-master和redis-slave两个后端存储服务组成。用户通过web前端提交数据，写入到redis-master上，然后通过读取同步到redis-slave上的数据展示给用户。

为了实现快速的在不同集群或者集群的不同namespace中部署Guestbook应用，可以先将Gustbook部署相关的配置保存到应用模板中，然后使用应用模板快速部署对应的应用。

本示例将介绍如何将创建Gustbook的应用模板。

## 步骤一: 创建应用模板

在[应用模板][1]列表中，点击新建按钮。

![001-新建应用模板.png-39.8kB][2]

## 步骤二: 编辑应用模板

**2.1 填写应用模板名称**

![应用模板gustbook示例-001.png-15.9kB][3]

**2.2 创建frontend服务**

(1) 点击图中`+`号，新增一个服务。服务名称设置为frontend。

![应用模板gustbook示例-002.png-25.9kB][4]

(2) 在模板内容的编辑框中，填写`frontend`服务的模板内容。可以直接拷贝下面的内容导编辑框中。

```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: frontend
  namespace: {{.NAMESPACE}}
spec:
  replicas: {{.FRONTEND_REPLICAS}}
  template:
    spec:
      containers:
      - env:
        - name: GET_HOSTS_FROM
          value: dns
        image: {{.FRONTEND_IMAGE}}:{{.FRONTEND_VERSION}}
        imagePullPolicy: Always
        name: php-redis
        resources:
          requests:
            cpu: 100m
        securityContext:
          privileged: false
      dnsPolicy: ClusterFirst
      restartPolicy: Always
---
apiVersion: v1
kind: Service
metadata:
  name: frontend
  namespace: {{.NAMESPACE}}
spec:
  ports:
  - name: tcp-80-80-fwdy6
    port: 80
    protocol: TCP
    targetPort: 80
  sessionAffinity: None
  type: LoadBalancer
```

**2.3 创建redis-master服务**

(1) 和`frontend`服务创建过程类似，新建一个`redis-master`服务。

(2) 填写`redis-master`服务的模板内容。

```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: redis-master
  namespace: {{.NAMESPACE}}
spec:
  template:
    spec:
      containers:
      - image: {{.REDIS_MASTER_IMAGE}}:{{.REDIS_MASTER_VERSION}}
        imagePullPolicy: Always
        name: master
        resources:
          limits:
            memory: 100Mi
          requests:
            cpu: 100m
            memory: 100Mi
        securityContext:
          privileged: false
      dnsPolicy: ClusterFirst
      restartPolicy: Always
---
apiVersion: v1
kind: Service
metadata:
  name: redis-master
  namespace: {{.NAMESPACE}}
spec:
  ports:
  - name: tcp-6379-6379-6d3d9
    port: 6379
    protocol: TCP
    targetPort: 6379
  sessionAffinity: None
  type: ClusterIP
```

**2.4 创建redis-slave服务**

(1) 和`frontend`服务创建过程类似，新建一个`redis-slave`服务。

(2) 填写`redis-slave`服务的模板内容。

```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: redis-slave
  namespace: {{.NAMESPACE}}
spec:
  template:
    spec:
      containers:
      - env:
        - name: GET_HOSTS_FROM
          value: dns
        image: {{.REDIS_SLAVE_IMAGE}}:{{.REDIS_SLAVE_VERSION}}
        imagePullPolicy: Always
        name: slave
        resources:
          limits:
            memory: 100Mi
          requests:
            cpu: 100m
            memory: 100Mi
        securityContext:
          privileged: false
      dnsPolicy: ClusterFirst
      restartPolicy: Always
---
apiVersion: v1
kind: Service
metadata:
  name: redis-slave
  namespace: {{.NAMESPACE}}
spec:
  externalName: ""
  ports:
  - name: tcp-6379-6379-av5fd
    port: 6379
    protocol: TCP
    targetPort: 6379
  sessionAffinity: None
  type: ClusterIP
```

创建后的服务如下图所示：

![应用模板gustbook示例-003.png-35kB][5]

**2.5 导出配置项，并填写配置项内容**

在应用模板汇总使用了多个变量，需要在配置项中为变量设置默认值。具体的做法如下。

(1) 点击`从模板内容导入`，导出模板中的变量作为配置项。这里导出`NAMESPACE`,FRONTEND_REPLICAS，FRONTEND_IMAGE，FRONTEND_VERSION，REDIS_MASTER_IMAGE，REDIS_MASTER_VERSION，REDIS_SLAVE_IMAGE，REDIS_SLAVE_IMAGE作为配置项。

![应用模板gustbook示例-004.png-32.6kB][6]

(2) 填写配置中配置项的内容。在本示例中，配置项的默认值如下。(可以根据需要进行修改)
```
NAMESPACE: default
FRONTEND_REPLICAS: 2
FRONTEND_IMAGE: ccr.ccs.tencentyun.com/library/gb-frontend
FRONTEND_VERSION: v4
REDIS_MASTER_IMAGE: ccr.ccs.tencentyun.com/library/redis
REDIS_MASTER_VERSION: e2e
REDIS_SLAVE_IMAGE: ccr.ccs.tencentyun.com/library/gb-redisslave
REDIS_SLAVE_IMAGE: v1
```
填写完之后，配置项的值如下图所示。

![应用模板gustbook示例-005.png-27kB][7]

## 步骤三: 完成应用模板编辑，并查看

在步骤二中，完成了应用模板的编辑。点击`完成`按钮，保存应用模板。

![应用模板gustbook示例-006.png-5.3kB][8]

这样应用模板就创建完成，可以在应用模板列表查看。

![应用模板gustbook示例-007.png-17.1kB][9]

接下来可以使用创建的模板，进行应用服务部署。关于如何使用应用模板进行应用部署可以参考[创建应用][10]。关于`Guestbook`这个应用模板具体部署应用的过程可以参考应用[模板示例-Guestbook应用][11]。

  [1]: https://console.cloud.tencent.com/ccs/template
  [2]: https://mc.qcloudimg.com/static/img/916facfa358f0ab96524c2e644a3b223/image.png
  [3]: https://mc.qcloudimg.com/static/img/ca4cfb00da6fef22577596fa145156fd/image.png
  [4]: https://mc.qcloudimg.com/static/img/5dad81c961661a5ee4147d1a5b3231a6/image.png
  [5]: https://mc.qcloudimg.com/static/img/3b29da4e2d2e758c0c144029bcf583d0/image.png
  [6]: https://mc.qcloudimg.com/static/img/dc0552a8a6b110b35d3f6e95fde12efc/image.png
  [7]: https://mc.qcloudimg.com/static/img/a3c9542183055e9ebc2cf834aae43957/image.png
  [8]: https://mc.qcloudimg.com/static/img/66635b054bf711fa4c570265bed3971a/image.png
  [9]: https://mc.qcloudimg.com/static/img/f371ff5c3969ecb50bc80f2599c5b67a/image.png
  [10]: https://cloud.tencent.com/document/product/457/11942
  [11]: https://cloud.tencent.com/document/product/457/11944