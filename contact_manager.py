
from contact import Contact

master_dict = {}
count =0

def show_all_contacts(): 
    for contact in contactslist: 
        # print info.first_name, info.last_name, info.mobile_number, info.work_number, info.email, info.twitter_handle
        print contact

def add_contact(): 
    new_contact_dict = {}

    first_name = raw_input("Enter name ")
    last_name = raw_input("Enter last name ") 
    mobile_number = raw_input("Enter mobile number ") 
    work_number = raw_input("Enter work number ")
    twitter_handle = raw_input("Enter twitter handle ")
    email = raw_input("Enter email ")
        for k,v in contact_dict.iteritems():
            if v.email == email:
                raw_input('do you have another email address, invalid ')
            else:
                contact_dict['contact information'] = user_contact
                count += 1
                master_dict[count] = contact_dict

    user_contact = Contact(first_name, last_name, mobile_number, work_number, email, twitter_handle)
    master_dict[count] = new_contact_dict
    

def edit_existing_contact():
    pass

def main():


if __name__ == '__main__':
    main()