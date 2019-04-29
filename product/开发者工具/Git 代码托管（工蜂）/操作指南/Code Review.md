## 创建评审、添加评委
>! Code Review 设置的【Suggestion reviewers】和【Necessary reviewers】有添加成员的话，在创建合并请求时会自动创建评审，【Suggestion reviewers】和【Necessary reviewers】中添加的成员会自动成为该 评审的评委。【Suggestion reviewers】可删除，【Necessary reviewers】不可删除。

1. 新建合并请求，创建成功后的部分截图如下所示。
![img](https://main.qcloudimg.com/raw/dee7e2666247a25f60d10cd0150c1b5d.png)
2. 单击右侧【Add reviewer】按钮并在下拉框中找到需要参与评审的人员来添加评委。
![img](https://main.qcloudimg.com/raw/48cdddaa5b021b6a8f327794d9215b88.png)
3. 添加评委成功之后，页面将会提示 “Review required.Merging is blocked .”，评审改变为锁定状态，即需要通过评委评审才可提交。
![img](https://main.qcloudimg.com/raw/b4804234f64c59e2dde22dca7f338def.png)
4. 评委收到之后可以在【Changes】查看内容，并进行相关评论。
![img](https://main.qcloudimg.com/raw/cf1ba37f4374c22cbb674273b62ec39e.png)
5. 评委确认没有问题后，可在 【Review Changes】进行是否通过的操作。
![img](https://main.qcloudimg.com/raw/8f1e0b826b1396fff41ecf9dfc31b3fe.png)
6. 当评委评审已经通过后，合并请求将改变为可合并状态。
![img](https://main.qcloudimg.com/raw/fcda2ac08277d901b0cd5da62d17b1d5.png)

## Code Review 设置
>!可在保护分支上设置评审的默认行为。当合并请求在该分支（作为目标分支）发起时，评审会依据配置自动带起。

操作步骤： `Settings-> Protected Branches-> Edit`，单击至如下所示页面。
![img](https://main.qcloudimg.com/raw/17f89dabacd1bfdede8e8ae702b857a4.png)

**上图设置详情：**

- Review：

  - 特点1（重要）：勾选后在评委没有通过评审之前阻止界面以及客户端本地合并该合并请求，不勾选时评审未通过前可通过客户端本地合并该合并请求。
  - 特点2：勾选后即使当前审阅状态已获批准，推送新提交也会自动重置状态为未批准 ，不勾选则没有该效应。

- Suggestion reviewers：
  【Suggestion reviewers】添加人员后创建合并请求 会自动成为评委且可以被移除。

- Necessary reviewers：
  【Necessary reviewers】添加人员后创建合并请求会自动成为评委，但是不能被移除。

- Branch setting：
  All approve 是全部评委通过，评审才能通过 ；

  Single approve 是当某个评委通过，评审即通过 （不设置的情况下默认为 Single approve）。

## Code Review 状态

- **Approving：** 评审创建后的初始状态，当有成员将该评审的状态改为 Change 或 Deny 状态后，再次打开这个评审 状态将会重新回到 Approving。
- **Change required：** 每一位 评委都可以将 Approving 状态更改为 Change required，再次打开该评审后状态将会变为 Approving。
- **Deny：** 每一位评委都可以将 Approving 状态更改为 Deny，再次打开评审后状态将会变为 Approving。
- **OK：**合并请求 的状态变更为 OK 时，即意味着该 合并请求通过评审（注意关注 评审设置是 All approve 还是 Single approve）。
