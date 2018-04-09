
![](//mc.qcloudimg.com/static/img/7156e8674b02fe38cf44b6b2fdcd58fb/image.png)
## About the Platform

XGPush is a professional platform for mobile App push that allows pushing billions of notifications/messages to mobile users within seconds. It supports both Android and iOS, and enables developers to push messages to specific users easily via embedded SDK, API calls or Web-based visualized operations and view the push results in real time, thus greatly improving user activity and waking up inactive users. 

## Definitions of Push Scenarios
### Push notifications
In XGPush product, notification refers to the Notification defined in the Android and iOS developer guides. The server sends messages to the specified mobile phones in real time via a linkage established between the mobile phones and the server.
This is designed to push a message visible to specific users to lead them to perform targeted actions. It is commonly used for such scenarios as product information delivery, news feeds, and personalized messaging.
![](//mc.qcloudimg.com/static/img/b569f541c780b40c09ab17d8e2ee46ae/image.png)
### Local notification
It refers to the Local Notification as defined in the Android developer guide.
An App pushes a visible message to the users by customizing the date, time and message content without going through the server. It is usually used for the local scheduled reminders from Apps, reminders for the end of building upgrades in game Apps, and some scenarios with a specified ending time.
![](//mc.qcloudimg.com/static/img/5e6f817951d4c0127d873803e5146e48/image.png)
For more information, please see the [external API list of XGPushManager for providing XGPush services](https://cloud.tencent.com/document/product/548/13950#xgpushmanager-.E5.8A.9F.E8.83.BD.E7.B1.BB).
### In-app message
The XGPush product allows an App to perform a series of operations at backend by pushing executable code instructions. With this feature, remote control of the App can be realized at the lowest possible cost. The content of the in-App messages pushed is customized by the App developers, and no pup-up notifications are provided for such messages.
In-App message supports a variety of scenarios and can be expanded by developers freely. For example: push the message command to some tagged users; allow the App to download the installation package automatically and upgrade to the latest version when connecting to WiFi; perform incremental update of App quickly; or allow the App to download the installation package and complete the incremental update silently as needed, without disturbing the users who don't need the update.
In addition, in-App messages can either be displayed in the notification bar, or be directly put into the App's message center, which delivers a flexibility much higher than pushing messages in the notification bar.
![](//mc.qcloudimg.com/static/img/f3127b12f5b033803c7f39f7eb4488a7/image.png)![](//mc.qcloudimg.com/static/img/f16962e169adbbdce3441c95e190a109/image.png)
### Tags
In XGPush product, it refers to tagging a group of users, such as iOS users who love food in Beijing, inactive users who have not used the App for more than 30 days, users with high spending potential, and team testing users.
A maximum of 10,000 tags are allowed for an App. Each token can have a maximum of 100 tags under one App. A tag cannot contain any space.
XGPush provides three default tags that can be used directly: geographic locations, application versions, and churned users. 
![](//mc.qcloudimg.com/static/img/dd7012aaa5f124e84db20967ceeca8ff/image.png)
### Account
In XGPush product, an alias/account is used to push messages to a specific user. The alias/account can be a QQ number, openid, email account or mobile number reported by the terminal during registration.
Please note that if you want to push messages to an account, you need to bind the account to the token first. Otherwise, you cannot push to the account successfully. For more information on how to bind the account to token, please see the [guide for connection to Android and iOS - push by account](https://cloud.tencent.com/document/product/548/13951#.E7.BB.91.E5.AE.9A.E8.B4.A6.E5.8F.B7.E6.B3.A8.E5.86.8C).
A maximum of 15 device tokens can be bound to an account. If the limit is exceeded, the latest token randomly override a previously bound one. 
![](//mc.qcloudimg.com/static/img/643897a0b559df65f41ac1a88452953a/image.png)







