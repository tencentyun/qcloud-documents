Users can customize the notification style as needed. Due to the limitation of the current customized ROM, some APIs cannot adapt to all models.
```
  XGCustomPushNotificationBuilder build = new  XGCustomPushNotificationBuilder();
        build.setSound(
                RingtoneManager.getActualDefaultRingtoneUri(
                getApplicationContext(), RingtoneManager.TYPE_ALARM))
                .setDefaults(Notification.DEFAULT_VIBRATE) // Vibration
                .setFlags(Notification.FLAG_NO_CLEAR); // Whether it can be cleared
        // Set custom notification layout, in which the notification background and other attributes can be set
        build.setLayoutId(R.layout.notification);
        // Set custom notification content ID
        build.setLayoutTextId(R.id.content);
        // Set custom notification header ID
        build.setLayoutTitleId(R.id.title);
        // Set custom notification image resources
        build.setLayoutIconDrawableId(R.drawable.logo);
        // Set the small notification icon in the status bar
        build.setIcon(R.drawable.right);
        // Set time ID
        build.setLayoutTimeId(R.id.time);
        // If you do not set the above custom layout but want to specify the notification bar image resources simply
        build.setNotificationLargeIcon(R.drawable.ic_action_search);
        // Save build_id on client
        XGPushManager.setPushNotificationBuilder(this, build_id, build);
        
```

