## Importing Configurations to Container
### Step 1: Create Configuration Item
1. Log in to the console, and enter `Configuration Item Name`, `Version Number` and `Version Description` to create a configuration item.
2. YAML syntax editing and visual editing are supported.

- The format of YAML syntax editing is `key:value`. "Value "can be a string or text. `"|"` indicates that `value` is text. YAML is separated with indentation.
- Visual editing is supported. "Value "can be a string or text.
As shown below:
![Alt text](https://mc.qcloudimg.com/static/img/c3bc8b5c36986fa59493cce525430df4/%7B70371D71-F78F-4523-92EB-55C1218F4EAC%7D.png)
A created configuration item can be used to create a service.

### Step 2: Defining Data Volume With Configuration Item
1. Log in to the console and click Create/Update Service
2. Add a data volume, specify the configuration file type, and select the Key of configuration file to be mounted to a container.

- Select `Use Configuration Item` and enter `data volume name' for specifying a directory for mounting.
- In this example, we enter `testname`, and select `testfilekey` in the configuration item created previously.
![Alt text](https://mc.qcloudimg.com/static/img/39bbb6a1ef33fedc573f15970e353598/%7B3095DD9A-DAC2-48DF-8318-1DB3FC10823C%7D.png)

### Step 3: Mount Data Volume to a Specified Directory

- Enter the container image and other basic information, click Advanced Settings and set a mount point.
- In this example, we set the directory `/config` as the specified mounting directory.
- Click Finish to complete creation. You can use the created configuration file in the container. After configurations are imported to the path, the key of the configuration file will exist as a file name.
![Alt text](https://mc.qcloudimg.com/static/img/3214c2ecac262baaecd38abeff985a51/%7B84A8993A-331C-4079-AD29-7C42EAB57592%7D.png)

### Step 4: Log in to the Container for Verification

- Go to the console, enter the service pod list page, and click Remote Console to log in to the container.
- View the status of mounting in the container.
![Alt text](https://mc.qcloudimg.com/static/img/351022df7843a0c3fb622801521d2947/%7BE525F58C-AAB0-4C19-921D-3B6A2DD77D55%7D.png)
![Alt text](https://mc.qcloudimg.com/static/img/a1aa8d30072d44441367b86db0f4eb25/%7B53F0E411-88A6-4661-8434-5156124BF057%7D.png)

### Step 5: Set Read Configuration for Application
The verification result in step 4 shows that, the configuration item has been mounted to the container as a data volume when the container starts. For the container images of business code or application, follow the above steps when you start the service to mount configurations to the container for operations such as application initialization.

