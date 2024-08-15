from faker import Faker

from data_generator_categories.generators_executor import GeneratorsExecutor


class PhoneNumbersGenerator(GeneratorsExecutor):
    """This class generates unique phone numbers using the Faker library."""

    @classmethod
    def generate_phone_numbers(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique phone numbers using the Faker library.

        Args:
            batch_size (int): The number of unique phone numbers to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique phone numbers.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.phone_number,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )
