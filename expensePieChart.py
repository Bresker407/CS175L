#CS 175
#Benedetto Aiello
#Expense Pie Chart
import matplotlib.pyplot as plt

def read_expenses(filename):
    expenses = {}
    try:
        file = open(filename, 'r')
        for line in file:
            try:
                category, amount = line.strip().split('\t')
                expenses[category] = int(amount)
            except ValueError:
                    print("Error: Data conversion error occurred while reading line:", line.strip())
    except IOError:
        print("Error: Unable to open file", filename)
    return expenses

def plot_pie_chart(expenses):
    labels = expenses.keys()
    amounts = expenses.values()

    plt.figure(figsize=(8, 6))
    plt.pie(amounts, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  
    plt.title('Expense Distribution')
    plt.show()

def main():
    filename = 'expenses.txt'
    expenses = read_expenses(filename)
    if expenses:
        plot_pie_chart(expenses)

if __name__ == "__main__":
    main()
