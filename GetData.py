import openai
# Đặt API key của bạn
openai.api_key = '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'
# trang check engine
#https://stackoverflow.com/questions/77789886/openai-api-error-the-model-text-davinci-003-has-been-deprecated
# Gửi yêu cầu và nhận kết quả
response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",  # Chọn mô hình GPT-3
    prompt="làm thế nào để yêu đời?",
    max_tokens=1000  # Số lượng từ tối đa trong kết quả
)
# In kết quả
print(response.choices[0].text)
