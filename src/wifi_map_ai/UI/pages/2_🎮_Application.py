import streamlit as st
import time

def main():
    house_icon = "Streamlit_Images\\house_icon.png"
    st.set_page_config(page_title="WiFi Planner", page_icon=house_icon, layout="wide")
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

    st.title("Application")

    st.subheader("Click on the floorplan and wait for prediction")
    st.text("")
    st.text("")
    left, right = st.columns(2)

    with left:
        st.image("Streamlit_Images\\house_installation_cut_rotated.png")
        # clicked = clickable_images(
        #     ["Streamlit_Images\\house_installation_cut_rotated.png",],
        #     titles=["Floorplan"],
        #     img_style={"margin": "5px", "height": "200px"},
        # )
    with right:
        time.sleep(5)
        st.image("Streamlit_Images\\test_prediction.png")
        st.text("")
        st.text("")


if __name__ == "__main__":
    main()