# docstring ===> เป็นการเขียนคำอธิบายให้กับฟังก์ชั่นที่เราตั้งขึ้นมาเอง  เวลาเราเอาเมาส์ไปชี้ที่ ฟังก์ชั่นจะได้มีคำอธิบายขึ้นมา
# docstring ===> จะเขียนบรรทัดถัดมาจาก def เท่านั้น
# ถ้าไม่กำหนด docstring ให้ฟังก์ชั่นที่เรากำหนด เวลาเอาเมาส์ไปชี้ที่คำอธิบายของฟังก

def format_name(last_name, first_name):
    """
    return the title cased full name
    """
    formatted_last_name = last_name.title()
    formatted_first_name = first_name.title()
    print(f"{formatted_last_name} {formatted_first_name}")

format_name(last_name, first_name)