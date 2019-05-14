If an exception occurs during the debugging or running of a function, Tencent Cloud SCF platform will catch the exception as far as possible and write the exception information to log. The exception generated during the running of a function includes handled error and unhandled error. For example, users can explicitly throw an exception in code:

```
def always_failed_handler(event,context):
    raise Exception('I failed!')
```

This function throws an exception in running process and returns the following error message:

```
File "/var/user/index.py", line 2, in always_failed_handler
raise Exception('I failed!')
Exception: I failed!
```
SCF platform will write this error message to the function log.

If you need to test this code, create a function and copy the function code without adding any trigger. Click the "Test" button on the console and select the "Hello World" example to test.

You can define how to deal with potential errors in your code to guarantee your application's robustness and scalability. For example: Inherit Exception class

```
class UserNameAlreadyExistsException(Exception): pass
            
def create_user(event):
    raise UserNameAlreadyExistsException('The username already exists,please change a name!')
```

Or use the Try statement to catch the error:

```
def create_user(event):
    try:
        createUser(event[username],event[pwd])
    except UserNameAlreadyExistsException,e:
        //catch error and do something
```   
     
When the code logic of the user does not catch the error, SCF will catch the error as far as possible. But if the error is one that the platform is unable to catch, such as the user function crashes and exits suddenly in the running process, the system will return a common error message.

The following list provides some common errors during code running

| Error Scenario | Returned Message |
|--|--|
| Throw an exception with raise |	{File "/var/user/index.py", line 2, in always_failed_handler raise Exception('xxx') Exception: xxx} |
| Method does not exist | {'module' object has no attribute 'xxx'} |
| Dependency module does not exist | {global name 'xxx' is not defined} |
| Timeout | {"time out"} |
