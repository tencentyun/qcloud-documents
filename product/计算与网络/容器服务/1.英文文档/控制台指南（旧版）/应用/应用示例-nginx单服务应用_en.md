In this document, we create an application template for an Nginx application with one service, and 

## Step 1: Create a template for Nginx application with one service

If the template of nginx single service application does not exist, you need to create one. For more information on how to create a template, please see [Application Template Example - Nginx Single Service Application][1].

You can skip this step if a corresponding application template exists.

## Step 2: Create an application

Click **New** button in the [Application List][2] to create an application based on the application template.

![应用nginx示例-010.png][create]

## Step 3: Configure the application

After an application is created, go to the Application Configuration page, where you can make configurations as follows:

1. Enter application name and description.
2. Select the region and cluster to which the application needs to be deployed.

![应用nginx示例-009.png][create2]

Click **Next** to go to the application editing page where you can modify the application template and configuration items.
1. Select an application template. Here, we choose the template `nginx` you just created.
2. Select configuration item. You can use the default configuration item in the template or the specific configuration item as needed. Here we choose the default configuration item in the template.

>**Note:**
>When you create an application, a duplicate is copied from the application template. When you update the template content in the application, the modified content cannot be synced to the original application template.

## Step 4: Edit the application

In the process of application editing, you can modify the template content and configuration files according to the requirement for the application. Since the content in the template has been edited, no additional modification is needed. Click `Finish` button to complete the editing. For more operations on application editing, please see [Application Template Operation Instructions][5].

![应用nginx示例-011.png][6]

This application is created upon the completion of application editing. It can be found on the application list page. However, the application is not yet deployed. Click the name of the application to go to its details page, and deploy the services in the application.
## Step 5: Deploy services in the application

1. In the application details page, the status of all services is `Not Deployed`. Click `Deploy` button to deploy the services.

![应用nginx示例-013.png][8]

2. Deploy the services of the application in cluster, and check whether the status for all services in the application is changed to "Launching".

![应用nginx示例-014.png][9]

>**Important:**
>For more operations on the services in the application, please see [Manage Services in the Application][11].

3. By clicking the corresponding service in the application, you are directed to the service page to view its details.

![应用nginx示例-015.png][10]

## Step 6: Access the deployed application

After the application is deployed, it can be accessed using the open public network address in the application service. `nginx` service can be accessed via open public network load balancer IP and ports.

![应用nginx示例-016.png][13]

  [1]: https://cloud.tencent.com/document/product/457/11945
  [2]: https://console.cloud.tencent.com/ccs/application
  [3]: https://mc.qcloudimg.com/static/img/b69a1f01ddfb2abc05512e324865b8b3/image.png
  [4]: https://mc.qcloudimg.com/static/img/27eda4339af5b2d86959287a4192e783/image.png
  [5]: https://cloud.tencent.com/document/product/457/12199
  [6]: https://mc.qcloudimg.com/static/img/68364f4d1cc623615e0ddc01b9f302ac/image.png

  [8]: https://mc.qcloudimg.com/static/img/0bb4b714e791dc5c8ade33e2b1dea3d7/image.png
  [9]: https://mc.qcloudimg.com/static/img/189cb4d6c49b3f9605c641045894b101/image.png
  [10]: https://mc.qcloudimg.com/static/img/ad600fc08984247d9201869767afa1d1/image.png
  [11]: https://cloud.tencent.com/document/product/457/11989
  [12]: https://mc.qcloudimg.com/static/img/3aea8dfee04dd0b8beb5a7aa48ce1bf1/image.png
  [13]: https://mc.qcloudimg.com/static/img/40eb6e610d8f57e2da3089ad29564fc9/image.png
  [create]: https://mc.qcloudimg.com/static/img/193ee99a7ccaff383b87ef2491a4468c/image.png
  [create2]: https://mc.qcloudimg.com/static/img/9bef862af44c4b1acc3a571589ebf71f/image.png
