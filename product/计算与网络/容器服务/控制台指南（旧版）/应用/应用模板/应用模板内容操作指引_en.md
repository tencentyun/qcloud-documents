In an application template (or an application), you can save the service deployment information as a template using YAML-based descriptive language for the purpose of reutilization or deployment of different applications in multiple environments. You can import and edit the template content of the service in Template Content field.

You can import the template content by importing service from UI or by adding an empty service.

>**Note:**
>You can select either one of the above methods depending on different scenarios.

**Import from UI**: The parameters of the service you entered on the console are automatically converted to a YAML description file in the template content. It is suitable when no YAML description file is available. **Add empty service**: You can directly copy the content of the existing YAML description file to the template content field. It is suitable when YAML description file is available.


## Template for Importing Service from UI

On the **Create Template** (or **Create Application**) page, click `Import Service from UI` button. The parameters you entered on the console are automatically converted to the service template content.

The parameter settings on **Import Service** page is identical to that on **Create Service** page.
Main parameters include: Basic information, volume, the running parameters of container, number of pods, service access type and port.

For example, to deploy a nginx service, you need to enter the following parameters:

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

For more information on parameter settings, please see [Create Service][4].

After configuring the parameters, click the `Finish` button, and the console automatically imports the template content of the service.
## Adding Empty Service and Importing Template Content

If a YAML file of the template content corresponding to the service exists, you can directly import the template content into the edit box as follows:

**Step 1: Create a service**
Click the "Add empty service" button to add a service.

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
  namespace: default
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
  namespace: default
spec:
  ports:
  - name: tcp-80-80-xoq5o
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

In this example, the parameter `namespace` is substituted with `NAMESPACE` as a variable. For more information on variable substitution, please see [Variable Substitution][7].

The system automatically extracts the variables in the template content as the configuration item. Then, enter default value of the variable in the configuration item. Here, it is set to `default`.

## Editing Template Content

You can directly edit the template content in Template Content field. For example, you can modify the number of service pod replicas to `2` in the template content.

![模板内容操作-01.png][9]

The syntax rule of template content conforms to the Kubernetes syntax. For more information on template content rule, please see [Orchestration Syntax Overview][10].

## Configuring Parameters in Template Content

In the template content, if a parameter varies with different environments or needs to be modified frequently, you can convert the parameter into a configurable variable. For example, the number of service pod replicas above may vary in different environments, so we can convert it to the variable `NGINX_REPLICAS`. For more information on variables in the template, please see [Variable Settings][11].


The system extracts the variables in the template content as the configuration item. Then, enter default value of the variable in the configuration item. Here, it is set to `2`.

You can select different configuration items in different deployment environments as needed, and adjust the number of pods in the service accordingly.

  [1]: https://mc.qcloudimg.com/static/img/4497405adc55f7eaec00774dd28852c7/image.png
  [2]: https://mc.qcloudimg.com/static/img/14eb885cb7632ca3cc716f8ad75459c1/image.png
  [3]: https://mc.qcloudimg.com/static/img/7f9b250c592b2fe84200242d3b092cd6/image.png
  [4]: https://cloud.tencent.com/document/product/457/9096#.E5.88.9B.E5.BB.BA.E6.9C.8D.E5.8A.A1
  [5]: https://mc.qcloudimg.com/static/img/3bf0b1e4e7bbd80d2fe7e79cc77afee4/image.png
  [6]: https://mc.qcloudimg.com/static/img/d605189b3d46f89d029257700b58668b/image.png
  [7]: https://cloud.tencent.com/document/product/457/11956
  [8]: https://mc.qcloudimg.com/static/img/2dc286573bcc698be261f0d17019745e/image.png
  [9]: https://mc.qcloudimg.com/static/img/f7abcee2f2197e7a0d5a39d867089072/image.png
  [10]: https://cloud.tencent.com/document/product/457/12200#.E7.BC.96.E6.8E.92.E8.AF.AD.E6.B3.95.E8.83.BD.E5.8A.9B.E8.AF.B4.E6.98.8E
  [11]: https://cloud.tencent.com/document/product/457/11956
  [12]: https://mc.qcloudimg.com/static/img/1531eb257002f221036adf3c892c99f0/image.png
  [13]: https://mc.qcloudimg.com/static/img/be8495acb9c4628c214b79b25b41b280/image.png
  [14]: https://mc.qcloudimg.com/static/img/0a68386d7bc5957ddf4110fdfdd15a00/image.png
  [15]: https://mc.qcloudimg.com/static/img/8da35376ee2001cc76a1b1e6c2287e33/image.png
