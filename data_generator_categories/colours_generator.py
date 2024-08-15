from functools import partial
from typing import Sequence
from faker import Faker

from data_generator_categories.generators_executor import GeneratorsExecutor


class ColoursGenerator(GeneratorsExecutor):
    """This class generates unique colours using the Faker library."""

    @classmethod
    def generate_colours(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
        hue: str | float | int | Sequence[int] | None = None,
        luminosity: str | None = None,
        color_format: str = "hex",
    ) -> list[str]:
        """Generate unique colours. Look at Faker documentation for more information about
        hue, luminosity and color_format: https://faker.readthedocs.io/en/stable/providers/faker.providers.color.html

        Args:
            batch_size (int): The number of colours to generate.
            max_attempts (int): The maximum number of attempts to generate a unique colour.
            max_iterations_without_change (int): The maximum number of iterations without change before giving up.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".
            hue (str | float | int | Sequence[int] | None, optional): The hue of the colour. Defaults to None.
            luminosity (str | None, optional): The luminosity of the colour. Defaults to None.
            color_format (str, optional): The format of the colour. Defaults to "hex".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: The generated colours.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        parialised_color = partial(
            faker_instance.unique.color,
            hue=hue,
            luminosity=luminosity,
            color_format=color_format,
        )
        return super().generate_unique_data(
            generator_function=parialised_color,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_colour_names(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique colour names.

        Args:
            batch_size (int): The number of colour names to generate.
            max_attempts (int): The maximum number of attempts to generate a unique colour name.
            max_iterations_without_change (int): The maximum number of iterations without change before giving up.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: The generated colour names.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.color_name,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_web_safe_colour_names(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique web safe colour names.

        Args:
            batch_size (int): The number of web safe colour names to generate.
            max_attempts (int): The maximum number of attempts to generate a unique web safe colour name.
            max_iterations_without_change (int): The maximum number of iterations without change before giving up.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: The generated web safe colour names.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.safe_color_name,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )
