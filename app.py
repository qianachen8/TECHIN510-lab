import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Qiana Chen - Web3.0 Builder | Creator | Storyteller | Art Appreciator",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="auto",
)

# Use columns to center the text "This is Qiana"
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<h1 style='text-align: center;'>This is Qianaaaaa</h1>", unsafe_allow_html=True)

st.markdown("##")  # Markdown for a larger space
st.markdown("##")  # Markdown for a larger space

# Load and display the image at 70% of the size
image = Image.open('./profile.png')
# Resize image to 70% of its size
image = image.resize((int(image.size[0] * 0.7), int(image.size[1] * 0.7)))
st.image(image)

# Add a spacer between the image and the text
st.markdown("##")  # Markdown for a larger space
st.markdown("#")   # Markdown for a smaller space

st.markdown("# Projects")
st.markdown("- [Lemonbox online nutrition supplier](https://qianachen.webflow.io/lemon-simple)")
st.markdown("- [Upup OS](https://qianachen.webflow.io/try)")
st.markdown("- [Innovative dating app in China](https://qianachen.webflow.io/wankr)")

st.markdown("##")  # Markdown for a larger space

st.markdown("# Contact")
st.write("Current Location: Belleve, WA")
st.write("Phone: +1 (206) 200-7855")
st.write("E-mail: qianachen8@gmail.com")


# Social media and other links
social_media = {
    "Instagram": ("https://linktr.ee/qianachen", "fab fa-instagram"),
    "Facebook": ("https://linktr.ee/qianachen", "fab fa-facebook"),
    "Github": ("https://linktr.ee/qianachen", "fab fa-github"),
    "LinkedIn": ("https://linktr.ee/qianachen", "fab fa-linkedin")
}


# Display social media icons with links
for platform, (link, icon) in social_media.items():
    st.markdown(f'<a href="{link}" target="_blank"><i class="{icon}"></i> {platform}</a>', unsafe_allow_html=True)


# Footer
ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">
<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/sape94" target="_blank"> by sape94</a></p>
</div>
</div>
"""
st.markdown(ft, unsafe_allow_html=True)
