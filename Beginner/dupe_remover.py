def remove_duplicates():

    shopping_list = []

    while True:
        item = input("\nAdd an item to your shopping list\nsay 'done' when you're finished! ")

        if item.lower() == "done":
            break

        shopping_list.append(item)

    unique_shopping_list = set(shopping_list)

    print("Here is your list with duplications removed! ")

    for item in unique_shopping_list:
        print(item)

    return unique_shopping_list

remove_duplicates()

