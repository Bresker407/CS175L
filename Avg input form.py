#Benedetto Aiello
#CSL 175
def calculate_avg(file_name):
    with open (file_name, 'r') as file:
        total = 0
        count = 0
        for line in file:
            number = int(line.strip())
            count += 1
            total += number
            print(f"I read in {count} number(s) Current number is: {number:8.2f} Total is: {total:8.2f}")
 
    average = total / count if count > 0 else 0
    print(f"Average: {average:.1f}")
 
def main():
    file_name = 'numbers.txt'
    calculate_avg(file_name)
 
if __name__ == "__main__":
    main()
