from functools import partial
import random
from urllib.parse import urlencode, urlunparse
from faker import Faker
from data_generator_categories.generators_executor import GeneratorsExecutor


class VirtualAddressesGenerator(GeneratorsExecutor):
    """This class generates unique URLs using the Faker library."""

    @classmethod
    def __generate_url(
        cls,
        faker_instance: Faker,
        max_path_length: int = 10,
        max_query_length: int = 5,
    ) -> str:
        """Generate a random URL using the Faker library.

        Args:
            faker_instance (Faker): An instance of the Faker library.
            max_path_length (int, optional): The maximum length of the URL path. Defaults to 10.
            max_query_length (int, optional): The maximum number of query parameters. Defaults to 5.

        Returns:
            str: A randomly generated URL.
        """
        protocols = ["http", "https"]
        protocol = random.choice(protocols)
        domain = faker_instance.unique.domain_word()
        subdomain = faker_instance.unique.domain_word() if random.random() < 0.5 else ""
        tld = faker_instance.unique.tld()
        path_length = random.randint(0, max_path_length)
        path = "/".join(faker_instance.unique.slug() for _ in range(path_length))
        common_params = ["id", "page", "sort", "filter", "lang", "search"]
        query_length = random.randint(0, max_query_length)
        query_params = {
            random.choice(common_params): faker_instance.unique.word()
            for _ in range(query_length)
        }
        netloc = f"{subdomain + '.' if subdomain else ''}{domain}.{tld}"
        query_string = urlencode(query_params)
        url = urlunparse((protocol, netloc, path, "", query_string, ""))
        return url

    @classmethod
    def generate_urls(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique URLs using the Faker library.

        Args:
            batch_size (int): The number of unique URLs to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique URLs.
        """
        return super().generate_unique_data(
            cls.__generate_url,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_ipv4_addresses(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique IPv4 addresses using the Faker library.

        Args:
            batch_size (int): The number of unique IPv4 addresses to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique IPv4 addresses.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.ipv4,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_ipv6_addresses(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique IPv6 addresses using the Faker library.

        Args:
            batch_size (int): The number of unique IPv6 addresses to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique IPv6 addresses.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.ipv6,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_mac_addresses(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        multicast: bool,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate unique MAC addresses using the Faker library.

        Args:
            batch_size (int): The number of unique MAC addresses to generate.
            max_attempts (int): The maximum number of attempts before stopping.
            max_iterations_without_change (int): The maximum number of iterations without change before stopping.
            multicast (bool): Whether to generate multicast MAC addresses.
            locale (str | list[str], optional): The locale to use. Defaults to "en_US".

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of unique MAC addresses.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        parametrised_mac_function = partial(
            faker_instance.unique.mac_address, multicast=multicast
        )
        return super().generate_unique_data(
            generator_function=parametrised_mac_function,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_personal_emails(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate a list of personal emails.

        Args:
            batch_size (int): The number of personal emails to generate.
            max_attempts (int): The maximum number of retries before giving up.
            max_iterations_without_change (int): The maximum number of iterations without change before giving up.
            locale (str | list[str]): The locale to use for the Faker instance.

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of personal emails.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.free_email,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_personal_example_emails(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate a list of personal emails.

        Args:
            batch_size (int): The number of personal emails to generate.
            max_attempts (int): The maximum number of retries before giving up.
            max_iterations_without_change (int): The maximum number of iterations without change before giving up.
            locale (str | list[str]): The locale to use for the Faker instance.

        Raises:
            ValueError: if batch_size is greater than max_attempts
            ValueError: if max_iterations_without_change is greater than max_attempts
            ValueError: if max_iterations_without_change is less than 0
            ValueError: if batch_size is less than or equal to 0

        Returns:
            list[str]: A list of personal emails.
        """
        faker_instance = Faker(use_weighting=False, locale=locale)
        return super().generate_unique_data(
            generator_function=faker_instance.unique.email,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )

    @classmethod
    def generate_company_emails(
        cls,
        batch_size: int,
        max_attempts: int,
        max_iterations_without_change: int,
        locale: str | list[str] = "en_US",
    ) -> list[str]:
        """Generate a list of company emails.

        Args:
            batch_size (int): The number of company emails to generate.
            max_attempts (int): The maximum number of retries before giving up.
            max_iterations_without_change (int): The maximum number of iterations without change before giving up.
            locale (str | list[str], optional): The locale to use for the Faker instance. Defaults to "en_US".

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
            generator_function=faker_instance.unique.company_email,
            batch_size=batch_size,
            max_attempts=max_attempts,
            max_iterations_without_change=max_iterations_without_change,
        )
