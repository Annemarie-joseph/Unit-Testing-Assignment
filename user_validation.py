import unittest



class TestEmailValidation(unittest.TestCase):
    def test_valid_email(self):
        email = "user@example.com"
        result = UserValidation.validate_email(email)
        self.assertTrue(result)

    def test_missing_at_symbol(self):
        email = "userexample.com"
        result = UserValidation.validate_email(email)
        self.assertFalse(result)

    def test_missing_domain(self):
        email = "user@"
        result = UserValidation.validate_email(email)
        self.assertFalse(result)

    def test_invalid_tld(self):
        email = "user@mail.c"
        result = UserValidation.validate_email(email)
        self.assertFalse(result)

    def test_email_with_subdomain(self):
        email = "user@mail.company.com"
        result = UserValidation.validate_email(email)
        self.assertTrue(result)

    def test_email_with_special_characters(self):
        email = "ramy.gomaa_21@mail.co"
        result = UserValidation.validate_email(email)
        self.assertTrue(result)

    def test_uppercase_email(self):
        email = "USER@MAIL.COM"
        result = UserValidation.validate_email(email)
        self.assertTrue(result)

    def test_email_with_space(self):
        email = "user name@mail.com"
        result = UserValidation.validate_email(email)
        self.assertFalse(result)

    def test_empty_email(self):
        email = ""
        result = UserValidation.validate_email(email)
        self.assertFalse(result)

    def test_null_input(self):
        email = None
        result = UserValidation.validate_email(email)
        self.assertFalse(result)


class TestUsernameValidation(unittest.TestCase):
    def test_valid_username(self):
        username = "ramy_gomaa"
        result = UserValidation.validate_username(username)
        self.assertTrue(result)

    def test_username_too_short(self):
        username = "ab"
        result = UserValidation.validate_username(username)
        self.assertFalse(result)

    def test_username_too_long(self):
        username = "ramygomaaisaverylongusername"
        result = UserValidation.validate_username(username)
        self.assertFalse(result)

    def test_username_with_spaces(self):
        username = "ramy gomaa"
        result = UserValidation.validate_username(username)
        self.assertFalse(result)

    def test_username_with_symbols(self):
        username = "ramy@123"
        result = UserValidation.validate_username(username)
        self.assertFalse(result)

    def test_username_with_digits(self):
        username = "ramy123"
        result = UserValidation.validate_username(username)
        self.assertTrue(result)

    def test_empty_username(self):
        username = ""
        result = UserValidation.validate_username(username)
        self.assertFalse(result)

    def test_null_input(self):
        username = None
        result = UserValidation.validate_username(username)
        self.assertFalse(result)


class TestPhoneNumberValidation(unittest.TestCase):
    def test_valid_vodafone_number(self):
        phone = "01012345678"
        result = UserValidation.validate_phone_number(phone)
        self.assertTrue(result)

    def test_valid_orange_number(self):
        phone = "01234567890"
        result = UserValidation.validate_phone_number(phone)
        self.assertTrue(result)

    def test_valid_etisalat_number(self):
        phone = "01198765432"
        result = UserValidation.validate_phone_number(phone)
        self.assertTrue(result)

    def test_valid_we_number(self):
        phone = "01555555555"
        result = UserValidation.validate_phone_number(phone)
        self.assertTrue(result)

    def test_valid_vodafone_with_country_code(self):
        phone = "201012345678"
        result = UserValidation.validate_phone_number(phone)
        self.assertTrue(result)

    def test_valid_orange_with_country_code(self):
        phone = "201234567890"
        result = UserValidation.validate_phone_number(phone)
        self.assertTrue(result)

    def test_invalid_prefix(self):
        phone = "01812345678"
        result = UserValidation.validate_phone_number(phone)
        self.assertFalse(result)

    def test_too_short(self):
        phone = "0101234567"
        result = UserValidation.validate_phone_number(phone)
        self.assertFalse(result)

    def test_too_long(self):
        phone = "010123456789"
        result = UserValidation.validate_phone_number(phone)
        self.assertFalse(result)

    def test_contains_characters(self):
        phone = "01012abc678"
        result = UserValidation.validate_phone_number(phone)
        self.assertFalse(result)

    def test_empty_phone_number(self):
        phone = ""
        result = UserValidation.validate_phone_number(phone)
        self.assertFalse(result)

    def test_null_input(self):
        phone = None
        result = UserValidation.validate_phone_number(phone)
        self.assertFalse(result)


class TestNationalIDValidation(unittest.TestCase):
    def test_valid_national_id(self):
        national_id = "29812251234567"
        result = UserValidation.validate_national_id(national_id)
        self.assertTrue(result)

    def test_too_short(self):
        national_id = "2981225123456"
        result = UserValidation.validate_national_id(national_id)
        self.assertFalse(result)

    def test_too_long(self):
        national_id = "298122512345678"
        result = UserValidation.validate_national_id(national_id)
        self.assertFalse(result)

    def test_contains_letters(self):
        national_id = "2981225AB34567"
        result = UserValidation.validate_national_id(national_id)
        self.assertFalse(result)

    def test_invalid_century_code(self):
        national_id = "19812251234567"
        result = UserValidation.validate_national_id(national_id)
        self.assertFalse(result)

    def test_invalid_month(self):
        national_id = "29813251234567"
        result = UserValidation.validate_national_id(national_id)
        self.assertFalse(result)

    def test_invalid_day(self):
        national_id = "29812323234567"
        result = UserValidation.validate_national_id(national_id)
        self.assertFalse(result)

    def test_invalid_governorate_code(self):
        national_id = "29812380034567"
        result = UserValidation.validate_national_id(national_id)
        self.assertFalse(result)

    def test_empty_input(self):
        national_id = ""
        result = UserValidation.validate_national_id(national_id)
        self.assertFalse(result)

    def test_null_input(self):
        national_id = None
        result = UserValidation.validate_national_id(national_id)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
