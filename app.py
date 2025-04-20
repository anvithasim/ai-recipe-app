import streamlit as st
import openai

# OpenAI API Key
openai.api_key = "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"

st.set_page_config(page_title="AI Recipe + Vibe Generator")
st.title("🍳 AI Recipe + Spotify Vibes Generator")

ingredients = st.text_input("🥦 What ingredients do you have?")
vibe = st.selectbox("💫 What’s your cooking vibe?", [
    "Cozy",
    "Spicy",
    "Healthy",
    "Romantic",
    "High-protein",
    "Budget-friendly",
    "Energizing",
    "Comfort food",
    "Vegan",
    "Cheesy",
    "Hangover Cure",
    "Quick & Easy",
    "Dessert Vibes",
    "Fancy Dinner"
])

vibe_to_playlist = {
    "Cozy": "https://open.spotify.com/playlist/37i9dQZF1DX3PIPIT6lEg5",
    "Spicy": "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0",
    "Healthy": "https://open.spotify.com/playlist/2MjVkJ2SzdSChOpW4GvpiR",
    "Romantic": "https://open.spotify.com/playlist/37i9dQZF1DX50QitC6Oqtn",
    "High-protein": "https://open.spotify.com/playlist/37i9dQZF1DX4xuWVBs4FgJ",
    "Budget-friendly": "https://open.spotify.com/playlist/37i9dQZF1DWSqBruwoIXkA",
    "Energizing": "https://open.spotify.com/playlist/37i9dQZF1DX1s9knjP51Oa",
    "Comfort food": "https://open.spotify.com/playlist/37i9dQZF1DWX3387IZmjNa",
    "Vegan": "https://open.spotify.com/playlist/37i9dQZF1DX7YCknf2jT6s",
    "Cheesy": "https://open.spotify.com/playlist/37i9dQZF1DX6T5dWVv97mp",
    "Hangover Cure": "https://open.spotify.com/playlist/37i9dQZF1DWZJhOVGWqUKF",
    "Quick & Easy": "https://open.spotify.com/playlist/37i9dQZF1DXcA6dRp8rwjV",
    "Dessert Vibes": "https://open.spotify.com/playlist/37i9dQZF1DX4PP3DA4J0N8",
    "Fancy Dinner": "https://open.spotify.com/playlist/37i9dQZF1DXcCnTAt8CfNe"
}

if st.button("✨ Generate My Recipe + Playlist"):
    prompt = f"Create a creative recipe using these ingredients: {ingredients}. The recipe should have a {vibe.lower()} vibe. Include a name, ingredients list, and step-by-step instructions."

    with st.spinner("Cooking up your recipe..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        recipe = response['choices'][0]['message']['content']
        st.markdown("### 🥘 Your Recipe")
        st.markdown(recipe)

        st.markdown("### 🎶 Your Cooking Playlist")
        st.markdown(f"[Click here to listen on Spotify]({vibe_to_playlist[vibe]})")
