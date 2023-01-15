# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Main:
    def is_prime(number):
        for element in range(2, number):
            if number % element == 0:
                return False
        return True



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hello world")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
