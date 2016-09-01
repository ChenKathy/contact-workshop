class Contact(object): 
    def __init__ (self, first_name, last_name, mobile_number="", work_number="", email="", twitter_handle=""): 
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number
        self.work_number = work_number
        self.email = email
        self.twitter_handle = twitter_handle

    def send_text(self, message):
        if self.mobile_number is "":
            print "No mobile number exist."
        else:
            return "To: %s -%s" % (self.mobile_number, message)


class Dog(object):
    def __init__(self, fur=False, personality, claws, tail, color):
        self.fur = fur
        self.personality = personality
        self.claws = claws
        self.tail = tail
        self.color = color

romeo = Dog(False, "rebel", "short", "short", "brown")
#romeo is an instance of object Dog. Not an instance of object Contact.