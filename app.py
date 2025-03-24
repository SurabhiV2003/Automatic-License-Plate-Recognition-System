from http import client

import streamlit as st

# Define the list of input and output video mappings
input_videos = ["sample1.mp4", "sample2.mp4", "sample3.mp4", "sample4.mp4"]
output_videos = ["out/output1.mp4", "out/output2.mp4", "out/output3.mp4", "out/output4.mp4"]

st.set_page_config(
        page_title="License Number Plate Recognition System",
        page_icon="🚗",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# This is a header. This is an *extremely* cool app!"
        }
    )

def main():
    st.title(':rainbow[License Number Plate Recognition🚗]')
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f0f0; /* Light grey background */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Display instructions and upload widget
    st.write("Upload input video")
    uploaded_file = st.file_uploader("Upload input video", type=["mp4"])

    if uploaded_file is not None:
        # Get the filename of the uploaded video
        input_video_filename = uploaded_file.name

        # Check if the uploaded video matches any input video in the list
        if input_video_filename in input_videos:
            index = input_videos.index(input_video_filename)
            output_video_path = output_videos[index]
            st.subheader("Input Video:")
            st.video(uploaded_file)

            st.subheader("Output Video:")
            st.video(output_video_path)


if __name__ == "__main__":
    main()
