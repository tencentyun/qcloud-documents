nginx是最基础的一个服务，在应用中也算是最基础的一个应用，有点类似于"Hello World"示例。应用模板的示例，我们从"Hello World"的nginx应用开始。

## 步骤一:  新建应用模板

在[应用模板][1]列表中，点击新建按钮。

![应用模板nginx示例-009.png-39.8kB][2]

## 步骤二: 应用模板编辑

**2.1 填写应用的名称--`nginxapp`**

![应用模板nginx示例-010.png-27.5kB][3]

**2.2 创建nginx服务**

**创建服务方法1： 通过控制台导入服务模板**

点击导入服务按钮，会弹出导入服务的控制台。在控制台填写参数后，直接导入服务模板。

![应用模板nginx示例-011.png-78kB][4]

点击完成后可以看到在自动生成的服务模板信息：
![应用模板nginx示例-012.png-39.6kB][5]

**创建服务方法2： 手动添加服务模板**

(1) 点击在应用模板中新增服务--服务名称为`nginx`

![应用模板nginx示例-002.png-39kB][6]

(2) 在编辑框中填写服务的描述文本(YAML)格式

nginx服务的示例描述文本如下，可以直接将下面的文本拷贝到编辑框中。

```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  annotations:
    description: abc
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

在示例中，使用了`NAMESPACE`做为变量进行替换，更多关于变量替换的内容可以参考[补充变量替换链接]

填写完之后，如下图所示：

![应用模板nginx示例-003.png-46.1kB][8]

**2.3 填写默认配置项信息**

在应用模板的配置项部分，点击从模板导入按钮，自动提取模板中的变量。上面的示例中提出`NAMESPACE`变量作为配置文件的的key。(从控制台导出的服务模板已经自动将namespace提取成了`NAMESPACE`变量)

![应用模板nginx示例-004.png-42.5kB][9]

在配置项中填写`NAMESPACE`的值，这里填写为`default`，表示在默认的命名空间中部署。

![创建应用-005.png-7kB][10]

## 步骤三: 完成应用模板编辑，并查看

在步骤二中，完成了应用模板的编辑。点击`完成`按钮，保存应用模板。

![应用模板nginx示例-006.png-15.1kB][11]

这样应用模板就创建完成，可以在应用模板列表查看。

![应用模板nginx示例-007.png-20.6kB][12]

接下来可以使用创建的模板，进行应用服务部署。关于如何使用应用模板进行应用部署可以参考[补充应用创建链接]。关于`nginx`这个应用模板具体部署应用的过程可以参考 [补充应用创建示例--nginx单服务应用]


  [1]: https://console.cloud.tencent.com/ccs/template
  [2]: https://mc.qcloudimg.com/static/img/2de5054fff255008e18b60eb9142d643/image.png
  [3]: https://mc.qcloudimg.com/static/img/ccc8dff965275ff3f436bb53d8c394b3/image.png
  [4]: https://mc.qcloudimg.com/static/img/7016d8f37155a80aebdd23f9cf418f11/image.png
  [5]: https://mc.qcloudimg.com/static/img/78f7ba8c83da6cf4152dc228ff5d1abd/image.png
  [6]: https://mc.qcloudimg.com/static/img/d0c62ea6664384a4f08bb4df3f02145e/image.png
  [7]: https://mc.qcloudimg.com/static/img/d0c62ea6664384a4f08bb4df3f02145e/image.png
  [8]: https://mc.qcloudimg.com/static/img/8a729cf7c8f2c9f98e524e98cd08d7f3/image.png
  [9]: https://mc.qcloudimg.com/static/img/94e91388b81a0dcbca6a96afc9a33d31/image.png
  
  [10]: https://mc.qcloudimg.com/static/img/2c5e07b5f4bb224d9ff30102b8e958a6/image.png
  [11]: https://mc.qcloudimg.com/static/img/bd31c2a625d8a480c3edeffc9cd72de9/image.png
  [12]: https://mc.qcloudimg.com/static/img/3dc44d8e08039db14b28c9727920290a/image.png