# Canton FA Projesi — Sohbet Özeti
> Tarih: Nisan 2026  
> Kapsam: FA başvurusu araştırması, ekosistem analizi, multisig wallet fikri

---

## 1. Ne Yaptık

Bu sohbette şunları araştırdık ve analiz ettik:

- FA (Featured App) mailing list mesajları — 233 başvuru
- Canton Dev Fund GitHub — 153 PR
- canton.foundation ve canton.network siteleri
- Yeni onaylanan FA: HIFI
- PR #15 Nexus Framework durumu
- Potansiyel müşteri adayları

---

## 2. Proje Fikri

**Kurumsal multisig treasury wallet** — Canton Network üzerinde:

| Özellik | Açıklama |
|---------|----------|
| M-of-N multisig | Birden fazla onaylayan zorunlu |
| Mobil (iOS + Android) | React Native — cross-platform |
| Web arayüz | Kurumsal dashboard |
| Policy engine | Harcama limitleri, zaman kilidi, rol bazlı erişim |
| Swap entegrasyonu | Canton.exchange (OpenVector) ile entegrasyon — sıfırdan yazmak değil |
| Audit trail | Tüm imza ve işlem geçmişi on-chain |

**Bu kombinasyonu yapan 233 FA + 153 Dev Fund başvurusu içinde: SIFIR uygulama.**

Send Foundation (Privat Vault) bunu mailing list'te teyit etti:
> *"Canton protocol supports multisigs through decentralized namespaces, but there isn't a UI that natively supports this feature."*

---

## 3. Ekosistem Yapısı

### İki Ayrı Program

| | **Featured App (FA)** | **Dev Fund** |
|--|----------------------|--------------|
| Amaç | Uygulama onayı — sürekli CC ödülü | Geliştirme grant'ı — tek seferlik CC |
| Başvuru | canton.foundation/featured-app-request/ | github.com/canton-foundation/canton-dev-fund |
| Şart | Mainnet'te canlı, demo, ilk müşteri | Açık kaynak, community fayda |
| Yönetim | Tokenomics Committee | Tech & Ops Committee |

### Committee Üyeleri (FA Kararlarını Verenler)
- **Eric Saraniecki** (Digital Asset co-founder) — en etkili
- **Amanda Martin** (Canton Foundation COO) — süreci yönetiyor
- **Kinga Bosse** (MPCH COO)
- **Chris Kelly** (IntellectEU)
- **Juan Costa** (COO)
- **Chris Zuehlke** (Cumberland Global Head)

---

## 4. FA Başvurusu — Kritik Kurallar

### Resmi Zamanlama Kuralı
> *"Apply within two weeks of MainNet launch."*

Fikir/testnet aşamasında başvurmak = committee geri gönderir.

### Onay İçin Altın Formül
```
1. Mainnet'te çalışan demo          → zorunlu
2. Party ID hazır                   → zorunlu (format: [app]-mainnet-1::1220[64hex])
3. İlk müşteri adı                  → kritik
4. CC transfer tabanlı ödül         → committee tercih ediyor (marker değil)
5. Farming önlemi açık yazılmış     → "M-of-N imzası = farming imkansız"
6. "Canton" isminde YOK             → trademark kuralı
7. Demo video (16:9)                → async vote için zorunlu
```

### Kesinlikle Yapılmaması Gerekenler
1. "Canton" kelimesini uygulama adına koymak
2. API call / her imzada activity marker
3. "FA olmadan da launch ederiz" demek
4. TBC Party ID ile başvurmak
5. Demo olmadan başvurmak

### Onay Sonrası Yükümlülükler
- 1 aylık rapor: Mainnet'e çıkıştan 1 ay sonra Tokenomics call'da sunum
- Çeyreklik raporlama: Her 3 ayda bir
- Kapsam ihlali → FA status iptal
- Ödül ağırlığı her an değiştirilebilir

---

## 5. CC Ödül Mekanizması

### Activity Marker vs CC Transfer
| | Activity Marker | CC Transfer |
|--|----------------|-------------|
| Kontrol | Tam — siz tanımlarsınız | Protokol otomatik |
| Farming riski | Yüksek | Düşük |
| Committee görüşü | Şüpheli | Tercih edilen |
| Multisig için | Hayır | Evet |

### Ödül Akışı
```
Vault execute edilir
    ↓
Aynı atomik işlemde FeaturedAppRight.exercise()
    ↓
Activity Marker on-ledger'a yazılır
    ↓
Round sonunda (~10 dakika) Global Synchronizer dağıtır
    ↓
CC mint edilir → FA'nın Party ID'sine gönderilir
```

### Elastic vs Inelastic (Eric Saraniecki)
- **Elastic:** $1 harcayıp >$1 kazanmak — BME'de ekonomik ömrü biter, farming riski
- **Inelastic:** Kullanıcı gerçekten CC ödüyor — BME'de bile karlı, kurumsal modele uygun
- **Multisig için:** Vault execution fee = inelastic ✓

### Cantara — Neden Kullanmayalım?
- The Tie'ın FA'sı — başka bir uygulamaya bağımlılık
- ALUM Labs ve AKASEC terk etti: "moving away from Cantara due to its limitations"
- Multisig için yanlış model: subscription değil, transaction fee modeli
- Kendi CC transfer mekanizmanız daha sağlam

---

## 6. Başarılı Başvuruların Ortak Anatomisi

| Uygulama | Kritik Unsur | Onay Süresi |
|----------|-------------|-------------|
| Copper | "Cumberland has been using the app for several months" | 7 gün |
| Zodia | FCA lisanslı, bank-bred custodian | ~2-3 hafta |
| HydraX | MAS lisanslı broker-dealer | Koşullu onay |
| HandlPay | "Users paid $10-$1000, no drip rewards" | 5+ hafta |
| Bron Foundation | Cross-chain swap, USDC→CC köprüsü | 7 gün |

**Ortak tema:** Ya lisans/regülasyon ya da gerçek müşteri adı — biri mutlaka var.

---

## 7. Beklenmedik Sorular — Hazırlıklı Olunması Gerekenler

| Soru | Kim Sordu | Tuzak |
|------|-----------|-------|
| "Canton ismini neden kullandınız?" | Juan Costa | İsim değiştirmeye zorlandı |
| "Neden FA olmadan launch edemiyorsunuz?" | Chris Zuehlke | Send: "It wouldn't" → öldürücü yanıt |
| "144 tx sadece billing — gerçek usage?" | Juan Costa | API call başına marker planlayanları vurdu |
| "Privacy feature CC için de mi?" | Juan Costa | HandlPay'i revize ettirdi |

**Projeniz için hazır cevap:**
- "Neden FA olmadan olmaz?" → *"Vault execution fee'leri CC cinsinden — FA ödülleri bu fee'yi kullanıcıya subsidize etmemizi sağlıyor, rekabetçi fiyatlandırma için kritik."*
- "Farming önlemi?" → *"M-of-N insan imzası zorunlu — farming için tüm imzacıların koordinasyonu gerekir, ekonomik olarak anlamsız."*

---

## 8. Rakip Analizi

| Rakip | Zayıf Nokta |
|-------|------------|
| Timelock Labs | Web only, demo yok, stall'da, policy engine yok |
| Send/Privat Vault | Stall'da, consumer odaklı, kurumsal değil |
| SyncVotes | DAO odaklı, kurumsal treasury değil, mobil yok |
| Copper/Zodia/BitGo | MPC tabanlı, kurumsal ama native Canton multisig UI yok |

---

## 9. Mobil Mimari

Canton Network'e hiçbir uygulama mobil cihazdan direkt bağlanmıyor. Standart mimari:

```
MOBİL UYGULAMA (React Native / Flutter)
    ↓ REST API
VALIDATOR NODE (Backend — sizin sunucunuz)
    ↓
CANTON NETWORK (Global Synchronizer)
```

**Framework tavsiyesi:**
- JS/React bilen ekip varsa → React Native
- Native mobil deneyim varsa → Flutter
- Dataset'te sadece 1 native iOS wallet var (Cansai/Tenkai) — Android wallet sıfır

---

## 10. Canton Dev Fund — PR #15 Nexus Framework

**Durum:** Needs Revision (18 başvuru arasında)

**Zaman çizelgesi:**
| Tarih | Olay |
|-------|------|
| 22 Şubat 2026 | PR açıldı |
| 19 Mart 2026 | "Dev Fund Incoming" listesine alındı |
| 25 Mart 2026 | hythloda: 4 soru sordu |
| 27 Mart 2026 | 4 soruya yanıt verildi + dosya güncellendi |
| 6 Nisan 2026 | Ping yorumu + nexus repo linki paylaşıldı |
| 6 Nisan 2026 | 5 reviewer (hythloda, tkatrichenko, stas-sbi, waynecollier-da, isegall-da) bildirim aldı |

**Nexus repo:** github.com/mehmetkr-31/nexus  
Paketler: `@nexus-framework/core`, `@nexus-framework/react`, `@nexus-framework/cli`  
Durum: Canlı kod var, README profesyonel, 6 star

**Dev Fund Board Durumu (Nisan 2026):**
| Sütun | Sayı |
|-------|------|
| Incoming | ~40 |
| Needs Champion | ~22 |
| In Review | ~5 |
| Ready for Vote | 3 |
| Approved | 5 |
| Needs Revision | 18 |
| Declined | ~3 |

**Onaylanan 5 proje:** Hepsi Digital Asset (3) veya elite firma (Obsidian, Certora).  
**Dışarıdan onaylanan en hızlı:** CCTools — çalışan ürün + 12 günde 11K kullanıcı → 24 saatte Ready for Vote.

---

## 11. Yeni Onaylanan FA: HIFI

**Başvuru:** 16 Ocak 2026  
**Durum:** Demo aşamasına geçti (onay yolunda)  
**Party ID:** `HIFI-validator-1::1220c44096409d3244021ae82992ccae3a1208fa79cacf450760b6f2cd9dfee2daa6`

**Kim:** Stablecoin altyapı şirketi — API platformu, 130+ ülke, 10B+ hesap, Visa Direct ortağı, SOC 2 Type II, MSB lisanslı.

**Ne yapıyor Canton'da:** Kurumsal hazine otomasyonu, global ödemeler, stablecoin + tokenized U.S. Treasury erişimi.

**Neden onaylandı:**
1. SOC 2 + MSB lisansı — regülatör onaylı
2. Party ID başvuruda hazırdı
3. Visa ortaklığı — Fortune 100 traction kanıtı
4. "Global financial institutions" müşteri profili
5. Tek soru yok, direkt demo'ya geçildi

**Projenizle ilişkisi:** HIFI bir API platformu — geliştirici odaklı. Sizin projeniz son kullanıcı UI'ı. HIFI'nin enterprise müşterileri Canton'a geldiğinde native multisig wallet ihtiyacı doğar → **potansiyel entegrasyon partneri veya dağıtım kanalı.**

---

## 12. Potansiyel Müşteri Adayları

### Tier 1 — En Sıcak (Multisig'e direkt ihtiyaç var)

| # | Şirket | Neden Sıcak | İletişim |
|---|--------|-------------|----------|
| 1 | **Lattice Foundation** | "Corporate treasury + approval workflows" kendi FA'sında yazıyor | https://lattice.cash |
| 2 | **SyncVotes** | "Multi-signature treasuries" kendi ürün spec'inde geçiyor | https://syncvotes.com |
| 3 | **Send Foundation / Privat** | Boşluğu komiteye yazılı teyit etti | https://privat.app |
| 4 | **Ubyx** | Super Validator, kurucu Tony McLaughlin = 30 yıl kurumsal hazine uzmanı | https://ubyx.xyz |
| 5 | **HydraX / Metra** | Ürün spec'inde multi-party signature zorunlu | https://hydrax.io |

### Tier 2 — Sıcak (Kurumsal hazine var, custody çözümü yok)

| # | Şirket | Neden Sıcak | İletişim |
|---|--------|-------------|----------|
| 6 | **HIFI** | Enterprise treasury API, Fortune 100 müşterileri Canton'a geliyor | https://hifi.com |
| 7 | **Launchnodes** | Canton Foundation üyesi, finansal kurumlar için uygulama geliştiriyor | https://launchnodes.com |
| 8 | **Quokka** | Ürün mimarisinde "multi-sig DAOs" geçiyor | https://quokka.living |
| 9 | **TradeChain** | $80M kurumsal sermaye, multi-party onay gerektirir | https://tradechain.finance |
| 10 | **Ditto CCvault** | Kurumsal hazine yield ürünü, custody yok | https://dittonetwork.io |

### Tier 3 — Super Validators (CC hazinesi var)

| # | SV | Neden | Öncelik |
|---|-----|-------|---------|
| 11 | **Cumberland DRW** | Dünyanın en büyük kripto market maker'ı, firma politikası multi-party approval gerektiriyor | Çok yüksek |
| 12 | **MPCH** | Custody şirketi — ürünü anlayacak ilk kişiler | Yüksek |
| 13 | **Republic Crypto** | 500K kullanıcı, kurumsal validator hizmeti | Yüksek |
| 14 | **Proof Group** | Kurumsal yatırım firması | Yüksek |
| 15 | **7RIDGE** | Private markets asset manager | Yüksek |

### Rakip (Takip Et)
- **Timelock Labs** — Aynı konsept, web only, stall'da. Mobil + policy engine ile geride bırakılabilir.

---

## 13. Nasıl Ulaşacağız

### Kanallar (Öncelik Sırasıyla)

**1. Tokenomics Mailing List**
- Adres: tokenomics+subscribe@lists.sync.global
- Önce abone ol, sonra aktif katılımcı ol
- Potansiyel müşteriler orada — mesajlarını oku, yorum yap, tanış

**2. Canton Discord**
- https://discord.gg/canton
- #builders ve #ecosystem kanalları
- Lattice, SyncVotes, Quokka gibi ekipler orada

**3. Canton Telegram**
- https://t.me/CantonNetwork1

**4. Direkt website iletişim**
- Her şirketin contact formu veya email'i

**5. Canton Foundation BD ekibi**
- Bo Zhang (Avrupa): canton.foundation/contact-us
- Parth Chaturvedi (APAC/Orta Doğu): canton.foundation/contact-us
- Teagan Buckley (Global DeFi): canton.foundation/contact-us
- Jatin Pandya (Developer Relations): canton.foundation/contact-us

**6. LinkedIn**
- Super Validator temsilcileri LinkedIn'de aktif
- Chris Zuehlke (Cumberland), Kinga Bosse (MPCH), Tony McLaughlin (Ubyx)

### İlk Mesaj Stratejisi
```
Yanlış: "Merhaba, multisig wallet yapıyoruz, pilot yapar mısınız?"
Doğru:  "Canton'da treasury yönetimi için native multisig UI eksikliğini 
         fark ettik. Send Foundation da bunu teyit etti. Sizin [X workflow] 
         için nasıl bir çözüm kullanıyorsunuz şu an?"
```

---

## 14. Yol Haritası

```
ŞİMDİ (Nisan 2026)
→ Scope netleştir — MVP: temel multisig + web + mobil
→ İlk müşteri adayı belirle (Tier 1 listesinden)
→ FA başvuru formunu taslak yaz
→ Tokenomics mailing list'e abone ol

1-3. AY
→ Testnet/Devnet'te MVP: vault create → imzala → execute
→ Validator node kur (self-hosted veya MPCH/Catalyst managed)
→ Party ID oluştur: [appname]-mainnet-1::1220[hex]
→ React Native mobil + web arayüz

3-5. AY
→ Mainnet deploy
→ Demo video çek (Google Drive, 16:9)
→ İlk müşteri pilot anlaşması imzala
→ FA başvurusu gönder

5-7. AY
→ Committee süreci (Amanda Martin'in sorusuna 24h içinde yanıt)
→ 5 dakika demo sunumu
→ Async vote
→ ONAY
```

---

## 15. Faydalı Linkler

| Kaynak | URL |
|--------|-----|
| FA Başvurusu | https://canton.foundation/featured-app-request/ |
| Dev Fund | https://canton.foundation/grants-program/ |
| Dev Fund GitHub | https://github.com/canton-foundation/canton-dev-fund |
| Nexus PR #15 | https://github.com/canton-foundation/canton-dev-fund/pull/15 |
| Tokenomics Mailing List | https://lists.sync.global/g/tokenomics |
| Mainnet Docs | https://docs.sync.global/ |
| Testnet Docs | https://docs.test.sync.global/ |
| DevNet Docs | https://docs.dev.sync.global/ |
| Developer Docs | https://docs.digitalasset.com/ |
| Ekosistem Apps | https://www.cantonecosystem.com/ |
| SV Network Status | https://canton.foundation/sv-network-status/ |
| Brand Guidelines | https://www.canton.network/brand-kit-trademark-use |
| Discord | https://discord.gg/canton |
| Telegram | https://t.me/CantonNetwork1 |
| HIFI (yeni FA) | https://hifi.com |
| Lattice (müşteri adayı) | https://lattice.cash |
| SyncVotes (müşteri adayı) | https://syncvotes.com |
| Timelock Labs (rakip) | https://timelock.tech |
