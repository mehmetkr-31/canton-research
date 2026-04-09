# Canton Ekosistem Analizi
> Son güncelleme: Nisan 2026  
> Kaynaklar: canton.foundation, canton.network, fa_messages.json, canton-dev-fund GitHub

---

## 1. Canton Foundation — Yapı ve Yönetim

### Kimdir?
Canton Foundation (eski adı: Global Synchronizer Foundation / GSF), Canton Network'ün Global Synchronizer'ını yöneten bağımsız vakıf. Amaç: tarafsız yönetim, şeffaf karar alma, ekosistem büyümesi.

**Resmi web sitesi:** https://canton.foundation  
**Executive Director:** Melvis Langyintuo (eski OKX, Goldman Sachs, JPMorgan)  
**COO:** Amanda Martin (FA başvurularını yöneten kişi — eski Linux Foundation)  
**Developer Relations:** Jatin Pandya

### Ağ İstatistikleri (Nisan 2026)
| Metrik | Değer |
|--------|-------|
| Super Validator Nodes | 45 |
| Total Validators | 865 |
| Daily Fees | $2.3M |
| Coin Supply | 38.3B CC |

---

## 2. Super Validator Listesi (Tam)

Super Validator'lar yönetim kararlarında oy hakkına sahip. FA başvurularını onaylayan committee bu kurumlardan oluşuyor.

5North, 7Ridge, Angelhack, BitGo, Bitwave, Broadridge, Canton Foundation, Chainlink, Circle, CoinMetrics, Copper, **Cumberland**, Dfns, **Digital Asset**, Elliptic, Figment, Hypernative, **IntellectEU**, Kaiko, Kiln, LayerZero, Ledger, Liberty City Ventures, Lukka, **MPCH**, Obsidian Systems, **Proof Group**, Quantstamp, SBI, Taurus, **Tradeweb**, TRM, Zenith, zerohash, Orb-1-LP

**Tokenomics Committee'de aktif olanlar:**
- Eric Saraniecki (Digital Asset co-founder) — en etkili karar verici
- Amanda Martin (Canton Foundation COO) — süreci yönetiyor
- Kinga Bosse (MPCH COO)
- Chris Kelly (IntellectEU)
- Juan Costa (COO)
- Chris Zuehlke (Cumberland Global Head)

---

## 3. Foundation Üyeleri

### Premier Üyeler
5North, 7Ridge, BNP Paribas, BNY, Broadridge, Cumberland, Digital Asset, **DTCC**, **Euroclear**, HSBC, IntellectEU, Liberty City Ventures, Liquidity Tech, Obsidian Systems, SBI, T-RIZE, Tradeweb

> Not: DTCC + Canton ortaklığı — DTC-Custodied U.S. Treasury Securities tokenizasyonu 2026 hedefi

### General Üyeler (Seçilmiş)
Angelhack, BitSafe, Blockdaemon, Chainlink Labs, **Copper**, Fairmint, Figment, Kaiko, Kaleido, LayerZero, **MPCH**, Moody's, **Zodia Custody**, Proof Group, The Tie, TRM Labs, Taurus, Ubyx, Send, Redstone

---

## 4. Featured App (FA) Programı

### Nedir?
Featured App = Canton Network'ün resmi olarak onayladığı ve CC (Canton Coin) ödülü kazanma hakkına sahip uygulamalar.

**FA başvuru sayfası:** https://canton.foundation/featured-app-request/

### KRITIK KURAL: Ne Zaman Başvurulur?
> **"Apply within two weeks of MainNet launch."**
> 
> *"You should only apply for FA designation when your application is within two weeks of launching on MainNet. If that is not the case, the Committee will request you reapply when within that time frame."*

**Çeviri:** Mainnet'e almadan 2 hafta önce veya mainnet'e aldıktan sonra başvurun. Daha erken başvurmak = commitee sizi geri gönderir.

### Başvuru Formu — Tüm Alanlar
1. Email (Zorunlu)
2. Name of applying institution (Zorunlu)
3. Summary of Company and Background (Zorunlu)
4. Name of the application (Zorunlu)
   - **DİKKAT:** "Canton" kelimesi uygulama adında KULLANILAMAZ
5. URL of the applying institution (Zorunlu)
6. Product Website
7. Emails for Responsible Persons
8. **Party ID for the Featured Application**
9. URL for the public code repository (if available)
10. Link to Brand Materials (optional)
11. **Demo Video 16:9 ratio (optional ama pratikte ZORUNLU)**

**Application Details:**
12. Provide a summary of what your application will do (Zorunlu) — sosyal medya/web için kullanılır
13. Describe the expected users (Zorunlu)
14. **How will your application interact with Canton Network and leverage Canton Coin and Activity Markets for application rewards?** (Zorunlu)
15. Describe how your application will interact with the ledger (Zorunlu)
16. **Describe the activities that your application will earn application rewards from** (Zorunlu)
17. **Does this activity use Canton Coin or Activity Markers to generate rewards?** (Zorunlu)
18. For the reward earning use case, estimates (Zorunlu):
    - On a per user basis, what is your expected daily number of transactions
    - Under what conditions may a user generate multiple transactions per round/epoch?
    - How do you expect your transactions to scale as your customer base scales?
19. What is your anticipated launch date on MainNet? (Zorunlu)
20. **Who will be your first customers and what is the expected go-live dates?** (Zorunlu)
21. **How would not having FA status change your operating plans?** (Zorunlu)
22. **Does your application have any controls to prevent non-bona fide transactions?** (Zorunlu)
23. Is your application smart contract audited? (Zorunlu)

### Onay Sonrası Yükümlülükler
- **1 aylık rapor:** Mainnet'e çıkıştan 1 ay sonra Tokenomics call'da sunum
  - Günlük işlem sayısı (use case bazlı)
  - Round başına maksimum işlem
  - Activity marker mı yoksa CC transfer mı
  - Başlangıç ve bitiş kullanıcı sayısı
- **Çeyreklik raporlama:** Her 3 ayda bir aynı format
- **Kapsam ihlali = status iptal:** Onaylanan kapsam dışında aktivite tespit edilirse uyarı, ardından iptal
- **Ödül ağırlığı her an değiştirilebilir**
- **FA status her an iptal edilebilir**

### FA Başvuru Süreci Adımları
```
1. Mainnet'e 2 hafta kala veya yeni çıkınca form doldur
   → canton.foundation/featured-app-request/
2. Amanda Martin formu alır, committee'ye iletir
3. Committee responsible persons'ı toplantıya davet eder (5 dk sunum + Q&A)
4. Toplantıda yeterli bilgi varsa oy → yoksa async vote
5. Async vote: committee üyeleri email üzerinden oy kullanır
6. Onay sonrası 2 hafta içinde on-chain governance action
7. Activity marker kullanılıyorsa 2 hafta içinde ağırlık belirlenir
```

---

## 5. Protocol Development Fund (Grants Programı)

**GitHub:** https://github.com/canton-foundation/canton-dev-fund  
**Uygulama:** https://canton.foundation/grants-program/

### Nedir?
Tüm network ödüllerinin **%5'i** Protocol Development Fund'a ayrılır (CIP-0082).  
Para kaynağı: SV rewards + App Rewards + Validator Rewards'tan pro-rata kesinti.  
Para birimi: Canton Coin (CC).  
Ödeme: Milestone bazlı.

### FA vs Dev Fund Farkı
| | **Featured App** | **Dev Fund** |
|--|-----------------|--------------|
| Amaç | Uygulama onayı — sürekli CC ödülü | Geliştirme finansmanı — tek seferlik grant |
| Başvuru | FA form (canton.foundation) | GitHub PR |
| Kapsam | Son kullanıcı uygulaması | Açık kaynak altyapı, ortak fayda |
| Şart | Mainnet'te canlı | Açık kaynak veya shared benefit |
| Yönetim | Tokenomics Committee | Tech & Ops Committee |

### Dev Fund'a Kimler Başvurabilir?
- Foundation üyeleri: direkt başvuru
- Dışarıdan gelenlerin bir Tech & Ops Committee üyesi "champion" olarak desteklemesi gerekiyor
- Community: champion bulursa başvurabilir

### Dev Fund'da Onaylanan 5 Proje (Nisan 2026)
| PR | Proje | Kim | CC Miktarı | Süre |
|----|-------|-----|-----------|------|
| #76 | Logical Synchronizer Upgrades | Digital Asset (Wayne Collier) | 12M CC | 18 gün |
| #53 | ISS-Based BFT | Digital Asset (Wayne Collier) | 20M CC | 17 gün |
| #97 | Token Standard V2 | Digital Asset (Bernhard Elsner) | 12M CC | 15 gün |
| #32 | Daml3 Training | Obsidian Systems | 5.29M CC | 24 gün |
| #130 | Daml Package Analyzer | Certora | 2.01M CC | 9 gün |

### PR #15 — Nexus Framework (Bizim Başvurumuz)
- **Durum:** Needs Revision
- **Label:** canton-apis
- **Son hareket:** 6 Nisan 2026 — ping yorumu atıldı, 5 reviewer bildirim aldı
- **İlerleme:** hythloda'nın 4 sorusu yanıtlandı, kod repo'su paylaşıldı

---

## 6. Canton Network — Teknik Mimari

**Resmi site:** https://www.canton.network  
**Developer docs:** https://docs.digitalasset.com/

### Temel Özellikler
- **Privacy-first:** Kurumsal kullanım için programlanabilir gizlilik
- **DAML:** Akıllı kontrat dili (Haskell tabanlı)
- **Global Synchronizer:** Atomic cross-chain transaction altyapısı
- **Canton Coin (CC):** Native token — network fees, FA rewards, Dev Fund

### Uygulama Kategorileri (canton.foundation'dan)
1. Blockchain Explorers
2. Bridges / Oracles
3. **Custodians & Wallets** ← bizim kategorimiz
4. Daml Dev Solutions
5. Data & Analytics
6. DeFi
7. NaaS (Node-as-a-Service)
8. Tokenization

### Use Cases (canton.network'ten)
- Crypto Derivatives
- 24x7 On-chain Financing
- Private Stablecoin Payments
- Asset Tokenization
- Custody & Wallets
- Collateral Mobility

### Önemli Haberler
- **DTCC + Canton:** DTC-Custodied U.S. Treasury tokenizasyonu — 2026 hedefi
- **Digital Asset $135M fundraise:** Canton Network büyümesini hızlandırma
- **LSEG Digital Settlement Platform:** Bloomberg haberleşti (Ocak 2026)
- **Tokenized Treasuries $10B+:** Markets Media (Ocak 2026)

---

## 7. Ekosisteme Giriş İçin İletişim Kanalları

| Kanal | Amaç | Adres |
|-------|------|-------|
| FA Başvurusu | Tokenomics Committee | tokenomics+subscribe@lists.sync.global |
| FA Soruları | Genel operasyon | operations@sync.global |
| Dev Fund | GitHub PR | github.com/canton-foundation/canton-dev-fund |
| Developer | Jatin Pandya | canton.foundation/contact-us |
| BD (Avrupa) | Bo Zhang | canton.foundation/contact-us |
| BD (APAC/Orta Doğu) | Parth Chaturvedi | canton.foundation/contact-us |
| Discord | Geliştirici topluluğu | discord.gg/canton |
| Telegram | Topluluk | t.me/CantonNetwork1 |
| Twitter/X | Canton Foundation | @CantonFdn |
| Twitter/X | Canton Network | @cantonnetwork |

---

## 8. Validator Node Gereksinimleri

### Party ID Formatları
```
[app-name]-mainnet-[n]::1220[64 hex karakter]
Örnek: multisig-vault-mainnet-1::1220a4b5c6d7e8f9...

MPCH altyapısı kullananlar:
MPCH-[identifier]-[n]::1220[64 hex karakter]

Eski format (auth0 tabanlı):
auth0_[id]::[1220hex]
```

### Validator Seçenekleri
- **Self-hosted:** Kendi altyapın — tam kontrol
- **Managed (MPCH):** MPCH'nin altyapısını kullan — birden fazla FA bu yolu kullandı
- **Managed (Catalyst/IntellectEU):** Alternatif managed provider

### Mainnet Zamanlaması
- Minimum bekleme süresi yok
- Ditto Network: 7 gün sonra başvurdu
- Nuxaris: 3 gün sonra başvurdu
- Önemli olan: başvuru anında mainnet'te canlı olması

---

## 9. CC Ödül Mekanizması

### Nasıl Çalışır?
```
FA'nın Party ID'si + FeaturedAppRight kontratı
         ↓
Vault execution / CC transfer / Activity Marker
         ↓
Aynı atomik işlemde FeaturedAppRight.exercise()
         ↓
Round sonunda (~her 10 dakika) Global Synchronizer dağıtır
         ↓
CC mint edilir → FA'nın Party ID'sine gönderilir
```

### Ödül Türleri
| Tür | Mekanizma | Committee Görüşü |
|-----|-----------|-----------------|
| CC Transfer | Otomatik — CC harcandığında | Tercih edilen |
| Activity Marker | Manuel — FeaturedAppRight.exercise() | Kabul ama şüpheli |
| Cantara Billing | The Tie'ın platformu üzerinden | Kabul ama bağımlılık riski |

### Elastic vs Inelastic (Eric Saraniecki'den)
- **Elastic:** $1 harcayıp >$1 kazanmak — BME'de ekonomik ömrü biter
- **Inelastic:** Kullanıcı gerçekten CC ödiyor, uygulama tutuyor — BME'de bile karlı
- **Multisig için:** Vault execution fee = inelastic ✓

### Standart Billing Cadence
- 144 işlem/kullanıcı/gün = round başına 1 işlem (Cantara modeli)

---

## 10. Wallet/Custody Kategorisi — Onaylı Uygulamalar

| Uygulama | Şirket | Durum | Party ID Formatı |
|----------|--------|-------|-----------------|
| Copper Custody | Copper.co | LIVE (Jan 2025) | `55b1197e-...::1220...` |
| Metra | HydraX | ONAYLANDI (Mar 2025) | `a831fc43-...::1220...` |
| Zodia Custody | Zodia | Async vote | `ZodiaCustody-validator-1::1220...` |
| HandlPay | Verso Network | Async vote | `handlpay-main-1::1220...` |
| Cansai (iOS) | Tenkai GmbH | Demo aşaması | `tenkai-main-1::1220...` |
| Republic Wallet | Republic Crypto | Demo aşaması | `Republic-validator-1::1220...` |
| BitGo Qualified Custody | BitGo | Başvuruldu | Belirtilmemiş |

### Henüz Yapılmamış (Boşluk)
**Kurumsal multisig + mobil (iOS/Android) + web + swap + policy engine = 0 uygulama**

---

## 11. FA Başvurusu için Kritik Kurallar

### KESİNLİKLE YAPILMAMASI GEREKENLER
1. **"Canton" kelimesini uygulama adına koymak** — trademark ihlali, zorla değiştirtilir
2. **API call başına activity marker** — farming, reddedilir
3. **Her imzada marker tetikleme** — farming riski, committee bunu sorgular
4. **"FA olmadan da launch ederiz"** demek — "Neden FA istiyor ki?" sorusunu doğurur
5. **TBC Party ID ile başvurmak** — gecikmeye yol açar
6. **Demo olmadan başvurmak** — "Next step: demo" döngüsünde takılırsınız

### KESİNLİKLE YAPILMASI GEREKENLER
1. Başvuruda mainnet Party ID hazır olmalı
2. Demo video (Google Drive veya YouTube, 16:9)
3. İlk müşteri adı — en az bir "X şirketi kullanacak" taahhüdü
4. CC transfer tabanlı ödül mekanizması (marker değil)
5. Farming önlemi açıkça yazılmış
6. Amanda Martin'in sorusuna 24 saat içinde yanıt

---

## 12. Sıradaki Adımlar — Wallet/Multisig Projesi için Yol Haritası

### Başvuru Zamanlaması
```
Resmi kural: Mainnet'e 2 hafta kala VEYA mainnet'e çıktıktan sonra

YANLIŞ:  Fikir aşamasında başvur (committee geri gönderir)
YANLIŞ:  Testnet'teyken başvur (mainnet şart)
DOĞRU:   MVP mainnet'te çalışıyor + demo video + ilk müşteri adı hazır
```

### Zaman Çizelgesi
```
ŞİMDİ         → Scope netleştir, ilk müşteri adayı belirle
1-3 AY        → Testnet/Devnet'te MVP yap (temel multisig akışı)
3-5 AY        → Mainnet'e al, validator node kur, Party ID oluştur
5. AY         → Demo video çek, FA başvurusu gönder
5-7. AY       → Committee süreci, onay
```

### Başvuruda Güçlü Olması Gereken Yanıtlar
| Soru | Güçlü Cevap Örneği |
|------|-------------------|
| İlk müşteri | "[X şirketi] pilot anlaşması imzalandı" |
| Farming önlemi | "M-of-N insan imzası zorunlu — farming için tüm imzacıların koordinasyonu gerekir, ekonomik olarak anlamsız" |
| Neden FA? | "Vault execution fee'leri CC cinsinden — FA ödülleri bu fee'yi kullanıcıya subsidize etmemizi sağlıyor, rekabetçi fiyatlandırma için kritik" |
| CC/Marker | "CC transfer — vault execution her zaman CC fee gerektiriyor, ayrıca marker yok" |
| Günlük tx | "Vault execute başına 1 işlem — kullanıcı başına aylık ortalama 5-10 execute bekliyoruz" |

---

## 13. Faydalı Linkler

| Kaynak | URL |
|--------|-----|
| Canton Foundation | https://canton.foundation |
| Canton Network | https://www.canton.network |
| FA Başvurusu | https://canton.foundation/featured-app-request/ |
| Dev Fund | https://canton.foundation/grants-program/ |
| Dev Fund GitHub | https://github.com/canton-foundation/canton-dev-fund |
| Ekosistem Apps | https://www.cantonecosystem.com/ |
| Mainnet Docs | https://docs.sync.global/ |
| Testnet Docs | https://docs.test.sync.global/ |
| DevNet Docs | https://docs.dev.sync.global/ |
| Developer Docs | https://docs.digitalasset.com/ |
| SV Network Status | https://canton.foundation/sv-network-status/ |
| Brand Guidelines | https://www.canton.network/brand-kit-trademark-use |
| Discord | https://discord.gg/canton |
| Telegram | https://t.me/CantonNetwork1 |
| Twitter Canton Fdn | https://x.com/CantonFdn |
| Twitter Canton Net | https://x.com/cantonnetwork |
