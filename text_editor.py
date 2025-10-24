MAX_TEXT_SIZE = 100
MAX_ACTIONS = 10

text = ""
undo_stack = []
redo_stack = []

def insert_text(new_text):
    global text

    if len(undo_stack) < MAX_ACTIONS:
        undo_stack.append(text)

    if len(text) + len(new_text) <= MAX_TEXT_SIZE:
        text = text + new_text
        redo_stack.clear()
    else:
        print("Text is too long!")

def undo():
    global text

    if len(undo_stack) > 0:
        redo_stack.append(text)
        text = undo_stack.pop()
    else:
        print("Nothing to undo.")

def redo():
    global text

    if len(redo_stack) > 0:
        undo_stack.append(text)
        text = redo_stack.pop()
    else:
        print("Nothing to redo.")

def display_text():
    print("Current text: " + text)

def main():
    while True:
        print("\nText Editor - Choose an option:")
        print("1. Insert Text")
        print("2. Undo")
        print("3. Redo")
        print("4. Show Text")
        print("5. Exit")
        
        choice = input("Your choice: ")

        if choice == "1":
            new_text = input("Enter text to insert: ")
            insert_text(new_text)
        elif choice == "2":
            undo()
        elif choice == "3":
            redo()
        elif choice == "4":
            display_text()
        elif choice == "5":
            print("Exiting editor...")
            break
        else:
            print("Invalid choice. Please try again.")

main()
