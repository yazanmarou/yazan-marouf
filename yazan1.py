yazan1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
yazan2 = [80, 443, 21, 53]

y = dict(zip(yazan1, yazan2))
print(y)



yazan = int(input("Enter a number: "))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(yazan)
print(f"The factorial of {yazan} is {result}")




a = ['Network', 'Bio', 'Programming', 'Physics', 'Music']

for item in a:
    if item.startswith('B'):
        print(item)




     
z = {i: i+1 for i in range(11)}
print(z)







def binary_to_decimal(binary_str):
    """
    Converts a binary number (as a string) to its equivalent decimal number.
    """
    try:
     
        for D in binary_str:
            if D not in ['0', '1']:
                raise ValueError("Invalid binary number. Please enter a valid binary number.")
        
        
        deci = 0
        for i, bit in enumerate(reversed(binary_str)):
            deci += int(bit) * 2 ** i
        
        return deci
    
    except ValueError as w:
        print(w)
        return None


binary_number = input("Enter a binary number: ")


decimal_number = binary_to_decimal(binary_number)


if decimal_number is not None:
    print(f"The equivalent decimal number is: {decimal_number}")




    
import json
import csv

def calculate_score(user_answers, correct_answers):
    score = 0
    for question, answer in user_answers.items():
        if answer == correct_answers.get(question):
            score += 1
    return score

def save_results(user_name, user_answers, score, file_format):
    file_name = f'{user_name}_quiz_results.{file_format}'
    if file_format == 'json':
        with open(file_name, 'w') as json_file:
            json.dump({'username': user_name, 'result': f'{score}/20', 'Answers': user_answers}, json_file)
        print('results saved in JSON')
    elif file_format == 'csv':
        with open(file_name, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Question', 'User Answer'])
            for question, answer in user_answers.items():
                csv_writer.writerow([question, answer])
            csv_writer.writerow(['Score', f'{score}/20'])
        print('results saved in CSV')
    else:
        print('file format not available. do not save it.')

user_name = input(' your name: ')

file_name = input(' the file name : ')

with open(file_name, 'r') as file:
    inf = file.read()

questions_and_answers = json.loads(inf)

user_answers = {}
for question in questions_and_answers.keys():
    user_answer = input(f'Your answer for "{question}": ')
    user_answers[question] = user_answer

score = calculate_score(user_answers, questions_and_answers)
print(f'Your score is: {score}/20')

file_format = input('Choose the file format to save the results (JSON or CSV): ')
save_results(user_name, user_answers, score, file_format)


class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate

    def __str__(self):
        return f"Account Holder: {self.account_holder}\nAccount Balance: ${self.balance:.2f}\nInterest Rate: {self.interest_rate*100:.2f}%"

bank_account = BankAccount("124578963", "Ahmad Marouf")

bank_account.deposit(1000)
print(f"Current Balance: ${bank_account.get_balance():.2f}")

bank_account.withdraw(500)
print(f"Current Balance: ${bank_account.get_balance():.2f}")

savings_account = SavingsAccount("222333444", "Yazan Marouf", 0.05)

savings_account.apply_interest()
print(savings_account)
