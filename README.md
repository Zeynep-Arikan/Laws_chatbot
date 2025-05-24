# Kadın Hakları Chatbot

Bu proje, LangChain framework'ü kullanarak Türkiye'de kadın hakları ve yasaları hakkında bilgi sağlayan bir chatbot uygulamasıdır. Proje, web kaynaklarından ve PDF dökümanlarından bilgi çekerek, kullanıcı sorularına yanıt vermek üzere modüler bir yapıda geliştirilmiştir.

## Özellikler

- **Web Arama:** İlgili web sitelerinden dokümanları çekip, metin parçalarına ayırır ve vektör veritabanına ekler.
- **PDF Arama :** PDF dökümanlarından veri çekip arama yapabildiğiniz modül (kullanılmıyorsa kaldırılabilir).
- **Sohbet Bazlı Sorgulama:** Kullanıcı sorularına, bilgi kaynaklarından çıkarılan verilerle yanıt üretir.
- **LLM API Kullanımı:** Hugging Face Hub üzerinden `mistralai/Mistral-7B-Instruct-v0.2` modelini kullanarak yanıt oluşturur.

## Kurulum

1. **Python Gereksinimleri:**  
   Python 3.8 ve üstü bir sürüm kullanmanızı öneririz.

2. **Gerekli Paketlerin Kurulumu:**  
   Terminalde proje dizinine gidip aşağıdaki komutları çalıştırın:

   ````bash
   pip install -U langchain
   pip install -U langchain-community
   pip install -U llama-cpp-python
   pip install -U langchain-openai