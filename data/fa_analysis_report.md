# GSF Tokenomics Mailing List — Tam Analiz Raporu
**Kaynak:** lists.sync.global/g/tokenomics  
**Çekilen veri:** 726 topic, 233 FA thread  
**Tarih:** Nisan 2026

---

## 1. Veri Özeti

| Metrik | Değer |
|--------|-------|
| Toplam topic | 726 |
| FA başvuru thread'i | 233 |
| Mesaj içeren thread | 233 (tamamı) |
| Onay kelimesi geçen mesaj | 105 |
| Soru/inceleme mesajı | 130 |
| Concern/withdrawn | 56 |
| Async vote geçen thread | 18 |
| Video/demo sunulan | 138 |

---

## 2. Başvuru Kategorileri

| Kategori | Başvuru Sayısı |
|----------|---------------|
| Validator / Infrastructure | 56 |
| Wallet / Custody / Treasury | 49 |
| Exchange / Trading (DEX, OTC) | 49 |
| AI / Agent | 29 |
| Data / Oracle / Analytics | 23 |
| Tokenization / RWA | 13 |
| Payment / Settlement | 7 |
| DeFi / Finance | 4 |
| Gaming / Betting | 1 |
| Diğer | 2 |

**Canton Vault için çıkarım:** Wallet/Custody/Treasury kategorisi 49 başvuruyla en kalabalık ikinci kategori. Rekabet yüksek ama alan committee tarafından iyi biliniyor — "multisig treasury" kavramı tanıdık.

---

## 3. Committee Üyeleri ve Rolleri

Tüm FA thread'lerinden elde edilen aktif isimler:

| İsim | Kurum | Rol | Aktivite |
|------|-------|-----|---------|
| **Amanda Martin** | Linux Foundation | Program Director — koordinatör, tüm thread'leri yönetiyor | En aktif |
| **Eric Saraniecki** | Digital Asset | Tokenomics teknik sorumlusu — BME, Activity Marker sorularını yanıtlıyor | Çok aktif |
| **Kinga Bosse** | MPCH | COO — oy kullanıyor, hızlı approve veriyor | Aktif |
| **Chris Kelly** | IntellectEU | Teknik sorular soruyor | Aktif |
| **Prakash Neelakantan** | Broadridge | Oy kullanıyor | Orta |
| **Chris Zuehlke** | Cumberland DRW | Oy kullanıyor | Orta |
| **Chris Matturri** | Proof Group | Oy kullanıyor | Az |
| **Veronica Augustsson** | 7RIDGE/C7 | Oy kullanıyor | Az |
| **Juan Costa** | (Super Validator?) | Tokenomics mekanizması sorgular | Az |

### Kritik Bilgi
- **Amanda Martin** tüm süreci yönetiyor. İlk temas noktası o.
  E-posta: `amartin@linuxfoundation.org`
- **Eric Saraniecki** teknik itirazları çözüyor. Activity Marker planın ona mantıklı gelmesi lazım.
- Onay için **birden fazla üyenin "X approves"** yazması gerekiyor. Kaç üye şart belli değil ama 4 yeterli görünüyor.

---

## 4. Onay Süreci — Keşfedilen Pattern'lar

### Pattern A: Hızlı Onay (1-3 gün)
**Örnek:** Orphil LLC (Agentic Ledger) — 22 Ekim 2025, 1 günde onaylandı.

```
Başvuru gönderildi (Amanda ilettiği via thread)
→ Şirket bir güncelleme yaptı (Activity Marker sorusunu netleştirdi)
→ Amanda async vote açtı: "Any questions or concerns?"
→ MPCH: "MPCH approves"
→ IntellectEU: "IEU approves"
→ Cumberland DRW: "Cumberland DRW approves"
→ Proof Group: "Proof Group approves"
→ 7RIDGE: "7RIDGE/C7 approves"
→ Amanda: "We have enough votes. I will make the announcement."
```

**Ne sağladı?** Başvuruda Activity Marker kullanımı net yazılmıştı. "No markers for reads" diyerek committee'nin potansiyel itirazını baştan kesti.

---

### Pattern B: Orta Uzunluk (1-4 hafta)
**Örnek:** HandlPay by Verso Network AG — Ekim–Aralık 2025

```
Başvuru gönderildi
→ Juan soru sordu: "Privacy nasıl çalışıyor? Farming riski yok mu?"
→ Eric yanıtladı: "CC public ama stablecoin private. Farming endişesini paylaşmıyorum."
→ Juan tekrar yazdı: "Ama 10dk'da bir CC drip = kurumsal müşteriyle aynı ödül, bu adil mi?"
→ Eric yanıtladı: "BME'de elastic/inelastic ayrımı var, her ikisi de değerli."
→ Amanda: "Async vote yapabilir miyiz? Şirketten video ister misiniz?"
→ Şirket video linki gönderdi (Google Drive)
→ Amanda güncelleme iletti: kullanıcı büyüme rakamları + Activity Marker planı
→ Thread açık kaldı (devam eden onay süreci)
```

**Ne yavaşlattı?** Farming/gaming riski sorusu — bu konu committee için hassas.

---

### Pattern C: Uzun / Takılı (1+ ay)
- Genellikle Activity Marker planı belirsiz olan başvurular
- "What exactly triggers the marker?" sorusuna net cevap verilemeyen başvurular
- Proof of concept / testnet aktivitesi gösterilemeyen başvurular

---

### Pattern D: Withdrawn
- Başvurucu geri çekiyor (genellikle committee soruları yanıtsız kalınca)
- Örnek: `[WITHDRAWN] Featured App Request: BitDynamics AB - Cantonmarkets`

---

## 5. Committee'nin Sorduğu Sorular

Tüm thread'lerden çıkarılan sık sorular:

### Teknik Sorular (Eric Saraniecki soruyor)
1. **"What exactly triggers the Activity Marker?"** — En sık sorulan soru. Her başvuruda bekleniyor.
2. **"Is this elastic or inelastic activity?"** — BME mekanizması perspektifinden sorguluyor.
3. **"How does this avoid farming/gaming the rewards?"** — Drip incentive / sybil riski var mı?
4. **"Does this use CC or Activity Markers for rewards?"** — İkisi farklı, net olmalı.
5. **"What is the party ID structure?"** — `company-mainnet-1::1220...` formatında olmalı.

### Proje Sorguları (Genel committee)
6. **"How many active users / what is the traction?"** — Testnet aktivitesi + kullanıcı sayısı isteniyor.
7. **"Is the code open source?"** — GitHub linki varsa güçlendiriyor.
8. **"How will this contribute to the Canton ecosystem long-term?"** — Geçici değil kalıcı değer göster.
9. **"Can you provide a video demo?"** — Google Drive linki formatında.

### Wallet/Custody özelinde (Chris Kelly soruyor)
10. **"Would this same logic apply to all featured apps hitting the credential limit?"** — Precedent yaratıyor musun?

---

## 6. Onay Gereksinimleri (Keşfedilen)

Başarılı başvurularda ortak olan unsurlar:

1. **Net Party ID** — `company-mainnet-1::1220[hash]` formatında, mainnet'te aktif
2. **Somut Activity Marker planı** — "X event olduğunda marker tetiklenir" şeklinde net tanım
3. **Testnet/mainnet aktivite kanıtı** — Başvuru sırasında zaten çalışıyor olmalı
4. **Kullanıcı büyüme rakamları** — MAU, transaction count, growth %
5. **Farming karşıtı mekanizma** — Committee'ye "gaming yok" güvencesi
6. **Video demo** (tercihen Google Drive) — Async vote için kritik
7. **Hızlı yanıt süresi** — Amanda'nın soruları 24-48 saat içinde yanıtlanmalı

---

## 7. Başvuru Formu Alanları (Gerçek Format)

Mevcut başvurulardan çıkarılan form yapısı:

```
New Featured App Submission Details

Name of Applying Institution: [Şirket adı]
Name of the application: [Uygulama adı]
URL of the applying institution: [Web sitesi]
Emails for Responsible Persons: [email1, email2]
Party ID for the Featured Application: [company-mainnet-1::1220...]
URL for the public code repository (if available): [GitHub]
Provide a summary of what your application will do: [200-400 kelime]
Describe the expected users of your application: [hedef kitle]
How will your application interact with the Canton Network and leverage
Canton Coin and Activity Markets for application rewards? [kritik alan]
Describe how your application will interact with the ledger: [teknik detay]
Does this activity use Canton Coin or Activity Markers to generate rewards?: [YES/NO + açıklama]
```

---

## 8. Canton Vault İçin Strateji

### 8.1 Başvuru Öncesi Hazırlık

**Önce şunları tamamla:**
- [ ] Mainnet Party ID oluştur: `cantonvault-mainnet-1::1220[hash]`
- [ ] En az 2 hafta mainnet aktivite yap (transaction geçmişi oluş)
- [ ] Activity Marker tetikleyici olayları tam tanımla (vault oluşturma, imza, transfer)
- [ ] 3-5 dakikalık Google Drive demo videosu hazırla
- [ ] Kullanıcı sayısı / transaction count not et

**Amanda'ya yazmadan önce:**
- `tokenomics+subscribe@lists.sync.global` ile listeye üye ol
- Thread arşivini takip et, committee'nin güncel hassasiyetlerini anla
- Bir Office Hours slotu ayırt (tokenomics meeting saatini bul)

---

### 8.2 Başvuru Formu için Önerilen Metin

```
Name of Applying Institution: Canton Vault [şirket tüzel adı]
Name of the application: Canton Vault
URL: [cantonvault.xyz veya ne ise]
Emails: mehmet@... ali@...
Party ID: cantonvault-mainnet-1::1220[gerçek hash]

Summary:
Canton Vault is a multi-signature treasury and governance platform on Canton Network.
Built as "Safe for Canton," it enables institutions and individuals to manage shared
on-chain assets with configurable M-of-N signature policies. Key features:
- Multi-party vault creation with DAML smart contract enforcement
- Policy Engine for programmable spending rules and approval workflows
- Canton Coin treasury management with full audit trail
- Enterprise governance layer for institutional deployment

Expected Users:
- DAOs and investment collectives managing shared Canton Coin treasuries
- Enterprises requiring multi-party approval for on-chain transactions
- Validator operators needing governance tooling for treasury management
- Individual users wanting secure multi-sig CC storage

Canton Network Interaction & Activity Markers:
Canton Vault generates verifiable on-chain activity through three event types:
1. VaultCreation — triggers Activity Marker when a new multisig vault is deployed
2. SignatureSubmission — each co-signer submitting approval creates a ledger event
3. VaultExecution — when threshold is met and transaction executes, final marker fires

All markers are generated by genuine economic activity (vault operations), not
artificial inflation. The platform charges a CC-denominated service fee on vault
execution, creating inelastic demand for Canton Coin.

Anti-gaming mechanism: Markers only fire on executed vault operations, not on
drafts or failed proposals. Volume is naturally bounded by institutional workflows.

Ledger Interaction:
Backend uses Canton Validator REST API (Splice SDK). DAML contracts enforce
M-of-N logic on-chain. All vault state changes are permanent ledger entries.

CC/Activity Markers: YES.
- Vault creation fee: paid in CC
- Execution fee: paid in CC (burned via BME)
- Activity Markers: tied to VaultCreation + VaultExecution events
```

---

### 8.3 Eric Saraniecki'nin Sorularına Hazır Cevaplar

**S: "What exactly triggers the Activity Marker?"**
> "Two events trigger markers: (1) VaultCreation — when an institution deploys a new multisig vault. (2) VaultExecution — when the M-of-N threshold is met and the transaction executes on-chain. SignatureSubmissions are recorded on-ledger but do not generate reward-eligible markers, to prevent artificial inflation."

**S: "Is this elastic or inelastic activity?"**
> "Primarily inelastic. Vault creation and execution are tied to real business workflows — enterprise treasury operations don't scale with reward rates. A hedge fund doesn't create 10x vaults because rewards are higher."

**S: "How does this avoid farming/gaming?"**
> "Markers only fire on vault execution, which requires M-of-N human signers and a real CC outflow. You cannot farm this without spending CC. The minimum vault operation costs [X] CC in fees."

**S: "What is your testnet/mainnet traction?"**
> "We have [N] vaults created on testnet, [X] total executions, [Y] unique parties involved. Mainnet Party ID is live as of [tarih]."

---

### 8.4 Timeline

| Hafta | Eylem |
|-------|-------|
| Şimdi | Party ID oluştur, mainnet'e al |
| +1 hafta | 2 haftalık aktivite periodu başlat |
| +2 hafta | Demo video çek (Google Drive) |
| +3 hafta | Başvuruyu listexe gönder |
| +3 gün | Amanda'nın sorusunu bekle, 24 saat içinde yanıtla |
| +1 hafta | Async vote başlar, committee üyelerinin onayı beklenir |
| +2 hafta | Onay veya ek soru dönemi |

---

### 8.5 Riskler ve Önlemler

| Risk | Önlem |
|------|-------|
| "Farming riski var" itirazı | Inelastic aktivite, CC fee requirement, M-of-N insan imzası ile savun |
| Activity Marker belirsiz | Tam teknik tanımı başvuruda yaz, Eric'in sorusunu öncele |
| Wallet/Treasury kalabalık kategori | Unique value prop vurgula: multi-sig governance + institutional focus |
| Testnet aktivitesi yok | Başvurmadan önce en az 2 hafta mainnet aktivite yap |
| Amanda dönmezse | 1 hafta sonra nazikçe follow-up e-posta at |
| Async vote yeterli oy almaz | Office Hours'a katıl, committee'yi tanı |

---

## 9. Önemli Kaynaklar

- **Coordinator:** Amanda Martin — `amartin@linuxfoundation.org`
- **Teknik soru:** Eric Saraniecki — `eric@digitalasset.com`
- **Liste:** `tokenomics@lists.sync.global`
- **Abone ol:** `tokenomics+subscribe@lists.sync.global`
- **Governance thread:** "Featured Applications Governance" — approved FA form güncellemelerini takip et
- **Örnek iyi başvuru:** Orphil LLC (Agentic Ledger) thread'i — hızlı onay template'i

---

*Rapor oluşturulma tarihi: Nisan 2026*  
*Veri kaynağı: 233 FA thread, 726 mailing list topic*
