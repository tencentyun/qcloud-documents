The process of Devops often involves multiple environments such as development (Dev), testing (Test/beta), pre-release (pre-product) and production (product) environment. You need to deploy an application in different environments.

WordPress is a content management platform. It is one of the most popular network publishing platforms for building blogs and websites in the world. It allows users to publish, manage and organize various contents onto target websites. We will take deploying WordPress as an example to demonstrate how to isolate different environments via `Namespace` and how to deploy an application in different environments using "application template + configuration".

## Step 1: Create an application template for WordPress

`Wordpress` contains a frontend WordPress service and a backend MariaDB service. MariaDB is a MySQL-like database service. For more information, please see [MariaDB Overview][1]. When creating an application template for WordPress, you need to:

 1. Create an application template for WordPress
 2. Import MariaDB
 3. Import WordPress
 4. Convert the parameters to configuration items

### Creating an Application Template for WordPress

On the [Application Template List][2] page, click `New` to create an application template.

![应用管理wordpress-01.png-38.2kB][3]

In the application template, enter `wordpress` as the application template name.

![应用管理wordpress-02.png-29.3kB][4]

### Importing MariaDB

In the Tencent Cloud CCS service, you can import the service template on the console or from YAML file, whichever you need. For more information on how to import the service, please see [Application Template Operation Instructions][5].

**Method 1: Import on the console**

Click the `Import Service` button and enter the parameters on the console.

![应用管理wordpress-03.png-70.1kB][6]

Basic information:
1. Service name: `mariadb`
2. Service description: `mariadb service`

Volume information:
3. Volume: Cloud Disk. Cloud disk name: `vol`

Image parameters:
4. Set image parameters in the running parameters of the container:
Container name: `mariadb`
Image name: `mariadb`
Tag: `latest`


Other running parameters of the container:
5. Container environment variables:
MYSQL_ROOT_PASSWORD: root

Mount point of the volume:
6. Mount point of vol: /var/lib/mysql 
(For more information on data mounting, please see [Volume Overview][8])


The number of pods:
7. Number of pods: 1

Access method:
8. Access method: In-cluster access
9. Access port: Set both container port and service port to 3306
(For more information on service access, please see [Set Service Access Method][10])

Click `OK` to automatically generate the template content in YAML format.

**Method 2: Import from YAML file**

On the application template page, click `+` to add a service. Set the image name to `mariadb`.

![应用管理wordpress-06.png-39.1kB][11]

In the template content editing area, import the following YAML text content:

```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  annotations:
    description: mariadb service
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
`NAMESPACE` and `ReleaseCBS_mariadb_vol` are automatically extracted as configuration items. Enter `default` for `NAMESPACE`. `NAMESPACE` is used to represent which namespace in the cluster the service is deployed to. For more information on namespace, please see [Namespace Usage Guide][12]. `ReleaseCBS_XXXX` is the variable defined by CCS for use of CBS disk. For more information on the custom variable ReleaseCBS, please see [Custom Variable - ReleaseCBS][13].

![应用管理wordpress-07.png-50.7kB][14]

### Importing WordPress

**Method 1: Import on the console**

Click the `Import Service` button and enter the parameters on the console.

Basic information:
1. Service name: `wordpress`
2. Service description: `wordpress service`

Volume information:
3. Volume: cloud disk. Cloud disk name: `wordpress-persistent-storage`

Image parameters:
4. Set image parameters in the running parameters of the container:
Container name: `wordpress`
Image name: `wordpress`
Tag: `latest`

Container resource limits:
5. CPU resource required for the container: 0.1 core. Maximum CPU resource available for the container: 0.2 core


Other running parameters of the container:
6. Container environment variables:
WORDPRESS_DB_HOST: mariadb
WORDPRESS_DB_PASSWORD: root

Mount point of the volume:
7. Mount point of vol: /var/www/html 
(For more information on data mounting, please see [Volume Overview][17])

The number of pods:
8. Number of pods: 1

Access method:
9. Set the access method to "Public network access"
10. Access port: Set both container port and service port to 3306
(For more information on service access, please see [Set Service Access Method][19])

Click `OK` to automatically generate the template content in YAML format.

**Method 2: Import from YAML file**

On the application template page, click `+` to add a service. Set the image name to `wordpress`.

In the template content editing area, import the following YAML text content:

```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  annotations:
    description: wordpress service
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
ReleaseCBS_wordpress_wordpress_persistent_storage is automatically extracted as the configuration item. `ReleaseCBS_XXXX` is the variable defined by CCS for use of CBS disk. For more information on the custom variable ReleaseCBS, please see [Custom Variable - ReleaseCBS][21].

### Converting Parameters to Configuration Items

Parameters may remain the same when the application is deployed in different environments. In the template content area, CPU resource needs to be a variable that can be set to different values in different environments.
![wordpress][23]

In this example, CPU resource and the maximum available CPU resource are variables, represented by `CPU_LIMITS` and `CPU_REQUEST` respectively and shown in the format of `{{.}}`. For more information on variables in the template, please see [Variables Settings][24].
`CPU_LIMITS` and `CPU_REQUEST` are automatically extracted. Set the default values of `CPU_LIMITS` and `CPU_REQUEST` to 200m and 100m respectively. (1m=0.001 core).

Click `Finish` to save the template information. You can view the new template on the [Template List][25] page.

![应用管理wordpress-14.png-27.4kB][26]

## Step 2: Create Namespaces in different environments

Namespace is an abstract collection of a group of resources and objects. Service instances in different environments can be deployed in different namespaces.

If you already have a cluster, create a namespace on the cluster directly. Otherwise, please see [Basic Operations for Cluster][27] to create a cluster.

**Creating a namespace on the cluster**

1. Select ID/Name of a cluster on the cluster list page.
2. Click Namespace List, and then click **New Namespace**.

For more information on Namespace, please see [Namespace Usage Guide][28].

![应用管理wordpress-23.png-31.1kB][29]

In this example, create devnamespace, testnamespace, prenamespace, and prodnamespace.

![应用管理wordpress-24.png-33kB][30]

## Step 3: Create CBS disks in different environments
Select a region on the [CBS][31] page, and click **New** to create a cloud disk.

![应用管理wordpress-16.png-35.2kB][32]

Enter the parameters:

![应用管理wordpress-17.png-93.9kB][33]

Main parameters include:
1. Disk name, such as: wordpress-dev
2. The project and region to which the cloud disk belongs.
3. Billing type and disk type. **Prepaid** and **HDD Cloud Storage** are selected here.
4. Capacity, which varies with different environments. 10 GB is used in dev, test and pre-product environments, and 50 GB is used in product environment.
5. Number of disks. You need to purchase two disks for each environment because each of the two services in the application occupies a disk.
6. Click `Finish` to confirm purchase.

After the disks are purchased, wait for 2-3 minutes, and then you can check the disks on the CBS disk page.

![应用管理wordpress-18.png-76.3kB][34]

## Step 4: Create configuration items for different environments

You can save the differentiated information for different environments via configuration items. On the [Configuration Items][35] page, click **New** to create the configuration file.

![应用管理wordpress-15.png-35.2kB][36]

**Configuration items for dev environment:**

![应用管理wordpress-19.png-31.5kB][37]

```
NAMESPACE: devnamespace
ReleaseCBS_mariadb_vol: disk-peivemz1
ReleaseCBS_wordpress_wordpress_persistent_storage: disk-aq0280h5
CPU_LIMITS: 200m
CPU_REQUEST: 100m
```

**Configuration items for test environment:**

![应用管理wordpress-22.png-31.8kB][38]

```
NAMESPACE: testnamespace
ReleaseCBS_mariadb_vol: disk-fifiv4ht
ReleaseCBS_wordpress_wordpress_persistent_storage: disk-1ywc14gb
CPU_LIMITS: 200m
CPU_REQUEST: 100m
```

**Configuration items for pre-product environment:**

![应用管理wordpress-20.png-31.8kB][39]

```
NAMESPACE: prenamespace
ReleaseCBS_mariadb_vol: disk-fyzh7vgp
ReleaseCBS_wordpress_wordpress_persistent_storage: disk-pxtmsa7b
CPU_LIMITS: 200m
CPU_REQUEST: 100m
```
**Configuration items for product environment:**

![应用管理wordpress-22.png-31.8kB][40]

```
NAMESPACE: prodnamespace
ReleaseCBS_mariadb_vol: disk-r68yb55t
ReleaseCBS_wordpress_wordpress_persistent_storage: disk-frs991e5
CPU_LIMITS: 800m
CPU_REQUEST: 400m
```

Set more available resources in the "product" environment. Set CPU_LIMITS and CPU_REQUEST to 800m (0.8 core) and 400m (0.4 core) respectively.

## Step 5: Create applications for different environments

### Creating an Application
Select the cluster with a namespace in the [Application List][41]. Click the `New` button.

### Selecting the Template and Configuration for the Application
On the New Application page, select the template and configuration for the application.

![应用管理wordpress-26.png-41.7kB][43]

Application name: wordpress-dev
Application description: The application for dev environment
Region: The region to which the cluster belongs in `Step 2`
Cluster: The cluster in `Step 2`
Template: The template created in `Step 1`
Configuration item: The configuration item for the dev environment created in `Step 4`

Click `Next` and re-edit the template content in the application. Since the application template and configuration item are already configured, click `Finish` to complete editing the application content.

![应用管理wordpress-27.png-39.5kB][44]

### Viewing Application Status

You can view the new application on the application list page, but it has not been deployed.

![应用管理wordpress-28.png-17.7kB][45]

### Deploying the Application Service on the Application Details Page

Click the application name to view the details. You can deploy the application on the application details page.

![应用管理wordpress-29.png-30.5kB][46]

Click `Deploy` to deploy the service in the application.

### Viewing Service Information

After the deployment is complete, the deployment and running statuses of the service in the application become `Deployed` and `Running` respectively.

![应用管理wordpress-30.png-37.4kB][47]

For more information on the service, click on the service name to redirect to the service details page.

![应用管理wordpress-31.png-48.7kB][48]

### Access Service Testing

You can initiate a request for service access by using the public IP and service port in WordPress.

![应用管理wordpress-32.png-62kB][49]

The WordPress application is deployed in the dev (development) environment.

### Deploying the Application in Different Environments

Select the configurations for different environments when configuring the application, and then the application is deployed to different environments. After the deployment is completed, you can view the application information in the application list.

![应用管理wordpress-33.png-28.9kB][50]

The application is deployed to different environments based on the same application template and the configuration information under different environments.

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
