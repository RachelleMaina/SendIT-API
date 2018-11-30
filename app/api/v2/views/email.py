from flask_mail import Message
from instance.config import Config


class Emails(object):
    """Class to handle app emails"""
    def user_registration(self, email):
        """Method to return email after successiful registration"""
        from app import send_email
        mail = send_email()
        sender = Config()       
        subject = "Registration"
        msg = Message(subject, sender=sender.SENDER, recipients=[email])
        msg.body = "You have registred with sendit courier services" + "\n\n\n\nKind Regards,\nSendIT Courier Services"
        mail.send(msg)

    def change_status(self, email, order, user_by_id):
        """Method to return email after successiful change of parcel order status"""
        from app import send_email
        mail = send_email()
        sender = Config()
        subject = "Parcel Delivery"
        msg = Message(subject, sender=sender.SENDER, recipients=[email])
        msg.body = "Dear " + user_by_id["username"] + ", " + "\n\nThe Status of your parcel delivery order is: " + order[
            "status"] + "\n\n\n\nKind Regards,\nSendIT Courier Services"
        
        mail.send(msg)

    def change_location(self, email, order, user_by_id):
        """Method to return email after successiful change of parcel order location"""
        from app import send_email
        mail = send_email()
        sender = Config()
        subject = "Parcel Delivery"
        msg = Message(subject, sender=sender.SENDER, recipients=[email])
        msg.body = "Dear " + user_by_id["username"] + ", " + "\n\nYour Parcel is now at: " + order[
            "current_location"] + "\n\n\n\nKind Regards\nSendIT Courier Services"
        mail.send(msg)

    def change_destination(self, email, order, users):
        """Method to return email after successiful change of parcel destination"""
        from app import send_email
        mail = send_email()
        sender = Config()
        subject = "Parcel Delivery"
        msg = Message(subject, sender=sender.SENDER, recipients=[email])
        msg.body = "Dear " + users["username"] + ", " + "\n\nYou have changede the destination of your Parcel to  " + order[
            "destination"] + "\n\n\n\nKind Regards\nSendIT Courier Services"
        mail.send(msg)
