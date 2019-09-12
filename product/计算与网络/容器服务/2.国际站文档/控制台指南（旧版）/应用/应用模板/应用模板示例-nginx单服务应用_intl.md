Similar to the "Hello World" example, "nginx" is one of the most basic services and one of the most basic applications. This example shows how to create a nginx application template of "Hello World".

## Step 1: Create Application Template

In the [Application Template][1] list, click **New**.

![应用模板nginx示例-009.png-39.8kB][2]

## Step 2: Edit Application Template

**2.1 Enter the application name `nginxapp`**

![应用模板nginx示例-010.png-27.5kB][3]

**2.2 Add nginx service**

A service is added to an application template by importing the corresponding template content. Two methods are provided to import service template content: 1. import on the console; 2. import from YAML file

>**Note:**
>You can select either one of the methods depending on different scenarios.

For more information on how to import the service, please see [Application Template Operation Instructions][4].

**Method 1: Import service on the console**

Click the "Import Service" button, and enter corresponding parameters in the pop-up Import Service console.

![应用模板nginx示例-014.png-78kB][5]
![应用模板nginx示例-015.png][6]

The parameters to be set in the `nginx` service include:

Basic information:
1. Enter the service name: `nginx`
2. Enter the service description: `nginx service`

Volume information:
3. Unused data disk: None

Image parameters:
4. Set image parameters in the running parameters of the container:
Container name: `nginx`
Image name: `nginx`
Version: `latest`

The number of pods:
5. Number of pods: 1

Access method:
6. Access method: In-cluster access
7. Access port: Set both container port and service port to 80

For more information on parameter settings, please see [Create Service][7].

After configuring the parameters, click the `Finish` button, and the console automatically imports the template content of the service.

![应用模板nginx示例-012.png-39.6kB][8]

**Method 2: Import service from YAML file**

If a YAML file of the template content corresponding to the service exists, you can directly import the template content into the edit box. Proceed as follows:

**Step 1: Create a service**
In the template content editing area, click "+" to add a new service. Set the service name as `nginx`.

![应用模板nginx示例-002.png-39kB][9]

**Step 2: Import the template content**

You can directly copy the following content of the YAML file into the edit box to import the template content of the service.

```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  annotations:
    description: nginx service
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

**Step 3: Extract variables from the template content**

In this example, the parameter `namespace` is replaced with `NAMESPACE` as a variable. For more information on variable substitution, please see [Variable Substitution][10].

Click `Import from the template` button to extract the variable in the template content as the configuration item. Then, enter default value of the variable in the configuration item. Here, it is set to `default`.

Details are shown as follows:

![应用模板nginx示例-017.png][11]

**2.3 Set common parameters as variables**
Some parameters in the template content may be changed frequently or need to be set to different values in different environments. You can set these parameters as variables in the template content and assign values to them in the configuration item. In this way, if a parameter needs to be modified, you only need to modify the configuration item instead of the template content. You can also use different parameters from different configuration item files to deploy applications in different environments.

In this example, we configure the number of pod replicas (`replicas`) as the variable `NGINX_REPLICAS`, the image name as `IMAGE_NAME`, and the image version (`image`) as `IMAGE_VERSION`.

![应用模板nginx示例-018.png][12]

In the Configuration Item of the application template, click the "Import from template" button to automatically extract variables from the template. Assign values to variables: Set `NGINX_REPLICAS` to `2`; `IMAGE_NAME` to `nginx`; and `IMAGE_VERSION` to latest.

![应用模板nginx示例-019.png][13]

## Step 3: Complete Editing and View Application Template

You have completed the editing of the application template in Step 2. Click **Finish** to save the application template. Now, the application template is created. You can view it the application template list.

![应用模板nginx示例-007.png-20.6kB][15]

Next, you can deploy the application service using the created template. For more information on how to deploy services using application template, please see [Create Application][16]. For more information on how to deploy application using the `nginx` application template, please see [Application Template Example - Nginx Single Service Application][17].

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
