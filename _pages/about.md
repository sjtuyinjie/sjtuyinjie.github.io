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

  a.about-chip {
    text-decoration: none;
    transition: border-color 0.18s ease, background 0.18s ease, color 0.18s ease;
  }

  a.about-chip:hover {
    border-color: #60a5fa;
    background: #dbeafe;
    color: #1e40af;
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
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 0.8rem;
  }

  .theme-card {
    display: flex;
    flex-direction: column;
    overflow: hidden;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    background: #ffffff;
    box-shadow: 0 8px 20px rgba(15, 23, 42, 0.06);
    transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease;
    scroll-margin-top: 5rem;
    min-width: 0;
  }

  .theme-card:hover {
    border-color: #93c5fd;
    box-shadow: 0 14px 28px rgba(37, 99, 235, 0.12);
    transform: translateY(-2px);
  }

  .theme-preview {
    position: relative;
    aspect-ratio: 16 / 9;
    overflow: hidden;
    background: linear-gradient(180deg, #f1f5f9, #e2e8f0);
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
    padding: 0.28rem;
    background: transparent;
  }

  .theme-slide-title {
    position: absolute;
    z-index: 3;
    left: 50%;
    top: 50%;
    margin: 0;
    color: #ffffff;
    font-size: clamp(0.92rem, 1.15vw, 1.28rem);
    font-weight: 800;
    letter-spacing: 0.04em;
    line-height: 1.2;
    opacity: 0;
    transform: translate(-50%, -50%);
    pointer-events: none;
    white-space: nowrap;
    -webkit-text-stroke: 2px #0f172a;
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
    left: 0.5rem;
    bottom: 0.45rem;
    padding: 0.14rem 0.45rem;
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 999px;
    background: rgba(15, 23, 42, 0.88);
    color: #ffffff;
    font-size: 0.62rem;
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
    display: flex;
    flex: 1;
    flex-direction: column;
    padding: 0.85rem 0.85rem 0.95rem;
  }

  .theme-header {
    display: flex;
    align-items: flex-start;
    gap: 0.45rem;
    margin-bottom: 0.4rem;
  }

  .theme-icon {
    display: inline-flex;
    flex-shrink: 0;
    width: 1.65rem;
    height: 1.65rem;
    align-items: center;
    justify-content: center;
    border-radius: 0.5rem;
    background: rgba(239, 246, 255, 0.95);
    color: var(--about-primary);
    font-size: 0.75rem;
    margin-top: 0.05rem;
  }

  .theme-card h3 {
    margin: 0;
    color: #0f172a;
    font-size: clamp(0.82rem, 1.05vw, 0.95rem);
    font-weight: 700;
    line-height: 1.28;
  }

  .theme-description {
    flex: 1;
    margin: 0 0 0.65rem;
    min-height: calc(0.76rem * 1.55 * 3);
    color: var(--about-muted);
    font-size: 0.76rem;
    line-height: 1.55;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .theme-papers {
    display: flex;
    flex-wrap: wrap;
    gap: 0.3rem;
  }

  .about-page a.theme-paper-tag {
    color: #1d4ed8;
    text-decoration: none;
  }

  .theme-paper-tag {
    padding: 0.16rem 0.42rem;
    border-radius: 0.3rem;
    background: rgba(239, 246, 255, 0.95);
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.01em;
    transition: background 0.18s ease, color 0.18s ease;
  }

  .about-page a.theme-paper-tag:hover {
    background: var(--about-primary);
    color: #ffffff;
    text-decoration: none;
  }

  .about-page h2 {
    margin-top: 0;
    padding-top: 1.35rem;
    color: #0f172a;
    border-bottom-color: #dbeafe;
    scroll-margin-top: 0;
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

  .representative-badge {
    display: inline-block;
    margin-left: 0.35rem;
    padding: 0.12rem 0.42rem;
    border-radius: 0.3rem;
    background: #fff3a8;
    color: #5b4500;
    font-size: 0.7em;
    font-weight: 650;
    vertical-align: middle;
    white-space: nowrap;
  }

  .about-page .hoverTable tr.publication-row--representative {
    background: #fff8d6;
    box-shadow: inset 3px 0 0 #eab308;
  }

  .about-page .hoverTable tr.publication-row--representative:hover {
    background: #fff3b0;
  }

  .about-page .hoverTable tr.publication-row--representative .archive__item-title,
  .about-page .hoverTable tr.publication-row--representative .publication-authors,
  .about-page .hoverTable tr.publication-row--representative td {
    color: #1f2937;
  }

  .about-page .hoverTable tr.publication-row--representative a {
    color: #1d4ed8;
  }

  .about-page .hoverTable tr.publication-row--representative a:hover {
    color: #6d28d9;
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

  .about-meta-note.metric-breakdown-card {
    top: 50%;
    bottom: auto;
    left: calc(100% + 0.55rem);
    width: 17.5rem;
    max-width: min(17.5rem, calc(100vw - 2rem));
    padding: 0.7rem 0.75rem 0.55rem;
    border: 1px solid rgba(148, 163, 184, 0.22);
    border-radius: 0.65rem;
    background: linear-gradient(165deg, rgba(15, 23, 42, 0.97), rgba(30, 41, 59, 0.96));
    box-shadow: 0 14px 36px rgba(15, 23, 42, 0.28);
    white-space: normal;
    transform: translateY(-50%) translateX(0.25rem);
  }

  .stars-card-title {
    margin: 0 0 0.45rem;
    color: #e2e8f0;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
  }

  .stars-stack {
    display: flex;
    width: 100%;
    height: 0.42rem;
    margin-bottom: 0.55rem;
    overflow: hidden;
    border-radius: 999px;
    background: rgba(148, 163, 184, 0.2);
  }

  .stars-stack-seg {
    height: 100%;
    min-width: 2px;
  }

  .stars-list {
    display: flex;
    flex-direction: column;
    gap: 0.28rem;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .stars-row {
    display: grid;
    grid-template-columns: 0.55rem minmax(0, 1fr) auto;
    column-gap: 0.4rem;
    row-gap: 0.16rem;
    align-items: center;
  }

  .stars-dot {
    width: 0.42rem;
    height: 0.42rem;
    border-radius: 999px;
  }

  .stars-name {
    overflow: hidden;
    color: #f1f5f9;
    font-size: 0.74rem;
    font-weight: 600;
    line-height: 1.2;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .stars-count {
    color: #cbd5e1;
    font-size: 0.72rem;
    font-variant-numeric: tabular-nums;
    font-weight: 600;
    white-space: nowrap;
  }

  .stars-bar-track {
    grid-column: 2 / 4;
    height: 0.18rem;
    overflow: hidden;
    border-radius: 999px;
    background: rgba(148, 163, 184, 0.18);
  }

  .stars-bar-fill {
    height: 100%;
    border-radius: 999px;
  }

  .stars-updated {
    margin-top: 0.5rem;
    padding-top: 0.4rem;
    border-top: 1px solid rgba(148, 163, 184, 0.2);
    color: #94a3b8;
    font-size: 0.68rem;
    line-height: 1.3;
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

  .metric-tooltip-wrap:hover .about-meta-note.metric-breakdown-card,
  .metric-tooltip-wrap:focus-within .about-meta-note.metric-breakdown-card {
    transform: translateY(-50%) translateX(0);
  }

  .floating-robot {
    position: fixed;
    left: 0;
    top: 0;
    z-index: 9999;
    display: inline-flex;
    width: 3.4rem;
    height: 3.4rem;
    align-items: center;
    justify-content: center;
    pointer-events: none;
    filter: drop-shadow(0 10px 18px rgba(15, 23, 42, 0.22));
    transform: translate(-50%, -50%);
    animation: robot-fly-up 1.2s ease-out forwards;
    will-change: transform, opacity;
  }

  .floating-robot img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    pointer-events: none;
  }

  html[data-theme="dark"] .floating-robot {
    filter: drop-shadow(0 12px 22px rgba(0, 0, 0, 0.45));
  }


  @keyframes robot-fly-up {
    0% {
      opacity: 0;
      transform: translate(-50%, -10%) translateY(8px);
    }

    14% {
      opacity: 1;
      transform: translate(-50%, -50%) translateY(0);
    }

    100% {
      opacity: 0;
      transform: translate(calc(-50% + var(--robot-drift, 0px)), -50%) translateY(-118px);
    }
  }

  @media (max-width: 1100px) {
    .themes-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 0.9rem;
    }

    .theme-card h3 {
      font-size: 0.95rem;
    }

    .theme-description {
      font-size: 0.8rem;
      min-height: calc(0.8rem * 1.55 * 2);
      -webkit-line-clamp: 2;
    }

    .theme-slide-title {
      font-size: 1.2rem;
    }
  }

  @media (max-width: 640px) {
    .themes-grid {
      grid-template-columns: 1fr;
    }
  }

  @media (max-width: 520px) {
    .about-hero {
      padding: 1.1rem;
    }
  }

  html[data-theme="dark"] .about-page {
    --about-primary: #7dd3fc;
    --about-accent: #5eead4;
    --about-hover: #93c5fd;
    --about-work: #fbbf24;
    --about-author: #5eead4;
    --about-author-bg: rgba(45, 212, 191, 0.14);
    --about-ink: #e8edf5;
    --about-muted: #9aa6b8;
    --about-surface: #151b24;
    --about-border: rgba(125, 211, 252, 0.18);
  }

  html[data-theme="dark"] .about-hero {
    background:
      radial-gradient(circle at top right, rgba(56, 189, 248, 0.14), transparent 34%),
      linear-gradient(145deg, #12161e 0%, #0e131a 100%);
    box-shadow: 0 16px 36px rgba(0, 0, 0, 0.28);
  }

  html[data-theme="dark"] .about-chip {
    border-color: rgba(125, 211, 252, 0.28);
    color: #bae6fd;
    background: rgba(14, 165, 233, 0.12);
  }

  html[data-theme="dark"] a.about-chip:hover {
    border-color: rgba(125, 211, 252, 0.45);
    background: rgba(56, 189, 248, 0.18);
    color: #e0f2fe;
  }

  html[data-theme="dark"] .about-section-note {
    color: #e2e8f0;
  }

  html[data-theme="dark"] .theme-card {
    border-color: rgba(148, 163, 184, 0.16);
    background: #12161e;
    box-shadow: 0 12px 28px rgba(0, 0, 0, 0.28);
  }

  html[data-theme="dark"] .theme-card:hover {
    border-color: rgba(125, 211, 252, 0.35);
    box-shadow: 0 18px 36px rgba(14, 165, 233, 0.12);
  }

  html[data-theme="dark"] .theme-preview {
    background: linear-gradient(180deg, #151b24, #10151d);
  }

  html[data-theme="dark"] .theme-card h3,
  html[data-theme="dark"] .about-page h2 {
    color: #f1f5f9;
  }

  html[data-theme="dark"] .about-page h2 {
    border-bottom-color: rgba(125, 211, 252, 0.2);
  }

  html[data-theme="dark"] .theme-icon {
    background: rgba(56, 189, 248, 0.12);
    color: #7dd3fc;
  }

  html[data-theme="dark"] .theme-paper-tag {
    background: rgba(56, 189, 248, 0.12);
  }

  html[data-theme="dark"] .about-page a.theme-paper-tag {
    color: #7dd3fc;
  }

  html[data-theme="dark"] .about-page a.theme-paper-tag:hover {
    background: #0ea5e9;
    color: #041018;
  }

  html[data-theme="dark"] .about-page .hoverTable tr {
    background: #12161e;
  }

  html[data-theme="dark"] .about-page .hoverTable tr:hover {
    background: #18202c;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.28);
  }

  html[data-theme="dark"] .about-page .publication-authors,
  html[data-theme="dark"] .about-page .project-authors {
    color: #e2e8f0;
  }

  html[data-theme="dark"] .highlight-soft {
    background: rgba(251, 191, 36, 0.18);
    color: #fde68a;
  }

  html[data-theme="dark"] .about-page .hoverTable tr.publication-row--representative {
    background: linear-gradient(90deg, rgba(251, 191, 36, 0.16), rgba(251, 191, 36, 0.08));
    box-shadow: inset 3px 0 0 #fbbf24;
  }

  html[data-theme="dark"] .about-page .hoverTable tr.publication-row--representative:hover {
    background: linear-gradient(90deg, rgba(251, 191, 36, 0.22), rgba(251, 191, 36, 0.12));
  }

  html[data-theme="dark"] .about-page .hoverTable tr.publication-row--representative .archive__item-title,
  html[data-theme="dark"] .about-page .hoverTable tr.publication-row--representative .publication-authors,
  html[data-theme="dark"] .about-page .hoverTable tr.publication-row--representative td,
  html[data-theme="dark"] .about-page .hoverTable tr.publication-row--representative strong {
    color: #f8fafc;
  }

  html[data-theme="dark"] .about-page .hoverTable tr.publication-row--representative .publication-authors b,
  html[data-theme="dark"] .about-page .hoverTable tr.publication-row--representative .publication-authors strong {
    color: var(--about-author);
    background: var(--about-author-bg);
  }

  html[data-theme="dark"] .about-page .hoverTable tr.publication-row--representative .venue-note {
    color: #fca5a5;
  }

  html[data-theme="dark"] .about-page .hoverTable tr.publication-row--representative a {
    color: #7dd3fc;
  }

  html[data-theme="dark"] .about-page .hoverTable tr.publication-row--representative a:hover {
    color: #bae6fd;
  }

  html[data-theme="dark"] .representative-badge {
    background: rgba(251, 191, 36, 0.22);
    color: #fde68a;
    border: 1px solid rgba(251, 191, 36, 0.35);
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
My work has appeared in leading robotics and AI venues, including <strong>CoRL, ICRA, IROS, RA-L, CVPR, TRO, TAES</strong>, and <strong>GPS Solutions</strong>. My research has been supported by the National Key R&D Program and the <a class="org-link" href="https://www.nsfc.gov.cn/english/site_1/index.html">NSFC</a>. Representative projects include <strong><a class="work-link" href="https://wmcraftnet.github.io/">WM-Craftnet</a></strong>, <strong><a class="work-link" href="https://github.com/SJTU-ViSYS/M2DGR">M2DGR</a></strong>, <strong><a class="work-link" href="https://github.com/SJTU-ViSYS/Ground-Fusion">Ground-Fusion</a></strong>, <strong><a class="work-link" href="https://arxiv.org/abs/2407.11333">DAF</a></strong>, <strong><a class="work-link" href="https://github.com/sjtuyinjie/Ground-Fusion2">Ground-Fusion++ / M3DGR</a></strong> and so on, with <span class="metric-tooltip-wrap"><span id="scholar-citations" class="about-highlight-red"><strong>Google Scholar citations</strong></span><span id="scholar-last-updated" class="about-meta-note metric-breakdown-card">loading latest citation count...</span></span>. I am also an active open-source contributor, with <span class="metric-tooltip-wrap"><span id="github-stars" class="about-highlight-red"><strong>GitHub stars</strong></span><span id="github-stars-last-updated" class="about-meta-note metric-breakdown-card">loading latest GitHub stars...</span></span> across my projects.
</p>

<div class="about-chip-row" aria-label="Research interests">
  <a href="#theme-dexterous-manipulation" class="about-chip">Dexterous Manipulation</a>
  <a href="#theme-fusion-slam" class="about-chip">Multi-sensor Fusion SLAM</a>
  <a href="#theme-multimodal-reasoning" class="about-chip">Multi-modal Reasoning</a>
  <a href="#theme-whole-body-control" class="about-chip">Whole-Body Control</a>
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
  <a href="https://github.com/sjtuyinjie" target="_blank">
    <img src="https://img.shields.io/github/followers/sjtuyinjie?style=flat-square&logo=github&logoColor=white&label=Followers&color=00C000" alt="GitHub Followers" />
  </a>
</div>

## News
{% include news.html %}

## Research Themes

<div class="research-themes">

<p class="research-intro">My research spans <strong>dexterous manipulation</strong>, <strong>multi-sensor fusion SLAM</strong>, <strong>multi-modal reasoning</strong>, and <strong>whole-body control</strong> — building robust perception and embodied autonomy for real-world robots.</p>

<div class="themes-grid">

<div class="theme-card" id="theme-dexterous-manipulation">
  <div class="theme-preview">
    <div class="theme-slide active" data-duration="11055">
      <div class="theme-slide-intro-veil" aria-hidden="true"></div>
      <div class="theme-slide-media">
        <a href="https://wmcraftnet.github.io/" target="_blank" rel="noopener noreferrer">
          <video muted playsinline preload="metadata" poster="/gifs/wmcraftnet_poster.jpg" aria-label="WM-Craftnet teaser">
            <source src="/gifs/wmcraftnet_teaser.mp4" type="video/mp4" />
          </video>
        </a>
      </div>
      <span class="theme-slide-title">WM-Craftnet</span>
      <span class="theme-slide-tag">WM-Craftnet</span>
    </div>
    <div class="theme-slide" data-duration="15070">
      <div class="theme-slide-intro-veil" aria-hidden="true"></div>
      <div class="theme-slide-media">
        <a href="https://www.sharpa.com/pages/wave" target="_blank" rel="noopener noreferrer">
          <img src="/gifs/rotation.gif" alt="Multi-object rotation demo" loading="lazy" />
        </a>
      </div>
      <span class="theme-slide-title">Multi-Object Rotation</span>
      <span class="theme-slide-tag">Multi-Object Rotation</span>
    </div>
    <div class="theme-slide-dots">
      <button class="theme-dot active" data-index="0" type="button" aria-label="Show WM-Craftnet teaser"></button>
      <button class="theme-dot" data-index="1" type="button" aria-label="Show multi-object rotation"></button>
    </div>
  </div>
  <div class="theme-body">
    <div class="theme-header">
      <div class="theme-icon"><i class="fa fa-hand" aria-hidden="true"></i></div>
      <h3>Dexterous Manipulation</h3>
    </div>
    <p class="theme-description">World-model priors for robust, object-ID-free visuotactile in-hand manipulation.</p>
    <div class="theme-papers">
      <a href="https://wmcraftnet.github.io/" target="_blank" rel="noopener noreferrer" class="theme-paper-tag">WM-Craftnet</a>
      <a href="https://www.sharpa.com/pages/wave" target="_blank" rel="noopener noreferrer" class="theme-paper-tag">Multi-Object Rotation</a>
    </div>
  </div>
</div>

<div class="theme-card" id="theme-fusion-slam">
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
    <p class="theme-description">Fusion frameworks and benchmarks for robust localization under sensor failure and outdoor corner cases.</p>
    <div class="theme-papers">
      <a href="https://sjtuyinjie.github.io/ultrafusion-web/" target="_blank" rel="noopener noreferrer" class="theme-paper-tag">Ultra-Fusion</a>
      <a href="https://github.com/SJTU-ViSYS/Ground-Fusion" target="_blank" rel="noopener noreferrer" class="theme-paper-tag">Ground-Fusion</a>
      <a href="https://github.com/SJTU-ViSYS/M2DGR" target="_blank" rel="noopener noreferrer" class="theme-paper-tag">M2DGR</a>
      <a href="https://sjtuyinjie.github.io/M3DGR-website/" target="_blank" rel="noopener noreferrer" class="theme-paper-tag">M3DGR</a>
    </div>
  </div>
</div>

<div class="theme-card" id="theme-multimodal-reasoning">
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
    <p class="theme-description">Cross-modal perception and navigation using vision, audio, and LiDAR reflectance for scene understanding.</p>
    <div class="theme-papers">
      <a href="https://sites.google.com/view/disentangled-acoustic-fields/home" target="_blank" rel="noopener noreferrer" class="theme-paper-tag">DAF</a>
      <a href="https://nidar-web.github.io/" target="_blank" rel="noopener noreferrer" class="theme-paper-tag">NIDAR</a>
    </div>
  </div>
</div>

<div class="theme-card" id="theme-whole-body-control">
  <div class="theme-preview">
    <div class="theme-slide active" data-duration="4800">
      <div class="theme-slide-intro-veil" aria-hidden="true"></div>
      <div class="theme-slide-media">
        <a href="https://mp.weixin.qq.com/s/Avhnn3QPbnm8lRxSwvRB3g" target="_blank" rel="noopener noreferrer">
          <img src="/gifs/idc.gif" alt=" demo" loading="lazy" />
        </a>
      </div>
      <span class="theme-slide-title">IDC Robot</span>
      <span class="theme-slide-tag">IDC Robot</span>
    </div>
    <div class="theme-slide-dots">
      <button class="theme-dot active" data-index="0" type="button" aria-label="Show IDC Robot"></button>
    </div>
  </div>
  <div class="theme-body">
    <div class="theme-header">
      <div class="theme-icon"><i class="fa fa-robot" aria-hidden="true"></i></div>
      <h3>Whole-body Control</h3>
    </div>
    <p class="theme-description">Whole-body control coordinating navigation, balance, and manipulation for mobile robots in human environments.</p>
    <div class="theme-papers">
      <a href="https://www.youtube.com/watch?v=WplE1GW5K3o" target="_blank" rel="noopener noreferrer" class="theme-paper-tag">IDC Robot</a>
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
    var scholarCacheKey = 'aboutScholarCitationsV2';
    var githubStarsCacheKey = 'aboutGithubStarsV2';
    var scholarMetricRendered = false;
    var githubMetricRendered = false;
    var sharedScholarFallback = {
      value: Number('{{ site.data.scholar_stats.citations | default: 0 }}'),
      updatedAt: '{{ site.data.scholar_stats.updated_at | default: "" }}',
      breakdown: [
        {% for paper in site.data.scholar_stats.papers %}
        { name: {{ paper.name | jsonify }}, stars: Number('{{ paper.citations }}') }{% unless forloop.last %},{% endunless %}
        {% endfor %}
      ]
    };
    var sharedGithubFallback = {
      value: Number('{{ site.data.github_stars.stars | default: 0 }}'),
      updatedAt: '{{ site.data.github_stars.updated_at | default: "" }}'
    };
    var starPalette = ['#60a5fa', '#2dd4bf', '#fbbf24', '#f87171', '#38bdf8', '#a78bfa', '#34d399', '#fb923c'];
    var othersColor = '#94a3b8';
    var paperNameAliases = [
      [/Innovation-based Kalman filter/i, 'Innovation-KF'],
      [/Towards Robust Sensor-Fusion Ground SLAM/i, 'M3DGR & GF2'],
      [/Implicit Event-RGBD Neural SLAM/i, 'EN-SLAM'],
      [/Disentangled Acoustic Fields/i, 'DAF'],
      [/Ground-[Cc]hallenge/i, 'Ground-Challenge'],
      [/Ground-Fusion/i, 'Ground-Fusion'],
      [/M2C-GVIO/i, 'M2C-GVIO'],
      [/Sky-GVINS/i, 'Sky-GVINS'],
      [/Ultra-Fusion/i, 'Ultra-Fusion'],
      [/WM-Craftnet/i, 'WM-Craftnet'],
      [/In-P3 VIO/i, 'In-P3 VIO'],
      [/\bLIGO\b/i, 'LIGO'],
      [/\bM2DGR\b/i, 'M2DGR']
    ];
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
    var shortRepoName = function (fullName) {
      var parts = String(fullName || '').split('/');
      return parts.length > 1 ? parts[parts.length - 1] : fullName;
    };
    var shortPaperName = function (title) {
      var clean = String(title || '').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
      for (var i = 0; i < paperNameAliases.length; i += 1) {
        if (paperNameAliases[i][0].test(clean)) {
          return paperNameAliases[i][1];
        }
      }
      var beforeColon = clean.split(/[:：]/)[0].trim();
      return beforeColon.length > 28 ? (beforeColon.slice(0, 26) + '…') : beforeColon;
    };
    var buildThresholdBreakdown = function (items, threshold) {
      var sorted = items.slice().sort(function (a, b) {
        return b.stars - a.stars;
      });
      var major = [];
      var others = 0;

      sorted.forEach(function (item) {
        if (item.stars >= threshold) {
          major.push({
            name: item.name,
            stars: item.stars
          });
        } else {
          others += item.stars;
        }
      });

      if (others > 0) {
        major.push({ name: 'Others', stars: others });
      }

      return major;
    };
    var buildStarsBreakdown = function (repos) {
      return buildThresholdBreakdown(repos.map(function (repo) {
        return {
          name: shortRepoName(repo.name),
          stars: repo.stars
        };
      }), 101);
    };
    var buildCitationBreakdown = function (papers) {
      return buildThresholdBreakdown(papers.map(function (paper) {
        return {
          name: shortPaperName(paper.name),
          stars: paper.stars
        };
      }), 25);
    };
    var renderMetricBreakdownCard = function (updatedNode, total, breakdown, updatedAt, title) {
      if (!updatedNode) {
        return;
      }

      if (!breakdown || !breakdown.length) {
        updatedNode.textContent = updatedAt ? ('last update: ' + updatedAt) : 'loading...';
        return;
      }

      var maxStars = Math.max.apply(null, breakdown.map(function (item) {
        return item.stars;
      }));
      var stackHtml = breakdown.map(function (item, idx) {
        var color = item.name === 'Others' ? othersColor : starPalette[idx % starPalette.length];
        var width = total > 0 ? ((item.stars / total) * 100).toFixed(2) : 0;
        return '<span class="stars-stack-seg" style="width:' + width + '%;background:' + color + ';"></span>';
      }).join('');
      var rowsHtml = breakdown.map(function (item, idx) {
        var color = item.name === 'Others' ? othersColor : starPalette[idx % starPalette.length];
        var barWidth = maxStars > 0 ? ((item.stars / maxStars) * 100).toFixed(2) : 0;
        return '<li class="stars-row">' +
          '<span class="stars-dot" style="background:' + color + ';"></span>' +
          '<span class="stars-name">' + item.name + '</span>' +
          '<span class="stars-count">' + formatNumber(item.stars) + '</span>' +
          '<span class="stars-bar-track"><span class="stars-bar-fill" style="width:' + barWidth + '%;background:' + color + ';"></span></span>' +
          '</li>';
      }).join('');

      updatedNode.innerHTML =
        '<p class="stars-card-title">' + title + '</p>' +
        '<div class="stars-stack">' + stackHtml + '</div>' +
        '<ul class="stars-list">' + rowsHtml + '</ul>' +
        (updatedAt ? ('<div class="stars-updated">last update: ' + updatedAt + '</div>') : '');
    };
    var readMetricCache = function (key) {
      try {
        var cached = localStorage.getItem(key);
        return cached ? JSON.parse(cached) : null;
      } catch (err) {
        return null;
      }
    };
    var writeMetricCache = function (key, value, extra) {
      var cache = {
        value: value,
        updatedAt: nowString()
      };

      if (extra) {
        Object.keys(extra).forEach(function (k) {
          cache[k] = extra[k];
        });
      }

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
        renderMetricBreakdownCard(updatedNode, value, cache && cache.breakdown, cache && cache.updatedAt, 'Citations by paper');
        return;
      }
      if (node === githubStarsNode) {
        githubMetricRendered = true;
        renderMetricBreakdownCard(updatedNode, value, cache && cache.breakdown, cache && cache.updatedAt, 'Stars by project');
        return;
      }
      if (updatedNode && cache && cache.updatedAt) {
        updatedNode.textContent = 'last update: ' + cache.updatedAt;
      }
    };
    var stripHtml = function (value) {
      return String(value || '').replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
    };
    var parseScholarPapers = function (text) {
      var papers = [];
      var seen = {};
      var htmlRe = /class="gsc_a_at"[^>]*>([\s\S]*?)<\/a>[\s\S]*?class="gsc_a_ac[^"]*"[^>]*>\s*([\d,]*)/gi;
      var htmlMatch = htmlRe.exec(text);

      while (htmlMatch) {
        var htmlTitle = stripHtml(htmlMatch[1]);
        var htmlCites = Number((htmlMatch[2] || '0').replace(/,/g, '')) || 0;
        if (htmlTitle && !seen[htmlTitle]) {
          seen[htmlTitle] = true;
          papers.push({ name: htmlTitle, stars: htmlCites });
        }
        htmlMatch = htmlRe.exec(text);
      }

      if (papers.length) {
        return papers;
      }

      var mdRe = /^\|\s*(?!Title)(.+?)\s*\|\s*(\d+)\s*\|\s*\d{4}\s*\|/gm;
      var mdMatch = mdRe.exec(text);
      while (mdMatch) {
        var mdTitle = stripHtml(mdMatch[1]).replace(/\s+[A-Z]\s+[A-Za-z].*$/, function (tail) {
          return /ESI|CVPR|IEEE|arXiv|Satellite|GPS|Geo-spatial|Proceedings/i.test(tail) ? tail : '';
        }).trim();
        var firstAuthorCut = mdTitle.search(/\s[A-Z]\s+[A-Za-z]/);
        if (firstAuthorCut > 12) {
          mdTitle = mdTitle.slice(0, firstAuthorCut).trim();
        }
        var mdCites = Number(mdMatch[2]);
        if (mdTitle && Number.isFinite(mdCites) && !seen[mdTitle]) {
          seen[mdTitle] = true;
          papers.push({ name: mdTitle, stars: mdCites });
        }
        mdMatch = mdRe.exec(text);
      }

      return papers;
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
    var parseScholarPayload = function (text) {
      var citations = parseScholarCitations(text);
      var papers = parseScholarPapers(text);
      if (citations === null && !papers.length) {
        return null;
      }
      if (citations === null && papers.length) {
        citations = papers.reduce(function (sum, paper) {
          return sum + paper.stars;
        }, 0);
      }
      return {
        citations: citations,
        breakdown: papers.length ? buildCitationBreakdown(papers) : null
      };
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
            updatedAt: sharedScholarFallback.updatedAt || 'shared fallback',
            breakdown: sharedScholarFallback.breakdown
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
            var payload = parseScholarPayload(text);
            if (!payload || payload.citations === null) {
              throw new Error('parse failed');
            }
            return payload;
          })
          .catch(function () {
            return tryFetch(idx + 1);
          });
      };

      tryFetch(0).then(function (payload) {
        if (!payload) {
          return;
        }
        var breakdown = payload.breakdown && payload.breakdown.length
          ? payload.breakdown
          : sharedScholarFallback.breakdown;
        var extra = breakdown && breakdown.length ? { breakdown: breakdown } : null;
        renderMetricUpdate(
          citationNode,
          updatedNode,
          payload.citations,
          'Google Scholar citations',
          writeMetricCache(scholarCacheKey, payload.citations, extra)
        );
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
    var fetchUserReposFromReposApi = function (type, page, collected) {
      return fetchGithubJson('https://api.github.com/users/sjtuyinjie/repos?type=' + type + '&per_page=100&page=' + page)
        .then(function (repos) {
          var next = collected.concat(repos.map(function (repo) {
            return {
              name: repo.full_name || repo.name,
              stars: repo.stargazers_count || 0
            };
          }));

          if (repos.length === 100) {
            return fetchUserReposFromReposApi(type, page + 1, next);
          }

          return next;
        });
    };
    var fetchUserReposFromSearchApi = function (page, collected) {
      return fetchGithubJson('https://api.github.com/search/repositories?q=user:sjtuyinjie+fork:true&per_page=100&page=' + page)
        .then(function (result) {
          var repos = result.items || [];
          var next = collected.concat(repos.map(function (repo) {
            return {
              name: repo.full_name || repo.name,
              stars: repo.stargazers_count || 0
            };
          }));

          if (repos.length === 100 && page < 10) {
            return fetchUserReposFromSearchApi(page + 1, next);
          }

          return next;
        });
    };
    var fetchUserRepos = function () {
      var methods = [
        function () { return fetchUserReposFromReposApi('owner', 1, []); },
        function () { return fetchUserReposFromReposApi('all', 1, []); },
        function () { return fetchUserReposFromSearchApi(1, []); }
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
          return {
            name: fullName,
            stars: repo.stargazers_count || 0
          };
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
            return {
              name: fullName,
              stars: Math.round(numeric)
            };
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
        fetchUserRepos(),
        Promise.all(featuredGithubRepos.map(fetchRepoStarsWithFallback))
      ]).then(function (results) {
        var allRepos = results[0].concat(results[1]);
        var totalStars = allRepos.reduce(function (sum, repo) {
          return sum + (repo.stars || 0);
        }, 0);
        var breakdown = buildStarsBreakdown(allRepos);
        var cache = writeMetricCache(githubStarsCacheKey, totalStars, { breakdown: breakdown });

        renderMetricUpdate(githubStarsNode, githubStarsUpdatedNode, totalStars, 'GitHub stars', cache);
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

    var robotIconNames = ['hand', 'humanoid', 'smplx', 'quadruped', 'arm', 'wheeled'];
    var robotIconIndex = 0;

    document.addEventListener('click', function (event) {
      if (event.target.closest(ignoredSelector)) {
        return;
      }

      var name = robotIconNames[robotIconIndex % robotIconNames.length];
      robotIconIndex += 1;
      var robot = document.createElement('span');
      var img = document.createElement('img');
      robot.className = 'floating-robot';
      img.src = '/images/click-robots/dark-' + name + '.png';
      img.alt = '';
      robot.appendChild(img);
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
