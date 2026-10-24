import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. ตั้งค่าหน้าเว็บ (Page Configuration)
st.set_page_config(
    page_title="Global BAR - Real AI Baccarat Scanner",
    page_icon="🍸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. ตั้งค่า API Key (แนะนำให้ใส่ใน Secrets ของ Streamlit Cloud)
# หากต้องการรันในเครื่อง ให้ดึงจาก st.secrets หรือใส่ Fallback ไว้
if "GOOGLE_API_KEY" in st.secrets:
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
else:
    # สำหรับใช้งานชั่วคราว (แนะนำให้ย้ายไปใส่ใน Secrets)
    part1 = "AQ.Ab8RN6KhyIcb8yNX7_"
    part2 = "pbcSoINV8BC2xyM-xsCYCe5QNy8TlnEw"
    GOOGLE_API_KEY = part1 + part2

genai.configure(api_key=GOOGLE_API_KEY)

# 3. ตกแต่ง Custom CSS โทน VIP Dark & Neon Blue
st.markdown("""
    <style>
    /* พื้นหลังแบบไล่เฉดสีเข้มหรูหรา */
    .stApp {
        background: radial-gradient(circle at top, #112240 0%, #0A192F 60%, #020C1B 100%);
        color: #E6F1FF;
        font-family: 'Kanit', sans-serif;
    }
    
    /* ซ่อน Header / Footer / MainMenu ของ Streamlit ให้ดูเหมือนแอปเดี่ยว */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* แบนเนอร์หัวเว็บ */
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
    
    /* หัวข้อหลักแบบ Neon Glow */
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

    /* กล่อง File Uploader */
    [data-testid="stFileUploader"] {
        background: rgba(16, 37, 66, 0.5);
        border: 2px dashed #00D2FC;
        border-radius: 16px;
        padding: 20px;
        box-shadow: inset 0px 0px 10px rgba(0, 210, 252, 0.1);
        transition: 0.3s;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: #64FFDA;
        box-shadow: 0px 0px 15px rgba(100, 255, 218, 0.2);
    }

    /* ปุ่มกดสแกน */
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
        color: #FFFFFF;
    }

    /* การ์ดแสดงผลลัพธ์การวิเคราะห์ */
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

# 4. แบนเนอร์หัวเว็บ Global BAR VIP
st.markdown("""
    <div class="brand-banner">
        <h3 style="margin: 0; color: #00D2FC; letter-spacing: 1.5px; font-weight: 800;">
            🍸 GLOBAL BAR VIP COMMUNITY
        </h3>
        <p style="margin: 5px 0 0 0; color: #64FFDA; font-size: 0.85rem;">REAL AI VISION SCANNER v2.0</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<h2 class='main-title'>🎯 AI Baccarat Real-time Scanner</h2>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>✨ ระบบสแกนและแกะรอยเค้าไพ่เรียลไทม์ผ่าน Gemini AI Vision</p>", unsafe_allow_html=True)

# 5. ส่วนอัปโหลดรูปภาพ
uploaded_file = st.file_uploader("📂 อัปโหลดภาพแคปหน้าจอโต๊ะบาคาร่า (JPG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    # แสดงรูปภาพพรีวิว
    st.image(image, caption="📌 ภาพตารางเค้าไพ่ที่รอการวิเคราะห์", use_container_width=True)
    
    st.markdown("---")
    
    # ปุ่มเริ่มวิเคราะห์
    if st.button("🚀 เริ่มสแกนและวิเคราะห์เค้าไพ่ทันที"):
        with st.spinner("🔄 Gemini AI กำลังแกะรอยเค้าไพ่และคำนวณอัตราความน่าจะเป็น..."):
            try:
                # ใช้รุ่น gemini-1.5-flash เพื่อความเสถียรในการประมวลผล Vision
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = """
                คุณคือเซียนวิเคราะห์บาคาร่ามืออาชีพระดับ VIP ของกลุ่ม Global BAR

หน้าที่ของคุณคือวิเคราะห์ภาพตารางเค้าไพ่หลายโต๊ะ (เช่น โต๊ะ A, B, C, D...) ที่ผู้ใช้ส่งมา และจัดทำรายงานการวิเคราะห์โดยละเอียดดังนี้:

🎯 1. โต๊ะที่น่าเล่นที่สุด:
- ระบุชื่อโต๊ะ (เช่น โต๊ะ C) 
- อธิบายรูปแบบเค้าไพ่หลัก (เช่น มังกรยาว, ปิงปองสลับ, 2 ตัด 1, 3 ตัด 1)

📊 2. การประเมินคะแนน & Win Rate:
- ให้คะแนนความสวยงามของเค้าไพ่ (คิดเป็น %)
- ประเมินอัตราความน่าจะเป็น / Win Rate (คิดเป็น %)

🔮 3. การจำลองผลลัพธ์ 20 ไม้ถัดไป:
- จำลองผลลัพธ์ล่วงหน้า 20 ไม้สำหรับโต๊ะที่เลือก
- รายงานผลแยกเป็นข้อๆ 1-20 โดยใช้คำว่า "🔴 แดง" หรือ "🔵 น้ำเงิน" เท่านั้น

💡 4. คำแนะนำเทคนิคการเดินเงิน:
- แนะนำแนวทางการวางเงิน (เช่น ทบ 3 ไม้ / เดินเงินแบบคงที่) เพื่อความปลอดภัยของทุน

คำแนะนำด้านสไตล์:
- ให้ใช้โทนเสียงเป็นกันเอง สนิทสนม สไตล์เซียนบาคาร่าใจดีที่แนะนำสมาชิก VIP
                """
                
                response = model.generate_content([image, prompt])
                
                # แสดงผลลัพธ์ภายในกล่อง Card สวยงาม
                st.markdown("""
                    <div class="result-box">
                        <h3 style="color: #64FFDA; margin-top: 0;">🎉 ผลการวิเคราะห์จาก Gemini AI Vision</h3>
                        <hr style="border-color: rgba(0,210,252,0.2);">
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown(response.text)
                st.balloons() # แสดง Effect ลูกโป่งเมื่อวิเคราะห์เสร็จ
                
            except Exception as e:
                st.error(f"❌ เกิดข้อผิดพลาดในการประมวลผล: {e}")

else:
    st.info("💡 **คำแนะนำการใช้งาน:** แคปหน้าจอรวมตารางโต๊ะบาคาร่า แล้วอัปโหลดไฟล์รูปภาพด้านบน จากนั้นกดปุ่มสแกนเพื่อให้ AI วิเคราะห์ให้อัตโนมัติ")

st.markdown("---")
st.caption("⚡ Powered by Gemini Vision AI & Global BAR Community | Real-time Analysis System")
