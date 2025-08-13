import streamlit as st
import streamlit_tags
from datetime import date

# Example data
articles = [
    {"id": 1, "title": "First Post", "body": "This is the first post", "tags": ["news", "update"], "user": "alice"},
    {"id": 2, "title": "Second Post", "body": "Another article body", "tags": ["tech"], "user": "bob"},
    {"id": 3, "title": "Third Post", "body": "More content here", "tags": ["fun", "news"], "user": "carol"},
    {"id": 4, "title": "Third Post", "body": "More content here", "tags": ["fun", "news"], "user": "carol"},
    {"id": 5, "title": "Third Post", "body": "More content here", "tags": ["fun", "news"], "user": "carol"},
    {"id": 6, "title": "Third Post", "body": "More content here", "tags": ["fun", "news"], "user": "carol"},
]

def article_card(article):
    with st.container():
        col1, col2 = st.columns([9,1])
        with col1:
            st.markdown(
                f"""
                <div style="
                    border:1px solid #ccc; 
                    border-radius:10px; 
                    padding:10px; 
                    margin-bottom:5px;
                ">
                    <h4 style="padding:2px;font-weight:bold;">{article['title']}</h4>
                    <p style="margin-bottom:5px;margin:0px;font-style:italic;color:gray;">by {article['user']}</p>
                    <p style="margin-bottom:0px;">{article['body']}</p>
                    <div style="
                        display:flex; 
                        justify-content:space-between; 
                        align-items:center; 
                        margin-top:5px;
                    ">
                        <span>Tags: {', '.join(article['tags'])}</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col2:
            if st.button("❌", key=f"delete_{article['id']}"):
                confirm_deletion()


@st.dialog("Confirm Deletion")
def confirm_deletion():
    st.write(f"Are you sure you want to delete the article '{article['title']}'?")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Delete"):
            # Todo: Add deletion Logic
            st.rerun()
    with col2:
        if st.button("Cancel"):
            st.rerun()


tabs = st.tabs(["Publish new articles", "Search for articles"])
with tabs[0]:
    st.header("Publish New Article")

    title = st.text_input(label="", placeholder="Article's title")
    content = st.text_area(label="", placeholder="Write your article here!")
    tags = streamlit_tags.st_tags(label="", text="Add tags")

    if st.button("Publish"):
        # Todo: Add creation logic
        st.success("Article published!")

with tabs[1]:
    all_tags = sorted({tag for a in articles for tag in a['tags']}) #placeholder

    title_filter = st.text_input("Title contains...")
    tags_filter = streamlit_tags.st_tags(label="Tags:", suggestions=all_tags, text="Add tags")
    date_filter = st.date_input("Published on or after", value=None)
    user_filter = st.text_input("Username")

    # Render filtered articles
    with st.container(height=500):
        for article in articles:
            article_card(article)
