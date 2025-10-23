import re
from datetime import datetime

class UserValidation:
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate the format of an email address."""
        if not email:
            return False
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$'
        return re.fullmatch(pattern, email) is not None

    @staticmethod
    def validate_username(username: str) -> bool:
        """Validates username (3–20 chars, letters/numbers/underscore only)."""
        if not username:
            return False
        pattern = r'^[a-zA-Z0-9_]{3,20}$'
        return re.fullmatch(pattern, username) is not None

    @staticmethod
    def validate_phone_number(phone: str) -> bool:
        """Validates Egyptian phone number (starts with 010, 011, 012, or 015 — 11 digits total or +20 prefix)."""
        if not phone:
            return False
        pattern = r'^(?:\+?20|0)?(10|11|12|15)\d{8}$'
        return re.fullmatch(pattern, phone) is not None

    @staticmethod
    def validate_national_id(national_id: str) -> bool:
        """Validates Egyptian national ID (14 digits with valid date and governorate code)."""
        if not national_id or not re.fullmatch(r'\d{14}', national_id):
            return False

        century = national_id[0]
        year = int(national_id[1:3])
        month = int(national_id[3:5])
        day = int(national_id[5:7])
        governorate = national_id[7:9]

        if century == '2':
            year += 1900
        elif century == '3':
            year += 2000
        else:
            return False

        try:
            datetime(year, month, day)
        except ValueError:
            return False

        valid_governorates = {
            '01', '02', '03', '04', '11', '12', '13', '14', '15', '16', '17',
            '18', '19', '21', '22', '23', '24', '25', '26', '27', '28', '29',
            '31', '32', '33', '34', '35', '88'
        }

        return governorate in valid_governorates
