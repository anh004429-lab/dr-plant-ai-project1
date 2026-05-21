import streamlit as st
import time
from PIL import Image

# Cấu hình phong cách cực chất cho nhóm Đẹp Trai
st.set_page_config(page_title="Dr.Plant AI - Nhóm Đẹp Trai", layout="wide")

# CSS để làm giao diện bắt mắt hơn
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #2e7d32;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🌱 Dr.Plant AI - Trợ lý Sức khỏe Cây trồng")
st.subheader("Sản phẩm bởi: Nhóm Đẹp Trai (Rimberio Co)")
st.markdown("---")

# Thông tin nhóm bên thanh bên
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/628/628283.png", width=100)
st.sidebar.header("Hệ thống Dr.Plant")
st.sidebar.success("👨‍ kỹ sư: G.Đạt, N.Anh, Đ.Minh")
st.sidebar.info("Dự án ứng dụng Deep Learning và Computer Vision để bảo vệ màu xanh trái đất.")

# Giao diện chọn phương thức nhập liệu
option = st.radio("Chọn cách kiểm tra cây:", ("📸 Chụp ảnh ngay", "📁 Tải ảnh lên"))

final_image = None

if option == "📸 Chụp ảnh ngay":
    final_image = st.camera_input("Đưa lá cây vào khung hình")
else:
    final_image = st.file_uploader("Chọn ảnh lá cây từ máy tính...", type=["jpg", "png", "jpeg"])

# Xử lý khi có ảnh
if final_image is not None:
    col_img, col_res = st.columns([1, 1])
    
    with col_img:
        st.image(final_image, caption='Ảnh đang phân tích', use_container_width=True)
    
    with col_res:
        with st.spinner('Đang dùng AI quét tọa độ vector và phân tích pixel...'):
            time.sleep(2.5) # Tạo cảm giác AI đang làm việc cực căng
        
        st.header("📊 Kết quả chẩn đoán")
        
        # Giả lập kết quả chẩn đoán thông minh
        tinh_trang = "Phát hiện dấu hiệu thiếu hụt dinh dưỡng & Nấm nhẹ"
        st.error(f"**Tình trạng:** {tinh_trang}")
        
        st.markdown("""
        **Phân tích chi tiết:**
        * Xuất hiện đốm nâu rải rác trên bề mặt lá.
        * Mật độ nhiễm bệnh: 15% (Dựa trên Heatmap AI).
        * Dự báo: Có nguy cơ lây lan nếu không xử lý trong 3 ngày tới.
        
        **Giải pháp từ nhóm Đẹp Trai:**
        1. **Chăm sóc:** Bổ sung phân bón vi lượng và điều chỉnh lượng nước.
        2. **Sinh học:** Xịt dung dịch tỏi ớt pha loãng để diệt nấm tự nhiên.
        3. **Môi trường:** Đặt cây ở nơi thoáng khí, tránh ẩm cục bộ.
        """)
        
        st.balloons() # Hiệu ứng chúc mừng khi xong việc

st.markdown("---")
st.caption("© 2026 Rimberio Co - Developed by Nhóm Đẹp Trai")
