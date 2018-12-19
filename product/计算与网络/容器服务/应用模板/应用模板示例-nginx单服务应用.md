nginx是最基础的一个服务，在应用中也算是最基础的一个应用，有点类似于"Hello World"示例。应用模板的示例，我们从"Hello World"的nginx应用开始。

## 步骤一:  新建应用模板

在[应用模板][1]列表中，单击新建按钮。

## 步骤二: 应用模板编辑

### 2.1 添加nginx服务**

应用模板中增加服务，是通过导入服务相对应的模板内容实现的。导入服务模板内容包括两种可选的方式: 1. 从控制台导入 2. YAML文件导入

>**注意：**
>可以根据场景选择使用其中的任意一种方式

更多关于服务导入的说明可以参考[应用模板内容操作指引][4]。

**导入方法1： 控制台导入服务**

单击UI导入服务按钮，会弹出导入服务的控制台，在导入服务控制台填写相应参数。

![应用模板nginx示例-014.png-78kB][import]
在`nginx`服务中设置的参数包括：

设置服务的基本信息：
1. 填写服务名称`nginx`
2. 填写服务描述`nginx服务`

设置服务的数据卷信息：
未使用数据盘，无。

设置镜像参数：
4. 在设置容器运行参数中的镜像参数：
容器名称设置为`nginx`
镜像名称设置为`nginx`
版本号选择为`latest`

设置服务的实例数：
5. 服务的实例数设置为1

设置服务的访问方式：
6. 服务的访问方式设置为集群内访问
7. 服务的访问端口：容器端口和服务端口都设置成80

更多关于参数设置内容可以参考 [服务创建][7]操作的相关文档。

填写参数后，单击导入服务的`完成`按钮，控制台自动导入服务的模板内容。

**导入方法2： YAML文件导入**

如果已经存在服务对应的模板内容的YAML文件，可以直接将模板内容导入到编辑框中。具体的步骤如下：

**步骤一 创建对应的服务**：
单击"新增空服务"号按钮，新增一个服务。服务名称设置为`nginx`。

**步骤二 导入模板内容**：

可以将下面YAML文件中的内容，直接拷贝到编辑框中，导入服务的模板内容。

```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  annotations:
    description: nginx服务
  creationTimestamp: null
  name: nginx
  namespace: '{{.NAMESPACE}}'
spec:
  replicas: 1
  revisionHistoryLimit: 5
  selector: {}
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
    spec:
      containers:
      - image: nginx:latest
        imagePullPolicy: Always
        name: nginx
        resources:
          requests:
            cpu: 200m
        securityContext:
          privileged: false
      serviceAccountName: ""
      volumes: null
status: {}
---
apiVersion: v1
kind: Service
metadata:
  creationTimestamp: null
  name: nginx
  namespace: '{{.NAMESPACE}}'
spec:
  ports:
  - name: tcp-80-80-ogxxh
    nodePort: 0
    port: 80
    protocol: TCP
    targetPort: 80
  selector: {}
  type: LoadBalancer
status:
  loadBalancer: {}
```

在示例中，使用了`NAMESPACE`将`namespace`
填写完之后，如下图所示：

![应用模板nginx示例-017.png][show]



## 步骤三: 完成应用模板编辑，并查看

在步骤二中，完成了应用模板的编辑。单击`完成`按钮，保存应用模板。这样应用模板就创建完成，可以在应用模板列表查看。
接下来可以使用创建的模板，进行应用服务部署。关于如何使用应用模板进行应用部署可以参考[创建应用][16]。关于`nginx`这个应用模板具体部署应用的过程可以参考[应用模板示例-Nginx单服务应用][17]。

[1]: https://console.cloud.tencent.com/ccs/template
[import]:https://mc.qcloudimg.com/static/img/3edab39e7f0dff61d121dc6b0cca6892/image.png
[show]:https://mc.qcloudimg.com/static/img/7d19bbccbcf86d5514d2f92562444bff/image.png

[16]: https://cloud.tencent.com/document/product/457/11942
[17]: https://cloud.tencent.com/document/product/457/11952
