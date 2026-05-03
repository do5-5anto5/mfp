fruitsBasket = ['apple', 'orange', 'watermelon', 'strawberry', 'grape', 'kiwi', 'banana']

# forcing the loop stops with break, canceling actions from this loop before it
for fruit in fruitsBasket:
    if fruit != 'strawberry':
        print(f'{fruit} is not a straberry...')
    elif fruit == 'strawberry':
        print('strawberry found! yum!!!')
        break
    

subscribers = { 
    'Kayla': True,
    'Bea': False,
    'Math': True,
    'Dann': False,
}

# using continue, go for next item iteration, canceling code below excution
for person, whantsEmail in subscribers.items():
    if not whantsEmail:
        continue
    else:
        print(f'Sending email to subscriber {person}')
