# trying to make a multiplexer

class Cache:
    # decide on data structure
    
    def cache_data():
        # private function
        # device input --> can not send data periodically, just store

class Sensor_Device:
    # i2c
    # each i2c device has separate clock pin, but mux only connects to data pin
    float clock_rate_hz
    bool clock_rise_read
    # read means input, false = write means output
    bool mode_is_read
    int sclk_pin_num
    int sdata_pin_num
    # store current clock rise read
    bool is_clock_rise_read

    # mux will send commands to retrieve data

    # i2c sensor : 2 lines
    # SCLK connected separately to some other clock source
    # SDATA connected to mux
    def Sensor_Device():

        # do not need many getter and setter methods since configure at beginning
        # need methods to handle operations, like an API


    # there could be multiple values to cache related to the sensor, there may need to be processing
    def get_data(self, int register):
        # read data from register
        # check cache

    def write_data(self , int register, int data):
        # write data to a register
        # write to cache first


    def set_mode():
        # 

    def get_mode():
        # 

class Pin:

    def Pin():
        # constructor
        # do not think priority matters because look at combination of all 4 pins at a time
        bool mode_is_input
        Sensor_Device* 

class Mux:
    self.pin1_input
    self.pin2_input
    self.pin3_input
    self.pin4_input
    self.pin1_output
    self.pin2_output
    self.pin3_output
    self.pin4_output
    def Mux():
        # constructor
        

class HIL_Tests:
    def HIL_Tests():
        # constructor
