import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Privacy Policy Analysis Dashboard",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dictionary mapping each company to its logo URL
company_logos = {
    "Apple": "apple_logo.png",
    "Amazon": "amazon_logo.png",
    "Uber": "uber_logo.png",
    "Facebook": "facebook_logo.png",
    "Google": "google_logo.png",
    "Paytm": "paytm_logo.png"
}

# Sidebar
with st.sidebar:
    st.title("Privacy Policy Analysis 🕵🏻‍♂")
    company = st.selectbox("Select a company", list(company_logos.keys()))

# Main Page Title
st.title(f"Privacy Policy Analysis for {company}")
st.write('\n')

# Dividing the main area into three columns
col1, col2, col3 = st.columns(3)

# Column 1: Logo and About Company
with col1:
    st.image(company_logos[company], width=130)
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.subheader("&nbsp;&nbsp;About")

    if company == "Facebook":
        st.markdown("""
        - Global social media giant connecting billions of users worldwide
        - Owns popular platforms like Instagram, WhatsApp, and Messenger
        - Drives revenue through targeted digital advertising services
        """)
    elif company == "Paytm":
        st.markdown("""
        - Offers seamless transactions via Paytm Wallet, UPI, and QR codes
        - Wide range of services including bill payments, recharge, and shopping
        - Provides financial products like loans, insurance, and mutual funds
        """)
    elif company == "Google":
        st.markdown("""
        - Dominates internet search with its flagship Google Search engine
        - Offers popular services like Gmail, Google Maps, and Google Drive
        - Operates YouTube, the world’s largest video-sharing platform
        """)
    elif company == "Amazon":
        st.markdown("""
        - Offers a vast selection of products with fast delivery services
        - Dominates cloud computing through Amazon Web Services (AWS)
        - Operates popular devices like Kindle, Echo, and Fire TV
        """)
    elif company == "Uber":
        st.markdown("""
        - Global ride-hailing platform connecting riders with drivers in real-time
        - Offers diverse services like UberX, Uber Black, and Uber Pool
        - Uses dynamic pricing based on real-time demand and supply
        """)
    elif company == "Apple":
        st.markdown("""
        - Innovative leader in technology with iconic products like iPhone
        - Seamless ecosystem connecting devices through iCloud and other services
        - Known for exclusive operating systems like iOS, macOS, and watchOS
        """)

# Column 2: Data Collected and Data Used
with col2:
    st.subheader("📊 How Data is Collected & Used")
    if company == "Facebook":
        st.markdown("""
        - *Data Collection*:  
            - Collects user profiles, posts, likes, comments, messages, browsing activity, and device metadata (e.g., location, IP address)  
        - *Data Usage*:  
            - Provides targeted ads and recommends content using machine learning 
        - *Platforms*:  
            - Facebook, Instagram, WhatsApp, Messenger, third-party websites
        - *Data Breach Cases*:  
            - Records Of 200,000 Facebook Marketplace Users Found On Dark Web ([Source](https://www.ndtv.com/world-news/records-of-200-000-facebook-marketplace-users-found-on-dark-web-5067851)) 
            - Personal details of 6.1 million Facebook users in India leaked online ([Source](https://economictimes.indiatimes.com/tech/technology/personal-details-of-6-1-million-facebook-users-in-india-leaked-online/articleshow/81916959.cms?from=mdr)) 
        """)
    elif company == "Paytm":
        st.markdown("""
        - *Data Collection*:  
            - Collects phone numbers, payment details, transaction history, and KYC documents
        - *Data Usage*:  
            - Facilitates payments and analyzes transaction history for personalized offers
        - *Platforms*:  
            - Paytm Wallet, Paytm Payments Bank, UPI, Paytm Mall
        - *Proof*:  
            - Paytm data breach: 3.4 million users affected ([Source](https://www.timesnownews.com/technology-science/paytm-data-breach-3-4-million-users-affected-how-to-check-if-you-were-one-of-them-article-93162945)).  
            - Paytm Mall suffers data breach, ransom demanded by hackers ([Source](https://www.livemint.com/companies/news/paytm-mall-suffers-data-breach-ransom-demanded-by-hackers-cyble-report-11598793039641.html)).  
        """)
    elif company == "Google":
        st.markdown("""
        - *Data Collection*:  
            - Tracks search queries, browsing, location, device activity, and Gmail data
        - *Data Usage*:  
            - Delivers targeted ads and personalized services like route suggestions
        - *Platforms*:  
            - Google Search, YouTube, Gmail, Google Maps, Android
        - *Data Breach Cases*:  
            - Google data leak: Secret of search ranking algorithm is out, 2,500 internal documents leaks ([Source](https://www.financialexpress.com/life/technology-google-data-leak-secret-of-search-ranking-algorithm-is-out-2500-internal-documents-leaks-3507044/))
            - Potential Data Leak from Google: 1 Million Records Exposed ([Source](https://www.redhotcyber.com/en/post/potential-data-leak-from-google-1-million-records-exposed/))
        """)
    elif company == "Amazon":
        st.markdown("""
        - *Data Collection*:  
            - Collects purchase history, browsing patterns, Alexa interactions, and device data  
        - *Data Usage*:  
            - Personalizes recommendations and improves voice recognition  
        - *Platforms*:  
            - Amazon website, Alexa, Kindle, Fire TV, AWS  
        - *Data Breach Cases*:  
            - Amazon confirms employee data breach ([Source](https://www.theverge.com/2024/11/11/24293817/amazon-employee-emails-phone-numbers-moveit-data-breach))  
            - Turkey fines Amazon’s Twitch 2 million lira for data breach ([Source](https://indianexpress.com/article/technology/tech-news-technology/turkey-fines-amazons-twitch-2-million-lira-for-data-breach-9675461/lite/))  
        """)
    elif company == "Uber":
        st.markdown("""
        - *Data Collection*:  
            - Gathers ride data, payment details, GPS information, and user behavior  
        - *Data Usage*:  
            - Matches riders and drivers, personalizes offers, and optimizes routes  
        - *Platforms*:  
            - Uber, Uber Eats, third-party integrations  
        - *Data Breach Cases*:  
            - Uber fined $324M over EU drivers’ data transfer breach ([Source](https://techcrunch.com/2024/08/26/uber-fined-324m-over-eu-driver-data-transfer-breach/))
            - Uber Breach Exposes the Data of 57 Million Drivers and Users ([Source](https://www.trendmicro.com/vinfo/in/security/news/cybercrime-and-digital-threats/uber-breach-exposes-the-data-of-57-million-drivers-and-users)) 
        """)
    elif company == "Apple":
        st.markdown("""
        - *Data Collection*:  
            - Collects device analytics, app usage, location data, and Siri interactions  
        - *Data Usage*:  
            - Enhances Siri and search, powers app and music recommendations  
        - *Platforms*:  
            - iOS, macOS, iCloud, Apple Pay, Siri, Apple Watch  
        - *Data Breach Cases*:  
            - Data breaches through in-app ads and push notifications ([Source](https://www.livemint.com/technology/iphone-users-on-alert-reports-indicate-data-breaches-through-in-app-ads-and-push-notifications-11706252499809.html))  
            - Source Code for Internal Tools Allegedly Stolen ([Source](https://www.gadgets360.com/internet/news/apple-alleged-breach-internal-tools-source-code-intelbroker-dark-web-leak-5930326))
        """)


# Column 3: Merits, Demerits, and Score
with col3:
    st.subheader("✅ Merits")
    if company == "Facebook":
        st.markdown("""
        - Implements encryption for messages on Messenger
        - Allows users to control data sharing
        - Provides privacy checkups for enhanced security
        """)
    elif company == "Apple":
        st.markdown("""
        - Strong encryption protects user data
        - Safari blocks third-party cookie tracking
        - Privacy labels inform app data use
        """)
    elif company == "Uber":
        st.markdown("""
        - Anonymizes data to protect personal information
        - Limits driver access to rider contact details
        - Conducts regular security audits to ensure compliance
        """)
    elif company == "Paytm":
        st.markdown("""
        - Provides encrypted transactions for secure payments
        - Limits third-party access to personal data
        - Protects payment details with tokenization technology
        """)
    elif company == "Google":
        st.markdown("""
        - Data is anonymized in many services
        - Regularly conducts security audits and updates
        - Transparency in data collection and usage
        """)
    elif company == "Amazon":
        st.markdown("""
        - Encrypts sensitive data during transmission and storage
        - Offers transparency in data usage policies
        - Protects user data with strong encryption
        """)

    st.subheader("❌ Demerits")

    if company == "Facebook":
        st.markdown("""
        - User data exploited in the Cambridge Analytica scandal
        - Tracks user behavior extensively, even off-platform
        - Weak controls on harmful or offensive content
        """)
    elif company == "Apple":
        st.markdown("""
        - Retains location data even with location services off
        - Siri recordings were analyzed without user consent
        - Third-party apps sometimes bypass data safeguards
        """)
    elif company == "Uber":
        st.markdown("""
        - Tracks user locations extensively even after trips
        - Data breaches exposed sensitive rider and driver data
        - Employees misused "God View" to track individuals
        """)
    elif company == "Paytm":
        st.markdown("""
        - Inadequate consent for targeted advertising
        - Retention of user data for extended periods
        - Weak data localization policies despite sensitive information
        """)
    elif company == "Google":
        st.markdown("""
        - Continuously tracks user behavior via services
        - Limited transparency on ad-targeting practices
        - "Incognito mode" still collects some user data
        """)
    elif company == "Amazon":
        st.markdown("""
        - Uses Alexa recordings for data analysis without clarity
        - Shares customer data with third-party advertisers
        - Collects detailed shopping and browsing habits
        """)


        # Function to create a circular progress bar
    def circular_progress_bar(percentage, company_name):
        html_code = f"""
        <div style="display: flex; justify-content: flex-start; align-items: center; height: 150px; margin-left: 8%;">
            <div style="position: relative; width: 150px; height: 150px;">
                <svg width="150" height="150" viewBox="0 0 36 36">
                    <path
                        stroke="#ddd"
                        stroke-width="3.8"
                        fill="none"
                        d="M18 2.0845
                        a 15.9155 15.9155 0 0 1 0 31.831
                        a 15.9155 15.9155 0 0 1 0 -31.831"
                    />
                    <path
                        stroke="#4CAF50"
                        stroke-width="3.8"
                        stroke-dasharray="{percentage}, 100"
                        fill="none"
                        d="M18 2.0845
                        a 15.9155 15.9155 0 0 1 0 31.831
                        a 15.9155 15.9155 0 0 1 0 -31.831"
                    />
                </svg>
                <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 1.2rem; font-weight: bold;">
                    {percentage}%
                </div>
            </div>
        </div>
        """
        return html_code




    # Example usage of the function
    st.subheader("🛡 Privacy Score")

    if company == "Facebook":
        merits_score = 60
    elif company == "Apple":
        merits_score = 85
    elif company == "Uber":
        merits_score = 70
    elif company == "Paytm":
        merits_score = 60
    elif company == "Google":
        merits_score = 75
    elif company == "Amazon":
        merits_score = 75

    # Display the circular progress bar
    st.markdown(circular_progress_bar(merits_score, company), unsafe_allow_html=True)