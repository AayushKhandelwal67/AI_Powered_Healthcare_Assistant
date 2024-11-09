# Catalyst 🏥

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![Figma](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)](https://www.figma.com/)

## Fast-Tracking Specialist Access for Smarter, Quicker Care 🚀

Catalyst is an innovative healthcare solution designed to integrate seamlessly with Sharp Healthcare's existing application, addressing the critical challenges in specialist healthcare access and patient care management in San Diego.

### 🌟 Key Features

#### 1. AI-Powered Specialist Matching
- **Smart Symptom Analysis**: Interactive chatbot for initial symptom assessment
- **Personalized Screening**: Follow-up questions for accurate specialist matching
- **Intelligent Recommendation**: ML-based doctor matching using historical data and ratings
- **Professional Validation**: Optional medical professional verification before appointment booking

#### 2. Medical Report Analyzer
- **Jargon-Free Summaries**: Converts complex medical reports into simple language
- **Abnormality Detection**: Highlights tests requiring attention
- **Visual Analysis**: Supports both PDF and image format medical reports
- **Actionable Insights**: Provides clear improvement recommendations

### 🛠️ Technical Implementation

#### Specialist Recommendation System
```python
# Core Components:
- Symptom tokenization and vectorization
- Case similarity analysis
- Doctor rating integration
- Multilingual support
```

#### LLM Integration
- **Primary Models**: OpenBioLLM (fine-tuned), GPT-4o
- **Dynamic Model Routing**: Cost-effective switching based on query complexity
- **Multimodal Capabilities**: Text and image processing support

### 💻 Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **AI Models**: OpenAI GPT models, Open-source medical LLMs
- **Document Processing**: PyPDF2
- **Design**: Figma

### 🚀 Getting Started

1. Clone the repository
```bash
git clone [repository-url]
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up environment variables
```bash
# Create .env file and add:
OPENAI_API_KEY=your_openai_api_key_here
```

4. Run the application
```bash
python hack.py
```


### 🎯 Problem Statement

In San Diego, patients face significant challenges:
- 30-90+ day wait times for specialists
- Uncertainty in specialist selection
- Risk of condition deterioration during wait periods
- Complex healthcare system navigation

### 💡 Solution Impact

1. **For Patients**
   - Reduced wait times
   - Accurate specialist matching
   - Clear medical information
   - Improved healthcare journey

2. **For Healthcare Providers**
   - Optimized patient routing
   - Enhanced pre-appointment information
   - Improved resource allocation
   - Better patient outcomes

