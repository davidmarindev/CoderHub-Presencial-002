# Open Close Principle (OCP)

from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, message, user):
        self.message = message
        self.user = user

    @abstractmethod
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print(f"Sending email to {self.user}: {self.message}")

class SMSNotification(Notification):
    def send(self):
        print(f"Sending SMS to {self.user}: {self.message}")
        
class PushNotification(Notification):
    def send(self):
        print(f"Sending push notification to {self.user}: {self.message}")

class WhatsappNotification(Notification):
    def send(self):
        print(f"Sending WhatsApp message to {self.user}: {self.message}")
