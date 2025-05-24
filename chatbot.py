from web_search import web_chat
from pdf_search import pdf_chat_from_folder  # Yeni fonksiyonu buraya import et

def main():
    print("Kadın Hakları Chatbot'una hoş geldiniz.")
    print("Arama modu seçiniz:")
    print("1 - PDF Arama")
    print("2 - Web Arama")
    print("çık - Çıkış")

    while True:
        secim = input("Seçiminiz (1/2/çık): ").strip().lower()

        if secim == "1":
            pdf_chat_from_folder("dosyalar")
        elif secim == "2":
            web_chat()
        elif secim in ["çık", "exit", "quit"]:
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen 1, 2 veya 'çık' yazınız.")

if __name__ == "__main__":
    main()
