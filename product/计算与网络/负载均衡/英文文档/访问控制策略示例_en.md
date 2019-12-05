## Example of CLB CAM Policy

### CLB Full Read-write Policy
Authorize a sub-user of full management permission of CLB service (creating, managing, etc.).
> Policy name: CLBResourceFullAccess
```
{
  "version": "2.0",
  "statement": [
    {
      "action": [
            "name/clb:*",
      ],
      "resource": "*",
      "effect": "allow"
    }
  ]
}
```
### CLB Read-only Policy
Authorize a sub-user of read-only access to the CLB (that is, the permission to view all the resources under CLB), but the user cannot create, update, or delete them. Because a user must view the resources before operating them in the console, you are recommended to enable the CLB full read permission for the sub-accounts.
> Policy name: CLBResourceReadOnlyAccess

```
{
  "version": "2.0",
  "statement": [
    {
      "action": [
            "name/clb:Describe*",
      ],
      "resource": "*",
      "effect": "allow"
    }
  ]
}
```

