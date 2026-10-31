/**
 * SubjectZone - Q&A Display Engine
 * Manages rendering of questions, toggleable answers, TTS playback, and STT voice response.
 */

import { speechEngine } from './speech-engine.js';

export class QAEngine {
  constructor(containerId, options = {}) {
    this.container = document.getElementById(containerId);
    this.currentQuestions = [];
    this.allAnswersVisible = false;
    this.onAnswerToggle = options.onAnswerToggle || null;

    // Listen for TTS events from speech engine to update play button states
    window.addEventListener('tts-started', (e) => this.handleTTSStarted(e.detail.cardId));
    window.addEventListener('tts-ended', (e) => this.handleTTSEnded(e.detail.cardId));
  }

  renderUnitQuestions(chapter) {
    this.currentQuestions = chapter ? chapter.questions || [] : [];
    this.allAnswersVisible = false;

    if (!chapter || this.currentQuestions.length === 0) {
      this.renderPrepState(chapter);
      return;
    }

    const groups = [];
    const groupIndex = new Map();
    this.currentQuestions.forEach(q => {
      const key = q.section || 'Questions';
      if (!groupIndex.has(key)) {
        groupIndex.set(key, groups.length);
        groups.push({ name: key, questions: [] });
      }
      groups[groupIndex.get(key)].questions.push(q);
    });

    let html = `
      <div class="questions-list-wrapper">
        <div class="unit-heading">
          <h2>Unit ${chapter.number}: ${chapter.title}</h2>
          <span class="unit-heading-count">${this.currentQuestions.length} solved questions</span>
        </div>
    `;

    groups.forEach((group, gi) => {
      const bookPages = group.questions.map(q => q.bookPage).filter(Boolean);
      let rangeLabel = '';
      if (bookPages.length) {
        const lo = Math.min(...bookPages);
        const hi = Math.max(...bookPages);
        rangeLabel = lo === hi ? `Book p.${lo}` : `Book pp.${lo}–${hi}`;
      }
      html += `
        <div class="section-group" id="section_group_${gi}" data-section-name="${group.name}">
          <div class="section-group-header">
            <span class="section-group-name">${group.name}</span>
            <span class="section-group-meta">${group.questions.length} questions${rangeLabel ? ' • ' + rangeLabel : ''}</span>
          </div>
      `;
      group.questions.forEach(q => { html += this.renderQuestionCard(q); });
      html += `</div>`;
    });

    html += `</div>`;
    this.container.innerHTML = html;
    this.bindQuestionEvents();
  }

  renderQuestionCard(q) {
    const isMCQ = q.type === 'mcq';
    let typeLabel = 'Extensive Q';
    let badgeClass = 'erq';
    if (isMCQ) {
      typeLabel = 'MCQ';
      badgeClass = 'mcq';
    } else if (q.type === 'sq') {
      typeLabel = 'Structured Q';
      badgeClass = 'sq';
    } else if (q.type === 'numerical') {
      typeLabel = 'Numerical';
      badgeClass = 'numerical';
    } else if (q.type === 'self') {
      typeLabel = 'Self-Assessment';
      badgeClass = 'self';
    }

    let html = `
      <article class="question-card" id="card_${q.id}" data-qid="${q.id}">
        <div class="question-card-header">
          <div class="question-meta-group">
            <span class="question-type-badge ${badgeClass}">${typeLabel}</span>
            <span class="question-num-tag">${q.type === 'numerical' ? 'Num ' + q.number : 'Q' + q.number}</span>
          </div>
          <div class="card-action-btns">
            <button class="card-icon-btn tts-btn" id="tts_btn_${q.id}" title="Read question & answer aloud" data-action="tts">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
            </button>
            <button class="card-icon-btn stt-btn" id="stt_btn_${q.id}" title="Practice answering by voice" data-action="stt">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>
            </button>
          </div>
        </div>

        <div class="question-content-box">
          <div class="question-text">${q.question}</div>
    `;

    if (q.figure) {
      // Some solutions carry a textual description of the printed figure
      // instead of an image path; show those as a caption rather than a
      // broken image.
      const isImagePath = /^(https?:|\/|data:|\.\/)/.test(q.figure);
      if (isImagePath) {
        html += `
        <div class="question-figure">
          <img src="${q.figure}" alt="Figure for question ${q.number}" loading="lazy" />
        </div>
      `;
      } else {
        html += `
        <div class="question-figure-caption">
          <strong>Figure:</strong> ${q.figure}
        </div>
      `;
      }
    }

    // Render MCQ options if applicable
    if (isMCQ && q.options && q.options.length > 0) {
      html += `<div class="mcq-options-grid" id="options_grid_${q.id}">`;
      q.options.forEach(opt => {
        html += `
          <div class="mcq-option-item" data-opt-key="${opt.key}">
            <span class="mcq-option-letter">(${opt.key})</span>
            <span class="mcq-option-text">${opt.text}</span>
          </div>
        `;
      });
      html += `</div>`;
    }

    // Voice Practice Box (STT)
    html += `
      <div class="stt-practice-container" id="stt_box_${q.id}">
        <div class="stt-header-row">
          <span>Voice Practice Mode (Speak your answer)</span>
          <span class="stt-status-indicator" id="stt_status_${q.id}">Listening...</span>
        </div>
        <div class="stt-transcript-text" id="stt_transcript_${q.id}">Speak into your microphone...</div>
      </div>
    `;

    // Answer Toggle Row
    html += `
      <div class="answer-toggle-row">
        <button class="toggle-answer-btn" id="btn_toggle_${q.id}" data-action="toggle-answer">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
          <span class="toggle-label">Show Answer</span>
        </button>
      </div>

      <div class="answer-expandable-box" id="answer_box_${q.id}">
    `;

    if (isMCQ) {
      html += `
        <div class="correct-badge-banner">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"></polyline></svg>
          <span>Correct Answer: ${q.correctAnswer}</span>
        </div>
      `;
      if (q.explanation) {
        html += `
          <div class="explanation-callout">
            <strong>Scientific Explanation:</strong> ${q.explanation}
          </div>
        `;
      }
    } else {
      html += `
        <div class="answer-body-text">${q.answer}</div>
      `;
      if (q.explanation) {
        html += `
          <div class="explanation-callout">
            <strong>Key Notes & Explanation:</strong> ${q.explanation}
          </div>
        `;
      }
    }

    html += `
        </div>
      </article>
    `;
    return html;
  }

  renderPrepState(chapter) {
    const title = chapter ? `Unit ${chapter.number}: ${chapter.title}` : 'No Unit Selected';
    this.container.innerHTML = `
      <div class="no-solutions-placeholder">
        <div class="placeholder-icon">🛠️</div>
        <h3>${title}</h3>
        <p style="font-size: 0.85rem; color: var(--text-muted); max-width: 320px;">
          Verified solutions for this unit are in preparation. Every question, sub-part and diagram will be added with full worked explanations.
        </p>
        <button class="placeholder-jump-btn" id="btnJumpNextSolved">
          Jump to Next Solved Unit →
        </button>
      </div>
    `;

    const jumpBtn = document.getElementById('btnJumpNextSolved');
    if (jumpBtn) {
      jumpBtn.addEventListener('click', () => {
        window.dispatchEvent(new CustomEvent('request-next-solved-unit', { detail: { fromUnit: chapter ? chapter.number : 0 } }));
      });
    }
  }

  scrollToSection(sectionName) {
    const group = this.container.querySelector(`.section-group[data-section-name="${sectionName}"]`);
    if (group) group.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  bindQuestionEvents() {
    this.currentQuestions.forEach(q => {
      const card = document.getElementById(`card_${q.id}`);
      if (!card) return;

      // Toggle Answer button
      const toggleBtn = card.querySelector('[data-action="toggle-answer"]');
      const answerBox = document.getElementById(`answer_box_${q.id}`);
      if (toggleBtn && answerBox) {
        toggleBtn.addEventListener('click', () => {
          this.toggleAnswerForQuestion(q.id);
        });
      }

      // TTS Button
      const ttsBtn = card.querySelector('[data-action="tts"]');
      if (ttsBtn) {
        ttsBtn.addEventListener('click', () => {
          this.readQuestionAloud(q);
        });
      }

      // STT Button
      const sttBtn = card.querySelector('[data-action="stt"]');
      if (sttBtn) {
        sttBtn.addEventListener('click', () => {
          this.toggleSTTForQuestion(q.id);
        });
      }
    });
  }

  toggleAnswerForQuestion(qid, forceState = null, opts = {}) {
    const card = document.getElementById(`card_${qid}`);
    const toggleBtn = document.getElementById(`btn_toggle_${qid}`);
    const answerBox = document.getElementById(`answer_box_${qid}`);
    if (!toggleBtn || !answerBox) return;

    const q = this.currentQuestions.find(item => item.id === qid);
    const shouldOpen = forceState !== null ? forceState : !answerBox.classList.contains('open');

    if (shouldOpen) {
      answerBox.classList.add('open');
      toggleBtn.classList.add('open');
      toggleBtn.querySelector('.toggle-label').textContent = 'Hide Answer';

      // If MCQ, highlight the correct option item
      if (q && q.type === 'mcq' && q.correctAnswer) {
        const match = q.correctAnswer.match(/\(([a-e])\)/i);
        if (match) {
          const correctKey = match[1].toLowerCase();
          const optEl = card.querySelector(`[data-opt-key="${correctKey}"]`);
          if (optEl) optEl.classList.add('is-correct-revealed');
        }
      }
    } else {
      answerBox.classList.remove('open');
      toggleBtn.classList.remove('open');
      toggleBtn.querySelector('.toggle-label').textContent = 'Show Answer';

      // Remove MCQ option highlight
      card.querySelectorAll('.mcq-option-item').forEach(el => {
        el.classList.remove('is-correct-revealed');
      });
    }

    if (q && this.onAnswerToggle) {
      this.onAnswerToggle(q, shouldOpen, opts);
    }
  }

  toggleAllAnswers(showAll) {
    this.allAnswersVisible = showAll;
    this.currentQuestions.forEach(q => {
      this.toggleAnswerForQuestion(q.id, showAll, { fromBatch: true });
    });
  }

  readQuestionAloud(q) {
    let fullTextToRead = `Question ${q.number}. ${q.question}. `;

    if (q.type === 'mcq') {
      if (q.optionsRaw) {
        fullTextToRead += `Options: ${q.optionsRaw}. `;
      }
      const answerBox = document.getElementById(`answer_box_${q.id}`);
      if (answerBox && answerBox.classList.contains('open')) {
        fullTextToRead += `Correct answer is: ${q.correctAnswer}. ${q.explanation}`;
      }
    } else {
      const answerBox = document.getElementById(`answer_box_${q.id}`);
      if (answerBox && answerBox.classList.contains('open')) {
        fullTextToRead += `Answer: ${q.answer}`;
      }
    }

    speechEngine.speak(fullTextToRead, q.id);
  }

  toggleSTTForQuestion(qid) {
    const sttBox = document.getElementById(`stt_box_${qid}`);
    const sttBtn = document.getElementById(`stt_btn_${qid}`);
    const transcriptEl = document.getElementById(`stt_transcript_${qid}`);
    const statusEl = document.getElementById(`stt_status_${qid}`);

    if (!sttBox) return;

    if (sttBox.classList.contains('open')) {
      sttBox.classList.remove('open');
      sttBtn.classList.remove('listening');
      speechEngine.stopListening();
    } else {
      // Close other STT boxes
      document.querySelectorAll('.stt-practice-container').forEach(el => el.classList.remove('open'));
      document.querySelectorAll('.stt-btn').forEach(el => el.classList.remove('listening'));

      sttBox.classList.add('open');
      sttBtn.classList.add('listening');
      transcriptEl.textContent = "Listening... Speak your answer now.";

      speechEngine.startListening(
        (transcript) => {
          transcriptEl.textContent = `"${transcript}"`;
        },
        () => {
          sttBtn.classList.remove('listening');
          statusEl.textContent = "Finished listening";
        }
      );
    }
  }

  handleTTSStarted(cardId) {
    if (!cardId) return;
    const btn = document.getElementById(`tts_btn_${cardId}`);
    const card = document.getElementById(`card_${cardId}`);
    if (btn) btn.classList.add('playing');
    if (card) card.classList.add('active-reading');
  }

  handleTTSEnded(cardId) {
    if (!cardId) {
      document.querySelectorAll('.tts-btn').forEach(b => b.classList.remove('playing'));
      document.querySelectorAll('.question-card').forEach(c => c.classList.remove('active-reading'));
      return;
    }
    const btn = document.getElementById(`tts_btn_${cardId}`);
    const card = document.getElementById(`card_${cardId}`);
    if (btn) btn.classList.remove('playing');
    if (card) card.classList.remove('active-reading');
  }
}
