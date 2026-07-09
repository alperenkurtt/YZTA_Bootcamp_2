import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_cv(cv_text, job_text, match_result):
    """
    CV ile iş ilanını, önceden hesaplanmış anahtar kelime eşleşmesini temel alarak
    Gemini kullanarak analiz eder.
    """

    matched = ", ".join(match_result["matched"]) or "yok"
    missing = ", ".join(match_result["missing"]) or "yok"

    prompt = f"""
    Sen profesyonel bir kariyer danışmanısın.

    Aşağıdaki CV ile iş ilanını karşılaştır.

    CV:
    {cv_text}

    İş İlanı:
    {job_text}

    CV - İş İlanı eşleşme skoru koddan hesaplanmıştır: %{match_result["score"]}
    Eşleşen beceriler: {matched}
    Eksik beceriler: {missing}

    Bu verileri temel alarak aşağıdaki başlıklarda analiz yap:

    1. Güçlü Yönler
    2. ATS Uyumluluğu (skoru tekrar hesaplama, sadece değerlendirme yaz)
    3. Eksik becerilere dayalı CV Geliştirme Önerileri

    Yanıtını Türkçe ver.
    """

    response = model.generate_content(prompt)

    return response.text

