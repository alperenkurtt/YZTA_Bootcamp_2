import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_cv(cv_text, job_text):
    """
    CV ile iş ilanını Gemini kullanarak analiz eder.
    """

    prompt = f"""
    Sen profesyonel bir kariyer danışmanısın.

    Aşağıdaki CV ile iş ilanını karşılaştır.

    CV:
    {cv_text}

    İş İlanı:
    {job_text}

    Lütfen aşağıdaki başlıklarda analiz yap:

    1. CV - İş İlanı Uyum Oranı (%)
    2. Güçlü Yönler
    3. Eksik Yetkinlikler
    4. ATS Uyumluluğu
    5. CV Geliştirme Önerileri

    Yanıtını Türkçe ver.
    """

    response = model.generate_content(prompt)

    return response.text

