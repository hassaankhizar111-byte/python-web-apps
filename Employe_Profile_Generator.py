import streamlit as st

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Employee Profile Generator",
    page_icon="🪪",
    layout="centered",
)

# ─────────────────────────────────────────────
#  CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #0d0f14;
    color: #e8e8e8;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2.5rem 1.5rem 3rem; max-width: 780px; }

.hero-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 3.6rem;
    letter-spacing: 4px;
    color: #ffffff;
    line-height: 1;
    margin-bottom: 2px;
}
.hero-sub {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 3px;
    color: #00e5b0;
    text-transform: uppercase;
    margin-bottom: 2rem;
}
.emp-card {
    background: linear-gradient(135deg, #161b26 0%, #1a2030 100%);
    border: 1px solid #2a3040;
    border-left: 4px solid #00e5b0;
    border-radius: 12px;
    padding: 28px 32px;
    margin-bottom: 18px;
    box-shadow: 0 8px 32px rgba(0,229,176,0.06);
    position: relative;
    overflow: hidden;
}
.emp-card::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 120px; height: 120px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(0,229,176,0.07) 0%, transparent 70%);
    pointer-events: none;
}
.sec-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 3px;
    color: #00e5b0;
    text-transform: uppercase;
    margin-bottom: 10px;
}
.stat-grid { display: flex; gap: 14px; flex-wrap: wrap; }
.stat-box {
    flex: 1;
    min-width: 130px;
    background: #0d1117;
    border: 1px solid #2a3040;
    border-radius: 8px;
    padding: 14px 18px;
    position: relative;
}
.stat-box .val {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.9rem;
    color: #ffffff;
    line-height: 1;
}
.stat-box .lbl {
    font-family: 'DM Mono', monospace;
    font-size: 0.58rem;
    letter-spacing: 2px;
    color: #5a6070;
    text-transform: uppercase;
    margin-top: 4px;
}
.accent-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #00e5b0;
    position: absolute;
    top: 12px; right: 12px;
}
.name-banner {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.4rem;
    letter-spacing: 3px;
    color: #ffffff;
    margin-bottom: 4px;
}
.code-pill {
    display: inline-block;
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    background: #0d1117;
    border: 1px solid #00e5b0;
    color: #00e5b0;
    border-radius: 99px;
    padding: 4px 14px;
    letter-spacing: 1px;
    margin-bottom: 16px;
}
.code-seg { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 10px; }
.seg-block {
    background: #0d1117;
    border: 1px solid #2a3040;
    border-radius: 8px;
    padding: 10px 16px;
    text-align: center;
    flex: 1; min-width: 90px;
}
.seg-block .seg-val {
    font-family: 'DM Mono', monospace;
    font-size: 1rem;
    font-weight: 500;
    color: #00e5b0;
}
.seg-block .seg-key {
    font-family: 'DM Mono', monospace;
    font-size: 0.55rem;
    letter-spacing: 2px;
    color: #3d4452;
    text-transform: uppercase;
    margin-top: 4px;
}
.address-line {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.88rem;
    color: #7a8090;
    line-height: 1.6;
}
.div-line {
    border: none;
    border-top: 1px solid #1e2430;
    margin: 22px 0;
}
.footer-stamp {
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 3px;
    color: #2a3040;
    text-align: center;
    margin-top: 3rem;
    text-transform: uppercase;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  DATA MODEL
# ─────────────────────────────────────────────
class Employee:
    def __init__(self, first_name, last_name, age,
                 position, salary, years_experience,
                 address_line1, address_line2, employee_code):
        self.first_name       = first_name
        self.last_name        = last_name
        self.full_name        = first_name + ' ' + last_name
        self.age              = age
        self.position         = position
        self.salary           = salary
        self.years_experience = years_experience
        self.address          = address_line1 + ', ' + address_line2
        self.employee_code    = employee_code
        self.department       = employee_code[0:3]
        self.year_code        = employee_code[4:8]
        self.initials         = employee_code[9:11]
        self.serial           = employee_code[-3:]

    def summary(self):
        return (f"{self.full_name} is {self.age} years old | "
                f"{self.position} | ${self.salary:,} | "
                f"{self.years_experience} yrs exp")


# ─────────────────────────────────────────────
#  SESSION STATE
# ─────────────────────────────────────────────
if "show_profile" not in st.session_state:
    st.session_state.show_profile = False

if "emp_data" not in st.session_state:
    st.session_state.emp_data = {}

# ─────────────────────────────────────────────
#  HEADER
# ─────────────────────────────────────────────
st.markdown('<div class="hero-title">EMPLOYEE</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Profile Generator · Python Strings Demo</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  SHOW FORM
# ─────────────────────────────────────────────
if not st.session_state.show_profile:

    st.markdown("""
    <div class="emp-card" style="margin-bottom:24px;">
        <div class="sec-label">Enter Employee Details</div>
        <div style="font-family:'DM Sans',sans-serif;font-size:0.85rem;color:#5a6070;">
            Fill in all fields below, then click Generate Profile.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        first_name    = st.text_input("First Name",    placeholder="e.g. John")
        age           = st.text_input("Age",           placeholder="e.g. 28")
        salary        = st.text_input("Salary ($)",    placeholder="e.g. 75000")
        address_line1 = st.text_input("Address Line 1",placeholder="e.g. 123 Main Street")

    with col2:
        last_name        = st.text_input("Last Name",        placeholder="e.g. Doe")
        position         = st.text_input("Position",         placeholder="e.g. Data Analyst")
        years_experience = st.text_input("Years Experience", placeholder="e.g. 5")
        address_line2    = st.text_input("Address Line 2",   placeholder="e.g. Apartment 4B")

    employee_code = st.text_input("Employee Code", placeholder="e.g. DEV-2026-JD-001")

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🪪 Generate Profile", use_container_width=True):
        errors = []

        if not first_name.strip():
            errors.append("First Name is required.")
        if not last_name.strip():
            errors.append("Last Name is required.")
        if not age.strip() or not age.strip().isdigit():
            errors.append("Age must be a number.")
        if not salary.strip() or not salary.strip().isdigit():
            errors.append("Salary must be a number.")
        if not years_experience.strip() or not years_experience.strip().isdigit():
            errors.append("Years Experience must be a number.")
        if not position.strip():
            errors.append("Position is required.")
        if not employee_code.strip() or len(employee_code.strip()) < 12 or employee_code.strip().count('-') < 3:
            errors.append("Employee Code must be like: DEV-2026-JD-001")

        if errors:
            for e in errors:
                st.error(f"⚠️ {e}")
        else:
            st.session_state.emp_data = {
                "first_name":       first_name.strip(),
                "last_name":        last_name.strip(),
                "age":              int(age.strip()),
                "position":         position.strip(),
                "salary":           int(salary.strip()),
                "years_experience": int(years_experience.strip()),
                "address_line1":    address_line1.strip() or "N/A",
                "address_line2":    address_line2.strip() or "",
                "employee_code":    employee_code.strip(),
            }
            st.session_state.show_profile = True
            st.rerun()

# ─────────────────────────────────────────────
#  SHOW PROFILE
# ─────────────────────────────────────────────
else:
    d = st.session_state.emp_data

    emp = Employee(
        d["first_name"], d["last_name"], d["age"],
        d["position"], d["salary"], d["years_experience"],
        d["address_line1"], d["address_line2"], d["employee_code"]
    )

    # Sidebar
    with st.sidebar:
        st.markdown("### 👤 Profile Active")
        st.markdown(f"**{emp.full_name}**")
        st.markdown(f"`{emp.employee_code}`")
        st.markdown("---")
        if st.button("✏️ Edit Profile", use_container_width=True):
            st.session_state.show_profile = False
            st.rerun()

    # Card 1: Identity
    st.markdown(f"""
    <div class="emp-card">
        <div class="sec-label">Identity</div>
        <div class="name-banner">{emp.full_name.upper()}</div>
        <div class="code-pill">{emp.employee_code}</div>
        <div class="address-line">📍 {emp.address}</div>
    </div>
    """, unsafe_allow_html=True)

    # Card 2: Stats
    st.markdown(f"""
    <div class="emp-card">
        <div class="sec-label">Overview</div>
        <div class="stat-grid">
            <div class="stat-box">
                <div class="accent-dot"></div>
                <div class="val">{emp.age}</div>
                <div class="lbl">Age</div>
            </div>
            <div class="stat-box">
                <div class="accent-dot"></div>
                <div class="val">{emp.years_experience}Y</div>
                <div class="lbl">Experience</div>
            </div>
            <div class="stat-box">
                <div class="accent-dot"></div>
                <div class="val">${emp.salary // 1000}K</div>
                <div class="lbl">Salary / yr</div>
            </div>
        </div>
        <hr class="div-line">
        <div class="address-line">💼 {emp.position}</div>
    </div>
    """, unsafe_allow_html=True)

    # Card 3: Code Breakdown
    st.markdown(f"""
    <div class="emp-card">
        <div class="sec-label">Code Breakdown · String Slicing</div>
        <div style="font-family:'DM Mono',monospace;font-size:0.75rem;color:#5a6070;margin-bottom:8px;">
            "{emp.employee_code}"
        </div>
        <div class="code-seg">
            <div class="seg-block">
                <div class="seg-val">{emp.department}</div>
                <div class="seg-key">[0:3] Dept</div>
            </div>
            <div class="seg-block">
                <div class="seg-val">{emp.year_code}</div>
                <div class="seg-key">[4:8] Year</div>
            </div>
            <div class="seg-block">
                <div class="seg-val">{emp.initials}</div>
                <div class="seg-key">[9:11] Initials</div>
            </div>
            <div class="seg-block">
                <div class="seg-val">{emp.serial}</div>
                <div class="seg-key">[-3:] Serial</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Summary expander
    with st.expander("📋 Full Summary String (f-string output)"):
        st.code(emp.summary(), language="text")

    # Footer
    st.markdown(
        f'<div class="footer-stamp">Generated · {emp.employee_code} · Python String Operations</div>',
        unsafe_allow_html=True
    )