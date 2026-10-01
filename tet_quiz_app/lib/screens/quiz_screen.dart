import 'dart:async';
import 'package:flutter/material.dart';
import '../models/question.dart';
import '../models/quiz_session.dart';
import '../models/subject.dart';
import '../services/question_repository.dart';
import '../services/storage_service.dart';
import '../widgets/hint_tip_widget.dart';
import '../widgets/question_palette_sheet.dart';
import 'result_screen.dart';

class QuizScreen extends StatefulWidget {
  final List<Question> initialQuestions;
  final String quizTitle;
  final bool isGrandTest;
  final String? subjectId;
  final int? questionCount;

  const QuizScreen({
    super.key,
    required this.initialQuestions,
    required this.quizTitle,
    this.isGrandTest = false,
    this.subjectId,
    this.questionCount,
  });

  @override
  State<QuizScreen> createState() => _QuizScreenState();
}

class _QuizScreenState extends State<QuizScreen> with WidgetsBindingObserver {
  final StorageService _storage = StorageService();
  final QuestionRepository _repo = QuestionRepository();

  late List<QuizQuestionState> _questionStates;
  int _currentIndex = 0;
  late final ScrollController _scrollController;
  late final ScrollController _sectionTabScrollController;

  // Timer
  Timer? _timer;
  int _elapsedSeconds = 0;
  bool _isTimerPaused = false;

  // Instant Feedback (for Subject Level Practice only, ON by default)
  bool _isInstantFeedbackOn = true;

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
    _scrollController = ScrollController();
    _sectionTabScrollController = ScrollController();
    _initQuiz(widget.initialQuestions);
    _startTimer();
  }

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    if (state == AppLifecycleState.paused || state == AppLifecycleState.inactive) {
      _pauseTimer();
    } else if (state == AppLifecycleState.resumed) {
      _resumeTimer();
    }
  }

  void _initQuiz(List<Question> questions) {
    _questionStates = questions
        .map((q) => QuizQuestionState(
              question: q,
              showHint: false,
              showMemoryTip: false,
              showAnswer: false,
            ))
        .toList();
    _currentIndex = 0;
    _elapsedSeconds = 0;
    _isTimerPaused = false;
  }

  void _startTimer() {
    _timer?.cancel();
    _timer = Timer.periodic(const Duration(seconds: 1), (t) {
      if (mounted && !_isTimerPaused) {
        setState(() => _elapsedSeconds++);
      }
    });
  }

  void _pauseTimer() {
    if (!_isTimerPaused && mounted) {
      setState(() => _isTimerPaused = true);
    }
  }

  void _resumeTimer() {
    if (_isTimerPaused && mounted) {
      setState(() => _isTimerPaused = false);
    }
  }

  void _toggleTimerPause() {
    if (_isTimerPaused) {
      _resumeTimer();
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Timer Resumed ▶'),
          duration: Duration(milliseconds: 800),
        ),
      );
    } else {
      _pauseTimer();
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Timer Paused ⏸'),
          duration: Duration(milliseconds: 800),
        ),
      );
    }
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    _timer?.cancel();
    _scrollController.dispose();
    _sectionTabScrollController.dispose();
    super.dispose();
  }

  String get _formattedTime {
    final m = _elapsedSeconds ~/ 60;
    final s = _elapsedSeconds % 60;
    return '${m.toString().padLeft(2, '0')}:${s.toString().padLeft(2, '0')}';
  }

  // --- Sections for Grand Test ---
  List<_SectionInfo> _getSections() {
    if (!widget.isGrandTest) return [];

    final Map<String, _SectionInfo> map = {};
    for (int i = 0; i < _questionStates.length; i++) {
      final q = _questionStates[i];
      final sid = q.question.subjectId;
      if (!map.containsKey(sid)) {
        final sub = Subject.findById(sid);
        map[sid] = _SectionInfo(
          subjectId: sid,
          title: sub?.title ?? q.question.subjectName,
          shortTitle: _getShortTitle(sid),
          startIndex: i,
          color: sub?.primaryColor ?? const Color(0xFF4F46E5),
        );
      }
      map[sid]!.totalCount++;
      if (q.isAttempted) {
        map[sid]!.attemptedCount++;
      }
    }
    return map.values.toList();
  }

  String _getShortTitle(String subjectId) {
    switch (subjectId) {
      case 'cdp':
        return 'CDP';
      case 'telugu':
        return 'Telugu';
      case 'english':
        return 'English';
      case 'maths':
        return 'Maths';
      case 'physics':
        return 'Physics';
      case 'biology':
        return 'Biology';
      default:
        return 'Section';
    }
  }

  int _getCurrentSectionIndex(List<_SectionInfo> sections) {
    if (sections.isEmpty) return 0;
    for (int i = sections.length - 1; i >= 0; i--) {
      if (_currentIndex >= sections[i].startIndex) {
        return i;
      }
    }
    return 0;
  }

  void _goToQuestion(int index) {
    if (index >= 0 && index < _questionStates.length) {
      setState(() => _currentIndex = index);
      if (_scrollController.hasClients) {
        _scrollController.animateTo(
          0,
          duration: const Duration(milliseconds: 200),
          curve: Curves.easeOut,
        );
      }
    }
  }

  void _goToSection(_SectionInfo section) {
    _goToQuestion(section.startIndex);
  }

  void _selectOption(int optionKey) {
    setState(() {
      final current = _questionStates[_currentIndex];
      if (current.selectedOptionKey == optionKey) {
        // Toggle off if clicked again
        current.selectedOptionKey = null;
      } else {
        current.selectedOptionKey = optionKey;
      }
    });
  }

  void _toggleReview() {
    setState(() {
      _questionStates[_currentIndex].isMarkedForReview =
          !_questionStates[_currentIndex].isMarkedForReview;
    });
  }

  void _toggleShowAnswer() {
    setState(() {
      _questionStates[_currentIndex].showAnswer =
          !_questionStates[_currentIndex].showAnswer;
    });
  }

  void _openPalette() {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (ctx) => QuestionPaletteSheet(
        questions: _questionStates,
        currentIndex: _currentIndex,
        onSelectQuestion: _goToQuestion,
        onSubmitTest: _confirmSubmit,
      ),
    );
  }

  void _confirmSubmit() {
    final answered = _questionStates.where((q) => q.isAttempted).length;
    final unattempted = _questionStates.length - answered;
    final review = _questionStates.where((q) => q.isMarkedForReview).length;

    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('Submit Quiz?'),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('Are you sure you want to finish the quiz?'),
            const SizedBox(height: 14),
            _buildSummaryRow('Total Questions:', '${_questionStates.length}'),
            _buildSummaryRow('Answered:', '$answered', color: const Color(0xFF10B981)),
            _buildSummaryRow('Marked for Review:', '$review', color: const Color(0xFF8B5CF6)),
            _buildSummaryRow('Unanswered:', '$unattempted', color: const Color(0xFFEF4444)),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(ctx),
            child: const Text('Cancel / కొనసాగించండి'),
          ),
          ElevatedButton(
            onPressed: () {
              Navigator.pop(ctx);
              _finishQuiz();
            },
            child: const Text('Submit Now'),
          ),
        ],
      ),
    );
  }

  Widget _buildSummaryRow(String label, String value, {Color? color}) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 2),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(label, style: const TextStyle(fontSize: 14)),
          Text(
            value,
            style: TextStyle(
              fontSize: 14,
              fontWeight: FontWeight.bold,
              color: color,
            ),
          ),
        ],
      ),
    );
  }

  Future<void> _finishQuiz() async {
    _timer?.cancel();

    int correctCount = 0;
    int wrongCount = 0;
    int attemptedCount = 0;

    final Map<String, SubjectStat> subjectStats = {};

    for (final state in _questionStates) {
      final q = state.question;
      final sid = q.subjectId;

      if (!subjectStats.containsKey(sid)) {
        subjectStats[sid] = SubjectStat(
          subjectId: sid,
          subjectTitle: q.subjectName,
        );
      }

      final stat = subjectStats[sid]!;
      stat.total++;

      if (state.isAttempted) {
        attemptedCount++;
        stat.attempted++;
        if (state.isCorrect) {
          correctCount++;
          stat.correct++;
        } else {
          wrongCount++;
          stat.wrong++;
        }
      }
    }

    final total = _questionStates.length;
    final unattempted = total - attemptedCount;
    final scorePct = total > 0 ? (correctCount / total) * 100 : 0.0;

    final result = QuizResult(
      quizTitle: widget.quizTitle,
      isGrandTest: widget.isGrandTest,
      totalQuestions: total,
      attemptedCount: attemptedCount,
      correctCount: correctCount,
      wrongCount: wrongCount,
      unattemptedCount: unattempted,
      elapsedSeconds: _elapsedSeconds,
      scorePercentage: scorePct,
      subjectStats: subjectStats,
      questions: _questionStates,
      completedAt: DateTime.now(),
    );

    await _storage.saveQuizResult(
      title: widget.quizTitle,
      score: correctCount,
      total: total,
      percentage: scorePct,
      timeSeconds: _elapsedSeconds,
      isGrandTest: widget.isGrandTest,
    );

    if (!mounted) return;

    Navigator.pushReplacement(
      context,
      MaterialPageRoute(
        builder: (ctx) => ResultScreen(
          result: result,
          onRestart: () => _restartQuiz(),
        ),
      ),
    );
  }

  Future<void> _restartQuiz() async {
    Navigator.of(context).popUntil((route) => route.isFirst);

    List<Question> newQuestions;
    if (widget.isGrandTest) {
      newQuestions = await _repo.generateGrandMockTest();
    } else if (widget.subjectId != null) {
      newQuestions = await _repo.generateSubjectQuiz(
        widget.subjectId!,
        count: widget.questionCount,
      );
    } else {
      newQuestions = List<Question>.from(widget.initialQuestions)..shuffle();
    }

    if (!mounted) return;

    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (ctx) => QuizScreen(
          initialQuestions: newQuestions,
          quizTitle: widget.quizTitle,
          isGrandTest: widget.isGrandTest,
          subjectId: widget.subjectId,
          questionCount: widget.questionCount,
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final isDark = theme.brightness == Brightness.dark;

    if (_questionStates.isEmpty) {
      return const Scaffold(body: Center(child: Text('No questions available')));
    }

    final currentState = _questionStates[_currentIndex];
    final currentQ = currentState.question;
    final subject = Subject.findById(currentQ.subjectId);
    final isBookmarked = _storage.isBookmarked(currentQ);
    final sections = _getSections();
    final activeSectionIndex = _getCurrentSectionIndex(sections);

    // Subject practice feedback visibility
    final isSubjectPractice = !widget.isGrandTest;
    final showAnswerRevealed = isSubjectPractice &&
        ((_isInstantFeedbackOn && currentState.isAttempted) || currentState.showAnswer);

    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: const Icon(Icons.arrow_back_rounded),
          onPressed: _showExitDialog,
        ),
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              'Q ${_currentIndex + 1} of ${_questionStates.length}',
              style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
            ),
            Text(
              widget.quizTitle,
              style: TextStyle(
                fontSize: 12,
                color: isDark ? Colors.white60 : const Color(0xFF64748B),
                fontWeight: FontWeight.normal,
              ),
            ),
          ],
        ),
        actions: [
          // Timer badge (clickable to pause/resume)
          InkWell(
            onTap: _toggleTimerPause,
            borderRadius: BorderRadius.circular(8),
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
              margin: const EdgeInsets.symmetric(vertical: 10),
              decoration: BoxDecoration(
                color: _isTimerPaused
                    ? Colors.amber.withValues(alpha: 0.2)
                    : (isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0)),
                borderRadius: BorderRadius.circular(8),
                border: _isTimerPaused
                    ? Border.all(color: Colors.amber, width: 1)
                    : null,
              ),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Icon(
                    _isTimerPaused ? Icons.pause_circle_rounded : Icons.timer_outlined,
                    size: 16,
                    color: _isTimerPaused ? Colors.amber[800] : null,
                  ),
                  const SizedBox(width: 4),
                  Text(
                    _formattedTime,
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 13,
                      color: _isTimerPaused ? Colors.amber[800] : null,
                    ),
                  ),
                ],
              ),
            ),
          ),
          // Bookmark button
          IconButton(
            icon: Icon(
              isBookmarked ? Icons.bookmark_rounded : Icons.bookmark_border_rounded,
              color: isBookmarked ? Colors.amber : null,
            ),
            tooltip: 'Bookmark Question',
            onPressed: () async {
              await _storage.toggleBookmark(currentQ);
              setState(() {});
            },
          ),
          // Palette Grid button
          IconButton(
            icon: const Icon(Icons.grid_view_rounded),
            tooltip: 'Question Palette',
            onPressed: _openPalette,
          ),
        ],
      ),
      body: Column(
        children: [
          // Section Shift Bar (Only for Main Grand Mock Test - 150 questions)
          if (widget.isGrandTest && sections.isNotEmpty)
            _buildSectionBar(sections, activeSectionIndex, isDark),

          // Instant Answer Check Toggle (Only in Subject Level Practice)
          if (isSubjectPractice)
            _buildSubjectFeedbackBar(isDark),

          // Overall Progress Bar
          LinearProgressIndicator(
            value: (_currentIndex + 1) / _questionStates.length,
            minHeight: 3.5,
            backgroundColor: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0),
            valueColor: AlwaysStoppedAnimation<Color>(
              subject?.primaryColor ?? theme.colorScheme.primary,
            ),
          ),

          // Scrollable Question Content
          Expanded(
            child: SingleChildScrollView(
              controller: _scrollController,
              padding: const EdgeInsets.fromLTRB(16, 14, 16, 24),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  // Subject Tag & Review Indicator
                  Row(
                    children: [
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                        decoration: BoxDecoration(
                          color: (subject?.primaryColor ?? theme.colorScheme.primary)
                              .withValues(alpha: 0.15),
                          borderRadius: BorderRadius.circular(8),
                        ),
                        child: Text(
                          subject?.title ?? currentQ.subjectName,
                          style: TextStyle(
                            color: subject?.primaryColor ?? theme.colorScheme.primary,
                            fontWeight: FontWeight.bold,
                            fontSize: 12,
                          ),
                        ),
                      ),
                      const Spacer(),
                      if (currentState.isMarkedForReview)
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                          decoration: BoxDecoration(
                            color: const Color(0xFFEDE9FE),
                            borderRadius: BorderRadius.circular(6),
                          ),
                          child: const Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Icon(Icons.flag_rounded, size: 14, color: Color(0xFF7C3AED)),
                              SizedBox(width: 4),
                              Text(
                                'Review',
                                style: TextStyle(
                                  color: Color(0xFF7C3AED),
                                  fontSize: 11,
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                            ],
                          ),
                        ),
                    ],
                  ),
                  const SizedBox(height: 12),

                  // Question Card
                  Card(
                    elevation: 0,
                    margin: EdgeInsets.zero,
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(16),
                      side: BorderSide(
                        color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0),
                      ),
                    ),
                    child: Padding(
                      padding: const EdgeInsets.all(18),
                      child: Text(
                        currentQ.question,
                        style: theme.textTheme.titleMedium?.copyWith(
                          fontSize: 16.5,
                          height: 1.5,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                    ),
                  ),

                  const SizedBox(height: 16),

                  // Options List
                  ...currentQ.options.map((opt) {
                    final isSelected = currentState.selectedOptionKey == opt.key;
                    final isCorrect = opt.key == currentQ.answer;

                    Color bgColor;
                    Color borderColor;
                    Color textColor;
                    Widget? trailingIcon;

                    if (showAnswerRevealed) {
                      // Subject level practice with feedback / answer revealed
                      if (isCorrect) {
                        bgColor = isDark ? const Color(0xFF064E3B) : const Color(0xFFD1FAE5);
                        borderColor = const Color(0xFF10B981);
                        textColor = isDark ? const Color(0xFF6EE7B7) : const Color(0xFF065F46);
                        trailingIcon = const Icon(Icons.check_circle_rounded, color: Color(0xFF10B981), size: 20);
                      } else if (isSelected && !isCorrect) {
                        bgColor = isDark ? const Color(0xFF450A0A) : const Color(0xFFFEE2E2);
                        borderColor = const Color(0xFFEF4444);
                        textColor = isDark ? const Color(0xFFFCA5A5) : const Color(0xFF991B1B);
                        trailingIcon = const Icon(Icons.cancel_rounded, color: Color(0xFFEF4444), size: 20);
                      } else {
                        bgColor = isDark ? const Color(0xFF1E293B) : Colors.white;
                        borderColor = isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0);
                        textColor = isDark ? Colors.white70 : const Color(0xFF334155);
                      }
                    } else {
                      // Normal mode (or Main Grand Test where answers are strictly hidden)
                      if (isSelected) {
                        bgColor = (subject?.primaryColor ?? theme.colorScheme.primary).withValues(alpha: 0.12);
                        borderColor = subject?.primaryColor ?? theme.colorScheme.primary;
                        textColor = isDark ? Colors.white : const Color(0xFF0F172A);
                        trailingIcon = Icon(
                          Icons.check_circle_rounded,
                          color: subject?.primaryColor ?? theme.colorScheme.primary,
                          size: 20,
                        );
                      } else {
                        bgColor = isDark ? const Color(0xFF1E293B) : Colors.white;
                        borderColor = isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0);
                        textColor = isDark ? Colors.white70 : const Color(0xFF334155);
                      }
                    }

                    return Padding(
                      padding: const EdgeInsets.only(bottom: 10),
                      child: Material(
                        color: Colors.transparent,
                        child: InkWell(
                          borderRadius: BorderRadius.circular(14),
                          onTap: () => _selectOption(opt.key),
                          child: Container(
                            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
                            decoration: BoxDecoration(
                              color: bgColor,
                              borderRadius: BorderRadius.circular(14),
                              border: Border.all(
                                color: borderColor,
                                width: (isSelected || (showAnswerRevealed && isCorrect)) ? 2 : 1,
                              ),
                            ),
                            child: Row(
                              children: [
                                Container(
                                  width: 32,
                                  height: 32,
                                  decoration: BoxDecoration(
                                    color: (showAnswerRevealed && isCorrect)
                                        ? const Color(0xFF10B981)
                                        : (showAnswerRevealed && isSelected && !isCorrect
                                            ? const Color(0xFFEF4444)
                                            : (isSelected
                                                ? (subject?.primaryColor ?? theme.colorScheme.primary)
                                                : Colors.transparent)),
                                    shape: BoxShape.circle,
                                    border: Border.all(
                                      color: borderColor,
                                      width: 1.5,
                                    ),
                                  ),
                                  alignment: Alignment.center,
                                  child: Text(
                                    '${opt.key}',
                                    style: TextStyle(
                                      fontWeight: FontWeight.bold,
                                      fontSize: 14,
                                      color: (isSelected || (showAnswerRevealed && isCorrect))
                                          ? Colors.white
                                          : (isDark ? Colors.white70 : const Color(0xFF334155)),
                                    ),
                                  ),
                                ),
                                const SizedBox(width: 12),
                                Expanded(
                                  child: Text(
                                    opt.text,
                                    style: TextStyle(
                                      fontSize: 15,
                                      fontWeight: isSelected ? FontWeight.w600 : FontWeight.w400,
                                      color: textColor,
                                    ),
                                  ),
                                ),
                                ?trailingIcon,
                              ],
                            ),
                          ),
                        ),
                      ),
                    );
                  }),

                  // Subject Practice: Answer Feedback Banner + Show Answer Button
                  if (isSubjectPractice) ...[
                    const SizedBox(height: 6),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        // Show Answer Button
                        TextButton.icon(
                          onPressed: _toggleShowAnswer,
                          icon: Icon(
                            currentState.showAnswer ? Icons.visibility_off_rounded : Icons.visibility_rounded,
                            size: 18,
                            color: const Color(0xFF0284C7),
                          ),
                          label: Text(
                            currentState.showAnswer ? 'Hide Answer' : 'Show Answer (సమాధానం)',
                            style: const TextStyle(
                              color: Color(0xFF0284C7),
                              fontWeight: FontWeight.bold,
                              fontSize: 13,
                            ),
                          ),
                        ),
                        // Clear Selection button
                        if (currentState.isAttempted)
                          TextButton.icon(
                            onPressed: () {
                              setState(() => currentState.selectedOptionKey = null);
                            },
                            icon: const Icon(Icons.clear_rounded, size: 16),
                            label: const Text('Clear response'),
                            style: TextButton.styleFrom(
                              foregroundColor: isDark ? Colors.white60 : const Color(0xFF64748B),
                            ),
                          ),
                      ],
                    ),

                    // Correct/Wrong Announcement Banner
                    if (showAnswerRevealed)
                      Container(
                        margin: const EdgeInsets.only(top: 8, bottom: 4),
                        padding: const EdgeInsets.all(12),
                        decoration: BoxDecoration(
                          color: currentState.isCorrect
                              ? const Color(0xFF10B981).withValues(alpha: 0.12)
                              : const Color(0xFFEF4444).withValues(alpha: 0.12),
                          borderRadius: BorderRadius.circular(10),
                          border: Border.all(
                            color: currentState.isCorrect
                                ? const Color(0xFF10B981)
                                : const Color(0xFFEF4444),
                            width: 1.2,
                          ),
                        ),
                        child: Row(
                          children: [
                            Icon(
                              currentState.isCorrect
                                  ? Icons.check_circle_rounded
                                  : Icons.cancel_rounded,
                              color: currentState.isCorrect
                                  ? const Color(0xFF10B981)
                                  : const Color(0xFFEF4444),
                              size: 20,
                            ),
                            const SizedBox(width: 8),
                            Expanded(
                              child: Text(
                                currentState.isCorrect
                                    ? 'Correct Answer! (సరైన సమాధానం)'
                                    : 'Incorrect. Correct Option is (${currentQ.answer})',
                                style: TextStyle(
                                  fontWeight: FontWeight.bold,
                                  fontSize: 13.5,
                                  color: currentState.isCorrect
                                      ? (isDark ? const Color(0xFF6EE7B7) : const Color(0xFF065F46))
                                      : (isDark ? const Color(0xFFFCA5A5) : const Color(0xFF991B1B)),
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                  ],

                  // In Grand Test: Simple Clear Response button
                  if (widget.isGrandTest && currentState.isAttempted)
                    Align(
                      alignment: Alignment.centerRight,
                      child: TextButton.icon(
                        onPressed: () {
                          setState(() => currentState.selectedOptionKey = null);
                        },
                        icon: const Icon(Icons.clear_rounded, size: 16),
                        label: const Text('Clear response'),
                        style: TextButton.styleFrom(
                          foregroundColor: isDark ? Colors.white60 : const Color(0xFF64748B),
                        ),
                      ),
                    ),

                  // Hints & Memory Tips Section (Below each question, accessible on click)
                  HintTipWidget(
                    hint: currentQ.hint,
                    memoryTip: currentQ.memoryTip,
                    initialShowHint: currentState.showHint,
                    initialShowTip: currentState.showMemoryTip,
                    onHintToggled: (val) => currentState.showHint = val,
                    onTipToggled: (val) => currentState.showMemoryTip = val,
                  ),
                ],
              ),
            ),
          ),

          // Bottom Navigation Bar
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
            decoration: BoxDecoration(
              color: isDark ? const Color(0xFF1E293B) : Colors.white,
              border: Border(
                top: BorderSide(
                  color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0),
                ),
              ),
            ),
            child: SafeArea(
              child: Row(
                children: [
                  // Previous button
                  IconButton.outlined(
                    onPressed: _currentIndex > 0
                        ? () => _goToQuestion(_currentIndex - 1)
                        : null,
                    icon: const Icon(Icons.chevron_left_rounded),
                    tooltip: 'Previous Question',
                  ),
                  const SizedBox(width: 8),

                  // Mark for Review toggle
                  Expanded(
                    child: OutlinedButton.icon(
                      style: OutlinedButton.styleFrom(
                        side: BorderSide(
                          color: currentState.isMarkedForReview
                              ? const Color(0xFF8B5CF6)
                              : (isDark ? const Color(0xFF475569) : const Color(0xFFCBD5E1)),
                        ),
                        backgroundColor: currentState.isMarkedForReview
                            ? const Color(0xFF8B5CF6).withValues(alpha: 0.1)
                            : Colors.transparent,
                        foregroundColor: currentState.isMarkedForReview
                            ? const Color(0xFF8B5CF6)
                            : null,
                      ),
                      onPressed: _toggleReview,
                      icon: Icon(
                        currentState.isMarkedForReview
                            ? Icons.flag_rounded
                            : Icons.flag_outlined,
                        size: 18,
                      ),
                      label: Text(
                        currentState.isMarkedForReview ? 'Reviewing' : 'Review',
                        style: const TextStyle(fontSize: 13),
                      ),
                    ),
                  ),
                  const SizedBox(width: 8),

                  // Next or Submit
                  if (_currentIndex < _questionStates.length - 1)
                    Expanded(
                      child: ElevatedButton.icon(
                        onPressed: () => _goToQuestion(_currentIndex + 1),
                        icon: const Icon(Icons.chevron_right_rounded),
                        label: const Text('Next'),
                      ),
                    )
                  else
                    Expanded(
                      child: ElevatedButton.icon(
                        style: ElevatedButton.styleFrom(
                          backgroundColor: const Color(0xFF10B981),
                        ),
                        onPressed: _confirmSubmit,
                        icon: const Icon(Icons.check_rounded),
                        label: const Text('Submit'),
                      ),
                    ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  // --- Sticky Section Tab Bar for Grand Mock Test ---
  Widget _buildSectionBar(List<_SectionInfo> sections, int activeIndex, bool isDark) {
    return Container(
      height: 48,
      decoration: BoxDecoration(
        color: isDark ? const Color(0xFF0F172A) : const Color(0xFFF8FAFC),
        border: Border(
          bottom: BorderSide(
            color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0),
          ),
        ),
      ),
      child: ListView.builder(
        controller: _sectionTabScrollController,
        scrollDirection: Axis.horizontal,
        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
        itemCount: sections.length,
        itemBuilder: (context, index) {
          final s = sections[index];
          final isActive = index == activeIndex;
          final pct = s.percentAttempted;

          return Padding(
            padding: const EdgeInsets.only(right: 8),
            child: Material(
              color: Colors.transparent,
              child: InkWell(
                borderRadius: BorderRadius.circular(20),
                onTap: () => _goToSection(s),
                child: AnimatedContainer(
                  duration: const Duration(milliseconds: 200),
                  padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
                  decoration: BoxDecoration(
                    color: isActive
                        ? s.color.withValues(alpha: 0.18)
                        : (isDark ? const Color(0xFF1E293B) : Colors.white),
                    borderRadius: BorderRadius.circular(20),
                    border: Border.all(
                      color: isActive
                          ? s.color
                          : (isDark ? const Color(0xFF334155) : const Color(0xFFCBD5E1)),
                      width: isActive ? 1.6 : 1,
                    ),
                  ),
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Container(
                        width: 8,
                        height: 8,
                        decoration: BoxDecoration(
                          color: s.color,
                          shape: BoxShape.circle,
                        ),
                      ),
                      const SizedBox(width: 6),
                      Text(
                        s.shortTitle,
                        style: TextStyle(
                          fontSize: 12.5,
                          fontWeight: isActive ? FontWeight.bold : FontWeight.w600,
                          color: isActive ? s.color : null,
                        ),
                      ),
                      const SizedBox(width: 6),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 1),
                        decoration: BoxDecoration(
                          color: pct == 100
                              ? const Color(0xFF10B981).withValues(alpha: 0.2)
                              : (isDark ? const Color(0xFF334155) : const Color(0xFFF1F5F9)),
                          borderRadius: BorderRadius.circular(10),
                        ),
                        child: Text(
                          '$pct%',
                          style: TextStyle(
                            fontSize: 10.5,
                            fontWeight: FontWeight.bold,
                            color: pct == 100
                                ? const Color(0xFF10B981)
                                : (isDark ? Colors.white70 : const Color(0xFF475569)),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          );
        },
      ),
    );
  }

  // --- Sub-header for Subject Practice: Instant Feedback Toggle ---
  Widget _buildSubjectFeedbackBar(bool isDark) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 6),
      decoration: BoxDecoration(
        color: isDark ? const Color(0xFF1E293B) : const Color(0xFFF8FAFC),
        border: Border(
          bottom: BorderSide(
            color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0),
          ),
        ),
      ),
      child: Row(
        children: [
          Icon(
            Icons.speed_rounded,
            size: 16,
            color: _isInstantFeedbackOn ? const Color(0xFF10B981) : Colors.grey,
          ),
          const SizedBox(width: 6),
          Expanded(
            child: Text(
              'Instant Answer Check (తక్షణ సరిచూపు)',
              style: TextStyle(
                fontSize: 12,
                fontWeight: FontWeight.w600,
                color: isDark ? Colors.white70 : const Color(0xFF475569),
              ),
            ),
          ),
          Switch(
            value: _isInstantFeedbackOn,
            activeTrackColor: const Color(0xFF10B981),
            activeThumbColor: Colors.white,
            materialTapTargetSize: MaterialTapTargetSize.shrinkWrap,
            onChanged: (val) {
              setState(() => _isInstantFeedbackOn = val);
            },
          ),
        ],
      ),
    );
  }

  void _showExitDialog() {
    _pauseTimer();
    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('Leave Quiz?'),
        content: const Text(
          'Timer is paused. Do you want to continue the quiz, submit now, or leave?',
        ),
        actions: [
          TextButton(
            onPressed: () {
              Navigator.pop(ctx);
              _resumeTimer();
            },
            child: const Text('Continue Quiz'),
          ),
          TextButton(
            onPressed: () {
              Navigator.pop(ctx);
              Navigator.pop(context);
            },
            child: const Text('Leave', style: TextStyle(color: Colors.red)),
          ),
          ElevatedButton(
            onPressed: () {
              Navigator.pop(ctx);
              _finishQuiz();
            },
            child: const Text('Submit Quiz'),
          ),
        ],
      ),
    );
  }
}

class _SectionInfo {
  final String subjectId;
  final String title;
  final String shortTitle;
  final int startIndex;
  final Color color;
  int totalCount = 0;
  int attemptedCount = 0;

  _SectionInfo({
    required this.subjectId,
    required this.title,
    required this.shortTitle,
    required this.startIndex,
    required this.color,
  });

  int get percentAttempted =>
      totalCount > 0 ? ((attemptedCount / totalCount) * 100).round() : 0;
}
