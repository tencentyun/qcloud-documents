Guestbook is a typical web application service, and consists of a frontend service and two backend storage services, redis-master and redis-slave. Data submitted by users through the web frontend is written into redis-master and synced to redis-slave. The synced data is then read and presented to users.

To quickly deploy Guestbook application in different clusters or different namespaces in a cluster, you can store the configurations related to Guestbook deployment into an application template, and then use the template to quickly deploy the application.

This example shows how to create a Guestbook application template.

## Step 1: Create Application Template

In the [Application Template][1] list, click **New**.

![001-新建应用模板.png-39.8kB][2]

## Step 2: Edit Application Template

**2.1 Enter the application template name**

![应用模板gustbook示例-001.png-15.9kB][3]

**2.2 Create frontend service**

(1) Click **+** to add a service. Set the service name as "frontend".

![应用模板gustbook示例-002.png-25.9kB][4]

(2) In the template content edit box, enter the template content of the `frontend` service. You can directly copy the following content into the edit box.

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

**2.3 Create redis-master service**

(1) Create a `redis-master` service using the same process as the `frontend` service.

(2) Enter the template content of the `redis-master` service.

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

**2.4 Create redis-slave service**

(1) Create a `redis-slave` service using the same process as the `frontend` service.

(2) Enter the template content of the `redis-slave` service.

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

The created service is shown as below:

![应用模板gustbook示例-003.png-35kB][5]

**2.5 Export configuration items, and enter the content of configuration items**

Multiple variables are used in the application template. You need to set default values for the variables in configuration items. You can proceed as follows:

(1) Click `Import from the template` to export variables in the template as configuration items. In this example, `NAMESPACE`, FRONTEND_REPLICAS, FRONTEND_IMAGE, FRONTEND_VERSION, REDIS_MASTER_IMAGE, REDIS_MASTER_VERSION, REDIS_SLAVE_IMAGE and REDIS_SLAVE_IMAGE are exported as configuration items.

![应用模板gustbook示例-004.png-32.6kB][6]

(2) Enter the content of configuration items. In this example, the default values of configuration items are provided as follows. (Values can be modified as needed)
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
The values of configuration items are shown as follows.

![应用模板gustbook示例-005.png-27kB][7]

## Step 3: Complete Editing and View Application Template

You have completed the editing of the application template in Step 2. Click **Finish** button to save the application template.

![应用模板gustbook示例-006.png-5.3kB][8]

Now, the application template is created. You can view it the application template list.

![应用模板gustbook示例-007.png-17.1kB][9]

Next, you can deploy the application service using the created template. For more information on how to deploy services using application template, please see [Create Application][10]. For more information on how to deploy application using the `Guestbook` application template, please see [Template Example - Guestbook Application][11].

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
