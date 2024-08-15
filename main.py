from data_generator import DataGenerator


def main():
    # print(
    #     len(
    #         generator.names_generator.generate_first_names(
    #             batch_size=1_000,
    #             max_attempts=1_000_000_000,
    #             max_iterations_without_change=20,
    #         )
    #     )
    # )
    print("Supported locales:", DataGenerator.get_supported_locales())
    data = DataGenerator.bank_codes_generator.generate_bban_codes(
        batch_size=1_000_000,
        max_attempts=1_000_000,
        max_iterations_without_change=5_000,
    )
    print(len(data))


if __name__ == "__main__":
    main()
