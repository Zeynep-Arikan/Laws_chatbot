# Chatbot ana fonksiyonu
from web_search import web_chat

def main():
    print("Kadın Hakları Chatbot'una hoş geldiniz.")
    # Sadece web araması yapılıyor; PDF arama seçeneği kaldırıldı.
    web_chat()

if __name__ == "__main__":
    main()