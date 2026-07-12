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
    overflow: visible;
  }

  .about-page a {
    color: var(--about-primary);
    text-decoration: none;
  }

  .about-page a:hover {
    color: var(--about-hover);
    text-decoration: underline;
  }

  .sidebar .author__name {
    text-align: center;
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
    overflow: visible;
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
    overflow: visible;
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
    justify-content: center;
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

  .research-themes {
    margin: 0.5rem 0 1.8rem;
  }

  .research-intro {
    margin: 0 0 1.25rem;
    color: var(--about-ink);
    font-size: 0.98rem;
    line-height: 1.72;
  }

  .themes-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
  }

  .theme-card {
    display: flex;
    flex-direction: column;
    overflow: hidden;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    background: #ffffff;
    box-shadow: 0 10px 24px rgba(15, 23, 42, 0.07);
    transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
  }

  .theme-card:hover {
    border-color: #93c5fd;
    box-shadow: 0 16px 32px rgba(37, 99, 235, 0.14);
    transform: translateY(-2px);
  }

  .theme-preview {
    position: relative;
    aspect-ratio: 16 / 9;
    overflow: hidden;
    background: linear-gradient(180deg, #f8fafc, #eef6ff);
  }

  .theme-slide {
    position: absolute;
    inset: 0;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.45s ease;
  }

  .theme-slide.active {
    opacity: 1;
    pointer-events: auto;
  }

  .theme-slide-intro-veil {
    display: none;
  }

  .theme-slide-media {
    position: absolute;
    inset: 0;
    z-index: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 1;
    transform: scale(1);
  }

  .theme-slide-media a {
    display: flex;
    width: 100%;
    height: 100%;
    align-items: center;
    justify-content: center;
  }

  .theme-slide img,
  .theme-slide video {
    width: 100%;
    height: 100%;
    object-fit: contain;
    padding: 0.65rem;
  }

  .theme-slide-title {
    position: absolute;
    z-index: 3;
    left: 50%;
    top: 50%;
    margin: 0;
    color: #ffffff;
    font-size: 1.62rem;
    font-weight: 800;
    letter-spacing: 0.06em;
    line-height: 1.2;
    opacity: 0;
    transform: translate(-50%, -50%);
    pointer-events: none;
    white-space: nowrap;
    -webkit-text-stroke: 2.5px #0f172a;
    paint-order: stroke fill;
    text-shadow:
      -1px 0 0 #0f172a,
      1px 0 0 #0f172a,
      0 -1px 0 #0f172a,
      0 1px 0 #0f172a,
      0 4px 16px rgba(15, 23, 42, 0.32);
  }

  .theme-slide-tag {
    position: absolute;
    z-index: 3;
    left: 0.65rem;
    bottom: 0.55rem;
    padding: 0.18rem 0.55rem;
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 999px;
    background: rgba(15, 23, 42, 0.88);
    color: #ffffff;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.02em;
    line-height: 1.2;
    opacity: 0;
    pointer-events: none;
    white-space: nowrap;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.18);
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);
  }

  .theme-slide.introducing .theme-slide-title {
    animation: theme-title-fade 1.6s ease forwards;
  }

  .theme-slide.introducing .theme-slide-tag {
    animation: theme-tag-fade 1.6s ease forwards;
  }

  .theme-slide:not(.introducing).active .theme-slide-title {
    opacity: 0;
  }

  .theme-slide:not(.introducing).active .theme-slide-tag {
    opacity: 1;
    transform: translateY(0);
  }

  @keyframes theme-title-fade {
    0% {
      opacity: 0;
      transform: translate(-50%, -50%) scale(0.98);
    }

    14% {
      opacity: 1;
      transform: translate(-50%, -50%) scale(1);
    }

    62% {
      opacity: 1;
      transform: translate(-50%, -50%) scale(1);
    }

    78% {
      opacity: 0;
      transform: translate(-50%, -50%) scale(1);
    }

    100% {
      opacity: 0;
    }
  }

  @keyframes theme-tag-fade {
    0%,
    64% {
      opacity: 0;
      transform: translateY(5px);
    }

    80% {
      opacity: 1;
      transform: translateY(0);
    }

    100% {
      opacity: 1;
      transform: translateY(0);
    }
  }

  .theme-slide-dots {
    position: absolute;
    left: 50%;
    bottom: 0.55rem;
    z-index: 4;
    display: flex;
    gap: 0.42rem;
    transform: translateX(-50%);
  }

  .theme-dot {
    width: 0.55rem;
    height: 0.55rem;
    padding: 0.3rem;
    border: 0;
    border-radius: 999px;
    background-color: rgba(148, 163, 184, 0.55);
    background-clip: content-box;
    box-sizing: content-box;
    cursor: pointer;
    transition: background-color 0.18s ease, transform 0.18s ease;
  }

  .theme-dot:hover {
    background-color: rgba(100, 116, 139, 0.75);
  }

  .theme-dot.active {
    background-color: var(--about-primary);
    transform: scale(1.12);
  }

  .theme-dot:focus-visible {
    outline: 2px solid rgba(37, 99, 235, 0.85);
    outline-offset: 2px;
  }

  .theme-body {
    padding: 1rem 1.05rem 1.1rem;
  }

  .theme-header {
    display: flex;
    align-items: center;
    gap: 0.55rem;
    margin-bottom: 0.45rem;
  }

  .theme-icon {
    display: inline-flex;
    width: 1.85rem;
    height: 1.85rem;
    align-items: center;
    justify-content: center;
    border-radius: 0.55rem;
    background: rgba(239, 246, 255, 0.95);
    color: var(--about-primary);
    font-size: 0.82rem;
  }

  .theme-card h3 {
    margin: 0;
    color: #0f172a;
    font-size: 1.02rem;
    font-weight: 700;
  }

  .theme-tagline {
    margin: 0 0 0.45rem;
    color: var(--about-accent);
    font-size: 0.9rem;
    font-weight: 600;
  }

  .theme-description {
    margin: 0 0 0.75rem;
    color: var(--about-muted);
    font-size: 0.84rem;
    line-height: 1.62;
  }

  .theme-papers {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
  }

  .theme-paper-tag {
    padding: 0.2rem 0.5rem;
    border-radius: 0.35rem;
    background: rgba(239, 246, 255, 0.95);
    color: #1d4ed8;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.01em;
    text-decoration: none;
    transition: background 0.18s ease, color 0.18s ease;
  }

  .theme-paper-tag:hover {
    background: var(--about-primary);
    color: #ffffff;
    text-decoration: none;
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

  .about-highlight-red {
    color: #dc2626;
    font-weight: 800;
  }

  .about-meta-note {
    position: absolute;
    bottom: calc(100% + 0.45rem);
    left: 50%;
    z-index: 20;
    display: block;
    width: max-content;
    max-width: none;
    padding: 0.3rem 0.55rem;
    border-radius: 0.35rem;
    margin-top: 0;
    background: rgba(15, 23, 42, 0.92);
    color: #ffffff;
    font-size: 0.78rem;
    line-height: 1.35;
    opacity: 0;
    pointer-events: none;
    transform: translateX(-50%) translateY(0.25rem);
    transition: opacity 0.15s ease, transform 0.15s ease, visibility 0.15s ease;
    visibility: hidden;
    white-space: nowrap;
    overflow: visible;
  }

  .metric-tooltip-wrap {
    position: relative;
    display: inline-block;
    cursor: help;
    overflow: visible;
  }

  .metric-tooltip-wrap:hover .about-meta-note,
  .metric-tooltip-wrap:focus-within .about-meta-note {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
    visibility: visible;
  }

  .floating-robot {
    position: fixed;
    left: 0;
    top: 0;
    z-index: 9999;
    pointer-events: none;
    font-size: 1.45rem;
    transform: translate(-50%, -50%);
    animation: robot-fly-up 1.15s ease-out forwards;
    will-change: transform, opacity;
  }

  @keyframes robot-fly-up {
    0% {
      opacity: 0;
      transform: translate(-50%, -20%) scale(0.78) rotate(-8deg);
    }

    12% {
      opacity: 1;
    }

    100% {
      opacity: 0;
      transform: translate(calc(-50% + var(--robot-drift, 0px)), -130px) scale(1.25) rotate(12deg);
    }
  }

  @media (max-width: 1100px) {
    .themes-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }
  }

  @media (max-width: 768px) {
    .themes-grid {
      grid-template-columns: 1fr;
    }
  }

  @media (max-width: 520px) {
    .about-hero {
      padding: 1.1rem;
    }
  }
</style>

<div class="about-page" markdown="1">

<section class="about-hero" markdown="1">
<!-- <p class="about-eyebrow">Research Engineer · Robotics & Embodied AI</p> -->

<p class="about-intro">
I am a passionate researcher and engineer working at the intersection of <strong>Robotics</strong> and <strong>Embodied AI</strong>. I graduated from <strong><a class="org-link" href="https://en.sjtu.edu.cn/">Shanghai Jiao Tong University</a> (ARWU30, QS 36, US News 37, THE 40)</strong>, where I was advised by <strong><a class="person-name" href="https://sais.sjtu.edu.cn/faculty/zoudanping.html">Prof. Danping Zou</a></strong> and <strong><a class="person-name" href="https://english.seiee.sjtu.edu.cn/english/detail/842_811.htm">Prof. Wenxian Yu</a></strong> at <strong><a class="org-link" href="https://drone.sjtu.edu.cn/">SJTU-VISYS Lab</a></strong>.
</p>

<p class="about-intro">
I have also been fortunate to work with <strong><a class="person-name" href="https://people.csail.mit.edu/ganchuang/">Prof. Chuang Gan</a></strong> as a research intern at the <strong><a class="org-link" href="https://mitibmwatsonailab.mit.edu/">MIT-IBM Watson AI Lab</a></strong>, and with <strong><a class="person-name" href="https://mech.hku.hk/academic-staff/zhang-f/">Prof. Fu Zhang</a></strong> during <a class="org-link" href="https://gradsch.hku.hk/news_and_events/news_and_future_events/summer-research-programme-2023">SRP2023</a> at <strong><a class="org-link" href="https://github.com/hku-mars">HKU MaRS Lab</a></strong>. Previously, I spent productive and memorable time at <strong><a class="org-link" href="https://roboticsx.tencent.com/#/">Tencent Robotics X Lab</a></strong>, <strong><a class="org-link" href="https://www.shlab.org.cn/">Shanghai AI Lab </a></strong><strong><a class="org-link" href="https://www.pjlab-ipec.com/">IPEC group</a></strong>, and <strong><a class="org-link" href="http://www.bdi.org.cn/">Shanghai Beidou Research Institute</a></strong>, working on robotics and intelligent systems.
</p>

<p class="about-intro">
My work has appeared in leading robotics and AI venues, including <strong>ICRA, IROS, RA-L, CVPR, TRO, TAES</strong>, and <strong>GPS Solutions</strong>. My research has been supported by the National Key R&D Program and the <a class="org-link" href="https://www.nsfc.gov.cn/english/site_1/index.html">NSFC</a>. Representative projects include <strong><a class="work-link" href="https://github.com/SJTU-ViSYS/M2DGR">M2DGR</a></strong>, <strong><a class="work-link" href="https://github.com/SJTU-ViSYS/Ground-Fusion">Ground-Fusion</a></strong>, <strong><a class="work-link" href="https://arxiv.org/abs/2407.11333">DAF</a></strong>, <strong><a class="work-link" href="https://github.com/sjtuyinjie/Ground-Fusion2">Ground-Fusion++ / M3DGR</a></strong> and so on, with <span class="metric-tooltip-wrap"><span id="scholar-citations" class="about-highlight-red"><strong>Google Scholar citations</strong></span><span id="scholar-last-updated" class="about-meta-note">loading latest citation count...</span></span>. I am also an active open-source contributor, with <span class="metric-tooltip-wrap"><span id="github-stars" class="about-highlight-red"><strong>GitHub stars</strong></span><span id="github-stars-last-updated" class="about-meta-note">loading latest GitHub stars...</span></span> across my projects.
</p>

<div class="about-chip-row" aria-label="Research interests">
  <span class="about-chip">Reinforcement Learning</span>
  <span class="about-chip">Dexterous Manipulation</span>
  <span class="about-chip">Whole-Body Control</span>
  <span class="about-chip">Multi-modal Reasoning</span>
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

## Research Themes

<div class="research-themes">

<p class="research-intro">Reliable localization and rich scene understanding are prerequisites for robots that operate in the real world. My research builds this foundation through <strong>multi-sensor fusion SLAM</strong>, <strong>multi-modal reasoning</strong>, and <strong>whole-body control</strong> — unifying LiDAR, vision, IMU, GNSS, audio, and reflectance cues for robust perception, and extending coordinated locomotion and manipulation for embodied autonomy under corner cases.</p>

<div class="themes-grid">

<div class="theme-card">
  <div class="theme-preview">
    <div class="theme-slide active" data-duration="20400">
      <div class="theme-slide-intro-veil" aria-hidden="true"></div>
      <div class="theme-slide-media">
        <a href="https://sjtuyinjie.github.io/ultrafusion-web/" target="_blank" rel="noopener noreferrer">
          <video muted playsinline preload="metadata" aria-label="Ultra-Fusion demo">
            <source src="/gifs/ultrafusion_corridor.mp4" type="video/mp4" />
          </video>
        </a>
      </div>
      <span class="theme-slide-title">Ultra-Fusion</span>
      <span class="theme-slide-tag">Ultra-Fusion</span>
    </div>
    <div class="theme-slide" data-duration="9620" data-playback-rate="2">
      <div class="theme-slide-intro-veil" aria-hidden="true"></div>
      <div class="theme-slide-media">
        <a href="https://github.com/SJTU-ViSYS/M2DGR" target="_blank" rel="noopener noreferrer">
          <video muted playsinline preload="metadata" aria-label="M2DGR demo">
            <source src="/gifs/m2dgr.mp4" type="video/mp4" />
          </video>
        </a>
      </div>
      <span class="theme-slide-title">M2DGR</span>
      <span class="theme-slide-tag">M2DGR</span>
    </div>
    <div class="theme-slide" data-duration="6800">
      <div class="theme-slide-intro-veil" aria-hidden="true"></div>
      <div class="theme-slide-media">
        <a href="https://github.com/SJTU-ViSYS/Ground-Fusion" target="_blank" rel="noopener noreferrer">
          <img src="/gifs/gf.gif" alt="Ground-Fusion demo" loading="lazy" />
        </a>
      </div>
      <span class="theme-slide-title">Ground-Fusion</span>
      <span class="theme-slide-tag">Ground-Fusion</span>
    </div>
    <div class="theme-slide" data-duration="9970" data-playback-rate="3">
      <div class="theme-slide-intro-veil" aria-hidden="true"></div>
      <div class="theme-slide-media">
        <a href="https://sjtuyinjie.github.io/M3DGR-website/" target="_blank" rel="noopener noreferrer">
          <video muted playsinline preload="metadata" aria-label="M3DGR demo">
            <source src="/gifs/m3dgr.mp4" type="video/mp4" />
          </video>
        </a>
      </div>
      <span class="theme-slide-title">M3DGR</span>
      <span class="theme-slide-tag">M3DGR</span>
    </div>
    <div class="theme-slide-dots">
      <button class="theme-dot active" data-index="0" type="button" aria-label="Show Ultra-Fusion"></button>
      <button class="theme-dot" data-index="1" type="button" aria-label="Show M2DGR"></button>
      <button class="theme-dot" data-index="2" type="button" aria-label="Show Ground-Fusion"></button>
      <button class="theme-dot" data-index="3" type="button" aria-label="Show M3DGR"></button>
    </div>
  </div>
  <div class="theme-body">
    <div class="theme-header">
      <div class="theme-icon"><i class="fa fa-map-marker" aria-hidden="true"></i></div>
      <h3>Multi-sensor Fusion SLAM</h3>
    </div>
    <p class="theme-tagline">Where is the robot?</p>
    <p class="theme-description">Tightly-coupled fusion frameworks and large-scale benchmarks that keep ground robots localized under sensor degradation, spatiotemporal perturbation, and challenging outdoor corner cases.</p>
    <div class="theme-papers">
      <a href="https://sjtuyinjie.github.io/ultrafusion-web/" target="_blank" rel="noopener noreferrer" class="theme-paper-tag">Ultra-Fusion</a>
      <a href="https://github.com/SJTU-ViSYS/Ground-Fusion" target="_blank" rel="noopener noreferrer" class="theme-paper-tag">Ground-Fusion</a>
      <a href="https://github.com/SJTU-ViSYS/M2DGR" target="_blank" rel="noopener noreferrer" class="theme-paper-tag">M2DGR</a>
      <a href="https://sjtuyinjie.github.io/M3DGR-website/" target="_blank" rel="noopener noreferrer" class="theme-paper-tag">M3DGR</a>
    </div>
  </div>
</div>

<div class="theme-card">
  <div class="theme-preview">
    <div class="theme-slide active" data-duration="6240">
      <div class="theme-slide-intro-veil" aria-hidden="true"></div>
      <div class="theme-slide-media">
        <a href="https://sites.google.com/view/disentangled-acoustic-fields/home" target="_blank" rel="noopener noreferrer">
          <img src="/gifs/daf.gif" alt="DAF demo" loading="lazy" />
        </a>
      </div>
      <span class="theme-slide-title">DAF</span>
      <span class="theme-slide-tag">DAF</span>
    </div>
    <div class="theme-slide" data-duration="21367">
      <div class="theme-slide-intro-veil" aria-hidden="true"></div>
      <div class="theme-slide-media">
        <a href="https://nidar-web.github.io/" target="_blank" rel="noopener noreferrer">
          <video muted playsinline preload="metadata" aria-label="NIDAR demo">
            <source src="/gifs/nidar.mp4" type="video/mp4" />
          </video>
        </a>
      </div>
      <span class="theme-slide-title">NIDAR</span>
      <span class="theme-slide-tag">NIDAR</span>
    </div>
    <div class="theme-slide-dots">
      <button class="theme-dot active" data-index="0" type="button" aria-label="Show DAF"></button>
      <button class="theme-dot" data-index="1" type="button" aria-label="Show NIDAR"></button>
    </div>
  </div>
  <div class="theme-body">
    <div class="theme-header">
      <div class="theme-icon"><i class="fa fa-compass" aria-hidden="true"></i></div>
      <h3>Multi-modal Reasoning</h3>
    </div>
    <p class="theme-tagline">How to reason across modalities?</p>
    <p class="theme-description">Multi-modal perception and navigation modules that unify vision, audio, and LiDAR reflectance for richer physical scene understanding, simulation-ready sensing, and downstream autonomy.</p>
    <div class="theme-papers">
      <a href="https://sites.google.com/view/disentangled-acoustic-fields/home" target="_blank" rel="noopener noreferrer" class="theme-paper-tag">DAF</a>
      <a href="https://nidar-web.github.io/" target="_blank" rel="noopener noreferrer" class="theme-paper-tag">NIDAR</a>
    </div>
  </div>
</div>

<div class="theme-card">
  <div class="theme-preview">
    <div class="theme-slide active" data-duration="4800">
      <div class="theme-slide-intro-veil" aria-hidden="true"></div>
      <div class="theme-slide-media">
        <a href="https://www.youtube.com/watch?v=WplE1GW5K3o" target="_blank" rel="noopener noreferrer">
          <img src="/gifs/idc.gif" alt="Mobile Manipulation demo" loading="lazy" />
        </a>
      </div>
      <span class="theme-slide-title">Mobile Manipulation</span>
      <span class="theme-slide-tag">Mobile Manipulation</span>
    </div>
    <div class="theme-slide-dots">
      <button class="theme-dot active" data-index="0" type="button" aria-label="Show Mobile Manipulation"></button>
    </div>
  </div>
  <div class="theme-body">
    <div class="theme-header">
      <div class="theme-icon"><i class="fa fa-robot" aria-hidden="true"></i></div>
      <h3>Whole-body Control</h3>
    </div>
    <p class="theme-tagline">How to manipulate on mobile robots?</p>
    <p class="theme-description">Coordinated whole-body control for mobile manipulators — coupling locomotion, balance, and dexterous interaction so robots can operate fluidly in human-centric environments.</p>
    <div class="theme-papers">
      <a href="https://www.youtube.com/watch?v=WplE1GW5K3o" target="_blank" rel="noopener noreferrer" class="theme-paper-tag">Mobile Manipulation</a>
    </div>
  </div>
</div>

</div>
</div>

<script>
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.theme-preview').forEach(function (preview) {
      var slides = preview.querySelectorAll('.theme-slide');
      var dots = preview.querySelectorAll('.theme-dot');
      var current = 0;
      var timer = null;
      var introTimer = null;
      var videoEndHandler = null;
      var AUTO_INTERVAL = 10000;
      var INTRO_DURATION = 1600;

      function clearAdvanceTimer() {
        if (timer) {
          clearTimeout(timer);
          timer = null;
        }
        if (introTimer) {
          clearTimeout(introTimer);
          introTimer = null;
        }
      }

      function clearSlideState(slide) {
        if (!slide) {
          return;
        }
        clearVideoEndHandler(slide);
        slide.classList.remove('introducing', 'playing');
        var video = slide.querySelector('video');
        if (video) {
          video.pause();
          video.currentTime = 0;
        }
        var label = slide.querySelector('.theme-slide-title');
        var tag = slide.querySelector('.theme-slide-tag');
        if (label) {
          label.style.animation = 'none';
        }
        if (tag) {
          tag.style.animation = 'none';
        }
      }

      function clearVideoEndHandler(slide) {
        var video = slide.querySelector('video');
        if (video && videoEndHandler) {
          video.removeEventListener('ended', videoEndHandler);
          videoEndHandler = null;
        }
      }

      function resetSlideMedia(slide) {
        clearSlideState(slide);
      }

      function slideDuration(slide) {
        return parseInt(slide.dataset.duration, 10) || 5000;
      }

      function slidePlaybackRate(slide) {
        return parseFloat(slide.dataset.playbackRate) || 1;
      }

      function prepareVideoPlayback(video, slide) {
        video.playbackRate = slidePlaybackRate(slide);
        video.currentTime = 0;
      }

      function restartGif(img) {
        var src = img.getAttribute('src').split('?')[0];
        img.src = src + '?cycle=' + Date.now();
      }

      function restartLabelAnimation(slide) {
        var title = slide.querySelector('.theme-slide-title');
        var tag = slide.querySelector('.theme-slide-tag');

        [title, tag].forEach(function (node) {
          if (!node) {
            return;
          }
          node.style.animation = 'none';
          void node.offsetWidth;
          node.style.animation = '';
        });
      }

      function startSlideMedia(slide) {
        var video = slide.querySelector('video');
        var img = slide.querySelector('img');

        if (video) {
          prepareVideoPlayback(video, slide);
          var playPromise = video.play();
          if (playPromise && typeof playPromise.catch === 'function') {
            playPromise.catch(function () {});
          }
          return;
        }

        if (img) {
          restartGif(img);
        }
      }

      function scheduleAfterFullPlayback(slide, onDone) {
        var video = slide.querySelector('video');

        if (video) {
          videoEndHandler = function () {
            clearVideoEndHandler(slide);
            onDone();
          };
          video.addEventListener('ended', videoEndHandler);
          prepareVideoPlayback(video, slide);
          var playPromise = video.play();
          if (playPromise && typeof playPromise.catch === 'function') {
            playPromise.catch(function () {
              timer = setTimeout(onDone, slideDuration(slide));
            });
          }
          return;
        }

        var img = slide.querySelector('img');
        if (img) {
          restartGif(img);
          timer = setTimeout(onDone, slideDuration(slide));
        }
      }

      function runSlideIntro(slide, fromManualNav, onAdvance) {
        restartLabelAnimation(slide);
        slide.classList.add('introducing');
        startSlideMedia(slide);

        introTimer = setTimeout(function () {
          slide.classList.remove('introducing');
        }, INTRO_DURATION);

        if (fromManualNav) {
          scheduleAfterFullPlayback(slide, onAdvance);
          return;
        }

        timer = setTimeout(onAdvance, AUTO_INTERVAL);
      }

      function showSlide(index, fromManualNav) {
        clearAdvanceTimer();
        clearSlideState(slides[current]);
        slides[current].classList.remove('active');
        dots[current].classList.remove('active');
        current = ((index % slides.length) + slides.length) % slides.length;
        slides[current].classList.add('active');
        dots[current].classList.add('active');

        runSlideIntro(slides[current], fromManualNav, function () {
          showSlide(current + 1, false);
        });
      }

      dots.forEach(function (dot) {
        dot.addEventListener('click', function (event) {
          event.preventDefault();
          showSlide(parseInt(this.dataset.index, 10), true);
        });
      });

      showSlide(0, false);
    });
  });
</script>

## Publication
<p class="about-section-note">
Currently, I focus on <strong>reinforcement learning</strong>, <strong>dexterous manipulation</strong>, and <strong>whole-body control</strong>. My long-term goal is to build practical intelligent robots that can operate safely and reliably in human environments, assisting people with everyday physical tasks. Previously, I worked on <strong>multi-sensor fusion SLAM</strong>(algorithms and benchmarks) and <strong>multi-modal reasoning</strong>. Representative works are <span class="highlight-soft">highlighted</span>.
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

<script>
  (function () {
    var ignoredSelector = 'a, button, input, textarea, select, label, img, iframe, video, audio, canvas, svg, .clickable-gif';
    var scholarUrl = 'https://scholar.google.com/citations?user=Y8LVRYIAAAAJ&hl=en';
    var citationNode = document.getElementById('scholar-citations');
    var updatedNode = document.getElementById('scholar-last-updated');
    var githubStarsNode = document.getElementById('github-stars');
    var githubStarsUpdatedNode = document.getElementById('github-stars-last-updated');
    var featuredGithubRepos = [
      'SJTU-ViSYS/M2DGR',
      'SJTU-ViSYS/Ground-Fusion',
      'SJTU-ViSYS/M2DGR-plus',
      'SJTU-ViSYS/Sky-GVINS'
    ];
    var scholarCacheKey = 'aboutScholarCitations';
    var githubStarsCacheKey = 'aboutGithubStars';
    var scholarMetricRendered = false;
    var githubMetricRendered = false;
    var sharedScholarFallback = {
      value: Number('{{ site.data.scholar_stats.citations | default: 0 }}'),
      updatedAt: '{{ site.data.scholar_stats.updated_at | default: "" }}'
    };
    var sharedGithubFallback = {
      value: Number('{{ site.data.github_stars.stars | default: 0 }}'),
      updatedAt: '{{ site.data.github_stars.updated_at | default: "" }}'
    };
    var nowString = function () {
      var d = new Date();
      var pad = function (n) {
        return String(n).padStart(2, '0');
      };
      return d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate()) + ' ' + pad(d.getHours()) + ':' + pad(d.getMinutes());
    };
    var formatNumber = function (value) {
      return value.toLocaleString('en-US');
    };
    var readMetricCache = function (key) {
      try {
        var cached = localStorage.getItem(key);
        return cached ? JSON.parse(cached) : null;
      } catch (err) {
        return null;
      }
    };
    var writeMetricCache = function (key, value) {
      var cache = {
        value: value,
        updatedAt: nowString()
      };

      try {
        localStorage.setItem(key, JSON.stringify(cache));
      } catch (err) {
        return cache;
      }

      return cache;
    };
    var renderMetricUpdate = function (node, updatedNode, value, label, cache) {
      if (node) {
        node.innerHTML = '<strong>' + formatNumber(value) + ' ' + label + '</strong>';
      }
      if (node === citationNode) {
        scholarMetricRendered = true;
      }
      if (node === githubStarsNode) {
        githubMetricRendered = true;
      }
      if (updatedNode && cache && cache.updatedAt) {
        updatedNode.textContent = 'last update: ' + cache.updatedAt;
      }
    };
    var parseScholarCitations = function (text) {
      var htmlPatterns = [
        /class="gsc_rsb_std">([\d,]+)<\/td>/,
        /<td[^>]*>\s*Citations\s*<\/td>\s*<td[^>]*>\s*([\d,]+)\s*<\/td>/i
      ];
      var markdownPatterns = [
        /Citations[\s\S]*?\n\s*([\d,]+)/i,
        /Citations\s+([\d,]+)/i
      ];
      var patterns = htmlPatterns.concat(markdownPatterns);
      var match = null;

      for (var i = 0; i < patterns.length; i += 1) {
        match = text.match(patterns[i]);
        if (match) {
          break;
        }
      }

      if (!match) {
        return null;
      }

      var numeric = Number(match[1].replace(/,/g, ''));
      return Number.isFinite(numeric) ? numeric : null;
    };
    var fetchTextWithRetries = function (url, retries) {
      var attemptsLeft = typeof retries === 'number' ? retries : 2;

      return fetch(url, { method: 'GET' }).then(function (resp) {
        if (!resp.ok) {
          throw new Error('bad response');
        }
        return resp.text();
      }).catch(function (err) {
        if (attemptsLeft <= 0) {
          throw err;
        }
        return fetchTextWithRetries(url, attemptsLeft - 1);
      });
    };
    var updateScholarOnVisit = function () {
      if (!citationNode) {
        return;
      }

      var cachedScholar = readMetricCache(scholarCacheKey);
      if (cachedScholar && Number.isFinite(cachedScholar.value)) {
        renderMetricUpdate(citationNode, updatedNode, cachedScholar.value, 'Google Scholar citations', cachedScholar);
      }

      setTimeout(function () {
        if (!scholarMetricRendered && Number.isFinite(sharedScholarFallback.value) && sharedScholarFallback.value > 0) {
          renderMetricUpdate(citationNode, updatedNode, sharedScholarFallback.value, 'Google Scholar citations', {
            updatedAt: sharedScholarFallback.updatedAt || 'shared fallback'
          });
        }
      }, 3000);

      var proxies = [
        scholarUrl,
        'https://api.allorigins.win/raw?url=' + encodeURIComponent(scholarUrl),
        'https://r.jina.ai/http://scholar.google.com/citations?user=Y8LVRYIAAAAJ&hl=en'
      ];

      var tryFetch = function (idx) {
        if (idx >= proxies.length) {
          return Promise.resolve(null);
        }

        return fetchTextWithRetries(proxies[idx], 2)
          .then(function (text) {
            var citations = parseScholarCitations(text);
            if (citations === null) {
              throw new Error('parse failed');
            }
            return citations;
          })
          .catch(function () {
            return tryFetch(idx + 1);
          });
      };

      tryFetch(0).then(function (citations) {
        if (citations === null) {
          return;
        }
        renderMetricUpdate(citationNode, updatedNode, citations, 'Google Scholar citations', writeMetricCache(scholarCacheKey, citations));
      });
    };

    var fetchGithubJsonDirect = function (url) {
      return fetch(url, {
        method: 'GET',
        headers: {
          Accept: 'application/vnd.github+json'
        }
      }).then(function (resp) {
        if (!resp.ok) {
          throw new Error('bad response');
        }
        return resp.json();
      });
    };
    var fetchGithubJsonViaProxy = function (url) {
      return fetch('https://api.allorigins.win/raw?url=' + encodeURIComponent(url), {
        method: 'GET'
      }).then(function (resp) {
        if (!resp.ok) {
          throw new Error('bad response');
        }
        return resp.json();
      });
    };
    var fetchGithubJsonFromJina = function (url) {
      return fetch('https://r.jina.ai/http://' + url.replace(/^https?:\/\//, ''), {
        method: 'GET'
      }).then(function (resp) {
        if (!resp.ok) {
          throw new Error('bad response');
        }
        return resp.text();
      }).then(function (text) {
        return JSON.parse(text);
      });
    };
    var fetchGithubJson = function (url, retries) {
      var attemptsLeft = typeof retries === 'number' ? retries : 2;

      return fetchGithubJsonDirect(url).catch(function (err) {
        if (attemptsLeft <= 0) {
          return fetchGithubJsonViaProxy(url).catch(function () {
            return fetchGithubJsonFromJina(url);
          });
        }

        return fetchGithubJson(url, attemptsLeft - 1);
      });
    };
    var fetchUserRepoStarsFromReposApi = function (type, page, total) {
      return fetchGithubJson('https://api.github.com/users/sjtuyinjie/repos?type=' + type + '&per_page=100&page=' + page)
        .then(function (repos) {
          var pageTotal = repos.reduce(function (sum, repo) {
            return sum + (repo.stargazers_count || 0);
          }, total);

          if (repos.length === 100) {
            return fetchUserRepoStarsFromReposApi(type, page + 1, pageTotal);
          }

          return pageTotal;
        });
    };
    var fetchUserRepoStarsFromSearchApi = function (page, total) {
      return fetchGithubJson('https://api.github.com/search/repositories?q=user:sjtuyinjie+fork:true&per_page=100&page=' + page)
        .then(function (result) {
          var repos = result.items || [];
          var pageTotal = repos.reduce(function (sum, repo) {
            return sum + (repo.stargazers_count || 0);
          }, total);

          if (repos.length === 100 && page < 10) {
            return fetchUserRepoStarsFromSearchApi(page + 1, pageTotal);
          }

          return pageTotal;
        });
    };
    var fetchUserRepoStars = function () {
      var methods = [
        function () { return fetchUserRepoStarsFromReposApi('owner', 1, 0); },
        function () { return fetchUserRepoStarsFromReposApi('all', 1, 0); },
        function () { return fetchUserRepoStarsFromSearchApi(1, 0); }
      ];
      var tryMethod = function (idx) {
        if (idx >= methods.length) {
          return Promise.reject(new Error('all user star methods failed'));
        }

        return methods[idx]().catch(function () {
          return tryMethod(idx + 1);
        });
      };

      return tryMethod(0);
    };
    var fetchRepoStars = function (fullName) {
      return fetchGithubJson('https://api.github.com/repos/' + fullName)
        .then(function (repo) {
          return repo.stargazers_count || 0;
        });
    };
    var fetchRepoStarsWithFallback = function (fullName) {
      return fetchRepoStars(fullName).catch(function () {
        return fetchTextWithRetries('https://r.jina.ai/http://github.com/' + fullName, 1)
          .then(function (text) {
            var match = text.match(/([\d,.]+[kK]?)\s+stars/i);
            if (!match) {
              throw new Error('repo star parse failed');
            }
            var raw = match[1].replace(/,/g, '');
            var multiplier = /k$/i.test(raw) ? 1000 : 1;
            var numeric = Number(raw.replace(/k$/i, '')) * multiplier;
            if (!Number.isFinite(numeric)) {
              throw new Error('repo star parse failed');
            }
            return Math.round(numeric);
          });
      });
    };
    var updateGithubStarsOnVisit = function () {
      if (!githubStarsNode) {
        return;
      }

      var cachedGithubStars = readMetricCache(githubStarsCacheKey);
      if (cachedGithubStars && Number.isFinite(cachedGithubStars.value)) {
        renderMetricUpdate(githubStarsNode, githubStarsUpdatedNode, cachedGithubStars.value, 'GitHub stars', cachedGithubStars);
      }

      setTimeout(function () {
        if (!githubMetricRendered && Number.isFinite(sharedGithubFallback.value) && sharedGithubFallback.value > 0) {
          renderMetricUpdate(githubStarsNode, githubStarsUpdatedNode, sharedGithubFallback.value, 'GitHub stars', {
            updatedAt: sharedGithubFallback.updatedAt || 'shared fallback'
          });
        }
      }, 3000);

      Promise.all([
        fetchUserRepoStars(),
        Promise.all(featuredGithubRepos.map(fetchRepoStarsWithFallback))
      ]).then(function (results) {
        var userStars = results[0];
        var featuredStars = results[1].reduce(function (sum, stars) {
          return sum + stars;
        }, 0);
        var totalStars = userStars + featuredStars;

        renderMetricUpdate(githubStarsNode, githubStarsUpdatedNode, totalStars, 'GitHub stars', writeMetricCache(githubStarsCacheKey, totalStars));
      }).catch(function () {
        if (!githubMetricRendered && !cachedGithubStars && Number.isFinite(sharedGithubFallback.value) && sharedGithubFallback.value > 0) {
          renderMetricUpdate(githubStarsNode, githubStarsUpdatedNode, sharedGithubFallback.value, 'GitHub stars', {
            updatedAt: sharedGithubFallback.updatedAt || 'shared fallback'
          });
          return;
        }
        if (!cachedGithubStars && githubStarsUpdatedNode) {
          githubStarsUpdatedNode.textContent = 'GitHub stars update failed';
        }
      });
    };

    updateScholarOnVisit();
    updateGithubStarsOnVisit();

    document.addEventListener('click', function (event) {
      if (event.target.closest(ignoredSelector)) {
        return;
      }

      var robot = document.createElement('span');
      robot.className = 'floating-robot';
      robot.textContent = '🤖✨';
      robot.style.left = event.clientX + 'px';
      robot.style.top = event.clientY + 'px';
      robot.style.setProperty('--robot-drift', (Math.random() * 36 - 18).toFixed(0) + 'px');

      document.body.appendChild(robot);
      robot.addEventListener('animationend', function () {
        robot.remove();
      });
    });
  })();
</script>

</div>
