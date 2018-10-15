The following describes how to configure and provide a usage plan for a specific user:
1. Create a service. Create and configure an API to make it effective and responsive.
2. Publish the service to an environment, such as "release".
3. Create a pair of secret_id + secret_key.
	(1) Go to the Key tab, and click **New**.
	![New key](//mc.qcloudimg.com/static/img/75e5ee23716b3d25e30e26a9ae8ec401/image.png)
	(2) Enter the key name, and click **Submit**.
	![Key information](//mc.qcloudimg.com/static/img/bf16f50982a95f549cd3e030023703c7/image.png)
4. Create a usage plan.
	(1) Go to the Usage Plan tab, and click **New**.
![Plan](//mc.qcloudimg.com/static/img/eac08df78a6bf577a1c6d64dcbe2eee1/image.png)
	(2) Edit the usage plan, and click **Finish**.
	![Plan information](//mc.qcloudimg.com/static/img/d5fe773a5ae782075478e52f682b4eb0/image.png)

5. Bind the usage plan to a service environment.
	(1) Select the service just created on the Service page, and then go to the Usage Plan tab and click **Bind**.
	![Binding plan](//mc.qcloudimg.com/static/img/d19d744bab06175489e15adf49fd9877/image.png)
	(2) Enter the release environment to be bound to, select the usage plan to be bound, and click **Submit**.
	![Binding information](//mc.qcloudimg.com/static/img/e32e10d6af1d2155e0616d4ff9cfe75d/image.png)

6. After the steps above are completed, you can provide the secret_id + secret_key created in Step 3 to end users. End users can obtain the verification using the secret_id + secret_key, and then access the API published in the service via the secondary domain name of the service or by binding a private domain name.

