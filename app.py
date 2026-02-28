import json
import streamlit as st

st.set_page_config(page_title="Rosary Meditations", page_icon="📿", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,600;1,400&family=Cinzel:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'EB Garamond', serif;
}

h1, h2, h3 {
    font-family: 'Cinzel', serif;
}

.stApp {
    background-color: #1a1208;
    color: #e8d9b5;
}

section[data-testid="stSidebar"] {
    background-color: #120d04;
    border-right: 1px solid #4a3520;
}

.mystery-title {
    font-family: 'Cinzel', serif;
    font-size: 1.8rem;
    color: #c9a84c;
    text-align: center;
    margin-bottom: 0.2rem;
    letter-spacing: 0.05em;
}

.mystery-subtitle {
    font-family: 'EB Garamond', serif;
    font-style: italic;
    font-size: 1.1rem;
    color: #a08050;
    text-align: center;
    margin-bottom: 2rem;
}

.section-header {
    font-family: 'Cinzel', serif;
    font-size: 0.85rem;
    letter-spacing: 0.15em;
    color: #c9a84c;
    text-transform: uppercase;
    border-bottom: 1px solid #4a3520;
    padding-bottom: 0.4rem;
    margin-top: 2rem;
    margin-bottom: 1rem;
}

.scripture-ref {
    display: inline-block;
    background: #2a1e0a;
    border: 1px solid #4a3520;
    color: #c9a84c;
    font-family: 'Cinzel', serif;
    font-size: 0.8rem;
    padding: 0.2rem 0.7rem;
    margin: 0.2rem;
    border-radius: 2px;
    letter-spacing: 0.05em;
}

.summary-text {
    font-size: 1.1rem;
    line-height: 1.9;
    color: #d4c49a;
    font-style: italic;
}

.reflection-item {
    display: flex;
    gap: 1rem;
    margin-bottom: 0.9rem;
    align-items: flex-start;
}

.reflection-number {
    font-family: 'Cinzel', serif;
    color: #c9a84c;
    font-size: 0.8rem;
    min-width: 1.5rem;
    padding-top: 0.2rem;
}

.reflection-text {
    font-size: 1rem;
    line-height: 1.75;
    color: #d4c49a;
}

.question-item {
    font-size: 1rem;
    line-height: 1.75;
    color: #d4c49a;
    padding: 0.5rem 0;
    border-bottom: 1px solid #2a1e0a;
}

.prayer-label {
    font-family: 'Cinzel', serif;
    font-size: 0.75rem;
    letter-spacing: 0.12em;
    color: #c9a84c;
    text-transform: uppercase;
    margin-bottom: 0.3rem;
}

.prayer-text {
    font-size: 1rem;
    line-height: 1.8;
    color: #d4c49a;
    font-style: italic;
    margin-bottom: 1.2rem;
    padding-left: 1rem;
    border-left: 2px solid #4a3520;
}

.quote-block {
    background: #130e03;
    border-left: 3px solid #c9a84c;
    padding: 1rem 1.2rem;
    margin-bottom: 1.2rem;
    border-radius: 0 4px 4px 0;
}

.quote-text {
    font-size: 1rem;
    line-height: 1.8;
    color: #d4c49a;
    font-style: italic;
    margin-bottom: 0.5rem;
}

.quote-author {
    font-family: 'Cinzel', serif;
    font-size: 0.75rem;
    color: #c9a84c;
    letter-spacing: 0.1em;
}

.divider {
    border: none;
    border-top: 1px solid #2a1e0a;
    margin: 2rem 0;
}

/* Selectbox styling */
.stSelectbox label {
    font-family: 'Cinzel', serif !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.1em !important;
    color: #a08050 !important;
    text-transform: uppercase !important;
}
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    with open("rosary.json", "r") as f:
        return json.load(f)


MYSTERY_LABELS = {
    'joyful': 'Joyful Mysteries',
    'luminous': 'Luminous Mysteries',
    'sorrowful': 'Sorrowful Mysteries',
    'glorious': 'Glorious Mysteries',
}

ORDINAL_LABELS = {
    '1': 'First', '2': 'Second', '3': 'Third', '4': 'Fourth', '5': 'Fifth'
}

PRAYER_LABELS = {
    'blessing_and_adoration': 'Blessing & Adoration',
    'praise': 'Praise',
    'thanksgiving': 'Thanksgiving',
    'intercession': 'Intercession',
    'petition': 'Petition',
}

data = load_data()

with st.sidebar:
    st.markdown("<div style='font-family:Cinzel,serif;color:#c9a84c;font-size:1.1rem;letter-spacing:0.1em;margin-bottom:1.5rem;'>📿 ROSARY MEDITATIONS</div>", unsafe_allow_html=True)

    mystery_key = st.selectbox(
        "Mystery",
        options=list(MYSTERY_LABELS.keys()),
        format_func=lambda k: MYSTERY_LABELS[k]
    )

    mystery_data = data.get(mystery_key, {})
    available_numbers = sorted(mystery_data.keys(), key=lambda x: int(x))

    number_key = st.selectbox(
        "Mystery Number",
        options=available_numbers,
        format_func=lambda k: f"{ORDINAL_LABELS.get(str(k), k)} Mystery"
    )

    entry = mystery_data.get(str(number_key), mystery_data.get(number_key, {}))

    st.markdown("<hr style='border-color:#2a1e0a;margin:1.5rem 0;'>", unsafe_allow_html=True)
    st.markdown("<div style='font-family:Cinzel,serif;color:#4a3520;font-size:0.7rem;letter-spacing:0.1em;'>SECTIONS</div>", unsafe_allow_html=True)

    sections = ['scripture', 'summary', 'reflections', 'questions', 'prayers', 'quotes']
    section_labels = {
        'scripture': 'Scripture References',
        'summary': 'The Story in Brief',
        'reflections': 'Points to Ponder',
        'questions': 'Application Questions',
        'prayers': 'Prayer',
        'quotes': 'Quotes from the Saints',
    }
    show_sections = {}
    for s in sections:
        if s in entry:
            show_sections[s] = st.checkbox(section_labels[s], value=True)

if not entry:
    st.warning("No data found for this mystery.")
    st.stop()

title = entry.get('title', '')
st.markdown(f"<div class='mystery-title'>{title}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='mystery-subtitle'>{MYSTERY_LABELS[mystery_key]} · {ORDINAL_LABELS.get(str(number_key), number_key)} Mystery</div>", unsafe_allow_html=True)

# Scripture
if show_sections.get('scripture') and 'scripture' in entry:
    st.markdown("<div class='section-header'>Scripture References</div>", unsafe_allow_html=True)
    refs_html = ''.join(f"<span class='scripture-ref'>{ref}</span>" for ref in entry['scripture'])
    st.markdown(refs_html, unsafe_allow_html=True)

# Summary
if show_sections.get('summary') and 'summary' in entry:
    st.markdown("<div class='section-header'>The Story in Brief</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='summary-text'>{entry['summary']}</div>", unsafe_allow_html=True)

# Reflections
if show_sections.get('reflections') and 'reflections' in entry:
    st.markdown("<div class='section-header'>Points to Ponder</div>", unsafe_allow_html=True)
    for i, reflection in enumerate(entry['reflections'], 1):
        st.markdown(f"""
        <div class='reflection-item'>
            <div class='reflection-number'>{i}.</div>
            <div class='reflection-text'>{reflection}</div>
        </div>
        """, unsafe_allow_html=True)

# Questions
if show_sections.get('questions') and 'questions' in entry:
    st.markdown("<div class='section-header'>Application Questions</div>", unsafe_allow_html=True)
    for i, q in enumerate(entry['questions'], 1):
        st.markdown(f"""
        <div class='reflection-item'>
            <div class='reflection-number'>{i}.</div>
            <div class='reflection-text'>{q}</div>
        </div>
        """, unsafe_allow_html=True)

# Prayers
if show_sections.get('prayers') and 'prayers' in entry:
    st.markdown("<div class='section-header'>Prayer</div>", unsafe_allow_html=True)
    for key, label in PRAYER_LABELS.items():
        if key in entry['prayers']:
            st.markdown(f"<div class='prayer-label'>{label}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='prayer-text'>{entry['prayers'][key]}</div>", unsafe_allow_html=True)

# Quotes
if show_sections.get('quotes') and 'quotes' in entry:
    st.markdown("<div class='section-header'>Quotes from the Saints</div>", unsafe_allow_html=True)
    for quote in entry['quotes']:
        st.markdown(f"""
        <div class='quote-block'>
            <div class='quote-text'>"{quote['quote']}"</div>
            <div class='quote-author'>— {quote['author']}</div>
        </div>
        """, unsafe_allow_html=True)
