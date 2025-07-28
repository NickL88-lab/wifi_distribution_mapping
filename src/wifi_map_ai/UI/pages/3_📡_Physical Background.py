import streamlit as st
import base64
import os.path
from PIL import Image

main_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"..")

house_icon = os.path.join(main_path, "Streamlit_Images", "house_icon.png")
icon = Image.open(house_icon)
st.set_page_config(page_title="WiFi Planner", page_icon=icon, layout="wide")
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

# ---- HEADER SECTION ----
with st.container():
    # left_column_1, right_column_1 = st.columns(2)
    # with left_column_1:
    st.write(" ")
    st.write(" ")
    st.title("Physical Background")
    st.write(" ")
    st.subheader("Introduction to Indoor Electromagnetic Propagation")
    st.write(
        "Indoor electromagnetic propagation is a field of study that examines the behavior of electromagnetic waves within enclosed spaces such as buildings, apartments, and other structures."
        "This area of research is fundamental for understanding wireless communication systems like WiFi, which rely on the transmission and reception of electromagnetic signals.")
    st.write("At the core of electromagnetic propagation lies Maxwell's equations, a set of four fundamental equations that describe the behavior of electric and magnetic fields in space and time. ")
    st.write("These equations govern how electromagnetic waves propagate through different mediums, including air, walls, and other obstacles present in indoor environments. "
             "Understanding the physical principles described by Maxwell's equations is essential for analyzing and optimizing wireless communication systems within indoor spaces.")
    st.write(" ")
    st.subheader("Factors Influencing Indoor Propagation")
    st.write("Indoor electromagnetic propagation is influenced by various factors, each of which plays a significant role in shaping the behavior of electromagnetic waves within confined spaces. As a master's student in telecommunications engineering, it's crucial to grasp the intricate interplay between these factors to design and optimize wireless communication systems effectively.")
    st.write("One of the primary factors affecting indoor propagation is the composition and structure of building materials. Different materials, such as concrete, brick, glass, and wood, exhibit varying levels of attenuation and reflection properties, impacting the propagation of electromagnetic waves. For instance, materials with high conductivity, such as metal, can cause significant signal attenuation and reflection, leading to signal degradation and shadowing effects within buildings.")
    st.write("Moreover, the layout and geometry of indoor environments contribute to the complexity of electromagnetic propagation. The presence of walls, partitions, doors, and furniture can introduce obstacles that obstruct or diffract electromagnetic waves, leading to multipath propagation phenomena. Understanding how these obstacles interact with electromagnetic waves is crucial for predicting signal coverage and quality within indoor spaces.")
    st.write("Furthermore, the frequency of the electromagnetic waves used for communication plays a crucial role in indoor propagation characteristics. Higher frequency signals experience more significant attenuation and are more susceptible to blockage by obstacles compared to lower frequency signals. Therefore, selecting an appropriate frequency band is essential for achieving reliable and robust indoor wireless communication.")
    st.write("Overall, mastering the understanding of these factors influencing indoor electromagnetic propagation is essential for designing efficient and resilient wireless communication systems for indoor environments. By considering the complex interplay between building materials, layout, environmental conditions, and frequency characteristics, telecommunications engineers can optimize signal coverage, minimize interference, and enhance the performance of indoor wireless networks.")
    st.write(" ")
    st.subheader("Multipath Propagation")
    st.write("Multipath propagation is a phenomenon commonly observed in indoor environments, where electromagnetic waves take multiple paths to reach a receiver due to reflections, diffractions, and scattering. Understanding multipath propagation is crucial for designing robust wireless communication systems capable of mitigating its effects.")
    st.write("Reflections occur when electromagnetic waves encounter surfaces such as walls, floors, and ceilings, causing them to bounce off and propagate in different directions. These reflected waves can interfere with the direct path signal, resulting in constructive or destructive interference depending on their phase relationship. In severe cases, strong reflections can lead to signal fading, where signal strength fluctuates rapidly due to interference patterns.")
    st.write("Diffraction occurs when electromagnetic waves encounter sharp edges or corners, causing them to bend around obstacles and propagate into regions that would otherwise be shadowed. Diffraction effects are particularly pronounced in indoor environments with complex layouts and irregular structures. Understanding diffraction phenomena is essential for predicting signal coverage and ensuring reliable communication in obstructed areas.")
    st.write("Scattering occurs when electromagnetic waves interact with small objects or irregularities in the propagation medium, causing them to scatter in various directions. Scattering can lead to multipath propagation by introducing additional signal paths with different propagation delays and attenuations. As a telecommunications engineer, it's crucial to model and characterize scattering phenomena to assess their impact on signal quality and reliability.")
    st.write("In summary, multipath propagation is a complex phenomenon that significantly impacts the performance of wireless communication systems in indoor environments.")
    st.write("")
    st.subheader("Simulation and Modeling Techniques")
    left,right = st.columns(2)
    with right:
        file_path = os.path.join(main_path, "Streamlit_Images", "House_cut.gif")
        file_ = open(file_path, "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
            unsafe_allow_html=True
        )
    with left:
        st.write(
            "One of the key challenges in indoor electromagnetic propagation is the complexity of the propagation environment, which often involves intricate geometries, multiple reflecting surfaces, and varying material properties. Traditional full-wave electromagnetic simulators, while accurate, may struggle to handle the computational demands of simulating such complex scenarios, especially for large-scale indoor environments.")
        st.write(
            "n this context, asymptotic solvers such as Ansys HFSS SBR+ (Shooting and Bouncing Rays Plus) offer significant advantages for telecommunications engineers. HFSS SBR+ employs asymptotic methods to efficiently model electromagnetic wave propagation in complex environments by tracing rays and accounting for specular and diffuse reflections, diffraction, and scattering phenomena.")
        st.write(
            "One of the key strengths of HFSS SBR+ is its ability to accurately predict the propagation characteristics of electromagnetic waves in indoor environments with minimal computational resources. By leveraging asymptotic techniques, HFSS SBR+ can rapidly analyze large-scale scenarios with high accuracy, making it an invaluable tool for telecommunications engineers tasked with designing wireless communication systems for indoor applications.")
        st.write("")
        st.write("Furthermore, HFSS SBR+ provides comprehensive post-processing tools for analyzing simulation results, allowing engineers to visualize signal propagation patterns, identify areas of signal degradation or interference, and optimize antenna placement and configuration to improve wireless network performance.")
        st.write("In conclusion, mastering simulation and modeling techniques, especially asymptotic solvers like Ansys HFSS SBR+, is essential for telecommunications engineering master's students specializing in indoor electromagnetic propagation. By leveraging the capabilities of HFSS SBR+ to efficiently model and analyze complex indoor environments, students can gain valuable insights into the behavior of wireless communication systems and develop innovative solutions to address the challenges of indoor wireless connectivity.")
        st.write("")
    st.subheader("Applications in Smart Homes and IoT")
    st.write("In smart homes, wireless communication technologies such as WiFi, Bluetooth, Zigbee, and Z-Wave rely on indoor electromagnetic propagation to facilitate communication between various smart devices, sensors, and actuators distributed throughout the living space. By leveraging indoor propagation characteristics, smart home systems can enable remote monitoring and control of devices, automate routine tasks, and enhance comfort, convenience, and security for occupants.")
    st.write("For example, indoor propagation modeling can help optimize the placement of WiFi access points, Bluetooth beacons, and Zigbee hubs to ensure comprehensive coverage and reliable connectivity throughout the home. By analyzing signal propagation patterns and identifying areas of signal attenuation or interference, telecommunications engineers can design robust wireless networks capable of supporting a wide range of smart home applications, including smart lighting, HVAC control, home security, and entertainment systems.")
    st.write("In summary, indoor electromagnetic propagation plays a vital role in enabling the seamless integration of wireless communication technologies and IoT devices within smart homes. By leveraging indoor propagation modeling and analysis techniques, telecommunications engineers can design robust, scalable, and energy-efficient wireless networks capable of supporting a wide range of smart home applications and enhancing the overall quality of life for occupants.")
    st.write("")

    # with right_column_1:
    #     house_image = "Streamlit_Images\\router.png"
    #     st.image(house_image, use_column_width=True)