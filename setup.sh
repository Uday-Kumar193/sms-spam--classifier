mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"uday_b230594ec@nitc.ac.in\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
