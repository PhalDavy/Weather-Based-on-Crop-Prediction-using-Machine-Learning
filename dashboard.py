import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import requests
import random
import pandas as pd
import altair as alt

def main(Location, area2, prod, name):
    def get_weather_data(api_key, city_name, units):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city_name,
            "units": units,
            "appid": api_key
        }
        response = requests.get(base_url, params=params)
        data = response.json()
        return data

    def fetch_weather_data():
        api_key = "0cf12bb436cb1339b908188393f69676"
        city_name = Location
        units = 'metric'

        try:
            weather_data = get_weather_data(api_key, city_name, units)
            return weather_data
        except Exception as e:
            st.error(f"Error fetching weather data: {e}")
            return None
        
    
    def display_production_bar_graph(last_production):
        months = ['August-2023', 'September-2023', 'October-2023', 'November-2023', 'December-2023']
        random_values = [random.randint(1000, 6000) for _ in range(len(months) - 1)]
        data = list(zip(months[:-1], random_values))
        data.append(('January-2024', last_production))

        df = pd.DataFrame(data, columns=['Month', 'Production'])

        months_order = ['August-2023', 'September-2023', 'October-2023', 'November-2023', 'December-2023', 'January-2024']
        df['Month'] = pd.Categorical(df['Month'], categories=months_order, ordered=True)

        df = df.sort_values(by='Month')

        bars = alt.Chart(df).mark_bar(color='#d7fce5').encode(
            x='Month',
            y='Production'
        )

        text = bars.mark_text(
            align='center',
            baseline='bottom',
            dy=-10,  
            fontSize=13,  
            fontWeight='bold',  
        ).encode(
            text='Production:Q'  
        )

        chart = (bars + text).properties(
            width=alt.Step(50),  
            height=380  
        )
        st.altair_chart(chart, use_container_width=True)


    def display_weather_data(weather_data):

        if "main" in weather_data:
            box_color = "#d7fce5"  
            temp = weather_data["main"]["temp"]
            humidity = weather_data.get("main", {}).get("humidity", 0)
            cloud_coverage = weather_data.get("clouds", {}).get("all", 0)
            wind_speed = weather_data.get("wind", {}).get("speed", 0)
            pressure = weather_data.get("main", {}).get("pressure", 0)
            icon_url = f"http://openweathermap.org/img/w/{weather_data['weather'][0]['icon']}.png"
            weather_caption = weather_data['weather'][0]['description'].title()

            # Get today's date
            today_date = datetime.now().strftime("%Y-%m-%d")
            today_with_text = datetime.now().strftime("Today | %d %B %Y")

            st.markdown(
                f'<div style="background-color: {box_color}; padding: 12px; border-radius: 5px; width: 290px; display: flex; align-items: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">'
                f'<div>'
                f'<span style="color: black; font-size: 18px; font-weight: bold;">Weather</span><br>'
                f'<img src="{icon_url}" style="width: 120px; height: 120px; margin-right: 10px;">'
                f'<div>'
                f'<span style="color: black; font-size: 20px;">{today_with_text}</span><br>'
                f'<span style="color: black; font-size: 12px;">{weather_caption}</span>'
                f'</div>'
                f'</div>'
                f'</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div style="background-color: {box_color}; padding: 12px; border-radius: 5px; width: 290px; display: flex; align-items: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">'
                f'<div>'
                f'<span style="color: black; font-size: 17px;">🌡️ Temperature:    <strong>{round(temp)}°C</strong></span><br><br>'
                f'<span style="color: black; font-size: 17px;">💧 Humidity:       <strong>{humidity}%</strong></span><br><br>'
                f'<span style="color: black; font-size: 17px;">☁️ Clouds Coverage: <strong>{cloud_coverage}%</strong></span><br><br>'
                f'<span style="color: black; font-size: 17px;">💨 Wind Speed:      <strong>{wind_speed}m/s</strong></span><br><br>'
                f'<span style="color: black; font-size: 17px;">⏲️ Pressure:        <strong>{pressure}hPa</strong></span>'
                f'</div>'
                f'</div>'
                f'</div>',
                unsafe_allow_html=True
            )

            
        

        else:
            st.warning("No weather data available.")
    
    def table():
        st.title("Welcome to Your Farm Dashboard, " + name)
        st.write(" ")
        st.write(" ")
        col1, col2, col3, col4 = st.columns(4)

        box_color = "#d7fce5"

        with col1:
            st.markdown(
                f'<div style="background-color: {box_color}; padding: 15px; border-radius: 5px; width: 300px; display: flex; align-items: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">'
                f'<img src="https://cdn-icons-png.flaticon.com/512/898/898133.png" style="width: 60px; height: 60px; margin-right: 30px; margin-left: 10px;">'
                f'<div>'
                f'<span style="color: black; font-size: 19px; margin-right: 30px;">Crop Name</span><br>'
                f'<span style="color: black; font-weight: bold; font-size: 35px;">Rice</span>'
                f'</div>'
                f'</div>',
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                f'<div style="background-color: {box_color}; padding: 15px; border-radius: 5px; width: 300px; display: flex; align-items: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">'
                f'<img src="https://cdn.icon-icons.com/icons2/3760/PNG/512/house_building_home_icon_231000.png" style="width: 60px; height: 60px; margin-right: 30px; margin-left: 10px;">'
                f'<div>'
                f'<span style="color: black; font-size: 19px; margin-right: 30px;">City Name</span><br>'
                f'<span style="color: black; font-weight: bold; font-size: 35px;">{Location}</span>'
                f'</div>'
                f'</div>',
                unsafe_allow_html=True
            )


        with col3:
            area3 = int(area2)
            st.markdown(
                f'<div style="background-color: {box_color}; padding: 15px; border-radius: 5px; width: 300px; display: flex; align-items: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">'
                f'<img src="https://cdn-icons-png.flaticon.com/512/9098/9098519.png" style="width: 60px; height: 60px; margin-right: 30px; margin-left: 10px;">'
                f'<div>'
                f'<span style="color: black; font-size: 19px; margin-right: 30px;">Farm Area</span><br>'
                f'<span style="color: black; font-weight: bold; font-size: 35px;">{area3}</span>'
                f'</div>'
                f'</div>',
                unsafe_allow_html=True
            )

        with col4:
            prod1 = int(prod)
            st.markdown(
                f'<div style="background-color: {box_color}; padding: 15px; border-radius: 5px; width: 300px; display: flex; align-items: center; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);">'
                f'<img src="https://cdn3.iconfinder.com/data/icons/farm-and-nature/512/Farm_wheat_bag-512.png" style="width: 60px; height: 60px; margin-right: 30px; margin-left: 10px;">'
                f'<div>'
                f'<span style="color: black; font-size: 19px; margin-right: 25px;">Last Production</span><br>'
                f'<span style="color: black; font-weight: bold; font-size: 35px;">{prod1}</span>'
                f'</div>'
                f'</div>',
                unsafe_allow_html=True
            )

        st.write(" ")
        st.write(" ")

        col5, col6 = st.columns([0.8, 2.6])
        with col5:
            weather_data = fetch_weather_data()

            if weather_data:
                display_weather_data(weather_data)

        with col6:
            st.write(" ")
            col20, col21, col22 = st.columns([0.1,5,0.35])
            with col20:
                st.write(" ")
            with col21:
                with st.expander("Production Details", expanded=True):
                    st.write(" ")
                    st.write(" ")
                    display_production_bar_graph(prod)
            with col22:
                st.write(" ")


    table()

    
    
        
if __name__=='__main__':
    main()