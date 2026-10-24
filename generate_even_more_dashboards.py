import os

out_dir = r"c:\Users\ASUS\Downloads\Pixietools\jack-portfolio\public\images\dashboards"

# 13. Google Ads PPC Lead Dashboard
google_ads_ppc_scale = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 540" width="840" height="540">
  <defs>
    <linearGradient id="gadsBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a1324"/>
      <stop offset="100%" stop-color="#050a14"/>
    </linearGradient>
  </defs>
  <rect width="840" height="540" rx="20" fill="url(#gadsBg)" stroke="#1e3a8a" stroke-width="2"/>
  <rect x="0" y="0" width="840" height="56" fill="#101d36" rx="20 20 0 0"/>
  <rect x="24" y="16" width="24" height="24" rx="6" fill="#4285F4"/>
  <text x="32" y="33" fill="#ffffff" font-family="sans-serif" font-weight="900" font-size="14">G</text>
  <text x="56" y="33" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="700">Google Ads &bull; Search Campaigns</text>
  <text x="320" y="33" fill="#93c5fd" font-family="sans-serif" font-size="12">High-Ticket Roof Replacement &bull; Exact Match High-Intent</text>
  
  <rect x="680" y="14" width="136" height="28" rx="14" fill="#3b82f6" opacity="0.2"/>
  <text x="696" y="32" fill="#60a5fa" font-family="sans-serif" font-size="11" font-weight="700">TARGET ROAS</text>
  
  <g transform="translate(24, 76)">
    <rect x="0" y="0" width="186" height="84" rx="12" fill="#13233e" stroke="#1e3a8a"/>
    <text x="16" y="26" fill="#93c5fd" font-family="sans-serif" font-size="11" font-weight="700">TOTAL SPEND</text>
    <text x="16" y="56" fill="#ffffff" font-family="sans-serif" font-size="22" font-weight="800">$28,400.00</text>
    <text x="16" y="74" fill="#60a5fa" font-family="sans-serif" font-size="10">Target Search Top #1</text>
  </g>
  <g transform="translate(226, 76)">
    <rect x="0" y="0" width="186" height="84" rx="12" fill="#13233e" stroke="#1e3a8a"/>
    <text x="16" y="26" fill="#93c5fd" font-family="sans-serif" font-size="11" font-weight="700">QUALIFIED LEADS</text>
    <text x="16" y="56" fill="#10b981" font-family="sans-serif" font-size="24" font-weight="800">420 Calls</text>
    <text x="16" y="74" fill="#34d399" font-family="sans-serif" font-size="10">Conversion Rate: 16.4%</text>
  </g>
  <g transform="translate(428, 76)">
    <rect x="0" y="0" width="186" height="84" rx="12" fill="#13233e" stroke="#1e3a8a"/>
    <text x="16" y="26" fill="#93c5fd" font-family="sans-serif" font-size="11" font-weight="700">COST PER CALL (CPL)</text>
    <text x="16" y="56" fill="#ffffff" font-family="sans-serif" font-size="22" font-weight="800">$67.60</text>
    <text x="16" y="74" fill="#34d399" font-family="sans-serif" font-size="10">&#8595; -48% vs Industry Avg</text>
  </g>
  <g transform="translate(630, 76)">
    <rect x="0" y="0" width="186" height="84" rx="12" fill="#13233e" stroke="#1e3a8a"/>
    <text x="16" y="26" fill="#93c5fd" font-family="sans-serif" font-size="11" font-weight="700">PIPELINE VALUE</text>
    <text x="16" y="56" fill="#34d399" font-family="sans-serif" font-size="22" font-weight="800">$1,420,000</text>
    <text x="16" y="74" fill="#34d399" font-family="sans-serif" font-size="10">72 Closed Roofs</text>
  </g>
  
  <g transform="translate(24, 180)">
    <rect x="0" y="0" width="792" height="336" fill="#0d182c" rx="12" stroke="#1e3a8a"/>
    <line x1="40" y1="60" x2="750" y2="60" stroke="#1e293b" stroke-dasharray="4"/>
    <line x1="40" y1="130" x2="750" y2="130" stroke="#1e293b" stroke-dasharray="4"/>
    <line x1="40" y1="200" x2="750" y2="200" stroke="#1e293b" stroke-dasharray="4"/>
    <line x1="40" y1="260" x2="750" y2="260" stroke="#1e293b"/>
    <!-- Growth trajectory curve -->
    <path d="M 40 240 Q 200 220, 380 150 T 560 90 T 740 40" fill="none" stroke="#60a5fa" stroke-width="4"/>
    <circle cx="740" cy="40" r="6" fill="#ffffff" stroke="#3b82f6" stroke-width="3"/>
    <text x="560" y="55" fill="#93c5fd" font-family="sans-serif" font-size="12" font-weight="700">Impression Share: 84.2% Absolute Top</text>
  </g>
</svg>'''

# 14. E-Commerce & High-Ticket Funnel Breakdown
ecommerce_funnel = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 540" width="840" height="540">
  <defs>
    <linearGradient id="fnBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#120c1e"/>
      <stop offset="100%" stop-color="#07040d"/>
    </linearGradient>
  </defs>
  <rect width="840" height="540" rx="20" fill="url(#fnBg)" stroke="#3b0764" stroke-width="2"/>
  <rect x="0" y="0" width="840" height="56" fill="#1e0d33" rx="20 20 0 0"/>
  <text x="24" y="34" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="700">Full-Funnel Conversion &amp; Friction Elimination</text>
  <text x="380" y="34" fill="#d8b4fe" font-family="sans-serif" font-size="12">142,000 Visitors &bull; 4.82% Overall Conversion Rate</text>
  
  <g transform="translate(24, 76)">
    <rect x="0" y="0" width="792" height="438" fill="#160c24" rx="12" stroke="#3b0764"/>
    
    <!-- Stage 1 -->
    <g transform="translate(24, 30)">
      <rect x="0" y="0" width="744" height="60" rx="8" fill="#221138"/>
      <text x="20" y="34" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="700">1. Landing Page Visitors</text>
      <text x="260" y="34" fill="#c084fc" font-family="sans-serif" font-size="13">142,000 Sessions</text>
      <text x="620" y="34" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="800">100% Volume</text>
    </g>
    <!-- Stage 2 -->
    <g transform="translate(24, 102)">
      <rect x="0" y="0" width="744" height="60" rx="8" fill="#221138"/>
      <text x="20" y="34" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="700">2. Instant Lead Form Initiated</text>
      <text x="260" y="34" fill="#c084fc" font-family="sans-serif" font-size="13">18,420 Users</text>
      <text x="620" y="34" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="800">12.9% Dropoff: Low</text>
    </g>
    <!-- Stage 3 -->
    <g transform="translate(24, 174)">
      <rect x="0" y="0" width="744" height="60" rx="8" fill="#221138"/>
      <text x="20" y="34" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="700">3. Phone Call / Booking Completed</text>
      <text x="260" y="34" fill="#c084fc" font-family="sans-serif" font-size="13">6,840 Calls Booked</text>
      <text x="620" y="34" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="800">37.1% Completion</text>
    </g>
    <!-- Stage 4 -->
    <g transform="translate(24, 246)">
      <rect x="0" y="0" width="744" height="60" rx="8" fill="#221138"/>
      <text x="20" y="34" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="700">4. Signed Contractor Deals</text>
      <text x="260" y="34" fill="#34d399" font-family="sans-serif" font-size="14" font-weight="800">1,428 Closed Contracts</text>
      <text x="620" y="34" fill="#34d399" font-family="sans-serif" font-size="14" font-weight="900">$4,280,000 Value</text>
    </g>
    
    <g transform="translate(24, 326)">
      <text x="20" y="24" fill="#94a3b8" font-family="sans-serif" font-size="12">Optimized by Yogesh Panwar: Frictionless mobile form + Instant WhatsApp routing</text>
      <text x="20" y="46" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="700">&#8593; Result: 2.8x higher closing rate compared to standard email lead forms</text>
    </g>
  </g>
</svg>'''

# 15. Video Split Testing Hook Matrix
video_split_hooks = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 540" width="840" height="540">
  <defs>
    <linearGradient id="vsBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#180c14"/>
      <stop offset="100%" stop-color="#0a0509"/>
    </linearGradient>
  </defs>
  <rect width="840" height="540" rx="20" fill="url(#vsBg)" stroke="#831843" stroke-width="2"/>
  <rect x="0" y="0" width="840" height="56" fill="#2a0f20" rx="20 20 0 0"/>
  <text x="24" y="34" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="700">Direct-Response Video Hook Split Test</text>
  <text x="360" y="34" fill="#f472b6" font-family="sans-serif" font-size="12">Hook Rate Comparison Across 3 Creative Variants</text>
  
  <g transform="translate(24, 76)">
    <rect x="0" y="0" width="248" height="430" rx="12" fill="#22101b" stroke="#be185d"/>
    <rect x="14" y="14" width="220" height="200" rx="8" fill="#180812"/>
    <rect x="24" y="24" width="80" height="24" rx="4" fill="#10b981"/>
    <text x="32" y="40" fill="#000" font-family="sans-serif" font-size="10" font-weight="900">WINNER</text>
    <text x="124" y="110" text-anchor="middle" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="800">Hook A: "Secret Leak"</text>
    <text x="124" y="130" text-anchor="middle" fill="#f472b6" font-family="sans-serif" font-size="10">Emotional Pattern Interrupt</text>
    <text x="16" y="250" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="700">3s Hook: 78.4%</text>
    <text x="16" y="275" fill="#34d399" font-family="sans-serif" font-size="14" font-weight="800">ROAS: 6.42x</text>
    <text x="16" y="300" fill="#f472b6" font-family="sans-serif" font-size="11">1.4M Views &bull; $84K Rev</text>
    <rect x="16" y="350" width="216" height="36" rx="8" fill="#be185d"/>
    <text x="80" y="372" fill="#fff" font-family="sans-serif" font-size="11" font-weight="700">Primary Scale</text>
  </g>
  
  <g transform="translate(296, 76)">
    <rect x="0" y="0" width="248" height="430" rx="12" fill="#22101b" stroke="#3b0764"/>
    <rect x="14" y="14" width="220" height="200" rx="8" fill="#180812"/>
    <rect x="24" y="24" width="80" height="24" rx="4" fill="#64748b"/>
    <text x="32" y="40" fill="#fff" font-family="sans-serif" font-size="10" font-weight="900">CONTROL</text>
    <text x="124" y="110" text-anchor="middle" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="800">Hook B: "Need a Roof?"</text>
    <text x="124" y="130" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="10">Traditional Pitch</text>
    <text x="16" y="250" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="700">3s Hook: 34.2%</text>
    <text x="16" y="275" fill="#e2e8f0" font-family="sans-serif" font-size="14" font-weight="800">ROAS: 2.10x</text>
    <text x="16" y="300" fill="#94a3b8" font-family="sans-serif" font-size="11">High dropoff at 0:02</text>
    <rect x="16" y="350" width="216" height="36" rx="8" fill="#1e1822"/>
    <text x="96" y="372" fill="#64748b" font-family="sans-serif" font-size="11" font-weight="700">Paused</text>
  </g>
  
  <g transform="translate(568, 76)">
    <rect x="0" y="0" width="248" height="430" rx="12" fill="#22101b" stroke="#3b82f6"/>
    <rect x="14" y="14" width="220" height="200" rx="8" fill="#180812"/>
    <rect x="24" y="24" width="80" height="24" rx="4" fill="#3b82f6"/>
    <text x="32" y="40" fill="#fff" font-family="sans-serif" font-size="10" font-weight="900">SCALE</text>
    <text x="124" y="110" text-anchor="middle" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="800">Hook C: "Hail Storm Alert"</text>
    <text x="124" y="130" text-anchor="middle" fill="#93c5fd" font-family="sans-serif" font-size="10">Urgency &amp; Insurance</text>
    <text x="16" y="250" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="700">3s Hook: 68.9%</text>
    <text x="16" y="275" fill="#34d399" font-family="sans-serif" font-size="14" font-weight="800">ROAS: 5.12x</text>
    <text x="16" y="300" fill="#93c5fd" font-family="sans-serif" font-size="11">820K Views &bull; $52K Rev</text>
    <rect x="16" y="350" width="216" height="36" rx="8" fill="#1e293b" stroke="#3b82f6"/>
    <text x="88" y="372" fill="#93c5fd" font-family="sans-serif" font-size="11" font-weight="700">Active Retarget</text>
  </g>
</svg>'''

# 16. Google 5-Star Reviews & Trust Signals Engine
local_seo_review_engine = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 540" width="840" height="540">
  <defs>
    <linearGradient id="reBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a1a17"/>
      <stop offset="100%" stop-color="#040e0c"/>
    </linearGradient>
  </defs>
  <rect width="840" height="540" rx="20" fill="url(#reBg)" stroke="#047857" stroke-width="2"/>
  <rect x="0" y="0" width="840" height="56" fill="#0d2b24" rx="20 20 0 0"/>
  <text x="24" y="34" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="700">Google Business Profile &bull; Review Velocity Engine</text>
  <text x="360" y="34" fill="#6ee7b7" font-family="sans-serif" font-size="12">284 Verified 5-Star Reviews &bull; 4.98 Aggregate Rating</text>
  
  <g transform="translate(24, 76)">
    <rect x="0" y="0" width="792" height="438" fill="#0a241e" rx="12" stroke="#059669"/>
    
    <g transform="translate(30, 30)">
      <text x="0" y="20" fill="#a7f3d0" font-family="sans-serif" font-size="12" font-weight="700">GOOGLE RATING</text>
      <text x="0" y="64" fill="#ffffff" font-family="sans-serif" font-size="44" font-weight="900">4.98 &#9733;</text>
      <text x="0" y="90" fill="#34d399" font-family="sans-serif" font-size="11">284 Verified Reviews</text>
    </g>
    <g transform="translate(280, 30)">
      <text x="0" y="20" fill="#a7f3d0" font-family="sans-serif" font-size="12" font-weight="700">MONTHLY INBOUND CALLS</text>
      <text x="0" y="64" fill="#34d399" font-family="sans-serif" font-size="44" font-weight="900">384</text>
      <text x="0" y="90" fill="#a7f3d0" font-family="sans-serif" font-size="11">+185% vs Old Profile</text>
    </g>
    <g transform="translate(540, 30)">
      <text x="0" y="20" fill="#a7f3d0" font-family="sans-serif" font-size="12" font-weight="700">LOCAL PACK LOCKOUT</text>
      <text x="0" y="64" fill="#38bdf8" font-family="sans-serif" font-size="44" font-weight="900">100%</text>
      <text x="0" y="90" fill="#6ee7b7" font-family="sans-serif" font-size="11">Top 3 in 15-Mile Radius</text>
    </g>
    
    <!-- Testimonial rows -->
    <g transform="translate(30, 140)">
      <rect x="0" y="0" width="732" height="70" rx="8" fill="#11362e"/>
      <text x="16" y="28" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="700">"Yogesh's team ranked our roofing company #1 in Dallas within 90 days. We closed 48 replacements!"</text>
      <text x="16" y="52" fill="#34d399" font-family="sans-serif" font-size="11">&bull; Mark Henderson, Owner &bull; $980,000 Verified Closed Work</text>
    </g>
    <g transform="translate(30, 226)">
      <rect x="0" y="0" width="732" height="70" rx="8" fill="#11362e"/>
      <text x="16" y="28" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="700">"The combination of Google Ads + Meta video creative doubled our qualified calls. Best agency ROI."</text>
      <text x="16" y="52" fill="#34d399" font-family="sans-serif" font-size="11">&bull; David R., Commercial General Contractor &bull; 5.4x ROAS</text>
    </g>
    
    <g transform="translate(30, 320)">
      <text x="0" y="24" fill="#a7f3d0" font-family="sans-serif" font-size="12" font-weight="700">&#8593; Engineered by Yogesh Panwar: Google Business Profile Optimization &amp; Automated Review Funnels</text>
    </g>
  </g>
</svg>'''

files = {
    "google_ads_ppc_scale.svg": google_ads_ppc_scale,
    "ecommerce_funnel.svg": ecommerce_funnel,
    "video_split_hooks.svg": video_split_hooks,
    "local_seo_review_engine.svg": local_seo_review_engine,
}

for filename, content in files.items():
    filepath = os.path.join(out_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated: {filename} ({len(content)} bytes)")
