import csv


def read_csv_file(file_name):
    data = []

    # Membuka dan membaca file csv dengan with agar tertutup secara otomatis
    with open(file_name, mode="r") as file:
        temp = csv.reader(file)

        # Iterasi setiap baris dan menyimpannya ke dalam list data
        for row in temp:
            data.append(row)
            print(row)

    return data


if __name__ == "__main__":
    file_name = "username.csv"
    read_csv_file(file_name)
