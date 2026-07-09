def extract_requirements(job_text):
    """
    İş ilanı metnindeki 'Requirements' bölümünden madde listesini çıkarır.
    """
    lines = job_text.splitlines()
    keywords = []
    in_requirements = False

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue

        lowered = stripped.lower()
        if lowered == "requirements":
            in_requirements = True
            continue
        if lowered == "responsibilities":
            in_requirements = False
            continue

        if in_requirements:
            keywords.append(stripped.lstrip("-").strip())

    return keywords


def match_keywords(cv_text, keywords):
    """
    Verilen anahtar kelimelerin CV metninde geçip geçmediğini kontrol eder.
    """
    cv_lower = cv_text.lower()

    matched = [kw for kw in keywords if kw.lower() in cv_lower]
    missing = [kw for kw in keywords if kw.lower() not in cv_lower]
    score = round(len(matched) / len(keywords) * 100) if keywords else 0

    return {
        "matched": matched,
        "missing": missing,
        "score": score,
    }
