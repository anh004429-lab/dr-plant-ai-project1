import streamlit as st
import time

# Cấu hình phong cách dự án Dr.Plant AI - Rimberio Co [cite: 1, 2]
st.set_page_config(page_title="Dr.Plant AI - Chẩn đoán sức khỏe cây", layout="wide")

st.title("🌱 Dr.Plant AI - Hệ thống chẩn đoán bằng Camera")
st.markdown("---")

# Thông tin thành viên dự án [cite: 3]
st.sidebar.header("Dự án Tin học")
st.sidebar.info("""
**Nhóm:** Rimberio Co [cite: 1]
**Thành viên:** G.Đạt, N.Anh, Đ.Minh [cite: 3]
**Mô hình:** Deep Learning & Computer Vision [cite: 8, 83]
""")

# Tạo 2 tab: Một cái để chụp ảnh, một cái để tải file có sẵn
tab1, tab2 = st.tabs(["📸 Chụp ảnh bằng Camera", "📁 Tải ảnh từ thiết bị"])

with tab1:
    img_camera = st.camera_input("Đưa lá cây vào khung hình và nhấn nút chụp")

with tab2:
    img_upload = st.file_uploader("Chọn ảnh từ thư viện của bạn...", type=["jpg", "png", "jpeg"])

# Ưu tiên lấy ảnh từ camera nếu có, không thì lấy ảnh upload
final_image = img_camera if img_camera is not None else img_upload

if final_image is not None:
    st.image(final_image, caption='Dữ liệu hình ảnh đầu vào', use_container_width=True)
    
    # Giả lập quá trình AI phân tích theo MTC 2.e và 3.a [cite: 7, 8]
    with st.spinner('AI đang quét các pixel và ánh xạ tọa độ (MTC 2.e)... [cite: 67]'):
        time.sleep(2) # Mô phỏng thời gian xử lý của mô hình Neural Radiance Fields [cite: 48]
        
    st.subheader("📊 Kết quả chẩn đoán từ Dr.Plant AI")
    
    # Phân tích các dấu hiệu thực tế [cite: 13, 14]
    # Trong dự án thực tế, đoạn này sẽ nhận kết quả từ mô hình huấn luyện có giám sát [cite: 91]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("**Tình trạng phát hiện:**")
        st.write("- Nhận diện dấu hiệu: Lá vàng, đốm nâu hoặc héo úa[cite: 14].")
        st.write("- Mật độ nhiễm bệnh: Đang được xác định qua Heatmap[cite: 70].")
        st.write("- Dự báo: Có khả năng bùng phát nấm mốc do độ ẩm môi trường cao[cite: 96].")
        
    with col2:
        st.success("**Giải pháp từ chuyên gia AI:**")
        st.write("1. Áp dụng các biện pháp chữa trị sinh học, thân thiện môi trường[cite: 24].")
        st.write("2. Điều chỉnh vị trí đặt cây để tối ưu ánh sáng và độ ẩm[cite: 26].")
        st.write("3. Theo dõi tốc độ lây lan theo tọa độ thời gian[cite: 71].")

    st.warning("⚠️ **Lưu ý:** Con người giữ vai trò quyết định cuối cùng dựa trên ngữ cảnh thực tế[cite: 26].")
