## Creating Application Template
 
Log in to the [Tencent Cloud CCS Console](https://console.cloud.tencent.com/ccs), and click **New** on the **Application Management** -> [**Application Template**][1] page.
 
![应用模板列表][createtpl]

## Adding Service in Application Template

A service is added to an application template by importing the corresponding template content. The service template content can be imported on the console or from YAML file.

>**Note:**
>You can select either one of the above methods depending on different scenarios.

For more information on how to import template content, please see [Application Template Operation Instructions][3].

**Method 1: Import service on the console**:

Click the **Import Service** button, and the corresponding console pops up.

![应用模板创建-005.png-76.3kB][4]

Result:
![应用模板创建-006.png-44.8kB][5]

On the console, enter corresponding parameters, then click **OK**, and the service template content is automatically generated. For more information on how to import template content on the console, please see [Application Template Operation Instructions - Import Service on the Console][6].

**Method 2: Import service from YAML file**:

Click **Add Service** button to add a service.

![应用模板创建-007.png-26.5kB][7]

In the service editing box, edit the service content. You can directly copy the template content into the service editing box. The following is the template content of a nginx example. For more information on how to import template from YAML file, please see [Application Template Operation Instructions - Import Template from YAML File][8].

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

In the edit box of the application template content, you can edit and modify the content of corresponding service. For example, you can modify the image tag in the template content from "latest" to "stable".

![应用模板创建-009.png-48.7kB][9]

Template content meets a certain orchestration syntax rule. For more information, please see [Orchestration Syntax Overview][10].
  
## Setting the Configuration Items of Application Template

In the template content, if a parameter varies with different environments or needs to be modified frequently, you can convert it into a configurable variable. For example, you can set the image tag to the variable `IMAGE_VERSION` in the above example, and set the value of `IMAGE_VERSION` in the configuration item to "stable".

The procedure is as follows:

**Step 1: Edit the template content and replace the parameters with variables**
Replace the parameter of the image tag in template content with the variable `IMAGE_VERSION`, as shown below. The format of the variable is "{{.xxxx}}". For more information on variable settings, please see [Variable Settings][11].

![应用模板创建-011.png][12]


**Step 2: Set the values of variables in configuration items**

Set the value of `IMAGE_VERSION` in the configuration item to "stable". In this case, when you deploy the application using the application template, the image tag is "stable" if you use default configuration items in the template. You can also set the variable `IMAGE_VERSION` to different values depending on the requirements for various environments, so as to deploy the application using different image tags under different environments.


## Saving Application Template

After entering the application template content and the default configuration items, click `Finish` button to save the new application template.


## Viewing Created Template

You can view the application template you just created on the [Application Template][16] list page.

![应用模板创建-010.png-39kB][17]


  [1]: https://console.cloud.tencent.com/ccs/template
  [createtpl]: https://mc.qcloudimg.com/static/img/f72ada368e069275051bc9693f677b40/image.png
  [3]: https://cloud.tencent.com/document/product/457/12199
  [4]: https://mc.qcloudimg.com/static/img/5b4226371374d94705cb273b6b2dc005/image.png
  [5]: https://mc.qcloudimg.com/static/img/0f5702315684aefd9d8c69940815adfb/image.png
  [6]: https://cloud.tencent.com/document/product/457/12199#.E6.8E.A7.E5.88.B6.E5.8F.B0.E5.AF.BC.E5.85.A5.E6.9C.8D.E5.8A.A1.E7.9A.84.E6.A8.A1.E6.9D.BF.E5.86.85.E5.AE.B9
  [7]: https://mc.qcloudimg.com/static/img/1688a7e5da5a4363f98cf4b544777e9e/image.png
  [8]: https://cloud.tencent.com/document/product/457/12199#yaml.E6.96.87.E4.BB.B6.E5.AF.BC.E5.85.A5.E6.A8.A1.E6.9D.BF.E5.86.85.E5.AE.B9
  [9]: https://mc.qcloudimg.com/static/img/f2527116281c92eb3953ed9cc0253efe/image.png
  [10]: https://cloud.tencent.com/document/product/457/12200#.E7.BC.96.E6.8E.92.E8.AF.AD.E6.B3.95.E8.83.BD.E5.8A.9B.E8.AF.B4.E6.98.8E
  [11]: https://cloud.tencent.com/document/product/457/11956
  [12]: https://mc.qcloudimg.com/static/img/1941a75697ada897daff0b481fbf32a5/image.png
  [14]: https://mc.qcloudimg.com/static/img/bdad7e3c9ffea42a2b959e8d156b320a/image.png
  [16]: https://console.cloud.tencent.com/ccs/template
  [17]: https://mc.qcloudimg.com/static/img/1fa6890d7a45fcddeb8a2a99767886f8/image.png
