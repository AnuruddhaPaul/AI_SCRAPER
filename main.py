import streamlit as st
import time
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_ollama

# Page configuration
st.set_page_config(
    page_title="AI Web Scraper Pro",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    /* Main app styling */
    .main {
        padding-top: 2rem;
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    
    .header-title {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .header-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
        margin-bottom: 0;
    }
    
    /* Card styling */
    .card {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border: 1px solid #e1e5e9;
        margin-bottom: 2rem;
    }
    
    .card-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #3498db;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.7rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(52, 152, 219, 0.4);
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e1e5e9;
        padding: 0.7rem;
        font-size: 1rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #3498db;
        box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
    }
    
    .stTextArea > div > div > textarea {
        border-radius: 10px;
        border: 2px solid #e1e5e9;
        font-size: 1rem;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #3498db;
        box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
    }
    
    /* Progress and success styling */
    .success-message {
        background: linear-gradient(135deg, #2ecc71 0%, #27ae60 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
        font-weight: 600;
    }
    
    .info-message {
        background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
        font-weight: 600;
    }
    
    /* Sidebar styling */
    .sidebar-content {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    
    /* Stats cards */
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    
    /* Feature list */
    .feature-list {
        list-style: none;
        padding: 0;
    }
    
    .feature-list li {
        padding: 0.5rem 0;
        border-bottom: 1px solid #ecf0f1;
    }
    
    .feature-list li:before {
        content: "✓";
        color: #2ecc71;
        font-weight: bold;
        margin-right: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-container">
    <h1 class="header-title">🤖 AI Web Scraper Pro</h1>
    <p class="header-subtitle">Intelligent web scraping and content analysis powered by AI</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if 'dom_content' not in st.session_state:
    st.session_state.dom_content = None
if 'scraping_complete' not in st.session_state:
    st.session_state.scraping_complete = False
if 'scraped_url' not in st.session_state:
    st.session_state.scraped_url = ""

# Sidebar
with st.sidebar:
    st.markdown("""
    <div class="sidebar-content">
        <h3>🚀 Features</h3>
        <ul class="feature-list">
            <li>Smart web scraping</li>
            <li>AI-powered content parsing</li>
            <li>Real-time analysis</li>
            <li>Clean data extraction</li>
            <li>Interactive results</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.scraping_complete:
        content_length = len(st.session_state.dom_content) if st.session_state.dom_content else 0
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{content_length:,}</div>
            <div class="stat-label">Characters Scraped</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">✓</div>
            <div class="stat-label">Ready for Analysis</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 💡 How to use:")
    st.markdown("""
    1. **Enter URL** - Paste the website URL you want to scrape
    2. **Scrape** - Click the scrape button to extract content
    3. **Analyze** - Describe what you want to parse from the content
    4. **Get Results** - Receive AI-powered analysis
    """)

# Main content area with columns
col1, col2 = st.columns([2, 1])

with col1:
    # Step 1: URL Input and Scraping
    st.markdown("""
    <div class="card">
        <div class="card-header">🌐 Website Scraping</div>
    </div>
    """, unsafe_allow_html=True)
    
    url = st.text_input(
        "Enter Website URL",
        placeholder="https://example.com",
        help="Enter the complete URL including http:// or https://"
    )
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2])
    
    with col_btn1:
        scrape_button = st.button("🚀 Scrape Website", type="primary")
    
    with col_btn2:
        if st.session_state.scraping_complete:
            if st.button("🔄 Clear Data"):
                st.session_state.dom_content = None
                st.session_state.scraping_complete = False
                st.session_state.scraped_url = ""
                st.rerun()

    # Scraping logic
    if scrape_button:
        if url:
            if url.startswith(('http://', 'https://')):
                try:
                    # Show progress
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    status_text.markdown('<div class="info-message">🔍 Connecting to website...</div>', unsafe_allow_html=True)
                    progress_bar.progress(25)
                    time.sleep(0.5)
                    
                    # Scrape the website
                    dom_content = scrape_website(url)
                    progress_bar.progress(50)
                    
                    status_text.markdown('<div class="info-message">📄 Extracting content...</div>', unsafe_allow_html=True)
                    body_content = extract_body_content(dom_content)
                    progress_bar.progress(75)
                    
                    status_text.markdown('<div class="info-message">🧹 Cleaning content...</div>', unsafe_allow_html=True)
                    cleaned_content = clean_body_content(body_content)
                    progress_bar.progress(100)
                    
                    # Store the DOM content in session state
                    st.session_state.dom_content = cleaned_content
                    st.session_state.scraping_complete = True
                    st.session_state.scraped_url = url
                    
                    # Clear progress indicators
                    progress_bar.empty()
                    status_text.markdown('<div class="success-message">✅ Website scraped successfully!</div>', unsafe_allow_html=True)
                    
                    time.sleep(1)
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Error scraping website: {str(e)}")
            else:
                st.error("❌ Please enter a valid URL starting with http:// or https://")
        else:
            st.error("❌ Please enter a website URL")

    # Display scraped content
    if st.session_state.scraping_complete and st.session_state.dom_content:
        st.markdown(f"""
        <div class="success-message">
            ✅ Successfully scraped: {st.session_state.scraped_url}
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("📄 View Scraped Content", expanded=False):
            st.text_area(
                "DOM Content",
                st.session_state.dom_content,
                height=300,
                help="This is the cleaned content extracted from the website"
            )

    # Step 2: AI Analysis
    if st.session_state.scraping_complete:
        st.markdown("""
        <div class="card">
            <div class="card-header">🤖 AI Content Analysis</div>
        </div>
        """, unsafe_allow_html=True)
        
        parse_description = st.text_area(
            "What would you like to extract or analyze?",
            placeholder="e.g., Extract all product names and prices, Summarize the main article, Find contact information, etc.",
            height=100,
            help="Describe in detail what information you want to extract from the scraped content"
        )
        
        col_parse1, col_parse2 = st.columns([1, 3])
        
        with col_parse1:
            parse_button = st.button("🧠 Analyze Content", type="primary")
        
        if parse_button:
            if parse_description:
                try:
                    # Show analysis progress
                    with st.spinner("🔍 AI is analyzing the content..."):
                        progress_bar = st.progress(0)
                        status_text = st.empty()
                        
                        status_text.markdown('<div class="info-message">📊 Splitting content into chunks...</div>', unsafe_allow_html=True)
                        progress_bar.progress(33)
                        dom_chunks = split_dom_content(st.session_state.dom_content)
                        
                        status_text.markdown('<div class="info-message">🤖 AI processing content...</div>', unsafe_allow_html=True)
                        progress_bar.progress(66)
                        parsed_result = parse_with_ollama(dom_chunks, parse_description)
                        
                        progress_bar.progress(100)
                        status_text.markdown('<div class="success-message">✅ Analysis complete!</div>', unsafe_allow_html=True)
                        
                        # Clear progress indicators
                        time.sleep(0.5)
                        progress_bar.empty()
                        status_text.empty()
                    
                    # Display results
                    st.markdown("""
                    <div class="card">
                        <div class="card-header">📋 Analysis Results</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown(parsed_result)
                    
                    # Download option
                    st.download_button(
                        label="📥 Download Results",
                        data=parsed_result,
                        file_name=f"analysis_results_{int(time.time())}.txt",
                        mime="text/plain"
                    )
                    
                except Exception as e:
                    st.error(f"❌ Error during analysis: {str(e)}")
            else:
                st.error("❌ Please describe what you want to analyze")

with col2:
    # Tips and instructions
    st.markdown("""
    <div class="card">
        <div class="card-header">💡 Pro Tips</div>
        <ul class="feature-list">
            <li><strong>Specific queries</strong> get better results</li>
            <li>Try "Extract all email addresses"</li>
            <li>Use "Summarize in 3 points"</li>
            <li>Ask for "Table data as CSV format"</li>
            <li>Request "Contact information only"</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Sample URLs for testing
    st.markdown("""
    <div class="card">
        <div class="card-header">🧪 Sample URLs</div>
        <p><small>Try these for testing:</small></p>
    </div>
    """, unsafe_allow_html=True)
    
    sample_urls = [
        "https://example.com",
        "https://news.ycombinator.com",
        "https://httpbin.org/html"
    ]
    
    for sample_url in sample_urls:
        if st.button(f"📝 {sample_url}", key=f"sample_{sample_url}"):
            st.session_state.sample_url = sample_url
            st.rerun()
    
    if hasattr(st.session_state, 'sample_url'):
        st.info(f"💡 Sample URL selected: {st.session_state.sample_url}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; opacity: 0.7; margin-top: 2rem;">
    <p>🤖 AI Web Scraper Pro - Powered by Advanced AI Technology</p>
    <p><small>Built with Streamlit • Enhanced with Custom Styling</small></p>
</div>
""", unsafe_allow_html=True)