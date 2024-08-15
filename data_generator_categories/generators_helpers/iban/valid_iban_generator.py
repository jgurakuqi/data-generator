import random
from schwifty import IBAN
from data_generator_categories.generators_helpers.iban.valid_iban_country_codes import (
    valid_country_codes as imported_valid_country_codes,
)
from data_generator_categories.generators_helpers.i_generator import iGenerator


class ValidIbanGenerator(iGenerator):
    valid_country_codes: list[str] = imported_valid_country_codes

    @classmethod
    def __generate_random_digits(cls, length: int) -> str:
        """Generate a string of random digits.

        Args:
            length (int): The length of the string to generate.

        Returns:
            str: The generated string of random digits.
        """
        return "".join(random.choices("0123456789", k=length))

    @classmethod
    def generate(cls, max_attempts: int = 1_000_000) -> str | None:

        for _ in range(max_attempts):
            random_country_code = random.choice(cls.valid_country_codes)
            random_bank_code = cls.__generate_random_digits(4)
            random_account_number = cls.__generate_random_digits(10)

            try:
                generated_iban = IBAN.generate(
                    country_code=random_country_code,
                    bank_code=random_bank_code,
                    account_code=random_account_number,
                )
                return str(generated_iban)
            except:
                pass

        print(
            f"IbanGenerator::generate_valid_iban::Failed to generate an IBAN after {max_attempts} attempts."
        )
        return None
