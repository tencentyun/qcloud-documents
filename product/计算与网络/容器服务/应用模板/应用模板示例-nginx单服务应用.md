nginx是最基础的一个服务，在应用中也算是最基础的一个应用，有点类似于"Hello World"示例。应用模板的示例，我们从"Hello World"的nginx应用开始。

## 步骤一:  新建应用模板

在[应用模板][1]列表中，点击新建按钮。

![应用模板nginx示例-009.png-39.8kB][2]

## 步骤二: 应用模板编辑

**2.1 填写应用的名称--`nginxapp`**

![应用模板nginx示例-010.png-27.5kB][3]

**2.2 添加nginx服务**

应用模板中增加服务，是通过导入服务相对应的模板内容实现的。导入服务模板内容包括两种可选的方式: 1. 从控制台导入 2. YAML文件导入

>**注意：**
>可以根据场景选择使用其中的任意一种方式

更多关于服务导入的说明可以参考[应用模板内容操作指引][4]。

**导入方法1： 控制台导入服务**

点击导入服务按钮，会弹出导入服务的控制台，在导入服务控制台填写相应参数。

![应用模板nginx示例-014.png-78kB][5]
![应用模板nginx示例-015.png][6]

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

填写参数后，点击导入服务的`完成`按钮，控制台自动导入服务的模板内容。

![应用模板nginx示例-012.png-39.6kB][8]

**导入方法2： YAML文件导入**

如果已经存在服务对应的模板内容的YAML文件，可以直接将模板内容导入到编辑框中。具体的步骤如下：

**步骤一 创建对应的服务**：
在模板内容编辑区域，点击"+"号按钮，新增一个服务。服务名称设置为`nginx`。

![应用模板nginx示例-002.png-39kB][9]

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

**步骤三 提取模板内容中的变量**：

在示例中，使用了`NAMESPACE`将`namespace`参数作为变量进行替换，更多关于变量替换的说明可以参考[变量替换][10]。

点击`从模板内容导入`按钮，提取模板内容中的变量作为配置项。然后在配置项中填写变量的默认值，这里设置成`default`。

填写完之后，如下图所示：

![应用模板nginx示例-017.png][11]

**2.3 常用参数变量化**
在模板内容中可能有些参数需要经常改变或者在不同环境中需要设置不同的值。可以将这部分参数在模板内容设置成变量，在配置项中对变量进行赋值。这样如果需要修改这个参数，就只需要修改配置项，不需要对模板内容进行修改。在不同环境中，也可以通过使用不同的配置项文件，对不同环境下的应用使用不同的参数进行部署。

在本示例中，我们将实例副本数(`replicas`)转换成变量`NGINX_REPLICAS`，镜像名称和版本(`image`)分别`IMAGE_NAME`和`IMAGE_VERSION`。

![应用模板nginx示例-018.png][12]

在应用模板的配置项部分，点击从模板导入按钮，自动提取模板中的变量。分别对变量赋值： `NGINX_REPLICAS`设置为`2`，`IMAGE_NAME`设置为`nginx`,`IMAGE_VERSION`s设置为latest。

![应用模板nginx示例-019.png][13]

## 步骤三: 完成应用模板编辑，并查看

在步骤二中，完成了应用模板的编辑。点击`完成`按钮，保存应用模板。这样应用模板就创建完成，可以在应用模板列表查看。

![应用模板nginx示例-007.png-20.6kB][15]

接下来可以使用创建的模板，进行应用服务部署。关于如何使用应用模板进行应用部署可以参考[创建应用][16]。关于`nginx`这个应用模板具体部署应用的过程可以参考[应用模板示例-Nginx单服务应用][17]。

  [1]: https://console.cloud.tencent.com/ccs/template
  [2]: https://mc.qcloudimg.com/static/img/2de5054fff255008e18b60eb9142d643/image.png
  [3]: https://mc.qcloudimg.com/static/img/ccc8dff965275ff3f436bb53d8c394b3/image.png
  [4]: https://cloud.tencent.com/document/product/457/12199
  [5]: https://mc.qcloudimg.com/static/img/4c24dba39ed4637fdf71054859b8623a/image.png
  [6]: https://mc.qcloudimg.com/static/img/ac1fda92af3cd48d8f573c10fb82cfe9/image.png
  [7]: https://mc.qcloudimg.com/static/img/7016d8f37155a80aebdd23f9cf418f11/image.png
  [8]: https://mc.qcloudimg.com/static/img/78f7ba8c83da6cf4152dc228ff5d1abd/image.png
  [9]: https://mc.qcloudimg.com/static/img/d0c62ea6664384a4f08bb4df3f02145e/image.png
  [10]: https://mc.qcloudimg.com/static/img/7016d8f37155a80aebdd23f9cf418f11/image.png
  [11]: https://mc.qcloudimg.com/static/img/2e2029729c2c525a4fb39db94cace6fa/image.png
  [12]: https://mc.qcloudimg.com/static/img/9ea24fc4ac6874c763e49be0c54b4713/image.png
  [13]: https://mc.qcloudimg.com/static/img/95805801a80af3430b85674c8e3721f9/image.png
  [14]: https://mc.qcloudimg.com/static/img/bd31c2a625d8a480c3edeffc9cd72de9/image.png
  [15]: https://mc.qcloudimg.com/static/img/3dc44d8e08039db14b28c9727920290a/image.png
  [16]: https://cloud.tencent.com/document/product/457/11942
  [17]: https://cloud.tencent.com/document/product/457/11952