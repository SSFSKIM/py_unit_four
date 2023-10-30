#Steve
#10.26


def get_cost(age, county):
    '''
    get age and county as input, output the discounted price based on information
    every percentage discount is discount from basic price only when it is said that
    'discount from basic price' in the instruction. Thus, all the other percentage discount
    is based on current ticket price
    :return:
    '''
    ticket = 70
    if county == 'Montgomery':
        ticket = 60
    if age < 5:
        ticket = 0
    if age > 65:
        ticket = ticket/2
        if county == 'Prince George':
            ticket = 0.925*ticket
    if county == 'Howard' and age < 14:
        ticket = 70*0.82
    if age < 0:
        return -1
    return ticket
def main():
    '''
    made it keep go using while loop
    if age is not valid, it asks again, and for valid age, it gives cost
    :return:
    '''
    while True:
        age = int(input('what is your age'))
        if age < 0:
            print('invalid age, input age that is not negative')
        else:
            county = input('what county do you live(discount for Montgomery, Prince George, Howard)')
            print(f'the cost of your ticket is ${get_cost(age, county)}')


if __name__ == '__main__':
    main()
