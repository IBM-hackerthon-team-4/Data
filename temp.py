from google_images_download import google_images_download

# 객체 생성
response = google_images_download.googleimagesdownload()

# 검색어와 옵션 설정
arguments = {
    "keywords": "sunset, mountains",
    "limit": 5,  # 다운로드할 이미지 개수
    "print_urls": True,  # 이미지 URL 출력
    "format": "jpg",  # 이미지 포맷 지정
    "size": "medium",  # 이미지 크기 (large, medium, icon 등)
    "aspect_ratio": "panoramic"  # 종횡비 옵션
}

# 이미지 다운로드 실행
paths = response.download(arguments)

# 다운로드된 이미지 경로 출력
print(paths)
