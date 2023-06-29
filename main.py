from utils import get_data, get_executed_operations, get_last_operations, get_data_format


def main():
    data = get_data()
    data = get_executed_operations(data)
    data = get_last_operations(data, count_last_operations=5)
    data = get_data_format(data)

    for item in data:
        print(item, end="\n\n")


if __name__ == "__main__":
    main()
