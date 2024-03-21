#Benedetto Aiello
#CS-175-2
#Average input pt 2
def calculate_avg(file_name):
    try:
        with open (file_name, 'r') as file:
            total = 0
            count = 0
            for line in file:
                try:
                    number = int(line.strip())
                except ValueError:
                    print(f"Error: Bad Input {line.strip()} skipping")
                    continue
                count += 1
                total += number
                print(f"I read in {count} number(s) Current number is: {number:8.2f} Total is: {total:8.2f}")

        average = total / count if count > 0 else 0
        print(f"Average: {average:.1f}")

    except IOError:
        print(f"SystemExit: File not found: '{file_name}'- exiting")

def main():
    file_name = 'numbers.txt'
    calculate_avg(file_name)

if __name__ == "__main__":
    main()
