## Overview
Tencent Cloud DNS supports the assignment of sub domain names under the first-level domain name to different projects to manage them. For example, "qcloud.com" belongs to the default project, and you can assign "cloud.tencent.com" to project A, and assign "test.qcloud.com" to project B.

You should note the following:
- The assignment of sub domain names to different projects is only for the domain name itself, while the project relations for domain names of different levels are not affected. For example, if "qcloud.com " belongs to the default project, when you assign "cloud.tencent.com" to project A, "a.cloud.tencent.com" will still belong to the default project instead of being assigned to project A as well.
- The collaborator who has permission over the sub domain name can only perform resolution for this sub domain name. For example, if "qcloud.com" belongs to the default Project, when "cloud.tencent.com" is assigned to project A, the collaborator can only add resolution records such as `www.qlcoud.com` > A record > 8.8.8.8 (host name can only be "www"), but not resolution records for "qcloud.com" and "a.cloud.tencent.com" (host name cannot be "@" or "a.www").
- Current resolution is not affected when domain name is assigned and moved between projects.

## Operation Instructions
### Assign A Sub Domain Name for Which Resolution Is Already Added
1. Method 1
From the domain name record management page, select resolution records to assign projects. In this way,the corresponding sub domain names can be managed after being assigned to specified projects. In the figure below, we select `www.qcloud-example.com` to assign to project.
![](//mc.qcloudimg.com/static/img/60ca6fd590a8c607bfd47df84a362270/image.png)
2. Method 2
Select a first-level domain name, click **Batch Operation** -> **Assign Sub Domain Name to Project**, and enter the sub domain name in the pop-up window to assign it.
![](//mc.qcloudimg.com/static/img/73e344ba533817ca84623d23158dc359/image.png)
![](//mc.qcloudimg.com/static/img/8dc6737c5e6508cf161d19f2776b1f59/image.png)
For example, enter "www" and corresponding resolution records of this host name will be loaded. After sub domain name is assigned to project, the resolution records will follow the sub domain name to the new project without being affected.
![](//mc.qcloudimg.com/static/img/3ec9f9375d56f8e73241c697b4efcb48/image.png)
### Assign A Sub Domain Name for Which Resolution Hasn't Been Added
You can also assign sub domain names for which no resolution has been added yet. For example, enter "test", and you can still assign the sub domain name to project for management although no resolution is added for `test.qcloud-example.com `.
![](//mc.qcloudimg.com/static/img/a5f791477e5bd07ef4be8ce80f80bfb8/image.png)
### Project Permission
In the **Collaborative Sub Domain Name** list, the collaborator of project 123 can perform resolution operations to sub domain names under this project.
![](//mc.qcloudimg.com/static/img/da641d70cf664895938a8e0e302c4aab/image.png)
However, the collaborator can only add resolution for the sub domain names in the **Collaborative Sub Domain Name** list. For example, the collaborator can only add resolution records for "www" and "test", as shown in this figure.
![](//mc.qcloudimg.com/static/img/2118da62aa76deeaf1d7b1d9ed395163/image.png)
Likewise, the collaborator of project 123 can also assign sub domain names that belong to this project. If the collaborator also has permission over project 456, then the collaborator can move the domain names to project 456 as well.
![](//mc.qcloudimg.com/static/img/7071d7046f4aefb376545d77d3cbe6bd/image.png)
Global collaborator can filter the resolution records of first-level domain names according to projects, in order to check which resolutions are added in different projects.
![](//mc.qcloudimg.com/static/img/cd42f9711c42ea0884873a6818aa1e69/image.png)
