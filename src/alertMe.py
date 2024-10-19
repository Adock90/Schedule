from winotify import Notification, audio

def notification(message, title, do):
    notif = Notification(app_id="Schedule", 
                        title=title,
                        msg=message,
                        duration="short",
                        )
    if do != None:
        notif.add_actions(label="launch",
                        launch=do)
    notif.show()