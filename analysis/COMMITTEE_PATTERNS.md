# Committee Pattern'lari ve Onay Sureci
> Tarih: Nisan 2026
> Kaynak: 226 FA thread analizi, tokenomics mailing list

---

## 1. Committee Uyeleri

| Isim | Kurum | Rol | Aktivite Seviyesi |
|------|-------|-----|-------------------|
| **Amanda Martin** | Linux Foundation (Canton Foundation COO) | Koordinator -- tum thread'leri yonetiyor | En aktif |
| **Eric Saraniecki** | Digital Asset (co-founder) | Teknik sorumlu -- BME, Activity Marker | Cok aktif |
| **Kinga Bosse** | MPCH (COO) | Oy veriyor, hizli approve | Aktif |
| **Chris Kelly** | IntellectEU | Teknik sorular soruyor | Aktif |
| **Prakash Neelakantan** | Broadridge | Oy veriyor | Orta |
| **Chris Zuehlke** | Cumberland DRW | Oy veriyor | Orta |
| **Chris Matturri** | Proof Group | Oy veriyor | Az |
| **Veronica Augustsson** | 7RIDGE/C7 | Oy veriyor | Az |
| **Juan Costa** | (Super Validator?) | Tokenomics mekanizmasi sorguluyor | Az ama etkili |

---

## 2. Onay Pattern'lari

### Pattern A: Hizli Onay (1-3 gun)
**Ornek:** Orphil LLC (Agentic Ledger)

```
1. Basvuru gelir (Amanda iletir)
2. Sirket guncelleme yapar (Activity Marker netlestirir)
3. Amanda async vote acar: "Any questions or concerns?"
4. MPCH: "MPCH approves"
5. IntellectEU: "IEU approves"
6. Cumberland DRW: "Cumberland DRW approves"
7. Proof Group: "Proof Group approves"
8. 7RIDGE: "7RIDGE/C7 approves"
9. Amanda: "We have enough votes. I will make the announcement."
```

**Neden hizli?** Activity Marker kullanimi net yazilmis, "No markers for reads" diyerek farming itirazini bastan kesmis.

### Pattern B: Orta Uzunluk (1-4 hafta)
**Ornek:** HandlPay by Verso Network AG

```
1. Basvuru gelir
2. Juan soru sorar: "Privacy nasil calisiyor? Farming riski?"
3. Eric yanitlar: "CC public ama stablecoin private"
4. Juan tekrar: "10dk'da bir CC drip = kurumsal musteriyle ayni odul, adil mi?"
5. Eric: "BME'de elastic/inelastic ayrimi var"
6. Amanda: "Async vote yapalim mi? Video ister misiniz?"
7. Sirket video gonderir
8. Amanda guncelleme iletir
9. Thread acik kalir...
```

**Neden yavas?** Farming/gaming riski sorusu -- committee'nin hassas noktasi.

### Pattern C: Takili / Uzun (1+ ay)
- Activity Marker plani belirsiz
- "What exactly triggers the marker?" sorusuna net cevap yok
- Testnet aktivitesi gosterilememis
- Demo video yok

### Pattern D: Withdrawn
- Committee sorulari yanitsiz kalininca basvurucu geri cekiyor
- Ornek: `[WITHDRAWN] BitDynamics AB - Cantonmarkets`

---

## 3. Committee'nin Sordugu Sorular

### En Sik Sorulanlar (Her basvuruda bekle)

| # | Soru | Kim Soruyor | Neden Onemli |
|---|------|------------|--------------|
| 1 | "What exactly triggers the Activity Marker?" | Eric Saraniecki | En sik sorulan soru |
| 2 | "Is this elastic or inelastic activity?" | Eric Saraniecki | BME perspektifi |
| 3 | "How does this avoid farming/gaming the rewards?" | Eric / Juan | Drip incentive, sybil riski |
| 4 | "Does this use CC or Activity Markers for rewards?" | Eric Saraniecki | Ikisi farkli, net olmali |
| 5 | "What is the party ID structure?" | Amanda Martin | Format kontrolu |
| 6 | "How many active users / traction?" | Genel committee | Testnet + kullanici sayisi |
| 7 | "Can you provide a video demo?" | Amanda Martin | Async vote icin kritik |
| 8 | "Who will be your first customers?" | Genel committee | Somut isim isteniyor |
| 9 | "How would not having FA status change your plans?" | Form sorusu | "It wouldn't" = oldurucu |
| 10 | "Canton ismini neden kullandiniz?" | Juan Costa | Trademark ihlali |

### Tehlikeli Sorular

| Soru | Tuzak | Dogru Cevap |
|------|-------|-------------|
| "Neden FA olmadan launch edemiyorsunuz?" | "It wouldn't" demek = neden FA istiyor? | "Vault execution fee'leri CC cinsinden -- FA odulleri bu fee'yi kullaniciya subsidize etmemizi sagliyor" |
| "144 tx sadece billing -- gercek usage?" | API call basina marker planlayanlar vuruldu | Transaction basina degil, vault execution basina marker |
| "Privacy feature CC icin de mi?" | HandlPay'i revize ettirdi | Net teknik aciklama hazirla |

---

## 4. Onay Icin Gereken Unsurlar

Basarili basvurularda ortak olan:

1. **Net Party ID** -- `company-mainnet-1::1220[hash]` formatinda, mainnet'te aktif
2. **Somut Activity Marker plani** -- "X event oldugunda marker tetiklenir"
3. **Testnet/mainnet aktivite kaniti** -- Basvuru aninda calisiyor olmali
4. **Kullanici buyume rakamlari** -- MAU, transaction count, growth %
5. **Farming karsiti mekanizma** -- Committee'ye "gaming yok" guvencesi
6. **Video demo** (Google Drive, 16:9) -- Async vote icin kritik
7. **Hizli yanit suresi** -- Amanda'nin sorulari 24-48 saat icinde yanitlanmali
8. **Ilk musteri adi** -- En az bir "X sirketi kullanacak" taahhüdü

---

## 5. Kesinlikle Yapilmamalari

1. **"Canton" kelimesini uygulama adina koymak** -- trademark ihlali
2. **API call basina activity marker** -- farming, reddedilir
3. **Her imzada marker tetikleme** -- farming riski
4. **"FA olmadan da launch ederiz" demek** -- oldurucu
5. **TBC Party ID ile basvurmak** -- gecikme
6. **Demo olmadan basvurmak** -- "Next step: demo" dongusune girer

---

## 6. Basarili Basvuru Ornekleri

| Uygulama | Kritik Unsur | Onay Suresi |
|----------|-------------|-------------|
| Copper Custody | "Cumberland has been using the app for several months" | 7 gun |
| Orphil (Agentic Ledger) | Net marker plani, "No markers for reads" | 1 gun |
| Zodia Custody | FCA lisansli, bank-bred custodian | ~2-3 hafta |
| HydraX / Metra | MAS lisansli broker-dealer | Kosullu onay |
| Bron Foundation | Cross-chain swap, USDC->CC koprusu | 7 gun |

**Ortak tema:** Ya lisans/regulasyon ya da gercek musteri adi -- biri mutlaka var.

---

## 7. Onay Sureci Adimlari

```
1. Mainnet'e 2 hafta kala veya yeni cikinca form doldur
   -> canton.foundation/featured-app-request/
2. Amanda Martin formu alir, committee'ye iletir
3. Committee responsible persons'i toplantiya davet eder (5 dk sunum + Q&A)
4. Toplantida yeterli bilgi varsa oy -> yoksa async vote
5. Async vote: committee uyeleri email uzerinden oy kullanir
6. Onay sonrasi 2 hafta icinde on-chain governance action
7. Activity marker kullaniliyorsa 2 hafta icinde agirlik belirlenir
```

---

## 8. Iletisim Bilgileri

| Kisi | Email | Rol |
|------|-------|-----|
| Amanda Martin | amartin@linuxfoundation.org | Surucu yonetiyor, ilk temas noktasi |
| Eric Saraniecki | eric@digitalasset.com | Teknik sorular |
| Genel | operations@sync.global | FA operasyon sorulari |
| Tokenomics listesi | tokenomics@lists.sync.global | Mailing list |
| Abone ol | tokenomics+subscribe@lists.sync.global | Listeye katilim |

---

*Son guncelleme: Nisan 2026*
