---
permalink: /
title: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
  .about-page {
    --about-primary: #2563eb;
    --about-accent: #0f766e;
    --about-hover: #6d28d9;
    --about-work: #b45309;
    --about-author: var(--about-accent);
    --about-author-bg: #ecfdf5;
    --about-ink: #1f2937;
    --about-muted: #64748b;
    --about-surface: #f8fafc;
    --about-border: #dbeafe;
  }

  .about-page a {
    color: var(--about-primary);
    text-decoration: none;
  }

  .about-page a:hover {
    color: var(--about-hover);
    text-decoration: underline;
  }

  .about-hero {
    margin: 0 0 1.6rem;
    padding: 1.4rem 1.5rem;
    border: 1px solid var(--about-border);
    border-radius: 18px;
    background:
      radial-gradient(circle at top right, rgba(37, 99, 235, 0.12), transparent 32%),
      linear-gradient(135deg, #ffffff 0%, var(--about-surface) 100%);
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.06);
  }

  .about-eyebrow {
    margin: 0 0 0.6rem;
    color: var(--about-accent);
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .about-intro {
    margin-bottom: 0.85rem;
    color: var(--about-ink);
    font-size: 1.02rem;
    line-height: 1.72;
  }

  .about-intro:last-child {
    margin-bottom: 0;
  }

  .about-page a.person-name {
    color: var(--about-accent);
    font-weight: 700;
  }

  .about-page a.person-name:hover {
    color: #0b5f58;
  }

  .about-page a.org-link {
    color: var(--about-primary);
    font-weight: 700;
  }

  .about-page a.org-link:hover {
    color: #1d4ed8;
  }

  .about-page a.work-link {
    color: var(--about-work);
    font-weight: 700;
  }

  .about-page a.work-link:hover {
    color: #92400e;
  }

  .about-chip-row,
  .about-links {
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
    align-items: center;
  }

  .about-chip-row {
    margin-top: 1rem;
  }

  .about-chip {
    padding: 0.28rem 0.68rem;
    border: 1px solid #bfdbfe;
    border-radius: 999px;
    color: #1d4ed8;
    background: rgba(239, 246, 255, 0.9);
    font-size: 0.78rem;
    font-weight: 600;
  }

  .about-links {
    justify-content: center;
    margin: 1rem 0 1.4rem;
  }

  .about-links a {
    line-height: 0;
  }

  .about-section-note {
    color: #111827;
    line-height: 1.65;
  }

  .research-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(140px, 1fr));
    gap: 1rem;
    margin: 1rem 0 1.6rem;
  }

  .research-card {
    display: flex;
    min-height: 180px;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    background: #ffffff;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
    transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
  }

  .research-card:hover {
    border-color: #93c5fd;
    box-shadow: 0 16px 32px rgba(37, 99, 235, 0.14);
    transform: translateY(-3px);
  }

  .research-card img {
    width: 100%;
    height: 125px;
    object-fit: contain;
    padding: 0.75rem;
    background: linear-gradient(180deg, #f8fafc, #eef6ff);
  }

  .research-card-title {
    margin: 0;
    padding: 0.75rem 0.9rem 0.9rem;
    color: var(--about-ink);
    font-weight: 700;
    text-align: center;
  }

  .about-page h2 {
    margin-top: 1.9rem;
    color: #0f172a;
    border-bottom-color: #dbeafe;
  }

  .about-page .news {
    font-size: 0.82em;
  }

  .about-page .hoverTable {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0 0.35rem;
  }

  .about-page .hoverTable td {
    padding: 0.55rem 0.65rem;
    border: 0;
  }

  .about-page .hoverTable tr {
    background: #ffffff;
    transition: background 0.18s ease, box-shadow 0.18s ease;
  }

  .about-page .hoverTable tr:hover {
    background: #f8fbff;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06);
  }

  .about-page .publication-authors,
  .about-page .project-authors {
    color: #111827;
  }

  .about-page .publication-authors b,
  .about-page .publication-authors strong,
  .about-page .project-authors b,
  .about-page .project-authors strong {
    padding: 0.03rem 0.18rem;
    border-radius: 0.25rem;
    color: var(--about-author);
    background: var(--about-author-bg);
    font-weight: 800;
  }

  .about-page .venue-note {
    color: #b91c1c;
    font-weight: 800;
  }

  .highlight-soft {
    padding: 0.05rem 0.28rem;
    border-radius: 0.3rem;
    background: #fff7cc;
  }

  .visitor-map {
    margin-top: 0.8rem;
    padding: 0.8rem;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    background: #ffffff;
    text-align: left;
  }

  @media (max-width: 900px) {
    .research-grid {
      grid-template-columns: repeat(2, minmax(140px, 1fr));
    }
  }

  @media (max-width: 520px) {
    .about-hero {
      padding: 1.1rem;
    }

    .research-grid {
      grid-template-columns: 1fr;
    }
  }
</style>

<div class="about-page" markdown="1">

<section class="about-hero" markdown="1">
<!-- <p class="about-eyebrow">Research Engineer · Robotics & Embodied AI</p> -->

<p class="about-intro">
I am a research engineer working at the intersection of <strong>Robotics</strong> and <strong>Embodied AI</strong>. I graduated from <strong><a class="org-link" href="https://en.sjtu.edu.cn/">Shanghai Jiao Tong University</a> (上海交通大学, THE 43, QS 45, ARWU 46)</strong>, where I was advised by <strong><a class="person-name" href="https://sais.sjtu.edu.cn/faculty/zoudanping.html">Prof. Danping Zou</a></strong> and <strong><a class="person-name" href="https://english.seiee.sjtu.edu.cn/english/detail/842_811.htm">Prof. Wenxian Yu</a></strong> at <strong><a class="org-link" href="https://drone.sjtu.edu.cn/">SJTU-VISYS Lab</a></strong>.
</p>

<p class="about-intro">
I have also been fortunate to work with <strong><a class="person-name" href="https://people.csail.mit.edu/ganchuang/">Prof. Chuang Gan</a></strong> as a research intern at the <strong><a class="org-link" href="https://mitibmwatsonailab.mit.edu/">MIT-IBM Watson AI Lab</a></strong>, and with <strong><a class="person-name" href="https://mech.hku.hk/academic-staff/zhang-f/">Prof. Fu Zhang</a></strong> during <a class="org-link" href="https://gradsch.hku.hk/news_and_events/news_and_future_events/summer-research-programme-2023">SRP2023</a> at <strong><a class="org-link" href="https://github.com/hku-mars">HKU MaRS Lab</a></strong>. Previously, I spent productive and memorable time at <strong><a class="org-link" href="https://roboticsx.tencent.com/#/">Tencent Robotics X Lab</a></strong>, <strong><a class="org-link" href="https://www.shlab.org.cn/">Shanghai AI Lab</a></strong>, and <strong><a class="org-link" href="http://www.bdi.org.cn/">Shanghai Beidou Research Institute</a></strong>, working on robotics and intelligent systems.
</p>

<p class="about-intro">
My work has appeared in leading robotics and AI venues, including <strong>ICRA, IROS, RA-L, CVPR, TRO, TAES</strong>, and <strong>GPS Solutions</strong>. My research has been supported by the National Key R&D Program and the <a class="org-link" href="https://www.nsfc.gov.cn/english/site_1/index.html">NSFC</a>. Representative projects include <strong><a class="work-link" href="https://github.com/SJTU-ViSYS/M2DGR">M2DGR</a></strong>, <strong><a class="work-link" href="https://github.com/SJTU-ViSYS/Ground-Fusion">Ground-Fusion</a></strong>, <strong><a class="work-link" href="https://arxiv.org/abs/2407.11333">DAF</a></strong>, <strong><a class="work-link" href="https://github.com/sjtuyinjie/Ground-Fusion2">Ground-Fusion++ / M3DGR</a></strong>, <a class="work-link" href="https://github.com/Joanna-HE/LIGO.">LIGO</a>, <a class="work-link" href="https://github.com/DelinQu/EN-SLAM">EN-SLAM</a>, <a class="work-link" href="https://github.com/sjtuyinjie/Ground-Challenge">Ground-Challenge</a>, and <a class="work-link" href="https://github.com/SJTU-ViSYS/Sky-GVINS">Sky-GVINS</a>. I am also an active open-source contributor, with <strong>3k+ GitHub stars</strong> across my projects.
</p>

<div class="about-chip-row" aria-label="Research interests">
  <span class="about-chip">Reinforcement Learning</span>
  <span class="about-chip">Dexterous Manipulation</span>
  <span class="about-chip">Whole-Body Control</span>
  <span class="about-chip">Multi-modal Navigation</span>
</div>
</section>

<div class="about-links">
  <a href="https://scholar.google.com/citations?user=Y8LVRYIAAAAJ&hl=en" target="_blank">
    <img src="https://img.shields.io/badge/Google%20Scholar-blue?style=flat&logo=google-scholar&logoColor=white" alt="Google Scholar" />
  </a>
  <a href="https://github.com/sjtuyinjie/sjtuyinjie/blob/main/assets/wechat.jpg" target="_blank">
    <img src="https://img.shields.io/badge/Wechat-green?style=flat&logo=wechat&logoColor=white" alt="Wechat" />
  </a>
  <a href="mailto:robot_yinjie@outlook.com">
    <img src="https://img.shields.io/badge/-Email-c14438?style=flat&logo=Gmail&logoColor=white" alt="Email" />
  </a>
  <a href="https://github.com/sjtuyinjie" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white" alt="GitHub" />
  </a>
  <a href="https://github.com/sjtuyinjie" target="_blank">
    <img src="https://badges.strrl.dev/years/sjtuyinjie?style=flat-square&logo=github" alt="GitHub Years" />
  </a>
  <a href="https://github.com/sjtuyinjie?tab=repositories" target="_blank">
    <img src="https://badges.strrl.dev/repos/sjtuyinjie?style=flat-square&logo=github" alt="GitHub Repos" />
  </a>
</div>

## News
{% include news.html %}

## Selected Research

<div class="research-grid">
  <div class="research-card">
    <a href="https://github.com/SJTU-ViSYS/M2DGR" target="_blank">
      <img src="/gifs/m2dgr.gif" alt="M2DGR demo" loading="lazy" />
    </a>
    <p class="research-card-title"><a class="work-link" href="https://github.com/SJTU-ViSYS/M2DGR" target="_blank">M2DGR</a></p>
  </div>
  
  <div class="research-card">
    <a href="https://github.com/sjtuyinjie/Ground-Fusion2" target="_blank">
      <img src="/gifs/gf.gif" alt="Ground-Fusion demo" loading="lazy" />
    </a>
    <p class="research-card-title"><a class="work-link" href="https://github.com/sjtuyinjie/Ground-Fusion2" target="_blank">Ground-Fusion</a></p>
  </div>
  
  <div class="research-card">
    <a href="https://sites.google.com/view/disentangled-acoustic-fields/home" target="_blank">
      <img src="/gifs/daf.gif" alt="DAF demo" loading="lazy" />
    </a>
    <p class="research-card-title"><a class="work-link" href="https://sites.google.com/view/disentangled-acoustic-fields/home" target="_blank">DAF</a></p>
  </div>
  
  <div class="research-card">
    <a href="https://github.com/sjtuyinjie/M3DGR" target="_blank">
      <img src="/gifs/m3dgr.gif" alt="M3DGR demo" loading="lazy" />
    </a>
    <p class="research-card-title"><a class="work-link" href="https://github.com/sjtuyinjie/M3DGR" target="_blank">M3DGR</a></p>
  </div>
</div>

## Publication
<p class="about-section-note">
Currently, I focus on <strong>reinforcement learning</strong>, <strong>dexterous manipulation</strong>, and <strong>whole-body control</strong>. My long-term goal is to build practical intelligent robots that can operate safely and reliably in human environments, assisting people with everyday physical tasks. Previously, I worked on <strong>multi-sensor fusion SLAM algorithms and benchmarks under corner cases</strong> and <strong>multimodal navigation</strong>. Representative works are <span class="highlight-soft">highlighted</span>.
</p>

{% for post in site.publications reversed %} {% include publications.html %} {% endfor %}

## Projects
{% for post in site.projects reversed %} {% include projects.html %} {% endfor %}

## Academic Service
{% include service.html %}

## Honors
{% include honors.html %}

## Teaching
{% include teaching.html %}

## Map

<div class="visitor-map">
  <script type="text/javascript" id="clustrmaps" src="//clustrmaps.com/map_v2.js?d=vTCiAvCm0aG85BtQG8a4pBHf0ElbAyAwmz5KIj6EvrY&cl=2d78ad&w=600&t=tt"></script>
</div>

</div>
