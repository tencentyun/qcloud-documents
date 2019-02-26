This document describes how to use Tencent Cloud CLI after you install and configure it.

## Call Format
The basic syntax to use the Tencent Cloud command line is as follows:
```
qcloudcli <command> <operation> [options and parameters]
```

Where,
- "command" is the name of a command module, such as cvm, cdb, and lb;
- "operation" is the operation supported by the corresponding module, i.e. API name;
- "parameters" are the input parameters supported by the corresponding operation API. The format is: `-- parameter name parameter value`;
- "options" are global options that specify the output format of the result and the user who uses such result. The format is: `--option name option value`.

Here's an example to explain:

```
$ qcloudcli cvm DescribeInstances --status 3 --output table
```
This command outputs the `status 3` CVM instance information of the `default account` in `table` format. Where,

- The module name is `cvm`;
- The API name is `DescribeInstances`;
- Only one input parameter `status` is set to 3;
- The output format of the final result is set to `table` (not the default JSON set during "qcloudcli configure")
![Alt text](https://mc.qcloudimg.com/static/img/e2bd3431211054cf21281085fe137097/image.png)

## Input Parameters in JSON format
"qcloudcli" allows input parameters in JSON format.</br>
When the input parameter is a common array, it needs to be input in the following format:

```
qcloudcli cvm DescribeInstances --instanceIds '["ins-0ljnjsco","ins-p01nc1jg"]'
```
This command outputs two instances with instanceId of `ins-0ljnjsco` and `ins-p01nc1jg` under the default account.
![Alt text](https://mc.qcloudimg.com/static/img/ea65663ff3324d4980cf730caf8ee92a/1472885594968.png
)
</br>When the input parameter is an associate array, it needs to be input in the following format:
```
qcloudcli lb RegisterInstancesWithLoadBalancer --backends '[{"instanceId":"aaaa"},{"instanceId":"bbbb"}]'
```

Note: In the Windows Command Processor environment, a double quote (") need to be represented by a backslash (\), with the entire JSON value enclosed in double quotation marks (").

For example:
```
C:\Users\test>qcloudcli cvm DescribeInstances --instanceIds "[\"ins-0ljnjsco\",\"ins-p01nc1j\"]"
```
In the Windows PowerShell environment, a double quote (") need to be represented by a backslash (\), with the entire JSON value enclosed in single quotation marks (').

For example:
```
qcloudcli cvm DescribeInstances --instanceIds '[\"ins-0ljnjsco\",\"ins-p01nc1jg\"]'
```
## Help and Error Message
In any case, an appropriate help documentation will display when you enter an incorrect command or commands such as `--help`, `-h` and `help`.

### Main Command (qcloudcli) Help
When you enter help in the main command (qcloudcli) mode, a brief description of the command line function are displayed. When you use qcloudcli for the first time, you are prompted to set up account information using "qcloudcli configure" command:
![Alt text](https://mc.qcloudimg.com/static/img/abb23d0adbb64241ce146ebae195822f/1472885725338.png)

### Command (command) Mode Help
When you enter help in the command (command) mode, all the operations (APIs) supported by the current command (module) are displayed:
![Alt text](https://mc.qcloudimg.com/static/img/e25608538058ed9be477c3ba2f7127a1/1472885751387.png)

### API (operation) Mode Help
When you enter help in API mode, all the input parameters and the global options supported by the current operation are displayed:
 ![Alt text](https://mc.qcloudimg.com/static/img/68db29d00ad435a2ff1f546c4d4970f5/1472885775072.png)

The descriptions of the global option parameters are as follows:

--RegionId: The region information of the API, such as gz, hk, ca, sh, shjr, bj, and sg;   

--SecretId: The SecretId used by the API; 

--SecretKey: The SecretKey used by the API; 

--output: The output format of the API, such as JSON, table, and text;

--profile: The account used by the API. The specific account information is set by the command `qcloudcli configure --profile XXX` or `qcloudcli addprofile`.


