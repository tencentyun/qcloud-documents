A scaling activity will be canceled under such conditions that a conflict occurs when the scaling activity is triggered as the scheduled task starts or the requirement of the alarm scaling policy is met.

**Causes of Conflict:**
- Other scaling activities are in progress;
- The scaling group is under cooldown period.

**Will the alarm scaling activity be rebooted if canceled?**
- No, the**alarm scaling** activity cannot be rebooted if canceled. If the requirements for alarm scaling are met, another alarm scaling activity will be triggered.
- **Scheduled task **  defines the expected, maximum and minimum group size, so the scaling group will keep trying until the actual number of instances equals the expected number of instances.

>Note: A suspended scaling group does not try any scaling activity. That's why such activity is not recorded as canceled scaling activity in the "Scaling Activity".

