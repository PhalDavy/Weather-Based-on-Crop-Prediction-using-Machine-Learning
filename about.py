import streamlit as st

def main():
    st.title("About Us")
    col1, col2 = st.columns([2, 2])

    with col1:
        col4, col5 = st.columns([4, 1])
        with col4:
            st.write(" ")
            st.write(" ")
            st.write(" ")
            # st.write(" ")
            # st.write(" ")
            # st.write(" ")
            about_text = """
            <div style="font-size: 20px; line-height: 1.6; text-align: left;">
                In our farm management and yield prediction dashboard, we are dedicated to revolutionizing agricultural practices 
                by providing a comprehensive and user-friendly platform. Our mission is to empower farmers with valuable insights, 
                fostering informed decision-making for optimal crop yields. With cutting-edge technology and data-driven analytics, 
                we aim to streamline farm management processes, from crop planning to harvest, ensuring efficiency and sustainability.
            </div>
            """

            st.markdown(about_text, unsafe_allow_html=True)

            st.write(" ")
            about_text2 = """
            <div style="font-size: 20px; line-height: 1.6; text-align: left;">
                Join us on this journey towards smarter farming and sustainable yields. Together, let's cultivate a 
                future where is not only a way of life but a thriving and technologically advanced industry.
            </div>
            """

            st.markdown(about_text2, unsafe_allow_html=True)

            st.write(" ")
            st.write(" ")

            # Contact information with logos and aligned text
            st.markdown(
                """
                <div style="display: flex; align-items: center;">
                    <img src="https://assets.stickpng.com/images/58485698e0bb315b0f7675a8.png" alt="logo" style="width: 30px; margin-right: 15px;">
                    <h3 style="font-family: 'Arial Black', Arial, sans-serif; margin-top: 0; font-size: 20px;">info@example.com</h3>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <div style="display: flex; align-items: center;">
                    <img src="https://thumb.ac-illust.com/94/94a938537d9d8075525510281066f95d_t.jpeg" alt="logo" style="width: 30px; margin-right: 15px;">
                    <h3 style="font-family: 'Arial Black', Arial, sans-serif; margin-top: 0; font-size: 20px;">+123 456 7890</h3>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <div style="display: flex; align-items: center;">
                    <img src="https://t1.gstatic.com/images?q=tbn:ANd9GcSngapbWw4BBXdJZ2k9I14-pKQU88nlFBis-fLlaEHv0Ai2jplE" alt="logo" style="width: 30px; margin-right: 15px;">
                    <h3 style="font-family: 'Arial Black', Arial, sans-serif; margin-top: 0; font-size: 20px;">@example_twitter</h3>
                </div>
                """,
                unsafe_allow_html=True
            )


        with col5:
            st.write(" ")

    with col2:
        st.image("https://img.freepik.com/free-vector/about-us-concept-illustration_114360-639.jpg")

if __name__ == "__main__":
    main()