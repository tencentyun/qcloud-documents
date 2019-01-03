## Configuring Template and Managing Multiple Environments
### Step 1: Create a configuration item
1. Log in to the console, and enter `Configuration Item Name`, `Tag Number` and `Tag Description` to create a configuration item.
2. YAML syntax editing and visual editing are supported.

- The format of YAML syntax editing is `key:value`. "Value" can be a string or text. `"|"` indicates that value is text. YAML is separated with indentation.
- For visual editing, "value" can be a string or text.
See the figure below:
![Alt text](https://mc.qcloudimg.com/static/img/c3bc8b5c36986fa59493cce525430df4/%7B70371D71-F78F-4523-92EB-55C1218F4EAC%7D.png)
After the configuration item is created, it can be used to create a service.

### Step 2: Replace variables using configuration item when creating or updating an application template
1. Go to the Create/Update Application Template page
2. Set a parameter that changes frequently as a variable
3. Select an existing configuration item to assign a value to the variable

![Alt text][1]
![Alt text][2]

[1]:https://main.qcloudimg.com/raw/c2df22bd3c91e735fa306da88178fb3b.png
[2]:https://main.qcloudimg.com/raw/c4c04b186ce8e9e9c978e8a6870f2c36.png

