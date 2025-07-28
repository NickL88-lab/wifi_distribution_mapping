import streamlit as st
from PIL import Image
import os.path
main_path = os.path.dirname(os.path.realpath(__file__))

#from streamlit_option_menu import option_menu

def main():

    house_icon = os.path.join(main_path, "Streamlit_Images", "house_icon.png")
    icon = Image.open(house_icon)
    st.set_page_config(page_title="WiFi Planner", page_icon=icon, layout="wide")

    # Imposta lo stile dell'interfaccia utente
    set_interface_style()

    # ---- HEADER SECTION ----
    with st.container():
        left_column_1, right_column_1 = st.columns(2)

        with left_column_1:
            st.write(" ")
            st.write(" ")
            st.subheader("Hey,  Welcome to ")
            st.write(" ")
            st.title("WiFi Planner")
            st.write(" ")
            st.write(" ")
            st.write(
                "This app utilizes artificial intelligence to predict the distribution of electromagnetic field emitted by a WiFi router within an apartment. "
                "In the modern world where users are increasingly making their homes smarter, it's crucial to start with an optimal distribution of the WiFi signal to enable interaction among various smart home sensors. "
                "It's possible to evaluate multiple installation points for the WiFi antenna to achieve the desired field distribution.")

            st.write("This app serves an educational purpose and is a basic example for students approaching the study of indoor electromagnetic propagation. "
                     "The model has been trained on synthetic data generated from simulations conducted with Ansys HFSS, the gold standard of electromagnetic simulation.")


        with right_column_1:
            house_image = os.path.join(main_path, "Streamlit_Images", "Untitled.png")
            image = Image.open(house_image)

            st.image(image, use_column_width=True)


    st.write("\n\n\n")

    # Add button
    start_button = st.button("Let's Start!")
    if start_button:
        # Reindirizza a una nuova pagina o sezione
        st.switch_page("pages/2_🎮_Application.py")

def set_interface_style():
    # Imposta lo stile dell'interfaccia utente
    st.markdown(
        """
        <style>
        .css-1aumxhk {
            color: blue;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #0e2443;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
