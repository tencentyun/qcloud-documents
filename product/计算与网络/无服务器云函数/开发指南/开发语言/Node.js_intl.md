The following Node.js programming language versions are supported:

* Node.js 6.10
* Node.js 8.9

## Function Form

The form of Node.js function is generally as follows:

```
exports.main_handler = (event, context, callback) => {
    console.log("Hello World")
    console.log(event)
    console.log(context)
    callback(null, event); 
};
```

## Execution Method

When creating an SCF, you need to specify the execution method. When using Node.js, the execution method is similar to `index.main_handler`, where `index` indicates that the entry file to be executed is `index.js` and `main_handler` indicates that the entry function to be executed is `main_handler` function. When submitting a code zip package using local zip file upload and COS upload, make sure that the root directory of the zip package contains the specified entry file and the file contains the defined entry function. File name and function name must be same with those entered in execution method to avoid execution failures caused by the inability to find the entry file and entry function.

## Input Parameter

The input parameters in the Node.js environment include event, context and callback, where callback is an optional parameter.
* event: Passes triggering event data.
* context: Passes runtime information to your processing program.
* callback: Returns the information to the caller based on your needs. If this parameter is not specified, null is returned.

## Return and Exception

The input parameter `callback` is required for your processing program to return information. The syntax for `callback` is:

```
callback(Error error, Object result);
```

Where:

* error: Optional. Returns the error message when the function execution fails internally. It can be set to null for successful executions.
* result: Feasible parameter. Returns the successful execution result of the function. The parameter needs to be compatible with JSON.stringify for JSON format serialization.


The processing methods of returned values vary depending on the call type of the function. The returned values of synchronous call will be returned to the caller in serialized JSON format, and the returned values of asynchronous call will be discarded. Regardless of synchronous or asynchronous calls, the returned values are displayed in `ret_msg` of the function log.


## Log
You can use the following statement in the program to complete the log output:

* console.log()
* console.error()
* console.warn()
* console.info()

The output can be found in the `log` of the function log.

## Included Libraries and Usage

### COS SDK

[Node.js SDK of COS](https://cloud.tencent.com/document/product/436/8629) (`cos-nodejs-sdk-v5` version) is included in the SCF running environment.

The COS SDK can be introduced and used in the code as follows:


```
var COS = require('cos-nodejs-sdk-v5');
```

For more information on COS SDK, please see [COS Node.js SDK](https://cloud.tencent.com/document/product/436/8629).

