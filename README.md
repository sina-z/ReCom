# ReCom - Music Recommendation System

A hands-on learning project to build and deploy a music recommendation system from scratch, covering the full ML pipeline from data exploration to production deployment.

## 🎯 Project Goals

This project is designed as a **learning journey** to understand:
- Building recommendation systems (collaborative filtering, matrix factorization, etc.)
- ML experiment tracking and model comparison
- Model serving via REST API
- Containerization with Docker
- Deployment to production
- MLOps fundamentals (monitoring, retraining, A/B testing)

**Note**: The focus is on learning the complete stack, not creating the most sophisticated recommendation algorithm.

## 📋 Project Phases

### ✅ Phase 0: Data Acquisition and Exploration (Current)
- Finding/creating music dataset
- Exploratory data analysis
- Understanding data characteristics (sparsity, distributions)
- Setting up basic data pipeline

### 🔲 Phase 1: Basic Recommendation Algorithm
- Implementing collaborative filtering
- Train/test split
- Basic evaluation metrics (precision@k, recall@k)

### 🔲 Phase 2: Experiment Tracking & Model Comparison
- Setting up MLflow
- Implementing multiple algorithms
- Systematic model comparison

### 🔲 Phase 3: Model Serving (API)
- Building FastAPI endpoint
- Model persistence and loading
- Input validation and error handling

### 🔲 Phase 4: Containerization
- Creating Dockerfile
- Building and testing Docker images
- Docker Compose setup

### 🔲 Phase 5: Deployment
- Cloud deployment (Render/Railway)
- Production monitoring and logging

### 🔲 Phase 6: MLOps & Iteration (Optional)
- Model retraining pipeline
- A/B testing framework
- Performance monitoring

## 🛠️ Tech Stack

- **Language**: Python 3.13.0
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **ML**: scikit-learn (Phase 1+)
- **Experiment Tracking**: MLflow (Phase 2+)
- **API**: FastAPI (Phase 3+)
- **Containerization**: Docker (Phase 4+)
- **Deployment**: TBD (Phase 5+)

## 📁 Project Structure

```
ReCom/
├── data/                  # Dataset storage (gitignored)
│   ├── raw/              # Original, unmodified data
│   └── processed/        # Cleaned, transformed data
├── notebooks/            # Jupyter notebooks for exploration
├── src/                  # Source code (Python modules)
│   ├── data/            # Data loading and preprocessing
│   ├── models/          # Recommendation algorithms
│   ├── evaluation/      # Metrics and evaluation
│   └── api/             # API code (Phase 3+)
├── models/               # Trained model artifacts (gitignored)
├── tests/                # Unit tests
├── docs/                 # Additional documentation
├── .gitignore           # Git ignore rules
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.13.0
- pip (Python package manager)
- git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ReCom.git
   cd ReCom
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate it
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

**Phase 0 - Data Exploration**
```bash
# Start Jupyter notebook
jupyter notebook

# Open notebooks in the notebooks/ directory
```

More usage instructions will be added as the project progresses through different phases.

## 📊 Current Status

**Phase**: 0 - Data Acquisition and Exploration  
**Last Updated**: February 2026

## 🤝 Contributing

This is a personal learning project, but suggestions and feedback are welcome! Feel free to open an issue.

## 📝 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

- Learning resources and inspiration will be documented here as the project progresses
- Dataset sources will be credited once selected

---

**Note**: This README will be updated as the project evolves through each phase.
