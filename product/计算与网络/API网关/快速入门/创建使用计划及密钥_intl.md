After a service is published, you must create a usage plan and a key and bind them to the service before you can call it successfully.
1. Create a pair of secret_id + secret_key.
	(1) Go to the Key tab, and click **New**.
	![Key List](//mc.qcloudimg.com/static/img/dba3b996aff0e3cae78e30ea949c04ba/image.png)
	(2) Enter the key name, and click **Submit**.
	![Create a Key](//mc.qcloudimg.com/static/img/b552fcf62a764e6807b924d8f68a5c69/image.png)

2. Create a usage plan.
	(1) Go to the Usage Plan tab, and click **New**.
	![Usage plan list](//mc.qcloudimg.com/static/img/e00d7896c262b72cd039b818a41dc22c/image.png)
	(2) Edit the usage plan, and click **Finish**.
![Create a usage plan](//mc.qcloudimg.com/static/img/210a7b685bf94ae5603bfab0be182c9a/image.png)

3. Bind the created secret_id + secret_key in the Usage Plan tab.
	(1) Go to the Usage Plan tab, and select the created service.
	![Usage plan list](//mc.qcloudimg.com/static/img/e520bbd87f1202a9536bd5646f6b4ea4/image.png)
	(2) Click **Bind Key**.
	![Bind a key](//mc.qcloudimg.com/static/img/1cf88feb2bc753ce9d9dc038cee834dc/image.png)
	(3) Bind the created secret_id + secret_key in the Usage Plan tab, and click **Submit**.
	![Bind a key](//mc.qcloudimg.com/static/img/7232cd0acbec6d2aefee23e962fe4b0c/image.png)
	
4. Bind the usage plan to a service environment.
	(1) Go to the Usage Plan tab, and select the created service.
	![Usage plan list](//mc.qcloudimg.com/static/img/e520bbd87f1202a9536bd5646f6b4ea4/image.png)
	(2) Go to the **Bound Environment** page, and click **Bind Service Environment**.
	![Bind a service environment](//mc.qcloudimg.com/static/img/045ce20ca4f085e4ab4823f1b5dd29eb/image.png)
	(3) Enter the service and the environment to be bound, and click **Submit**.
	![Enter the environment to be bound to](//mc.qcloudimg.com/static/img/f4afc060250f32e36cf5e5a5e40025ff/image.png)
> Note: If two usage plans are to be bound to the same environment, the two usage plans cannot be bound to the same key.

5. After the steps above are completed, you can provide the secret_id + secret_key created in Step 1 to end users. End users can obtain the verification using the secret_id + secret_key, and then access the API published in the service via the secondary domain name of the service or by binding a private domain name.
