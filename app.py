
import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Vũng Tàu Travel",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- DATA ----------
TOURS = {
    "Vũng Tàu 1 ngày – Biển, Núi & Thành phố": {
        "price_adult": 450000,
        "price_child": 300000,
        "image": "https://images.unsplash.com/photo-1583417319070-4a69db38a482?auto=format&fit=crop&w=1200&q=80",
        "schedule": [
            "07:00 – Đón khách tại điểm hẹn",
            "08:00 – Tham quan Tượng Chúa Kitô Vua",
            "10:00 – Bãi Sau, tự do chụp ảnh và vui chơi",
            "11:30 – Ăn trưa",
            "13:00 – Bạch Dinh",
            "15:00 – Mũi Nghinh Phong",
            "16:30 – Khởi hành về điểm trả khách",
        ],
        "description": "Hành trình khám phá những điểm nổi bật của Vũng Tàu trong một ngày."
    },
    "Vũng Tàu 2 ngày 1 đêm – Trải nghiệm biển": {
        "price_adult": 1250000,
        "price_child": 850000,
        "image": "https://images.unsplash.com/photo-1559592413-7cec4d0cae2b?auto=format&fit=crop&w=1200&q=80",
        "schedule": [
            "Ngày 1: Đón khách – Bãi Sau – ăn trưa – Bạch Dinh – Mũi Nghinh Phong",
            "Buổi tối: Tự do khám phá thành phố biển",
            "Ngày 2: Ăn sáng – tham quan Núi Lớn – mua đặc sản",
            "11:30 – Ăn trưa và trả phòng",
            "14:00 – Khởi hành về điểm trả khách",
        ],
        "description": "Phù hợp cho gia đình, nhóm bạn và đoàn lớp muốn có thêm thời gian nghỉ dưỡng."
    },
    "Vũng Tàu – Hồ Tràm 2 ngày 1 đêm": {
        "price_adult": 1650000,
        "price_child": 1100000,
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80",
        "schedule": [
            "Ngày 1: Đón khách – Vũng Tàu – ăn trưa – tham quan thành phố",
            "15:00 – Di chuyển đến Hồ Tràm",
            "18:00 – Nhận phòng và tự do nghỉ ngơi",
            "Ngày 2: Ăn sáng – vui chơi biển – ăn trưa",
            "14:00 – Khởi hành về Vũng Tàu và trả khách",
        ],
        "description": "Kết hợp tham quan Vũng Tàu và nghỉ dưỡng tại khu vực Hồ Tràm."
    }
}

# ---------- STYLE ----------
st.markdown("""
<style>
    .main {
        background: #f7fbff;
    }
    .hero {
        padding: 2.2rem;
        border-radius: 22px;
        background: linear-gradient(120deg, #0077b6, #00b4d8);
        color: white;
        margin-bottom: 1.5rem;
    }
    .hero h1 {
        font-size: 3rem;
        margin-bottom: .5rem;
    }
    .hero p {
        font-size: 1.15rem;
    }
    .tour-card {
        padding: 1rem;
        border: 1px solid #dceaf2;
        border-radius: 18px;
        background: white;
        min-height: 260px;
        box-shadow: 0 5px 18px rgba(0,0,0,.05);
    }
    .price {
        font-size: 1.25rem;
        font-weight: 700;
        color: #0077b6;
    }
    .small-muted {
        color: #667085;
        font-size: .9rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div class="hero">
    <h1>🌊 Vũng Tàu Travel</h1>
    <p>Khám phá thành phố biển – Đặt tour nhanh chóng, đơn giản và thuận tiện.</p>
</div>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.header("🔎 Tìm tour")
    selected_tour = st.selectbox("Chọn chương trình", list(TOURS.keys()))
    st.divider()
    st.markdown("### 📞 Liên hệ")
    st.write("☎️ 0900 123 456")
    st.write("📧 vungtautravel@gmail.com")
    st.write("📍 Vũng Tàu, Bà Rịa – Vũng Tàu")

tour = TOURS[selected_tour]

# ---------- TOUR DETAIL ----------
left, right = st.columns([1.35, 1])

with left:
    st.image(tour["image"], use_container_width=True)

with right:
    st.subheader(selected_tour)
    st.write(tour["description"])
    st.markdown(
        f'<div class="price">Người lớn: {tour["price_adult"]:,}đ/người</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="price">Trẻ em: {tour["price_child"]:,}đ/người</div>',
        unsafe_allow_html=True
    )

st.divider()

st.subheader("🗺️ Lịch trình")
for item in tour["schedule"]:
    st.write("• " + item)

st.divider()

# ---------- REGISTRATION ----------
st.subheader("📝 Đăng ký tour")

with st.form("tour_registration"):
    c1, c2 = st.columns(2)

    with c1:
        full_name = st.text_input("Họ và tên *")
        phone = st.text_input("Số điện thoại *")
        email = st.text_input("Email")
        departure_date = st.date_input(
            "Ngày khởi hành *",
            min_value=date.today()
        )

    with c2:
        adults = st.number_input("Số người lớn", min_value=1, max_value=100, value=1)
        children = st.number_input("Số trẻ em", min_value=0, max_value=100, value=0)
        pickup = st.text_input("Điểm đón")
        note = st.text_area("Ghi chú / yêu cầu đặc biệt")

    submitted = st.form_submit_button("🚀 GỬI ĐĂNG KÝ", use_container_width=True)

# ---------- RESULT ----------
if submitted:
    if not full_name.strip() or not phone.strip():
        st.error("Vui lòng nhập đầy đủ họ tên và số điện thoại.")
    else:
        total = adults * tour["price_adult"] + children * tour["price_child"]

        st.success("🎉 Đăng ký tour thành công!")

        st.markdown("### 📋 Thông tin đăng ký")
        result_col1, result_col2 = st.columns(2)

        with result_col1:
            st.write(f"**Khách hàng:** {full_name}")
            st.write(f"**Điện thoại:** {phone}")
            st.write(f"**Email:** {email if email else 'Chưa cung cấp'}")
            st.write(f"**Tour:** {selected_tour}")

        with result_col2:
            st.write(f"**Ngày khởi hành:** {departure_date.strftime('%d/%m/%Y')}")
            st.write(f"**Người lớn:** {adults}")
            st.write(f"**Trẻ em:** {children}")
            st.write(f"**Điểm đón:** {pickup if pickup else 'Chưa cung cấp'}")

        st.info(f"💰 **Tổng tạm tính: {total:,} VNĐ**")

        if note:
            st.write(f"**Ghi chú:** {note}")

        st.warning(
            "Đây là bản demo đăng ký tour. Để sử dụng thực tế, "
            "có thể kết nối dữ liệu với Google Sheets, Firebase, Supabase "
            "hoặc cơ sở dữ liệu riêng."
        )

# ---------- FOOTER ----------
st.divider()
st.caption("© 2026 Vũng Tàu Travel | Web app đăng ký tour du lịch")
