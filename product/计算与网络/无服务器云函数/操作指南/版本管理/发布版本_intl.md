After configuring an SCF, submitting code, and performing online test, you can release a fixed version of SCF to avoid online business errors or execution failures caused by subsequent code modification and test.

## $LATEST Version

The attribute of $LATEST version is given to a SCF during creation of the SCF. $LATEST version refers to the current editable version. $LATEST version exists as an editable version in the whole lifecycle of an SCF. 

## Releasing a Version

You can release a version at any time. The $LATEST version is released as the latest version every time a version of SFC is released.

Click **Release** on the SCF page, enter the release description, and then click **OK** to complete the release of an SCF version.

The configuration and code of the $LATEST version of SCF are replicated and saved as version information in the SCF platform.

> **Note:**
The fixed release only records the configuration and code of the $LATEST SCF version, but does not record its trigger configuration. The newly released version has no triggers.

Releasing a version will generate a version number. The initial version number is 1. The subsequent version number is increased by an increment of 1 for each release.

## Viewing a Version

In the version selection drop-down menu at the upper right corner of the SCF page, you can select the desired version to view its function configuration and code.

After that, the function configuration, code, triggers, logs, and monitoring information of the selected release display. The function configuration and code remain the same as they are released, and they cannot be edited or changed. Triggers may vary for different versions. Logs and monitoring information are the specific call logs and monitoring data of the selected release.

## Use of Versions

Releasing a fixed version can keep function configurations and codes unchanged so as to protect businesses from being affected by development and tests. You are recommended to release a fixed version after completion of development and tests and bind triggers to it for actual business. You can use the $LATEST version to develop and test codes.

### Triggers for different versions

You can bind different triggers to different versions of SCFs. As versions of the same SCF are separate from each other, each trigger can only trigger the SCF to which it is bound.

You can bind a maximum of 2 triggers of each type to an SCF. For example, if you have bound two COS triggers to version 1 of SCF demo1, you can only bind timed and CMQ Topic triggers to other versions of SCF demo1, while no other COS triggers are allowed to be bound to.

The limit that at most 2 triggers of each type can be bound to an SCF only applies to the triggers displayed on the SCF Triggers page. SCF triggers for other products and services are not limited. For example, for SCFs triggered by API gateways, you can configure as many APIs as possible to trigger an SCF.

> Quota increase: If you need to increase the trigger quota, [submit a ticket](https://console.cloud.tencent.com/workorder/category) to apply for a higher quota.

### Cloud API Trigger

When you use Cloud API InvokeFunctioncalling to trigger the calling of an SCF, you can specify a particular version to trigger by using the optional parameter Qualifier. If this parameter is not used, the $LATEST version is triggered by default.



