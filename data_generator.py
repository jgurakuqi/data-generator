from faker import Faker
from typing import Any
from faker.config import AVAILABLE_LOCALES
from data_generator_categories.names_generator import NamesGenerator
from data_generator_categories.virtual_addresses_generator import (
    VirtualAddressesGenerator,
)
from data_generator_categories.date_time_generator import DateTimesGenerator
from data_generator_categories.physical_addresses_generator import (
    PhysicalAddressesGenerator,
)
from data_generator_categories.bank_codes_generator import BankCodesGenerator
from data_generator_categories.vat_codes_generator import VatCodesGenerator
from data_generator_categories.phone_numbers_generator import PhoneNumbersGenerator
from data_generator_categories.social_security_numbers_generator import (
    SocialSecurityNumbersGenerator,
)
from data_generator_categories.generic_codes_generator import GenericCodesGenerator
from data_generator_categories.text_generator import TextGenerator
from data_generator_categories.colours_generator import ColoursGenerator


class DataGenerator:
    """This class interfaces with the Faker library and other generator classes
    to generate data in batches.
    """

    names_generator = NamesGenerator
    virtual_addresses_generator = VirtualAddressesGenerator
    date_times_generator = DateTimesGenerator
    physical_addresses_generator = PhysicalAddressesGenerator
    bank_codes_generator = BankCodesGenerator
    vat_codes_generator = VatCodesGenerator
    social_security_numbers_generator = SocialSecurityNumbersGenerator
    phone_numbers_generator = PhoneNumbersGenerator
    generic_codes_generator = GenericCodesGenerator
    text_generator = TextGenerator
    colours_generator = ColoursGenerator

    def __setattr__(self, name: str, value: Any) -> None:
        """Set an attribute on the DataGenerator object. This method prevents the
        user from changing immutable attributes such as the generator classes references.

        Args:
            name (str): The name of the attribute to set.
            value (Any): The value to set the attribute to.

        Raises:
            AttributeError: If the attribute is immutable.
        """
        immutable_attributes = [
            "names_generator",
            "virtual_addresses_generator",
            "date_times_generator",
            "physical_addresses_generator",
            "bank_codes_generator",
            "vat_codes_generator",
            "social_security_numbers_generator",
            "phone_numbers_generator",
            "generic_codes_generator",
            "text_generator",
        ]
        if name in immutable_attributes:
            raise AttributeError(
                f"DataGenerator::__setattr__::ERROR::{name} is immutable."
            )
        super().__setattr__(name, value)

    @staticmethod
    def __get_locale(lc: str) -> str:
        """Get the locale from the locale code.

        Args:
            lc (str): The locale code.

        Returns:
            str: The locale.
        """
        loc = lc.split("_")
        if len(loc) > 1:
            return loc[1].upper()
        else:
            return loc[0].upper()

    @classmethod
    def get_supported_locales(cls) -> list[str]:
        """Get the list of supported locales.

        Returns:
            list[str]: The list of supported locales.
        """
        faker_instance = Faker(
            use_weighting=False,
        )
        return [
            faker_instance.unique.local_latlng(
                country_code=cls.__get_locale(local), coords_only=False
            )
            for local in AVAILABLE_LOCALES
        ]
