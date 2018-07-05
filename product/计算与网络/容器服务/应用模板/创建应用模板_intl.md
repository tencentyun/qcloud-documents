## Creating Application Template
 
Log in to the [Tencent Cloud TKE Console](https://console.cloud.tencent.com/ccs). Click **New** on the [Application][1] page.
 
![Application Template List][2]

## Adding Service in Application Template

A service is added to an application template by importing the corresponding template content. Two methods are provided to import service template content: 1. import on the console; 2. import from YAML file

>**Note:**
>You can select either one of the methods depending on different scenarios.

For more information on how to import template content, please see [Application Template Operation Instructions][3].

**Method 1: Import service on the console**:

Click **Import Service**, and the Import Service console pops up.

![应用模板创建-005.png-76.3kB][4]

![应用模板创建-006.png-44.8kB][5]

On the console, enter corresponding parameters, then click **OK**, and the service template content is automatically generated. For more information on how to import template content on the console, please see [Application Template Operation Instructions - Import Service on the Console][6].

**Method 2: Import service from YAML file**:

Click **+** to add service.

![应用模板创建-007.png-26.5kB][7]

In the service editing box, edit the service content. You can directly copy the template content to the service editing box. The following is the template content of a nginx example. For more information on how to import template from YAML file, please see [Application Template Operation Instructions - Import Template from YAML File][8].

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
  - name: tcp-80-80-ai6zd
    nodePort: 0
    port: 80
    protocol: TCP
    targetPort: 80
  selector: {}
  type: LoadBalancer
status:
  loadBalancer: {}
```

## Editing Application Template Content

In the edit box of the application template content, you can edit and modify the content of corresponding service. For example, you can modify the image version in the template content from "latest" to "stable".

![应用模板创建-009.png-48.7kB][9]

Template content meets a certain orchestration syntax rule. For more information, please see [Orchestration Syntax Overview][10].
  
## Setting the Configuration Items of Application Template

In the template content, if a parameter varies with different environments or needs to be modified frequently, you can convert the parameter into a configurable variable. For example, you can set the image version to the variable `IMAGE_VERSION` in the above example, and set the value of `IMAGE_VERSION` in the configuration item to "stable".

The procedure is as follows:

**Step 1: Edit the template content and replace the parameters with variables**
Replace the parameter of the image version in template content with the variable `IMAGE_VERSION`, as shown below. The format of the variable is `{{.xxxx}}`. For more information on variable settings, please see [Variable Settings][11].

![应用模板创建-011.png][12]

**Step 2: Extract variables in the template as configuration items**

In configuration item area, click **Import from the template** button to extract the variables in the template as configuration items.

![应用模板创建-012.png][13]

**Step 3: Set the variables in configuration items**

Set the value of `IMAGE_VERSION` to "stable" in configuration items. In this case, when you deploy the application using the application template, the image version is `stable` if you use default configuration items in the template. You can also set the variable `IMAGE_VERSION` to different values depending on the requirements for various environments, so as to deploy the application using different image versions under different environments.

![应用模板创建-013.png][14]

## Saving Application Template

After entering the application template content and the default configuration items, click "Finish" button to save the new application template.

![应用模板创建-008.png-24.8kB][15]

## Viewing Created Template

You can view the application template you just created on the [Application Template][16] list page.

![应用模板创建-010.png-39kB][17]


  [1]: https://console.cloud.tencent.com/ccs/template
  [2]: https://mc.qcloudimg.com/static/img/916facfa358f0ab96524c2e644a3b223/image.png
  [3]: https://cloud.tencent.com/document/product/457/12199
  [4]: https://mc.qcloudimg.com/static/img/e071d917c7f3b06ccaca50700e42d233/image.png
  [5]: https://mc.qcloudimg.com/static/img/c6f4b27b1b49cfe17f4f3ba91286c28c/image.png
  [6]: https://cloud.tencent.com/document/product/457/12199#.E6.8E.A7.E5.88.B6.E5.8F.B0.E5.AF.BC.E5.85.A5.E6.9C.8D.E5.8A.A1.E7.9A.84.E6.A8.A1.E6.9D.BF.E5.86.85.E5.AE.B9
  [7]: https://mc.qcloudimg.com/static/img/bcacd95ac7545135efabfbee1b802f37/image.png
  [8]: https://cloud.tencent.com/document/product/457/12199#yaml.E6.96.87.E4.BB.B6.E5.AF.BC.E5.85.A5.E6.A8.A1.E6.9D.BF.E5.86.85.E5.AE.B9
  [9]: https://mc.qcloudimg.com/static/img/339429c850d4d5359d018202b60ed534/image.png
  [10]: https://cloud.tencent.com/document/product/457/12200#.E7.BC.96.E6.8E.92.E8.AF.AD.E6.B3.95.E8.83.BD.E5.8A.9B.E8.AF.B4.E6.98.8E
  [11]: https://cloud.tencent.com/document/product/457/11956
  [12]: https://mc.qcloudimg.com/static/img/f15c3759fcb010aefabc8bf82a4e755a/image.png
  [13]: https://mc.qcloudimg.com/static/img/6881a3715cd30420b3f9f10f8c9397dc/image.png
  [14]: https://mc.qcloudimg.com/static/img/bdad7e3c9ffea42a2b959e8d156b320a/image.png
  [15]: https://mc.qcloudimg.com/static/img/434bace9cc2026205ec300299e2c1a47/image.png
  [16]: https://console.cloud.tencent.com/ccs/template
  [17]: https://mc.qcloudimg.com/static/img/ee06586b2b4743920a45a4e62918ba06/image.png
