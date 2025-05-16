accounts = {}


def deposit(name, sum_):
    if name not in accounts:
        accounts[name] = 0
    accounts[name] += sum_


def withdraw(name, sum_):
    if name not in accounts:
        accounts[name] = 0
    accounts[name] -= sum_


def balance(name):
    if name not in accounts:
        return "ERROR"
    return str(accounts[name])


def transfer(name1, name2, sum_):
    if name1 not in accounts:
        accounts[name1] = 0
    if name2 not in accounts:
        accounts[name2] = 0
    accounts[name1] -= sum_
    accounts[name2] += sum_


def income(p):
    for name, balance in accounts.items():
        if balance > 0:
            accounts[name] += int(balance * p / 100)


strs = input().split()
while strs != ' ':
    operation = strs[0]
    if operation == 'DEPOSIT':
        name = strs[1]
        sum_ = int(strs[2])
        deposit(name, sum_)
    elif operation == 'WITHDRAW':
        name = strs[1]
        sum_ = int(strs[2])
        withdraw(name, sum_)
    elif operation == 'BALANCE':
        name = strs[1]
        print(balance(name))
    elif operation == 'TRANSFER':
        name1 = strs[1]
        name2 = strs[2]
        sum_ = int(strs[3])
        transfer(name1, name2, sum_)
    elif operation == 'INCOME':
        p = int(strs[1])
        income(p)
strs = input()
