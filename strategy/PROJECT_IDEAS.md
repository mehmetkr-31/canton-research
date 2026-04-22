# Canton Network Proje Fikirleri ve Degerlendirme
# 226 FA Basvurusu + Gercek Pazar Verileri ile Desteklenmis
# Son Guncelleme: Nisan 2026

---

## OZET KARAR

**Oncelikli Fikir: RepoAMM (Open-Access Treasury Repo Marketplace)**

Neden:
- 226 FA basvurusunda dogrudan rakip yok (kanıtlandi)
- Broadridge DLR + Tradeweb buy-side'i serve etmiyor
- $346M/yil unremunerated collateral (Canton'un kendi verisi)
- HackCanton Track 2 icin ideal

---

## FİKİR #1: RepoAMM — ONCELIKLI SECIM

### Ne Yapar?
US Treasury ve diger HQLA'lar ile stablecoin (USDC/USYC) arasinda
AMM tabanli intraday repo piyasasi. Herkes LP olabilir,
herkes borrow edebilir. Broadridge DLR'nin demokratize versiyonu.

### Problem (Kanıtlı)
**Kaynak:** Broadridge DLR whitepaper
> "Buy-side firms are cost-conscious. They won't spend money to be leaders,
> but once they see broad activity, they will jump in."

**Kaynak:** Canton Blog (Kelly Mathieson, Ocak 2026)
> "58% of market participants struggling with collateral management"
> "$25B per firm unremunerated overnight"

**Kaynak:** FA Basvurusu #57 - Tradeweb
> "First trade done on 26-Jul-2025 with DRW & Virtu"
> Sadece buyuk kurumsal - kucuk firmalar erisemiyor

**Rakip Yok:** 226 FA basvurusunda buy-side open-access repo YOKTUR.

### Kullanici Hikayeleri (Use Cases)

**Hikaye 1: Verition Fund Management (hedge fund)**
```
Sabah 9:15 - Saat 11:30 arasi $20M cash acigi var
Eski durum: Goldman Sachs'i ara, minimum $50M, bilateral
Yeni durum: RepoAMM'e gir, $20M USDC al, $20M Treasury ver
2.25 saat sonra geri ode, sadece 2.25 saat faiz ode
Tasarruf: Gunluk overdraft fee ortadan kalkar
```

**Hikaye 2: Pension Fund LP**
```
$500M US Treasury portfoyu var
Cuma aksam: Treasury bos duruyor, yield yok
RepoAMM'e LP olarak gir: Treasury havuza kor
Hafta sonu hedge fund'lara otomatik repo
Pazartesi: $500M geri + hafta sonu faizi
Ekstra kazanc: $346M/yil potansiyeli (Tier 1 firma icin)
```

**Hikaye 3: Asset Manager Overnight Optimization**
```
Gunde 3 kere treasury pozisyonu degisiyor
Her seferinde bilateral repo negotiate etmek yerine:
RepoAMM'de anlık fiyat, anlık execute
Settlement: Atomik (T+0, saniyeler)
```

### Teknik Mimari

**Daml Contracts:**
```
RepoPool:
  - treasuryAssets: [TokenizedTreasury]
  - stablecoinAssets: [USDC]
  - k: Decimal  -- constant product k = x * y
  - fee: Decimal -- 10 bps (0.1%)

BorrowRequest:
  - borrower: Party
  - collateral: TokenizedTreasury
  - amount: Decimal
  - duration: RelTime
  - rate: Decimal  -- AMM tarafindan hesaplanir

RepaymentObligation:
  - borrower: Party
  - principal: Decimal
  - interest: Decimal
  - dueAt: Time
  - collateralHeld: TokenizedTreasury
```

**AMM Formulu:**
```
x * y = k  (constant product)
x = Treasury pool
y = USDC pool

Repo rate = f(x, y, duration)
Rate = base_rate + utilization_premium
```

**Canton Entegrasyonlari:**
- Circle USDC/USYC (mevcut Featured App)
- DTCC tokenized US Treasuries (2026 H1 geliyor)
- Broadridge DLR ile komplementer (cakismiyor)
- Chainlink oracle (Treasury fiyat feed)

### Rakip Analizi (FA Verisinden)

| Uygulama | Ne Yapiyor | RepoAMM ile Cakisiyor mu? |
|----------|-----------|--------------------------|
| Broadridge DLR | Institutional repo | HAYIR - farkli segment |
| Tradeweb | Electronic repo marketplace | HAYIR - institutional only |
| Cantex | Spot DEX | HAYIR - token swap, repo degil |
| Canton Exchange | AMM DEX | HAYIR - token swap, repo degil |
| ACME | Overcollateralized lending | HAYIR - lending, repo degil |
| Rhein Finance | Collateralized lending | HAYIR - lending, repo degil |

**Sonuc: DOGRUDAN RAKIP YOK**

### Is Modeli

```
Gelir Kaynaklari:
1. Trading fee: 10 bps her repo'dan
   - $100M gunluk volume x 10 bps = $100K/gun
   - Yillik: $36.5M (optimistik)

2. Protocol yield: LP fee'lerin %20'si
   - LP'lara %80, protokol %20

3. Canton Coin rewards (Featured App)
   - Her transaction = Activity Marker
   - Aylik CC reward pool'dan pay

Gercekci Year 1:
   - $10M gunluk volume x 10 bps x 250 gun = $2.5M
```

### HackCanton MVP Plani

**Hafta 1-2: Core Contracts**
- [ ] RepoPool Daml contract
- [ ] BorrowRequest + RepaymentObligation contracts
- [ ] AMM fiyatlama logic (x*y=k)
- [ ] USDC mock integration (testnet)

**Hafta 3: UI + Demo**
- [ ] Pool dashboard (TVL, rates, utilization)
- [ ] Borrow interface (amount, duration, collateral)
- [ ] LP interface (deposit, withdraw, earnings)
- [ ] Demo scenario: $1M Treasury → $1M USDC borrow

**Hafta 4: Polish + Pitch**
- [ ] Demo video
- [ ] 1-page business brief
- [ ] Pilot plan (Rhein Finance / Haven Digital ile entegrasyon)

### HackCanton Pitch Ozeti

**Problem:**
$25B per firm unremunerated overnight (Canton/ValueExchange).
Broadridge DLR ve Tradeweb sadece buyuk kurumlara hizmet ediyor.
Buy-side firmalar (hedge fund, asset manager) repo'ya erisemiyor.

**Cozum:**
RepoAMM: Canton uzerinde herkesin erisebilecegi, AMM-tabanli,
24/7 calisan tokenized Treasury repo piyasasi.

**Pazar:**
- $6.9T/ay mevcut repo volume (Broadridge DLR)
- $346M/yil unremunerated collateral (Tier 1 firma basina)
- 58% market participant struggling = potansiyel kullanici

**Canton Farki:**
Sub-transaction privacy + atomic settlement = buy-side artik katilabilir
(Public chain'de pozisyon gorunurlugu sorun oldugundan katilmiyorlardi)

**Track:** Track 2 - Financial Applications

---

## FİKİR #2: Weekend Yield Automator — IKINCI SECIM

### Ne Yapar?
Cuma aksam US Treasury pozisyonunu otomatik olarak repo'ya sokup
Pazartesi sabah geri ceken smart contract. "Set and forget" yield.

### Problem (Kanıtlı)
**Kaynak:** Canton Blog (Barnaby Nelson, Subat 2026):
> "6:45 pm on a Friday, the financial world effectively goes into hibernation"
> "$346M per annum increase in interest earnings for Tier 1 firms"
> "120 extra hours per week = 170% increase"

### Kullanici Hikayesi
```
Cuma 18:44: $100M Treasury pozisyonu var
Smart contract trigger: Otomatik repo baslatilir
Cuma 18:45 - Pazartesi 08:00: Repo aktif, yield birikir
Pazartesi 08:00: Repo unwind, principal + yield geri gelir
Kullanici: Hic dokunmadan $346M/yil potansiyeli
```

### Neden RepoAMM'den Sonra Gelebilir
- RepoAMM olursa Weekend Automator bu platform uzerinde calisir
- RepoAMM = infrastructure, Weekend Automator = ust katman uygulama
- Track 1 (RWA & Business Workflows) icin de uygun

---

## FİKİR #3: Intraday Liquidity Forecaster — UCUNCU SECIM

### Ne Yapar?
Settlement pipeline'ini analiz ederek gelecek saatlerdeki nakit
acik/fazlasini tahmin eden ve otomatik intraday repo baslatip
daylight overdraft fee'lerini minimize eden araç.

### Problem (Kanıtlı)
**Kaynak:** Broadridge Whitepaper:
> "Some firms spend $1M+ per year on daylight overdraft alone"
> "Until now, the main thing slowing settlement has been people"

**Kanit:** SocGen Case Study:
> "Before DLR: ~$1M/yil daylight overdraft"
> "After DLR: 4/5 days zero fee = 80% reduction"

### Neden Daha Az Oncelikli
- Cok teknik (ML + settlement pipeline analysis)
- Broadridge DLR zaten kısmen coziyor
- Buy-side icin daha az ilgili (sell-side sorunlu daha fazla)
- Track 4 (Analytics) icin uygun ama Track 2 odak

---

## HACKCANTON TRACK KARARI

**Secim: Track 2 — Financial Applications**

Gerekceler:
1. RepoAMM tam olarak Track 2 kriterlerine uygundur
2. "Real economic activity" = repo volume
3. "Liquidity flows" = LP → pool → borrower
4. "Composability" = USDC + Treasury + Canton privacy

**Ikincil Track: Track 1 — RWA & Business Workflows**
- "End-to-end workflow" = Treasury tokenization → Repo → Settlement
- "Roles" = LP (issuer), Borrower (holder), Protocol (observer)
- "Business brief" = hedge fund treasury management use case

---

## SONUC

RepoAMM icin 226 FA basvurusu tarandı:
- Dogrudan rakip: 0
- Dolaysiyla ilgili: Tradeweb (institutional), Broadridge (institutional)
- Tamamlayici: Rhein Finance (lending), Haven Digital (lending)
- Kullanilabilir Altyapi: Circle USDC, DTCC Treasuries, Chainlink

**Tavsiye: HackCanton'a RepoAMM ile katil.**
Gercek problem, kanıtlanmis pazar, sifir dogrudan rakip.
