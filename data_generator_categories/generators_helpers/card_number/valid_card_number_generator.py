from faker import Faker
from data_generator_categories.generators_helpers.i_generator import iGenerator


class ValidCardNumberGenerator(iGenerator):

    @staticmethod
    def luhn_checksum(card_number: str) -> bool:
        try:
            digits = [int(d) for d in str(card_number)]
        except:
            return False

        for i in range(len(digits) - 2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] -= 9

        checksum = sum(digits)
        return checksum % 10 == 0

    @classmethod
    def generate(
        cls, faker_instance: Faker, max_attempts: int = 1_000_000
    ) -> str | None:
        for _ in range(max_attempts):
            card_number = faker_instance.credit_card_number()
            if cls.luhn_checksum(card_number):
                return card_number

        print(
            f"CardNumberGenerator::generate::Failed to generate a card number after {max_attempts} attempts."
        )
        return None
