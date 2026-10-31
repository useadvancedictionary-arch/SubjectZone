/**
 * SubjectZone - Main Application Controller
 * Supports multi-grade, multi-subject solved-exercise browsing
 * with verified solutions, TTS & STT.
 */

import { QAEngine } from './qa-engine.js';
import { speechEngine } from './speech-engine.js';

class SubjectZoneApp {
  constructor() {
    this.subjectsConfig = null;
    this.currentGrade = 'class_x';
    this.activeSubjectId = 'physics_x';
    this.activeSubjectConfig = null;
    this.activeSubjectData = null;
    this.currentUnit = null;
    this.allAnswersShown = false;

    // Sub-components
    this.qaEngine = null;

    this.init();
  }

  async init() {
    try {
      // 1. Load multi-grade & subject catalog
      const respConfig = await fetch('/data/subjects.json');
      this.subjectsConfig = await respConfig.json();

      // Check URL search params for subject preference if any
      const urlParams = new URLSearchParams(window.location.search);
      const requestedSubject = urlParams.get('subject') || 'physics_x';

      // Adopt the configured active grade; jump grades if the requested subject lives elsewhere
      this.currentGrade = this.subjectsConfig.activeGrade || 'class_x';
      const ownerGrade = Object.keys(this.subjectsConfig.subjects).find(g =>
        (this.subjectsConfig.subjects[g] || []).some(s => s.id === requestedSubject));
      if (ownerGrade) this.currentGrade = ownerGrade;

      // 2. Initialize sub-components
      this.initQAEngine();
      this.bindUIEvents();
      this.renderGradeCards();
      this.renderModalSubjects();
      this.updateGradeUI();

      // 3. Load active subject
      await this.loadSubject(requestedSubject);

    } catch (err) {
      console.error("Initialization error:", err);
    }
  }

  initQAEngine() {
    this.qaEngine = new QAEngine('solutionsBody');

    // Jump forward to the next unit that has solved questions
    window.addEventListener('request-next-solved-unit', (e) => {
      this.navigateToNextSolvedUnit(e.detail.fromUnit);
    });
  }

  isSubjectReady(subject) {
    return !!subject && subject.status === 'ready' && !!subject.dataFile &&
      (subject.totalQuestionsSolved || 0) > 0;
  }

  async loadSubject(subjectId) {
    try {
      const gradeSubjects = this.subjectsConfig.subjects[this.currentGrade] || [];
      let subjConfig = gradeSubjects.find(s => s.id === subjectId);
      if (!this.isSubjectReady(subjConfig)) {
        subjConfig = gradeSubjects.find(s => this.isSubjectReady(s)) || subjConfig;
      }
      if (!subjConfig || !subjConfig.dataFile) return;

      this.activeSubjectId = subjConfig.id;
      this.activeSubjectConfig = subjConfig;

      // Fetch dataset
      const resp = await fetch(subjConfig.dataFile);
      this.activeSubjectData = await resp.json();

      // Update UI elements
      this.updateSubjectUI();
      this.buildSidebarUnits();

      // Open the first unit that has solved questions
      const firstSolved = (this.activeSubjectData.chapters || []).find(ch => (ch.questions || []).length > 0);
      this.navigateToUnit(firstSolved ? firstSolved.number : 1);

    } catch (err) {
      console.error(`Failed to load subject ${subjectId}:`, err);
    }
  }

  gradeEntry(gradeId) {
    return (this.subjectsConfig.grades || []).find(g => g.id === (gradeId || this.currentGrade)) || null;
  }

  gradeLabel(gradeId) {
    const g = this.gradeEntry(gradeId);
    if (!g) return 'Class X (SSC-II)';
    return `${g.name} (${(g.level || '').replace(' Part ', '-')})`;
  }

  iconEmoji(icon) {
    const map = {
      atom: '⚛️', dna: '🧬', flask: '⚗️', calculator: '📐', 'laptop-code': '💻',
      'book-open': '📖', landmark: '🏛️', 'feather-alt': '🪶'
    };
    return map[icon] || '📖';
  }

  updateGradeUI() {
    const headerGradeName = document.getElementById('headerGradeName');
    if (headerGradeName) headerGradeName.textContent = this.gradeLabel(this.currentGrade);
  }

  renderGradeCards() {
    const grid = document.getElementById('modalGradesGrid');
    if (!grid) return;
    grid.querySelectorAll('.select-card-btn').forEach(card => {
      const gid = card.getAttribute('data-grade-id');
      const g = this.gradeEntry(gid);
      const available = g && g.available;
      card.classList.toggle('active', gid === this.currentGrade);
      card.style.opacity = available ? '1' : '0.6';
      card.style.cursor = available ? 'pointer' : 'not-allowed';
    });
  }

  renderModalSubjects() {
    const grid = document.getElementById('modalSubjectsGrid');
    const heading = document.getElementById('modalSubjectsHeading');
    if (!grid) return;
    const g = this.gradeEntry(this.currentGrade);
    if (heading && g) heading.textContent = `${g.name} Available Subjects`;

    const subjects = this.subjectsConfig.subjects[this.currentGrade] || [];
    grid.innerHTML = subjects.map(s => {
      const ready = this.isSubjectReady(s);
      const desc = ready
        ? `${s.totalQuestionsSolved} Solved • ${s.totalChapters} Units`
        : 'Solutions in preparation';
      return `
        <div class="select-card-btn${s.id === this.activeSubjectId ? ' active' : ''}" data-subject-id="${s.id}" style="${ready ? 'cursor:pointer;' : 'opacity:0.6;'}">
          <span class="select-card-title">${this.iconEmoji(s.icon)} ${s.name}</span>
          <span class="select-card-desc"${ready ? ' style="color:var(--accent-emerald-light);"' : ''}>${desc}</span>
        </div>
      `;
    }).join('');
  }

  async selectGrade(gradeId) {
    const g = this.gradeEntry(gradeId);
    if (!g || !g.available || gradeId === this.currentGrade) return;
    this.currentGrade = gradeId;
    this.updateGradeUI();
    this.renderGradeCards();
    this.renderModalSubjects();
    const first = (this.subjectsConfig.subjects[gradeId] || []).find(s => this.isSubjectReady(s));
    if (first) await this.loadSubject(first.id);
  }

  updateSubjectUI() {
    if (!this.activeSubjectConfig) return;
    const cfg = this.activeSubjectConfig;

    // Header pills
    const headerSubjName = document.getElementById('headerSubjectName');
    const headerSubjPill = document.getElementById('headerSubjectPill');
    if (headerSubjName) headerSubjName.textContent = cfg.name;
    if (headerSubjPill) {
      const dot = headerSubjPill.querySelector('span:first-child');
      if (dot && cfg.accentColor) dot.style.background = cfg.accentColor;
    }

    // Sidebar book card
    const titleEl = document.getElementById('sidebarBookTitle');
    const iconEl = document.getElementById('sidebarBookIcon');
    const boardEl = document.getElementById('sidebarBookBoard');
    const tagSolved = document.getElementById('sidebarTagSolved');
    const tagExercises = document.getElementById('sidebarTagExercises');
    const tagChapters = document.getElementById('sidebarTagChapters');

    const g = this.gradeEntry(this.currentGrade);
    if (titleEl) titleEl.textContent = `${cfg.name} — ${g ? g.name : 'Class X'}`;
    if (iconEl) iconEl.textContent = this.iconEmoji(cfg.icon);
    if (boardEl) boardEl.textContent = cfg.board || 'Sindh Textbook Board, Jamshoro';
    if (tagSolved) tagSolved.textContent = cfg.totalQuestionsSolved ? `${cfg.totalQuestionsSolved} Solved` : '100% Solved';
    if (tagExercises) {
      const sets = this.countExerciseSets();
      tagExercises.textContent = `${sets} Exercise Set${sets === 1 ? '' : 's'}`;
    }
    if (tagChapters) {
      const chCount = this.activeSubjectData ? this.activeSubjectData.chapters.length : (cfg.totalChapters || 10);
      tagChapters.textContent = `${chCount} Units`;
    }

    // Modal subject cards active class
    const modalGrid = document.getElementById('modalSubjectsGrid');
    if (modalGrid) {
      modalGrid.querySelectorAll('.select-card-btn').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('data-subject-id') === cfg.id);
      });
    }
  }

  countExerciseSets() {
    if (!this.activeSubjectData) return 0;
    const seen = new Set();
    (this.activeSubjectData.chapters || []).forEach(ch => {
      (ch.questions || []).forEach(q => seen.add(`${ch.number}::${q.section || 'Questions'}`));
    });
    return seen.size;
  }

  unitSections(ch) {
    const groups = [];
    const index = new Map();
    (ch.questions || []).forEach(q => {
      const key = q.section || 'Questions';
      if (!index.has(key)) {
        index.set(key, groups.length);
        groups.push({ name: key, count: 0 });
      }
      groups[index.get(key)].count++;
    });
    return groups;
  }

  buildSidebarUnits() {
    const listContainer = document.getElementById('sidebarChaptersList');
    if (!listContainer || !this.activeSubjectData) return;

    let html = '';
    this.activeSubjectData.chapters.forEach(ch => {
      const sections = this.unitSections(ch);
      const solvedCount = (ch.questions || []).length;
      html += `
        <div class="chapter-item" id="chapter_item_${ch.number}">
          <div class="chapter-item-header" data-ch="${ch.number}">
            <div class="chapter-header-left">
              <span class="chapter-number-pill">${ch.number}</span>
              <span class="chapter-name">${ch.title}</span>
            </div>
            <div class="chapter-header-right">
              <span class="chapter-page-span">${solvedCount ? solvedCount + ' solved' : '—'}</span>
              <span class="chapter-arrow">›</span>
            </div>
          </div>
          <div class="chapter-pages-container">
      `;

      if (sections.length) {
        sections.forEach(sec => {
          html += `
            <button class="chapter-quick-btn has-exercise" data-unit="${ch.number}" data-section="${sec.name}">
              <span>${sec.name}</span>
              <span class="chapter-page-span">${sec.count}</span>
            </button>
          `;
        });
      } else {
        html += `<div class="chapter-prep-note">Solutions in preparation</div>`;
      }

      html += `
          </div>
        </div>
      `;
    });

    listContainer.innerHTML = html;

    // Bind unit click events
    listContainer.querySelectorAll('.chapter-item-header').forEach(header => {
      header.addEventListener('click', () => {
        const item = header.closest('.chapter-item');
        const isOpen = item.classList.contains('open');
        listContainer.querySelectorAll('.chapter-item').forEach(i => i.classList.remove('open'));
        if (!isOpen) item.classList.add('open');
        this.navigateToUnit(parseInt(header.getAttribute('data-ch'), 10));
      });
    });

    listContainer.querySelectorAll('.chapter-quick-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        this.navigateToUnit(parseInt(btn.getAttribute('data-unit'), 10), btn.getAttribute('data-section'));
      });
    });
  }

  navigateToUnit(unitNumber, sectionName = null) {
    if (!this.activeSubjectData) return;
    const chapters = this.activeSubjectData.chapters || [];
    const ch = chapters.find(c => c.number === unitNumber) || null;
    this.currentUnit = unitNumber;

    // Render questions & solutions for this unit
    this.qaEngine.renderUnitQuestions(ch);

    const countBadge = document.getElementById('solutionsCountBadge');
    const count = ch ? (ch.questions || []).length : 0;
    if (countBadge) {
      countBadge.textContent = `${count} Solved`;
      countBadge.style.display = count > 0 ? 'inline-block' : 'none';
    }

    // Highlight active unit & section in sidebar
    document.querySelectorAll('.chapter-item').forEach(el => {
      const isActive = el.id === `chapter_item_${unitNumber}`;
      el.classList.toggle('active', isActive);
      if (isActive) el.classList.add('open');
    });
    document.querySelectorAll('.chapter-quick-btn').forEach(btn => {
      btn.classList.toggle('active',
        parseInt(btn.getAttribute('data-unit'), 10) === unitNumber && btn.getAttribute('data-section') === sectionName);
    });

    // Scroll solutions back to top (or to the requested section)
    const body = document.getElementById('solutionsBody');
    if (body) body.scrollTop = 0;
    if (sectionName) this.qaEngine.scrollToSection(sectionName);

    // Reset master toggle
    this.allAnswersShown = false;
    const masterBtn = document.getElementById('btnMasterToggleAnswers');
    if (masterBtn) {
      masterBtn.innerHTML = `
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
        <span>Show All Answers</span>
      `;
    }
  }

  navigateUnitDelta(delta) {
    if (!this.activeSubjectData) return;
    const chapters = this.activeSubjectData.chapters || [];
    if (!chapters.length) return;
    const idx = chapters.findIndex(c => c.number === this.currentUnit);
    const next = Math.max(0, Math.min(chapters.length - 1, (idx < 0 ? 0 : idx) + delta));
    this.navigateToUnit(chapters[next].number);
  }

  navigateToNextSolvedUnit(fromUnit) {
    if (!this.activeSubjectData) return;
    const chapters = this.activeSubjectData.chapters || [];
    const solved = chapters.filter(c => (c.questions || []).length > 0);
    if (!solved.length) return;
    const target = solved.find(c => c.number > fromUnit) || solved[0];
    this.navigateToUnit(target.number);
  }

  bindUIEvents() {
    // Keyboard shortcuts (ArrowLeft / ArrowRight move between units)
    window.addEventListener('keydown', (e) => {
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;
      if (e.key === 'ArrowRight' || e.key === 'PageDown') {
        this.navigateUnitDelta(1);
      } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        this.navigateUnitDelta(-1);
      }
    });

    // Master Toggle: Show / Hide All Answers
    const masterBtn = document.getElementById('btnMasterToggleAnswers');
    if (masterBtn) {
      masterBtn.addEventListener('click', () => {
        this.allAnswersShown = !this.allAnswersShown;
        this.qaEngine.toggleAllAnswers(this.allAnswersShown);
        masterBtn.innerHTML = this.allAnswersShown
          ? `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line></svg><span>Hide All Answers</span>`
          : `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg><span>Show All Answers</span>`;
      });
    }

    // Voice Search / Commands (STT in Header)
    const voiceSearchBtn = document.getElementById('btnVoiceSearch');
    if (voiceSearchBtn) {
      voiceSearchBtn.addEventListener('click', () => {
        if (voiceSearchBtn.classList.contains('recording')) {
          voiceSearchBtn.classList.remove('recording');
          speechEngine.stopListening();
        } else {
          voiceSearchBtn.classList.add('recording');
          speechEngine.startListening(
            (transcript) => {
              this.handleVoiceCommand(transcript);
            },
            () => {
              voiceSearchBtn.classList.remove('recording');
            }
          );
        }
      });
    }

    // Modals: Grade & Subject Switcher
    const gradeModalBtn = document.getElementById('btnOpenGradeModal');
    const headerSubjPill = document.getElementById('headerSubjectPill');
    const gradeModal = document.getElementById('gradeModalBackdrop');
    const closeGradeModal = document.getElementById('btnCloseGradeModal');

    if (gradeModalBtn && gradeModal) {
      gradeModalBtn.addEventListener('click', () => gradeModal.classList.add('open'));
    }
    if (headerSubjPill && gradeModal) {
      headerSubjPill.addEventListener('click', () => gradeModal.classList.add('open'));
    }
    if (closeGradeModal && gradeModal) {
      closeGradeModal.addEventListener('click', () => gradeModal.classList.remove('open'));
    }

    // Grade cards click (delegated)
    const gradesGrid = document.getElementById('modalGradesGrid');
    if (gradesGrid) {
      gradesGrid.addEventListener('click', (e) => {
        const card = e.target.closest('.select-card-btn');
        const gid = card && card.getAttribute('data-grade-id');
        if (gid) this.selectGrade(gid);
      });
    }

    // Modal Subject Cards click (delegated: grid is re-rendered per grade)
    const modalGrid = document.getElementById('modalSubjectsGrid');
    if (modalGrid) {
      modalGrid.addEventListener('click', async (e) => {
        const card = e.target.closest('.select-card-btn');
        const targetSubjId = card && card.getAttribute('data-subject-id');
        if (!targetSubjId) return;
        const gradeSubjects = this.subjectsConfig.subjects[this.currentGrade] || [];
        const targetCfg = gradeSubjects.find(s => s.id === targetSubjId);
        if (this.isSubjectReady(targetCfg)) {
          await this.loadSubject(targetSubjId);
          if (gradeModal) gradeModal.classList.remove('open');
        } else if (targetCfg) {
          alert(`${targetCfg.name} textbook solutions are currently in preparation.`);
        }
      });
    }

    // Speech Settings Modal
    const speechSettingsBtn = document.getElementById('btnOpenSpeechSettings');
    const speechModal = document.getElementById('speechModalBackdrop');
    const closeSpeechModal = document.getElementById('btnCloseSpeechModal');
    if (speechSettingsBtn && speechModal) {
      speechSettingsBtn.addEventListener('click', () => speechModal.classList.add('open'));
    }
    if (closeSpeechModal && speechModal) {
      closeSpeechModal.addEventListener('click', () => speechModal.classList.remove('open'));
    }

    // Speech Rate control
    const speechRateSelect = document.getElementById('speechRateSelect');
    if (speechRateSelect) {
      speechRateSelect.addEventListener('change', (e) => {
        speechEngine.setRate(e.target.value);
      });
    }

    // Mobile Sidebar Toggle
    const mobileSidebarBtn = document.getElementById('btnMobileSidebarToggle');
    const sidebar = document.getElementById('appSidebar');
    if (mobileSidebarBtn && sidebar) {
      mobileSidebarBtn.addEventListener('click', () => {
        sidebar.classList.toggle('mobile-open');
      });
    }
  }

  handleVoiceCommand(cmd) {
    const text = cmd.toLowerCase().trim();

    // Grade switching voice commands
    const gradeMatch = text.match(/class\s+(x|ix|xi|xii|10|9|11|12|ten|nine|eleven|twelve)\b/);
    if (gradeMatch) {
      const alias = { '9': 'class_ix', 'nine': 'class_ix', '10': 'class_x', 'ten': 'class_x', '11': 'class_xi', 'eleven': 'class_xi', '12': 'class_xii', 'twelve': 'class_xii' };
      this.selectGrade(alias[gradeMatch[1]] || `class_${gradeMatch[1]}`);
      return;
    }

    // Subject switching voice commands (any subject of the current grade)
    const gradeSubjects = this.subjectsConfig.subjects[this.currentGrade] || [];
    const byName = gradeSubjects.find(s => text.includes(s.name.toLowerCase()));
    if (byName) {
      this.loadSubject(byName.id);
      return;
    }

    // Check for "chapter X" or "unit X"
    const chMatch = text.match(/(?:chapter|unit)\s+(\d+)/);
    if (chMatch) {
      this.navigateToUnit(parseInt(chMatch[1], 10));
      return;
    }

    // "next" or "previous"
    if (text.includes('next')) {
      this.navigateUnitDelta(1);
    } else if (text.includes('previous') || text.includes('back')) {
      this.navigateUnitDelta(-1);
    } else if (text.includes('exercise') || text.includes('solution') || text.includes('answer')) {
      this.navigateToNextSolvedUnit(this.currentUnit || 0);
    }
  }
}

// Instantiate and start app on DOM ready
document.addEventListener('DOMContentLoaded', () => {
  window.subjectZoneApp = new SubjectZoneApp();
});
