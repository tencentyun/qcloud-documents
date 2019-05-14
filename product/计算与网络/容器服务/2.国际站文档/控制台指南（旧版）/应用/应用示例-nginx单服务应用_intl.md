We use nginx single service application as the basic example of application template. The nginx single service is also used as an example for applications.

## Step 1: Create Template of nginx Single Service Application

If the template of nginx single service application does not exist, you need to create one. For more information on how to create a template, please see [Application Template Example - Nginx Single Service Application][1].

You can skip this step if a corresponding application template exists.

## Step 2: Create New Application

Click "New" button in the [Application List][2] to create an application based on the application template.

![应用nginx示例-010.png][3]

## Step 3: Configure Application

After a new application is created, go to the Application Configuration page, where you can make configurations as follows, including:

1. Enter application name and description.

2. Select the region and cluster to which the application needs to be deployed.

3. Select an application template. Here, we choose the template `nginxapp` you just created.

4. Select configuration items. You can use the default configuration item in the template or the specific configuration item as needed. Here we choose the default configuration item in the template.

![应用nginx示例-009.png][4]

Click "Next" to go to the application editing page where you can modify the application template and configuration items.

>**Note:**
>When you create an application, a duplicate is copied from the application template. When you update the template content in the application, the modified content cannot be synced to the original application template.

## Step 4: Edit Application

In the process of application editing, you can modify the template content and configuration files according to the requirement for the application. Since the content in the template has been edited, no additional modification is needed. Click `Finish` button to complete the editing. For more operations on application editing, please see [Application Template Operation Instructions][5].

![应用nginx示例-011.png][6]

This application is already created upon the completion of application editing. The application can be found on the application list page. However, the application is not yet deployed. Click the name of the application to go to its details page, and deploy the services in the application.

![应用nginx示例-012.png][7]

## Step 5: Deploy Services in the Application

1. In the application details page, the status of all services is "Not deployed". Click "Deploy" button to deploy the services.

![应用nginx示例-013.png][8]

2. Deploy the services of the application in cluster, and check whether the status for all services in the application is changed to "Deployed".

![应用nginx示例-014.png][9]

>**Important:**
>For more operations on the services in the application, please see [Manage Services in the Application][11].

3. By clicking the corresponding service in the application, you are directed to the service page to view its details.

![应用nginx示例-015.png][10]

## Step 6: Access deployed application

After the application deployment is completed, you can access the application from the public network on which the service in the application is exposed. Access `nginx` service via open public network load balancer IP and ports.

![应用nginx示例-016.png][13]

  [1]: https://cloud.tencent.com/document/product/457/11945
  [2]: https://console.cloud.tencent.com/ccs/application
  [3]: https://mc.qcloudimg.com/static/img/b69a1f01ddfb2abc05512e324865b8b3/image.png
  [4]: https://mc.qcloudimg.com/static/img/27eda4339af5b2d86959287a4192e783/image.png
  [5]: https://cloud.tencent.com/document/product/457/12199
  [6]: https://mc.qcloudimg.com/static/img/29b8b3c642795c76378a741eeab8b736/image.png
  [7]: https://mc.qcloudimg.com/static/img/5beb99f8f3e1782900d571a9c5466f4b/image.png
  [8]: https://mc.qcloudimg.com/static/img/c13e5aaa41978d7dc8d46d84db8ea85d/image.png
  [9]: https://mc.qcloudimg.com/static/img/a6a26401e6c2d642020eef0113eda339/image.png
  [10]: https://mc.qcloudimg.com/static/img/ad600fc08984247d9201869767afa1d1/image.png
  [11]: https://cloud.tencent.com/document/product/457/11989
  [12]: https://mc.qcloudimg.com/static/img/3aea8dfee04dd0b8beb5a7aa48ce1bf1/image.png
  [13]: https://mc.qcloudimg.com/static/img/40eb6e610d8f57e2da3089ad29564fc9/image.png
