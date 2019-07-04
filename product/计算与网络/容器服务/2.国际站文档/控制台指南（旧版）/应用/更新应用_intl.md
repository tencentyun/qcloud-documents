## Updating Application on the Application List Page

Log in to the [Tencent Cloud TKE Console](https://console.cloud.tencent.com/ccs). View the application list in [Application][1] page. Click **Update** to update the specific application.

![应用更新-06.png][2]

## Updating Methods
You can choose to update the application 1) by using template; 2) by editing application manually

## Updating Using a Template

This means to select a new application template. Replace the content of the existing service template in the application with the content of a new application template. In the updating method selection page, select "By using template".

![应用更新-08.png][3]

After a corresponding template is selected, choose the specific configuration file as needed. If you want to use default configuration files in the template, select **Default Configuration** button.

After specific configuration files are selected, the updating status of the service is automatically displayed in **Changes** area, and the differences between the updated service template and the existing service template in the application are also displayed. For more information on service differentiation, please see [Manage Services in the Application][4].

## Updating Manually

Use an existing template in the application. However, the configuration items can be selected as needed. If **Default Configuration** is selected, directly use the existing configuration in the application.

![应用更新-09.png][5]

## Editing and Updating Application

For updating selection, click **Next** button. Enter the application editing page. You can make further modifications to the template content and configuration items as needed in the application editing page. For more information on specific operations, please see [Application Template Operation Instructions][6].

>**Note:**
>When you create an application, a duplicate is copied from the application template. The content of the application template directly updated cannot be synced to the original application template.

Click **Finish** button on application updating page to complete the updating process.

## Implementing the Updating of Application

In the application details page, the status of the service in the application is changed from **Deployed** to **Deployed and pending update**. For more information about the service status in your application, please see [Manage Services in the Application][7].

![应用更新-10.png][8]

Click the **Update** button to update the service by using new template content and configuration item. After the service is updated, its status is changed to **Deployed** again.

![应用更新-11.png][9]

>**Note:**
>The services in the application can be updated only when the content of the application template is changed. (If a variable in the configuration file of the application is changed, and it is used in the service template, then the content of the service template is also regarded as being changed.)

  [1]: https://console.cloud.tencent.com/ccs/application
  [2]: https://mc.qcloudimg.com/static/img/032baec148056bed81f60b03b66378d2/image.png
  [3]: https://mc.qcloudimg.com/static/img/613a57f14aa47e0d4b329b69e5289323/image.png
  [4]: https://cloud.tencent.com/document/product/457/11989
  [5]: https://mc.qcloudimg.com/static/img/0f6c15f0d641dbaf3f4083e60bf2f6fa/image.png
  [6]: https://cloud.tencent.com/document/product/457/12199
  [7]: https://cloud.tencent.com/document/product/457/11989
  [8]: https://mc.qcloudimg.com/static/img/5ed504a954fe7fd6cd1bdbb66783e39c/image.png
  [9]: https://mc.qcloudimg.com/static/img/35b0688899d46f3fa2958b7f9606a8bc/image.png
