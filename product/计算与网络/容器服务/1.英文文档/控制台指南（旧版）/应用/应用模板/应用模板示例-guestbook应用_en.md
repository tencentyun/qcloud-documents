Guestbook is a typical web application service, and consists of a frontend service and two backend storage services, redis-master and redis-slave. Data submitted by users through the web frontend is written into redis-master and synced to redis-slave. The synced data is then read and presented to users.

To quickly deploy Guestbook application in different clusters or different namespaces in a cluster, you can store the configurations related to Guestbook deployment into an application template, and then use the template to quickly deploy the application.

This example shows how to create a Guestbook application template.

## Step 1: Create an application template

In the [Application Template][1] list, click the **New** button.

![001-新建应用模板.png-39.8kB][2]

## Step 2: Edit the application template

**2.1 Enter the application template name**

![应用模板gustbook示例-001.png-15.9kB][3]

**2.2 Create frontend service**

(1) Click the `Add empty service` button to add a service, and set its name to `nginx`.

![应用模板gustbook示例-002.png-25.9kB][4]

(2) Enter the template content of `frontend` service in the template content edit box. You can directly copy the following content into the edit box.

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
        image: ccr.ccs.tencentyun.com/library/gb-frontend:{{.FRONTEND_VERSION}}
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
      - image: ccr.ccs.tencentyun.com/library/redis:{{.REDIS_MASTER_VERSION}}
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
        image: ccr.ccs.tencentyun.com/library/gb-redisslave :{{.REDIS_SLAVE_VERSION}}
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

Multiple variables are used in the application template. You need to configure default values for the variables as follows:
Enter the content of configuration items. In this example, the default values of configuration items are provided as follows. (Values can be modified as needed)
```
NAMESPACE: default
FRONTEND_REPLICAS: 2
FRONTEND_VERSION: v4
REDIS_MASTER_VERSION: e2e
REDIS_SLAVE_VERSION: v1
```
![应用模板gustbook示例-004.png-32.6kB][6]

## Step 3: Complete editing and view the application template

After you have completed the editing of the application template in step 2, click the `Finish` button to save it.
Now, the application template is created. You can view it the application template list.

![应用模板gustbook示例-006.png-5.3kB][8]

Next, you can deploy the application service using the created template. For more information on how to deploy services using application template, please see [Create Application][10]. For more information on how to deploy application using the `Guestbook` application template, please see [Template Example - Guestbook Application][11].

  [1]: https://console.cloud.tencent.com/ccs/template
  [2]: https://mc.qcloudimg.com/static/img/0102424d765d3deab8a2b81bee485337/image.png
  [3]: https://mc.qcloudimg.com/static/img/43d6a83add5684351d6ad5bbb3bef7b1/image.png
  [4]: https://mc.qcloudimg.com/static/img/138339c3113312e63dc7ff401706c5c2/image.png
  [5]: https://mc.qcloudimg.com/static/img/4283f6420c2d97c6d3e2da97b1f9b677/image.png
  [6]: https://mc.qcloudimg.com/static/img/93f595d1d91ea5d7eeabedca4201a713/image.png
  [8]: https://mc.qcloudimg.com/static/img/e8fcce18d38450eb9aaa23f4092077db/image.png
  [10]: https://cloud.tencent.com/document/product/457/11942
  [11]: https://cloud.tencent.com/document/product/457/11944
