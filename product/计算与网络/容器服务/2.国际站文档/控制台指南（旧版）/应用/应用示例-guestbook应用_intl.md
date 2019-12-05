Guestbook is a typical web application service, and consists of a frontend service and two backend storage services, redis-master and redis-slave. Data submitted by users through the web frontend is written into redis-master and synced to redis-slave. The synced data is then read and presented to users.

[Guestbook Application Template][1] describes how to store the deployment information of `Guestbook` using template. This example shows how to quickly deploy `Guestbook application` with a created template.

## Step 1: Create Guestbook Application Template

When creating a template of Guestbook application, refer to [Guestbook application template][2]

## Step 2: Create New Application

Click "New" button in the [Application List][3].

![应用guestbook示例-009.png][4]

## Step 3: Configure Application

After a new application is created, go to the application configuration page and perform the following operations:

1. Enter application name and description.

2. Select the region and the cluster to which the application needs to be deployed.

3. Select an application template. Here, we choose the template `Guestbook` you just created.

4. Select configuration item. You can use the default configuration item in the template or the specific configuration item as needed. Here we choose the default configuration item in the template.

![应用guestbook示例-10.png][5]

Click "Next" to go to the application editing page where you can modify the application template and configuration items.

>**Note:**
>When you create an application, a duplicate is copied from the application template. When you update the template content in the application, the modified content cannot be synced to the original application template.

## Step 4: Edit Application

In the process of application editing, you can modify the template content and configuration files according to the requirement for the application. Since the content in the template has been edited, no additional modification is needed. Click `Finish` button to complete the editing. For more operations on application editing, please see [Application Template Operation Instructions][6].

![应用guestbook示例-011.png][7]

This application is already created upon the completion of application editing. The application can be found on the application list page. However, the application is not yet deployed. Click the name of the application to go to its details page, and deploy the services in the application.

![应用guestbook示例-012.png][8]

## Step 5: Deploy Services in the Application

In the application details page, the status of all services is "Not deployed". Click "Deploy" button to deploy the services.

![应用guestbook示例-016.png][9]

Check whether the status for all services in the application is changed to "Deployed".

![应用guestbook示例-013.png][10]

By clicking the name of a service in the application, you are directed to the service page to view its details.

![应用guestbook示例-014.png][11]

## Step 6: Access Deployed Application

Access the frontend service using the load balancer IP of `frontend` service.

![应用guestbook示例-015.png][13]


  [1]: https://cloud.tencent.com/document/product/457/11951
  [2]: https://cloud.tencent.com/document/product/457/11951
  [3]: https://console.cloud.tencent.com/ccs/application
  [4]: https://mc.qcloudimg.com/static/img/1d72f8ebdcbbb6559c18a0e4e3650b7e/image.png
  [5]: https://mc.qcloudimg.com/static/img/9f2b15de7a6416830146b6cccee91898/image.png
  [6]: https://mc.qcloudimg.com/static/img/36b6b557c0f66c8879e6ecf61688948f/image.png
  [7]: https://mc.qcloudimg.com/static/img/2f14693c14edc218126f3d2015af4944/image.png
  [8]: https://mc.qcloudimg.com/static/img/04da2c9b6c55fb3bed0086d02172fc6d/image.png
  [9]: https://mc.qcloudimg.com/static/img/0a2637c38a76511120ddd1aada70128c/image.png
  [10]: https://mc.qcloudimg.com/static/img/2b21ccb636b27964ddc760141267e68d/image.png
  [11]: https://mc.qcloudimg.com/static/img/c9c0ca79b3fe41d9a33bebfec53d7b74/image.png
  [12]: https://mc.qcloudimg.com/static/img/059891cc1b9177964366b4dcf97c2bcc/image.png
  [13]: https://mc.qcloudimg.com/static/img/d45bb96194851eed18b07acbf8c23121/image.png
