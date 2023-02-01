class BME280:
    '''Class to mock temp sensor'''
    def __init__(self):
        '''Constructor for mock'''

    def get_temperature(self):
        '''Temp'''
        return 20.0

    def get_humidity(self):
        '''Humidity'''
        return 20.0