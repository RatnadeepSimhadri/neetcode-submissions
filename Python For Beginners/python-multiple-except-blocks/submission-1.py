def divide_numbers(a: str, b: str) -> None:
    try:
        a_num = int(a)
        b_num = int(b)
        result = a_num / b_num
        print(result)
    except ValueError:
        print("Error: Invalid value!")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except Exception:
        print("An error occured:")





# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
