# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass
# class Dog(Animal):

#     def sound(self):
#         print("Bark")

# d = Dog()

# d.sound()



class EmailService:

    def _connect(self):
        print("Connecting to Email services ...")
    
    def _authenticate(self):
        print("Authentication is in progress ..")
    def send_email(self):
        self._connect()
        self._authenticate()
        print("Email sending is in progress ..")
        self._disconnect()
    def _disconnect(self):
        print("Email sent and User Disconnected Successfully !!")
    
email = EmailService()
email.send_email()




