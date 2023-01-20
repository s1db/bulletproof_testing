import time

class CarApiClient:

    def __init__(self, api_key) -> None:
        self.connected(api_key = api_key)
    
    def connected(self, api_key):
        if api_key == 'adsf2354adf4Xadf':
            return True    
        else:
            raise Exception('Could not connect to external API')
        
    def manifacturer_is_not_bankrupt(self, manufacturer):
        time.sleep(5)
        
        if manufacturer in ['Ford', 'BMW', 'Honda']:
            return True
        
        if manufacturer == 'Tesla':
            return False
        
        raise Exception('Manufacturer not found')
