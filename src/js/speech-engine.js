/**
 * SubjectZone - Speech Engine (TTS & STT)
 * Cross-platform browser implementation using Web Speech API
 */

class SpeechEngine {
  constructor() {
    this.synth = window.speechSynthesis || null;
    this.voices = [];
    this.selectedVoice = null;
    this.rate = 1.0;
    this.pitch = 1.0;
    this.isPlaying = false;
    this.currentUtterance = null;
    this.activeCardId = null;

    // Speech Recognition (STT)
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition || null;
    this.recognition = SpeechRecognition ? new SpeechRecognition() : null;
    this.isListening = false;

    this.initTTS();
    this.initSTT();
  }

  initTTS() {
    if (!this.synth) {
      console.warn("SpeechSynthesis API not supported in this browser.");
      return;
    }

    const loadVoices = () => {
      this.voices = this.synth.getVoices();
      // Prefer standard English natural voices
      this.selectedVoice = this.voices.find(v => v.lang.startsWith('en') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Samantha') || v.name.includes('David'))) 
                           || this.voices.find(v => v.lang.startsWith('en')) 
                           || this.voices[0];
    };

    loadVoices();
    if (this.synth.onvoiceschanged !== undefined) {
      this.synth.onvoiceschanged = loadVoices;
    }
  }

  initSTT() {
    if (!this.recognition) {
      console.warn("SpeechRecognition API not supported in this browser.");
      return;
    }

    this.recognition.continuous = false;
    this.recognition.interimResults = true;
    this.recognition.lang = 'en-US';
  }

  speak(text, cardId = null, onEndCallback = null) {
    if (!this.synth) {
      alert("Text-to-Speech is not supported in this browser.");
      return;
    }

    // If currently speaking this card, stop it (toggle behavior)
    if (this.isPlaying && this.activeCardId === cardId) {
      this.stop();
      return;
    }

    this.stop();

    if (!text || text.trim() === '') return;

    // Clean text of extra markdown formatting
    const cleanedText = text
      .replace(/\(a\)|\(b\)|\(c\)|\(d\)/gi, '')
      .replace(/[#*_`]/g, '')
      .trim();

    this.currentUtterance = new SpeechSynthesisUtterance(cleanedText);
    if (this.selectedVoice) {
      this.currentUtterance.voice = this.selectedVoice;
    }
    this.currentUtterance.rate = this.rate;
    this.currentUtterance.pitch = this.pitch;

    this.activeCardId = cardId;
    this.isPlaying = true;

    // UI feedback event dispatch
    window.dispatchEvent(new CustomEvent('tts-started', { detail: { cardId } }));

    this.currentUtterance.onend = () => {
      this.isPlaying = false;
      this.activeCardId = null;
      window.dispatchEvent(new CustomEvent('tts-ended', { detail: { cardId } }));
      if (onEndCallback) onEndCallback();
    };

    this.currentUtterance.onerror = (e) => {
      console.error("TTS Error:", e);
      this.isPlaying = false;
      this.activeCardId = null;
      window.dispatchEvent(new CustomEvent('tts-ended', { detail: { cardId } }));
    };

    this.synth.speak(this.currentUtterance);
  }

  stop() {
    if (this.synth && this.isPlaying) {
      this.synth.cancel();
      this.isPlaying = false;
      const prevId = this.activeCardId;
      this.activeCardId = null;
      window.dispatchEvent(new CustomEvent('tts-ended', { detail: { cardId: prevId } }));
    }
  }

  setRate(newRate) {
    this.rate = Math.max(0.5, Math.min(2.0, parseFloat(newRate)));
  }

  setVoice(voiceIndex) {
    if (this.voices[voiceIndex]) {
      this.selectedVoice = this.voices[voiceIndex];
    }
  }

  // Speech to Text (STT)
  startListening(onTranscript, onEnd) {
    if (!this.recognition) {
      alert("Speech-to-Text is not supported on this browser. Try Google Chrome or Microsoft Edge.");
      if (onEnd) onEnd();
      return;
    }

    if (this.isListening) {
      this.stopListening();
      return;
    }

    this.isListening = true;

    this.recognition.onresult = (event) => {
      let finalTranscript = '';
      for (let i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
          finalTranscript += event.results[i][0].transcript;
        } else {
          finalTranscript += event.results[i][0].transcript;
        }
      }
      if (onTranscript) onTranscript(finalTranscript);
    };

    this.recognition.onerror = (err) => {
      console.error("STT Error:", err);
      this.isListening = false;
      if (onEnd) onEnd();
    };

    this.recognition.onend = () => {
      this.isListening = false;
      if (onEnd) onEnd();
    };

    try {
      this.recognition.start();
    } catch (e) {
      console.error("Recognition start failed:", e);
      this.isListening = false;
      if (onEnd) onEnd();
    }
  }

  stopListening() {
    if (this.recognition && this.isListening) {
      this.recognition.stop();
      this.isListening = false;
    }
  }
}

export const speechEngine = new SpeechEngine();
