Tencent Cloud Command Line Interface (CLI) is a unified tool to manage Tencent Cloud resources. With Tencent Cloud CLI, you can quickly and easily call Tencent Cloud API to manage your Tencent Cloud resources and automate them through scripts for diversified combination and reuse.

## Product Features
### Multi-product Integration

CLI integrates all products that support Tencent Cloud APIs. You can configure and manage Tencent Cloud products under the command line. All the operations that can be performed on the console page can be implemented by executing commands on CLI, including creating a CVM, operating a CVM, creating a CBS disk, viewing CBS disk usage, creating a VPC and adding resources to a VPC.

- Use the command `qcloudcli cvm DescribeInstances` to view CVMs under the current account
- Use the command `qcloudcli cbs DescribeCbsStorages` to view CBS disks
- Use the command `qcloudcli vpc DescribeNatGateway` to view NAT gateway
- Other commands

You can use Tencent Cloud CLI to operate Tencent Cloud resources on a non-graphical page.

### Multi-account Support
You can set multiple accounts for the CLI and rapidly switch between accounts.

- Use the command `qcloudcli addprofile` to add an account
- Use the command `qcloudcli showconfigure` to view the profile
- Use the command `qcloudcli configure --profile [username]` to modify the profile of a specified account
- Use the command `qcloudcli useprofile --name [username]` to switch the current account

### Multi-platform Support
Tencent CLI can be installed and used on Windows, Mac OS and Linux/Unix to meet the requirements of different developers. Its commands can be automatically completed under Linux/Unix environment.
After installing python on Windows, MacOS or Linux/Unix, you can install Tencent Cloud CLI by executing pip. If you are able to proficiently use it on Linux, you can also perform the same on Windows. This is because the execution commands of CLI functions are the same on each platform.

### Multiple Output Formats
CLI supports multiple output formats. You can choose from text, json and table as an output format.

- For text, the result is output in a text format. Each line is returned as a record and is separated by a space. This format is suitable for the acquired resource list to be saved as a text or to be converted into a table.
- For json, the result is returned in a json format. This format is suitable for secondary encoding. You can acquire the information by resolving the returned json.
- For table, the result is returned in a table format. It is highly visualized and suitable for operating cloud resources just using CLI.


