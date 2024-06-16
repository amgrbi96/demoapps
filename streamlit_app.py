import streamlit as st
import yfinance as yf
import pandas as pd

# Function to fetch and process intraday data
def get_intraday_data(ticker, period='30d', interval='15m'):
    # Download historical data
    try:
        data = yf.download(ticker, period=period, interval=interval)
    except Exception as e:
        st.error(f"Error fetching data for {ticker}: {e}")
        return None

    # Ensure we have data
    if data.empty:
        return None

    # Reset index to move the datetime index into a column
    data.reset_index(inplace=True)

    # Check if 'Datetime' column exists and is properly formatted
    if 'Datetime' in data.columns:
        data['Datetime'] = pd.to_datetime(data['Datetime'])
    elif 'date' in data.columns:  # Sometimes it can be lowercase 'date'
        data['Datetime'] = pd.to_datetime(data['date'])
    else:
        st.error(f"No 'Datetime' column found in data for {ticker}")
        return None

    # Extract the date and time from the datetime index
    data['Date'] = data['Datetime'].dt.date
    data['Time'] = data['Datetime'].dt.time

    # Pivot the table to get closing prices for each 15-minute interval
    pivot_df = data.pivot(index='Date', columns='Time', values='Close')

    return pivot_df

# List of companies (tickers) to display
tickers =[
    "1010.SR",
    "1020.SR",
    "1030.SR",
    "1050.SR",
    "1060.SR",
    "1080.SR",
    "1111.SR",
    "1120.SR",
    "1140.SR",
    "1150.SR",
    "1180.SR",
    "1182.SR",
    "1183.SR",
    "1201.SR",
    "1202.SR",
    "1210.SR",
    "1211.SR",
    "1212.SR",
    "1213.SR",
    "1214.SR",
    "1301.SR",
    "1302.SR",
    "1303.SR",
    "1304.SR",
    "1320.SR",
    "1320.SR",
    "1321.SR",
    "1322.SR",
    "1810.SR",
    "1820.SR",
    "1830.SR",
    "1831.SR",
    "1832.SR",
    "1833.SR",
    "2001.SR",
    "2010.SR",
    "2020.SR",
    "2020.SR",
    "2030.SR",
    "2040.SR",
    "2050.SR",
    "2060.SR",
    "2070.SR",
    "2080.SR",
    "2081.SR",
    "2082.SR",
    "2083.SR",
    "2090.SR",
    "2100.SR",
    "2110.SR",
    "2120.SR",
    "2130.SR",
    "2140.SR",
    "2150.SR",
    "2160.SR",
    "2170.SR",
    "2180.SR",
    "2190.SR",
    "2200.SR",
    "2210.SR",
    "2220.SR",
    "2222.SR",
    "2223.SR",
    "2230.SR",
    "2240.SR",
    "2250.SR",
    "2270.SR",
    "2280.SR",
    "2281.SR",
    "2282.SR",
    "2283.SR",
    "2290.SR",
    "2300.SR",
    "2310.SR",
    "2320.SR",
    "2330.SR",
    "2340.SR",
    "2350.SR",
    "2360.SR",
    "2370.SR",
    "2380.SR",
    "2381.SR",
    "2382.SR",
    "3001.SR",
    "3002.SR",
    "3003.SR",
    "3004.SR",
    "3005.SR",
    "3007.SR",
    "3008.SR",
    "3010.SR",
    "3020.SR",
    "3030.SR",
    "3040.SR",
    "3050.SR",
    "3060.SR",
    "3080.SR",
    "3090.SR",
    "3091.SR",
    "4001.SR",
    "4002.SR",
    "4003.SR",
    "4004.SR",
    "4005.SR",
    "4006.SR",
    "4007.SR",
    "4008.SR",
    "4009.SR",
    "4010.SR",
    "4011.SR",
    "4012.SR",
    "4013.SR",
    "4014.SR",
    "4015.SR",
    "4020.SR",
    "4030.SR",
    "4031.SR",
    "4040.SR",
    "4050.SR",
    "4051.SR",
    "4061.SR",
    "4070.SR",
    "4071.SR",
    "4080.SR",
    "4081.SR",
    "4082.SR",
    "4090.SR",
    "4100.SR",
    "4110.SR",
    "4130.SR",
    "4140.SR",
    "4141.SR",
    "4142.SR",
    "4150.SR",
    "4160.SR",
    "4161.SR",
    "4162.SR",
    "4163.SR",
    "4164.SR",
    "4170.SR",
    "4180.SR",
    "4190.SR",
    "4191.SR",
    "4192.SR",
    "4200.SR",
    "4210.SR",
    "4220.SR",
    "4230.SR",
    "4240.SR",
    "4250.SR",
    "4260.SR",
    "4261.SR",
    "4262.SR",
    "4270.SR",
    "4280.SR",
    "4290.SR",
    "4291.SR",
    "4292.SR",
    "4300.SR",
    "4310.SR",
    "4320.SR",
    "4321.SR",
    "4322.SR",
    "4323.SR",
    "4330.SR",
    "4331.SR",
    "4332.SR",
    "4333.SR",
    "4334.SR",
    "4335.SR",
    "4336.SR",
    "4337.SR",
    "4338.SR",
    "4338.SR",
    "4339.SR",
    "4340.SR",
    "4342.SR",
    "4344.SR",
    "4345.SR",
    "4346.SR",
    "4347.SR",
    "4348.SR",
    "4349.SR",
    "4700.SR",
    "4701.SR",
    "5110.SR",
    "6001.SR",
    "6002.SR",
    "6004.SR",
    "6010.SR",
    "6012.SR",
    "6013.SR",
    "6014.SR",
    "6015.SR",
    "6020.SR",
    "6040.SR",
    "6050.SR",
    "6060.SR",
    "6070.SR",
    "6090.SR",
    "7010.SR",
    "7020.SR",
    "7030.SR",
    "7040.SR"]  # Replace with your desired tickers

# Streamlit app
st.title('Intraday Price Data')

# Create tabs for each company
tab_names = [ticker for ticker in tickers]
tabs = st.tabs(tab_names)

# Loop through the tickers and fetch the data for each
for i, ticker in enumerate(tickers):
    with tabs[i]:
        st.header(f'{ticker} - 15-Minute Interval Closing Prices')
        
        # Fetch and process the data
        df = get_intraday_data(ticker)
        
        # Display the data in a table
        if df is not None:
            st.dataframe(df)
        else:
            st.write(f'No data available for {ticker}')

# To run the Streamlit app, save this script as `app.py` and execute the following command in your terminal:
# streamlit run app.py

