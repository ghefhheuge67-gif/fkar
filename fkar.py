import streamlit as st

st.set_page_config( page_title="المهندس ذو الفقار صادق | الأمن السيبراني", page_icon="🛡️",
    layout="centered"
)

# 2. كود التصميم السايبيري والتحركات والألوان (CSS)
st.markdown("""
    <style>
    /* تهيئة الصفحة بالكامل باللون الداكن الفخم */
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #060713 !important;
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl;
        text-align: right;
    }
    
    /* إخفاء القوائم الافتراضية لتبدو كصفحة ويب مستقلة ومحترفة */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* تحسين شكل الحاوية الرئيسية */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }

    /* تأثيرات الحركة والأنيميشن */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes glow {
        0% { border-color: #4f46e5; box-shadow: 0 0 10px rgba(79, 70, 229, 0.2); }
        50% { border-color: #06b6d4; box-shadow: 0 0 20px rgba(6, 182, 212, 0.6); }
        100% { border-color: #4f46e5; box-shadow: 0 0 10px rgba(79, 70, 229, 0.2); }
    }

    /* تصميم ترحيب الصفحة الأولى */
    .welcome-box {
        background: linear-gradient(135deg, #10122c, #090a1a);
        border: 2px solid #4f46e5;
        border-radius: 24px;
        padding: 40px;
        text-align: center;
        animation: fadeIn 1s ease-out, glow 4s infinite;
        margin-bottom: 30px;
    }
    
    .welcome-title {
        color: #ffffff;
        font-size: 32px;
        font-weight: 900;
        margin-bottom: 15px;
        background: linear-gradient(90deg, #06b6d4, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* تصميم بطاقات المعلومات والمنشورات */
    .cyber-card {
        background: rgba(16, 18, 44, 0.7);
        border: 1px solid #1e2246;
        border-radius: 20px;
        padding: 30px;
        margin-top: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        animation: fadeIn 1.2s ease-out;
        transition: all 0.4s ease;
    }
    
    .cyber-card:hover {
        transform: translateY(-5px) scale(1.01);
        border-color: #a855f7;
        box-shadow: 0 15px 35px rgba(168, 85, 247, 0.2);
    }

    .section-headline {
        font-size: 24px;
        font-weight: 700;
        color: #06b6d4;
        border-bottom: 2px solid #1e2246;
        padding-bottom: 10px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
    }

    .article-text {
        color: #b4b9e2;
        font-size: 16px;
        line-height: 1.8;
        text-align: justify;
    }

    .highlight-text {
        color: #a855f7;
        font-weight: bold;
    }

    /* ستايل الأزرار التفاعلية */
    .stButton>button {
        background: linear-gradient(90deg, #4f46e5, #a855f7) !important;
        color: white !important;
        border: none !important;
        padding: 12px 28px !important;
        border-radius: 12px !important;
        font-size: 16px !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.4) !important;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: scale(1.02) !important;
        box-shadow: 0 6px 25px rgba(6, 182, 212, 0.6) !important;
        background: linear-gradient(90deg, #06b6d4, #4f46e5) !important;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- الصفحة الأولى: رابط الترحيب -----------------
# نستخدم حيلة ذكية بالبايثون لعمل صفحات متعددة بضغطة زر تنبض بالحياة

if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

if st.session_state.page == 'welcome':
    st.write("") # مساحة علوية
    st.write("")
    # صندوق الترحيب الاحترافي اللامع
    st.markdown("""
    <div class="welcome-box">
        <div style="font-size: 60px; margin-bottom: 10px;">🛡️</div>
        <div class="welcome-title">مرحباً بكم في صفحة المهندس ذو الفقار صادق</div>
        <p style="color: #8a8fbc; font-size: 16px; max-width: 400px; margin: 0 auto 25px auto;">
            منصة رقمية تستعرض آفاق الحماية الرقمية، أمن البيانات، ومواجهة التهديدات السيبرانية في العصر الحديث.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # زر الانتقال التفاعلي للانتقال لصفحة التعريف
    st.write("اضغط أدناه لفتح البوابة الرقمية والدخول إلى الموقع المطور:")
    if st.button("دخول إلى صفحة المهندس ذو الفقار 🚀"):
        st.session_state.page = 'profile'
        st.rerun()

# ----------------- الصفحة الثانية: صفحة المهندس والمقالة -----------------
elif st.session_state.page == 'profile':
    
    # زر العودة السريع المتناسق
    if st.button("⬅️ العودة لصفحة الترحيب"):
        st.session_state.page = 'welcome'
        st.rerun()

    # بطاقة التعريف بالمهندس ذو الفقار صادق
    st.markdown("""
    <div class="cyber-card">
        <div class="section-headline">👨‍💻 نبذة عن المهندس ذو الفقار صادق</div>
        <div class="article-text">
            يبرز اسم <span class="highlight-text">المهندس ذو الفقار صادق</span> كأحد العقول الشابة والمتميزة في ميدان التكنولوجيا الحديثة، حيث اختار أن يكون في خط الدفاع الأول لعالمنا الرقمي كـ <b>مهندس تقنيات أمن سيبراني</b>. 
            <br><br>
            يجمع المهندس ذو الفقار بين الشغف البرمجي العميق والنظرة الاستراتيجية الثاقبة في تحليل الثغرات وحماية الشبكات. لا يقتصر دوره على كتابة الأكواد فحسب، بل يمتد إلى بناء بيئات رقمية محصنة تعتمد على أحدث معايير التشفير وأنظمة كشف التسلل، مؤمناً بأن الأمن الرقمي ليس مجرد جدار حماية، بل هو الركيزة الأساسية لاستمرار وتطور التكنولوجيا في عالمنا المعاصر.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # بطاقة التعريف باختصاص هندسة تقنيات الأمن السيبراني
    st.markdown("""
    <div class="cyber-card">
        <div class="section-headline">🌐 ما هي هندسة تقنيات الأمن السيبراني؟</div>
        <div class="article-text">
            إن تخصص <span class="highlight-text">هندسة تقنيات الأمن السيبراني (Cybersecurity Engineering)</span> هو الفن والعلم المسؤول عن حماية الأنظمة، الشبكات، البرامج، والهواتف من الهجمات الرقمية الخبيثة. 
            <br><br>
            في هذا التخصص، يتم تدريب المهندسين ليكونوا بمثابة "المعاريين البرمجيين والشرطة السرية" للإنترنت، حيث تشمل مهامهم الأساسية:
            <br>
            • <b>اختبار الاختراق (Penetration Testing):</b> التفكير كالمخترقين لاكتشاف نقاط الضعف قبل استغلالها. <br>
            • <b>التشفير وحماية البيانات:</b> تحويل البيانات الحساسة إلى رموز معقدة يستحيل فكها. <br>
            • <b>الاستجابة للحوادث الرقمية:</b> التدخل الفوري لإيقاف الهجمات وتحليل الأدلة الجنائية الرقمية.
            <br><br>
            مع تسارع التحول الرقمي، أصبح هذا الاختصاص هو العصب المحرك لأمان الشركات، البنوك، والحكومات حول العالم.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # تذييل الصفحة اللطيف
    st.markdown("<p style='text-align: center; color: #4f46e5; margin-top: 30px; font-weight: bold;'>تَمَّت البرمجة والتصميم بكل فخر بواسطة بايثون و ذو الفقار صادق ⚙️</p>", unsafe_allow_html=True)