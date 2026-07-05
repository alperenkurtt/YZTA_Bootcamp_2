from utils.file_reader import read_file
from utils.ai_analyzer import analyze_cv


def main():
    print("=" * 60)
    print("NorthCompass")
    print("AI Destekli Kariyer Platformu")
    print("=" * 60)

    cv_text = read_file("sample_data/sample_cv.txt")
    job_text = read_file("sample_data/sample_job.txt")

    print("\nCV ve iş ilanı analiz ediliyor...\n")

    result = analyze_cv(cv_text, job_text)

    print(result)


if __name__ == "__main__":
    main()
