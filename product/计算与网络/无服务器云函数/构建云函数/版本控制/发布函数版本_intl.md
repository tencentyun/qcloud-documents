After configuring the cloud function, submitting code, and performing online test, you can create a version of the cloud function by releasing it to avoid online business errors or execution failures caused by subsequent code modification and test.

## $LATEST Version

The attribute of $LATEST version is provided to a cloud function when it is created. The $LATEST version points to the current editable version, and it exists in the whole lifecycle of cloud function as an editable version. 

## Publishing Version

You can publish a version at any time. Any release of cloud function is to publish $LATEST version as the latest version.

Click the **Publish** button on the function interface, enter the release description, and click **OK** to complete the release of the cloud function version.

The cloud function platform will make a copy of the configuration and code content of the $LATEST version of the current function, and save it as version content.

> **Note:**
The published version only records and fixes the configuration and code of the $LATEST version of the current function, but does not record the trigger configuration of the function. The newly published function version does not have any triggers.

After a version is released, the version number of the release is generated, which starts from 1 and increases progressively with each release. The version number has no upper limit.

## Viewing Version

You can use the version selection drop-down menu in the upper right corner of the function interface to switch to the desired version to view the function configuration and code.

On the released version interface, the specific function configuration, code, trigger, log, and monitoring information are displayed. Where, the function configuration and code remain in the same status as they are at the time of release, and the status cannot be edited or changed. Triggers may have different configurations in different versions. The log and monitoring content are respectively the specific call logs and monitoring data of the corresponding version.

## Using Version

The version feature is mainly used for fixing of function configuration and code to avoid the impact on the business caused by developing and test. It is recommended to publish a version after the developing and test is completed, and then bind the trigger with the released version to run the actual business. The $LATEST version continues to be used for further code developing and debugging as a version for developing and test.

### Version Trigger

Triggers can be independently bound to all released versions of cloud functions. The versions of the same function is independent among each other, and each trigger can independently trigger the function to run.

As to the limit on the number of triggers, a maximum of 2 triggers of each type can be bound. The limit is set based on the single function of cloud function. For example, if two COS triggers are bound on version 1 of the function demo1, the COS triggers cannot be bound to other versions of this function, and only timer triggers or CMQ Topic triggers can be bound.

The upper limit of 2 triggers of each type only covers the triggers configured on the cloud function trigger page. The cloud function triggers configured in other products or services are not subject to the limit. For example, for the cloud function triggered by API gateway, as many APIs as needed can be configured to trigger the same cloud function.

> Quota increase: If you need to increase the trigger quota, please [submit a ticket](https://console.cloud.tencent.com/workorder/category) to apply.

### Cloud API Trigger

When calling of a cloud function is triggered by the cloud API InvokeFunction, the specific version to be triggered can be specified using the optional parameter Qualifier. If this parameter is not used, the $LATEST version is triggered by default.



