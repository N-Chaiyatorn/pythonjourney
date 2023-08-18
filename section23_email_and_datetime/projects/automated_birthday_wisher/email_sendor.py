import smtplib

class EmailSendor():
    def __init__(self):
        self.reciever_data_dict = {}

    def determine_user_email_text(self, row, seperated_line_text_list):
        seperated_line_text_list[0] = seperated_line_text_list[0].replace("[NAME]", row["name"])
        seperated_line_text_list[6] = "Pan"

        for line in seperated_line_text_list:
            if line == "":
                seperated_line_text_list[seperated_line_text_list.index(line)] = "\n\n"

        text = ""
        
        for line in seperated_line_text_list:
            text += line

        return text

    def sending_emails(self, sendor_email, connection):
        for name in self.reciever_data_dict:
            connection.sendmail(from_addr = sendor_email, to_addrs = self.reciever_data_dict[name]["email"], msg = f"Subject:Birthday wish!!!!\n\n{self.reciever_data_dict[name]['text']}")

        
