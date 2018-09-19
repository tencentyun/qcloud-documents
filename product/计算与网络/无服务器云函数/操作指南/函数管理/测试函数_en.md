The test feature of cloud function is used to initiate a direct function call on the page, simulate the triggering events sent by the trigger, and display the execution status, returned content, and operation log of the cloud function, and can also be used to directly debug the functions and codes on the page.

## Test Operation

After a cloud function is created, log in to the console, click **Test**, select and edit the test event template on the pop-up test function page, and finally click the **Run Test** button.

## Test Event Template

As new versions are released, the default test event templates will increase continuously.

The test event template is used to simulate the events and contents passed to the cloud function when the cloud function is triggered by the corresponding trigger. The events and contents are passed as the event parameter in the function. The data structure of the test event template must be JSON format. Here are the default test event templates and descriptions:

* Hello World Event Template: A simple, custom event template. With it, you can enter the custom event content when triggering functions through the Cloud APIs.
* COS File Upload and Deletion Event Template: It simulates the binding with a COS trigger, and then the events generated and passed in the cloud function will be triggered when a file is uploaded into the Bucket or a file in the Bucket is deleted.
* CMQ Topic Event Template: It simulates the binding with the CMQ subscription, and then the events generated and passed in the cloud function will be triggered when CMQ receives a message.
* API Gateway Event Template: It simulates the binding of the API gateway with the cloud function, and then the events generated and passed in the cloud function will be triggered when an API request reaches the API gateway.



### Test Event Template Customization

Before the test, you can modify the test templates according to your own event conditions. The modified test templates will be passed to the function as the event content to trigger the function. The modified test templates must be in JSON format.

### Creating and Saving Custom Test Event Template

To avoid the trouble of modifying the templates each time entering the test interface, you can save the modified test template as the custom template. After selecting the template to be modified, click the **New Template** button to modify the template, and save it. If the saved template is used for testing once, it will appear on the test interface when you enter this page again.

### Deleting Custom Test Event Template

If a custom template is no longer used, you can select it and click the **Delete** button to delete it.

## Service Limits

Service limits on custom test event templates is as follows:

- Custom test event templates are account-based. All functions under the same account share the same test event template.
- A maximum of 5 custom test templates can be configured for a single account.
- The maximum size of each custom test template is 64 KB.

