import streamlit as st
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(
    page_title="AI YouTube Description Generator",
    page_icon=":film_frames:",  # Favicon emoji
    layout="centered",  # Page layout option
)

# Directly set the API key here (ensure security in production)
GOOGLE_API_KEY = "AIzaSyDL_nopsrrujLZJuMjVbSLxjkC8B11LOMw"

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Streamlit app layout
st.title("AI YouTube Description Generator")

# User input: Video title, keyword, or idea
video_input = st.text_input("Enter the YouTube title, keyword, or idea about your video:")

# Checkbox for including timestamps
include_timestamps = st.checkbox("Include timestamps in the description")

# Generate the YouTube description based on the user input
if st.button("Generate Description"):
    timestamp_section = (
        """
        🕒 **Timestamps:**
        - 00:00 Introduction
        - 01:30 [Section Title]
        - 03:45 [Another Section Title]
        """
        if include_timestamps else ""
    )
    
    prompt = f"""
    Based on the following video title, keyword, or idea, generate the best possible YouTube description that is SEO-optimized, engaging, and designed to rank well on YouTube.

    Video Input:
    {video_input}

    The description should:
    1. Start with a captivating introduction using emojis to grab attention.
    2. Include relevant keywords naturally embedded in the text.
    3. Be well-structured with bullet points or sections to make it easy to read.
    4. Include a call-to-action (CTA) that encourages viewers to like, subscribe, and engage with the content.
    5. {timestamp_section}
    6. Add any additional relevant information, such as links to related content, to enhance the video's discoverability on YouTube.

    **Examples**:
    
    - **Title**: "Top 10 Travel Destinations in 2024 🌍✈️"
    - **Description**:
      ```
      🌟 Ready to explore the world? Join us as we countdown the top 10 must-visit travel destinations for 2024! From tropical paradises to cultural hotspots, we've got you covered. Don't miss out on these amazing places! 🌴✨
      
      🔎 **In this video:**
      - Discover hidden gems you need to add to your bucket list
      - Learn travel tips and hacks for each destination
      - Get inspired for your next adventure!

      👉 **Like and subscribe** for more travel guides and tips! Hit the notification bell so you never miss an update. ✨

      🔗 **Related Videos:**
      - [Top 10 Budget Travel Tips](https://www.youtube.com/watch?v=example)
      - [How to Travel Solo Safely](https://www.youtube.com/watch?v=example)

      {timestamp_section}
      ```

    - **Title**: "How to Start a Successful YouTube Channel in 2024 📈"
    - **Description**:
      ```
      🚀 Thinking of starting a YouTube channel? Now is the perfect time! In this video, we walk you through the essential steps to launch and grow a successful YouTube channel in 2024. From content creation to monetization, we've got everything you need to know.

      📋 **What you'll learn:**
      - Choosing the right niche for your channel
      - Tips for creating engaging content
      - How to grow your subscriber base quickly
      - Monetization strategies to start earning from day one

      👍 **Don't forget to smash that like button,** **subscribe,** and **ring the notification bell** so you never miss an update. Your support helps us create more valuable content! 🔔

      🔗 **Check out our other videos:**
      - [YouTube SEO Tips for 2024](https://www.youtube.com/watch?v=example)
      - [Best Video Editing Software for Beginners](https://www.youtube.com/watch?v=example)

      {timestamp_section}
      ```

    Please generate a similar YouTube description that is well-structured, engaging, and optimized for ranking.
    """
    
    with st.spinner("Generating description..."):
        # Generate the description using the Gemini-Pro model
        response = model.generate_content([prompt])
        description = response.text

    # Display the generated description
    st.subheader("Generated YouTube Description")
    st.write(description)
