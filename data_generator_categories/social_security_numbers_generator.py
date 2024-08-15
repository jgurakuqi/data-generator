from faker import Faker

from data_generator_categories.generators_executor import GeneratorsExecutor


class SocialSecurityNumbersGenerator(GeneratorsExecutor):
    """This class generates unique social security numbers using the Faker library."""

    @classmethod
    def generate_ssns(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate a list of Social Security Numbers.

        Args:
            batch_size (int): The number of Social Security Numbers to generate.
            max_attempts (int): The maximum number of retries before giving up.
            max_iterations_without_change (int): The maximum number of iterations without change before giving up.
            locale (str | list[str]): The locale to use for the Faker instance.

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of Social Security Numbers.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.ssn,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )
