The following Python programming language versions are supported:
* Python 2.7
* Python 3.6

## Function Form

The form of Python function is generally as follows:
```python
import json

def main_handler(event, context):
    print("Received event: " + json.dumps(event, indent = 2)) 
    print("Received context: " + str(context))
    return("Hello World")
```

## Execution Method

When creating an SCF, you need to specify the execution method. When using Python, the execution method is similar to `index.main_handler`, where `index` indicates that the entry file to be executed is `index.py` and `main_handler` indicates that the entry function to be executed is `main_handler` function. When submitting a code zip package using local zip file upload and COS upload, make sure that the root directory of the zip package contains the specified entry file and the file contains the defined entry function. File name and function name must be same with those entered in execution method to avoid execution failures caused by the inability to find the entry file and entry function.

## Input Parameter

The input parameters in the Python environment include event and context, both of which are of Python dict type.
* event: Passes triggering event data.
* context: Passes runtime information to your processing program.

## Return and Exception

Your processing program can return values using `return`. The processing method of returned values varies depending on the call type of the function.
* Synchronous call: In case of a synchronous call, the returned values are serialized and returned to the caller in JSON format. The caller can obtain the returned values for subsequent processing. For example, the call method for function debugging via the console is a synchronous call, which can capture and display the values returned by the function after the call is completed.
* Asynchronous call: For asynchronous call, because the call method returns a value just after the function is triggered and does not wait for the function to complete its execution, the returned value of the function will be discarded.

Regardless of synchronous or asynchronous calls, the returned values are displayed in `ret_msg` of the function log.

You can throw exceptions within a function using `raise Exception`. The thrown exceptions will be captured in the function running environment and displayed in the log in the form of `Traceback`.

## Log
You can use `print` or the `logging` module in your program to accomplish log output, as shown in the following function:
```python
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
def main_handler(event, context):
    logger.info('got event{}'.format(event))
    print("got event{}".format(event))
    return 'Hello World!'  
```

The output can be found in the `log` of the function log.


## Included Libraries and Usage

### COS SDK

[Python SDK of COS](https://cloud.tencent.com/document/product/436/6275) (`cos_sdk_v4` version) is included in the SCF running environment.

The COS SDK can be introduced and used in the code as follows:
```
import qcloud_cos
```

```
from qcloud_cos import CosClient
from qcloud_cos import DownloadFileRequest
from qcloud_cos import UploadFileRequest
```

For more information on COS SDK, please see [COS Python SDK](https://cloud.tencent.com/document/product/436/6275).

## Python 2 or 3?
When creating a function, you can select the desired running environment by choosing between `Python 2.7` or `Python 3.6`.

Python's official suggestions on selection of Python 2 or Python 3 can be found [here](https://wiki.python.org/moin/Python2orPython3).


