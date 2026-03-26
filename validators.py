import re
def validate_email(email):
    """Validate email using regex"""
    pattern = r"^\w+@\w+\.(ac\.uk|gov\.uk|nhs\.net)$"
    return bool(re.match(pattern, email))

def validate_student_id(student_id):
    """Validate student ID (exactly 6 digits)"""
    pattern = r"^\d{6}$"
    return bool(re.match(pattern, student_id))

def validate_phone(phone):
    """Validate UK phone number (11 digits starting with 07)"""
    pattern = r"^07\d{9}$"
    return bool(re.match(pattern, phone))
#end
