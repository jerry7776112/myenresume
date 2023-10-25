from pathlib import Path

import streamlit as st
from PIL import Image




# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "MyCV.pdf"
profile_pic = current_dir / "assets" / "me.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Jerry Guo"
PAGE_ICON = ":wave:"
NAME = "Jerry Guo"
DESCRIPTION = """
Hi, I'm Guo Yihua, an interdisciplinary computer science student. Studying in the master class of the Department of Computer Science, Tunghai University, and the Secure Social Computing Laboratory.
"""
EMAIL = "jerry7776112@gmail.com"
SOCIAL_MEDIA = {
    "🔎LinkedIn": "https://www.linkedin.com/in/%E7%9B%8A%E8%8F%AF-yi-hua-guo-%E9%83%AD-5bba34217/",
    "🔎GitHub": "https://github.com/jerry7776112"
}
Certificate = {
    "► TUV NORD - Sustainability Management Manger(企業永續管理師)": "https://drive.google.com/file/d/1DqT6sA-XyZsDZTFxtpqv2RMCMQJdzWdr/view?usp=sharing",
    "► 2023 AIS3": "https://drive.google.com/file/d/1HOEAjDWpNBIF1rdNTN5SBQ-fcYiVcM5I/view?usp=share_link",
    "► 2021企業數據競賽": "https://drive.google.com/file/d/1WxWVO4X9hkPlcIP_Jw5WljkiceCGaSNk/view?usp=share_link",
    "► Career Essentials in Data Analysis by Microsoft and LinkedIn": "https://drive.google.com/file/d/1Vnnx_V0jHl7Kb4vOY2OLGoSzqOGVt0Px/view?usp=share_link",
    "► Career Essentials in Generative AI by Microsoft and LinkedIn": "https://drive.google.com/file/d/1Spc00dAScVEX_UvHm0Wo-S6ZXJ5WEfRx/view?usp=share_link",
    "► AWS Academy Graduate - AWS Academy Cloud Foundations": "https://drive.google.com/file/d/1a_sHHMygLk-QIQqfuWuvYvilfoajPHPe/view?usp=share_link",
    "► Great Learning - Bascis of EDA with Python": "https://drive.google.com/file/d/12mSIpCCOgC_DVB_WCP--GwxTcAjBDikZ/view?usp=share_link"
}


Awards = {
    "Session C4 : Social Media Security-Best Session Award":"https://drive.google.com/file/d/101XLGn2in1Kpse-jb0v-3Vy42Wiya0R_/view?usp=sharing",
    "Tracking of Disinformation Sources Based on Online Social Media: Examining Pages and URLs with BFS Evolution | CISC2023 第三十三屆全國資訊安全會議": "https://drive.google.com/file/d/1jsVZEON5R6CBKJqmoWwMq2LzJQdbKFFu/view?usp=share_link"

}

PROJECTS = {
    "🏆 DockerTutorial(Zero to Hero)-NOTE": "https://github.com/jerry7776112/dockerTutorial",
    "🏆 ETL 語意相似度分析": "https://github.com/jerry7776112/SemanticSimilarityETL",
    "🏆 Python & Kafka 餐點訂單分散式系統設計": "https://github.com/jerry7776112/pythonKafka",
    "🏆 SQL to Power BI Pizza銷售資料視覺化": "https://github.com/jerry7776112/SQLtoPowerBI",
    "🏆 使用pgAdmin操作Docker上的PostgreSQL": "https://github.com/jerry7776112/dockerSQLtoLocal",
    "🏆 利用AWS建立Open Weather ETL 並整合至 Apache Airflow": "https://github.com/jerry7776112/openweatherETL",
    "🏆 系統CPU & Memory監控 Flask & Docker 實作": "https://github.com/jerry7776112/pythonFlaskAppDocker",
    "🏆 資料模型設計實作": "https://github.com/jerry7776112/buildingDataModel",
    "🏆 AIS3-信用卡盜刷偵測": "https://drive.google.com/file/d/1FAm_uNvjlaySmr14Okb0yNIA9KAfXuXw/view?usp=sharing",
    "🏆 新經濟創與創新營運(創新提案)-穆斯林SuperApp": "https://drive.google.com/file/d/1wCJA2xUDWUa06Uvnt0cQZfe3AxvyCKRi/view?usp=drive_link",
    "🏆 數位科技的商業價值創造(創新提案)-虛擬生命園區平台": "https://drive.google.com/file/d/14c3jHwvgb1vwbvW_rWzbRfu2dW7X4BMp/view?usp=drive_link"
}

PUBLICATION = {
    "► Tracking of Disinformation Sources Based on Online Social Media: Examining Pages and URLs with BFS Evolution | CISC2023 第三十三屆全國資訊安全會議": "https://drive.google.com/file/d/1jsVZEON5R6CBKJqmoWwMq2LzJQdbKFFu/view?usp=share_link" ,
    "► 基於區塊鏈建立去中心化社群平台之共識演算法研析 | CISC2022 第三十二屆全國資訊安全會議": "https://drive.google.com/file/d/17BTHvmWmHHO6cFuzemgteEkjwKDbiltb/view?usp=sharing"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Research Directions")
st.write(
    """
- ✔️ Social Media Security
- ✔️ Data Mining
- ✔️ Data Engineering
- ✔️ Web System Development
- ✔️ Using heterogeneous data to analyze research topics on social platforms
- ✔️ Container Deploy
- ✔️ Cloud Application
"""
)
# Eduation
st.write('\n')
st.subheader("Eduation")
st.write("""
- 02/2022-Present   GPA: 4.12/4.30
- Tunghai University, Taichung, Taiwan Master of Engineering, Computer Science
-  (東海大學-資訊工程學系碩士)
- 06/2016-06/2020   GPA: 3.17/4.30
- Tunghai University, Taichung, Taiwan Bachelor of Engineering, Environmental Science and Engineering
-  (東海大學-環境科學與工程學系學士)
"""   
)

# CERTIFICATE
st.write('\n')
st.subheader("Certificates")
st.write("---")
for project, link in Certificate.items():
    st.write(f"[{project}]({link})")

# --- SKILLS ---
# st.subheader("Computer Skills")
# col1, col2 = st.columns(2, gap="small")
# with col1:
#     st.write(
#     """
#     - ►**Programming:** Python, R, Go
#     - ►**AI Library:** Sentence-Transformers, Scikit-learn
#     - ►**Data Processing:** Pandas, Numpy
#     - ►**ETL Tool:** Airflow, SSIS 
#     - ►**Data Visulization:** PowerBI, Plotly, Seaborn, Matplotlib
#     - ►**Social Network Visualization:** Gephi
#     - ►**Python Web Framework:** Flask
#     """
#     )
# with col2:
#     st.write(
#     """
#     - ►**Databases:** PostgresSQL, MongoDB, MySQL
#     - ►**Virtual Machine:** VirtualBox, VMware, Hyper-V
#     - ►**OS:** Windows, Linux
#     - ►**Version Control:** Git
#     - ►**Editor:** VScode, Nano, Vim
#     - ►**Scripts:** Bash
#     - ►**Cloud:** AWS
#     - ►**Container:** Docker, Kubernetes
#     """
#     )
    

st.write('\n')
st.subheader("Computer Skills")
st.write(
    """
- 👩‍💻 Programming: Python, R, Go
- 📚 AI Library: Sentence-Transformers, Scikit-learn
- 📚 Data Processing: Pandas, Numpy
- 📚 ETL Tool: Airflow, SSIS 
- 📊 Data Visulization: PowerBI, Plotly, Seaborn, Matplotlib
- 📊 Social Network Visualization: Gephi
- 📝 Python Web Framework: Flask
- 🗄️ Databases: PostgresSQL, MongoDB, MySQL
- 🗄️ Virtual Machine: VirtualBox, VMware, Hyper-V
- 🗄️ OS: Windows, Linux
- 🗄️ Version Control: Git
- 🗄️ Editor: VScode, Nano, Vim
- 🗄️ Scripts: Bash
- 🫙 Cloud: AWS
- 🫙 Container: Docker, Kubernetes
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Research Assistant - Secure Social Computing Laboratory | Department of Computer Science, Tunghai University**")
st.write("06/2023 - Present")
st.write(
    """
- ► Produced data engineering side projects, including building openweather ETL using AWS EC2 and S3 and deploying Python-Flask applications using Docker. Use Power BI to create a dynamic visual dashboard for pizza sales data.
- (製作資料工程side project，包括使用 AWS EC2 和 S3 建置 openweather ETL 以及使用 Docker 部署 Python-Flask 應用程式。 使用 Power BI 為披薩銷售資料建立動態視覺化儀表板。)
- **Skill Sets: AWS, Apache Airflow, Python, Python-Flask Framework, Makefile, Dockerfile, PostgreSQL, MongoDB, MS SQL, Power BI**
- ► Use "Tryhackme" to learn Cyber Security and obtain certificates including "Introduction to Cybersecurity", "Pre Security", "Jr Penetration Tester" and more. The skills include Network Exploitation, Web Exploitation, Linux Exploitation, Windows Exploitation, Pentesting.
- (使用「Tryhackme」進修網路安全課程並獲得包括「網路安全入門」、「進階網路安全」、「初級滲透測試員」等證書。 技能包括網路利用、Web 利用、Linux 利用、Windows 利用、滲透測試。)
- **Skill Sets: Burp Suite, Metasploit, Nmap, Nessus, Hydra**
"""
)
st.write("02/2022 - 06/2023")
st.write(""" 
- ► Collect public data from social networking platforms for big data analysis and disinformation tracking.
- (從社群網路平台收集公開資料，進行大數據分析和假新聞追蹤。）
- **Skill Sets: Vulnerability Assessment Concepts, Information Security Implementation, Big Data Analysis, Big Data Processing, Social Network Analysis, Paper Review, Paper Writing, Presentation Skills**
- ► For Cyber Security, build a ''Penetration Testing'' and ''Vulnerability Assessment'' environment using VMware virtual machine, and use a second virtual machine, Kali Linux, as the attacking party for testing; paper review, paper writing, and presentation skills.
- (網路安全方面，使用 VMware 虛擬機器建立『滲透測試』和『漏洞評估』環境，並使用第二個虛擬機器 Kali Linux 作為攻擊方進行測試;論文審查、論文撰寫和演講技巧、滲透測試技巧。)
- **Skill Sets: Virtual Machine, Penetration Testing Concepts, Vulnerability Assessment Concepts, Information Security Implementation** 
"""
)
st.write("🚧", "**Teaching Assistant | Department of Computer Science, Tunghai University**")
st.write("02/2022 - 06/2022")
st.write("""
- ► Instructing discussion sessions in the course of Artificial Intelligence.
- (在人工智慧概論課程中指導學生與帶領討論。)
- **Skill Sets: Basic Artificial Intelligence Concepts, Basic Computer Science Concepts, Communication & Team-Work**
""")

# --- JOB 2
st.write('\n')
st.write("🚧", "**Research Assistant - 資安卓越中心規劃建置計畫 | National Institute of Cyber Security 國家資通安全研究院**")
st.write("01/2023 - 06/2023")
st.write(
    """
- ► Based on the developed API & ETL pipeline, about 30 million pieces of public data of social networks were obtained.
- (利用取得的約3,000萬個社群網路公開資料，開發了API和ETL程序。)
- ► A social network analysis study was conducted using approximately 30 million pieces of public data.
- (使用大約 3000 萬個公開資料進行了社群網絡分析研究。)
- ► Based on the research questions, we visualized the social network for the social network message dissemination phenomenon study.
- (根據研究問題，我們將社群網路視覺化，進行社群網路訊息現象研究。)
- **Skill Sets: Big Data Analysis, Big Data Processing, Data Visualization, Social Network Analysis**
"""
)
st.write("07/2022 - 12/2022")
st.write("""
- ► The VMware virtual machine build uses a combination of deep learning semantic similarity analysis and artificial intelligence to develop an online social network API.
- (使用VMware虛擬機建構了結合深度學習語意相似性分析和人工智慧來開發線上社群網路可疑訊息追蹤API。)
- ► Packages VMware for delivery as a VMDK file.
- (將開發後的VMware打包為VMDK檔案。)
- ► The development process uses Git for version control and facilitates collaboration with other engineers.
- (開發過程中使用Git進行版本控制，方便與其他工程師的協作。)
- ► About 30 million social network public data were built into the PostgreSQL database, and design the database index to improve the search performance from the original 30 seconds per search to 0.77 seconds.
- (將約3000萬條社群網路公開資料建置在PostgreSQL資料庫中，並設計資料庫索引，將搜尋效能從原來的每次搜尋30秒提高到0.77秒。)
- ► Using Python Flask web application framework was combined with PostgreSQL to develop the API.
- (使用Python Flask框架結合PostgreSQL開發API。)
- ► About 6 million social network public data were built into the MongoDB database, and design the database index to improve the search performance.
- (將約600萬則社群網路公開資料建置到MongoDB資料庫中，並設計資料庫索引以提高搜尋效能。)
- ► Using Python Flask web application framework was combined with MongoDB to develop the API.
- (使用Python Flask框架結合MongoDB開發API。)
- **Skill Sets: Virtual Machine, Natural Language Processing, Deep Learning, API Development, SQL, Git, Team-Work**
""")

# --- JOB 3
st.write('\n')
st.write("🚧", "**學員-產業新尖兵試辦計畫_AI大數據企業實務應用班 | Tunghai University**")
st.write("07/2021 - 10/2021")
st.write(
    """
- ► Learn basic concepts of Python and R programming, data processing skills, as well as data visualization and artificial intelligence machine learning concepts.
- (學習Python和R程式設計的基本概念、資料處理技能，以及資料視覺化和人工智慧機器學習概念。)
- ► Participated in the "2021 Data Station" competition, using the "PChome product purchase list" dataset provided by the organizer.
- (參加「2021 Data Station」企業數據競賽，使用主辦單位提供的「PChome產品購買清單」資料集進行分析。)
- ► Based on the dataset, I processed and added new features to the data, and used third-party data to overlay it, and used Python machine learning algorithms such as decision trees and random forests to analyze the frequency of customers' purchases.
- (根據資料集，對資料進行了處理和新增特徵，並使用第三方資料對其進行疊加，最後使用決策樹、隨機森林等Python機器學習演算法來分析客戶的購買頻率。)
- **Skill Sets: Python Programming, R Programming, Data Processing Skills, Data Visualization, Data Analysis Based on Enterprise Data, Basic Artificial Intelligence Concepts**
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# PUBLICATION
st.write('\n')
st.subheader("Publications")
st.write("---")
for project, link in PUBLICATION.items():
    st.write(f"[{project}]({link})")

# AWARD
st.write('\n')
st.subheader("Awards")
st.write("---")
for project, link in Awards.items():
    st.write(f"[{project}]({link})")