"""Builds index.html, writing.html, work/processpro.html and 404.html from shared header/footer parts."""
import sys, html
ROOT=sys.argv[1]
SITE='https://www.shubhamnarang.in'
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">'

def head(title, desc, path, noindex=False):
    robots='<meta name="robots" content="noindex">\n' if noindex else ''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}<meta name="theme-color" content="#FFFFFF" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0E0F12" media="(prefers-color-scheme: dark)">
<link rel="canonical" href="{SITE}{path}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/images/portrait.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Shubham Narang">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/images/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{SITE}/images/og-image.jpg">
{FONTS}
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
'''

def header(cur):
    def a(href,label,key): return f'<a href="{href}"' + (' aria-current="page"' if cur==key else '') + f'>{label}</a>'
    return f'''<header class="site-head" id="head">
  <div class="wrap">
    <a class="name" href="/">Shubham Narang</a>
    <nav aria-label="Main">
      {a('/#work','Work','work')}
      {a('/writing','Writing','writing')}
      {a('/about','About','about')}
    </nav>
  </div>
</header>
'''

FOOT='''<footer class="site-foot" id="contact">
  <div class="wrap">
    <div class="mono">Contact</div>
    <h2>Got a problem worth seeing clearly?</h2>
    <div class="row">
      <button class="btn" type="button" id="copy" data-email="i.shubham25@gmail.com">i.shubham25@gmail.com</button>
      <a class="lnk" href="https://www.linkedin.com/in/shubhamnarang25" target="_blank" rel="noopener">LinkedIn ↗</a>
      <a class="lnk" href="https://github.com/inarang25" target="_blank" rel="noopener">GitHub ↗</a>
    </div>
    <div class="base"><span>© 2026 Shubham Narang · Chandigarh, India</span><span><a href="/">Work</a> · <a href="/writing">Writing</a> · <a href="/about">About</a></span></div>
  </div>
</footer>
<script>
(function(){
  var h=document.getElementById('head');
  function s(){ h.classList.toggle('scrolled', window.scrollY>8); } s(); window.addEventListener('scroll', s, {passive:true});
  var c=document.getElementById('copy'); if(!c) return;
  c.addEventListener('click', function(){
    var e=c.getAttribute('data-email');
    function done(){ c.textContent='Copied — talk soon'; setTimeout(function(){ c.textContent=e; }, 2200); }
    if(navigator.clipboard){ navigator.clipboard.writeText(e).then(done, function(){ location.href='mailto:'+e; }); } else { location.href='mailto:'+e; }
  });
})();
</script>
</body>
</html>
'''

def item(t, sub, d, m, msub='', href=None):
    inner=f'<span class="t">{t}'+(f'<small>{sub}</small>' if sub else '')+f'</span><span class="d">{d}</span><span class="m">{m}'+(f'<small>{msub}</small>' if msub else '')+'</span>'
    if href: return f'      <li><a class="item" href="{html.escape(href)}" target="_blank" rel="noopener">{inner}</a></li>'
    return f'      <li><div class="item">{inner}</div></li>'

PBI='https://app.powerbi.com/view?r='
enterprise=[
 ('Project Vihan','Mahindra Group · 2026 — now','Bringing ten business functions onto one data platform, with the C-suite dashboards read by the CEO every month and the CIO every week.','250+','KPIs being unified'),
 ('demand.ai','Mahindra Group · pilot','An ML engine that forecasts demand from market data, sentiment, rainfall and reservoir levels.','Pilot','in progress'),
 ('Process &amp; analytics transformation','IBM · 2022 — 2026','Celonis process mining and Power BI for Fortune 500 clients in manufacturing, retail fuel and aerospace.','15%','efficiency gains'),
 ('Defence programme delivery','Larsen &amp; Toubro · 2017 — 2019','Delivery of a defence programme with DRDO, and digitised procurement and supplier evaluation that cut operating cost by 10%.','₹50 Cr','programme delivered'),
]
studies=[
 ('Electronics demand forecast','Power BI','Finance, sales and supply-chain data in one model; a 26.8% forecast deviation surfaced.','Open ↗',PBI+'eyJrIjoiZjM3NjVlYjAtMjFkMi00MGFjLWExYjQtOTdkODg2MzY5OTEzIiwidCI6IjJlODViZWY5LWQ0OTktNGY1YS1hN2MxLWZkMGY0ZWNmYWVhNyJ9'),
 ('Hospitality revenue &amp; occupancy','Power BI','Revenue, occupancy and realisation by platform, category and season.','Open ↗',PBI+'eyJrIjoiYzY0NmY0Y2ItMTlhYS00NjhlLTg0MzgtMTNkNmVhNGU5OTczIiwidCI6IjJlODViZWY5LWQ0OTktNGY1YS1hN2MxLWZkMGY0ZWNmYWVhNyJ9'),
 ('SaaS subscription lifecycle','Power BI','892 users: active rate and resubscription, to inform retention.','Open ↗',PBI+'eyJrIjoiM2IxNjNkOTUtNTAyYS00Yjg0LTg1Y2UtNTVhM2Y3NWUxNGE3IiwidCI6IjJlODViZWY5LWQ0OTktNGY1YS1hN2MxLWZkMGY0ZWNmYWVhNyJ9'),
 ('British Airways reviews','Tableau','20,000+ customer reviews by aircraft type and geography.','Open ↗','https://public.tableau.com/views/BritishAirwaysReviewAnalysis_17263136404000/BritishAirwaysReview'),
 ('Indian EV market','Power BI','State-wise and OEM-wise sales and revenue.','Soon',None),
 ('FMCG service levels','Power BI','On-time, in-full and fill rate by city, customer and product.','Soon',None),
 ('Fuel retail sales &amp; inventory','Power BI','Revenue, litres and inventory across 20 stations.','Soon',None),
]
science=[
 ('Health insurance premium predictor','Python · Streamlit','A supervised model with a small app in front of it.','Try it ↗','https://inarang25-ml-project-premium-prediction.streamlit.app/'),
 ('Credit card target market','Python · pandas','Customer, credit and transaction analysis that found an untapped 18–25 segment.','Notebook ↗','https://github.com/inarang25/my-collab-notebooks/blob/main/EDA_%26_Target_Market_Identification.ipynb'),
 ('Credit card A/B test','Python · statistics','A test at 0.05 significance to validate the launch decision.','Notebook ↗','https://github.com/inarang25/my-collab-notebooks/blob/main/AB_Testing.ipynb'),
 ('eCommerce process mining','Celonis','Process mining on an eCommerce dataset to find operational bottlenecks.','Post ↗','https://www.linkedin.com/posts/shubhamnarang25_bigquery-sql-celonis-activity-7245681577702146048-G3sR'),
]

def ent_rows(): return '\n'.join(item(t,s,d,m,ms) for t,s,d,m,ms in enterprise)
def link_rows(L): return '\n'.join(item(t,s,d,m,'',href) if href else item(t,s,d,'',m) for t,s,d,m,href in L)

INDEX = head('Shubham Narang — data, AI and products','Shubham Narang — Digital Transformation Manager. Enterprise data and AI strategy, process mining, and products built end to end.','/') + header('work') + f'''
<main>

<section class="intro">
  <div class="wrap">
    <div class="who rise">
      <span class="av"><img src="/images/portrait-exec.webp" width="800" height="800" alt="Portrait of Shubham Narang"></span>
      <div><b>Shubham Narang</b><span>Digital Transformation Manager · Chandigarh, India</span></div>
    </div>
    <h1 class="rise d1">I help large organisations see themselves clearly through data <em>— and I build products of my own.</em></h1>
    <p class="rise d2">I lead enterprise data and AI work at Mahindra Group. Before that: process mining and analytics at IBM, and defence programme delivery at Larsen &amp; Toubro.</p>
    <div class="row rise d3">
      <a class="btn" href="#work">See the work</a>
      <a class="lnk" href="/about">About me →</a>
      <a class="lnk plain" href="https://www.linkedin.com/in/shubhamnarang25" target="_blank" rel="noopener">LinkedIn ↗</a>
    </div>
  </div>
</section>

<div class="wrap">
  <div class="figs" aria-label="Impact">
    <div><b>250+</b><span>KPIs being unified across ten business functions</span></div>
    <div><b>15%</b><span>efficiency gains for Fortune 500 clients at IBM</span></div>
    <div><b>₹50 Cr</b><span>defence programme delivered at L&amp;T</span></div>
    <div><b>10%</b><span>operating cost cut by digitising procurement</span></div>
  </div>
</div>

<div id="work">

<section class="sec">
  <div class="wrap">
    <div class="sec-head"><h2><span class="mono">01</span>Products</h2><p>Built, shipped and run on my own time.</p></div>

    <article class="feature">
      <div class="txt">
        <div class="mono">Process mining · Procurement</div>
        <h3>ProcessPro</h3>
        <p>Connects to an ERP, rebuilds every purchase order step by step, checks it against the ideal process, and shows where buying breaks the rules — and what it costs.</p>
        <div class="kpis">
          <div><b>₹102.2 Cr</b><span>spend analysed</span></div>
          <div><b>₹3.6 Cr</b><span>losses found</span></div>
          <div><b>13 / 14</b><span>planted mistakes caught</span></div>
        </div>
        <div class="row">
          <a class="btn" href="/work/processpro">Read the case study →</a>
          <a class="lnk" href="https://p2p-processpro.streamlit.app/" target="_blank" rel="noopener">Live app ↗</a>
        </div>
        <div class="note">Sample run on a fictional company. All data is synthetic.</div>
      </div>
      <a class="media" href="/work/processpro" aria-label="ProcessPro case study"><img src="/images/processpro/process_explorer.webp" width="1440" height="900" alt="ProcessPro process map of 1,208 purchase orders"></a>
    </article>

    <article class="feature">
      <div class="txt">
        <div class="mono">Consumer app · Baby care</div>
        <h3>nurchur.in</h3>
        <p>A baby-care tracker for feeding, growth, medicine and diapers. Prototyped on Lovable to move fast, then moved to a stack I own and run myself.</p>
        <div class="tags">React · Supabase · Vercel · Razorpay</div>
        <div class="row"><a class="btn ghost" href="https://nurchur.in" target="_blank" rel="noopener">Visit nurchur.in ↗</a></div>
      </div>
      <a class="media phones" href="https://nurchur.in" target="_blank" rel="noopener" aria-label="Visit nurchur.in">
        <img src="/images/tour/nurchur-1.webp" width="404" height="858" alt="nurchur.in home screen" loading="lazy">
        <img src="/images/tour/nurchur-2.webp" width="404" height="858" alt="nurchur.in feeding patterns" loading="lazy">
        <img src="/images/tour/nurchur-3.webp" width="404" height="858" alt="nurchur.in diaper mix and medicine timeline" loading="lazy">
      </a>
    </article>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head"><h2><span class="mono">02</span>Enterprise transformation</h2><p>Inside large organisations.</p></div>
    <ul class="list">
{ent_rows()}
    </ul>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head"><h2><span class="mono">03</span>Analytics studies</h2><p>Smaller dashboard studies, shared as I grow them.</p></div>
    <ul class="list compact">
{link_rows(studies)}
    </ul>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head"><h2><span class="mono">04</span>Data science &amp; experiments</h2><p>Models, tests and process mining.</p></div>
    <ul class="list compact">
{link_rows(science)}
    </ul>
  </div>
</section>

</div>

<section class="sec" id="writing">
  <div class="wrap">
    <div class="sec-head"><h2>Writing</h2><p>Notes on data, AI and building.</p></div>
    <div class="callout">
      <div><h3>The first essays are in preparation.</h3><p>On making data useful at the top of an organisation, and on building products alone.</p></div>
      <a class="btn ghost" href="/writing">Go to Writing →</a>
    </div>
  </div>
</section>

</main>
''' + FOOT

WRITING = head('Writing — Shubham Narang','Notes and essays by Shubham Narang on data, AI, process and building products.','/writing') + header('writing') + '''
<main>
<section class="page-head">
  <div class="wrap">
    <div class="mono rise">Writing</div>
    <h1 class="rise d1">Notes &amp; essays</h1>
    <p class="rise d2">On making data useful at the top of an organisation, on process, and on building products alone.</p>
  </div>
</section>
<section>
  <div class="wrap">
    <div class="callout">
      <div><h3>Nothing published yet.</h3><p>The first essays are being written. Email me and I'll send a note when they're up.</p></div>
      <a class="btn" href="mailto:i.shubham25@gmail.com?subject=Notify%20me%20when%20you%20publish">Notify me</a>
    </div>
    <ul class="list" style="margin-top:40px" aria-label="Planned topics">
      <li><div class="item"><span class="t">Why a process map can't see money</span><span class="d">What ProcessPro taught me about pairing process models with business rules.</span><span class="m"><small>Planned</small></span></div></li>
      <li><div class="item"><span class="t">One version of the truth</span><span class="d">What it takes to get ten functions to agree on a KPI.</span><span class="m"><small>Planned</small></span></div></li>
      <li><div class="item"><span class="t">Leaving the no-code tool</span><span class="d">Moving a live product onto a stack you own.</span><span class="m"><small>Planned</small></span></div></li>
    </ul>
  </div>
</section>
</main>
''' + FOOT

def shot(name, title, cap, alt):
    return f'<figure class="shot"><a href="/images/processpro/{name}.png" target="_blank" rel="noopener"><img src="/images/processpro/{name}.webp" width="1440" height="900" alt="{alt}" loading="lazy"></a><figcaption><b>{title}.</b> {cap}</figcaption></figure>'

PP = head('ProcessPro — case study · Shubham Narang','ProcessPro is a process-mining tool for procurement: it rebuilds every purchase order from the ERP, checks it against the ideal process, and shows where buying breaks the rules and what it costs.','/work/processpro') + header('work') + f'''
<main>

<section class="case-head">
  <div class="wrap">
    <a class="back" href="/#work">← All work</a>
    <div class="mono rise" style="margin-top:20px">Case study · Product · Purchase-to-pay, pharma manufacturing</div>
    <h1 class="rise d1">ProcessPro</h1>
    <p class="lede rise d2">Every order looked fine. The sequence told the truth. ProcessPro connects to an ERP, rebuilds every purchase order step by step, checks it against the ideal process, and shows where buying breaks the rules and what it costs.</p>
    <div class="row rise d3">
      <a class="btn" href="https://p2p-processpro.streamlit.app/" target="_blank" rel="noopener">Open the live app ↗</a>
      <a class="lnk" href="#findings">Jump to the findings</a>
    </div>
    <div class="banner"><i></i>Aravelle Formulations is a fictional company. All data is synthetic, generated for this project.</div>
  </div>
</section>

<div class="wrap">
  {shot('process_explorer','Process Explorer','The real process, mined from the event log. Dashed red lines are paths the ideal process does not allow.','ProcessPro process map: 1,208 cases, 122 variants, 77-day median cycle time')}
  <div class="figs" style="margin-top:40px" aria-label="Headline numbers">
    <div><b>₹102.2 Cr</b><span>spend analysed · 1,208 purchase orders, FY 2025–26</span></div>
    <div><b>7,899</b><span>events rebuilt from 23 ERP tables</span></div>
    <div><b>42%</b><span>of orders broke no business rule</span></div>
    <div><b>₹3.6 Cr</b><span>lost: paid twice, overcharged, overbilled</span></div>
  </div>
</div>

<div class="wrap">

<section class="part">
  <div class="mono">The problem</div>
  <div>
    <h2>Every company knows how its buying should work. Very few can see how it actually works.</h2>
    <p>A purchase order, a goods receipt, an invoice and a payment each look correct on their own. The problems hide in the order they happened in, in who did them, and in how far apart they were. That evidence is spread across thousands of ERP records that no one reads end to end.</p>
    <p>An invoice dated before the order existed. A batch released from quarantine by the storekeeper instead of Quality. A ₹15 lakh need split into two orders that each stay under the approval limit. None of these show up in a single document.</p>
    <p class="quote">Every document looked fine on its own. The problems only appear when you line them up in time.</p>
  </div>
</section>

<section class="part">
  <div class="mono">The company</div>
  <div>
    <h2>Aravelle Formulations, a fictional generic-medicines maker near Ahmedabad.</h2>
    <p>One GMP plant, 40 suppliers, 120 materials and 12 people across purchasing, stores, Quality and accounts. I configured the ERP like an implementation: approval at ₹10 lakh, goods into quarantine, Quality release before payment. Its ideal process has six steps.</p>
    <ol class="steps">
      <li><b>Request</b>A department records the need and owns the budget.</li>
      <li><b>Order</b>A buyer orders from an approved supplier at an agreed price.</li>
      <li><b>Approval</b>Orders of ₹10 lakh or more need the Purchase Head.</li>
      <li><b>Into quarantine</b>Goods arrive into a locked area. Nobody may use them yet.</li>
      <li><b>Quality release + invoice</b>The lab releases the batch. The invoice arrives in parallel.</li>
      <li><b>Payment</b>Only when the batch is released and the invoice is in.</li>
    </ol>
    <p style="margin-top:24px"><strong>What makes pharma different: Quality co-owns purchasing.</strong> Under Good Manufacturing Practice, only the Quality unit decides which supplier may supply which material, and when a batch may be used. Buying from an unapproved supplier or paying before release is a regulatory finding first and a cost problem second.</p>
  </div>
</section>

<section class="part">
  <div class="mono">The approach</div>
  <div>
    <h2>From raw ERP tables to a process, in five stages.</h2>
    <p>I built every layer myself, the way an implementation team and a process-mining team would split the work.</p>
    <ol class="steps">
      <li><b>Build the ERP</b>Approvals, receipt into quarantine, batches with expiry, payment terms and 12 role-based users.<small>Odoo 17 · PostgreSQL · Docker</small></li>
      <li><b>Run a year of buying</b>A planned year with 14 kinds of mistake planted at known rates, each written to an answer key.<small>Python</small></li>
      <li><b>Extract</b>SQL over 23 tables turns documents into an event log: case, step, time, person.<small>SQL · CSV · XES</small></li>
      <li><b>Check</b>An editable process model checks the order of steps. Fourteen business rules check amounts, roles, dates and quality data. Each finding is valued in rupees.<small>PM4Py · pandas</small></li>
      <li><b>Show</b>A six-page tool: overview, process explorer, conformance, issues, single order and the data behind every number.<small>Streamlit · Graphviz</small></li>
    </ol>
  </div>
</section>

<section class="part">
  <div class="mono">The product</div>
  <div>
    <h2>What ProcessPro looks like.</h2>
    <div class="grid2">
      {shot('overview','Overview','Headline KPIs and the main paths.','Purchase-to-pay overview with KPIs and main paths')}
      {shot('conformance_model','Conformance','Define the ideal process as a table; every order is replayed against it at once.','Editable ideal process model')}
      {shot('issues','Issues','Each problem in three sentences, the SAP setting that fixes it, and the orders behind it.','Issue page: same invoice paid twice, 29 orders, ₹83.4 lakh')}
      {shot('case','Case',"One order's timeline: who did what, and when.",'One purchase order timeline by role')}
    </div>
    <div style="margin-top:20px">{shot('data_reconciliation','Data','23 source tables with their SAP equivalents, and an eight-point reconciliation against the ERP.','Source tables and reconciliation')}</div>
  </div>
</section>

<section class="part" id="findings">
  <div class="mono">The findings</div>
  <div>
    <h2>₹102.2 crore spent. Only 42% of orders followed every rule.</h2>
    <p>76.5% of orders follow the ideal order of steps, across 122 distinct paths with a 77-day median cycle time. All amounts are before GST. The planted mistake rates are deliberately higher than a real company's, so every pattern appears within one year; the shape of the findings is what matters.</p>
    <div class="loss">
      <div><b class="big">₹3.6 Cr</b><span class="h">Money lost</span><dl>
        <div><dt>Billed for more than delivered</dt><dd>₹1.05 Cr</dd></div>
        <div><dt>Unrequested buying (estimated)</dt><dd>₹86 L</dd></div>
        <div><dt>Same invoice paid twice</dt><dd>₹83 L</dd></div>
        <div><dt>Charged above the agreed price</dt><dd>₹63 L</dd></div></dl></div>
      <div><b class="big">₹27.1 Cr</b><span class="h">Spend that skipped a check</span><dl>
        <div><dt>Large orders never approved</dt><dd>₹11.3 Cr</dd></div>
        <div><dt>Invoice booked before the goods</dt><dd>₹8.3 Cr</dd></div>
        <div><dt>Split, late-raised or changed orders</dt><dd>the rest</dd></div></dl></div>
      <div><b class="big">195</b><span class="h">Quality breaches on 176 orders</span><dl>
        <div><dt>Delivered close to expiry</dt><dd>68 orders</dd></div>
        <div><dt>Supplier Quality hadn't approved</dt><dd>45 orders</dd></div>
        <div><dt>Released by the store, not Quality</dt><dd>41 orders</dd></div></dl></div>
    </div>
  </div>
</section>

<section class="part">
  <div class="mono">What I learned</div>
  <div>
    <h2>Three insights from the build.</h2>
    <div class="cards">
      <div><b>A process map can't see money</b>A ₹69 lakh order with no approval follows a perfectly normal path. That is why ProcessPro pairs the process model with business rules: together they explain why 76.5% conform to the model but only 42% follow every rule.</div>
      <div><b>Exact-match controls fail on human typing</b>The ERP blocked 12 duplicate invoices and missed 17 that were retyped, <code>INV/25-26/0652</code> against <code>INV-25-26-0652</code>.</div>
      <div><b>Mistakes cascade</b>An invoice dated before its order starts the due-date clock early, so payment ends up late — with nobody planting it.</div>
      <div><b>Three fixes close most of it</b>Match the order and delivery before posting an invoice; hold payment on price or quantity differences; let Quality block unapproved suppliers and unreleased batches.</div>
    </div>
  </div>
</section>

<section class="part">
  <div class="mono">How I know it's right</div>
  <div>
    <h2>In a real company, accuracy means reconciliation.</h2>
    <p>Because the data is planted, I could grade every rule against the answer key, and check the tool's counts against the ERP itself.</p>
    <div class="figs" style="grid-template-columns:repeat(2,1fr)">
      <div><b>13 / 14</b><span>kinds of planted mistake found perfectly. Split orders, the one judgement call: 94%.</span></div>
      <div><b>8 / 8</b><span>counts reconcile with the ERP: orders, requests, approvals, receipts, releases, returns, invoices and payments.</span></div>
    </div>
  </div>
</section>

<section class="part">
  <div class="mono">For SAP readers</div>
  <div>
    <h2>Every object, mapped to SAP.</h2>
    <div class="scroll"><table class="map">
      <thead><tr><th>Step</th><th>In Odoo</th><th>In SAP</th></tr></thead>
      <tbody>
        <tr><td>Request</td><td>Purchase requisition (custom module)</td><td>EBAN</td></tr>
        <tr><td>Order</td><td>purchase_order / purchase_order_line</td><td>EKKO / EKPO</td></tr>
        <tr><td>Approval</td><td>Two-step approval, read from change history</td><td>Release strategy</td></tr>
        <tr><td>Quality release</td><td>Quarantine → Stock transfer</td><td>QM usage decision</td></tr>
        <tr><td>Invoice</td><td>Vendor bill</td><td>MIRO · RBKP</td></tr>
        <tr><td>Change history</td><td>mail_message / mail_tracking_value</td><td>CDHDR / CDPOS</td></tr>
      </tbody>
    </table></div>
  </div>
</section>

<section class="part">
  <div class="mono">What it shows</div>
  <div>
    <h2>Five things this project demonstrates.</h2>
    <div class="cards">
      <div><b>ERP implementation</b>Configured approvals, quarantine, batches and roles, and mapped every object to SAP.</div>
      <div><b>Pharma purchasing</b>Quality co-owns the process: approved suppliers per material, release before use, GMP.</div>
      <div><b>Process mining</b>Event-log design, discovery, conformance and reconciliation.</div>
      <div><b>Product</b>An interactive tool in a clean corporate style, built for walkthroughs.</div>
      <div><b>End-to-end ownership</b>From raw database tables to a live product.</div>
      <div><b>Stack</b>Odoo 17 Community · PostgreSQL · Docker · Python · pandas · PM4Py · Streamlit · Graphviz</div>
    </div>
    <div class="row" style="margin-top:28px">
      <a class="btn" href="https://p2p-processpro.streamlit.app/" target="_blank" rel="noopener">Open the live app ↗</a>
      <a class="lnk" href="/#work">← All work</a>
    </div>
  </div>
</section>

</div>
</main>
''' + FOOT

NF = head('Page not found — Shubham Narang','This page does not exist.','/404',noindex=True) + header('') + '''
<main>
<section class="page-head" style="padding-bottom:0">
  <div class="wrap">
    <div class="mono">404</div>
    <h1>This page doesn't exist — yet.</h1>
    <div class="row" style="margin-top:28px"><a class="btn" href="/">Go to Work</a><a class="lnk" href="/writing">Writing</a><a class="lnk" href="/about">About</a></div>
  </div>
</section>
</main>
''' + FOOT

for path,content in [('index.html',INDEX),('writing.html',WRITING),('work/processpro.html',PP),('404.html',NF)]:
    open(f'{ROOT}/{path}','w',encoding='utf-8').write(content)
    print(path,len(content))
