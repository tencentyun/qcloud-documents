# 应用模板示例-guestbook应用

标签（空格分隔）： 未分类

---

Guestbook是一个比较典型的web应用服务，其有一个frontend前端服务和redis-master和redis-slave两个后端存储服务组成。本示例将介绍如何将创建gustbook软件的应用模板。

## 步骤一: 创建应用模板

在应用模板列表中，点击新建按钮。

![001-新建应用模板.png-39.8kB][1]

## 步骤二: 编辑应用模板

**2.1 填写应用模板名称**

![应用模板gustbook示例-001.png-15.9kB][2]

**2.2 创建frontend服务**

(1) 点击图中`+`号，新增一个服务。服务名称设置为frontend。

![应用模板gustbook示例-002.png-25.9kB][3]

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
  type: LoadBalancer
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
  type: LoadBalancer
```

创建后的服务如下图所示：

![应用模板gustbook示例-003.png-35kB][4]

**2.5 导出配置项，并填写配置项内容**

在应用模板汇总使用了多个变量，需要在配置项中为变量设置默认值。具体的做法如下。

(1) 点击`从模板内容导入`，导出模板中的变量作为配置项。这里导出`NAMESPACE`,FRONTEND_REPLICAS，FRONTEND_IMAGE，FRONTEND_VERSION，REDIS_MASTER_IMAGE，REDIS_MASTER_VERSION，REDIS_SLAVE_IMAGE，REDIS_SLAVE_IMAGE作为配置项。

![应用模板gustbook示例-004.png-32.6kB][5]

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

![应用模板gustbook示例-005.png-27kB][6]

## 步骤三: 完成应用模板编辑，并查看

在步骤二中，完成了应用模板的编辑。点击`完成`按钮，保存应用模板。

![应用模板gustbook示例-006.png-5.3kB][7]

这样应用模板就创建完成，可以在应用模板列表查看。

![应用模板gustbook示例-007.png-17.1kB][8]


  [1]: http://static.zybuluo.com/yan234280533/ar92auc9ym0hq3mknll6zcst/001-%E6%96%B0%E5%BB%BA%E5%BA%94%E7%94%A8%E6%A8%A1%E6%9D%BF.png
  [2]: http://static.zybuluo.com/yan234280533/fe06z4qwow5oe0pw6jyzhha5/%E5%BA%94%E7%94%A8%E6%A8%A1%E6%9D%BFgustbook%E7%A4%BA%E4%BE%8B-001.png
  [3]: http://static.zybuluo.com/yan234280533/ar879876mtaryjs836dhenir/%E5%BA%94%E7%94%A8%E6%A8%A1%E6%9D%BFgustbook%E7%A4%BA%E4%BE%8B-002.png
  [4]: http://static.zybuluo.com/yan234280533/rz4jaizpr0hmbd13jlnsd32k/%E5%BA%94%E7%94%A8%E6%A8%A1%E6%9D%BFgustbook%E7%A4%BA%E4%BE%8B-003.png
  [5]: http://static.zybuluo.com/yan234280533/2v2h389rcum738va0n7o2ood/%E5%BA%94%E7%94%A8%E6%A8%A1%E6%9D%BFgustbook%E7%A4%BA%E4%BE%8B-004.png
  [6]: http://static.zybuluo.com/yan234280533/dyoujp93bf6fc32fh3p02d5m/%E5%BA%94%E7%94%A8%E6%A8%A1%E6%9D%BFgustbook%E7%A4%BA%E4%BE%8B-005.png
  [7]: http://static.zybuluo.com/yan234280533/2fej9p4quj8ivr7jj29h7i1z/%E5%BA%94%E7%94%A8%E6%A8%A1%E6%9D%BFgustbook%E7%A4%BA%E4%BE%8B-006.png
  [8]: http://static.zybuluo.com/yan234280533/mnvigivkticjnaaogw6l8ovq/%E5%BA%94%E7%94%A8%E6%A8%A1%E6%9D%BFgustbook%E7%A4%BA%E4%BE%8B-007.png