from numpy.char import center
import streamlit as st
import streamlit_tags
from API_requests import get_articles, create_article, delete_article

user = 1 # Placeholder for creating articles

@st.cache_data
def cached_get_articles(title=None, tags=None, user=None, date=None):
    return get_articles(title, tags, user, date)

def article_card(article):
    with st.container():
        col1, col2 = st.columns([9,1])
        with col1:
            tag_names = [tag["name"] for tag in article.get("tags", []) if isinstance(tag, dict) and "name" in tag]
            
            st.markdown(
                f"""
                <div style="
                    border:1px solid #ccc; 
                    border-radius:10px; 
                    padding:10px; 
                    margin-bottom:5px;
                ">
                    <h4 style="padding:2px;font-weight:bold;">{article.get("title", "No Title")}</h4>
                    <p style="margin-bottom:5px;margin:0px;font-style:italic;color:gray;">by {article.get("username", "Unknown User")}</p>
                    <p style="margin-bottom:0px;">{article.get("content", "No content")}</p>
                    <div style="
                        display:flex; 
                        justify-content:space-between; 
                        align-items:center; 
                        margin-top:5px;
                    ">
                        <span>Tags: {" - ".join(tag_names)}</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col2:
            article_id = article.get("id")
            if article_id and st.button("❌", key=f"delete_{article_id}"):
                confirm_deletion(article_id, article.get("title", "Unknown Article"))


@st.dialog("Confirm Deletion")
def confirm_deletion(article_id, article_title):
    st.write(f"Are you sure you want to delete the article '{article_title}'?")
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Delete"):
            if delete_article(article_id):
                st.success("Deleted!")
                st.rerun()
            else:
                st.error("Failed to delete")
    with col2:
        if st.button("Cancel"):
            st.rerun()


tabs = st.tabs(["Publish new articles", "Search for articles"])
with tabs[0]:
    st.header("Publish New Article")

    title = st.text_input(label=" ", placeholder="Article's title")
    content = st.text_area(label=" ", placeholder="Write your article here!")
    tags = streamlit_tags.st_tags(label=" ", text="Add tags")

    if st.button("Publish"):
        if create_article(title, content, tags, user):
            st.success("Article published!")
            st.rerun()
        else:
            st.error("Failed to publish the article")

with tabs[1]:
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        title_filter = st.text_input(label="Title contains...")
    with col2:
        tags_filter = streamlit_tags.st_tags(label="Tags:", text="Add tags")
    with col3:
        date_filter = st.date_input("Published on", value=None)
    with col4:
        user_filter = st.text_input("Username")

    articles = cached_get_articles(title_filter, tags_filter, user_filter, date_filter)
    with st.container(height=500):
        if not articles:
            st.write("No articles found")
        else:
            for article in articles:
                article_card(article)