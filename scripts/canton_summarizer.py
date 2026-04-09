import os
import glob
from bs4 import BeautifulSoup
import google.generativeai as genai
import json

# Gemini API Ayarları
# BURAYA KENDİ GEMINI API ANAHTARINI GİRMELİSİN
GENAI_API_KEY = os.environ.get("GEMINI_API_KEY", "SENIN_API_ANAHTARIN_BURAYA")
genai.configure(api_key=GENAI_API_KEY)

# Gemini 1.5 Flash modelini kullanıyoruz, hızlı ve uygun maliyetli/ücretsiz
model = genai.GenerativeModel('gemini-1.5-flash')

# Hedef Anahtar Kelimelerimiz (İngilizce ve Türkçe varyasyonlarıyla)
KEYWORDS = [
    # Global/Teknik
    "validator", "node", "validatör", "düğüm", "cc", "canton", "daml",
    # Süreç/Eylem
    "başvuru", "application", "uygulama", "app çıkartma", "kurulum", "setup",
    # Geliştirme
    "developer", "geliştirici", "sdk", "api", "dokümantasyon", "documentation",
    "deployment", "dağıtım", "smart contract", "akıllı sözleşme",
    # Proje Özel (Chronos)
    "scheduling", "zamanlama", "transaction", "işlem", "grant", "hibe"
]

def clean_html(filepath):
    """HTML dosyasını okur ve içindeki metni temizleyip çıkarır."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            
            # Script, style ve navbar/footer gibi genelde gereksiz olan bölümleri atıyoruz
            for element in soup(["script", "style", "nav", "footer"]):
                element.extract()
                
            # Saf metni al ve ekstra boşlukları temizle
            text = soup.get_text(separator=' ')
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            return text
    except Exception as e:
        print(f"Hata ({filepath} okunamadı): {e}")
        return None

def find_keywords(text):
    """Metin içindeki hedef anahtar kelimeleri bulur."""
    text_lower = text.lower()
    found_keywords = [word for word in KEYWORDS if word.lower() in text_lower]
    return found_keywords

def summarize_with_gemini(text, found_keywords):
    """Bulunan kelimelere odaklanarak Gemini'den teknik bir özet ister."""
    prompt = f"""
    Sen, Canton Network ve Web3 projeleri (CC, Daml, Validator Node kurulumu vb.) konusunda uzman bir geliştirici asistanısın.
    
    Aşağıdaki metni analiz et ve teknik bir özet çıkar.
    Özellikle metinde geçen şu konulara odaklan: {', '.join(found_keywords)}
    
    Format:
    - Kısa bir genel bakış (1-2 cümle)
    - Önemli teknik detaylar (Madde imleri şeklinde)
    - (Varsa) Kurulum, başvuru veya geliştirme gereksinimleri
    - 'Yapılması Gerekenler' başlığı altında teknik bir aksiyon listesi (Örn: Şu komutu çalıştır, şu formu doldur)
    
    Metin:
    {text[:25000]}
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Özetleme sırasında hata oluştu: {e}"

def process_directory(directory_path):
    """Belirtilen klasördeki tüm HTML dosyalarını tarar."""
    print(f"[{os.path.abspath(directory_path)}] klasörü taranıyor...\n" + "="*50)
    
    # Tüm .html dosyalarını bul
    search_pattern = os.path.join(directory_path, "**", "*.html")
    html_files = glob.glob(search_pattern, recursive=True)
    
    if not html_files:
        print("Uyarı: Klasörde hiç .html dosyası bulunamadı.")
        return

    rapor_icerigi = ""
    json_rapor = []
    
    for filepath in html_files:
        filename = os.path.basename(filepath)
        print(f"\nDosya İşleniyor: {filename}")
        
        # 1. HTML'i temizle
        text = clean_html(filepath)
        if not text or len(text) < 50: # Çok kısa metinleri atla
            print("- Metin bulunamadı veya çok kısa. Atlanıyor.")
            continue
            
        # 2. Anahtar kelimeleri ara
        found_keywords = find_keywords(text)
        score = len(found_keywords)
        
        # 3. Eğer ilgili anahtar kelimeler varsa işle
        if score > 0:
            print(f"- Önem Derecesi: {score} | Bulunan Kelimeler: {', '.join(found_keywords)}")
            print("- Gemini ile özetleniyor...")
            
            ozet = summarize_with_gemini(text, found_keywords)
            
            sonuc = f"\n{'='*50}\n"
            sonuc += f"📄 DOSYA: {filename}\n"
            sonuc += f"🔍 BULUNAN KELİMELER ({score}): {', '.join(found_keywords)}\n\n"
            sonuc += f"📝 ÖZET:\n{ozet}\n"
            sonuc += f"{'='*50}\n"
            
            rapor_icerigi += sonuc
            
            json_rapor.append({
                "dosya": filename,
                "bulunan_kelimeler": found_keywords,
                "skor": score,
                "ozet": ozet
            })
            
            print("- Tamamlandı.")
        else:
            print("- İlgili anahtar kelime bulunamadı. Atlanıyor.")

    # Tüm sonuçları bir rapora kaydet
    if rapor_icerigi:
        report_file = os.path.join(directory_path, "canton_analiz_raporu.txt")
        json_file = os.path.join(directory_path, "canton_analiz_raporu.json")
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("CANTON NETWORK & DAPP BİLGİ MADENCİLİĞİ RAPORU\n")
            f.write("="*50 + "\n")
            f.write(rapor_icerigi)
            
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_rapor, f, ensure_ascii=False, indent=4)
            
        print(f"\n✅ İŞLEM TAMAMLANDI! Özetler '{report_file}' ve '{json_file}' dosyalarına kaydedildi.")
    else:
        print("\nİşlem tamamlandı fakat raporlanacak veri bulunamadı.")

if __name__ == "__main__":
    # Scriptin çalıştığı klasörü hedef klasör olarak belirliyoruz
    hedef_klasor = "."
    process_directory(hedef_klasor)
