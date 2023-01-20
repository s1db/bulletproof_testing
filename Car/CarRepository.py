

class CarRepository:

    def __init__(self, db_connection) -> None:
        self.db_connection = db_connection
        self.cars = {
            'Ford': ['Mustang', 'Fiesta', 'Focus'],
            'BMW': ['M3', 'X5', 'iX'],
            'Honda': ['Civic', 'Jazz', 'E'],
        }
            
    def find_all_cars(self, manufacturer):
        if self.db_connection == True:
            return self.cars[manufacturer]
        else:
            raise Exception('Database connection lost!')