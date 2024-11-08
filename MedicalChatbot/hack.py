# from flask import Flask, request, jsonify, render_template
# from openai import OpenAI
# import os
# from dotenv import load_dotenv
# import base64
# from io import BytesIO

# load_dotenv()

# app = Flask(__name__)
# client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# def read_system_prompt(filename):
#     with open(filename, 'r') as file:
#         return file.read().strip()

# @app.route('/')
# def index():
#     return render_template('index_hack.html')

# @app.route('/chatbot', methods=['POST'])
# def chatbot():
#     user_message = request.json['message']
#     chat_history = request.json.get('chat_history', [])
#     query_type = request.json.get('query_type', 'general')
    
#     chat_history.append({"role": "user", "content": user_message})
    
#     try:
#         if query_type == 'specialist':
#             system_content = read_system_prompt('specialist_prompt.txt')
#         else:
#             system_content = read_system_prompt('general_prompt.txt')

#         messages = [
#             {"role": "system", "content": system_content},
#             *chat_history
#         ]

#         response = client.chat.completions.create(
#             model="gpt-4o",
#             messages=messages,
#             max_tokens=150
#         )
        
#         ai_message = response.choices[0].message.content
#         chat_history.append({"role": "assistant", "content": ai_message})
        
#         return jsonify({
#             'message': ai_message, 
#             'chat_history': chat_history
#         })
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

# @app.route('/analyze_image', methods=['POST'])
# def analyze_image():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400
#     if file and allowed_file(file.filename):
#         try:
#             # Read the file into memory
#             file_content = file.read()
#             # Encode the file content to base64
#             base64_image = base64.b64encode(file_content).decode('utf-8')
#             # Analyze the image
#             analysis_result = call_gpt4_vision(base64_image)
#             return jsonify({'result': analysis_result})
#         except Exception as e:
#             return jsonify({'error': str(e)}), 500
#     return jsonify({'error': 'File type not allowed'}), 400

# def call_gpt4_vision(base64_image):
#     prompt = read_system_prompt('image_prompt.txt')
    
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {
#                 "role": "user",
#                 "content": [
#                     {"type": "text", "text": prompt},
#                     {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
#                 ]
#             }
#         ],
#         max_tokens=500
#     )
    
#     return response.choices[0].message.content

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify, render_template
from openai import OpenAI
import os
from dotenv import load_dotenv
import base64
from io import BytesIO
import PyPDF2

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf'}

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB limit

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def read_system_prompt(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

@app.route('/')
def index():
    return render_template('index_hack.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json['message']
    chat_history = request.json.get('chat_history', [])
    query_type = request.json.get('query_type', 'general')
    
    chat_history.append({"role": "user", "content": user_message})
    
    try:
        if query_type == 'specialist':
            system_content = read_system_prompt('specialist_prompt.txt')
        else:
            system_content = read_system_prompt('general_prompt.txt')

        messages = [
            {"role": "system", "content": system_content},
            *chat_history
        ]

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=150
        )
        
        ai_message = response.choices[0].message.content
        chat_history.append({"role": "assistant", "content": ai_message})
        
        return jsonify({
            'message': ai_message, 
            'chat_history': chat_history
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/analyze_image', methods=['POST'])
def analyze_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        try:
            # Read the file into memory
            file_content = file.read()
            # Encode the file content to base64
            base64_image = base64.b64encode(file_content).decode('utf-8')
            # Analyze the image
            analysis_result = call_gpt4_vision(base64_image)
            return jsonify({'result': analysis_result})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return jsonify({'error': 'File type not allowed'}), 400

def call_gpt4_vision(base64_image):
    prompt = read_system_prompt('image_prompt.txt')
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }
        ],
        max_tokens=500
    )
    
    return response.choices[0].message.content

@app.route('/analyze_report', methods=['POST'])
def analyze_report():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        try:
            file_content = file.read()
            if file.filename.lower().endswith('.pdf'):
                text_content = extract_text_from_pdf(file_content)
            else:
                # For image files, we'll use base64 encoding
                base64_content = base64.b64encode(file_content).decode('utf-8')
                text_content = f"[Image content: data:image/jpeg;base64,{base64_content}]"
            
            analysis_result = analyze_report_content(text_content)
            return jsonify({'result': analysis_result})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return jsonify({'error': 'File type not allowed'}), 400

def extract_text_from_pdf(file_content):
    pdf_reader = PyPDF2.PdfReader(BytesIO(file_content))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def analyze_report_content(content):
    prompt = read_system_prompt('report_prompt.txt')
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"Here's the medical report content:\n\n{content}"}
        ],
        max_tokens=500
    )
    
    return response.choices[0].message.content

if __name__ == '__main__':
    app.run(debug=True)