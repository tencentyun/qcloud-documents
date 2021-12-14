在 Devops 流程中，往往包含多个环境，例如包含：开发（Dev），测试（Test/beta），预发布（pre-product）， 生产环境（product），在不同环境中都需要对应用进行部署。

WordPress 是一个内容管理平台，是世界上建立博客和网站最流行的网络发布平台之一，可以让用户轻松地发布，管理和组织各种内容到目标的网站上。在本示例中我们将通过 wordpress 部署的例子，介绍如何通过 `Namespace` 命名空间对不同环境进行隔离，通过应用模板+配置实现不同环境下应用的部署。

## 步骤1： 创建 wordpress 应用模板

在 `Wordpress` 中包含一个前端的 wordpress 服务和一个后端的 mariadb 服务（mariadb 是一个和 mysql 类似的数据库服务，可以参考 [mariadb 介绍][1]）。wordpress 应用模板创建过程包括以下几个步骤：
 1. 新建 wordpress 应用模板
 2. 导入 mariadb 服务
 3. 导入 wordpress 服务
 4. 参数转换为配置项

### 新建 wordpress 应用模板

1. 在 [应用模板列表][2] 页面，单击`新建`按钮，新建一个应用模板。
![应用管理wordpress-01.png-38.2kB][3]
2. 在应用模板中，填写应用模板的名称`wordpress`。
![应用管理wordpress-02.png-29.3kB][4]

### 导入 mariadb 服务

在腾讯云容器服务中，支持两种方式导入服务的模板内容：
- 通过控制台导入
- 通过 YAML 文件导入。

两种方式可以按照需要任意选择其中一种。更多关于服务导入方式的说明可以参考 [应用模板内容操作指引][5]。

**导入方法 1： 通过控制台之间导入**
单击`导入服务`按钮，在控制台填写服务对应参数。
![应用管理 wordpress-03.png-70.1kB][6]

设置服务的基本信息：
1. 填写服务名称`mariadb`
2. 填写服务描述`mariadb服务`

设置服务的数据卷信息：
3. 数据卷选择使用云硬盘，云盘名称填写`vol`

设置镜像参数：
4. 在设置容器运行参数中的镜像参数：
容器名称设置为`mariadb`
镜像名称设置为`mariadb`
版本号选择为`latest`


设置容器其他运行参数：
5. 设置容器环境变量：
MYSQL_ROOT_PASSWORD： root

设置数据卷的挂载点：
6. vol数据卷挂载点设置为：`/var/lib/mysql` 
（更多关于数据挂载的说明，可以参考 [数据卷概述][8]）


设置服务的实例数：
7. 服务的实例数设置为1

设置服务的访问方式：
8. 服务的访问方式设置为集群内访问
9. 服务的访问端口：容器端口和服务端口都设置成 3306
（更多关于服务访问方式的说明，可以参考 [服务访问方式设置][10]）

单击`确认`按钮，自动生成 YAML 形式的模板内容。

**导入方法 2： 通过 YAML 文件导入**

在应用模板页面，单击`+`按钮，新增一个服务。服务名称设置为`mariadb`。
![应用管理wordpress-06.png-39.1kB][11]
在模板内容编辑区域，将下面的 YAML 文本内容直接导入：
```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  annotations:
    description: mariadb服务
  creationTimestamp: null
  name: mariadb
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
      - env:
        - name: MYSQL_ROOT_PASSWORD
          value: {{.ROOT_PASSWORD_VALUE}}
        image: mariadb:latest
        imagePullPolicy: Always
        name: mariadb
        resources:
          requests:
            cpu: 200m
        securityContext:
          privileged: false
        volumeMounts:
        - mountPath: /var/lib/mysql
          name: vol
      serviceAccountName: ""
      volumes:
      - name: vol
        qcloudCbs:
          cbsDiskId: '{{.ReleaseCBS_mariadb_vol}}'
          fsType: ext4
status: {}
---
apiVersion: v1
kind: Service
metadata:
  creationTimestamp: null
  name: mariadb
  namespace: '{{.NAMESPACE}}'
spec:
  ports:
  - name: tcp-3306-3306-nh6kj
    nodePort: 0
    port: 3306
    protocol: TCP
    targetPort: 3306
  selector: {}
  type: ClusterIP
status:
  loadBalancer: {}
```
这里自动提取了 `NAMESPACE` 和 `ReleaseCBS_mariadb_vol` 作为配置项。并填写 `NAMESPACE` 配置项的值为 `default`。`NAMESPACE` 用来表示服务部署到集群的哪个命名空间，更多关于命名空间的说明可以参数 [Namespace使用指引][12]。 `ReleaseCBS_XXXX` 为容器服务为使用 CBS 云盘定义的变量，更多关于 ReleaseCBS 自定义变量的说明可以参考 [自定义变量--ReleaseCBS][13]。
![应用管理wordpress-07.png-50.7kB][14]

### 导入 wordpress 服务

**导入方法 1： 通过控制台之间导入**
单击`导入服务`按钮，在控制台填写服务对应参数

设置服务的基本信息：
1. 填写服务名称`wordpress`
2. 填写服务描述`wordpress服务`

设置服务的数据卷信息：
3. 数据卷选择使用云硬盘，云盘名称填写`wordpress-persistent-storage`

设置镜像参数：
4. 在设置容器运行参数中的镜像参数：
容器名称设置为`wordpress`
镜像名称设置为`wordpress`
版本号选择为`latest`

设置容器资源限制：
5. 设置容器的 CPU 分配资源为0.1核，限制最大的使用资源为0.2核


设置容器其他运行参数：
6. 设置容器环境变量：
WORDPRESS_DB_HOST： mariadb
WORDPRESS_DB_PASSWORD： root

设置数据卷的挂载点：
7. vol 数据卷挂载点设置为：/var/www/html 
（更多关于数据挂载的说明，可以参考[数据卷概述][17]）

设置服务的实例数：
8. 服务的实例数设置为 1

设置服务的访问方式：
9. 服务的访问方式设置为外网访问
10. 服务的访问端口：容器端口和服务端口都设置成 80
（更多关于服务访问方式的说明，可以参考[服务访问方式设置][19]）

单击`确认`按钮，自动生成 YAML 形式的模板内容。

**导入方法2： 通过 YAML 文件导入**

在应用模板页面，单击`+`按钮，新增一个服务。服务名称设置为`wordpress`。
在模板内容编辑区域，将下面的 YAML 文本内容直接导入：
```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  annotations:
    description: wordpress服务
  creationTimestamp: null
  name: wordpress
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
      - env:
        - name: WORDPRESS_DB_HOST
          value: mariadb
        - name: WORDPRESS_DB_PASSWORD
          value: root
        image: wordpress:latest
        imagePullPolicy: Always
        name: wordpress
        resources:
          limits:
            cpu: 200m
          requests:
            cpu: 100m
        securityContext:
          privileged: false
        volumeMounts:
        - mountPath: /var/www/html
          name: wordpress-persistent-storage
      serviceAccountName: ""
      volumes:
      - name: wordpress-persistent-storage
        qcloudCbs:
          cbsDiskId: '{{.ReleaseCBS_wordpress_wordpress_persistent_storage}}'
          fsType: ext4
status: {}
---
apiVersion: v1
kind: Service
metadata:
  creationTimestamp: null
  name: wordpress
  namespace: '{{.NAMESPACE}}'
spec:
  ports:
  - name: tcp-80-80-snfig
    nodePort: 0
    port: 80
    protocol: TCP
    targetPort: 80
  selector: {}
  type: LoadBalancer
status:
  loadBalancer: {}
```
这里自动提取 ReleaseCBS_wordpress_wordpress_persistent_storage 作为配置项。`ReleaseCBS_XXXX` 为容器服务为使用 CBS 云盘定义的变量，更多关于ReleaseCBS 自定义变量的说明可以参考 [自定义变量--ReleaseCBS][21]。

### 参数转换为配置项

在不同环境中部署，可能会存在不同环境下参数一致的情况。这里在模板内容区域将 CPU 使用资源设置为变量，在不同环境下设置成不同的值。
![wordpress][23]

在这个示例中我们将 CPU 分配资源量和最大限制使用资源量设置为变量。分别用变量 `CPU_LIMITS`和`CPU_REQUEST` 表示。变量的形式符合`{{.}}`这样的形式。更多关于模板中变量的使用可以参考 [变量设置][24]。
这里自动提取变量 `CPU_LIMITS`和`CPU_REQUEST`，设置 `CPU_LIMITS` 的默认值为 200 m，`CPU_REQUEST` 为 100 m。（1 m=0.001 核）。

单击`完成`后，保存模板信息。在 [模板列表页][25] 可以看到新创建的模板。

![应用管理wordpress-14.png-27.4kB][26]

## 步骤2： 创建不同环境的命名空间

命名空间（Namespace）是对一组资源和对象的抽象集合，可以将不同环境的服务实例部署在不同命名空间中。

如果我们已经有了一个集群，可以直接在集群上开始创建命名空间。如果我们还没有创建好的集群，可以参考 [集群基本操作][27]，创建一个集群。

**创建集群 Namespace**

1. 在集群列表页中选择某集群的 ID/名称。
2. 单击 Namespace 列表 ，单击**新建 Namespace**。
更多关于命名空间的操作，可以参考 [Namespace 使用指引][28]。
![应用管理 wordpress-23.png-31.1kB][29]
在本示例中，我们依次创建 devnamespace、testnamespace、prenamespace、prodnamespace。
![应用管理 wordpress-24.png-33kB][30]

## 步骤3： 创建不同环境的 CBS 盘
由于 [云硬盘][31 ]页面，选择对应的区域单击新建按钮，创建新的云硬盘。

![应用管理wordpress-16.png-35.2kB](https://main.qcloudimg.com/raw/cc26d6f3b84636984c25edf4d0653da8.png)

填写对应的参数：

![应用管理wordpress-17.png-93.9kB](https://main.qcloudimg.com/raw/64864b6a5f7c9d66e0e472eb6edcfa27.png)


设置的主要参数包括：
1. 磁盘名称，例如：wordpress-dev
2. 选择所属项目和所在地域。
3. 选择计费类型和磁盘类型，这里选择包年包月和普通云硬盘
4. 选择容量大小，对于不同环境使用的磁盘，选择不同大小。在 dev、test 及 pre-product 使用10GB，product 环境使用50GB。
5. 选择磁盘数量，由于应用中两个服务各使用了一块磁盘，所以每个环境需要购买两块磁盘。
6. 单击`完成`按钮，确认购买。

购买完成后，等待 2 - 3 分钟，可以看 CBS 盘的页面查看到对应的磁盘。

![应用管理wordpress-18.png-76.3kB][34]

## 步骤4： 创建不同环境的配置项

在不同环境中，可以将不同环境的差异化信息通过配置项保存。在 [配置项][35] 页面，单击新建按钮，可以创建对应的配置文件。
![应用管理wordpress-15.png-35.2kB][36]

**dev 环境配置项：**
![应用管理wordpress-19.png-31.5kB][37]
```
NAMESPACE: devnamespace
ReleaseCBS_mariadb_vol: disk-peivemz1
ReleaseCBS_wordpress_wordpress_persistent_storage: disk-aq0280h5
CPU_LIMITS: 200m
CPU_REQUEST: 100m
```

**test 环境配置项：**
![应用管理wordpress-22.png-31.8kB][38]
```
NAMESPACE: testnamespace
ReleaseCBS_mariadb_vol: disk-fifiv4ht
ReleaseCBS_wordpress_wordpress_persistent_storage: disk-1ywc14gb
CPU_LIMITS: 200m
CPU_REQUEST: 100m
```

**pre-product 环境配置项：**
![应用管理wordpress-20.png-31.8kB][39]
```
NAMESPACE: prenamespace
ReleaseCBS_mariadb_vol: disk-fyzh7vgp
ReleaseCBS_wordpress_wordpress_persistent_storage: disk-pxtmsa7b
CPU_LIMITS: 200m
CPU_REQUEST: 100m
```

**product 环境配置项：**
![应用管理wordpress-22.png-31.8kB][40]
```
NAMESPACE: prodnamespace
ReleaseCBS_mariadb_vol: disk-r68yb55t
ReleaseCBS_wordpress_wordpress_persistent_storage: disk-frs991e5
CPU_LIMITS: 800m
CPU_REQUEST: 400m
```
在 product 环境中，设置更大的可使用资源。将 CPU_LIMITS 和 CPU_REQUEST 分别设置成800m（0.8 核）和400m（0.4 核）。

## 步骤5： 创建不同环境的应用

### 新建应用
在 [应用列表][41] 选择创建了命名空间的集群。单击`新建`按钮。

### 选择应用对应的模板和配置
在新建应用页面，选择对应的应用模板和配置项。
![应用管理 wordpress-26.png-41.7kB][43]
应用名称： 设置为 wordpress-dev
应用描述:  开发环境应用
地域选择:  选择`步骤2`中的集群所在的地域
集群选择： 选择`步骤2`中的集群
模板选择:  选择`步骤1`中创建的应用模板
配置项选择: 选择`步骤四`中创建的开发环境的配置项

单击`下一步`，对应用中的模板内容进行再次编辑。由于我们已经在应用模板和配置项中完成了对应的设置，所以这里直接单击`完成`按钮，完成应用内容的编辑。
![应用管理 wordpress-27.png-39.5kB][44]

### 查看应用状态

在应用列表页面，可以查看到新创建的应用，只是此时应用还处于未部署状态。
![应用管理 wordpress-28.png-17.7kB][45]

### 应用详情页面部署应用中的服务

单击应用的名称，可以查看应用的详情。在应用的详情页面，可以对应用进行部署操作。
![应用管理 wordpress-29.png-30.5kB][46]

单击`部署`按钮完成应用中服务的部署。

### 查看服务的信息

在完成部署后，应用中服务的状态变为`已部署`，服务的运行状态变为`运行中`。
![应用管理 wordpress-30.png-37.4kB][47]

单击服务的名称，可以跳转到服务详细页面，可以查看更多服务的信息。
![应用管理 wordpress-31.png-48.7kB][48]

### 访问服务测试

使用 wordpress 中服务访问的外网 IP 和服务端口，可以发起对服务的访问。
![应用管理 wordpress-32.png-62kB][49]

这样就完成了 dev（开发）环境的 wordpress 应用的部署。

### 应用部署到不同环境

执行同样的步骤，在应用配置时选择不同环境下对应的配置。可以将应用部署到不同的环境。部署完成后，可以在应用列表查看应用的信息。
![应用管理 wordpress-33.png-28.9kB][50]

这样基于同一个应用模板和不同环境下的配置信息，就将应用部署到了不同的环境。

  [1]: https://baike.baidu.com/item/mariaDB/6466119?fr=aladdin
  [2]: https://console.cloud.tencent.com/ccs/template
  [3]: https://mc.qcloudimg.com/static/img/f72ada368e069275051bc9693f677b40/image.png
  [4]: https://mc.qcloudimg.com/static/img/d1f4c60ed9a58a3a0c7a4d5b454b5f4b/image.png
  [5]: https://cloud.tencent.com/document/product/457/12199
  [6]: https://mc.qcloudimg.com/static/img/5b4226371374d94705cb273b6b2dc005/image.png
  [8]: https://cloud.tencent.com/document/product/457/9112
  [10]: https://cloud.tencent.com/document/product/457/9098
  [11]: https://mc.qcloudimg.com/static/img/1688a7e5da5a4363f98cf4b544777e9e/image.png
  [12]: https://cloud.tencent.com/document/product/457/10177
  [13]: https://cloud.tencent.com/document/product/457/11956#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.8F.98.E9.87.8F--releasecbs
  [14]: https://mc.qcloudimg.com/static/img/0f5702315684aefd9d8c69940815adfb/image.png
  [17]: https://cloud.tencent.com/document/product/457/9112
  [19]: https://cloud.tencent.com/document/product/457/9098
  [21]: https://cloud.tencent.com/document/product/457/11956#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.8F.98.E9.87.8F--releasecbs
  [23]: https://mc.qcloudimg.com/static/img/3d8dfa525b98ec7fa486ff29f60492ec/image.png
  [24]: https://cloud.tencent.com/document/product/457/11956
  [25]: https://console.cloud.tencent.com/ccs/template
  [26]: https://mc.qcloudimg.com/static/img/d3a797c24d97677c0a9bbbbeaebd7d31/image.png
  [27]: https://cloud.tencent.com/document/product/457/9091
  [28]: https://cloud.tencent.com/document/product/457/10177
  [29]: https://mc.qcloudimg.com/static/img/9c1f92253cdf0533edc335320c8ad5ec/image.png
  [30]: https://mc.qcloudimg.com/static/img/124c953135374f32b98b7ee41c2babce/image.png
  [31]: https://console.cloud.tencent.com/cvm/cbs
  [32]: https://mc.qcloudimg.com/static/img/a474822226c01989519b851fdefcacf5/image.png
  [33]: https://mc.qcloudimg.com/static/img/b6be1779f4361ab70c5b89b05e25e245/image.png
  [34]: https://mc.qcloudimg.com/static/img/f02938505cd23263f99e269cc0c8f756/image.png
  [35]: https://console.cloud.tencent.com/ccs/config
  [36]: https://mc.qcloudimg.com/static/img/674255f2011d8c4117ada5bd7f6c6359/image.png
  [37]: https://mc.qcloudimg.com/static/img/0078f2c3547177b55af85cfcd4407592/image.png
  [38]: https://mc.qcloudimg.com/static/img/edde901ee9415a431aa4aa7592053fde/image.png
  [39]: https://mc.qcloudimg.com/static/img/c47b6166f9ac694d7007ba0022aae9d1/image.png
  [40]: https://mc.qcloudimg.com/static/img/bffc9672fffd153b3dad8a27d52c5b24/image.png
  [41]: https://console.cloud.tencent.com/ccs/application
  [43]: https://mc.qcloudimg.com/static/img/d2bd401b2abb09c06888a970f288dce7/image.png
  [44]: https://mc.qcloudimg.com/static/img/55c56855603f94e761d090ac054e99a7/image.png
  [45]: https://mc.qcloudimg.com/static/img/0bb385567036bbd8292a2483e873dfd9/image.png
  [46]: https://mc.qcloudimg.com/static/img/494789266f4a4bf401c9ef245b0d7760/image.png
  [47]: https://mc.qcloudimg.com/static/img/9db4a548647d0460f5208d54eba555e4/image.png
  [48]: https://mc.qcloudimg.com/static/img/0733772a5772f4672b07960d3e46be5b/image.png
  [49]: https://mc.qcloudimg.com/static/img/ec558f6e7736caa987d11b4fb0164de9/image.png
  [50]: https://mc.qcloudimg.com/static/img/f19d6d08555805408fc3f4f2abd570cb/image.png
