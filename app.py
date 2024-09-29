import streamlit as st
import pandas as pd
from datetime import datetime

# Load event dataset
events_df = pd.read_csv('data/events.csv')
events = events_df.to_dict(orient='records')

def main():
    st.title("Huerta Event App")

    menu = ["Login", "Find Events", "Chat with ChatGPT"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Sample data for people with similar interests
    people = [
        {"name": "Sophia", "interest": "Tech Workshops", "bio": "Tech enthusiast looking to connect.", "image": "https://via.placeholder.com/50"},
        {"name": "Isabella", "interest": "Entrepreneurship", "bio": "Founder of a local startup.", "image": "https://via.placeholder.com/50"},
        {"name": "Camila", "interest": "Art & Culture", "bio": "Artist exploring new ideas.", "image": "https://via.placeholder.com/50"}
    ]

    # Function to format the date
    def format_date(date_str):
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%B %d, %Y")

    # Function to format the time
    def format_time(time_str):
        time_obj = datetime.strptime(time_str, "%H:%M")
        return time_obj.strftime("%I:%M %p")

    # Styling (added circular profile image styling)
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #771891;  /* Purple background */
        }
        * {
            color: white !important;  /* Make all text white */
            font-size: 18px;  /* Base font size */
        }
        .custom-subheader {
            font-size: 32px !important;  /* Larger font for subheaders */
            font-weight: bold;
        }
        .location {
            background-color: rgba(128, 128, 128, 0.5);  /* Semi-transparent gray background */
            color: black;  /* Black text color */
            padding: 3px;  /* Padding around the text */
            border-radius: 5px;  /* Rounded corners */
        }
        .stButton>button {
            background-color: #4682B4; /* Custom button background */
            color: white;  /* Button text color */
            width: 100%;  /* Full width button */
            max-width: 150px;  /* Limit maximum width to 150px */
            margin: 5px auto;  /* Center buttons */
            padding: 10px 0;  /* Padding inside buttons for height */
            font-size: 16px;  /* Set font size */
        }
        .circle-img {
            border-radius: 50%;  /* Make image circular */
            width: 50px;  /* Set fixed width */
            height: 50px;  /* Set fixed height */
            object-fit: cover;  /* Maintain aspect ratio */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sidebar for People Want You!
    with st.sidebar:
        st.markdown('<h2 class="custom-subheader">People Want You!</h2>', unsafe_allow_html=True)
        for person in people:
            col1, col2 = st.columns([1, 3])  # Adjust proportions as needed
            with col1:
                # Circular profile image
                st.markdown(f'<img class="circle-img" src="{person["image"]}"/>', unsafe_allow_html=True)  
            with col2:
                st.write(person['name'])  # Display person's name
                st.write(f"**Interested in:** {person['interest']}")
                st.write(f"_{person['bio']}_")
                if st.button(f"Connect with {person['name']}"):
                    st.success(f"Connection request sent to {person['name']}!")

    # Initialize session state for selected event and show_all_events
    if 'selected_event' not in st.session_state:
        st.session_state.selected_event = None
    if 'show_all_events' not in st.session_state:
        st.session_state.show_all_events = False

    # Display event details if an event is selected
    if st.session_state.selected_event is not None:
        event = st.session_state.selected_event
        st.image("https://via.placeholder.com/150", caption=event['event_name'])  # Placeholder image
        # Display description first
        st.write(f"**Description:** {event['description']}")
        # Display combined date, time, and location at the bottom
        st.write(f"The event is on {format_date(event['event_date'])} at {format_time(event['event_time'])} in {event['location']}.")
        if st.button("Close Event"):
            st.session_state.selected_event = None  # Reset the selected event when the button is clicked
    else:
        # Display top 3 events
        st.markdown('<h2 class="custom-subheader">Top Events</h2>', unsafe_allow_html=True)
        cols = st.columns(3)  # Create 3 columns for top events
        for i, event in enumerate(events[:3]):  # Display only the top 3 events
            with cols[i]:
                st.markdown(f"<span class='location'>Location: {event['location']}</span>", unsafe_allow_html=True)  # Highlighted location
                st.image("https://via.placeholder.com/150", caption=event['event_name'])  # Placeholder image
                st.write(f"**Date:** {format_date(event['event_date'])}")
                st.write(f"**Time:** {format_time(event['event_time'])}")
                if st.button(f"View Event", key=f"view_event_{i}"):
                    st.session_state.selected_event = event  # Set the selected event

        # Button to view all events
        if st.button("View All Events"):
            st.session_state.show_all_events = True

        # If the user has clicked to view all events
        if st.session_state.show_all_events:
            st.markdown('<h2 class="custom-subheader">All Events</h2>', unsafe_allow_html=True)
            for event in events:
                st.markdown(f"<span class='location'>Location: {event['location']}</span>", unsafe_allow_html=True)  # Highlighted location
                st.image("https://via.placeholder.com/150", caption=event['event_name'])  # Placeholder image
                st.write(f"**Date:** {format_date(event['event_date'])}")
                st.write(f"**Time:** {format_time(event['event_time'])}")
                st.write(f"**Description:** {event['description']}")
                st.write("---")  # Divider between events

            # Button to close the events
            if st.button("Close Events"):
                st.session_state.show_all_events = False  # Reset the view

if __name__ == '__main__':
    main()
