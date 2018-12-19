## Set the Service to Be Activated upon Boot
### Usage Scenarios
We hope there is no manual intervention in the whole process of scale-up via auto scaling. Thus, we strongly recommend that you set the service to be activated on boot for the machine for auto scaling. The services include:

-**httpd** service
-**mysqld** service
-**php-fpm** service
-**tomcat** service
- etc.

The setting can be done within one minute - Modify the file /etc/rc.d/rc.local!

### Setting Method (taking centos as an example):


#### Step 1:  Open file "rc.local"
Input

    vim /etc/rc.d/rc.local

Do not change the existing contents and add contents at the end of the file.

> Here is the detailed operation for starters **(experienced users may skip this)**:
>
>Input "i" to enter the insert mode of vim, and then you can press the direction key "↓" to reach the end of the file and enter the content.


#### Step 2:  Input the service to be activated

This example demonstrates how to set the services httpd, mysqld and php-fpm to be activated upon boot on the built website. So the sentences below are added behind rc.local:

    service httpd start
    service mysqld start
    service php-fpm start

![](https://mc.qcloudimg.com/static/img/db828b166419cd933e13573c8838a6aa/image.jpg)

Save and exit. Then, these services will be accessed automatically by the website after the server is booted. Please note that different websites require different services. Set services in this step according to your needs.


> Operation TIPS **(experienced users may skip this):**
>
After entering the content, press the Esc key, **hold down the Shift key and press "Z" twice** to exit, that is, inputting ZZ.


#### Step 3: Verification (optional)
Reboot the server (Input reboot, or reboot the server in the console). After the server is rebooted, refresh the webpage on the website first without entering the server to see if there is a response. If there is a response, it means the setting is successful.

#### Step 4: Create an image based on this machine and use this image when creating scaling configurations
This step is simple. Refer to the guides below if you have problems with the operation:

[Create Custom Image](https://intl.cloud.tencent.com/document/product/213/4942)

[Create Scaling Configurations](https://cloud.tencent.com/document/product/377/8544)



