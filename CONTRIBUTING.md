# Katki Rehberi

Bu repo'ya katki yapmak icin asagidaki kurallara uy.

## Nasil Katki Yapilir

### 1. Yeni Arastirma / Bilgi Ekleme

- `analysis/` klasorune yeni `.md` dosyasi ekle veya mevcut dosyayi guncelle
- Dosya adi: `BUYUK_HARFLER_VE_ALT_CIZGI.md` formati
- Her dosyanin basinda tarih ve kaynak belirt

Ornek:
```markdown
# Konu Basligi
> Tarih: Nisan 2026
> Kaynak: [URL veya aciklama]

---

Icerik buraya...
```

### 2. Strateji Guncellemesi

- `strategy/` klasorundeki dosyalari guncelle
- Musteri listesi degisti mi? `CUSTOMER_TARGETS.md`'yi guncelle
- Yeni proje fikri mi? `PROJECT_IDEAS.md`'ye ekle

### 3. Toplanti Notlari

- `meeting-notes/` klasorune `YYYY-MM-DD_konu.md` formatiyla ekle
- Ornek: `2026-04-10_ilk-toplanti.md`

### 4. Yeni Veri

- Ham veriler `data/` klasorune
- JSON, CSV veya MD formati tercih et
- Buyuk dosyalar icin `.zip` kullan

## Dosya Formati

- Tum dokumanlar Markdown (`.md`) formatinda
- Turkce yaziyoruz
- Tablolar icin GitHub-flavored markdown kullan
- Kod bloklari icin ``` kullan

## Git Workflow

1. Kendi branch'ini ac:
   ```bash
   git checkout -b feature/yeni-arastirma
   ```

2. Degisikliklerini yap ve commit et:
   ```bash
   git add .
   git commit -m "analysis: FA onay sureci detayli analiz eklendi"
   ```

3. Push et ve PR ac:
   ```bash
   git push origin feature/yeni-arastirma
   ```

4. GitHub'da Pull Request olustur

### Commit Mesaji Formati

```
[klasor]: [ne yapildi]
```

Ornekler:
- `analysis: ekosistem analizine yeni FA verileri eklendi`
- `strategy: musteri listesi guncellendi`
- `data: yeni mailing list verileri eklendi`
- `meeting-notes: 10 Nisan toplanti notlari`

## Oncelik Sirasi

Simdilik en onemli katkialar:

1. **Yeni FA basvurularini takip etmek** -- mailing list'ten yeni basvurulari `data/`'ya eklemek
2. **Rakip takibi** -- Timelock Labs, SyncVotes gibi rakiplerin durumunu guncellemek
3. **Musteri gorusmeleri** -- Discord/Telegram'da yapilan gorusmeleri `meeting-notes/`'a not etmek
4. **Teknik arastirma** -- Daml, Canton API, Splice SDK hakkinda bilgi toplamak
