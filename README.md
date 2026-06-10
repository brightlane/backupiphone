# BackupiPhone — Global Affiliate Site

**Live URL:** https://brightlane.github.io/backupiphone/  
**Affiliate URL:** https://www.linkconnector.com/ta.php?lc=007949070195004532&atid=iPhoneBackup  
**Build script:** `build.py`

---

## Quick Start

```bash
git clone https://github.com/brightlane/backupiphone.git
cd backupiphone
python3 build.py
```

Requires Python 3.8+. No external dependencies.

---

## Deploy

Push `build.py` to `main`. Workflow builds and deploys automatically.

**Settings → Pages → Source → GitHub Actions**

---

## Project Structure

```
backupiphone/
├── build.py
├── README.md
├── .github/
│   └── workflows/
│       └── deploy.yml
└── dist/                       ← generated on build, never edit manually
    ├── index.html
    ├── assets/style.css
    ├── sitemap.xml
    ├── robots.txt
    ├── llms.txt
    ├── .nojekyll
    ├── 404.html
    ├── {slug}/index.html
    └── {lang}/{slug}/index.html
```

---

## Build Stats

| Metric | Value |
|---|---|
| Total pages | 1,958 |
| Languages | 24 |
| Keyword slugs | 88 |
| Affiliate links per page | 65 |
| Backup data types | 18 |
| Use-case scenarios | 12 |
| Testimonials | 9 |
| FAQ entries | 10 |
| Dependencies | 0 |

---

## Languages (24)

🇬🇧 English · 🇪🇸 Español · 🇫🇷 Français · 🇩🇪 Deutsch · 🇧🇷 Português · 🇯🇵 日本語 · 🇰🇷 한국어 · 🇨🇳 中文 · 🇸🇦 العربية · 🇮🇹 Italiano · 🇷🇺 Русский · 🇳🇱 Nederlands · 🇵🇱 Polski · 🇹🇷 Türkçe · 🇮🇩 Indonesia · 🇸🇪 Svenska · 🇻🇳 Tiếng Việt · 🇮🇳 हिन्दी · 🇲🇾 Melayu · 🇺🇦 Українська · 🇷🇴 Română · 🇨🇿 Čeština

---

## Keyword Slugs (88)

**Core** — `review` `download` `free` `software` `tool` `guide` `best` `comparison` `tutorial` `how-to`

**Backup actions** — `backup-iphone` `backup-iphone-to-pc` `backup-iphone-to-mac` `backup-without-icloud` `backup-without-itunes` `backup-to-computer` `backup-whatsapp` `backup-iphone-photos` `backup-iphone-messages` `backup-contacts` `backup-iphone-data` `backup-app-data`

**Restore & transfer** — `restore-iphone-backup` `restore-from-backup` `transfer-to-new-iphone` `transfer-iphone-data` `switch-iphone` `move-data-iphone`

**Scenarios** — `iphone-full-storage` `icloud-full` `before-ios-update` `before-factory-reset` `water-damage` `broken-iphone` `stolen-iphone` `upgrade-iphone` `android-to-iphone` `new-iphone-setup`

**Data types** — `whatsapp-backup` `whatsapp-transfer` `photos-backup` `messages-backup` `contacts-backup` `notes-backup` `call-history-backup`

**iTunes alternatives** — `itunes-alternative` `replace-itunes` `better-than-itunes` `itunes-backup-extractor` `read-itunes-backup` `access-itunes-backup`

**iCloud alternatives** — `icloud-alternative` `replace-icloud` `no-icloud` `free-icloud-alternative`

**How-to** — `how-to-backup-iphone-to-pc` `how-to-backup-iphone-to-mac` `how-to-backup-whatsapp-iphone` `how-to-transfer-iphone` `how-to-restore-iphone` `selective-restore`

**Devices** — `iphone-15-backup` `iphone-14-backup` `iphone-13-backup` `ipad-backup` `ios-17-backup` `iphone-se-backup`

**Platform** — `windows` `mac` `windows-10` `windows-11` `macos`

**Comparisons** — `vs-imazing` `vs-dr-fone` `vs-icarefone` `vs-tenorshare` `alternatives` `free-vs-paid` `best-free-backup`

**Security** — `encrypted-backup` `private-backup` `secure-backup` `local-backup`

**Long-tail** — `backup-iphone-locally` `offline-iphone-backup` `wireless-iphone-backup` `automatic-iphone-backup` `scheduled-iphone-backup`

---

## Page Sections (every page)

1. **Safety bar** — Blue gradient warning bar with direct CTA
2. **Nav** — Dark space theme, 5 nav links + green CTA button
3. **Hero** — Dual gradient, h1, badge row, 6 proof items
4. **Stats band** — 8 key stats (18+ data types, ∞ storage, $0 monthly fees, etc.)
5. **Backup data types** — 18 glowing green clickable cards (all affiliate)
6. **How it works** — 3-step guide with detailed copy
7. **Why this beats iCloud & iTunes** — 6 value prop cards
8. **Use-case scenarios** — 12 amber scenario cards (all affiliate)
9. **Testimonials** — 9 detailed real-world backup stories
10. **Pricing** — Free Trial / $39.99 Annual / $69.99 Lifetime
11. **FAQ** — 10 deep answers covering iCloud vs iTunes vs this tool
12. **Final CTA** — Green accent gradient banner
13. **Footer** — 5-column with backup types, scenarios, comparisons, how-to, languages

---

## Design

Deep space navy (`#060b18`) with electric blue (`#2563eb`) accents and safe green (`#22c55e`) CTAs. Feels secure, trusted, and essential — appropriate for a data protection product.

---

## Customising `build.py`

| Section | What to change |
|---|---|
| `AFFILIATE_URL` | Your LinkConnector URL |
| `BASE_URL` | Change if moving to a custom domain |
| `LANGUAGES` | Add/remove/edit languages |
| `BACKUP_TYPES` | Add/remove backup data type cards |
| `SCENARIOS` | Add/remove use-case scenario cards |
| `TESTIMONIALS` | Edit user stories |
| `FAQS_EN` | Edit FAQ questions and answers |
| `PAGE_SLUGS` | Add/remove keyword pages |
| `CSS` | Edit styles and colours |
| `build_page()` | Edit HTML layout |

After any change: `python3 build.py`

---

## Post-Deploy Checklist

- [ ] Repo Settings → Pages → Source → **GitHub Actions**
- [ ] Submit `sitemap.xml` to [Google Search Console](https://search.google.com/search-console)
- [ ] Submit `sitemap.xml` to [Bing Webmaster Tools](https://www.bing.com/webmasters)
- [ ] Add `/assets/og-image.png` (1200×630px)
- [ ] Add Google Analytics 4 tag in `build_page()` `<head>`
- [ ] Verify affiliate tracking in your LinkConnector dashboard

---

## Affiliate Disclosure

Commissions earned via LinkConnector. All links use `rel="noopener sponsored"`. FTC-compliant disclosure on every page. Apple, iPhone, iPad, iCloud, iTunes, and iOS are trademarks of Apple Inc.
