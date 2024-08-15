from faker import Faker
from data_generator_categories.generators_executor import GeneratorsExecutor


class CurrencyCodesGenerator(GeneratorsExecutor):
    """This class generates unique currency codes using the Faker library."""

    @classmethod
    def generate_cryptocurrencies(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique cryptocurrencies using the Faker library.

        Args:
            batch_size (int): The number of unique cryptocurrencies to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique cryptocurrencies.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.cryptocurrency,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_cryptocurrency_codes(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique cryptocurrency codes using the Faker library.

        Args:
            batch_size (int): The number of unique cryptocurrency codes to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique cryptocurrency codes.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.cryptocurrency_code,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_cryptocurrency_names(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique cryptocurrency names using the Faker library.

        Args:
            batch_size (int): The number of unique cryptocurrency names to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique cryptocurrency names.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.cryptocurrency_name,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_currencies(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique currencies using the Faker library.

        Args:
            batch_size (int): The number of unique currencies to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique currencies.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.currency,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_currency_codes(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique currency codes using the Faker library.

        Args:
            batch_size (int): The number of unique currency codes to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique currency codes.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.currency_code,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_currency_names(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique currency names using the Faker library.

        Args:
            batch_size (int): The number of unique currency names to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique currency names.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.currency_name,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_currency_symbols(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique currency symbols using the Faker library.

        Args:
            batch_size (int): The number of unique currency symbols to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique currency symbols.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.currency_symbol,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_pricetags(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique price tags using the Faker library.

        Args:
            batch_size (int): The number of unique price tags to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique price tags.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.pricetag,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )
