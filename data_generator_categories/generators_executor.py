from typing import Callable


class GeneratorsExecutor:

    @staticmethod
    def generate_unique_data(
        generator_function: Callable,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
    ) -> list[str]:
        """Generate unique data in batches using the provided generator function.

        Args:
            generator_function (Callable): The generator function to use.
            batch_size (int): The number of unique values to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique values.
        """
        unique_data = set()
        iterations_without_change = 0

        if batch_size > max_attempts:
            raise ValueError(
                "GeneratorsExecutor::generate_unique_data::batch_size must be less than or equal to max_attempts"
            )

        if max_iterations_without_change > max_attempts:
            raise ValueError(
                "GeneratorsExecutor::generate_unique_data::max_iterations_without_change must be less than or equal to max_attempts"
            )

        if max_iterations_without_change < 0:
            raise ValueError(
                "GeneratorsExecutor::generate_unique_data::max_iterations_without_change must be greater than or equal to 0"
            )

        if batch_size <= 0:
            raise ValueError(
                "GeneratorsExecutor::generate_unique_data::batch_size must be greater than 0"
            )

        for _ in range(max_attempts):
            data_before = len(unique_data)
            try:
                new_data = generator_function()
            except:
                break
            finally:
                unique_data.add(new_data)
                data_after = len(unique_data)

                if data_before == data_after:
                    iterations_without_change += 1
                    if iterations_without_change == max_iterations_without_change:
                        break
                else:
                    iterations_without_change = 0

                if len(unique_data) == batch_size:
                    break

        return list(unique_data)
