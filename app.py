import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# 1. ตั้งค่าหน้าเว็บ (Page Configuration)
st.set_page_config(
    page_title="Global BAR - Real AI Baccarat Scanner",
    page_icon="🍸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 🔒 ระบบตรวจสอบรหัสผ่าน (Password Protection)
# ==========================================
def check_password():
    """Returns True if the user entered the correct password."""
    def password_entered():
        # ตั้งค่ารหัสผ่านที่คุณต้องการตรงนี้ (สามารถเปลี่ยนได้ตามใจชอบ)
        if st.session_state["password"] == "globalbar2026":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # ลบรหัสออกจาก session เพื่อความปลอดภัย
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # หน้าต่างกรอกรหัสครั้งแรก
        st.markdown("<h2 style='text-align: center; color: #00D2FC;'>🔒 Global BAR VIP Security</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #8892B0;'>กรุณาใส่รหัสผ่านเพื่อเข้าใช้งานระบบสแกน</p>", unsafe_allow_html=True)
        st.text_input("รหัสผ่าน (Password)", type="password", on_change=password_entered, key="password")
        return False
        
    elif not st.session_state["password_correct"]:
        # กรณีใส่รหัสผิด
        st.markdown("<h2 style='text-align: center; color: #00D2FC;'>🔒 Global BAR VIP Security</h2>", unsafe_allow_html=True)
        st.text_input("รหัสผ่าน (Password)", type="password", on_change=password_entered, key="password")
        st.error("❌ รหัสผ่านไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง")
        return False
        
    else:
        # ถ้ารหัสถูกต้อง อนุญาตให้เข้าแอป
        return True

# ทำการเช็ครหัสผ่านก่อน หากผ่านถึงจะรันโค้ดด้านล่างทั้งหมด
if check_password():

    # 2. ตั้งค่า API Key
    if "GOOGLE_API_KEY" in st.secrets:
        GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
    else:
        part1 = "AQ.Ab8RN6KhyIcb8yNX7_"
        part2 = "pbcSoINV8BC2xyM-xsCYCe5QNy8TlnEw"
        GOOGLE_API_KEY = part1 + part2

    genai.configure(api_key=GOOGLE_API_KEY)

    # 3. ตกแต่ง Custom CSS โทน VIP Dark & Neon Blue
    st.markdown("""
        <style>
        .stApp {
            background: radial-gradient(circle at top, #112240 0%, #0A192F 60%, #020C1B 100%);
            color: #E6F1FF;
            font-family: 'Kanit', sans-serif;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .brand-banner {
            background: linear-gradient(135deg, rgba(31, 78, 121, 0.6) 0%, rgba(15, 37, 55, 0.8) 100%);
            border: 1px solid #00D2FC;
            box-shadow: 0px 0px 15px rgba(0, 210, 252, 0.3);
            padding: 15px 20px;
            border-radius: 16px;
            text-align: center;
            margin-bottom: 25px;
            backdrop-filter: blur(5px);
        }
        
        .main-title {
            color: #00D2FC;
            text-shadow: 0px 0px 18px rgba(0, 210, 252, 0.6);
            text-align: center;
            font-weight: 700;
            margin-bottom: 10px;
        }
        
        .sub-title {
            text-align: center;
            color: #8892B0;
            font-size: 0.95rem;
            margin-bottom: 25px;
        }

        [data-testid="stFileUploader"] {
            background: rgba(16, 37, 66, 0.5);
            border: 2px dashed #00D2FC;
            border-radius: 16px;
            padding: 20px;
            box-shadow: inset 0px 0px 10px rgba(0, 210, 252, 0.1);
        }

        .stButton>button {
            background: linear-gradient(90deg, #0052D4 0%, #4364F7 50%, #6FB1FC 100%);
            color: #FFFFFF;
            font-size: 1.1rem;
            font-weight: bold;
            border-radius: 12px;
            width: 100%;
            height: 55px;
            border: none;
            box-shadow: 0px 4px 15px rgba(67, 100, 247, 0.4);
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0px 6px 20px rgba(0, 210, 252, 0.6);
        }

        .result-box {
            background: rgba(17, 34, 64, 0.75);
            border: 1px solid rgba(0, 210, 252, 0.4);
            border-radius: 16px;
            padding: 25px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            backdrop-filter: blur(8px);
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    # 4. ส่วนหัวแอป (รองรับการแสดงโลโก้ถ้ามีไฟล์ logo.png)
    if os.path.exists("logo.png"):
        col_logo, col_text = st.columns([1, 4])
        with col_logo:
            logo = Image.open("logo.png")
            st.image(logo, width=80)
        with col_text:
            st.markdown("""
                <div style="padding-top: 5px;">
                    <h3 style="margin: 0; color: #00D2FC; letter-spacing: 1.5px; font-weight: 800;">GLOBAL BAR VIP</h3>
                    <p style="margin: 2px 0 0 0; color: #64FFDA; font-size: 0.85rem;">REAL AI VISION SCANNER v2.0</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="brand-banner">
                <h3 style="margin: 0; color: #00D2FC; letter-spacing: 1.5px; font-weight: 800;">🍸 GLOBAL BAR VIP COMMUNITY</h3>
                <p style="margin: 5px 0 0 0; color: #64FFDA; font-size: 0.85rem;">REAL AI VISION SCANNER v2.0</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<h2 class='main-title'>🎯 AI Baccarat Real-time Scanner</h2>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>✨ ระบบสแกนและแกะรอยเค้าไพ่เรียลไทม์ผ่าน Gemini AI Vision</p>", unsafe_allow_html=True)

    # 5. ส่วนอัปโหลดรูปภาพ & เรียก AI
    uploaded_file = st.file_uploader("📂 อัปโหลดภาพแคปหน้าจอโต๊ะบาคาร่า (JPG, PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="📌 ภาพตารางเค้าไพ่ที่รอการวิเคราะห์", use_container_width=True)
        st.markdown("---")
        
        if st.button("🚀 เริ่มสแกนและวิเคราะห์เค้าไพ่ทันที"):
            with st.spinner("🔄 Gemini AI กำลังแกะรอยเค้าไพ่และคำนวณอัตราความน่าจะเป็น..."):
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    
                    prompt = """
                    คุณคือเซียนวิเคราะห์บาคาร่ามืออาชีพระดับ VIP ของกลุ่ม Global BAR
                    หน้าที่ของคุณคือวิเคราะห์ภาพตารางเค้าไพ่หลายโต๊ะ (เช่น โต๊ะ A, B, C, D...) ที่ผู้ใช้ส่งมา และจัดทำรายงานการวิเคราะห์ดังนี้:
                    🎯 1. โต๊ะที่น่าเล่นที่สุด: ระบุชื่อโต๊ะ พร้อมอธิบายลักษณะเค้าไพ่
                    📊 2. การประเมินคะแนน & Win Rate: ให้คะแนนความสวยงามและเปอร์เซ็นต์ความน่าจะเป็น (%)
                    🔮 3. การจำลองผลลัพธ์ 20 ไม้ถัดไป: จำลองผลลัพธ์ล่วงหน้า 20 ไม้ แยกเป็นข้อๆ โดยใช้คำว่า "🔴 แดง" หรือ "🔵 น้ำเงิน" เท่านั้น
                    💡 4. คำแนะนำการเดินเงิน: แนวทางการวางเงินเพื่อความปลอดภัย
                    โทนเสียง: เป็นกันเอง สไตล์เซียนบาคาร่าใจดีที่แนะนำสมาชิก VIP
                    """
                    
                    response = model.generate_content([image, prompt])
                    
                    st.markdown("""
                        <div class="result-box">
                            <h3 style="color: #64FFDA; margin-top: 0;">🎉 ผลการวิเคราะห์จาก Gemini AI Vision</h3>
                            <hr style="border-color: rgba(0,210,252,0.2);">
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(response.text)
                    st.balloons()
                    
                except Exception as e:
                    st.error(f"❌ เกิดข้อผิดพลาดในการประมวลผล: {e}")

    else:
        st.info("💡 **คำแนะนำ:** กรอกรหัสผ่านสำเร็จแล้ว สามารถอัปโหลดภาพตารางเค้าไพ่เพื่อเริ่มสแกนได้ทันทีครับ")

    st.markdown("---")
    st.caption("⚡ Powered by Gemini Vision AI & Global BAR Community | Real-time Analysis System")
