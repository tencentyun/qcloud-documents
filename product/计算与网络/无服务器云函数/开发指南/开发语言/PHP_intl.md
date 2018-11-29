The following PHP programming language versions are supported:

* PHP 5.6
* PHP 7.2

## Function Form

The form of PHP function is generally as follows:

```
<?php

function main_handler($event, $context) {
    echo("hello world");
    print_r($event);
    return "hello world";
}

?>

```

## Execution Method

When creating an SCF, you need to specify the execution method. When using PHP, the execution method is similar to `index.main_handler`, where `index` indicates that the entry file to be executed is `index.php` and `main_handler` indicates that the entry function to be executed is `main_handler` function. When submitting a code zip package using local zip file upload and COS upload, make sure that the root directory of the zip package contains the specified entry file and the file contains the defined entry function. File name and function name must be same with those entered in execution method to avoid execution failures caused by the inability to find the entry file and entry function.

## Input Parameter

The input parameters in the PHP environment include $event and $context.

* $event: Passes triggering event data.
* $context: Passes runtime information to your processing program.

## Return and Exception

Your processing program can return values using `return`. The processing method of returned values varies depending on the call type of the function.

* Synchronous call: In case of a synchronous call, the returned values are serialized and returned to the caller in JSON format. The caller can obtain the returned values for subsequent processing. For example, the call method for function debugging via the console is a synchronous call, which can capture and display the values returned by the function after the call is completed.
* Asynchronous call: For asynchronous call, because the call method returns a value just after the function is triggered and does not wait for the function to complete its execution, the returned value of the function will be discarded.

Regardless of synchronous or asynchronous calls, the returned values are displayed in `ret_msg` of the function log.

In the function, you can exit the function by calling die(). Then the function will be marked as failed and the log will also record the output when the function exits using die().

## Log
You can use the following statement in the program to complete the log output:

* echo or echo()
* print or print()
* print_r()
* var_dump()

The output can be found in the `log` of the function log.


