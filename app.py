import streamlit as st
import pandas as pd
from datetime import date
import os

# 1. Cấu hình trang
st.set_page_config(
    page_title="Vũng Tàu Travel - Đăng Ký Tour",
    page_icon="🌊",
    layout="wide"
)

# 2. Dữ liệu các tour mẫu tại Vũng Tàu
TOURS = {
    "Tour 1: Khám phá Biển & Di tích Vũng Tàu (1 Ngày)": {
        "price": 500000,
        "description": "Tham quan Tượng Chúa Kito, Ngọn Hải Đăng, Bạch Dinh, tắm biển Bãi Sau.",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600"
    },
    "Tour 2: Trải nghiệm Ẩm thực & Mũi Nghinh Phong (2 Ngày 1 Đêm)": {
        "price": 1200000,
        "description": "Thưởng thức hải sản Đêm, ngắm bình minh Mũi Nghinh Phong, trải nghiệm chèo SUP.",
        "image": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?w=600"
    },
    "Tour 3: Nghỉ dưỡng Cao cấp Long Hải - Vũng Tàu (3 Ngày 2 Đêm)": {
        "price": 2500000,
        "description": "Trọn gói Resort 4 sao, ngâm khoáng nóng Bình Châu, BBQ hải sản ven biển.",
        "image": "https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?w=600"
    }
}

# File lưu trữ dữ liệu đăng ký
DATA_FILE = "danh_sach_dang_ky.csv"

# 3. Thanh Điều Hướng Sidebar
st.sidebar.title("📌 Danh Mục")
menu = st.sidebar.radio("Chọn chức năng:", ["Trang Chủ & Danh Sách Tour", "📝 Đăng Ký Tour", "📊 Danh Sách Đã Đăng Ký"])

# HEADER
st.title("🌊 VŨNG TÀU TRAVEL")
st.caption("Hệ thống đặt tour du lịch Vũng Tàu trực tuyến nhanh chóng & tiện lợi")
st.divider()

# TAB 1: TRANG CHỦ & DANH SÁCH TOUR
if menu == "Trang Chủ & Danh Sách Tour":
    st.subheader("🌴 Các Tour Du Lịch Nổi Bật")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        search_kw = st.text_input("🔍 Tìm kiếm tour:", placeholder="Nhập tên tour hoặc từ khóa...")
    
    for tour_name, tour_info in TOURS.items():
        if search_kw.lower() in tour_name.lower() or search_kw.lower() in tour_info["description"].lower():
            with st.container():
                c1, c2 = st.columns([1, 2])
                with c1:
                    st.image(tour_info["image"], use_container_width=True)
                with c2:
                    st.markdown(f"### {tour_name}")
                    st.write(f"**Mô tả:** {tour_info['description']}")
                    st.markdown(f"**Giá tour:** <span style='color:red; font-size:18px; font-weight:bold;'>{tour_info['price']:,} VNĐ / khách</span>", unsafe_allow_html=True)
                    st.info("👉 Vào mục **'Đăng Ký Tour'** ở menu bên trái để đặt tour này.")
                st.divider()

# TAB 2: FORM ĐĂNG KÝ
elif menu == "📝 Đăng Ký Tour":
    st.subheader("📝 Form Đăng Ký Tour Du Lịch")
    
    with st.form("booking_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            full_name = st.text_input("Họ và tên *", placeholder="Nguyễn Văn A")
            phone = st.text_input("Số điện thoại *", placeholder="0901234567")
            email = st.text_input("Email", placeholder="example@gmail.com")
            
        with col2:
            selected_tour = st.selectbox("Chọn Tour du lịch *", list(TOURS.keys()))
            travel_date = st.date_input("Ngày khởi hành *", min_value=date.today())
            num_people = st.number_input("Số lượng khách *", min_value=1, max_value=50, value=1)
            
        note = st.text_area("Yêu cầu đặc biệt (nếu có):", placeholder="Ăn chay, phòng đơn, hỗ trợ đưa đón...")
        
        # TÍNH TIỀN
        unit_price = TOURS[selected_tour]["price"]
        total_price = unit_price * num_people
        
        st.markdown(f"### 💳 Tổng chi phí dự kiến: :red[{total_price:,} VNĐ]")
        
        submit_button = st.form_submit_button("✅ Xác Nhận Đăng Ký")
        
        if submit_button:
            if not full_name or not phone:
                st.error("⚠️ Vui lòng điền đầy đủ Họ tên và Số điện thoại!")
            else:
                # Lưu dữ liệu
                new_data = pd.DataFrame([{
                    "Họ tên": full_name,
                    "Số điện thoại": phone,
                    "Email": email,
                    "Tour": selected_tour,
                    "Ngày đi": str(travel_date),
                    "Số người": num_people,
                    "Tổng tiền (VNĐ)": total_price,
                    "Ghi chú": note
                }])
                
                if os.path.exists(DATA_FILE):
                    new_data.to_csv(DATA_FILE, mode='a', header=False, index=False, encoding='utf-8-sig')
                else:
                    new_data.to_csv(DATA_FILE, index=False, encoding='utf-8-sig')
                
                st.success(f"🎉 Đăng ký thành công! Cảm ơn {full_name} đã lựa chọn Vũng Tàu Travel.")
                st.balloons()

# TAB 3: QUẢN LÝ ĐƠN ĐĂNG KÝ
elif menu == "📊 Danh Sách Đã Đăng Ký":
    st.subheader("📊 Quản Lý Đơn Đăng Ký (Dành cho Giáo viên / Admin)")
    
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE, encoding='utf-8-sig')
        
        # Thống kê nhanh
        m1, m2, m3 = st.columns(3)
        m1.metric("Tổng lượt đăng ký", len(df))
        m2.metric("Tổng số khách", df["Số người"].sum() if "Số người" in df else 0)
        m3.metric("Tổng doanh thu", f"{df['Tổng tiền (VNĐ)'].sum():,} VNĐ" if "Tổng tiền (VNĐ)" in df else "0 VNĐ")
        
        st.dataframe(df, use_container_width=True)
        
        # Nút tải file CSV
        csv_data = df.to_csv(index=False, encoding='utf-8-sig')
        st.download_button(
            label="📥 Tải báo cáo CSV",
            data=csv_data,
            file_name="danh_sach_dang_ky_tour.csv",
            mime="text/csv"
        )
    else:
        st.info("Chưa có lượt đăng ký nào trong hệ thống.")
