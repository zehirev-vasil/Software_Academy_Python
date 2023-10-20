client_db = {
    'A': [111, 100],
    'B': [222, 200],
    'C': [333, 300],
    'D': [444, 400],
    'E': [555, 500]
}

client_name = input('Enter your name: ')

if client_name in client_db:

    pin_verification_trials = 3

    for i in range(pin_verification_trials):

        pin = int(input('Please enter your PIN: '))

        if pin == client_db[client_name][0]:

            print(f'Your BALANCE IS: {client_db[client_name][1]}')

            operation = input('Please choose an operation WITHDRAW, DEPOSIT: ')

            if operation == 'WITHDRAW':

                for x in range(2):
                    amount = int(input('Please enter the amount to withdraw: ')) * -1
                    if amount <= client_db[client_name][1]:
                        client_db[client_name][1] += amount
                        break
                    else:
                        print('Please try again with smaller amount!')
                        continue
                print(f'Your balance is: {client_db[client_name][1]}')
                exit(0)

            elif operation == 'DEPOSIT':

                amount = int(input('Please enter the amount to deposit: '))
                client_db[client_name][1] += amount
                print(f'Your new balance is: {client_db[client_name][1]}')
                exit(0)

            else:

                print(f'your balance is: {client_db[client_name][1]}')

        else:

            pin_verification_trials -= 1
            print(f'Please note that you still have {pin_verification_trials} trials!')


else:
    print('No such customer, have a nice day!!!')
    exit(0)
