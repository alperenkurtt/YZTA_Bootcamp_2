import sys

from utils.file_reader import read_file
from utils.keyword_matcher import extract_requirements, match_keywords
from utils.ai_analyzer import analyze_cv


def main():
    sys.stdout.reconfigure(encoding="utf-8")

    print("=" * 60)
    print("NorthCompass")
    print("AI Destekli Kariyer Platformu")
    print("=" * 60)

    cv_text = read_file("sample_data/sample_cv_2.txt")
    job_text = read_file("sample_data/sample_job_2.txt")

    print("\nCV ve iş ilanı analiz ediliyor...\n")

    keywords = extract_requirements(job_text)
    match_result = match_keywords(cv_text, keywords)

    print(f"CV - İş İlanı Eşleşme Skoru: %{match_result['score']}")
    print(f"Eşleşen Beceriler: {', '.join(match_result['matched']) or 'yok'}")
    print(f"Eksik Beceriler: {', '.join(match_result['missing']) or 'yok'}")
    print()

    result = analyze_cv(cv_text, job_text, match_result)

    print(result)


if __name__ == "__main__":
    main()
