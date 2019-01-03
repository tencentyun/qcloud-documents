Guestbook is a typical web application service, and consists of a frontend service and two backend storage services, redis-master and redis-slave. Data submitted by users through the web frontend is written into redis-master and synced to redis-slave. The synced data is then read and presented to users.

[Guestbook Application Template][1] describes how to store the deployment information of `Guestbook` using template. This example shows how to quickly deploy `Guestbook application` with a created template.

## Step 1: Create Guestbook application template

When creating a template of Guestbook application, refer to [Guestbook application template][2]

## Step 2: Create an application

Click the **New** button in the [Application List][3].

![应用guestbook示例-009.png][4]

## Step 3: Configure the application

After an application is created, go to the application configuration page and perform the following operations:

1. Enter application name and description.
2. Select the region and cluster to which the application needs to be deployed.

![应用guestbook示例-10.png][5]

Click **Next** to go to the application editing page where you can modify the application template and configuration items.

1. Select an application template. Here, we choose the template `Guestbook` you just created.
2. Select configuration item. You can use the default configuration item in the template or the specific configuration item as needed. Here we choose the default configuration item in the template.
![应用guestbook示例-10.png][6]

>**Note:**
>When you create an application, a duplicate is copied from the application template. When you update the template content in the application, the modified content cannot be synced to the original application template.

## Step 4: Edit the application

In the process of application editing, you can modify the template content and configuration files according to the requirement for the application. Since the content in the template has been edited, no additional modification is needed. Click `Finish` button to complete the editing. For more operations on application editing, please see [Application Template Operation Instructions][6].

![应用guestbook示例-011.png][7]

This application is created upon the completion of application editing. It can be found on the application list page. However, the application is not yet deployed. Click the name of the application to go to its details page, and deploy the services in the application.

## Step 5: Deploy services in the application

In the application details page, the status of all services is `Not Deployed`. Click **Deploy** button to deploy the services.

![应用guestbook示例-016.png][9]

Check whether the status for all services in the application is changed to "Launching".

![应用guestbook示例-013.png][10]

By clicking the name of a service in the application, you are directed to the service page to view its details.

![应用guestbook示例-014.png][11]

## Step 6: Access the deployed application

Access the frontend service using the load balancer IP of `frontend` service.

![应用guestbook示例-015.png][13]


  [1]: https://cloud.tencent.com/document/product/457/11951
  [2]: https://cloud.tencent.com/document/product/457/11951
  [3]: https://console.cloud.tencent.com/ccs/application
  [4]: https://mc.qcloudimg.com/static/img/f94effc7b5ec3cdcd9821c27ea6b2871/image.png
  [5]: https://mc.qcloudimg.com/static/img/4e6d2c9483b595a773ef7bc9fe70d57b/image.png
  [6]: https://mc.qcloudimg.com/static/img/8e4e1a1d62d87803bb220cdb33fbeb07/image.png
  [7]: https://mc.qcloudimg.com/static/img/6529c013018af4adfb2dcdf2ae030085/image.png
  [9]: https://mc.qcloudimg.com/static/img/bc929d90e0ee89ef24d8c2bdf3bcff63/image.png
  [10]:https://mc.qcloudimg.com/static/img/0cb66aea86f1db958db13ebbee05f563/image.png
  [11]: https://mc.qcloudimg.com/static/img/c9c0ca79b3fe41d9a33bebfec53d7b74/image.png
  [12]: https://mc.qcloudimg.com/static/img/059891cc1b9177964366b4dcf97c2bcc/image.png
  [13]: https://mc.qcloudimg.com/static/img/d45bb96194851eed18b07acbf8c23121/image.png
