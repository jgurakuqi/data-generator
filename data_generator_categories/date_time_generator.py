from faker import Faker
from data_generator_categories.generators_executor import GeneratorsExecutor


class DateTimesGenerator(GeneratorsExecutor):
    """This class generates unique dates and times using the Faker library."""

    @classmethod
    def generate_dates(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate a list of unique dates.

        Args:
            batch_size (int): The number of unique dates to generate.
            max_attempts (int): The maximum number of retries before giving up.
            max_iterations_without_change (int): The maximum number of iterations without change before giving up.
            locale (str | list[str], optional): The locale to use for the Faker instance. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique dates.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.date,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_times(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate a list of unique times.

        Args:
            batch_size (int): The number of unique times to generate.
            max_attempts (int): The maximum number of retries before giving up.
            max_iterations_without_change (int): The maximum number of iterations without change before giving up.
            locale (str | list[str], optional): The locale to use for the Faker instance. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique times.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.time,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_datetimes(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate a list of unique datetimes.

        Args:
            batch_size (int): The number of unique datetimes to generate.
            max_attempts (int): The maximum number of retries before giving up.
            max_iterations_without_change (int): The maximum number of iterations without change before giving up.
            locale (str | list[str], optional): The locale to use for the Faker instance. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique datetimes.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.date_time,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_months(
        cls,
        batch_size: int,
        max_iterations_without_change: int,
        max_attempts: int = 5_000,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate a list of unique months.

        Args:
            batch_size (int): The number of unique months to generate.
            max_iterations_without_change (int): The maximum number of iterations without change before giving up.
            max_attempts (int, optional): The maximum number of attempts to generate a unique month. Defaults to 5_000.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique months.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.month_name,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_years(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate a list of unique years.

        Args:
            batch_size (int): The number of unique years to generate.
            max_attempts (int): The maximum number of attempts to generate a unique year.
            max_iterations_without_change (int): The maximum number of iterations without change before giving up.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: _description_
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.year,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )
