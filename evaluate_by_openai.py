import os
import glob
import PyPDF2
from openai import OpenAI
import time

# OpenAI API 키 설정
client = OpenAI(api_key='your_openai_api_key_here')

# PDF 파일이 있는 폴더 경로
folder_path = r"K:\내 드라이브\김규호@ewhaswu2\2025-1 사물인터넷 개론\Weekly Homework\0403과제"

def extract_text_from_pdf(pdf_path):
    """PDF 파일에서 텍스트를 추출하는 함수"""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"PDF 읽기 오류 ({pdf_path}): {e}")
        return ""

def evaluate_content(text):
    """OpenAI API를 사용하여 내용을 평가하는 함수"""
    try:
        prompt = f"""중학생 2학년학생한테 간단히 인터넷 TCP의 원리, 패킷스위칭과 서킷스위칭을 설명하는 자료인데, 
        중학교 2학년 수준에 맞되, 논리적이고 설명이 효과적인지 평가해서, 10점 만점으로 점수 부여하고, 한줄 코멘트 만들어줘

        평가할 내용:
        {text}
        """
        
        response = client.chat.completions.create(
            model="gpt-4",  # 또는 "gpt-3.5-turbo" 등 적절한 모델 선택
            messages=[
                {"role": "system", "content": "당신은 교육 자료를 평가하는 전문가입니다. 10점 만점으로 점수를 부여하고, 한 줄의 코멘트를 제공해야 합니다."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )
        
        return response.choices[0].message.content
    except Exception as e:
        print(f"API 호출 오류: {e}")
        return "평가 오류가 발생했습니다."

def main():
    # PDF 파일 목록 가져오기
    pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))
    
    if not pdf_files:
        print(f"'{folder_path}' 폴더에 PDF 파일이 없습니다.")
        return
    
    # 결과를 저장할 파일 경로
    result_file = os.path.join(folder_path, "평가_결과.txt")
    
    with open(result_file, 'w', encoding='utf-8') as f:
        f.write("PDF 파일 평가 결과\n")
        f.write("=" * 50 + "\n\n")
    
    # 각 PDF 파일 처리
    for pdf_file in pdf_files:
        print(f"처리 중: {os.path.basename(pdf_file)}")
        
        # PDF에서 텍스트 추출
        text = extract_text_from_pdf(pdf_file)
        
        if text:
            # 추출된 텍스트 평가
            evaluation = evaluate_content(text)
            
            # 결과 저장
            with open(result_file, 'a', encoding='utf-8') as f:
                f.write(f"파일: {os.path.basename(pdf_file)}\n")
                f.write("-" * 40 + "\n")
                f.write(f"평가:\n{evaluation}\n\n")
                f.write("=" * 50 + "\n\n")
            
            print(f"평가 완료: {os.path.basename(pdf_file)}")
            
            # API 호출 사이에 잠시 대기 (rate limit 방지)
            time.sleep(1)
        else:
            print(f"텍스트 추출 실패: {os.path.basename(pdf_file)}")
            
    # 종합 결과 파일 생성 (엑셀로 볼 수 있는 CSV 형식)
    csv_result_file = os.path.join(folder_path, "평가_결과_요약.csv")
    
    with open(csv_result_file, 'w', encoding='utf-8') as f:
        f.write("파일명,점수,코멘트\n")
        
        # 텍스트 파일에서 결과 추출하여 CSV로 정리
        with open(result_file, 'r', encoding='utf-8') as rf:
            lines = rf.readlines()
            
            current_file = ""
            for line in lines:
                if line.startswith("파일:"):
                    current_file = line.replace("파일:", "").strip()
                elif "점" in line and "/" in line:  # 점수 부분 찾기
                    parts = line.split()
                    for part in parts:
                        if "점" in part and "/" in part:
                            score = part.split("/")[0]
                            comment = line.replace(part, "").strip()
                            f.write(f'"{current_file}",{score},"{comment}"\n')
                            break

if __name__ == "__main__":
    main()
    print("모든 PDF 파일 평가가 완료되었습니다.")
    print("평가 결과는 '평가_결과.txt'와 '평가_결과_요약.csv' 파일에 저장되었습니다.")
