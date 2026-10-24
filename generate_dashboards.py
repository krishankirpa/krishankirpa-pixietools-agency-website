import os

out_dir = r"c:\Users\ASUS\Downloads\Pixietools\jack-portfolio\public\images\dashboards"
os.makedirs(out_dir, exist_ok=True)

# 1. Meta Ads Manager Main Dashboard
meta_ads_manager = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 540" width="840" height="540">
  <defs>
    <linearGradient id="metaBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b101b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0081FB"/>
      <stop offset="100%" stop-color="#00C6FF"/>
    </linearGradient>
  </defs>
  <!-- Background -->
  <rect width="840" height="540" rx="20" fill="url(#metaBg)" stroke="#1e293b" stroke-width="2"/>
  
  <!-- Top Bar -->
  <rect x="0" y="0" width="840" height="56" fill="#131c2e" rx="20 20 0 0"/>
  <circle cx="28" cy="28" r="6" fill="#ef4444"/>
  <circle cx="48" cy="28" r="6" fill="#f59e0b"/>
  <circle cx="68" cy="28" r="6" fill="#10b981"/>
  
  <!-- Meta Header -->
  <path d="M110 32 C115 20, 125 20, 130 32 C135 20, 145 20, 150 32 C145 44, 135 44, 130 32 C125 44, 115 44, 110 32 Z" fill="none" stroke="#0081FB" stroke-width="3"/>
  <text x="160" y="33" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="700">Meta Ads Manager</text>
  <text x="310" y="33" fill="#64748b" font-family="sans-serif" font-size="12">Account ID: 849-204-1829 &bull; Last 30 Days</text>
  
  <rect x="700" y="14" width="116" height="28" rx="14" fill="#0081FB" opacity="0.15"/>
  <rect x="700" y="14" width="116" height="28" rx="14" fill="none" stroke="#0081FB" stroke-width="1"/>
  <circle cx="714" cy="28" r="4" fill="#10b981"/>
  <text x="726" y="32" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="600">LIVE TRACKING</text>
  
  <!-- KPI Metrics Bar -->
  <g transform="translate(24, 76)">
    <!-- KPI 1 -->
    <rect x="0" y="0" width="186" height="84" rx="12" fill="#162032" stroke="#1e293b"/>
    <text x="16" y="26" fill="#94a3b8" font-family="sans-serif" font-size="11" font-weight="600" letter-spacing="0.5">AMOUNT SPENT</text>
    <text x="16" y="56" fill="#ffffff" font-family="sans-serif" font-size="22" font-weight="800">$34,820.00</text>
    <text x="16" y="74" fill="#10b981" font-family="sans-serif" font-size="10" font-weight="600">&uarr; Budget Pacing 98.4%</text>
    
    <!-- KPI 2 -->
    <rect x="202" y="0" width="186" height="84" rx="12" fill="#162032" stroke="#1e293b"/>
    <text x="218" y="26" fill="#94a3b8" font-family="sans-serif" font-size="11" font-weight="600" letter-spacing="0.5">PURCHASE ROAS</text>
    <text x="218" y="56" fill="#10b981" font-family="sans-serif" font-size="24" font-weight="800">5.41x</text>
    <text x="286" y="54" fill="#64748b" font-family="sans-serif" font-size="11">Avg</text>
    <text x="218" y="74" fill="#10b981" font-family="sans-serif" font-size="10" font-weight="600">&uarr; +42% vs Prev Period</text>
    
    <!-- KPI 3 -->
    <rect x="404" y="0" width="186" height="84" rx="12" fill="#162032" stroke="#1e293b"/>
    <text x="420" y="26" fill="#94a3b8" font-family="sans-serif" font-size="11" font-weight="600" letter-spacing="0.5">TOTAL PURCHASES</text>
    <text x="420" y="56" fill="#ffffff" font-family="sans-serif" font-size="22" font-weight="800">1,428</text>
    <text x="420" y="74" fill="#38bdf8" font-family="sans-serif" font-size="10" font-weight="600">CPA: $24.38</text>
    
    <!-- KPI 4 -->
    <rect x="606" y="0" width="186" height="84" rx="12" fill="#162032" stroke="#1e293b"/>
    <text x="622" y="26" fill="#94a3b8" font-family="sans-serif" font-size="11" font-weight="600" letter-spacing="0.5">CONVERSION VALUE</text>
    <text x="622" y="56" fill="#38bdf8" font-family="sans-serif" font-size="22" font-weight="800">$188,376</text>
    <text x="622" y="74" fill="#10b981" font-family="sans-serif" font-size="10" font-weight="600">&uarr; Profitable Scaling</text>
  </g>
  
  <!-- Campaign Table Header -->
  <g transform="translate(24, 180)">
    <rect x="0" y="0" width="792" height="34" fill="#1e293b" rx="6"/>
    <text x="16" y="22" fill="#cbd5e1" font-family="sans-serif" font-size="11" font-weight="700">CAMPAIGN NAME</text>
    <text x="270" y="22" fill="#cbd5e1" font-family="sans-serif" font-size="11" font-weight="700">DELIVERY</text>
    <text x="360" y="22" fill="#cbd5e1" font-family="sans-serif" font-size="11" font-weight="700">DAILY BUDGET</text>
    <text x="470" y="22" fill="#cbd5e1" font-family="sans-serif" font-size="11" font-weight="700">SPENT</text>
    <text x="560" y="22" fill="#cbd5e1" font-family="sans-serif" font-size="11" font-weight="700">ROAS</text>
    <text x="640" y="22" fill="#cbd5e1" font-family="sans-serif" font-size="11" font-weight="700">PURCHASES</text>
    <text x="730" y="22" fill="#cbd5e1" font-family="sans-serif" font-size="11" font-weight="700">VALUE</text>
  </g>
  
  <!-- Table Rows -->
  <!-- Row 1 -->
  <g transform="translate(24, 222)">
    <rect x="0" y="0" width="792" height="48" fill="#131c2e" rx="6" stroke="#1e293b"/>
    <circle cx="16" cy="24" r="5" fill="#10b981"/>
    <text x="32" y="28" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="600">[SCALE] CBO - Broad Targeting - Winning Angles</text>
    <rect x="270" y="14" width="60" height="20" rx="10" fill="#10b981" opacity="0.2"/>
    <text x="280" y="28" fill="#10b981" font-family="sans-serif" font-size="10" font-weight="700">Active</text>
    <text x="360" y="28" fill="#e2e8f0" font-family="sans-serif" font-size="12">$650.00</text>
    <text x="470" y="28" fill="#e2e8f0" font-family="sans-serif" font-size="12">$14,240</text>
    <text x="560" y="28" fill="#10b981" font-family="sans-serif" font-size="13" font-weight="800">5.82x</text>
    <text x="650" y="28" fill="#e2e8f0" font-family="sans-serif" font-size="12">624</text>
    <text x="724" y="28" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="700">$82,876</text>
  </g>
  
  <!-- Row 2 -->
  <g transform="translate(24, 278)">
    <rect x="0" y="0" width="792" height="48" fill="#131c2e" rx="6" stroke="#1e293b"/>
    <circle cx="16" cy="24" r="5" fill="#10b981"/>
    <text x="32" y="28" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="600">[TEST] Dynamic Creative - Video Hooks V3</text>
    <rect x="270" y="14" width="60" height="20" rx="10" fill="#10b981" opacity="0.2"/>
    <text x="280" y="28" fill="#10b981" font-family="sans-serif" font-size="10" font-weight="700">Active</text>
    <text x="360" y="28" fill="#e2e8f0" font-family="sans-serif" font-size="12">$250.00</text>
    <text x="470" y="28" fill="#e2e8f0" font-family="sans-serif" font-size="12">$6,840</text>
    <text x="560" y="28" fill="#10b981" font-family="sans-serif" font-size="13" font-weight="800">6.14x</text>
    <text x="650" y="28" fill="#e2e8f0" font-family="sans-serif" font-size="12">298</text>
    <text x="724" y="28" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="700">$41,997</text>
  </g>
  
  <!-- Row 3 -->
  <g transform="translate(24, 334)">
    <rect x="0" y="0" width="792" height="48" fill="#131c2e" rx="6" stroke="#1e293b"/>
    <circle cx="16" cy="24" r="5" fill="#10b981"/>
    <text x="32" y="28" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="600">[RETARGET] High-Intent Visitors 7D - Social Proof</text>
    <rect x="270" y="14" width="60" height="20" rx="10" fill="#10b981" opacity="0.2"/>
    <text x="280" y="28" fill="#10b981" font-family="sans-serif" font-size="10" font-weight="700">Active</text>
    <text x="360" y="28" fill="#e2e8f0" font-family="sans-serif" font-size="12">$200.00</text>
    <text x="470" y="28" fill="#e2e8f0" font-family="sans-serif" font-size="12">$4,920</text>
    <text x="560" y="28" fill="#10b981" font-family="sans-serif" font-size="13" font-weight="800">6.80x</text>
    <text x="650" y="28" fill="#e2e8f0" font-family="sans-serif" font-size="12">214</text>
    <text x="724" y="28" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="700">$33,456</text>
  </g>
  
  <!-- Row 4 -->
  <g transform="translate(24, 390)">
    <rect x="0" y="0" width="792" height="48" fill="#131c2e" rx="6" stroke="#1e293b"/>
    <circle cx="16" cy="24" r="5" fill="#10b981"/>
    <text x="32" y="28" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="600">[SCALE] Lookalike Audiences 1% - High-Ticket Leads</text>
    <rect x="270" y="14" width="60" height="20" rx="10" fill="#10b981" opacity="0.2"/>
    <text x="280" y="28" fill="#10b981" font-family="sans-serif" font-size="10" font-weight="700">Active</text>
    <text x="360" y="28" fill="#e2e8f0" font-family="sans-serif" font-size="12">$300.00</text>
    <text x="470" y="28" fill="#e2e8f0" font-family="sans-serif" font-size="12">$8,820</text>
    <text x="560" y="28" fill="#10b981" font-family="sans-serif" font-size="13" font-weight="800">4.52x</text>
    <text x="650" y="28" fill="#e2e8f0" font-family="sans-serif" font-size="12">292</text>
    <text x="724" y="28" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="700">$39,867</text>
  </g>
  
  <!-- Bottom status strip -->
  <g transform="translate(24, 456)">
    <rect x="0" y="0" width="792" height="56" fill="#0d1424" rx="10" stroke="#1e293b"/>
    <text x="20" y="33" fill="#94a3b8" font-family="sans-serif" font-size="12">Selected 4 Active Campaigns &bull; Blended ROAS: <tspan fill="#10b981" font-weight="800">5.41x</tspan> &bull; Total Value: <tspan fill="#38bdf8" font-weight="800">$188,376.00</tspan></text>
    <rect x="640" y="14" width="132" height="28" rx="6" fill="#0081FB"/>
    <text x="662" y="32" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="700">Export Report &rarr;</text>
  </g>
</svg>'''

# 2. Google Search Console Dashboard (48.7K Organic Clicks Hockey Stick)
gsc_clicks_impressions = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 540" width="840" height="540">
  <defs>
    <linearGradient id="gscBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#090d16"/>
    </linearGradient>
    <linearGradient id="clickGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#4285F4" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#4285F4" stop-opacity="0.0"/>
    </linearGradient>
    <linearGradient id="imprGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#00ACC1" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#00ACC1" stop-opacity="0.0"/>
    </linearGradient>
  </defs>
  
  <rect width="840" height="540" rx="20" fill="url(#gscBg)" stroke="#1e293b" stroke-width="2"/>
  
  <!-- Header -->
  <rect x="0" y="0" width="840" height="56" fill="#131c2e" rx="20 20 0 0"/>
  <!-- Google colors icon -->
  <circle cx="28" cy="28" r="7" fill="#4285F4"/>
  <circle cx="46" cy="28" r="7" fill="#EA4335"/>
  <circle cx="64" cy="28" r="7" fill="#FBBC05"/>
  <circle cx="82" cy="28" r="7" fill="#34A853"/>
  <text x="104" y="34" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="700">Google Search Console</text>
  <text x="274" y="34" fill="#94a3b8" font-family="sans-serif" font-size="12">Performance on Search &bull; Type: Web &bull; Last 3 Months</text>
  
  <!-- Verified Badge -->
  <rect x="670" y="14" width="146" height="28" rx="14" fill="#10b981" opacity="0.15"/>
  <rect x="670" y="14" width="146" height="28" rx="14" fill="none" stroke="#10b981" stroke-width="1"/>
  <text x="686" y="32" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="700">&check; VERIFIED AUDIT</text>
  
  <!-- GSC 4 Scorecards -->
  <g transform="translate(24, 76)">
    <!-- Total Clicks -->
    <rect x="0" y="0" width="186" height="78" rx="10" fill="#1e3a8a" opacity="0.4" stroke="#3b82f6"/>
    <text x="16" y="24" fill="#93c5fd" font-family="sans-serif" font-size="11" font-weight="700">&squ; Total Clicks</text>
    <text x="16" y="56" fill="#ffffff" font-family="sans-serif" font-size="26" font-weight="800">48.7K</text>
    <text x="110" y="54" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="700">+35.6% &uarr;</text>
    
    <!-- Total Impressions -->
    <rect x="202" y="0" width="186" height="78" rx="10" fill="#134e4a" opacity="0.4" stroke="#00ACC1"/>
    <text x="218" y="24" fill="#5eead4" font-family="sans-serif" font-size="11" font-weight="700">&squ; Total Impressions</text>
    <text x="218" y="56" fill="#ffffff" font-family="sans-serif" font-size="26" font-weight="800">942.5K</text>
    <text x="328" y="54" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="700">+58% &uarr;</text>
    
    <!-- Average CTR -->
    <rect x="404" y="0" width="186" height="78" rx="10" fill="#162032" stroke="#334155"/>
    <text x="420" y="24" fill="#94a3b8" font-family="sans-serif" font-size="11" font-weight="600">&squ; Average CTR</text>
    <text x="420" y="56" fill="#ffffff" font-family="sans-serif" font-size="26" font-weight="800">5.2%</text>
    <text x="480" y="54" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="700">+1.4% &uarr;</text>
    
    <!-- Average Position -->
    <rect x="606" y="0" width="186" height="78" rx="10" fill="#162032" stroke="#334155"/>
    <text x="622" y="24" fill="#94a3b8" font-family="sans-serif" font-size="11" font-weight="600">&squ; Average Position</text>
    <text x="622" y="56" fill="#38bdf8" font-family="sans-serif" font-size="26" font-weight="800">8.4</text>
    <text x="672" y="54" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="700">1,248 Top 10</text>
  </g>
  
  <!-- Graph Container -->
  <g transform="translate(24, 174)">
    <rect x="0" y="0" width="792" height="230" fill="#111827" rx="12" stroke="#1e293b"/>
    
    <!-- Grid Lines -->
    <line x1="40" y1="40" x2="760" y2="40" stroke="#1f2937" stroke-dasharray="4"/>
    <line x1="40" y1="90" x2="760" y2="90" stroke="#1f2937" stroke-dasharray="4"/>
    <line x1="40" y1="140" x2="760" y2="140" stroke="#1f2937" stroke-dasharray="4"/>
    <line x1="40" y1="190" x2="760" y2="190" stroke="#1f2937"/>
    
    <!-- Left Y-Axis labels -->
    <text x="24" y="44" fill="#64748b" font-family="sans-serif" font-size="10">2.5K</text>
    <text x="24" y="94" fill="#64748b" font-family="sans-serif" font-size="10">1.5K</text>
    <text x="24" y="144" fill="#64748b" font-family="sans-serif" font-size="10">500</text>
    <text x="32" y="194" fill="#64748b" font-family="sans-serif" font-size="10">0</text>
    
    <!-- Impressions Area Gradient (Teal) -->
    <path d="M 50 170 Q 180 160, 300 135 T 520 85 T 660 45 T 760 30 L 760 190 L 50 190 Z" fill="url(#imprGrad)"/>
    <path d="M 50 170 Q 180 160, 300 135 T 520 85 T 660 45 T 760 30" fill="none" stroke="#00ACC1" stroke-width="2.5"/>
    
    <!-- Clicks Area Gradient (Blue - Hockey Stick) -->
    <path d="M 50 185 Q 200 182, 340 165 T 520 115 T 650 65 T 760 42 L 760 190 L 50 190 Z" fill="url(#clickGrad)"/>
    <path d="M 50 185 Q 200 182, 340 165 T 520 115 T 650 65 T 760 42" fill="none" stroke="#4285F4" stroke-width="3.5"/>
    
    <!-- Active Datapoint Pin -->
    <circle cx="760" cy="42" r="5" fill="#ffffff" stroke="#4285F4" stroke-width="3"/>
    
    <!-- Callout Box -->
    <g transform="translate(560, 25)">
      <rect x="0" y="0" width="170" height="58" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="1.5"/>
      <text x="12" y="18" fill="#cbd5e1" font-family="sans-serif" font-size="10">Daily Peak: 2,410 Clicks</text>
      <text x="12" y="34" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="700">+35.6% Organic Growth</text>
      <text x="12" y="48" fill="#94a3b8" font-family="sans-serif" font-size="9">Google AI Search &amp; Map Pack #1</text>
    </g>
  </g>
  
  <!-- Bottom Top Keywords Row -->
  <g transform="translate(24, 420)">
    <rect x="0" y="0" width="792" height="96" fill="#131c2e" rx="10" stroke="#1e293b"/>
    <text x="20" y="26" fill="#94a3b8" font-family="sans-serif" font-size="11" font-weight="700">TOP RANKING QUERIES (320 IN TOP 3)</text>
    
    <!-- Keyword 1 -->
    <rect x="20" y="38" width="175" height="42" rx="6" fill="#1e293b"/>
    <circle cx="34" cy="59" r="4" fill="#10b981"/>
    <text x="46" y="54" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="600">roof replacement cost</text>
    <text x="46" y="70" fill="#10b981" font-family="sans-serif" font-size="10">Position #1 &bull; 12.8K Clicks</text>
    
    <!-- Keyword 2 -->
    <rect x="210" y="38" width="175" height="42" rx="6" fill="#1e293b"/>
    <circle cx="224" cy="59" r="4" fill="#10b981"/>
    <text x="236" y="54" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="600">metal roof contractor</text>
    <text x="236" y="70" fill="#10b981" font-family="sans-serif" font-size="10">Position #1 &bull; 9.3K Clicks</text>
    
    <!-- Keyword 3 -->
    <rect x="400" y="38" width="175" height="42" rx="6" fill="#1e293b"/>
    <circle cx="414" cy="59" r="4" fill="#10b981"/>
    <text x="426" y="54" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="600">commercial roofing dallas</text>
    <text x="426" y="70" fill="#10b981" font-family="sans-serif" font-size="10">Position #1 &bull; 7.1K Clicks</text>
    
    <!-- Keyword 4 -->
    <rect x="590" y="38" width="180" height="42" rx="6" fill="#1e293b"/>
    <circle cx="604" cy="59" r="4" fill="#10b981"/>
    <text x="616" y="54" fill="#f8fafc" font-family="sans-serif" font-size="11" font-weight="600">hail damage inspection</text>
    <text x="616" y="70" fill="#10b981" font-family="sans-serif" font-size="10">Position #2 &bull; 5.2K Clicks</text>
  </g>
</svg>'''

# 3. Google Analytics 4 Realtime Dashboard (Live Users Active Now)
ga4_realtime_users = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 540" width="840" height="540">
  <defs>
    <linearGradient id="ga4Bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0c1322"/>
      <stop offset="100%" stop-color="#070a12"/>
    </linearGradient>
  </defs>
  <rect width="840" height="540" rx="20" fill="url(#ga4Bg)" stroke="#1e293b" stroke-width="2"/>
  
  <!-- GA4 Header -->
  <rect x="0" y="0" width="840" height="56" fill="#111c30" rx="20 20 0 0"/>
  <rect x="24" y="16" width="24" height="24" rx="6" fill="#F9AB00"/>
  <text x="32" y="33" fill="#ffffff" font-family="sans-serif" font-weight="900" font-size="14">G</text>
  <text x="56" y="33" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="700">Google Analytics 4</text>
  <text x="210" y="33" fill="#94a3b8" font-family="sans-serif" font-size="12">Realtime Overview &bull; All Users</text>
  
  <rect x="670" y="14" width="146" height="28" rx="14" fill="#10b981" opacity="0.2"/>
  <circle cx="686" cy="28" r="5" fill="#10b981">
    <animate attributeName="opacity" values="1;0.3;1" dur="1.8s" repeatCount="indefinite"/>
  </circle>
  <text x="698" y="32" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="700">REALTIME STREAM</text>
  
  <!-- Live Users Giant Card -->
  <g transform="translate(24, 76)">
    <rect x="0" y="0" width="340" height="230" fill="#132038" rx="14" stroke="#1e3a8a"/>
    <text x="24" y="34" fill="#93c5fd" font-family="sans-serif" font-size="12" font-weight="700" letter-spacing="0.5">USERS IN LAST 30 MINUTES</text>
    <text x="24" y="98" fill="#ffffff" font-family="sans-serif" font-size="64" font-weight="900">428</text>
    <circle cx="160" cy="80" r="7" fill="#10b981">
      <animate attributeName="r" values="6;10;6" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="180" y="85" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="700">Live Active</text>
    
    <!-- Per minute mini bar chart -->
    <g transform="translate(24, 130)">
      <text x="0" y="14" fill="#94a3b8" font-family="sans-serif" font-size="10">USERS PER MINUTE</text>
      <!-- 20 mini bars -->
      ''' + "".join([f'<rect x="{i*14}" y="{70 - min(60, int(20 + abs((i-10)*3.5) + (i*1.8)))}" width="8" height="{min(60, int(20 + abs((i-10)*3.5) + (i*1.8)))}" rx="2" fill="#3b82f6"/>' for i in range(21)]) + '''
    </g>
  </g>
  
  <!-- Traffic Channels Breakdown Card -->
  <g transform="translate(384, 76)">
    <rect x="0" y="0" width="432" height="230" fill="#132038" rx="14" stroke="#1e3a8a"/>
    <text x="24" y="32" fill="#cbd5e1" font-family="sans-serif" font-size="12" font-weight="700">TOP TRAFFIC SOURCES (ACTIVE NOW)</text>
    
    <!-- Channel 1: Organic Search -->
    <g transform="translate(24, 52)">
      <text x="0" y="16" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="600">1. Organic Search (Google / SEO)</text>
      <text x="320" y="16" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="700">236 users (55%)</text>
      <rect x="0" y="24" width="384" height="8" rx="4" fill="#1e293b"/>
      <rect x="0" y="24" width="211" height="8" rx="4" fill="#10b981"/>
    </g>
    
    <!-- Channel 2: Paid Social (Meta Ads) -->
    <g transform="translate(24, 98)">
      <text x="0" y="16" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="600">2. Paid Social (Facebook &amp; Instagram)</text>
      <text x="320" y="16" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="700">142 users (33%)</text>
      <rect x="0" y="24" width="384" height="8" rx="4" fill="#1e293b"/>
      <rect x="0" y="24" width="126" height="8" rx="4" fill="#0081FB"/>
    </g>
    
    <!-- Channel 3: Direct & Referral -->
    <g transform="translate(24, 144)">
      <text x="0" y="16" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="600">3. Direct / Bookmarks</text>
      <text x="320" y="16" fill="#a78bfa" font-family="sans-serif" font-size="12" font-weight="700">50 users (12%)</text>
      <rect x="0" y="24" width="384" height="8" rx="4" fill="#1e293b"/>
      <rect x="0" y="24" width="46" height="8" rx="4" fill="#8B5CF6"/>
    </g>
  </g>
  
  <!-- Active Geos & High-Converting Landing Pages -->
  <g transform="translate(24, 326)">
    <rect x="0" y="0" width="792" height="190" fill="#0f192c" rx="14" stroke="#1e293b"/>
    <text x="24" y="28" fill="#94a3b8" font-family="sans-serif" font-size="11" font-weight="700">REALTIME TOP HIGH-CONVERTING LANDING PAGES</text>
    
    <g transform="translate(24, 46)">
      <rect x="0" y="0" width="365" height="40" rx="6" fill="#17243b"/>
      <text x="14" y="24" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="600">/roof-replacement-pricing</text>
      <text x="280" y="24" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="800">118 active</text>
    </g>
    
    <g transform="translate(405, 46)">
      <rect x="0" y="0" width="365" height="40" rx="6" fill="#17243b"/>
      <text x="14" y="24" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="600">/commercial-contractor-quote</text>
      <text x="280" y="24" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="800">92 active</text>
    </g>
    
    <g transform="translate(24, 98)">
      <rect x="0" y="0" width="365" height="40" rx="6" fill="#17243b"/>
      <text x="14" y="24" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="600">/metal-roofing-dallas</text>
      <text x="280" y="24" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="800">76 active</text>
    </g>
    
    <g transform="translate(405, 98)">
      <rect x="0" y="0" width="365" height="40" rx="6" fill="#17243b"/>
      <text x="14" y="24" fill="#f8fafc" font-family="sans-serif" font-size="12" font-weight="600">/free-inspection-request</text>
      <text x="280" y="24" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="800">64 active</text>
    </g>
    
    <text x="24" y="164" fill="#64748b" font-family="sans-serif" font-size="11">Top Visitor Metros: Dallas-Fort Worth TX, Houston TX, Atlanta GA, Denver CO, Austin TX, Dubai UAE</text>
  </g>
</svg>'''

# 4. Before / After Google Algorithm Core Update Ranking Graph
gsc_before_after = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 540" width="840" height="540">
  <defs>
    <linearGradient id="surgeBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1324"/>
      <stop offset="100%" stop-color="#070b14"/>
    </linearGradient>
    <linearGradient id="surgeArea" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#10b981" stop-opacity="0.0"/>
    </linearGradient>
  </defs>
  <rect width="840" height="540" rx="20" fill="url(#surgeBg)" stroke="#1e293b" stroke-width="2"/>
  
  <!-- Header -->
  <rect x="0" y="0" width="840" height="56" fill="#111c30" rx="20 20 0 0"/>
  <circle cx="28" cy="28" r="6" fill="#10b981"/>
  <text x="44" y="33" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="700">Google Core Update Impact Analysis</text>
  <text x="320" y="33" fill="#94a3b8" font-family="sans-serif" font-size="12">Before vs After SEO Architecture Migration &bull; 6-Month Window</text>
  
  <rect x="680" y="14" width="136" height="28" rx="14" fill="#10b981" opacity="0.2"/>
  <text x="696" y="32" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="700">+540% SURGE &uarr;</text>
  
  <!-- Graph Canvas -->
  <g transform="translate(24, 76)">
    <rect x="0" y="0" width="792" height="340" fill="#0d1527" rx="14" stroke="#1e293b"/>
    
    <!-- Vertical Benchmark Marker: "Core Update Deployed" -->
    <line x1="320" y1="20" x2="320" y2="300" stroke="#f59e0b" stroke-width="2" stroke-dasharray="6"/>
    
    <g transform="translate(240, 30)">
      <rect x="0" y="0" width="160" height="28" rx="6" fill="#f59e0b" opacity="0.2"/>
      <rect x="0" y="0" width="160" height="28" rx="6" fill="none" stroke="#f59e0b" stroke-width="1"/>
      <text x="12" y="18" fill="#fbbf24" font-family="sans-serif" font-size="10" font-weight="700">&#9889; SEO OVERHAUL DEPLOYED</text>
    </g>
    
    <!-- Grid -->
    <line x1="50" y1="80" x2="750" y2="80" stroke="#1f2937" stroke-dasharray="4"/>
    <line x1="50" y1="150" x2="750" y2="150" stroke="#1f2937" stroke-dasharray="4"/>
    <line x1="50" y1="220" x2="750" y2="220" stroke="#1f2937" stroke-dasharray="4"/>
    <line x1="50" y1="280" x2="750" y2="280" stroke="#1f2937"/>
    
    <!-- Flatline Before Curve (Red/Grey) -->
    <path d="M 50 260 Q 150 258, 240 262 T 320 250" fill="none" stroke="#ef4444" stroke-width="3"/>
    <g transform="translate(70, 210)">
      <rect x="0" y="0" width="150" height="36" rx="6" fill="#1e293b" stroke="#ef4444" stroke-width="1"/>
      <text x="12" y="16" fill="#fca5a5" font-family="sans-serif" font-size="10" font-weight="700">BEFORE: FLATLINE</text>
      <text x="12" y="28" fill="#94a3b8" font-family="sans-serif" font-size="9">120 Clicks/mo &bull; Stagnant</text>
    </g>
    
    <!-- Surge After Curve (Emerald Hockey Stick) -->
    <path d="M 320 250 Q 420 180, 520 110 T 660 55 T 750 35 L 750 280 L 320 280 Z" fill="url(#surgeArea)"/>
    <path d="M 320 250 Q 420 180, 520 110 T 660 55 T 750 35" fill="none" stroke="#10b981" stroke-width="4"/>
    <circle cx="750" cy="35" r="6" fill="#ffffff" stroke="#10b981" stroke-width="3"/>
    
    <g transform="translate(560, 60)">
      <rect x="0" y="0" width="175" height="54" rx="8" fill="#132a22" stroke="#10b981" stroke-width="1.5"/>
      <text x="12" y="18" fill="#a7f3d0" font-family="sans-serif" font-size="11" font-weight="700">AFTER: 5.4X EXPONENTIAL</text>
      <text x="12" y="34" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="800">48,720 Monthly Visits</text>
      <text x="12" y="47" fill="#6ee7b7" font-family="sans-serif" font-size="9">Top 3 Rankings Across Metro</text>
    </g>
  </g>
  
  <!-- Bottom Metric Compare Cards -->
  <g transform="translate(24, 432)">
    <rect x="0" y="0" width="384" height="84" rx="10" fill="#1e1822" stroke="#7f1d1d"/>
    <text x="16" y="24" fill="#f87171" font-family="sans-serif" font-size="11" font-weight="700">LEGACY ARCHITECTURE (OLD SITE)</text>
    <text x="16" y="52" fill="#ffffff" font-family="sans-serif" font-size="20" font-weight="700">0.8% CTR &bull; Avg Pos: 44.2</text>
    <text x="16" y="70" fill="#94a3b8" font-family="sans-serif" font-size="10">High bounce rate, $0 commercial leads generated</text>
  </g>
  <g transform="translate(432, 432)">
    <rect x="0" y="0" width="384" height="84" rx="10" fill="#0d261e" stroke="#10b981"/>
    <text x="16" y="24" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="700">YOGESH PANWAR SEO RESTRUCTURE</text>
    <text x="16" y="52" fill="#ffffff" font-family="sans-serif" font-size="20" font-weight="800">5.2% CTR &bull; 1,248 Top 10 Keywords</text>
    <text x="16" y="70" fill="#a7f3d0" font-family="sans-serif" font-size="10">Dominating Google AI Overviews &amp; Local Pack</text>
  </g>
</svg>'''

# 5. Video Editing Timeline & Motion Creative Dashboard (Premiere / CapCut)
video_editing_timeline = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 540" width="840" height="540">
  <defs>
    <linearGradient id="vidBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#120c18"/>
      <stop offset="100%" stop-color="#09050e"/>
    </linearGradient>
  </defs>
  <rect width="840" height="540" rx="20" fill="url(#vidBg)" stroke="#2e1065" stroke-width="2"/>
  
  <!-- Header -->
  <rect x="0" y="0" width="840" height="56" fill="#1e1030" rx="20 20 0 0"/>
  <rect x="24" y="16" width="24" height="24" rx="6" fill="#9333ea"/>
  <text x="32" y="33" fill="#ffffff" font-family="sans-serif" font-weight="900" font-size="14">Pr</text>
  <text x="56" y="33" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="700">Direct-Response Video Engine &bull; 4K Motion Suite</text>
  <text x="440" y="33" fill="#c084fc" font-family="sans-serif" font-size="12">Sequence: High_ROAS_Hook_V3.mp4 &bull; 9:16 Vertical</text>
  
  <rect x="710" y="14" width="106" height="28" rx="14" fill="#a855f7" opacity="0.2"/>
  <text x="726" y="32" fill="#d8b4fe" font-family="sans-serif" font-size="11" font-weight="700">EXPORT 4K</text>
  
  <!-- Video Preview Split Screen -->
  <g transform="translate(24, 72)">
    <rect x="0" y="0" width="280" height="220" fill="#000000" rx="10" stroke="#3b0764"/>
    <!-- Simulated 9:16 Frame -->
    <rect x="70" y="10" width="140" height="200" rx="8" fill="#1e1b4b" stroke="#6366f1"/>
    <!-- Simulated Hook text -->
    <rect x="80" y="30" width="120" height="34" rx="4" fill="#fbbf24"/>
    <text x="86" y="46" fill="#000000" font-family="sans-serif" font-size="9" font-weight="900">STOP PAYING $300</text>
    <text x="86" y="58" fill="#000000" font-family="sans-serif" font-size="8" font-weight="900">FOR SHARED LEADS!</text>
    
    <!-- Dynamic Caption -->
    <text x="140" y="160" text-anchor="middle" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="900" stroke="#000" stroke-width="0.5">SCALE WITH DIRECT SEO</text>
    <circle cx="140" cy="110" r="16" fill="#ffffff" opacity="0.8"/>
    <polygon points="135,102 148,110 135,118" fill="#000000"/>
  </g>
  
  <!-- Retention & Hook Metrics Panel -->
  <g transform="translate(320, 72)">
    <rect x="0" y="0" width="496" height="220" fill="#170e24" rx="10" stroke="#3b0764"/>
    <text x="20" y="28" fill="#e9d5ff" font-family="sans-serif" font-size="12" font-weight="700">RETENTION &amp; HOOK RATE ANALYTICS</text>
    
    <g transform="translate(20, 46)">
      <rect x="0" y="0" width="140" height="60" rx="8" fill="#24143a"/>
      <text x="12" y="20" fill="#c084fc" font-family="sans-serif" font-size="10">3-SEC HOOK RATE</text>
      <text x="12" y="46" fill="#34d399" font-family="sans-serif" font-size="22" font-weight="800">78.4%</text>
    </g>
    
    <g transform="translate(170, 46)">
      <rect x="0" y="0" width="140" height="60" rx="8" fill="#24143a"/>
      <text x="12" y="20" fill="#c084fc" font-family="sans-serif" font-size="10">AVG WATCH TIME</text>
      <text x="12" y="46" fill="#38bdf8" font-family="sans-serif" font-size="22" font-weight="800">92.6%</text>
    </g>
    
    <g transform="translate(320, 46)">
      <rect x="0" y="0" width="156" height="60" rx="8" fill="#24143a"/>
      <text x="12" y="20" fill="#c084fc" font-family="sans-serif" font-size="10">TOTAL REEL VIEWS</text>
      <text x="12" y="46" fill="#ffffff" font-family="sans-serif" font-size="22" font-weight="800">3.2M+</text>
    </g>
    
    <!-- Retention Graph Line -->
    <path d="M 20 180 Q 80 140, 180 148 T 340 155 T 470 162" fill="none" stroke="#a855f7" stroke-width="3"/>
    <text x="20" y="202" fill="#94a3b8" font-family="sans-serif" font-size="10">&bull; Retention beats 94% of competing TikTok/Instagram ad creatives</text>
  </g>
  
  <!-- Multi-Track Editing Timeline -->
  <g transform="translate(24, 306)">
    <rect x="0" y="0" width="792" height="210" fill="#140b20" rx="12" stroke="#2e1065"/>
    
    <!-- Timeline Ruler -->
    <line x1="120" y1="28" x2="770" y2="28" stroke="#3b0764"/>
    <text x="130" y="20" fill="#64748b" font-family="sans-serif" font-size="10">00:00</text>
    <text x="280" y="20" fill="#64748b" font-family="sans-serif" font-size="10">00:05</text>
    <text x="440" y="20" fill="#64748b" font-family="sans-serif" font-size="10">00:15</text>
    <text x="600" y="20" fill="#64748b" font-family="sans-serif" font-size="10">00:30</text>
    <text x="740" y="20" fill="#64748b" font-family="sans-serif" font-size="10">00:45</text>
    
    <!-- Red Playhead Needle -->
    <line x1="380" y1="10" x2="380" y2="200" stroke="#ef4444" stroke-width="2"/>
    <polygon points="374,10 386,10 380,22" fill="#ef4444"/>
    
    <!-- Track V3: Text & Kinetic Typography -->
    <text x="16" y="58" fill="#a855f7" font-family="sans-serif" font-size="11" font-weight="700">V3 Motion Subtitles</text>
    <rect x="130" y="44" width="160" height="22" rx="4" fill="#fbbf24" opacity="0.8"/>
    <text x="140" y="59" fill="#000" font-family="sans-serif" font-size="10" font-weight="700">[Hook Headline]</text>
    <rect x="300" y="44" width="220" height="22" rx="4" fill="#fbbf24" opacity="0.8"/>
    <text x="310" y="59" fill="#000" font-family="sans-serif" font-size="10" font-weight="700">[Kinetic Captions &amp; Emojis]</text>
    <rect x="530" y="44" width="230" height="22" rx="4" fill="#10b981" opacity="0.8"/>
    <text x="540" y="59" fill="#000" font-family="sans-serif" font-size="10" font-weight="700">[Call To Action Overlay]</text>
    
    <!-- Track V2: B-Roll & Visual Proof Overlays -->
    <text x="16" y="96" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="700">V2 Proof B-Roll</text>
    <rect x="130" y="82" width="110" height="24" rx="4" fill="#0284c7"/>
    <rect x="250" y="82" width="190" height="24" rx="4" fill="#0284c7"/>
    <rect x="450" y="82" width="160" height="24" rx="4" fill="#0284c7"/>
    <rect x="620" y="82" width="140" height="24" rx="4" fill="#0284c7"/>
    
    <!-- Track V1: 4K Primary Footage -->
    <text x="16" y="136" fill="#ec4899" font-family="sans-serif" font-size="11" font-weight="700">V1 4K Master</text>
    <rect x="130" y="122" width="630" height="24" rx="4" fill="#be185d"/>
    
    <!-- Track A1: Clean Voiceover & Sound Design -->
    <text x="16" y="178" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="700">A1 SFX &amp; Music</text>
    <rect x="130" y="164" width="630" height="24" rx="4" fill="#065f46"/>
    <!-- Simulated Audio Waveform -->
    <path d="M 140 176 L 150 168 L 160 184 L 170 170 L 180 182 L 190 172 L 210 180 L 230 167 L 250 184 L 280 170 L 320 182 L 360 168 L 400 184 L 450 170 L 500 182 L 560 168 L 620 180 L 700 172 L 750 176" fill="none" stroke="#34d399" stroke-width="2"/>
  </g>
</svg>'''

# 6. Local SEO Google Map Pack 25/25 #1 Geogrid
local_seo_grid_rank = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 540" width="840" height="540">
  <defs>
    <linearGradient id="mapBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1716"/>
      <stop offset="100%" stop-color="#060e0d"/>
    </linearGradient>
  </defs>
  <rect width="840" height="540" rx="20" fill="url(#mapBg)" stroke="#115e59" stroke-width="2"/>
  
  <rect x="0" y="0" width="840" height="56" fill="#0f2926" rx="20 20 0 0"/>
  <circle cx="28" cy="28" r="7" fill="#10b981"/>
  <text x="46" y="33" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="700">Local Google 3-Pack Geogrid Dominance</text>
  <text x="350" y="33" fill="#99f6e4" font-family="sans-serif" font-size="12">Target: "Commercial Roofing Contractor" &bull; 15-Mile Metro Radius</text>
  
  <rect x="670" y="14" width="146" height="28" rx="14" fill="#10b981" opacity="0.25"/>
  <text x="686" y="32" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="800">100% #1 RANKED</text>
  
  <!-- Map Grid Container -->
  <g transform="translate(24, 76)">
    <rect x="0" y="0" width="480" height="430" fill="#081c19" rx="14" stroke="#134e4a"/>
    
    <!-- Roads/Map Vectors Background -->
    <path d="M 40 120 Q 180 90, 320 180 T 460 220" fill="none" stroke="#134e4a" stroke-width="4"/>
    <path d="M 80 40 Q 140 240, 260 380" fill="none" stroke="#134e4a" stroke-width="4"/>
    <path d="M 380 40 L 320 400" fill="none" stroke="#134e4a" stroke-width="3"/>
    <circle cx="240" cy="215" r="90" fill="#10b981" opacity="0.06"/>
    <circle cx="240" cy="215" r="160" fill="#10b981" opacity="0.03"/>
    
    <!-- 5x5 Matrix of #1 Emerald Pins covering entire city -->
    ''' + "".join([
      f'''<g transform="translate({60 + col*85}, {50 + row*80})">
        <circle cx="0" cy="0" r="18" fill="#10b981" stroke="#ffffff" stroke-width="2"/>
        <text x="0" y="5" text-anchor="middle" fill="#000000" font-family="sans-serif" font-size="13" font-weight="900">#1</text>
      </g>'''
      for row in range(5) for col in range(5)
    ]) + '''
  </g>
  
  <!-- Right Details & GMB Telemetry Panel -->
  <g transform="translate(524, 76)">
    <rect x="0" y="0" width="292" height="430" fill="#0a221e" rx="14" stroke="#134e4a"/>
    <text x="20" y="34" fill="#a7f3d0" font-family="sans-serif" font-size="13" font-weight="800">MAP PACK PERFORMANCE</text>
    
    <g transform="translate(20, 56)">
      <rect x="0" y="0" width="252" height="74" rx="8" fill="#113630"/>
      <text x="14" y="24" fill="#99f6e4" font-family="sans-serif" font-size="11">INBOUND PHONE CALLS</text>
      <text x="14" y="54" fill="#ffffff" font-family="sans-serif" font-size="24" font-weight="900">384 / mo</text>
      <text x="140" y="54" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="700">&uarr; +185%</text>
    </g>
    
    <g transform="translate(20, 142)">
      <rect x="0" y="0" width="252" height="74" rx="8" fill="#113630"/>
      <text x="14" y="24" fill="#99f6e4" font-family="sans-serif" font-size="11">GOOGLE MAP VIEWS</text>
      <text x="14" y="54" fill="#ffffff" font-family="sans-serif" font-size="24" font-weight="900">42,800</text>
      <text x="130" y="54" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="700">&uarr; Dominating</text>
    </g>
    
    <g transform="translate(20, 228)">
      <rect x="0" y="0" width="252" height="74" rx="8" fill="#113630"/>
      <text x="14" y="24" fill="#99f6e4" font-family="sans-serif" font-size="11">EXCLUSIVE REPLACEMENT LEADS</text>
      <text x="14" y="54" fill="#34d399" font-family="sans-serif" font-size="24" font-weight="900">94 Jobs</text>
      <text x="135" y="54" fill="#99f6e4" font-family="sans-serif" font-size="11">$0 Ad Spend</text>
    </g>
    
    <g transform="translate(20, 318)">
      <text x="0" y="20" fill="#94a3b8" font-family="sans-serif" font-size="11">&bull; Google Maps 3-Pack Lockout</text>
      <text x="0" y="40" fill="#94a3b8" font-family="sans-serif" font-size="11">&bull; Verified 5-Star Reviews Engine</text>
      <text x="0" y="60" fill="#94a3b8" font-family="sans-serif" font-size="11">&bull; 0 Shared Leads. 100% Inbound.</text>
      <text x="0" y="80" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="700">Audited by Yogesh Panwar</text>
    </g>
  </g>
</svg>'''

# 7. Meta Ads Dynamic Creative Testing Matrix
meta_creative_matrix = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 540" width="840" height="540">
  <defs>
    <linearGradient id="cmBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#090d16"/>
    </linearGradient>
  </defs>
  <rect width="840" height="540" rx="20" fill="url(#cmBg)" stroke="#1e293b" stroke-width="2"/>
  <rect x="0" y="0" width="840" height="56" fill="#131c2e" rx="20 20 0 0"/>
  <text x="24" y="33" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="700">Meta Creative Sandbox &bull; Winning Angle Matrix</text>
  <text x="380" y="33" fill="#94a3b8" font-family="sans-serif" font-size="12">Testing 24 Hook Variations Across High-Ticket Homeowners</text>
  
  <!-- 3 Creative Cards -->
  <g transform="translate(24, 80)">
    <!-- Creative 1: WINNER -->
    <rect x="0" y="0" width="248" height="420" rx="12" fill="#132338" stroke="#0081FB" stroke-width="2"/>
    <rect x="14" y="14" width="220" height="230" rx="8" fill="#1e293b"/>
    <rect x="24" y="24" width="90" height="24" rx="4" fill="#10b981"/>
    <text x="32" y="40" fill="#000000" font-family="sans-serif" font-size="10" font-weight="900">WINNER 6.4X</text>
    <text x="124" y="130" text-anchor="middle" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="800">UGC Hook Angle #1</text>
    <text x="124" y="150" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="11">"Insurance Paid For Full Roof"</text>
    <text x="16" y="275" fill="#f8fafc" font-family="sans-serif" font-size="13" font-weight="700">Video Ad: Customer Testimonial</text>
    <text x="16" y="295" fill="#10b981" font-family="sans-serif" font-size="16" font-weight="900">ROAS: 6.42x &bull; CPA: $19.40</text>
    <text x="16" y="320" fill="#94a3b8" font-family="sans-serif" font-size="11">Spend: $12,400 &bull; Revenue: $79,600</text>
    <rect x="16" y="360" width="216" height="36" rx="8" fill="#0081FB"/>
    <text x="76" y="382" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="700">Scale Budget &uarr;</text>
  </g>
  
  <g transform="translate(296, 80)">
    <!-- Creative 2 -->
    <rect x="0" y="0" width="248" height="420" rx="12" fill="#132338" stroke="#1e293b"/>
    <rect x="14" y="14" width="220" height="230" rx="8" fill="#1e293b"/>
    <rect x="24" y="24" width="90" height="24" rx="4" fill="#3b82f6"/>
    <text x="32" y="40" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="900">STRONG 5.1X</text>
    <text x="124" y="130" text-anchor="middle" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="800">Drone 4K Reveal</text>
    <text x="124" y="150" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="11">Standing Seam Metal Finished</text>
    <text x="16" y="275" fill="#f8fafc" font-family="sans-serif" font-size="13" font-weight="700">Video Ad: High-End Showcase</text>
    <text x="16" y="295" fill="#10b981" font-family="sans-serif" font-size="16" font-weight="900">ROAS: 5.14x &bull; CPA: $24.80</text>
    <text x="16" y="320" fill="#94a3b8" font-family="sans-serif" font-size="11">Spend: $8,200 &bull; Revenue: $42,148</text>
    <rect x="16" y="360" width="216" height="36" rx="8" fill="#1e293b" stroke="#3b82f6"/>
    <text x="82" y="382" fill="#93c5fd" font-family="sans-serif" font-size="11" font-weight="700">Active Retarget</text>
  </g>
  
  <g transform="translate(568, 80)">
    <!-- Creative 3 -->
    <rect x="0" y="0" width="248" height="420" rx="12" fill="#132338" stroke="#1e293b"/>
    <rect x="14" y="14" width="220" height="230" rx="8" fill="#1e293b"/>
    <rect x="24" y="24" width="90" height="24" rx="4" fill="#8b5cf6"/>
    <text x="32" y="40" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="900">SCALE 4.6X</text>
    <text x="124" y="130" text-anchor="middle" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="800">Interactive Quiz Funnel</text>
    <text x="124" y="150" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="11">"Calculate Replacement Cost"</text>
    <text x="16" y="275" fill="#f8fafc" font-family="sans-serif" font-size="13" font-weight="700">Lead Ad: Direct Instant Form</text>
    <text x="16" y="295" fill="#10b981" font-family="sans-serif" font-size="16" font-weight="900">ROAS: 4.62x &bull; CPA: $18.20</text>
    <text x="16" y="320" fill="#94a3b8" font-family="sans-serif" font-size="11">Spend: $9,400 &bull; Revenue: $43,428</text>
    <rect x="16" y="360" width="216" height="36" rx="8" fill="#1e293b" stroke="#8b5cf6"/>
    <text x="88" y="382" fill="#c4b5fd" font-family="sans-serif" font-size="11" font-weight="700">Broad CBO</text>
  </g>
</svg>'''

# 8. High-ROAS Growth Curve & Attribution
meta_roas_growth = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 540" width="840" height="540">
  <defs>
    <linearGradient id="roasBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a1220"/>
      <stop offset="100%" stop-color="#060b14"/>
    </linearGradient>
    <linearGradient id="roasArea" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#3b82f6" stop-opacity="0.0"/>
    </linearGradient>
  </defs>
  <rect width="840" height="540" rx="20" fill="url(#roasBg)" stroke="#1e293b" stroke-width="2"/>
  
  <rect x="0" y="0" width="840" height="56" fill="#10192e" rx="20 20 0 0"/>
  <circle cx="28" cy="28" r="6" fill="#3b82f6"/>
  <text x="44" y="33" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="700">Meta Ads High-ROAS Scaling Trajectory</text>
  <text x="340" y="33" fill="#94a3b8" font-family="sans-serif" font-size="12">Scaling from $5,000/mo to $65,000/mo Spend</text>
  
  <!-- Main Chart Area -->
  <g transform="translate(24, 76)">
    <rect x="0" y="0" width="792" height="340" fill="#0d1526" rx="14" stroke="#1e293b"/>
    
    <line x1="60" y1="60" x2="750" y2="60" stroke="#1f2937" stroke-dasharray="4"/>
    <line x1="60" y1="130" x2="750" y2="130" stroke="#1f2937" stroke-dasharray="4"/>
    <line x1="60" y1="200" x2="750" y2="200" stroke="#1f2937" stroke-dasharray="4"/>
    <line x1="60" y1="270" x2="750" y2="270" stroke="#1f2937"/>
    
    <text x="24" y="64" fill="#64748b" font-family="sans-serif" font-size="10">6.0x</text>
    <text x="24" y="134" fill="#64748b" font-family="sans-serif" font-size="10">4.5x</text>
    <text x="24" y="204" fill="#64748b" font-family="sans-serif" font-size="10">3.0x</text>
    <text x="24" y="274" fill="#64748b" font-family="sans-serif" font-size="10">1.0x</text>
    
    <!-- Spend Curve (Cyan) -->
    <path d="M 60 250 Q 220 240, 400 170 T 600 110 T 740 70" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="4"/>
    
    <!-- ROAS Area and Curve (Blue) -->
    <path d="M 60 210 Q 220 180, 400 130 T 600 80 T 740 50 L 740 270 L 60 270 Z" fill="url(#roasArea)"/>
    <path d="M 60 210 Q 220 180, 400 130 T 600 80 T 740 50" fill="none" stroke="#3b82f6" stroke-width="4"/>
    <circle cx="740" cy="50" r="6" fill="#ffffff" stroke="#3b82f6" stroke-width="3"/>
    
    <!-- Annotation -->
    <g transform="translate(540, 70)">
      <rect x="0" y="0" width="180" height="60" rx="8" fill="#1e293b" stroke="#3b82f6"/>
      <text x="12" y="20" fill="#93c5fd" font-family="sans-serif" font-size="10">Current Scale: $65,000 Spend</text>
      <text x="12" y="38" fill="#34d399" font-family="sans-serif" font-size="15" font-weight="900">5.41x Blended ROAS</text>
      <text x="12" y="52" fill="#e2e8f0" font-family="sans-serif" font-size="10">$351,650 Gross Revenue</text>
    </g>
  </g>
  
  <g transform="translate(24, 432)">
    <rect x="0" y="0" width="792" height="84" rx="10" fill="#10192e" stroke="#1e293b"/>
    <text x="24" y="32" fill="#94a3b8" font-family="sans-serif" font-size="12">Key Scaling Lever: <tspan fill="#ffffff" font-weight="700">Dynamic Video Creative Matrix + Server-Side CAPI (100% Signal Match Quality)</tspan></text>
    <text x="24" y="58" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="700">&bull; No Ad Fatigue &bull; Sub-$25 Customer Acquisition Cost &bull; Compounding Monthly Margin</text>
  </g>
</svg>'''

files = {
    "meta_ads_manager.svg": meta_ads_manager,
    "gsc_clicks_impressions.svg": gsc_clicks_impressions,
    "ga4_realtime_users.svg": ga4_realtime_users,
    "gsc_before_after.svg": gsc_before_after,
    "video_editing_timeline.svg": video_editing_timeline,
    "local_seo_grid_rank.svg": local_seo_grid_rank,
    "meta_creative_matrix.svg": meta_creative_matrix,
    "meta_roas_growth.svg": meta_roas_growth,
}

for filename, content in files.items():
    filepath = os.path.join(out_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated: {filename} ({len(content)} bytes)")
