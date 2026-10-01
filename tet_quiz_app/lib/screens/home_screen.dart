import 'package:flutter/material.dart';
import '../models/question.dart';
import '../models/subject.dart';
import '../services/question_repository.dart';
import '../services/storage_service.dart';
import 'quiz_screen.dart';
import 'bookmarks_screen.dart';

class HomeScreen extends StatefulWidget {
  final ValueChanged<bool> onThemeChanged;
  final bool isDarkMode;

  const HomeScreen({
    super.key,
    required this.onThemeChanged,
    required this.isDarkMode,
  });

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final QuestionRepository _repo = QuestionRepository();
  final StorageService _storage = StorageService();

  bool _isLoading = false;
  int _bookmarkCount = 0;
  List<Map<String, dynamic>> _history = [];

  @override
  void initState() {
    super.initState();
    _loadInitialData();
  }

  Future<void> _loadInitialData() async {
    await _storage.init();
    await _repo.initialize();
    _updateStats();
  }

  void _updateStats() {
    if (mounted) {
      setState(() {
        _bookmarkCount = _storage.getBookmarkedKeys().length;
        _history = _storage.getHistory();
      });
    }
  }

  Future<void> _startGrandMockTest() async {
    setState(() => _isLoading = true);
    try {
      final List<Question> questions = await _repo.generateGrandMockTest();
      if (!mounted) return;
      setState(() => _isLoading = false);

      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (ctx) => QuizScreen(
            initialQuestions: questions,
            quizTitle: 'Grand Mock Test (150 Questions)',
            isGrandTest: true,
          ),
        ),
      ).then((_) => _updateStats());
    } catch (e) {
      if (mounted) {
        setState(() => _isLoading = false);
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Error loading test: $e')),
        );
      }
    }
  }

  Future<void> _startSubjectQuiz(Subject subject, int questionCount) async {
    setState(() => _isLoading = true);
    try {
      final List<Question> questions = await _repo.generateSubjectQuiz(
        subject.id,
        count: questionCount > 0 ? questionCount : null,
      );
      if (!mounted) return;
      setState(() => _isLoading = false);

      final title = questionCount > 0
          ? '${subject.title} ($questionCount Qs)'
          : '${subject.title} (All ${questions.length} Qs)';

      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (ctx) => QuizScreen(
            initialQuestions: questions,
            quizTitle: title,
            isGrandTest: false,
            subjectId: subject.id,
            questionCount: questionCount > 0 ? questionCount : null,
          ),
        ),
      ).then((_) => _updateStats());
    } catch (e) {
      if (mounted) {
        setState(() => _isLoading = false);
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Error loading subject questions: $e')),
        );
      }
    }
  }

  void _showSubjectOptions(Subject subject) {
    showModalBottomSheet(
      context: context,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
      ),
      builder: (ctx) {
        final theme = Theme.of(ctx);
        final isDark = theme.brightness == Brightness.dark;

        return Padding(
          padding: const EdgeInsets.fromLTRB(20, 16, 20, 24),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Center(
                child: Container(
                  width: 40,
                  height: 4,
                  decoration: BoxDecoration(
                    color: isDark ? Colors.white24 : Colors.black12,
                    borderRadius: BorderRadius.circular(2),
                  ),
                ),
              ),
              const SizedBox(height: 16),
              Row(
                children: [
                  Container(
                    padding: const EdgeInsets.all(10),
                    decoration: BoxDecoration(
                      color: subject.primaryColor.withValues(alpha: 0.15),
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Icon(subject.icon, color: subject.primaryColor, size: 28),
                  ),
                  const SizedBox(width: 14),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          subject.title,
                          style: theme.textTheme.titleMedium?.copyWith(
                            fontWeight: FontWeight.bold,
                            fontSize: 17,
                          ),
                        ),
                        Text(
                          subject.teluguTitle,
                          style: TextStyle(
                            fontSize: 13,
                            color: isDark ? Colors.white60 : const Color(0xFF64748B),
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 16),
              Text(
                'Select Question Count (ప్రశ్నల సంఖ్య ఎంచుకోండి):',
                style: theme.textTheme.bodyMedium?.copyWith(fontWeight: FontWeight.w600),
              ),
              const SizedBox(height: 12),
              _buildCountOptionTile(
                title: 'Quick Practice',
                count: 15,
                subtitle: '15 Questions • Shuffled • ~15 mins',
                subject: subject,
                onTap: () {
                  Navigator.pop(ctx);
                  _startSubjectQuiz(subject, 15);
                },
              ),
              const SizedBox(height: 8),
              _buildCountOptionTile(
                title: 'Standard Subject Test',
                count: 30,
                subtitle: '30 Questions • Standard TET Section • ~30 mins',
                subject: subject,
                onTap: () {
                  Navigator.pop(ctx);
                  _startSubjectQuiz(subject, 30);
                },
              ),
              const SizedBox(height: 8),
              _buildCountOptionTile(
                title: 'Intensive Practice',
                count: 50,
                subtitle: '50 Questions • High endurance • ~50 mins',
                subject: subject,
                onTap: () {
                  Navigator.pop(ctx);
                  _startSubjectQuiz(subject, 50);
                },
              ),
              const SizedBox(height: 8),
              _buildCountOptionTile(
                title: 'All Questions Bank',
                count: subject.totalQuestions,
                subtitle: 'Full Bank (${subject.totalQuestions} Questions)',
                subject: subject,
                onTap: () {
                  Navigator.pop(ctx);
                  _startSubjectQuiz(subject, subject.totalQuestions);
                },
              ),
            ],
          ),
        );
      },
    );
  }

  Widget _buildCountOptionTile({
    required String title,
    required int count,
    required String subtitle,
    required Subject subject,
    required VoidCallback onTap,
  }) {
    final theme = Theme.of(context);
    final isDark = theme.brightness == Brightness.dark;

    return Material(
      color: Colors.transparent,
      child: InkWell(
        borderRadius: BorderRadius.circular(12),
        onTap: onTap,
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
          decoration: BoxDecoration(
            color: isDark ? const Color(0xFF1E293B) : const Color(0xFFF8FAFC),
            borderRadius: BorderRadius.circular(12),
            border: Border.all(
              color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0),
            ),
          ),
          child: Row(
            children: [
              Container(
                width: 36,
                height: 36,
                decoration: BoxDecoration(
                  color: subject.primaryColor.withValues(alpha: 0.15),
                  shape: BoxShape.circle,
                ),
                alignment: Alignment.center,
                child: Text(
                  '$count',
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    color: subject.primaryColor,
                    fontSize: 13,
                  ),
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      title,
                      style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 14),
                    ),
                    Text(
                      subtitle,
                      style: TextStyle(
                        fontSize: 12,
                        color: isDark ? Colors.white60 : const Color(0xFF64748B),
                      ),
                    ),
                  ],
                ),
              ),
              const Icon(Icons.arrow_forward_ios_rounded, size: 14, color: Colors.grey),
            ],
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final isDark = theme.brightness == Brightness.dark;

    return Scaffold(
      appBar: AppBar(
        title: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(6),
              decoration: BoxDecoration(
                color: theme.colorScheme.primary.withValues(alpha: 0.15),
                borderRadius: BorderRadius.circular(8),
              ),
              child: Icon(
                Icons.school_rounded,
                color: theme.colorScheme.primary,
                size: 22,
              ),
            ),
            const SizedBox(width: 10),
            const Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'TET Test Practice',
                  style: TextStyle(fontSize: 17, fontWeight: FontWeight.w800),
                ),
                Text(
                  'Offline Practice & Mock Tests',
                  style: TextStyle(fontSize: 11, fontWeight: FontWeight.normal, color: Colors.grey),
                ),
              ],
            ),
          ],
        ),
        actions: [
          // Bookmark shortcut
          Stack(
            alignment: Alignment.center,
            children: [
              IconButton(
                icon: const Icon(Icons.bookmarks_outlined),
                tooltip: 'Saved Questions',
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (ctx) => const BookmarksScreen()),
                  ).then((_) => _updateStats());
                },
              ),
              if (_bookmarkCount > 0)
                Positioned(
                  top: 8,
                  right: 8,
                  child: Container(
                    padding: const EdgeInsets.all(4),
                    decoration: const BoxDecoration(
                      color: Colors.amber,
                      shape: BoxShape.circle,
                    ),
                    constraints: const BoxConstraints(
                      minWidth: 16,
                      minHeight: 16,
                    ),
                    child: Text(
                      '$_bookmarkCount',
                      style: const TextStyle(
                        fontSize: 10,
                        fontWeight: FontWeight.bold,
                        color: Colors.black,
                      ),
                    ),
                  ),
                ),
            ],
          ),
          // Dark/Light toggle
          IconButton(
            icon: Icon(widget.isDarkMode ? Icons.light_mode_outlined : Icons.dark_mode_outlined),
            tooltip: widget.isDarkMode ? 'Light Mode' : 'Dark Mode',
            onPressed: () => widget.onThemeChanged(!widget.isDarkMode),
          ),
        ],
      ),
      body: _isLoading
          ? const Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  CircularProgressIndicator(),
                  SizedBox(height: 16),
                  Text('Shuffling and preparing questions...'),
                ],
              ),
            )
          : RefreshIndicator(
              onRefresh: () async => _updateStats(),
              child: ListView(
                padding: const EdgeInsets.fromLTRB(16, 16, 16, 32),
                children: [
                  // Grand Mock Test Banner (Top Featured)
                  _buildGrandMockCard(context, isDark),

                  const SizedBox(height: 24),

                  // Quick Stats Row
                  Row(
                    children: [
                      _buildQuickStat(
                        icon: Icons.assignment_turned_in_outlined,
                        value: '${_history.length}',
                        label: 'Tests Taken',
                        color: const Color(0xFF6366F1),
                        isDark: isDark,
                      ),
                      const SizedBox(width: 10),
                      _buildQuickStat(
                        icon: Icons.star_border_rounded,
                        value: '$_bookmarkCount',
                        label: 'Saved Qs',
                        color: const Color(0xFFF59E0B),
                        isDark: isDark,
                      ),
                      const SizedBox(width: 10),
                      _buildQuickStat(
                        icon: Icons.quiz_outlined,
                        value: '2,643',
                        label: 'Total Bank',
                        color: const Color(0xFF10B981),
                        isDark: isDark,
                      ),
                    ],
                  ),

                  const SizedBox(height: 24),

                  // Section Title
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        'Subject Practice (విషయాల వారీగా)',
                        style: theme.textTheme.titleMedium?.copyWith(
                          fontSize: 17,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      Text(
                        '6 Subjects',
                        style: TextStyle(
                          fontSize: 12,
                          color: isDark ? Colors.white60 : const Color(0xFF64748B),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 12),

                  // Subjects List
                  ...Subject.allSubjects.map((subject) {
                    return _buildSubjectCard(context, subject, isDark);
                  }),
                ],
              ),
            ),
    );
  }

  Widget _buildGrandMockCard(BuildContext context, bool isDark) {
    return Container(
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: isDark
              ? [const Color(0xFF312E81), const Color(0xFF1E1B4B)]
              : [const Color(0xFF4F46E5), const Color(0xFF3730A3)],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(20),
        boxShadow: [
          BoxShadow(
            color: const Color(0xFF4F46E5).withValues(alpha: 0.35),
            blurRadius: 18,
            offset: const Offset(0, 8),
          ),
        ],
      ),
      child: Stack(
        children: [
          // Background decorative shapes
          Positioned(
            right: -20,
            bottom: -20,
            child: Icon(
              Icons.stars_rounded,
              size: 160,
              color: Colors.white.withValues(alpha: 0.08),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(20),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Top Tag
                Row(
                  children: [
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                      decoration: BoxDecoration(
                        color: const Color(0xFFF59E0B),
                        borderRadius: BorderRadius.circular(20),
                      ),
                      child: const Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(Icons.bolt_rounded, size: 14, color: Colors.white),
                          SizedBox(width: 4),
                          Text(
                            'FULL EXAM SIMULATION',
                            style: TextStyle(
                              color: Colors.white,
                              fontSize: 11,
                              fontWeight: FontWeight.bold,
                              letterSpacing: 0.5,
                            ),
                          ),
                        ],
                      ),
                    ),
                    const Spacer(),
                    const Icon(Icons.offline_bolt_rounded, color: Colors.white70, size: 18),
                    const SizedBox(width: 4),
                    const Text(
                      '100% Offline',
                      style: TextStyle(color: Colors.white70, fontSize: 12),
                    ),
                  ],
                ),
                const SizedBox(height: 14),

                // Main Title
                const Text(
                  'Grand Mock Test (150 Questions)',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 21,
                    fontWeight: FontWeight.w800,
                    letterSpacing: -0.4,
                  ),
                ),
                const SizedBox(height: 4),
                const Text(
                  'సమగ్ర మాక్ టెస్ట్ (మొత్తం 150 ప్రశ్నలు)',
                  style: TextStyle(
                    color: Colors.white70,
                    fontSize: 13,
                    fontWeight: FontWeight.w500,
                  ),
                ),
                const SizedBox(height: 12),

                // Distribution details
                Container(
                  padding: const EdgeInsets.all(12),
                  decoration: BoxDecoration(
                    color: Colors.white.withValues(alpha: 0.12),
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: const Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        children: [
                          Icon(Icons.shuffle_rounded, size: 16, color: Colors.amberAccent),
                          SizedBox(width: 8),
                          Expanded(
                            child: Text(
                              'Equal 25 Questions from each subject',
                              style: TextStyle(
                                color: Colors.white,
                                fontSize: 13,
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                          ),
                        ],
                      ),
                      SizedBox(height: 6),
                      Text(
                        'CDP (25) • Telugu (25) • English (25) • Maths (25) • Physics (25) • Biology (25)',
                        style: TextStyle(
                          color: Colors.white70,
                          fontSize: 12,
                          height: 1.3,
                        ),
                      ),
                      SizedBox(height: 4),
                      Text(
                        '⚡ Questions are freshly shuffled every time you start or restart!',
                        style: TextStyle(
                          color: Colors.amberAccent,
                          fontSize: 11.5,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    ],
                  ),
                ),

                const SizedBox(height: 16),

                // CTA Button
                SizedBox(
                  width: double.infinity,
                  child: ElevatedButton.icon(
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.white,
                      foregroundColor: const Color(0xFF4F46E5),
                      padding: const EdgeInsets.symmetric(vertical: 14),
                      elevation: 0,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(12),
                      ),
                    ),
                    onPressed: _startGrandMockTest,
                    icon: const Icon(Icons.play_arrow_rounded, size: 24),
                    label: const Text(
                      'Start Grand Test (150 Qs)',
                      style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildSubjectCard(BuildContext context, Subject subject, bool isDark) {
    final theme = Theme.of(context);

    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      child: InkWell(
        borderRadius: BorderRadius.circular(16),
        onTap: () => _showSubjectOptions(subject),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Row(
            children: [
              // Subject Icon Box
              Container(
                width: 48,
                height: 48,
                decoration: BoxDecoration(
                  color: subject.primaryColor.withValues(alpha: 0.14),
                  borderRadius: BorderRadius.circular(12),
                ),
                child: Icon(subject.icon, color: subject.primaryColor, size: 26),
              ),
              const SizedBox(width: 14),

              // Title and details
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      subject.title,
                      style: theme.textTheme.titleMedium?.copyWith(
                        fontWeight: FontWeight.bold,
                        fontSize: 15,
                      ),
                    ),
                    const SizedBox(height: 2),
                    Text(
                      subject.teluguTitle,
                      style: TextStyle(
                        fontSize: 12.5,
                        color: isDark ? Colors.white60 : const Color(0xFF64748B),
                      ),
                    ),
                    const SizedBox(height: 6),
                    Row(
                      children: [
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                          decoration: BoxDecoration(
                            color: subject.primaryColor.withValues(alpha: 0.1),
                            borderRadius: BorderRadius.circular(6),
                          ),
                          child: Text(
                            '${subject.totalQuestions} Questions',
                            style: TextStyle(
                              fontSize: 11,
                              fontWeight: FontWeight.bold,
                              color: subject.primaryColor,
                            ),
                          ),
                        ),
                        const SizedBox(width: 8),
                        const Text(
                          '• Hints & Tips',
                          style: TextStyle(fontSize: 11, color: Colors.grey),
                        ),
                      ],
                    ),
                  ],
                ),
              ),

              // Action button
              IconButton(
                icon: const Icon(Icons.arrow_forward_ios_rounded, size: 16),
                color: subject.primaryColor,
                onPressed: () => _showSubjectOptions(subject),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildQuickStat({
    required IconData icon,
    required String value,
    required String label,
    required Color color,
    required bool isDark,
  }) {
    return Expanded(
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 12, horizontal: 8),
        decoration: BoxDecoration(
          color: isDark ? const Color(0xFF1E293B) : Colors.white,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(
            color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0),
          ),
        ),
        child: Column(
          children: [
            Icon(icon, color: color, size: 22),
            const SizedBox(height: 4),
            Text(
              value,
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.w800,
                color: color,
              ),
            ),
            Text(
              label,
              style: TextStyle(
                fontSize: 11,
                color: isDark ? Colors.white60 : const Color(0xFF64748B),
                fontWeight: FontWeight.w500,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
