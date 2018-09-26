You can bind your independent domain name to a service using the domain binding function, so that the service can be provided by your own independent domain name. Perform the steps below:
1. Make sure your independent domain name has obtained the ICP license.
2. Configure CNAME resolution of the independent domain name to the sub-domain name provided by the service. Click **New** button on the custom domain name page. Enter the configuration information, and click **Confirm**.
![](https://mc.qcloudimg.com/static/img/88c5083867ed7c396244f290058e9185/image.png)
![](https://i.imgur.com/CBKEUwE.png)

> If you need the https protocol which supports the independent domain name, submit the SSL certificate of the domain name. The certificate can be uploaded as a file, or it can be submitted by filling in the certificate name, content and private key. 
3. After the CNAME resolution is configured, configure to bind the independent domain name in the service. Make sure the CNAME resolution is configured before the binding.
4. If you want to unbind, delete the bound independent domain name in the service first, and then delete the CNAME of the independent domain name.

## Path Mapping of a Custom Domain Name

To configure the mapping, you can use the default path mapping for the custom domain name. Then the URL path is "custom domain name/environment". For example, `www.yingxiong.com/release` points to the publishing environment; `www.yingxiong.com/prepub` points to the pre-publishing environment; `www.yingxiong.com/test` points to the test environment.
![](https://mc.qcloudimg.com/static/img/4dceea99a76647beca1da5d4de37ec85/image.png)

You can also configure your custom domain name. The URL of the custom path is "custom domain name/custom path", and the URL points to the mapped environment. For example, if the configured path is /mypath, the environment is publishing environment, the URL in this environment is `www.yingxiong.com/mypath`. If you want to use the root path, configure the path as "/".
When using custom path mapping, the default path mapping is not effective, that is, the custom domain name/environment name is not effective either.
The custom and default path mapping can still be edited after the configuration.
![](https://i.imgur.com/qBgXOOv.png)
![](https://mc.qcloudimg.com/static/img/d161334055893fff4b4bdce9e886b251/image.png)
If you need the https protocol which supports the independent domain name, submit the SSL certificate of the domain name. The certificate can be uploaded as a file, or it can be submitted by filling in the certificate name, content and private key.


