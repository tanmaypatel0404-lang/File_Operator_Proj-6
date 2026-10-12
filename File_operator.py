from datetime import datetime

class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"

    # Add new entry
    def add_entry(self):
        try:
            entry = input("Enter your journal entry: ")

            if entry == "":
                print("Entry cannot be empty.")
                return

            # Create file if it does not exist
            try:
                file = open(self.filename, "x")
                file.close()
            except FileExistsError:
                pass

            # Append the new entry
            file = open(self.filename, "a")

            current_time = datetime.now()
            time = current_time.strftime("%Y-%m-%d %H:%M:%S")

            file.write("[" + time + "]\n")
            file.write(entry + "\n")
            file.write("-" * 30 + "\n")

            file.close()

            print("Entry added successfully.")

        except PermissionError:
            print("Error: Permission denied.")
        except Exception as e:
            print("Error:", e)

    # View all journal entries
    def view_entries(self):
        try:
            file = open(self.filename, "r")

            content = file.read()
            file.close()

            if content == "":
                print("No journal entries found.")
            else:
                print("\nYour Journal Entries:")
                print("-" * 30)
                print(content)

        except FileNotFoundError:
            print("Error: The journal file does not exist.")
            print("Please add a new entry first.")

        except PermissionError:
            print("Error: Permission denied.")

    # Search for an entry
    def search_entry(self):
        try:
            keyword = input("Enter a keyword or date to search: ")

            file = open(self.filename, "r")
            content = file.read()
            file.close()

            if keyword.lower() in content.lower():
                print("\nMatching Entries:")
                print("-" * 30)

                entries = content.split("-" * 30)

                for entry in entries:
                    if keyword.lower() in entry.lower():
                        print(entry.strip())
                        print("-" * 30)

            else:
                print("No entries were found for the keyword:", keyword)

        except FileNotFoundError:
            print("Error: The journal file does not exist.")
            print("Please add a new entry first.")

        except PermissionError:
            print("Error: Permission denied.")

    # Delete all journal entries
    def delete_entries(self):
        try:
            # Check whether file exists
            file = open(self.filename, "r")
            file.close()

            confirm = input(
                "Are you sure you want to delete all entries? (yes/no): "
            )

            if confirm.lower() == "yes":

                # w mode clears the file
                file = open(self.filename, "w")
                file.close()

                print("All journal entries have been deleted.")

            elif confirm.lower() == "no":
                print("Delete operation cancelled.")

            else:
                print("Invalid input. Please enter yes or no.")

        except FileNotFoundError:
            print("No journal entries to delete.")

        except PermissionError:
            print("Error: Permission denied.")


# Main program
journal = JournalManager()

print("Welcome to Personal Journal Manager!")

while True:

    print("\nPlease select an option:")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        journal.add_entry()

    elif choice == "2":
        journal.view_entries()

    elif choice == "3":
        journal.search_entry()

    elif choice == "4":
        journal.delete_entries()

    elif choice == "5":
        print("Thank you for using Personal Journal Manager. Goodbye!")
        break

    else:
        print("Invalid option. Please select a valid option from the menu.")
