FROM python:3.7

# 파이썬 버퍼 제거
ENV PYTHONUNBUFFERED=1

# 작업 파일 설정
RUN mkdir /project
WORKDIR /project

# 파이썬 라이브러리 설치
COPY requirements.txt /project
RUN pip install -r requirements.txt

# -u 옵션으로 버퍼없이 즉시 출력
# stdout 과 stderr 스트림을 버퍼링하지 않도록 만듭니다. 이 옵션은 stdin 스트림에는 영향을 미치지 않습니다.
CMD ["python", "-u", "./main.py"]
