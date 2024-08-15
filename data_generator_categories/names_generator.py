import random
from faker import Faker
from data_generator_categories.generators_executor import GeneratorsExecutor


class NamesGenerator(GeneratorsExecutor):
    """This class generates unique names using the Faker library."""

    @classmethod
    def generate_first_names(
        cls,
        batch_size: int,
        max_attempts: int = 1_000_000,
        max_iterations_without_change: int = 50_000,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique persons' first names.

        Args:
            batch_size (int): The number of unique first names to generate.
            max_attempts (int, optional): The maximum number of attempts before stopping. Defaults to 1_000_000.
            max_iterations_without_change (int, optional): The maximum number of iterations without change before stopping. Defaults to 50_000.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique first names matching the provided locale.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.first_name,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_last_names(
        cls,
        batch_size: int,
        max_attempts: int = 1_000_000,
        max_iterations_without_change: int = 50_000,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique persons' last names.

        Args:
            batch_size (int): The number of unique last names to generate.
            max_attempts (int, optional): The maximum number of attempts before stopping. Defaults to 1_000_000.
            max_iterations_without_change (int, optional): The maximum number of iterations without change before stopping. Defaults to 50_000.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique last names matching the provided locale.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.last_name,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_full_names_single_locale(
        cls,
        batch_size: int,
        max_attempts: int = 1_000_000,
        max_iterations_without_change: int = 50_000,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique persons' full names where each full name is composed by a first name
        and a last name both belonging to the same locale.

        Args:
            batch_size (int): The number of unique full names to generate.
            max_attempts (int, optional): The maximum number of attempts before stopping. Defaults to 1_000_000.
            max_iterations_without_change (int, optional): The maximum number of iterations without change before stopping. Defaults to 50_000.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique full names matching the provided locale.
        """
        faker_instance: Faker = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.name,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_full_names(
        cls,
        batch_size: int,
        max_attempts: int = 1_000_000,
        max_iterations_without_change: int = 50_000,
        locales: list[str] = ["en_US", "it_IT"],
        random_shuffling: bool = True,
    ) -> list[str]:
        """Generate unique persons' full names where each full name is composed by a first name
        and a last name both belonging to possibly different locales.

        Args:
            batch_size (int): The number of unique full names to generate.
            max_attempts (int, optional): The maximum number of attempts before stopping. Defaults to 1_000_000.
            max_iterations_without_change (int, optional): The maximum number of iterations without change before stopping. Defaults to 50_000.
            locales (list[str], optional): The locales to use. Defaults to ["en_US", "it_IT"].
            random_shuffling (bool, optional): Whether to shuffle the generated data. Defaults to True.

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique full names matching the provided locales.
        """
        first_names = []
        last_names = []
        first_names += cls.generate_first_names(
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
            locale=locales,
        )
        print(f"First names: {len(first_names)}")
        last_names += cls.generate_last_names(
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
            locale=locales,
        )
        print(f"Last names: {len(last_names)}")
        if random_shuffling:
            random.shuffle(first_names)
            random.shuffle(last_names)
        return [
            f"{first_name} {last_name}"
            for first_name, last_name in zip(first_names, last_names)
        ]

    @classmethod
    def generate_company_names(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate a list of unique company names.

        Args:
            batch_size (int): The number of unique company names to generate.
            max_attempts (int): The maximum number of attempts to generate a unique company name.
            max_iterations_without_change (int): The maximum number of iterations without change before giving up.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique company names.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.company,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )
