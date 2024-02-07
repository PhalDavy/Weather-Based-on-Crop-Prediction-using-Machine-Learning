import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import firestore
from dashboard import main as dashboard_main

cred=credentials.Certificate('ui/yield-prediction-3c179-fe5bbdf79172.json')
#firebase_admin.initialize_app(cred)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
# doc_ref = None


def main():

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
    

    def f():
        try:
            user = auth.get_user_by_email(email)

            st.session_state.username = user.uid
            st.session_state.useremail = user.email

            st.session_state.signedout = True
            st.session_state.signout = True
        except:
            st.warning('Login Failed')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False
        st.session_state.username = ''
    
    username = st.session_state.get('username', '')

    if 'signedout' not in st.session_state:
        st.session_state.signedout = False
    if 'signout' not in st.session_state:
        st.session_state.signout = False

    if not st.session_state['signedout']:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.write(' ')
            st.image("https://img.freepik.com/free-vector/computer-login-concept-illustration_114360-7892.jpg")
        with col2:
            col1, col2, col3 = st.columns([0.4, 2, 0.2])
            with col1:
                st.write(' ')
            with col2:
                st.write(' ')
                st.write(' ')
                st.write(' ')
                st.write(' ')
                st.title("Welcome to AGT Dashboard")
                st.write(' ')
                st.write(' ')
                
            with col3:
                st.write(' ')
                
            
            col4, col5, col6 = st.columns([1, 1.5, 1.5])
            with col4:
                st.write(' ')
            with col5:
                choice = st.selectbox(r"$\textsf{\large Login/Sign Up}$", ['Login', 'Sign Up'])
                st.write(' ')
            with col6:
                st.write(' ')


            if choice == 'Login':

                col1, col2, col3 = st.columns([1, 1.5, 1.5])
                with col1:
                    st.write(' ')
                with col2:
                    email=st.text_input(r"$\textsf{\large Email Address}$")
                    st.write(' ')
                    password=st.text_input(r"$\textsf{\large Password}$", type='password')
                    st.write(' ')

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

                    st.button('Login', on_click=f)
                with col3:
                    st.write(' ')


            else:
                col1, col2, col3, col4 = st.columns([0.8, 2.2, 2.2, 0.8])
                with col1:
                    st.write(' ')
                with col2:
                    st.write(' ')
                    email = st.text_input(r"$\textsf{\large Email Address}$")
                    st.write(' ')
                    password=st.text_input(r"$\textsf{\large Password}$", type='password')
                    st.write(' ')
                    username = st.text_input(r"$\textsf{\large Enter Your User Name}$")
                    st.write(' ')
                with col3:
                    st.write(' ')
                    state_name = st.text_input(r"$\textsf{\large State Name}$")
                    st.write(' ')
                    area = st.number_input(r"$\textsf{\large Area}$")
                    st.write(' ')
                    production = st.number_input(r"$\textsf{\large Enter Your Last Crop Production}$")
                    st.write(' ')


                with col4:
                    st.write(' ')

                col9, col10, col11 = st.columns([2, 1, 2])

                with col9:
                    st.write(" ")
                with col10:
                    st.write(" ")
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

                    if st.button('Create my account'):
                        user = auth.create_user(email=email, password=password, uid=username)
                        db = firestore.client()
                        user_data = {
                            'Name': username,
                            'State_Name': state_name,
                            'Area': area,
                            'Production': production
                        }
                        df = [user_data]
                        for dff in df:
                            doc_ref = db.collection(u'Users').document(dff['Name'])
                            doc_ref.set(dff)

                        st.session_state.username = username

                        st.success('Account Created Successfully!')
                        st.markdown('Please Login Using Your Email and Password')
                        st.balloons
                with col11:
                    st.write(" ")

    if st.session_state.signout:
        db = firestore.client()
        users_ref = db.collection(u'Users')
        docs = users_ref.where('Name', '==', st.session_state.username).stream()

        for doc in docs:
            data = doc.to_dict()
            Location = data.get('State_Name')
            area2 = data.get('Area')
            prod = data.get('Production')
        name = st.session_state.username

        dashboard_main(Location, area2, prod, name)
        button_style = """
            <style>
                .stButton button {
                    width: 120px !important; /* Set your desired width */
                    height: 30px !important; /* Set your desired height */
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
        st.button('Sign Out', on_click=t)
        #     st.title(f"Welcome to AGT Dashboard, {st.session_state.username}!")
        #     st.image("https://png.pngtree.com/png-clipart/20220719/original/pngtree-farming-man-with-cart-vector-png-image_8381878.png")
        #     st.button('Sign Out', on_click=t)
            
            






