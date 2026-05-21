# BrandSpark AI

An intelligent AI-powered marketing system designed to help brands create, optimize, and manage their marketing campaigns.

## 🚀 Features

- AI-powered content generation
- Multi-channel campaign management
- Real-time analytics and insights
- User-friendly dashboard
- RESTful API backend

## 📋 Project Structure

```
brandspark_ai/
├── frontend/          # React + Vite frontend application
├── backend/           # Python Flask backend server
└── README.md         # Project documentation
```

## 🛠️ Tech Stack

### Frontend
- **Framework**: React 18
- **Build Tool**: Vite
- **Styling**: CSS
- **State Management**: React Hooks

### Backend
- **Framework**: Flask
- **Language**: Python 3.8+
- **Database**: (To be configured)
- **API**: RESTful

## 📦 Installation

### Prerequisites
- Node.js 16+ and npm
- Python 3.8+
- Git

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The frontend will run on `http://localhost:5173`

### Backend Setup

```bash
cd backend
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python main.py
```

The backend will run on `http://localhost:5000`

## 🔌 API Endpoints

- `GET /api/health` - Health check endpoint
- `GET /api/welcome` - Welcome message
- `POST /api/generate` - Generate marketing content

## 📝 Environment Variables

Create a `.env` file in the `backend/` directory:

```env
FLASK_ENV=development
FLASK_APP=main.py
DEBUG=True
```

## 🤝 Contributing

1. Create a new branch for your feature
2. Make your changes
3. Commit and push to your branch
4. Open a Pull Request

## 📄 License

MIT License - feel free to use this project for your needs.

## 📧 Support

For questions or issues, please open an issue on GitHub.

---

**Built with ❤️ using AI and modern web technologies**
