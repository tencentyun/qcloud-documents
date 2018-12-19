For each scaling group, you can control the time to add instances (scale-up) to it or delete instances (scale-down) from it. You can scale the scaling group manually by adding or removing instances, or allow AS to execute this process automatically by using scaling policy.

When the scaling group is scaled down automatically, you need to know which instances should be terminated in the first place based on the remove policy.

During scale-down, you can prevent specified instances from being terminated by AS using instance protection.

## Remove Policy

The scaling group will determine which CVM should be removed based on the remove policy during scale-down. You can choose from the following two remove policies:

- **Delete the oldest CVMs**: Delete the oldest CVMs that are added automatically; after this, delete the oldest CVMs that are added manually.
- **Delete the latest CVMs**: Delete the latest CVMs that are added automatically; after this, delete the latest CVMs that are added manually.

> Note: No matter the latest or oldest servers to be deleted, AS will delete the automatically created CVMs in the first place, and then delete manually added CVMs.

## Setting and Modifying Remove Policy in the Console
There are two ways to set up:
- Select the remove policy you want when creating the scaling group.
- In the details page of scaling group, click "Edit" to modify the scaling policy.


