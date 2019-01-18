### CLB Full Read-write Policy
Full read-write policy authorizes a sub-user of full management permission of CLB services (creating, managing, etc.).
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
Read-only policy authorizes a sub-user of read-only access to CLB (that is, the permission to view all the resources under all LBs), but the user cannot create, update, or delete them. Because a user must view the resources before operating them in the console, you are recommended to activate CLB full read permission for the sub-accounts.
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

