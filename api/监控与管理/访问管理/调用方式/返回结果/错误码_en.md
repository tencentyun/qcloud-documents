## Common Error Codes

The error codes in the returned result indicate the result of the call to the cloud API. "code" is common error code, which applies to APIs of all modules. A code of 0 means a successful call. Other value means a failed call. When the call fails, you can determine the cause of error and take appropriate actions based on the following table.

| Error Code | Error Type | Description |
| ------------ | ------------ | ------------ |
| 4000 | Invalid request parameter | Required parameters are missing, or the format of parameter values is incorrect. For specific error message, please see the message field in error description. |
| 4100 | Authentication failed | Signature authentication failed. |
| 4200 | Request expired | Request has expired. |
| 4300 | Access denied | The account is disabled or is not within the user range for the API. |
| 4400 | Quota exceeded | The number of requests has exceeded the quota limit. For more information, please see Request Quota section in the document. |
| 4500 | Replay attack | The Nonce and Timestamp parameters of request can ensure that each request is executed only once on the server. Therefore, the Nonce should not be identical to the previous one. The time difference between the Timestamp and Tencent CVM should not be greater than 2 hours. |
| 4600 | Unsupported protocol | Protocol is not supported. |
| 5100 | Failed to generate credential | An error occurred while generating a credential via API, which is backend service error |

## Module Error Codes

"code" is error code, and "codeDesc" is code description.

| Code | CodeDesc | Note | 
| ------------ | ------------ | ------------ |
| 4000 | InvalidParameter.policyName.InUse | The policy name already exists. Policy name must be unique under the same account as required by CAM. |
| 4000 | InvalidParameter | Invalid input parameter |
| 5100 | InternalError | Internal system error |
| 4000 | InvalidParameter.AttachmentFull | The number of policies bound to user/user group/role has reached the upper limit. The maximum number of policies to be added to a user/user group/role is 200. Binding of extra policies may fail. You can unbind some of the old policies first. |
| 4000 | InvalidParameter.principal.Error | The parameter "principal" in policy document is incorrect. |
| 4000 | InvalidParameter.action.Error | The parameter "action" in policy document is incorrect. |
| 4000 | InvalidParameter.effect.Error | The parameter "effect" in policy document is incorrect. |
| 4000 | MissingParameter.action | The field "action" in policy document is missing. |
| 4000 | InvalidParameter.policyName.TypeError | The type of policy name is incorrect. Policy name must be a string. |
| 4000 | InvalidParameter.policyName.Error | The policy name contains invalid characters or the length exceeds the limit. The maximum length of the policy name is 128 bytes. The policy name can only contain letters or <a>"+", "=", ",", ".", "@", "_", "-"</a>. | 
| 4000 | InvalidParameter.policyDocument.TypeError| The type of policy document is incorrect. |
| 4000 | MissingParameter.version| The field "version" in policy document is missing. |
| 4000 | InvalidParameter.version.Error | The parameter "version" in policy document is incorrect. |
| 4000 | MissingParameter.statement | The field "statement" in policy document is missing. |
| 4000 | InvalidParameter.statement.Error | The parameter "statement" in policy document is incorrect. |
| 4000 | InvalidParameter.policyDocument.LengthOverlimit | The length of policy document exceeds the limit, which is limited to 4,096 bytes. |
| 4000 | InvalidParameter.condition.Error | The parameter "condition" in policy document is incorrect. |
| 4000 | MissingParameter.resource | The field "resource" in policy document is missing. |
| 4000 | InvalidParameter.resource.Error | The parameter "resource" in policy document is incorrect. |
| 4000 | InvalidParameter.resource.user.Error| The "resource" in policy document is not a resource under your account. |
| 4000 | InvalidParameter.description.LengthOverlimit | The length of policy description exceeds the limit, which is limited to 300 bytes. |
| 4000 | MissingParameter.policyName | The input parameter "policyName" is missing. |
| 4000 | MissingParameter.policyDocument | The input parameter "policyDocument" is missing. |
| 4000 | InvalidParameter.description.TypeError | The type of policy description is incorrect. Policy description must be a string. |
| 4000 | InvalidParameter.policyId.NotExist | Policy ID does not exist. |
| 4000 | MissingParameter.policyId | The input parameter "policyId" is missing. |
| 4000 | InvalidParameter.policyId.TypeError | The type of policy ID is incorrect. Policy ID must be a number. |
| 4000 | InvalidParameter.policyFull | The number of policies under this account reaches the limit. The upper limit is 1,000. |
| 4000 | InvalidParameter.user.NotExist | User does not exist, or the user of field "principal" in policy document does not exist. |
| 4000 | InvalidParameter.group.NotExist | User group does not exist, or the user group of field "principal" in policy document does not exist. |
| 4000 | InvalidParameter.role.NotExist | The role does not exist. |
| 4000 | InvalidParameter.roleName.TypeError | The type of role name is incorrect. Role name must be a string. |
| 4000 | InvalidParameter.roleName.Error | The role name contains invalid characters or the length exceeds the limit. The maximum length of the role name is 128 bytes. The policy name can only contain letters or <a>"+", "=", ",", ".", "@", "_", "-"</a>. |
| 4000 | InvalidParameter.roleFull | The number of roles owned by this account reaches the limit. An account can have a maximum of 250 roles. |
| 4000 | InvalidParameter.roleName.InUse| The role name already exists. Role name must be unique under the same account. |
| 4000 | CanNotGetOwnerUin | User's OwnerUin cannot be obtained. Confirm whether the account ID is correct. |
| 4000 | GetAppIdError | User's AppId cannot be obtained. Confirm whether the account ID is correct. |
| 4000 | SetTimeOutOfTime | The validity period of the temporary certificate set by the user exceeds the maximum time limit. For more information, please see parameter description of specific API. |
| 4000 | StrategyInvalid | The policy information set for obtaining the temporary certificate of federated identity is incorrect. For the specific reason, please see "message". |


