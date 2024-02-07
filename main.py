import streamlit as st
from streamlit_option_menu import option_menu
import account, dashboard, crop_yield, about

st.set_page_config(
    page_title="Crop Yield Prediction",
    page_icon="https://pnglib.nyc3.cdn.digitaloceanspaces.com/uploads/2021/02/health-wellness-yoga-icon-png_602061c6507a2.png",
    layout="wide"
)

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

class MultiApp:

    def __init__(self):
        self.apps = []
        self.default_app = 'Account'  # Set 'Yield Prediction' as the default app

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='Menu',
                options=['Account', 'Yield Prediction', 'About Us', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                menu_icon='list',
                icons=['person-circle', 'bar-chart-line', 'question-circle-fill', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                default_index=self.apps.index(next(app for app in self.apps if app['title'] == self.default_app)),
                styles={
                    "container": {"padding": "5!important", "background-color": '#107a37'},
                    "icon": {"color": "black", "font-size": "23px"},
                    "nav-link": {"color": "black", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "#0f572a"},
                    "nav-link-selected": {"background-color": "#0f572a"},
                }
            )

        for app_data in self.apps:
            if app_data['title'] == app:
                app_data['function']()

# Create an instance of MultiApp
multi_app = MultiApp()

# Add apps in the desired order
multi_app.add_app('Account', account.main)
#multi_app.add_app('Dashboard', dashboard.main)
multi_app.add_app('Yield Prediction', crop_yield.main)
multi_app.add_app('About Us', about.main)

# Run the selected app
multi_app.run()
