>>> from pyatmos import download_sw_nrlmsise00,read_sw_nrlmsise00
>>> # Download or update the space weather file from www.celestrak.com
>>> swfile = download_sw_nrlmsise00() 
>>> # Read the space weather data
>>> swdata = read_sw_nrlmsise00(swfile) 