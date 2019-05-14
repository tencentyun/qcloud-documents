After the SSL certificate is deployed, the accessed site prompts "Connection is not secure". Is the certificate deployment failed?

A: The certificate has been successfully deployed. This problem occurs because that the browser considers the sites unsafe if they use HTTPS protocol and their pages contain unencrypted HTTP contents. In this case, the code needs to be modified.

For frontend modification, here are the references:
1. Reference resources with relative paths;
2. When referencing the absolute path, use `//` to reference resources. For example: `//img.qcloud.com/example.png` indicates compliance with the protocol of the current page, and the browser will automatically complete it.

