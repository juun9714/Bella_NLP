
text = open("jwh.txt",'r').readline()
# 문장을 나누고 각 문장을 단어별로 분할하여 리스트로 저장
tokenized_text=[sentence.split() for sentence in text.split(". ")]
# 결과 확인
print(tokenized_text)

# 문장 수
num_sentences = len(tokenized_text)
# 전체 문자 개수, 문자 종류
new_text=text.replace('.',' ').replace(',',' ').replace('\'',' ') # ' , . 삭제
total_characters = len(''.join(new_text.split())) # 띄어쓰기로 쪼개서, 띄어쓰기 없애고 합치기
unique_characters = len(set(''.join(new_text.split())))

# 전체 단어 수, 단어 종류 수
all_words = [word for sentence in tokenized_text for word in sentence]
total_words = len(all_words)
unique_words = len(set(all_words))

# 문장의 단어 개수의 평균
average_word_count = total_words / num_sentences

# 결과 출력
print("1) text의 크기(size):", len(text))
print("2) 문장의 개수:", num_sentences)
print("3) 전체 문자의 개수(순수 알파벳만):", total_characters)
print("   문자의 종류:", unique_characters)
print("4) 전체 단어의 수:", total_words)
print("   단어의 종류의 수:", unique_words)
print("5) 문장의 단어 개수의 평균:", average_word_count)
