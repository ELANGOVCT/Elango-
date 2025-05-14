# AI/ML Analytics to Predict and Prevent Quality Deviation Trends in Automotive Manufacturing

This project aims to leverage artificial intelligence and machine learning to proactively detect and prevent quality deviation trends in automotive manufacturing. The system is designed to identify issues before they escalate, reducing rework, waste, and warranty claims.

## Features
- Supervised and unsupervised ML models for quality prediction
- Real-time monitoring dashboard
- Batch-level analysis and scoring
- Role-based access and basic encryption for security

## Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn, XGBoost
- Streamlit/Flask for dashboards
- Matplotlib/Plotly for visualization

## How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the dashboard:
```bash
python dashboard.py
```

3. Train model:
```bash
python train_model.py
```

4. Predict:
```bash
python predict.py --input data/sample_input.csv
```

## Repository Structure
- /src/ : Source code
- /data/ : Input sample datasets
- /docs/ : Phase documents (PDFs)
- /screenshots/ : Dashboard UI images

## License
This project is licensed under the MIT License.
