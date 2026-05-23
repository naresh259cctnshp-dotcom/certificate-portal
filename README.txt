
Hosting Ready Certificate Portal

Local Run:
pip install -r requirements.txt
python app.py

Open:
http://127.0.0.1:5000

Render Hosting:
1. Upload project to GitHub
2. Open render.com
3. Create New Web Service
4. Connect GitHub Repo
5. Build Command:
   pip install -r requirements.txt
6. Start Command:
   gunicorn app:app
