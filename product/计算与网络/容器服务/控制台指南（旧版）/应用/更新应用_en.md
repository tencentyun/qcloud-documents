## Updating Application on the Application List Page

Log in to the [Tencent Cloud CCS Console](https://console.cloud.tencent.com/ccs). View the application list on the **Application Management** -> **[Application][1]** page. Click the `Update` button at the right side, and update the specific application.

![应用更新-06.png][2]

## Updating YAML Directly or Updating from New Template

Updating from new template is to select a new application template and replace the content of the existing service template in the application with the content of the new one. On the updating method selection page, select **Import from template**, or directly edit Yaml content to update the application.

![应用更新-08.png][3]

## Viewing Application Changes

Select an updated item, and click `Next` button to view the changes of this update.
![应用更新-查看变更][4]

>**Note:**
>When you create an application, a duplicate is copied from the application template. The content of the application template updated directly cannot be synced to the original application template.

Click `Finish` button on application updating page to complete the updating process.

## Implementing the Updating of Application

On the application details page, the status of the service in the application is changed from `Deployed` to `Pending update`. For more information on the status of services in application, please see [Manage Services in the Application][7].

![应用更新-10.png][8]
![应用更新-更新][9]
Click the `Update` button to update the service with new template content and configuration items. After the service is updated, its status returns to `Deployed`.


>**Note:**
>The services in the application can be updated only when the content of the application template is changed. (If a variable in the configuration file of the application is changed, and it is used in the service template, then the content of the service template is also regarded as being changed.)

  [1]: https://console.cloud.tencent.com/ccs/application
  [2]: https://mc.qcloudimg.com/static/img/3e0c65b322ed2d00b00740ad5bde061c/image.png
  [3]: https://mc.qcloudimg.com/static/img/f193819c4aa94c38a2ade5424d14fab2/image.png
  [4]: https://mc.qcloudimg.com/static/img/a13f93b7c425aefd1d0886f77e9de288/image.png
  [5]: https://mc.qcloudimg.com/static/img/0f6c15f0d641dbaf3f4083e60bf2f6fa/image.png

  [7]: https://cloud.tencent.com/document/product/457/11989
  [8]: https://mc.qcloudimg.com/static/img/46a5f28849df686e31e3d98a98c91ebd/image.png
  [9]: https://mc.qcloudimg.com/static/img/2ffa4bad944797fd50a85bd47f288eea/image.png
