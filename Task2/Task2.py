import timeit
import csv
from BTrees.OOBTree import OOBTree


def get_key_values_from_csv(csv_file_path: str) -> {int: dict}:
    csv_file_data = dict()
    with open(csv_file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row["ID"])  # Convert the identifier to integer type
            values = {
                "Name": row["Name"],
                "Category": row["Category"],
                "Price": float(row["Price"]),  # Convert the price to float type
            }
            csv_file_data[id] = values

    return csv_file_data


def add_item_to_tree(_tree: OOBTree, csv_file_data: []):
    _tree.update(csv_file_data)


def add_item_to_dict(_dict: dict, csv_file_data: []):
    _dict.update(csv_file_data)


# Create functions to perform a range query, retrieving all products within a defined price range
def range_query_tree(my_tree: OOBTree, start_price: float, end_price: float):
    return list(my_tree.items(min=start_price, max=end_price))


def range_query_dict(my_dict: dict, start_price: float, end_price: float):
    result = []
    for key, value in my_dict.items():
        if start_price <= value["Price"] <= end_price:
            result.append({key: value})
    return result


if __name__ == "__main__":
    # Create data structures
    my_tree = OOBTree()
    my_dict = dict()

    # Specify path to CSV file
    csv_file_path = "generated_items_data.csv"

    csv_file_data = get_key_values_from_csv(csv_file_path)

    # Populate the data structures
    add_item_to_tree(my_tree, csv_file_data)
    add_item_to_dict(my_dict, csv_file_data)

    # Set minimum and maximum price for range query
    min_price = 140
    max_price = 141

    print(
        f"Total range_query time for OOBTree: {timeit.timeit(stmt=lambda: range_query_tree(my_tree, min_price, max_price), number=100)} seconds"
    )
    print(
        f"Total range_query time for dict: {timeit.timeit(stmt=lambda: range_query_dict(my_dict, min_price, max_price), number=100)} seconds"
    )
