## 创建 Review、添加 Reviewer

>**注意：**  
> Code Review 设置的【Suggestion reviewers】和【Necessary reviewers】有添加成员的话，在创建 Merge Request 时会自动创建 Review，【Suggestion reviewers】和【Necessary reviewers】中添加的成员会自动成为该 Review 的 Reviewer。

1. 新建 Merge Request，创建成功后的部分截图如下所示。
![](https://mc.qcloudimg.com/static/img/b826e7a2545369e4b4925564f931617e/2017-09-18_105418.png)

2. 单击右侧【Add reviewer】按钮并在下拉框中找到需要参与评审的人员来添加 Reviewer。  
![](https://mc.qcloudimg.com/static/img/9816d1f662a1e2f360208103aa9c4bae/2017-09-15_093630.png)

3. 页面将会提示 “Merging is blocked. Review required.”，Review 改变为锁定状态，即需要通过评审才可提交。
![](https://mc.qcloudimg.com/static/img/c4ec0da3d825aec2a856a76adcaab63c/2017-09-15_094738.png)

4. Reviewer 收到之后可以在【Changes】查看内容，并进行相关评论。
![](https://mc.qcloudimg.com/static/img/cc0bb1c28dfa11760caef2a4e6822343/2017-09-18_103955.png)

5. Reviewer 确认没有问题后，可在 【Review Changes】进行是否通过的操作。
![](https://mc.qcloudimg.com/static/img/4d249876e6e8ea4d5cd51a11710d2302/2017-09-15_095345.png)

6. 当 Review 评审已经通过后，Merge Request 将改变为可合并状态。
![](https://mc.qcloudimg.com/static/img/7385118075d2e0e541f4d84ab5b9b0f9/2017-09-15_100629.png)

  
## Code Review 设置
> **注意：**  
> 可在保护分支上设置 Code Review 的默认行为。当 Merge Request 在该分支（作为目标分支）发起时，Code Review 会依据配置自动带起。

操作步骤： `Settings-> Protected Branches-> Edit`，单击至如下所示页面。
![](https://mc.qcloudimg.com/static/img/63a5157559f759e936764b56f0d99804/2017-09-18_120854.png)

**上图设置详情：**

- Features：
    - 特点1（重要）：勾选后在 Review 评审没有通过之前阻止界面以及客户端本地合并 Merge Request，不勾选时评审未通过前可通过客户端本地合并 Merge Request。
    - 特点2：OK 状态时勾选后再在 Source Branch 上提交 Commit 后 Review 状态自动更改为 Approving，不勾选则没有该效应。

- Suggestion reviewers：  
【Suggestion reviewers】添加人员后创建 Review 会自动成为 Reviewer且可以被移除。

- Necessary reviewers：  
【Necessary reviewers】添加人员后创建 Review 会自动成为 Reviewer，但是不能被移除。

- Branch setting：  
All approve 是所有 Reviewer 成员 Approve 后该 Review 的评审才算通过；  
Single approve 是 Reviewer 中一个成员 Approve 后该 Review 的评审就算通过（不设置的情况下默认为 Single approve）。

## Code Review 状态
- **Approving：** Review 创建后的初始状态，当有成员将该 Review 的状态改为 Change 或 Deny 状态后，再次 Reopen 该 Review ，状态将会重新回到 Approving。
- **Change required：** 每一位 Reviewer 成员都可以将 Approving 状态更改为 Change required，再次 Reopen 该 Review 后状态将会变为 Approving。
- **Deny：** 每一位 Reviewer 成员都可以将 Approving 状态更改为 Deny，再次 Reopen Review 后状态将会变为 Approving。
- **OK：** Review 的状态变更为 OK 时，即意味着该 Review 通过评审（注意关注 Review 设置是 All approve 还是 Single approve）。

  
