from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

fs = FlightSearch()
dm = DataManager()
data = fs.iata("Paris")
nm = NotificationManager()
rows = dm.get_rows().json()


def update_iata():
    for i in range(9):
        city = rows['sheet1'][i]['city']
        iata = fs.iata(city)
        id = rows['sheet1'][i]['id']
        params = {
            "sheet1": {
                "iataCode": iata
            }
        }
        dm.edit_row(id, params)


def search_lowest_prices():
    for i in range(9):
        msg = ''
        iata = rows['sheet1'][i]['iataCode']
        current_lowest_price = rows['sheet1'][i]['lowestPrice']
        id = rows['sheet1'][i]['id']
        flight_info = fs.price(iata)
        try:
            price = flight_info['price']
        except TypeError:
            price = "None"

        params = {
            "sheet1": {
                "lowestPrice": price
            }
        }
        if str(price) != 'None' and (str(current_lowest_price) == 'None' or int(current_lowest_price) >= int(price)):
            dm.edit_row(id, params)
            msg = f"""
Only ${flight_info['price']} to fly 
from {flight_info['origin_city']}-{flight_info['origin_airport']} to {flight_info['destination_city']}-{flight_info['destination_airport']},
from {flight_info['out_date']} to {flight_info['return_date']}         
"""
            print(f'New Low for {iata}')
            nm.send_msg(msg)
            return


search_lowest_prices()
