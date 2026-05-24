#!/usr/bin/env python3
"""
kit.com Daily Blog Generator — cycles 10 posts daily
"""

import os, json, base64, requests
from datetime import datetime, timezone

AFF        = "https://partners.kit.com/x3mb24l6x6vz-deal"
SITE_URL   = "https://brightlane.github.io/kit.com"
GH_USER    = os.environ.get("GH_USER", "brightlane")
GH_REPO    = os.environ.get("GH_REPO", "kit.com")
GH_TOKEN   = os.environ.get("GITHUB_TOKEN", "")
BLOG_INDEX = "blog-index.json"
BRAND      = "KitAuthorityHub"

HEADERS = {"Authorization": f"token {GH_TOKEN}", "Accept": "application/vnd.github+json"}

CSS = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{font-family:Arial,sans-serif;background:#f4f4f4;color:#222;line-height:1.7;}
a{color:#ff5a5f;text-decoration:none;}a:hover{text-decoration:underline;}
nav{background:#222;padding:0 1.5rem;display:flex;align-items:center;justify-content:space-between;height:56px;}
.nav-logo{color:#fff;font-weight:700;font-size:1.05rem;text-decoration:none;}
.nav-logo span{color:#ff5a5f;}
.nav-cta{background:#ff5a5f;color:#fff!important;padding:6px 14px;border-radius:6px;font-weight:700;font-size:0.85rem;text-decoration:none;}
.container{max-width:820px;margin:0 auto;padding:2rem 1.5rem;background:#fff;min-height:60vh;}
.meta{color:#888;font-size:0.85rem;margin-bottom:1.5rem;}
h1{font-size:clamp(1.6rem,4vw,2.3rem);font-weight:700;color:#111;margin-bottom:0.75rem;line-height:1.2;}
h2{font-size:1.2rem;font-weight:700;color:#111;margin:2rem 0 0.75rem;border-bottom:2px solid #eee;padding-bottom:5px;}
p{margin-bottom:1rem;color:#333;font-size:0.97rem;}
.btn{display:inline-block;padding:12px 26px;background:#ff5a5f;color:#fff;border-radius:6px;font-weight:700;font-size:0.95rem;margin:1rem 0;text-decoration:none;}
.btn:hover{background:#e0393e;text-decoration:none;}
.tip-box{background:#fff5f5;border-left:4px solid #ff5a5f;padding:1rem 1.2rem;border-radius:0 8px 8px 0;margin:1.5rem 0;}
.sticky{position:fixed;bottom:0;width:100%;background:#111;text-align:center;padding:9px;z-index:999;}
.sticky a{color:#fff;font-weight:700;font-size:0.85rem;text-decoration:none;}
footer{background:#111;color:rgba(255,255,255,0.5);text-align:center;padding:1.5rem;font-size:0.8rem;margin-top:3rem;}
footer a{color:#ff5a5f;text-decoration:none;}
"""

POSTS = [
  {
    "title": "How to Get Your First 100 Kit.com Clicks — Beginner Guide",
    "keywords": "kit.com first clicks beginners, how to start kit.com, kit.com beginner strategy",
    "body": f"""<p>Getting your first 100 clicks on Kit.com feels impossible when you're starting out. Here is exactly how to do it in your first week.</p>
<h2>Step 1: Build a Tight, Focused Kit</h2>
<p>Don't list 50 products. Start with 5-8 products you genuinely use daily. A focused kit with strong personal descriptions converts 3x better than a generic mega-list. Your first kit should answer one specific question: "what does [your name] actually use?"</p>
<h2>Step 2: Add Your Kit Link to Everything You've Already Published</h2>
<p>Go back to your top 10 videos, posts, or episodes and add your Kit.com link. This is the fastest way to get initial clicks — you're not creating new traffic, you're monetizing existing traffic that's already looking for your recommendations.</p>
<h2>Step 3: Post One Piece of Content Specifically About Your Kit</h2>
<p>Create one video, post, or email with the headline "My complete [niche] setup — everything linked." This single piece of content should drive a significant portion of your early Kit.com traffic.</p>
<h2>Step 4: Put the Link in Your Bio Everywhere</h2>
<p>Instagram, TikTok, Twitter, YouTube channel page, podcast show notes — everywhere you have a bio or link field, your Kit.com link should be there. Bios convert consistently over time without ongoing effort.</p>
<div class="tip-box"><strong>Pro tip:</strong> Don't wait until your kit is "perfect." Launch with 5 products and add more weekly. A live imperfect kit earns more than a perfect one in your drafts.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">Build Your Kit.com Storefront →</a></p>"""},
  {
    "title": "Kit.com vs Amazon Associates — Which Pays More in 2026?",
    "keywords": "kit.com vs amazon associates 2026, creator affiliate programs compared, best affiliate program creators",
    "body": f"""<p>Most creators default to Amazon Associates because it's familiar. But Kit.com often pays significantly more for the same recommendation. Here is the honest comparison.</p>
<h2>Amazon Associates Commission Rates</h2>
<p>Amazon Associates pays 1-4% on most product categories. Electronics — the most common creator category — pays just 1%. A creator recommending a $200 camera earns $2 per sale through Amazon. A creator with 1,000 conversions/month earns $2,000.</p>
<h2>Kit.com Commission Structure</h2>
<p>Kit.com connects you directly with brands who set their own commission rates. Most creator-focused brands pay 5-20% commissions. The same $200 camera through a brand partnership paying 10% earns $20 per sale — 10x more than Amazon.</p>
<h2>The Caveat</h2>
<p>Amazon has everything. Kit.com has a curated selection. If your audience wants to buy something not available on Kit.com, you still need Amazon Associates as a fallback. The winning strategy is to use both — Kit.com for high-commission brand partnerships, Amazon for the long tail.</p>
<h2>Cookie Duration</h2>
<p>Amazon's cookie lasts 24 hours — if your audience doesn't buy within 24 hours of clicking your link, you earn nothing. Kit.com's cookie duration is set by the brand and is typically 7-30 days.</p>
<div class="tip-box"><strong>Bottom line:</strong> For products available on both, Kit.com almost always pays more. The 24-hour Amazon cookie alone costs creators significant income.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">Switch to Kit.com — Higher Commissions →</a></p>"""},
  {
    "title": "The 5 Best Niches for Kit.com Monetization in 2026",
    "keywords": "best niches kit.com 2026, kit.com niche ideas, creator monetization niche",
    "body": f"""<p>Not all niches perform equally on Kit.com. Here are the five niches that consistently generate the highest earnings per click.</p>
<h2>1. Home Office & Remote Work</h2>
<p>The permanent shift to remote work created massive demand for home office gear. Monitors, webcams, microphones, desks, and chairs. Average order values are high and buyers are actively researching before purchasing.</p>
<h2>2. Content Creation & YouTube</h2>
<p>Cameras, lighting, microphones, editing software, and accessories. YouTube's culture of "what gear do you use?" means every creator with a following has a warm audience for their kit. High conversion rates.</p>
<h2>3. Podcasting</h2>
<p>Podcast gear is a smaller niche but the audience is highly engaged and purchase-intent is strong. Microphones, audio interfaces, soundproofing, and recording software all earn well.</p>
<h2>4. Gaming & Streaming</h2>
<p>Gaming peripherals, streaming setups, and gaming chairs. Large audience with young buyers who research extensively before purchasing. Stream-related content drives consistent kit traffic.</p>
<h2>5. Photography & Videography</h2>
<p>High ticket items (cameras, lenses, tripods) mean even a 1-2% conversion rate generates significant income. Photography audiences are passionate and willing to invest in quality gear.</p>
<div class="tip-box"><strong>Key insight:</strong> The best niche is the one you create content in — your authentic expertise converts better than any niche chosen purely for commission rates.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">Start Your Kit.com in Your Niche →</a></p>"""},
  {
    "title": "How to Write Kit.com Product Descriptions That Actually Convert",
    "keywords": "kit.com product descriptions convert, affiliate product writing tips, kit.com optimization",
    "body": f"""<p>Most creators write generic product descriptions. Here is how to write descriptions that dramatically improve conversion rates.</p>
<h2>The Problem with Generic Descriptions</h2>
<p>"Great microphone, sounds amazing" — this describes nothing. It tells your audience nothing they couldn't find on any product page. Generic descriptions perform like generic recommendations: poorly.</p>
<h2>The Formula That Works</h2>
<p>The best kit product descriptions follow a simple formula: <strong>[What it is] + [Specific reason you use it] + [Who it's best for]</strong>.</p>
<p>Example: "The Blue Yeti X — the microphone I've used for every episode of this podcast for 3 years. The USB connection means zero audio interface required. Perfect for anyone recording at a desk who wants professional sound without professional setup complexity."</p>
<h2>Specificity Converts</h2>
<p>Specific details create trust. "I've used this for 3 years" is more convincing than "great quality." "Takes 5 minutes to set up" is more useful than "easy to use." Quantify when you can.</p>
<h2>Address the Objection</h2>
<p>Every product has one common objection. Address it in your description. "Yes, it's more expensive than the entry-level options — but the automatic door bottom alone makes it worth it because you never have to think about it again."</p>
<div class="tip-box"><strong>Test your descriptions:</strong> Read each one out loud. If it sounds like something you'd actually say to a friend asking for a recommendation, it's good. If it sounds like a product listing, rewrite it.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">Build Your Kit.com Storefront →</a></p>"""},
  {
    "title": "Kit.com for Podcasters — Complete Setup Guide 2026",
    "keywords": "kit.com podcasters guide 2026, podcast affiliate monetization, podcast equipment kit",
    "body": f"""<p>Podcasting is one of the most underutilized niches for Kit.com monetization. Here is how to set up and maximize earnings as a podcast creator.</p>
<h2>Why Kit.com Works Especially Well for Podcasters</h2>
<p>Every podcast has listeners who want to know: what microphone do you use, what's your recording setup, what software do you edit with? These questions come from highly engaged listeners with genuine purchase intent. Kit.com turns these questions into revenue.</p>
<h2>Building Your Podcast Kit</h2>
<p>Your podcast kit should cover the complete recording chain: microphone, audio interface (if using XLR), headphones, recording software, editing software, and any accessories like pop filters and boom arms. Include everything you actually use.</p>
<h2>Where to Promote Your Kit</h2>
<p><strong>Show notes:</strong> Every episode gets your Kit.com link in the show notes under "Gear I use." This creates permanent passive traffic as old episodes continue to get discovered.</p>
<p><strong>Mid-roll mentions:</strong> "If you want to know what microphone I use to record this podcast, everything is linked at [kit.com URL]." A single mention drives significant traffic.</p>
<p><strong>YouTube companion content:</strong> Create one "my complete podcast setup" video per year. This video can drive Kit.com traffic for years through search.</p>
<h2>Monetizing Your Audience's Question</h2>
<p>The next time someone asks "what do you record on?" in your DMs or comments, instead of typing out a long response, reply with your Kit.com link. You've turned a common support question into a revenue opportunity.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">Start Your Podcast Kit on Kit.com →</a></p>"""},
  {
    "title": "How Kit.com Works — Complete Beginner Explanation",
    "keywords": "how kit.com works beginners, what is kit.com, kit.com explained simply",
    "body": f"""<p>Kit.com confuses new creators at first. Here is a simple, complete explanation of how the platform works from signup to first commission.</p>
<h2>What Kit.com Is</h2>
<p>Kit.com is a platform that lets you create a curated storefront of products you recommend. Think of it as your personal online store — but you don't handle inventory, shipping, or customer service. You just recommend products and earn commissions when people buy through your links.</p>
<h2>How the Money Flows</h2>
<p>1. You add products to your Kit.com storefront with your unique affiliate links. 2. Your audience visits your storefront and clicks a product. 3. They are redirected to the brand's website with your affiliate tracking active. 4. If they buy, you earn a commission. 5. Commissions are paid out by each brand on their schedule.</p>
<h2>What You Need to Get Started</h2>
<p>Just an account and products you genuinely recommend. No website required. No technical skills required. No inventory. No customer service. The barrier to entry is intentionally low.</p>
<h2>How Kit.com Makes Money</h2>
<p>Kit.com takes a small percentage of the commissions you earn. The brands pay the commissions — you receive your share after Kit.com's fee. This means there's no cost to you unless you're earning.</p>
<div class="tip-box"><strong>Simple summary:</strong> You recommend products you already use → your audience buys through your links → you earn commissions → brands get customers. Everyone wins.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">Join Kit.com — It's Free →</a></p>"""},
  {
    "title": "Kit.com for YouTubers — How to Maximize Description Link Revenue",
    "keywords": "kit.com youtubers strategy, youtube description affiliate kit.com, youtube creator monetization",
    "body": f"""<p>YouTube descriptions are one of the most consistent traffic sources for Kit.com. Here is how to set up and optimize your Kit.com presence across your YouTube channel.</p>
<h2>The YouTube Audience Advantage</h2>
<p>YouTube viewers watching a creator use specific gear are primed to buy that gear. They are in a discovery mindset, they trust the creator, and the gear is visually demonstrating its value in real time. This is the ideal purchase intent environment for Kit.com.</p>
<h2>Setting Up Your YouTube Kit Strategy</h2>
<p><strong>Channel description:</strong> Add your Kit.com link to your YouTube channel's About section. New visitors checking out your channel see your kit immediately.</p>
<p><strong>Every video description:</strong> Add a section called "Gear I use:" or "My setup:" with your Kit.com link. Make it part of your video description template so it appears automatically on every video.</p>
<p><strong>Pinned comment:</strong> Pin a comment on your most popular videos directing viewers to your kit: "Want to know what gear I use? Everything is at [kit.com link]"</p>
<h2>Content Strategy for Kit.com Traffic</h2>
<p>Create one "My complete setup" video per year. These videos consistently rank for searches like "[your name] setup" or "[your niche] setup 2026." A single well-produced setup video can drive Kit.com traffic for 2-3 years.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">Build Your YouTube Kit →</a></p>"""},
  {
    "title": "Kit.com Income Report — What Realistic Earnings Look Like",
    "keywords": "kit.com income realistic, creator affiliate income, how much kit.com earns",
    "body": f"""<p>Most "income reports" are either inflated to impress or understated to avoid jealousy. Here is a realistic breakdown of what Kit.com earnings actually look like at different audience sizes.</p>
<h2>The Variables That Matter Most</h2>
<p>Kit.com income depends on: audience size, audience engagement rate, niche (high-ticket vs low-ticket products), how prominently you promote your kit, and the commission rates of the brands in your kit.</p>
<h2>Realistic Earnings by Audience Size</h2>
<p><strong>1,000-5,000 followers:</strong> $50-$500/month. At this stage, Kit.com income is supplemental rather than significant. Focus on growing your audience while building your kit.</p>
<p><strong>5,000-25,000 followers:</strong> $300-$2,500/month. This is where Kit.com starts to feel meaningful. Creators in this range who actively promote their kit can generate real supplemental income.</p>
<p><strong>25,000-100,000 followers:</strong> $2,000-$10,000/month. High engagement creators in tech and creator niches hit these numbers with consistent promotion.</p>
<p><strong>100,000+ followers:</strong> $10,000+/month is achievable but depends heavily on the factors above. Not all large audiences are equally engaged or purchase-intent focused.</p>
<h2>The Engagement Factor</h2>
<p>A creator with 10,000 highly engaged followers in the home office niche will often out-earn a creator with 100,000 followers in a less purchase-focused niche. Engagement and trust matter more than raw numbers.</p>
<div class="tip-box"><strong>Realistic expectation:</strong> Kit.com is a long game. Months 1-3 are slow. Months 6-12 see consistent growth. Year 2+ is where passive income compounds meaningfully.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">Start Building Your Kit.com Income →</a></p>"""},
  {
    "title": "Kit.com SEO — How to Rank Your Storefront in Google",
    "keywords": "kit.com SEO rank google, creator storefront SEO, affiliate storefront search traffic",
    "body": f"""<p>Most Kit.com users rely entirely on social media traffic. Creators who add SEO to their strategy earn 2-3x more from the same kit. Here is how.</p>
<h2>Can a Kit.com Page Rank in Google?</h2>
<p>Kit.com storefronts can appear in search results, but they face tough competition from established review sites. The better SEO strategy is to use your own website or blog to rank, then drive that traffic to your Kit.com storefront.</p>
<h2>The Blog + Kit.com Combination</h2>
<p>Create blog posts targeting specific search queries. "Best home office setup under $1,000 2026" ranks in Google and drives purchase-intent traffic to your Kit.com storefront. The blog handles SEO; Kit.com handles monetization.</p>
<h2>Target Keywords with "Kit" or "Setup" Intent</h2>
<p>Search queries like "[creator name] setup," "[niche] gear list 2026," and "best tools for [activity]" all indicate strong purchase intent. Create content targeting these queries and link to your Kit.com storefront as the destination.</p>
<h2>Long-Tail Keyword Strategy</h2>
<p>Broad keywords ("best microphone") are too competitive. Specific keywords ("best USB microphone for podcast recording under $200") are achievable and attract buyers who are ready to purchase.</p>
<div class="tip-box"><strong>Quick win:</strong> Create one piece of SEO content per month targeting a specific "[niche] setup" or "[product type] recommendations" keyword. This builds consistent organic traffic over 12 months.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">Build Your Kit.com Storefront →</a></p>"""},
  {
    "title": "Kit.com vs Linktree — Which Is Better for Creators?",
    "keywords": "kit.com vs linktree, best link in bio creator, kit.com linktree comparison",
    "body": f"""<p>Many creators use Linktree as their link-in-bio solution. Kit.com does everything Linktree does — and also earns you money. Here is the comparison.</p>
<h2>What Linktree Offers</h2>
<p>Linktree gives you one URL that leads to a page of links. Clean, simple, free (with limitations). The free tier includes basic analytics and unlimited links. Paid plans add more customization.</p>
<h2>What Kit.com Offers</h2>
<p>Kit.com gives you a professional storefront that showcases your recommended products with descriptions, images, and affiliate links — all under one URL. Every product click can generate commission income. It's a link page that pays you.</p>
<h2>The Practical Difference</h2>
<p>Both solve the "one link" problem. But Linktree just routes traffic — it earns nothing from the people who click through to your recommendations. Kit.com turns every recommendation click into a potential commission.</p>
<h2>Can You Use Both?</h2>
<p>Yes. Many creators use Linktree for general links (social profiles, latest content, etc.) and Kit.com specifically for product recommendations. Or simply replace Linktree entirely with your Kit.com storefront and add non-product links as needed.</p>
<h2>Verdict</h2>
<p>If you regularly recommend products, Kit.com replaces Linktree and pays you. If you only need a link hub with no product recommendations, Linktree is sufficient.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn" rel="nofollow" target="_blank">Replace Linktree with Kit.com →</a></p>"""},
]

while len(POSTS) < 30:
    POSTS.append(POSTS[len(POSTS) % 10])

NAV = f"""<nav>
  <a href="{SITE_URL}/index.html" class="nav-logo" style="text-decoration:none;">🛠️ Kit<span>Authority</span>Hub</a>
  <a href="{AFF}" class="nav-cta" rel="nofollow" target="_blank">Get Started →</a>
</nav>"""

STICKY = f'<div class="sticky"><a href="{AFF}" rel="nofollow" target="_blank">🛠️ Join Kit.com Free — Build Your Creator Storefront</a></div>'

def build_post_html(post, slug, date_str):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{post['title']} | KitAuthorityHub</title>
<meta name="description" content="{post['keywords']}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{SITE_URL}/blog/{slug}">
<style>{CSS}</style>
</head>
<body>
{NAV}
<div class="container">
  <p class="meta">Published {date_str} &mdash; <a href="{SITE_URL}/blog-index.html">← All Posts</a> &mdash; by {BRAND}</p>
  <h1>{post['title']}</h1>
  {post['body']}
  <div style="border:1px solid #eee;padding:1.2rem;margin-top:2rem;border-radius:8px;background:#f9f9f9;">
    <strong>About KitAuthorityHub</strong><br>
    KitAuthorityHub independently reviews Kit.com and creator monetization platforms. Official Kit.com affiliate — ID: x3mb24l6x6vz.
  </div>
  <p style="text-align:center;margin-top:2rem;">
    <a href="{AFF}" class="btn" rel="nofollow" target="_blank">🛠️ Join Kit.com Free — Build Your Creator Storefront →</a>
  </p>
</div>
<footer><p>&copy; 2026 {BRAND} | <a href="{SITE_URL}/disclosure.html">Affiliate Disclosure</a> | Kit.com affiliate: x3mb24l6x6vz</p></footer>
{STICKY}
</body>
</html>"""

def gh_put(path, content, message):
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{path}"
    r = requests.get(url, headers=HEADERS)
    sha = r.json().get("sha") if r.status_code == 200 else None
    payload = {"message": message, "content": base64.b64encode(content.encode()).decode()}
    if sha:
        payload["sha"] = sha
    resp = requests.put(url, headers=HEADERS, json=payload)
    print(f"{'✅' if resp.status_code in (200,201) else '❌'} {path} ({resp.status_code})")

def load_blog_index():
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{BLOG_INDEX}"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        return json.loads(base64.b64decode(r.json()["content"]).decode())
    return []

def save_blog_index(data):
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{BLOG_INDEX}"
    r = requests.get(url, headers=HEADERS)
    sha = r.json().get("sha") if r.status_code == 200 else None
    payload = {"message": f"Blog index {datetime.utcnow().strftime('%Y-%m-%d')}",
               "content": base64.b64encode(json.dumps(data, indent=2).encode()).decode()}
    if sha:
        payload["sha"] = sha
    requests.put(url, headers=HEADERS, json=payload)

def build_blog_index_html(posts):
    items = "".join(f'<li style="margin-bottom:0.75rem;"><a href="{p["url"]}">{p["title"]}</a> <small style="color:#888;">({p["date"]})</small></li>' for p in reversed(posts[-30:]))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Kit.com Creator Blog 2026 | KitAuthorityHub</title>
<meta name="description" content="Kit.com guides, creator monetization tips, affiliate strategies, and SEO advice. Updated daily.">
<style>{CSS}
.hero{{background:#111;color:#fff;text-align:center;padding:3rem 1.5rem;}}
.hero h1{{font-size:2rem;font-weight:700;margin-bottom:0.5rem;}}
.hero h1 span{{color:#ff5a5f;}}
</style>
</head>
<body>
{NAV}
<div class="hero"><h1>🛠️ Kit<span>Authority</span>Hub Blog</h1><p style="color:rgba(255,255,255,0.75);">Kit.com guides, creator monetization tips, and affiliate strategies. Updated daily.</p></div>
<div class="container">
  <h2 style="border-bottom:2px solid #eee;padding-bottom:8px;margin-bottom:1.5rem;">Latest Posts</h2>
  <ul style="list-style:none;padding:0;">{items}</ul>
</div>
<footer><p>&copy; 2026 {BRAND} | <a href="{SITE_URL}/disclosure.html">Disclosure</a> | Kit.com affiliate: x3mb24l6x6vz</p></footer>
{STICKY}
</body>
</html>"""

if __name__ == "__main__":
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%B %d, %Y")
    day_num = now.timetuple().tm_yday % len(POSTS)
    post = POSTS[day_num]
    slug_base = post["title"].lower()
    for ch in " :,&'\"?!.—":
        slug_base = slug_base.replace(ch, "-")
    while "--" in slug_base:
        slug_base = slug_base.replace("--", "-")
    slug = slug_base[:60].strip("-") + f"-{now.strftime('%Y-%m-%d')}.html"
    gh_put(f"blog/{slug}", build_post_html(post, slug, date_str), f"Blog: {post['title']}")
    index = load_blog_index()
    index.append({"title": post["title"], "date": date_str, "url": f"blog/{slug}", "slug": slug})
    save_blog_index(index)
    gh_put("blog-index.html", build_blog_index_html(index), f"Blog index — {date_str}")
    print(f"✅ Published: {slug}")
