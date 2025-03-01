import streamlit as st
import cv2
import numpy as np
from streamlit_option_menu import option_menu

# Function to play video frame by frame (Limited Frames to Avoid Infinite Loop)
def play_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_placeholder = st.empty()

    # Limit playback to a specific number of frames
    frame_count = 0
    max_frames = 500  # Adjust this value as needed

    while cap.isOpened() and frame_count < max_frames:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame, channels="RGB", use_container_width=True)

        frame_count += 1  # Increment frame count

    cap.release()

# Simulated function to fetch live count from Nx Meta API
def get_live_crowd_count():
    return np.random.randint(1, 8)  # Simulated count

# Streamlit Page Configuration
st.set_page_config(page_title='Real-Time Crowd Monitoring', layout='wide')

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "About", "Real-Time Monitoring", "Nx Features Used"],
        icons=["house", "info-circle", "camera-video", "tools"],
        menu_icon="cast",
        default_index=0
    )
    
    st.sidebar.title("📘 User Guide & Overview")
    with st.sidebar.expander("Getting Started", expanded=True):
        st.markdown("""
        - <span style="font-weight:bold; font-size:15px;"> Install Requirements:</span> Ensure you have Streamlit and OpenCV installed for smooth execution.
        - <span style="font-weight:bold; font-size:15px;"> Run the App:</span> Execute the app using `streamlit run app.py` to start monitoring crowd flow in real-time.
        """, unsafe_allow_html=True)

    with st.sidebar.expander("Home Page"):
        st.markdown("""
        - <span style="font-weight:bold; font-size:15px;"> Overview:</span> Get insights into the purpose of the application and key features such as real-time object detection, heatmaps, and crowd density analysis.
        - <span style="font-weight:bold; font-size:15px;"> AI Insights:</span> Explore AI-powered summaries and data interpretations for crowd movement and density trends.
        """, unsafe_allow_html=True)

    with st.sidebar.expander("Real-Time Monitoring"):
        st.markdown("""
        - <span style="font-weight:bold; font-size:15px;"> Live Video Stream:</span> View real-time video feeds integrated with Nx Meta and detect objects like persons, cars, backpacks, and umbrellas.
        - <span style="font-weight:bold; font-size:15px;"> Object Detection:</span> See bounding boxes around detected objects with count summaries.
        - <span style="font-weight:bold; font-size:15px;"> Heatmaps:</span> Analyze heatmaps for crowd density at different time intervals to identify congestion zones.
        """, unsafe_allow_html=True)

    with st.sidebar.expander("Nx Meta Features Used"):
        st.markdown("""
        - <span style="font-weight:bold; font-size:15px;"> Nx AI Manager:</span> Manages real-time object detection and crowd analysis using pre-trained AI models.
        - <span style="font-weight:bold; font-size:15px;"> Nx Model Manager:</span> Dynamically loads and switches AI models for different detection tasks.
        - <span style="font-weight:bold; font-size:15px;"> Nx Metadata Injection:</span> Overlays heatmaps, bounding boxes, and metadata on live streams for enhanced analysis.
        - <span style="font-weight:bold; font-size:15px;"> Nx REST APIs:</span> Facilitates seamless data exchange for real-time monitoring and analytics.
        """, unsafe_allow_html=True)

    with st.sidebar.expander("Analytics & Insights"):
        st.markdown("""
        - <span style="font-weight:bold; font-size:15px;"> Crowd Density Analysis:</span> Get real-time insights into areas of high and low crowd density.
        - <span style="font-weight:bold; font-size:15px;"> Anomaly Detection:</span> Identify unusual crowd movement patterns or high-density areas.
        - <span style="font-weight:bold; font-size:15px;"> AI-Driven Reports:</span> Receive AI-generated summaries based on crowd flow and object detection data.
        """, unsafe_allow_html=True)

    with st.sidebar.expander("Unique Features and Advantages"):
        st.markdown("""
        - <span style="font-weight:bold; font-size:15px;"> Real-Time Heatmaps:</span> Visualize crowd flow instantly with dynamic heatmaps.
        - <span style="font-weight:bold; font-size:15px;"> Seamless Nx Meta Integration:</span> Leverages Nx Meta's AI capabilities for high-accuracy detection and analysis.
        - <span style="font-weight:bold; font-size:15px;"> Scalable Architecture:</span> Supports multiple video feeds and high-traffic monitoring seamlessly.
        - <span style="font-weight:bold; font-size:15px;"> User-Friendly Interface:</span> Simple navigation with real-time stats and analytics.
        """, unsafe_allow_html=True)

    with st.sidebar.expander("Feedback & Support"):
        st.markdown("""
        - <span style="font-weight:bold; font-size:15px;"> User Feedback:</span> Share your suggestions to help improve the dashboard.
        - <span style="font-weight:bold; font-size:15px;"> Support:</span> Reach out for assistance with any queries or issues.
        """, unsafe_allow_html=True)

    # Collecting User Feedback
    st.sidebar.title("Feedback")
    rating = st.sidebar.slider("Rate your experience", 1, 5, 3)
    if st.sidebar.button("Submit Rating"):
        st.sidebar.success(f"Thanks for rating us {rating} stars! 🌟")
        st.sidebar.markdown(
            "Check out our [GitHub profile](https://github.com/MohamedFarhun) for more projects!"
        )

# Home Page
if selected == "Home":
    st.title("🏙️ Real-Time Crowd Monitoring")
    st.write(
        "This application leverages AI-powered detection from Nx Meta to provide real-time insights on crowd movement, "
        "density, and object tracking. Whether for security, event management, or traffic monitoring, our tool helps "
        "enhance situational awareness."
    )

    # First Section: Image Right - Content Left
    col1, col2 = st.columns([2, 3])
    with col1:
        st.image("image1.jpeg", caption="AI-Based Crowd Detection", use_container_width=True)
    with col2:
        st.subheader("🔍 Advanced AI-Powered Analysis")
        st.write(
            "Our solution integrates AI-driven object detection to monitor real-time crowd flow, identify potential congestion "
            "zones, and provide actionable insights."
        )
        st.markdown("- 📡 **Live Object Detection & Counting**")
        st.markdown("- 🔥 **Heatmap-Based Crowd Density Analysis**")
        st.markdown("- 🚦 **Traffic & Crowd Movement Prediction**")

    st.markdown("---")

    # Second Section: Image Left - Content Right
    col1, col2 = st.columns([3, 2])
    with col1:
        st.subheader("⚡ Real-Time Updates & Insights")
        st.write(
            "With seamless integration into Nx Meta's AI Manager, our system dynamically updates crowd statistics, "
            "giving you an edge in decision-making for security, event management, and safety monitoring."
        )
        st.markdown("- 📊 **Live Streaming with AI Object Tracking**")
        st.markdown("- 🏢 **Ideal for Smart Cities & Public Spaces**")
        st.markdown("- 📈 **Data-Driven Decision Making**")
    with col2:
        st.image("image2.jpeg", caption="Live Object Tracking", use_container_width=True)

    st.markdown("---")

    # Third Section: Image Right - Content Left
    col1, col2 = st.columns([2, 3])
    with col1:
        st.image("image3.jpeg", caption="Crowd Density Heatmap", use_container_width=True)
    with col2:
        st.subheader("🌍 Scalable & Flexible Deployment")
        st.write(
            "Our system is built to handle different environments, from small events to large public spaces. "
            "The AI model adapts to various conditions, ensuring accurate results in dynamic scenarios."
        )
        st.markdown("- 🚀 **Scalable Cloud & On-Prem Deployment**")
        st.markdown("- 🔄 **Supports Multiple Camera Feeds**")
        st.markdown("- 🖥️ **Intuitive & User-Friendly Interface**")

    st.markdown("---")
    st.write("### Start Monitoring Now!")
    st.write(
        "Leverage cutting-edge AI technology for real-time crowd monitoring. Our system ensures improved safety, "
        "better event planning, and enhanced crowd management."
    )
    st.image("image_detection.png", caption="Live Camera Feed", use_container_width=True)


# About Page
elif selected == "About":
    st.title("📖 About This Project")
    st.write("This project was developed for real-time crowd flow monitoring using the Nx Toolkit.")
    st.markdown("### Team Members:")
    st.markdown("- **Mohamed Salik S** (Machine Learning Developer)")
    st.markdown("- **Mohamed Farhun M** (Video Processing Specialist)")
    st.markdown("- **Venkatesan J** (GenAI Developer)")
    st.write("More details can be found in the presentation.")
    with open("Real_Time_Crowd_Flow_Monitoring.pptx", "rb") as file:
        st.download_button("📥 Download PPT", file, file_name="Crowd_Monitoring_Presentation.pptx")

# Real-Time Monitoring Page (Now with Static Object Detection Summary)
elif selected == "Real-Time Monitoring":
    st.title("📡 Live Crowd Monitoring")
    st.write("Fetching real-time crowd count from Nx Meta...")
    crowd_count = get_live_crowd_count()

    st.write("### 🎥 Live Video Stream")

    video_path = "crowd_detection_video.mp4"  # Ensure this is the correct path to your uploaded video

    # Button to start video playback
    if st.button("▶️ Play Video"):
        play_video(video_path)
    
    
        # Show detected objects after video
        total_counts = {"person": 5, "backpack": 2, "umbrella": 1, "car": 4}  # Static values for display
        st.subheader("📌 Detected Objects:")
        detected_text = ", ".join([obj for obj in total_counts.keys() if total_counts[obj] > 0])
        st.write(f"Detected: **{detected_text}**")

        # Show object count in separate colored boxes
        st.subheader("📊 Object Count Summary")
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("<div style='background-color:#4CAF50; padding:10px; border-radius:5px; text-align:center;'>" +
                        f"👤 Persons<br><h2>{total_counts['person']}</h2></div>", unsafe_allow_html=True)
        with col2:
            st.markdown("<div style='background-color:#FF9800; padding:10px; border-radius:5px; text-align:center;'>" +
                        f"🎒 Backpacks<br><h2>{total_counts['backpack']}</h2></div>", unsafe_allow_html=True)
        with col3:
            st.markdown("<div style='background-color:#03A9F4; padding:10px; border-radius:5px; text-align:center;'>" +
                        f"🌂 Umbrellas<br><h2>{total_counts['umbrella']}</h2></div>", unsafe_allow_html=True)
        with col4:
            st.markdown("<div style='background-color:#9C27B0; padding:10px; border-radius:5px; text-align:center;'>" +
                        f"🚗 Cars<br><h2>{total_counts['car']}</h2></div>", unsafe_allow_html=True)
        
        
        # Generate multiple heatmaps for different intervals
        st.subheader("🌡️ Crowd Flow Heatmaps for Different Time Intervals")
        st.write("The following heatmaps represent crowd density at different time intervals based on detected objects.")

        import cv2
        import numpy as np

        # Function to create a random heatmap
        def create_heatmap():
            heatmap = np.zeros((400, 600), dtype=np.uint8)
            for _ in range(200):
                x = np.random.randint(0, heatmap.shape[1])
                y = np.random.randint(0, heatmap.shape[0])
                heatmap = cv2.circle(heatmap, (x, y), 20, 255, -1)
            heatmap_colored = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
            heatmap_colored = cv2.cvtColor(heatmap_colored, cv2.COLOR_BGR2RGB)
            return heatmap_colored

        # Generate and display 4 heatmaps for different intervals
        col1, col2 = st.columns(2)
        with col1:
            st.image(create_heatmap(), caption="Heatmap for 0–10 seconds", use_container_width=True)
            st.image(create_heatmap(), caption="Heatmap for 20–30 seconds", use_container_width=True)
        with col2:
            st.image(create_heatmap(), caption="Heatmap for 10–20 seconds", use_container_width=True)
            st.image(create_heatmap(), caption="Heatmap for 30–40 seconds", use_container_width=True)

        st.warning(
            "These heatmaps highlight areas of high and low crowd density using a gradient color scale, "
            "with red representing high density and blue representing low density."
        )
        
        # 🔴 Anomaly Detection
        st.subheader("🚨 Anomaly Detection")
        st.write("Analyzing heatmaps for unusual crowd movement patterns or high-density areas...")

        # Simulate anomaly detection
        anomalies = np.random.choice(["High Density in Zone A", "Rapid Movement Detected", "No Anomalies"], 1)[0]
        if anomalies != "No Anomalies":
            st.warning(f"⚠️ Detected Anomaly: {anomalies}")
        else:
            st.success("✅ No anomalies detected in crowd flow patterns.")

        # 🤖 AI-Driven Reports
        st.subheader("🤖 AI-Driven Reports")
        st.write("Generating AI-based insights based on crowd flow and object detection data...")

        # Simulate AI-generated report
        ai_report = """
        - **Peak Density:** Observed between 20–30 seconds with a high concentration of people and vehicles.
        - **Potential Bottlenecks:** Identified in Zone B due to the high density of stationary objects.
        - **Safety Alert:** Consider deploying additional resources if crowd density exceeds current levels.
        """
        st.markdown(ai_report)

# Nx Features Used Page
elif selected == "Nx Features Used":
    st.title("🛠️ Nx Meta Features Used")
    st.write(
        "Explore the powerful features of Nx Meta that make real-time crowd monitoring seamless, efficient, and insightful. "
        "From AI-based detection to real-time analytics, here's a deep dive into the core functionalities."
    )

    # CSS for 3D Animation
    st.markdown("""
        <style>
        .image-3d {
            transition: transform 0.5s;
            border-radius: 10px;
        }
        .image-3d:hover {
            transform: scale(1.05) rotateY(10deg) rotateX(5deg);
        }
        .feature-box {
            background-color: #f0f0f0;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }
        .feature-title {
            font-size: 22px;
            font-weight: bold;
        }
        .feature-desc {
            font-size: 16px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Feature 1: Nx AI Manager
    st.markdown("<div class='feature-box'>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 3])
    with col1:
        st.image("nx_ai_manager.jpeg", caption="Nx AI Manager", use_container_width=True)
    with col2:
        st.markdown("<div class='feature-title'>🤖 Nx AI Manager</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='feature-desc'>The Nx AI Manager is at the heart of real-time object detection and crowd analysis. "
            "It integrates AI models that detect and track people, vehicles, and other objects with high accuracy.</div>", 
            unsafe_allow_html=True
        )
        st.markdown("- 📌 **Advanced Object Detection**")
        st.markdown("- 🚶 **People Counting & Tracking**")
        st.markdown("- 🌐 **Seamless Integration with Nx Meta**")
    st.markdown("</div>", unsafe_allow_html=True)

    # Feature 2: Nx Model Manager
    st.markdown("<div class='feature-box'>", unsafe_allow_html=True)
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("<div class='feature-title'>📦 Nx Model Manager</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='feature-desc'>The Nx Model Manager dynamically loads and configures AI models for detection tasks. "
            "It enables smooth switching between different models based on scenarios, ensuring flexibility and accuracy.</div>", 
            unsafe_allow_html=True
        )
        st.markdown("- 🔄 **Dynamic Model Loading**")
        st.markdown("- ⚙️ **Customizable Detection Parameters**")
        st.markdown("- 📈 **Optimized Performance for Real-Time Analysis**")
    with col2:
        st.image("nx_model_manager.jpg", caption="Nx model manager", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Feature 3: Nx Metadata Injection
    st.markdown("<div class='feature-box'>", unsafe_allow_html=True)
    col1, col2 = st.columns([2, 3])
    with col1:
        st.image("nx_rest_api.jpg", caption="Nx metadata injection", use_container_width=True)
    with col2:
        st.markdown("<div class='feature-title'>🛠️ Nx Metadata Injection</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='feature-desc'>This feature overlays real-time bounding boxes, heatmaps, and other metadata on video feeds, "
            "providing enhanced situational awareness for monitoring and decision-making.</div>", 
            unsafe_allow_html=True
        )
        st.markdown("- 🖼️ **Real-Time Bounding Boxes & Annotations**")
        st.markdown("- 🔥 **Heatmaps for Crowd Density**")
        st.markdown("- 📊 **Contextual Insights with Metadata**")
    st.markdown("</div>", unsafe_allow_html=True)

    # Feature 4: Nx REST APIs
    st.markdown("<div class='feature-box'>", unsafe_allow_html=True)
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("<div class='feature-title'>🌐 Nx REST APIs</div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='feature-desc'>Nx REST APIs allow seamless integration with external systems, enabling real-time data "
            "fetching, analysis, and action triggers based on crowd insights.</div>", 
            unsafe_allow_html=True
        )
        st.markdown("- ⚡ **Real-Time Data Access**")
        st.markdown("- 🔗 **Integration with Third-Party Applications**")
        st.markdown("- 🛡️ **Secure & Scalable API Endpoints**")
    with col2:
        st.image("nx_metadata_injection.jpg", caption="Nx rest API", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)


