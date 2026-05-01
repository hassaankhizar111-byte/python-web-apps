import streamlit as st

st.set_page_config(
    page_title="Character Forge",
    page_icon="⚔",
    layout="centered"
)

st.markdown("""
    <style>
        .char-card {
            background: #111;
            border: 1px solid #333;
            border-radius: 12px;
            padding: 1.5rem;
            margin-top: 1rem;
            font-family: monospace;
        }
        .char-name {
            font-size: 2rem;
            font-weight: bold;
            letter-spacing: 0.1em;
            color: #fff;
        }
        .char-class {
            font-size: 0.85rem;
            color: #888;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            margin-top: 4px;
        }
        .stat-row {
            margin-top: 0.8rem;
            font-family: monospace;
            font-size: 1rem;
            color: #ccc;
        }
    </style>
""", unsafe_allow_html=True)


st.title("Character Forge")
st.caption("Distribute exactly 7 points across your stats. Min 1 — Max 4 each.")

st.divider()

name = st.text_input(
    "Character Name",
    max_chars=10,
    placeholder="Max 10 chars, no spaces"
)

st.markdown("#### Stats")

col1, col2, col3 = st.columns(3)
with col1:
    strength = st.number_input("STR — Strength", min_value=1, max_value=4, value=3, step=1)
with col2:
    intelligence = st.number_input("INT — Intelligence", min_value=1, max_value=4, value=3, step=1)
with col3:
    charisma = st.number_input("CHA — Charisma", min_value=1, max_value=4, value=1, step=1)


def format_dots(label, value):
    filled = "●" * value
    empty = "○" * (10 - value)
    return f"`{label}` {filled}{empty}"


def get_class(s, i, c):
    if s >= 3:
        return "WARRIOR — Born of iron and blood"
    elif i >= 3:
        return "MAGE — Master of the arcane"
    elif c >= 3:
        return "ROGUE — Shadow and silver tongue"
    else:
        return "WANDERER — Path yet unknown"


total = int(strength + intelligence + charisma)
remaining = 7 - total

if remaining > 0:
    st.warning(f"{remaining} point(s) remaining to distribute.")
elif remaining < 0:
    st.error(f"Over budget by {abs(remaining)} point(s). Reduce your stats.")
else:
    st.success("7 / 7 points used — ready to forge.")

st.divider()

if st.button("[ Create Character ]", use_container_width=True, type="primary"):
    errors = []

    if not name:
        errors.append("Character name is required.")
    elif " " in name:
        errors.append("Name cannot contain spaces.")

    if remaining != 0:
        errors.append("Stats must total exactly 7 points.")

    if errors:
        for e in errors:
            st.error(e)
    else:
        char_class = get_class(int(strength), int(intelligence), int(charisma))

        st.markdown(f"""
        <div class="char-card">
            <div class="char-name">{name.upper()}</div>
            <div class="char-class">{char_class}</div>
            <hr style="border-color:#333; margin: 1rem 0;">
            <div class="stat-row">STR &nbsp; {"●" * int(strength)}{"○" * (10 - int(strength))}</div>
            <div class="stat-row">INT &nbsp; {"●" * int(intelligence)}{"○" * (10 - int(intelligence))}</div>
            <div class="stat-row">CHA &nbsp; {"●" * int(charisma)}{"○" * (10 - int(charisma))}</div>
        </div>
        """, unsafe_allow_html=True)

        st.balloons()