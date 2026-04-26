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

  .about-highlight-red {
    color: #dc2626;
    font-weight: 800;
  }

  .about-meta-note {
    position: absolute;
    bottom: calc(100% + 0.45rem);
    left: 50%;
    z-index: 10;
    display: inline-block;
    width: max-content;
    max-width: min(220px, 80vw);
    padding: 0.25rem 0.45rem;
    border-radius: 0.35rem;
    margin-top: 0;
    background: rgba(15, 23, 42, 0.92);
    color: #ffffff;
    font-size: 0.78rem;
    line-height: 1.3;
    opacity: 0;
    pointer-events: none;
    transform: translateX(-50%) translateY(0.25rem);
    transition: opacity 0.15s ease, transform 0.15s ease, visibility 0.15s ease;
    visibility: hidden;
    white-space: nowrap;
  }

  .metric-tooltip-wrap {
    position: relative;
    display: inline-block;
    cursor: help;
  }

  .metric-tooltip-wrap:hover .about-meta-note,
  .metric-tooltip-wrap:focus-within .about-meta-note {
    opacity: 1;
    transform: translateX(-50%) translateY(0);
    visibility: visible;
  }

  .visitor-map {
    display: flex;
    justify-content: center;
    overflow: hidden;
    margin-top: 0.8rem;
    padding: 0.8rem;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    background: #ffffff;
    text-align: left;
  }

  .visitor-map #clustrmaps-widget-v2 {
    max-width: 100% !important;
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

    .visitor-map {
      padding: 0.5rem;
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
My work has appeared in leading robotics and AI venues, including <strong>ICRA, IROS, RA-L, CVPR, TRO, TAES</strong>, and <strong>GPS Solutions</strong>. My research has been supported by the National Key R&D Program and the <a class="org-link" href="https://www.nsfc.gov.cn/english/site_1/index.html">NSFC</a>. Representative projects include <strong><a class="work-link" href="https://github.com/SJTU-ViSYS/M2DGR">M2DGR</a></strong>, <strong><a class="work-link" href="https://github.com/SJTU-ViSYS/Ground-Fusion">Ground-Fusion</a></strong>, <strong><a class="work-link" href="https://arxiv.org/abs/2407.11333">DAF</a></strong>, <strong><a class="work-link" href="https://github.com/sjtuyinjie/Ground-Fusion2">Ground-Fusion++ / M3DGR</a></strong>, <a class="work-link" href="https://github.com/Joanna-HE/LIGO.">LIGO</a>, <a class="work-link" href="https://github.com/DelinQu/EN-SLAM">EN-SLAM</a>, <a class="work-link" href="https://github.com/sjtuyinjie/Ground-Challenge">Ground-Challenge</a>, and <a class="work-link" href="https://github.com/SJTU-ViSYS/Sky-GVINS">Sky-GVINS</a>, with <span class="metric-tooltip-wrap"><span id="scholar-citations" class="about-highlight-red" data-default="{{ site.data.scholar_stats.citations | default: 540 }}"><strong>{{ site.data.scholar_stats.citations | default: 540 }} Google Scholar citations</strong></span><span id="scholar-last-updated" class="about-meta-note">last updated: {{ site.data.scholar_stats.updated_at | default: "N/A" }}</span></span>. I am also an active open-source contributor, with <span class="metric-tooltip-wrap"><span id="github-stars" class="about-highlight-red" data-default="3000"><strong>3k+ GitHub stars</strong></span><span id="github-stars-last-updated" class="about-meta-note">updating GitHub stars...</span></span> across my projects.
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
  <script type="text/javascript" id="clustrmaps" src="//clustrmaps.com/map_v2.js?d=vTCiAvCm0aG85BtQG8a4pBHf0ElbAyAwmz5KIj6EvrY&co=2d78ad&cl=ffffff&w=800&t=tt"></script>
</div>

<script>
  (function () {
    var ignoredSelector = 'a, button, input, textarea, select, label, img, iframe, video, audio, canvas, svg, #clustrmaps-widget-v2, .clickable-gif';
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
    var todayString = function () {
      return new Date().toISOString().slice(0, 10);
    };
    var formatNumber = function (value) {
      return value.toLocaleString('en-US');
    };
    var parseScholarCitations = function (text) {
      var htmlPattern = /class="gsc_rsb_std">([\d,]+)<\/td>/;
      var markdownPattern = /Citations[\s\S]*?\n\s*([\d,]+)/i;
      var match = text.match(htmlPattern) || text.match(markdownPattern);
      if (!match) {
        return null;
      }

      var numeric = Number(match[1].replace(/,/g, ''));
      return Number.isFinite(numeric) ? numeric : null;
    };
    var updateScholarOnVisit = function () {
      if (!citationNode) {
        return;
      }

      var proxies = [
        'https://api.allorigins.win/raw?url=' + encodeURIComponent(scholarUrl),
        'https://r.jina.ai/http://scholar.google.com/citations?user=Y8LVRYIAAAAJ&hl=en'
      ];

      var tryFetch = function (idx) {
        if (idx >= proxies.length) {
          return Promise.resolve(null);
        }

        return fetch(proxies[idx], { method: 'GET' })
          .then(function (resp) {
            if (!resp.ok) {
              throw new Error('bad response');
            }
            return resp.text();
          })
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
        citationNode.innerHTML = '<strong>' + citations + ' Google Scholar citations</strong>';
        if (updatedNode) {
          updatedNode.textContent = 'last updated: ' + todayString();
        }
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
    var fetchGithubJson = function (url, retries) {
      var attemptsLeft = typeof retries === 'number' ? retries : 2;

      return fetchGithubJsonDirect(url).catch(function (err) {
        if (attemptsLeft <= 0) {
          return fetchGithubJsonViaProxy(url);
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
    var updateGithubStarsOnVisit = function () {
      if (!githubStarsNode) {
        return;
      }

      Promise.all([
        fetchUserRepoStars(),
        Promise.all(featuredGithubRepos.map(fetchRepoStars))
      ]).then(function (results) {
        var userStars = results[0];
        var featuredStars = results[1].reduce(function (sum, stars) {
          return sum + stars;
        }, 0);
        var totalStars = userStars + featuredStars;

        githubStarsNode.innerHTML = '<strong>' + formatNumber(totalStars) + ' GitHub stars</strong>';
        if (githubStarsUpdatedNode) {
          githubStarsUpdatedNode.textContent = 'last updated: ' + todayString();
        }
      }).catch(function () {
        if (githubStarsUpdatedNode) {
          githubStarsUpdatedNode.textContent = 'GitHub stars update failed';
        }
      });
    };

    updateScholarOnVisit();
    updateGithubStarsOnVisit();

    var enhanceVisitorDots = function () {
      var widget = document.getElementById('clustrmaps-widget-v2');
      if (!widget) {
        return false;
      }

      var layers = widget.querySelectorAll('canvas, svg');
      if (layers.length <= 1) {
        return false;
      }

      for (var i = 1; i < layers.length; i += 1) {
        layers[i].style.transform = 'scale(2)';
        layers[i].style.transformOrigin = 'center';
      }

      return true;
    };

    if (!enhanceVisitorDots()) {
      var observer = new MutationObserver(function () {
        if (enhanceVisitorDots()) {
          observer.disconnect();
        }
      });
      observer.observe(document.body, { childList: true, subtree: true });
      setTimeout(function () {
        observer.disconnect();
      }, 8000);
    }

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
