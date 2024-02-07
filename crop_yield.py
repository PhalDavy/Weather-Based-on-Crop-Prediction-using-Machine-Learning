import streamlit as st
import requests
import json

def main():

    # st.title("Crop Yiel Prediction")
    st.markdown(
        """
        <div style="display: flex; align-items: center;">
            <img src="https://static.vecteezy.com/system/resources/thumbnails/023/258/280/small/environment-protection-graphic-clipart-design-free-png.png" alt="logo" style="width: 90px; margin-right: 15px;">
            <h3 style="font-family: 'Arial Black', Arial, sans-serif; margin-top: 0; font-size: 50px;">Crop Yield Prediction</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(" ")
    st.write(" ")
    st.write(" ")

    col1, col2 = st.columns(2)

    with col1:
        with st.expander("State Name", expanded=True):

            state_name = st.selectbox("Choose the state name", [
                "Bihar",
                "Punjab",
                "Himachal Pradesh",
                "Kerala",
                "Odisha",
                "Andaman and Nicobar Islands",
                "Chhattisgarh",
                "Uttarakhand",
                "Jharkhand"
            ])
            if state_name == 'Bihar':
                state_name = 0
            elif state_name == 'Punjab':
                state_name = 1
            elif state_name == 'Himachal Pradesh':
                state_name = 2
            elif state_name == 'Kerala':
                state_name = 3
            elif state_name == 'Odisha':
                state_name = 4
            elif state_name == 'Andaman and Nicobar Islands':
                state_name = 5
            elif state_name == 'Chhattisgarh':
                state_name = 6
            elif state_name == 'Uttarakhand':
                state_name = 7
            else:
                state_name = 8

    with col2:
        with st.expander("Season", expanded=True):
            season = st.selectbox("Select the current season", [
                    "Autumn",
                    "Whole Year",
                    "Kharif",
                    "Winter",
                    "Summer",
                    "Rabi"
                ])
            if season == 'Autumn':
                season = 0
            elif season == 'Whole Year':
                season = 1
            elif season == 'Kharif':
                season = 2
            elif season == 'Winter':
                season = 3
            elif season == 'Summer':
                season = 4
            else:
                season = 5
    
    col3, col4 = st.columns(2)
    with col3:
        with st.expander("Area", expanded=True):
            area = st.number_input("Enter your farm area")
    with col4:
        with st.expander("Rainfall", expanded=True):
            rainfall = st.number_input("Enter the rainfall level that occur recently")

    col5, col6 = st.columns(2)
    with col5:
        with st.expander("Temperature", expanded=True):
            temperature = st.number_input("Enter the current temperature in your farm")
    with col6:
        with st.expander("Humidity", expanded=True):
            humidity = st.number_input("Enter the humidity in your farm")


    
    
    #store input value to pass to api
    input_data={
        "area": area,
        "rainfall": rainfall,
        "temperature": temperature,
        "humidity": humidity,
        "state_name": state_name,
        "season": season
    }
    # Custom CSS to increase the size and add color to the button
    button_style = """
        <style>
            .stButton button {
                width: 150px !important; /* Set your desired width */
                height: 50px !important; /* Set your desired height */
                background-color: #0f572a !important; /* Set your desired color */
                color: white !important; /* Set text color */
            }
            .stButton button span {
                font-size: 16px !important; /* Set font size */
            }
        </style>
    """

    # Apply the custom CSS
    st.markdown(button_style, unsafe_allow_html=True)
    crop = 0
    if st.button("Predict"):
        crop=requests.post(url=" http://127.0.0.1:8000/predict", data=json.dumps(input_data))
        crop=crop.json()
        c=crop['prediction']
        st.success(f'Based on the prediction, you can plant approximately {c:.2f} tons of crops.')     


if __name__=='__main__':
    main()
                   