Similar to the "Hello World" example, "nginx" is one of the most basic services and one of the most basic applications. This example shows how to create a nginx application template of "Hello World".

## Step 1: Create an application template

In the [Application Template][1] list, click the **New** button.

## Step 2: Edit the application template

### 2.1 Add nginx service**

A service is added to an application template by importing the corresponding template content. The service template content can be imported on the console or from YAML file.

>**Note:**
>You can select either one of the above methods depending on different scenarios.

For more information on how to import the service, please see [Application Template Operation Instructions][4].

**Method 1: Import service on the console**

Click the **Import service from UI** button, and enter corresponding parameters in the corresponding console that popped up.

![应用模板nginx示例-014.png-78kB][import]
The parameters to be set in the `nginx` service include:

Basic information:
1. Service name: `nginx`
2. Service description: `nginx service`

Volume information:
3. Unused data disk: None

Image parameters:
4. Set image parameters in the running parameters of the container:
Container name: `nginx`
Image name: `nginx`
Tag: `latest`

The number of pods:
5. Number of pods: 1

Access method:
6. Access method: In-cluster access
7. Access port: Set both container port and service port to 80

For more information on parameter settings, please see [Create Service][7].

After configuring the parameters, click the `Finish` button, and the console automatically imports the template content of the service.

**Method 2: Import service from YAML file**

If a YAML file of the template content corresponding to the service exists, you can directly import the template content into the edit box as follows:

**Step 1: Create a service**
Click the **Add empty service** button to add a service. Set the service name to `nginx`.

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

In this example, the parameter `namespace` is substituted with `NAMESPACE` as a variable. For more information on variable substitution, please see [Variable Substitution][7].
Details are shown as follows:

![应用模板nginx示例-017.png][show]



## Step 3: Complete editing and view the application template

After you have completed the editing of the application template in step 2, click the `Finish` button to save it. Now, the application template is created. You can view it in the application template list.
Next, you can deploy the application service using the created template. For more information on how to deploy services using application template, please see [Create Application][16]. For more information on how to deploy application using the `nginx` application template, please see [Application Template Example - Nginx Single Service Application][17].

[1]: https://console.cloud.tencent.com/ccs/template
[import]:https://mc.qcloudimg.com/static/img/3edab39e7f0dff61d121dc6b0cca6892/image.png
[show]:https://mc.qcloudimg.com/static/img/7d19bbccbcf86d5514d2f92562444bff/image.png

[16]: https://cloud.tencent.com/document/product/457/11942
[17]: https://cloud.tencent.com/document/product/457/11952
