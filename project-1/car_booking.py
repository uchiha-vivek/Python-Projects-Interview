import logging
logging.basicConfig(
    filename='project-1\cars.log',
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
)

"""Prices are in USD"""
cars = {
    'Tesla':200,
    "Tata":150,
    'Mahindra':180,
    'Mercedez':150
}

print('Welcome to the showroom !')
print('Tesla: 200$\nTata: 150$\nMahindra: 180$\nMercedez: 150$')

total_price=0
car_item = input('Enter the name of the brand you want to book :')
if car_item in cars:
    total_price+=cars[car_item]
    logging.info(f"your car {car_item} has been booked")
    print(f'your car {car_item} has been booked')
else :
    logging.info(f"We dont have this car {car_item} in our case right now")
    print(f'We dont have this car {car_item} in our case right now')

another_car = input('Please book any other car if you want  ? (Yes/No)  ')
if another_car =='Yes':
    if another_car in cars:
        total_price+=cars[another_car]
        logging.info(f'{another_car} has been booked')
        print(f'{another_car} has been booked ! ')
    else:
        logging.info(f'{another_car} not available')
        print(f'{another_car} not available')

logging.info(f'Your total amount is : {total_price}')
print(f'The toal amount you have to pay is : {total_price}')