## 现象描述
下载或更新 Provider 出现如下报错信息：
```bash
Initializing the backend...

Initializing provider plugins...
- Checking for available provider plugins on https://releases.hashicorp.com...

Error installing provider "tencentcloud": openpgp: signature made by unknown entity.

Terraform analyses the configuration and state and automatically downloads
plugins for the providers used. However, when attempting to download this
plugin an unexpected error occured.

This may be caused if for some reason Terraform is unable to reach the
plugin repository. The repository may be unreachable if access is blocked
by a firewall.

If automatic installation is not possible or desirable in your environment,
you may alternatively manually install plugins by downloading a suitable
distribution package and placing the plugin's executable file in the
following directory:
    terraform.d/plugins/darwin_amd64

```

## 问题定位
参考 [官网说明](https://discuss.hashicorp.com/t/terraform-updates-for-hcsec-2021-12/23570)，可得知是 Terraform 版本过低导致更新失败。

## 处理步骤
更新 Terraform 版本大于等于0.11.15版本即可。
