from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuration
app.config['ENV'] = os.getenv('FLASK_ENV', 'development')
app.config['DEBUG'] = os.getenv('DEBUG', 'True') == 'True'


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'BrandSpark AI backend is running'
    }), 200


@app.route('/api/welcome', methods=['GET'])
def welcome():
    """Welcome message endpoint"""
    return jsonify({
        'message': 'Welcome to BrandSpark AI! Your AI-powered marketing assistant is ready to help you create amazing campaigns.',
        'version': '0.1.0'
    }), 200


@app.route('/api/generate', methods=['POST'])
def generate_content():
    """Generate marketing content using AI"""
    try:
        data = request.get_json()
        
        if not data or 'prompt' not in data:
            return jsonify({
                'error': 'Missing required field: prompt'
            }), 400
        
        prompt = data['prompt']
        
        # TODO: Integrate with AI service (OpenAI, Claude, etc.)
        generated_content = f"Generated content for: {prompt}"
        
        return jsonify({
            'success': True,
            'prompt': prompt,
            'content': generated_content,
            'message': 'Content generated successfully'
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.route('/api/status', methods=['GET'])
def status():
    """Get system status"""
    return jsonify({
        'status': 'running',
        'environment': app.config['ENV'],
        'debug': app.config['DEBUG']
    }), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Endpoint not found',
        'status': 404
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error',
        'status': 500
    }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'])
