from functools import partial
import random
import string
from data_generator_categories.generators_executor import GeneratorsExecutor


class GenericCodesGenerator(GeneratorsExecutor):
    """This class generates unique generic codes using the Faker library."""

    @classmethod
    def __generate_code(
        cls,
        max_code_length: int,
        min_code_length: int = 1,
        include_digits: bool = True,
        include_characters: bool = True,
    ) -> str:
        """Generate a random code.

        Args:
            max_code_length (int): The maximum length of the code.
            min_code_length (int, optional): The minimum length of the code. Defaults to 1.
            include_digits (bool, optional): Tells whether to include digits in the code. Defaults to True.
            include_characters (bool, optional): Tells whether to include characters in the code. Defaults to True.

        Returns:
            str: The generated code.
        """
        characters = ""
        if include_digits:
            characters += string.digits
        if include_characters:
            characters += string.ascii_letters
        random_length = random.randint(min_code_length, max_code_length)
        return "".join(random.choice(characters) for _ in range(random_length))

    @classmethod
    def generate_codes(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        max_code_length: int,
        include_digits: bool = True,
        include_characters: bool = True,
        min_code_length: int = 1,
    ) -> list[str]:
        """Generate a list of random codes.

        Args:
            batch_size (int): The number of codes to generate.
            max_attempts (int): The maximum number of attempts to generate a unique code.
            max_iterations_without_change (int): The maximum number of iterations without change before giving up.
            max_code_length (int): The maximum length of the code.
            include_digits (bool, optional): Tells whether to include digits in the code. Defaults to True.
            include_characters (bool, optional): Tells whether to include characters in the code. Defaults to True.
            min_code_length (int, optional): The minimum length of the code. Defaults to 1.

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: The list of generated codes.
        """
        if not include_digits and not include_characters:
            raise ValueError(
                "FakeDataGenerator::generate_codes::At least one of include_digits or include_characters must be True"
            )
        if max_code_length < min_code_length:
            raise ValueError(
                "FakeDataGenerator::generate_codes::max_code_length must be greater than or equal to min_code_length"
            )
        if min_code_length < 1:
            raise ValueError(
                "FakeDataGenerator::generate_codes::min_code_length must be greater than or equal to 1"
            )

        partialised_generate_code = partial(
            cls.__generate_code,
            min_code_length=min_code_length,
            max_code_length=max_code_length,
            include_digits=include_digits,
            include_characters=include_characters,
        )
        return super().generate_unique_data(
            generator_function=partialised_generate_code,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )
