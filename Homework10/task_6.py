def car(manufacturer, release_year = 2024, **kwargs):
    print(f"manufacturer is {manufacturer}")
    print(f"release year is {release_year}")
    if kwargs:
        for key, value in kwargs.items():
            print(f"{key} is {value}")
    print("*" * 30)

car("chevrolet", 2021, brand_name = "camaro", quantity = 21)
car("mercedes", brand_name = "C class", quantity = 32)
car("chevrolet", 2020, brand_name = "corvette", quntity = 120)
car("BMW")

