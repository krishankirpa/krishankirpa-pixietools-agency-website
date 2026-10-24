import os

out_dir = r"c:\Users\ASUS\Downloads\Pixietools\jack-portfolio\public\images\dashboards"

# 9. Shopify / E-Commerce High-Ticket Revenue Scale Dashboard
shopify_revenue_scale = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 540" width="840" height="540">
  <defs>
    <linearGradient id="shBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a1714"/>
      <stop offset="100%" stop-color="#050e0c"/>
    </linearGradient>
  </defs>
  <rect width="840" height="540" rx="20" fill="url(#shBg)" stroke="#065f46" stroke-width="2"/>
  <rect x="0" y="0" width="840" height="56" fill="#0f2922" rx="20 20 0 0"/>
  <rect x="24" y="16" width="24" height="24" rx="6" fill="#95BF47"/>
  <text x="32" y="33" fill="#ffffff" font-family="sans-serif" font-weight="900" font-size="14">S</text>
  <text x="56" y="33" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="700">Shopify &amp; High-Ticket Contract Revenue</text>
  <text x="360" y="33" fill="#a7f3d0" font-family="sans-serif" font-size="12">Live Gross Sales: $248,650.00 &bull; +64% MoM Growth</text>
  
  <g transform="translate(24, 76)">
    <rect x="0" y="0" width="250" height="110" rx="12" fill="#11332a" stroke="#059669"/>
    <text x="18" y="28" fill="#a7f3d0" font-family="sans-serif" font-size="11" font-weight="700">MONTHLY REVENUE</text>
    <text x="18" y="68" fill="#ffffff" font-family="sans-serif" font-size="34" font-weight="900">$248,650</text>
    <text x="18" y="94" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="700">&uarr; +64% vs last month</text>
  </g>
  <g transform="translate(294, 76)">
    <rect x="0" y="0" width="250" height="110" rx="12" fill="#11332a" stroke="#059669"/>
    <text x="18" y="28" fill="#a7f3d0" font-family="sans-serif" font-size="11" font-weight="700">ONLINE STORE CONVERSION</text>
    <text x="18" y="68" fill="#ffffff" font-family="sans-serif" font-size="34" font-weight="900">4.82%</text>
    <text x="18" y="94" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="700">&uarr; Top 2% in Niche</text>
  </g>
  <g transform="translate(564, 76)">
    <rect x="0" y="0" width="252" height="110" rx="12" fill="#11332a" stroke="#059669"/>
    <text x="18" y="28" fill="#a7f3d0" font-family="sans-serif" font-size="11" font-weight="700">AVERAGE ORDER VALUE</text>
    <text x="18" y="68" fill="#ffffff" font-family="sans-serif" font-size="34" font-weight="900">$18,450</text>
    <text x="18" y="94" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="700">Commercial / Residential</text>
  </g>
  
  <g transform="translate(24, 206)">
    <rect x="0" y="0" width="792" height="308" fill="#0d241e" rx="14" stroke="#059669"/>
    <line x1="50" y1="60" x2="740" y2="60" stroke="#164e3f" stroke-dasharray="4"/>
    <line x1="50" y1="130" x2="740" y2="130" stroke="#164e3f" stroke-dasharray="4"/>
    <line x1="50" y1="200" x2="740" y2="200" stroke="#164e3f" stroke-dasharray="4"/>
    <line x1="50" y1="260" x2="740" y2="260" stroke="#164e3f"/>
    <!-- Revenue Surge Curve -->
    <path d="M 50 250 Q 220 220, 380 150 T 560 90 T 740 40" fill="none" stroke="#10b981" stroke-width="4"/>
    <circle cx="740" cy="40" r="6" fill="#ffffff" stroke="#10b981" stroke-width="3"/>
    <text x="560" y="50" fill="#a7f3d0" font-family="sans-serif" font-size="12" font-weight="700">All-Time High Daily Revenue: $18,400</text>
  </g>
</svg>'''

# 10. GSC Detailed Queries Table with Rankings
gsc_search_queries = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 540" width="840" height="540">
  <defs>
    <linearGradient id="sqBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e172a"/>
      <stop offset="100%" stop-color="#080c16"/>
    </linearGradient>
  </defs>
  <rect width="840" height="540" rx="20" fill="url(#sqBg)" stroke="#1e293b" stroke-width="2"/>
  <rect x="0" y="0" width="840" height="56" fill="#131c2e" rx="20 20 0 0"/>
  <text x="24" y="34" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="700">Google Search Console &bull; Top Ranking Queries Table</text>
  <text x="440" y="34" fill="#94a3b8" font-family="sans-serif" font-size="12">1,248 Keywords in Top 10 Positions (320 in Top 3)</text>
  
  <g transform="translate(24, 76)">
    <rect x="0" y="0" width="792" height="438" fill="#111c2e" rx="12" stroke="#1e293b"/>
    <rect x="0" y="0" width="792" height="38" fill="#1e293b" rx="12 12 0 0"/>
    <text x="24" y="24" fill="#cbd5e1" font-family="sans-serif" font-size="11" font-weight="700">TARGET SEARCH QUERY</text>
    <text x="360" y="24" fill="#cbd5e1" font-family="sans-serif" font-size="11" font-weight="700">CLICKS</text>
    <text x="480" y="24" fill="#cbd5e1" font-family="sans-serif" font-size="11" font-weight="700">IMPRESSIONS</text>
    <text x="610" y="24" fill="#cbd5e1" font-family="sans-serif" font-size="11" font-weight="700">CTR</text>
    <text x="700" y="24" fill="#cbd5e1" font-family="sans-serif" font-size="11" font-weight="700">POSITION</text>
    
    <!-- Row 1 -->
    <g transform="translate(0, 48)">
      <text x="24" y="24" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="600">commercial roof replacement cost dallas</text>
      <text x="360" y="24" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="700">12,840</text>
      <text x="480" y="24" fill="#e2e8f0" font-family="sans-serif" font-size="13">184,200</text>
      <text x="610" y="24" fill="#10b981" font-family="sans-serif" font-size="13" font-weight="700">6.97%</text>
      <rect x="700" y="8" width="48" height="24" rx="4" fill="#10b981"/>
      <text x="718" y="24" fill="#000" font-family="sans-serif" font-size="12" font-weight="900">#1</text>
    </g>
    
    <!-- Row 2 -->
    <g transform="translate(0, 102)">
      <text x="24" y="24" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="600">residential standing seam metal roofing</text>
      <text x="360" y="24" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="700">9,320</text>
      <text x="480" y="24" fill="#e2e8f0" font-family="sans-serif" font-size="13">142,800</text>
      <text x="610" y="24" fill="#10b981" font-family="sans-serif" font-size="13" font-weight="700">6.52%</text>
      <rect x="700" y="8" width="48" height="24" rx="4" fill="#10b981"/>
      <text x="718" y="24" fill="#000" font-family="sans-serif" font-size="12" font-weight="900">#1</text>
    </g>
    
    <!-- Row 3 -->
    <g transform="translate(0, 156)">
      <text x="24" y="24" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="600">emergency hail damage roof inspection</text>
      <text x="360" y="24" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="700">7,140</text>
      <text x="480" y="24" fill="#e2e8f0" font-family="sans-serif" font-size="13">98,600</text>
      <text x="610" y="24" fill="#10b981" font-family="sans-serif" font-size="13" font-weight="700">7.24%</text>
      <rect x="700" y="8" width="48" height="24" rx="4" fill="#10b981"/>
      <text x="718" y="24" fill="#000" font-family="sans-serif" font-size="12" font-weight="900">#1</text>
    </g>
    
    <!-- Row 4 -->
    <g transform="translate(0, 210)">
      <text x="24" y="24" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="600">best flat roof coating contractors</text>
      <text x="360" y="24" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="700">5,210</text>
      <text x="480" y="24" fill="#e2e8f0" font-family="sans-serif" font-size="13">78,400</text>
      <text x="610" y="24" fill="#10b981" font-family="sans-serif" font-size="13" font-weight="700">6.64%</text>
      <rect x="700" y="8" width="48" height="24" rx="4" fill="#10b981"/>
      <text x="718" y="24" fill="#000" font-family="sans-serif" font-size="12" font-weight="900">#2</text>
    </g>
    
    <!-- Row 5 -->
    <g transform="translate(0, 264)">
      <text x="24" y="24" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="600">industrial tpo roofing companies</text>
      <text x="360" y="24" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="700">4,890</text>
      <text x="480" y="24" fill="#e2e8f0" font-family="sans-serif" font-size="13">64,200</text>
      <text x="610" y="24" fill="#10b981" font-family="sans-serif" font-size="13" font-weight="700">7.61%</text>
      <rect x="700" y="8" width="48" height="24" rx="4" fill="#10b981"/>
      <text x="718" y="24" fill="#000" font-family="sans-serif" font-size="12" font-weight="900">#2</text>
    </g>
    
    <!-- Row 6 -->
    <g transform="translate(0, 318)">
      <text x="24" y="24" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="600">luxury slate roofing specialist</text>
      <text x="360" y="24" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="700">3,780</text>
      <text x="480" y="24" fill="#e2e8f0" font-family="sans-serif" font-size="13">52,100</text>
      <text x="610" y="24" fill="#10b981" font-family="sans-serif" font-size="13" font-weight="700">7.25%</text>
      <rect x="700" y="8" width="48" height="24" rx="4" fill="#10b981"/>
      <text x="718" y="24" fill="#000" font-family="sans-serif" font-size="12" font-weight="900">#3</text>
    </g>
  </g>
</svg>'''

# 11. Viral Video Hook Retention Curve
video_hook_retention = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 540" width="840" height="540">
  <defs>
    <linearGradient id="vrBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#14081c"/>
      <stop offset="100%" stop-color="#08030f"/>
    </linearGradient>
  </defs>
  <rect width="840" height="540" rx="20" fill="url(#vrBg)" stroke="#581c87" stroke-width="2"/>
  <rect x="0" y="0" width="840" height="56" fill="#200d30" rx="20 20 0 0"/>
  <text x="24" y="34" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="700">TikTok &amp; Instagram Reel Retention Curve</text>
  <text x="380" y="34" fill="#d8b4fe" font-family="sans-serif" font-size="12">Direct-Response Video Ad Creative Audit &bull; 1.4M Views</text>
  
  <g transform="translate(24, 76)">
    <rect x="0" y="0" width="792" height="438" fill="#170c22" rx="12" stroke="#3b0764"/>
    
    <!-- Retention Metrics -->
    <g transform="translate(30, 30)">
      <text x="0" y="20" fill="#a855f7" font-family="sans-serif" font-size="12" font-weight="700">3-SECOND HOOK RATE</text>
      <text x="0" y="58" fill="#34d399" font-family="sans-serif" font-size="34" font-weight="900">78.4%</text>
      <text x="0" y="80" fill="#94a3b8" font-family="sans-serif" font-size="11">Benchmark: 42%</text>
    </g>
    <g transform="translate(280, 30)">
      <text x="0" y="20" fill="#a855f7" font-family="sans-serif" font-size="12" font-weight="700">AVG PERCENT VIEWED</text>
      <text x="0" y="58" fill="#38bdf8" font-family="sans-serif" font-size="34" font-weight="900">92.6%</text>
      <text x="0" y="80" fill="#94a3b8" font-family="sans-serif" font-size="11">Completion: 64%</text>
    </g>
    <g transform="translate(540, 30)">
      <text x="0" y="20" fill="#a855f7" font-family="sans-serif" font-size="12" font-weight="700">VIRAL SHARES &amp; SAVES</text>
      <text x="0" y="58" fill="#ffffff" font-family="sans-serif" font-size="34" font-weight="900">28.4K</text>
      <text x="0" y="80" fill="#34d399" font-family="sans-serif" font-size="11">&uarr; Algorithm Loop Active</text>
    </g>
    
    <!-- Retention Graph Line -->
    <line x1="40" y1="360" x2="740" y2="360" stroke="#3b0764"/>
    <!-- Industry average line (Grey dashed) -->
    <path d="M 40 200 Q 150 280, 350 320 T 740 340" fill="none" stroke="#64748b" stroke-width="2" stroke-dasharray="6"/>
    <text x="560" y="325" fill="#64748b" font-family="sans-serif" font-size="10">Competitor Average (42%)</text>
    
    <!-- Yogesh Panwar Video Editing Retention Line (Purple/Cyan Glow) -->
    <path d="M 40 160 Q 150 180, 350 210 T 740 240" fill="none" stroke="#a855f7" stroke-width="4"/>
    <circle cx="740" cy="240" r="6" fill="#ffffff" stroke="#a855f7" stroke-width="3"/>
    <text x="520" y="225" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="700">Yogesh Panwar Edited Reel (78.4%)</text>
  </g>
</svg>'''

# 12. Meta Audience Segmentation & Lookalikes
meta_audience_lookalikes = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 540" width="840" height="540">
  <defs>
    <linearGradient id="auBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1326"/>
      <stop offset="100%" stop-color="#060a14"/>
    </linearGradient>
  </defs>
  <rect width="840" height="540" rx="20" fill="url(#auBg)" stroke="#1e3a8a" stroke-width="2"/>
  <rect x="0" y="0" width="840" height="56" fill="#132342" rx="20 20 0 0"/>
  <text x="24" y="34" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="700">Meta Custom Audiences &amp; CAPI Signal Match</text>
  <text x="420" y="34" fill="#93c5fd" font-family="sans-serif" font-size="12">Server-Side Meta Conversions API &bull; 9.4/10 Quality Score</text>
  
  <g transform="translate(24, 76)">
    <rect x="0" y="0" width="792" height="438" fill="#0f1d36" rx="12" stroke="#1e3a8a"/>
    
    <g transform="translate(24, 30)">
      <rect x="0" y="0" width="744" height="68" rx="8" fill="#152747"/>
      <text x="18" y="28" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="700">Lookalike (US, 1%) - High-Ticket Roof Replacement Buyers</text>
      <text x="18" y="52" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="700">Match Rate: 94.2% &bull; Size: 2.4M &bull; Blended ROAS: 5.84x</text>
      <rect x="620" y="18" width="100" height="32" rx="6" fill="#0081FB"/>
      <text x="642" y="38" fill="#fff" font-family="sans-serif" font-size="11" font-weight="700">Scaling &uarr;</text>
    </g>
    
    <g transform="translate(24, 114)">
      <rect x="0" y="0" width="744" height="68" rx="8" fill="#152747"/>
      <text x="18" y="28" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="700">Custom Audience - Video Viewers 75% + 95% (Last 30D)</text>
      <text x="18" y="52" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="700">Warm Retargeting &bull; Size: 184,000 &bull; Cost Per Lead: $14.20</text>
      <rect x="620" y="18" width="100" height="32" rx="6" fill="#10b981"/>
      <text x="646" y="38" fill="#000" font-family="sans-serif" font-size="11" font-weight="900">Active</text>
    </g>
    
    <g transform="translate(24, 198)">
      <rect x="0" y="0" width="744" height="68" rx="8" fill="#152747"/>
      <text x="18" y="28" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="700">Website High-Intent Lead Form Abandoners (14D)</text>
      <text x="18" y="52" fill="#fbbf24" font-family="sans-serif" font-size="12" font-weight="700">Direct Closing Angle &bull; Size: 28,400 &bull; ROAS: 7.12x</text>
      <rect x="620" y="18" width="100" height="32" rx="6" fill="#10b981"/>
      <text x="646" y="38" fill="#000" font-family="sans-serif" font-size="11" font-weight="900">Active</text>
    </g>
    
    <g transform="translate(24, 282)">
      <rect x="0" y="0" width="744" height="120" rx="8" fill="#0a1527"/>
      <text x="18" y="30" fill="#93c5fd" font-family="sans-serif" font-size="12" font-weight="700">META CAPI SERVER-SIDE TELEMETRY</text>
      <text x="18" y="56" fill="#ffffff" font-family="sans-serif" font-size="13">Event Deduplication: 100% &bull; External ID &amp; Phone Hash Matched: 98.4%</text>
      <text x="18" y="80" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="700">&bull; Zero data loss from iOS 14 / browser ad-blockers</text>
      <text x="18" y="104" fill="#a7f3d0" font-family="sans-serif" font-size="11">Full funnel attribution calibrated for maximum algorithmic ROAS delivery</text>
    </g>
  </g>
</svg>'''

more_files = {
    "shopify_revenue_scale.svg": shopify_revenue_scale,
    "gsc_search_queries.svg": gsc_search_queries,
    "video_hook_retention.svg": video_hook_retention,
    "meta_audience_lookalikes.svg": meta_audience_lookalikes,
}

for filename, content in more_files.items():
    filepath = os.path.join(out_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated: {filename} ({len(content)} bytes)")
