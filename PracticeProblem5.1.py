# Implement all of the operations of a Queue using list
# Using stack() LIFO using push() and pop(). queue() is FIFO, stack() is LIFO

FruitQueue = []

def enqueue():
    FruitQueue.append(input("Enter a fruit: "))
def dequeue():
    FruitQueue.pop(0)
def display_queue():
    print(FruitQueue)
def stop():
    print("Stopping Program")
    exit()

while True:
    print("Menu")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        enqueue()
    elif choice == "2":
        dequeue()
    elif choice == "3":
        display_queue()
    elif choice == "4":
        stop()
