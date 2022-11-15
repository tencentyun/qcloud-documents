## 背景信息

使用 Backend 配置 Terraform 会涉及执行环境和远端状态同步的问题，Terraform 引入了锁的机制避免多个执行环境操作同一个 backend 导致状态不同步，不同厂商均可通过 Terraform 提供的 lock interface 实现自己的状态锁。本文介绍 Cos backend 锁的实现步骤和异常处理。

## 状态锁与文件写入锁

根据 [源码](https://github.com/hashicorp/terraform/blob/v1.2.1/internal/backend/remote-state/cos/client.go#L75) 可知，Cos Backend 执行时会涉及2种锁。
- 状态锁，以 `terraform.tfstate.tflock` 文件形式出现，记录当前进程的信息并写入 Backend 存储桶：
```json
{
  "ID":"1234abcd-1234-cdef-5678-1234567890ab",
  "Operation":"OperationTypePlan",
  "Info":"",
  "Who":"UserName@Host",
  "Version":"1.3.0",
  "Created":"2006-01-02T15:04:05Z07:00",
  "Path":"terraform.tfstate.tflock"
}
```
- 文件写锁，用来避免多个进程同时对存储桶写入 `terraform.tfstate.tflock` 文件。Cos Backend 以腾讯云标签形式来实现，格式为：`tencentcloud-terraform-lock:xxxxxxxxx`（xxxxxxxxx 为 bucket:lockfile 的 MD5），**当文件写入成功后自动释放**。

## 上锁步骤[](id:lock)

通常情况下，执行 terraform 命令会进行如下步骤：

1. terraform 开始执行（plan / apply 等命令）。
2. Backend 服务对当前账号添加腾讯云标签作为文件写锁。
3. 存储桶检查并写入 `terraform.tfstate.tflock` 作为状态锁。
4. 删除标签，释放文件写锁。
5. 等待 terraform 执行完毕。
6. 存储桶检查并删除 `terraform.tfstate.tflock` 取消状态锁。
7. terraform 执行完毕。


## 异常处理
### 场景1
当有进程执行 [上锁步骤](#lock) 中的步骤4、5、6、7时，如果其他进程尝试操作同一 Backend，则会抛出 Lock Error，示例如下：
```text
╷
│ Error: Error acquiring the state lock
│ 
│ Error message: lock file terraform.tfstate.tflock exists
│ Lock Info:
│   ID:        1234abcd1234cdef56781234567890ab
│   Path:      terraform.tfstate.tflock
│   Operation: OperationTypePlan
│   Who:       UserName@Host
│   Version:   1.1.2
│   Created:   2006-01-02T15:04:05Z07:00
│   Info:      
│ 
│ 
│ Terraform acquires a state lock to protect the state from being written
│ by multiple users at the same time. Please resolve the issue above and try
│ again. For most commands, you can disable locking with the "-lock=false"
│ flag, but this is not recommended.
╵
```
- 此时其他执行环境需要等待当前进程执行完毕，或您可按照文中的英文提示加入 `-lock=false` 忽略状态锁重新执行（**不推荐该方式**）。
- 在此过程中，Terraform 进程意外退出而没有及时释放状态锁，需要您手动解锁：
 -  以上文为例，根据锁 ID 执行以下强行解锁命令，即可解锁。
```
terraform force-unlock -force 1234abcd1234cdef56781234567890ab
```
 - 删除存储桶下的 `terraform.tfstate.tflock` 文件也可解锁。

### 场景2
如在执行 [上锁步骤](#lock) 的步骤3、4时，由于进程中断而退出，标签锁未解开，此时再次进行 terraform 操作会报标签无法创建的异常：
```text
│ Error: Error acquiring the state lock
│
│ Error message: 2 errors occurred:
│       * failed to create tag: tencentcloud-terraform-lock -> xxxxxxxxx: [TencentCloudSDKError] Code=ResourceInUse.TagDuplicate, Message=tagKey-tagValue have exists.,
│ RequestId=47c57b0b-2491-42cd-9f29-0b14802681e5
│       * lock file terraform/state/terraform.tfstate.tflock not exists
│
│
│
│ Terraform acquires a state lock to protect the state from being written
│ by multiple users at the same time. Please resolve the issue above and try
│ again. For most commands, you can disable locking with the "-lock=false"
│ flag, but this is not recommended.
```

此时，Terraform 没有相关命令释放这个锁，您需要手动删除 `tencentcloud-terraform-lock:xxxxxxxxx` 标签。您可通过控制台，或调用云 API 接口 [DeleteTag](https://cloud.tencent.com/document/product/651/13568) 进行删除。
控制台操作步骤如下：
 1. 登录标签控制台，选择左侧导航栏中的 **[标签列表](https://console.cloud.tencent.com/tag/taglist)**。
 2. 单击如下图所示标签所在行右侧的**删除**，并在弹出窗口中单击**确定**即可。
![](https://qcloudimg.tencent-cloud.cn/raw/d57e4b5362e44f9f1995f6949beccaa4.png)
