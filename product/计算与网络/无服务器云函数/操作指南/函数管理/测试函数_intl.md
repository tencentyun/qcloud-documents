SCF's test feature is used to initiate a direct function call on the page, simulate the triggering events sent by the trigger, and display the execution status, returned content, and operation log of the SCF. It can also be used to directly debug the functions and codes on the page.

## Test Operations

After an SCF is created, log in to the console, click **Test**, select and edit the test event template on the pop-up test function page, and finally click the **Run Test** button.

## Test Event Templates

As products iterate, the default test event templates will also increase.

A test event template is used to simulate the events and contents passed to an SCF when an SCF is triggered to run. The events and contents are passed in the form of input parameter event in the function. A test event template must be in JSON format. The followings are the default test event templates and descriptions:

* Hello World event template: A simple, custom event template. With it, you can enter the custom event content when triggering functions through cloud APIs.
* COS file upload and deletion event template: It simulates the events generated and passed when an SCF is triggered because a file is uploaded or deleted in a bucket after a COS trigger is bound.
* CMQ topic event template: It simulates the events generated and passed when an SCF is triggered because a message queue receives messages after CMQ subscription is bound.
* API gateway event template: It simulates the events generated and passed when an SCF is triggered because an API request reaches the API gateway after an API gateway is bound to an SCF.



### Customization of test event templates

Before testing, you can modify the test templates according to your event conditions. The modified test templates will be passed to the function as the event content to trigger the function. The modified test templates must be in JSON format.

### Creating and saving custom test event templates

During testing, you can save the modified test templates as custom templates to avoid modifying them each time you enter the test page. After selecting the template to be modified, click the **New Template** button to modify the template, enter a name, and then save it. When you enter the test page after you have used the modified template, the function template used in the last test appears.

### Deleting custom test event templates

You can delete a custom template by selecting it and clicking the **Delete** button.

## Use Limits

Use limits on custom test event templates are as follows:

- Custom test event templates are account-based. All functions under the same account share the same test event template.
- A maximum of 5 custom test templates can be configured for a single account.
- The maximum size of each custom test template is 64 KB.

