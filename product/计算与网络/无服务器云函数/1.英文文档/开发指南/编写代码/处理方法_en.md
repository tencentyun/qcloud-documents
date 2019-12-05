When you write SCF code, the first and most important step is to write a method which is executed first when the SCF platform calls a function. To create a method, a common syntax structure should be followed:

```
def method_name(event,context): 
    ...
    return some_value
```

The method of all functions receives fixed input parameters: event and context. Do not delete any fixed input parameter.

## Getting Details of the Input Event from the event Parameter

SCF uses event parameter to pass event data to the function. This parameter is a `Python dict` parameter.

The user first needs to clarify what the function is for. For responding to the event trigger request from a cloud service (for example, uploading a file via COS to trigger the function)? Or for being called by other applications? (for example, implementing a common module)? Or it does not require any input?

In different cases, the value of event is different:

- If the function is triggered by a cloud service, the cloud service will pass the event in a platform-predefined and unchangeable format as the event parameter to the SCF. The user can write code in this format to get necessary information from the event parameter. (For example, when COS triggers the function, the details of Bucket and the files will be passed in [json format](https://cloud.tencent.com/document/product/583/9707#cos-.E8.A7.A6.E5.8F.91.E5.99.A8.E7.9A.84.E4.BA.8B.E4.BB.B6.E6.B6.88.E6.81.AF.E7.BB.93.E6.9E.84) to the event parameter)

- If the cloud function is called by other applications, you can freely define a parameter of dict type between the caller and the function code. The caller passes the data in the agreed format which is then acquired by the function code. For example, the agreed data structure of dict type is `{"key":"XXX"}`. When the caller passes the data `{"key":"abctest"}`, the function code can get the value `abctest` through `event[key]`;

- If the cloud function does not require any input, you can ignore event and context parameters in the code.

## (Optional) Returned Value

Returned value is the result returned after a user uses the `return` statement. The method of returned value is different depending on the call type of the function. For more information on the call types of functions, please see Key Concepts:
- For synchronous function call, SCF will return the value of the `return` statement in the code to the caller. For example, the "Test" button of the Tencent Cloud console calls the function synchronously. So when you use the console to call the function, the console will display the returned value. If nothing is returned in the code, a null value is returned.
- For asynchronous function call, the value is discarded.

For example, consider the following Python sample code.

```
def handler(event, context):
    message = 'Hello {} {}!'.format(event['first_name'], 
                                    event['last_name'])  
    return { 
        'message' : message
    } 
``` 
The code receives the input event from the event parameter and returns a message containing data.

Create a SCF, paste the code above and set the execution method to `index.handler`. After creation, click the "Test" button and run it to see the returned message. For details on how to create a function, see [Step 1: Create Hello World function](https://cloud.tencent.com/document/product/583/9204).
