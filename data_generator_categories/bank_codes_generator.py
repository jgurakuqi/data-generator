from functools import partial
from faker import Faker
from data_generator_categories.generators_executor import GeneratorsExecutor
from data_generator_categories.generators_helpers.card_number.valid_card_number_generator import (
    ValidCardNumberGenerator,
)
from data_generator_categories.generators_helpers.iban.valid_iban_generator import (
    ValidIbanGenerator,
)


class BankCodesGenerator(GeneratorsExecutor):
    """This class generates unique bank codes using the Faker library."""

    @classmethod
    def generate_unchecked_credit_card_numbers(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unchecked card numbers.

        Args:
            batch_size (int): The number of credit card numbers to generate.
            max_attempts (int): The maximum number of attempts to generate a unique card number.
            max_iterations_without_change (int): The maximum number of iterations without change before giving up.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: The generated card numbers.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.credit_card_number,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_valid_credit_card_numbers(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate valid card numbers.

        Args:
            batch_size (int): The number of credit card numbers to generate.
            max_attempts (int): The maximum number of attempts to generate a unique card number.
            max_iterations_without_change (int): The maximum number of iterations without change before giving up.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of valid card numbers.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        partilised_card_numbers_generator = partial(
            ValidCardNumberGenerator.generate,
            faker_instance=faker_instance,
        )
        return super().generate_unique_data(
            generator_function=partilised_card_numbers_generator,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    # @TODO: make the generator locale dependent
    @classmethod
    def generate_valid_ibans(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique valid IBANs using the ValidIbanGenerator class.

        Args:
            batch_size (int): The number of unique valid IBANs to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique valid IBANs.
        """
        return super().generate_unique_data(
            generator_function=ValidIbanGenerator.generate,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_aba_codes(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique ABA codes using the Faker library.

        Args:
            batch_size (int): The number of unique ABA codes to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique ABA codes.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.aba,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_bban_codes(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique BBAN codes using the Faker library.

        Args:
            batch_size (int): The number of unique BBAN codes to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique BBAN codes.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.bban,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_unchecked_ibans(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique unchecked IBANs using the Faker library.

        Args:
            batch_size (int): The number of unique unchecked IBANs to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique unchecked IBANs.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.iban,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_swift8_codes(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique Swift8 codes using the Faker library.

        Args:
            batch_size (int): The number of unique Swift8 codes to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique Swift8 codes.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.swift8,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_swift11_codes(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique Swift11 codes using the Faker library.

        Args:
            batch_size (int): The number of unique Swift11 codes to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique Swift11 codes.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.swift11,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )
