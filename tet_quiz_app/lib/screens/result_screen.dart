import 'package:flutter/material.dart';
import '../models/quiz_session.dart';
import '../models/subject.dart';
import '../widgets/hint_tip_widget.dart';

class ResultScreen extends StatefulWidget {
  final QuizResult result;
  final VoidCallback onRestart;

  const ResultScreen({
    super.key,
    required this.result,
    required this.onRestart,
  });

  @override
  State<ResultScreen> createState() => _ResultScreenState();
}

class _ResultScreenState extends State<ResultScreen> with SingleTickerProviderStateMixin {
  late TabController _tabController;
  String _filterType = 'all'; // all, incorrect, correct, unattempted

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final isDark = theme.brightness == Brightness.dark;
    final r = widget.result;

    return PopScope(
      canPop: true,
      child: Scaffold(
        appBar: AppBar(
          title: Text(r.isGrandTest ? 'Mock Test Result' : 'Quiz Result'),
          bottom: TabBar(
            controller: _tabController,
            tabs: const [
              Tab(icon: Icon(Icons.analytics_outlined), text: 'Performance'),
              Tab(icon: Icon(Icons.fact_check_outlined), text: 'Review Questions'),
            ],
          ),
        ),
        body: TabBarView(
          controller: _tabController,
          children: [
            _buildPerformanceTab(context, r, isDark),
            _buildReviewTab(context, r, isDark),
          ],
        ),
        bottomNavigationBar: Container(
          padding: const EdgeInsets.all(16),
          decoration: BoxDecoration(
            color: isDark ? const Color(0xFF1E293B) : Colors.white,
            boxShadow: [
              BoxShadow(
                color: Colors.black.withValues(alpha: 0.05),
                blurRadius: 10,
                offset: const Offset(0, -4),
              ),
            ],
          ),
          child: Row(
            children: [
              Expanded(
                child: OutlinedButton.icon(
                  onPressed: () {
                    Navigator.of(context).popUntil((route) => route.isFirst);
                  },
                  icon: const Icon(Icons.home_rounded),
                  label: const Text('Home'),
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                flex: 2,
                child: ElevatedButton.icon(
                  onPressed: widget.onRestart,
                  icon: const Icon(Icons.replay_rounded),
                  label: const Text('Restart (New Questions)'),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildPerformanceTab(BuildContext context, QuizResult r, bool isDark) {
    final theme = Theme.of(context);

    // Performance message
    String gradeTitle;
    String gradeSub;
    Color gradeColor;

    if (r.scorePercentage >= 80) {
      gradeTitle = 'Outstanding Performance! 🏆';
      gradeSub = 'అద్భుతమైన ప్రతిభ! You have excellent mastery over the topics.';
      gradeColor = const Color(0xFF10B981);
    } else if (r.scorePercentage >= 60) {
      gradeTitle = 'Good Effort! 👍';
      gradeSub = 'మంచి ఫలితం! Revision on weak subjects will boost your score further.';
      gradeColor = const Color(0xFF3B82F6);
    } else if (r.scorePercentage >= 40) {
      gradeTitle = 'Average Score 📚';
      gradeSub = 'మరింత సాధన అవసరం. Practice hints & memory tips to strengthen concepts.';
      gradeColor = const Color(0xFFF59E0B);
    } else {
      gradeTitle = 'Needs More Practice 💡';
      gradeSub = 'పట్టుదలతో పునశ్చరణ చేయండి. Focus on fundamentals & revise daily.';
      gradeColor = const Color(0xFFEF4444);
    }

    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        // Score Header Card
        Container(
          padding: const EdgeInsets.all(20),
          decoration: BoxDecoration(
            gradient: LinearGradient(
              colors: isDark
                  ? [const Color(0xFF312E81), const Color(0xFF1E1B4B)]
                  : [const Color(0xFF4F46E5), const Color(0xFF4338CA)],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
            borderRadius: BorderRadius.circular(20),
            boxShadow: [
              BoxShadow(
                color: const Color(0xFF4F46E5).withValues(alpha: 0.3),
                blurRadius: 15,
                offset: const Offset(0, 6),
              ),
            ],
          ),
          child: Column(
            children: [
              Text(
                r.quizTitle,
                style: const TextStyle(
                  color: Colors.white70,
                  fontSize: 14,
                  fontWeight: FontWeight.w500,
                ),
                textAlign: TextAlign.center,
              ),
              const SizedBox(height: 12),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.baseline,
                textBaseline: TextBaseline.alphabetic,
                children: [
                  Text(
                    '${r.correctCount}',
                    style: const TextStyle(
                      color: Colors.white,
                      fontSize: 48,
                      fontWeight: FontWeight.w900,
                    ),
                  ),
                  Text(
                    ' / ${r.totalQuestions}',
                    style: const TextStyle(
                      color: Colors.white70,
                      fontSize: 22,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 6),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 4),
                decoration: BoxDecoration(
                  color: Colors.white.withValues(alpha: 0.2),
                  borderRadius: BorderRadius.circular(20),
                ),
                child: Text(
                  '${r.scorePercentage.toStringAsFixed(1)}% Score',
                  style: const TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.bold,
                    fontSize: 16,
                  ),
                ),
              ),
              const SizedBox(height: 14),
              Container(
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(
                  color: Colors.black.withValues(alpha: 0.2),
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(color: gradeColor.withValues(alpha: 0.6), width: 1.5),
                ),
                child: Column(
                  children: [
                    Text(
                      gradeTitle,
                      style: const TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        fontSize: 15,
                      ),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      gradeSub,
                      textAlign: TextAlign.center,
                      style: const TextStyle(
                        color: Colors.white70,
                        fontSize: 12.5,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),

        const SizedBox(height: 16),

        // Quick Stats Row
        Row(
          children: [
            _buildStatCard(
              title: 'Correct',
              value: '${r.correctCount}',
              subtitle: 'సరియైనవి',
              icon: Icons.check_circle_rounded,
              color: const Color(0xFF10B981),
              isDark: isDark,
            ),
            const SizedBox(width: 10),
            _buildStatCard(
              title: 'Incorrect',
              value: '${r.wrongCount}',
              subtitle: 'తప్పులు',
              icon: Icons.cancel_rounded,
              color: const Color(0xFFEF4444),
              isDark: isDark,
            ),
            const SizedBox(width: 10),
            _buildStatCard(
              title: 'Skipped',
              value: '${r.unattemptedCount}',
              subtitle: 'రాయనివి',
              icon: Icons.help_outline_rounded,
              color: const Color(0xFF64748B),
              isDark: isDark,
            ),
          ],
        ),

        const SizedBox(height: 12),

        // Accuracy & Time Row
        Row(
          children: [
            _buildInfoCard(
              title: 'Accuracy',
              value: r.attemptedCount > 0
                  ? '${((r.correctCount / r.attemptedCount) * 100).toStringAsFixed(1)}%'
                  : '0%',
              icon: Icons.track_changes_rounded,
              color: const Color(0xFF8B5CF6),
              isDark: isDark,
            ),
            const SizedBox(width: 10),
            _buildInfoCard(
              title: 'Time Taken',
              value: r.timeFormatted,
              icon: Icons.timer_outlined,
              color: const Color(0xFF06B6D4),
              isDark: isDark,
            ),
          ],
        ),

        const SizedBox(height: 24),

        // Subject-wise Breakdown (especially for 150 Grand Mock Test)
        Text(
          'Subject-wise Breakdown (విషయాల వారీగా విశ్లేషణ)',
          style: theme.textTheme.titleMedium?.copyWith(fontWeight: FontWeight.bold),
        ),
        const SizedBox(height: 12),

        ...r.subjectStats.values.map((stat) {
          final subject = Subject.findById(stat.subjectId);
          final progress = stat.total > 0 ? (stat.correct / stat.total) : 0.0;

          return Card(
            margin: const EdgeInsets.only(bottom: 12),
            child: Padding(
              padding: const EdgeInsets.all(14),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      Container(
                        padding: const EdgeInsets.all(8),
                        decoration: BoxDecoration(
                          color: (subject?.primaryColor ?? theme.colorScheme.primary)
                              .withValues(alpha: 0.15),
                          borderRadius: BorderRadius.circular(8),
                        ),
                        child: Icon(
                          subject?.icon ?? Icons.subject_rounded,
                          size: 20,
                          color: subject?.primaryColor ?? theme.colorScheme.primary,
                        ),
                      ),
                      const SizedBox(width: 12),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              subject?.title ?? stat.subjectTitle,
                              style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 14),
                            ),
                            Text(
                              'Attempted: ${stat.attempted}/${stat.total} • Accuracy: ${stat.accuracy.toStringAsFixed(0)}%',
                              style: TextStyle(
                                fontSize: 12,
                                color: isDark ? Colors.white60 : const Color(0xFF64748B),
                              ),
                            ),
                          ],
                        ),
                      ),
                      Text(
                        '${stat.correct}/${stat.total}',
                        style: TextStyle(
                          fontSize: 16,
                          fontWeight: FontWeight.w800,
                          color: subject?.primaryColor ?? theme.colorScheme.primary,
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 10),
                  ClipRRect(
                    borderRadius: BorderRadius.circular(4),
                    child: LinearProgressIndicator(
                      value: progress,
                      minHeight: 6,
                      backgroundColor: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0),
                      valueColor: AlwaysStoppedAnimation<Color>(
                        subject?.primaryColor ?? theme.colorScheme.primary,
                      ),
                    ),
                  ),
                ],
              ),
            ),
          );
        }),

        const SizedBox(height: 80),
      ],
    );
  }

  Widget _buildStatCard({
    required String title,
    required String value,
    required String subtitle,
    required IconData icon,
    required Color color,
    required bool isDark,
  }) {
    return Expanded(
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 14, horizontal: 8),
        decoration: BoxDecoration(
          color: isDark ? const Color(0xFF1E293B) : Colors.white,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(
            color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0),
          ),
        ),
        child: Column(
          children: [
            Icon(icon, color: color, size: 24),
            const SizedBox(height: 6),
            Text(
              value,
              style: TextStyle(
                fontSize: 22,
                fontWeight: FontWeight.w800,
                color: color,
              ),
            ),
            Text(
              title,
              style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w600),
            ),
            Text(
              subtitle,
              style: TextStyle(
                fontSize: 10.5,
                color: isDark ? Colors.white54 : const Color(0xFF94A3B8),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildInfoCard({
    required String title,
    required String value,
    required IconData icon,
    required Color color,
    required bool isDark,
  }) {
    return Expanded(
      child: Container(
        padding: const EdgeInsets.all(14),
        decoration: BoxDecoration(
          color: isDark ? const Color(0xFF1E293B) : Colors.white,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(
            color: isDark ? const Color(0xFF334155) : const Color(0xFFE2E8F0),
          ),
        ),
        child: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(8),
              decoration: BoxDecoration(
                color: color.withValues(alpha: 0.15),
                borderRadius: BorderRadius.circular(10),
              ),
              child: Icon(icon, color: color, size: 22),
            ),
            const SizedBox(width: 12),
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: TextStyle(
                    fontSize: 12,
                    color: isDark ? Colors.white60 : const Color(0xFF64748B),
                  ),
                ),
                Text(
                  value,
                  style: const TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildReviewTab(BuildContext context, QuizResult r, bool isDark) {
    final theme = Theme.of(context);

    // Filter questions
    final filtered = r.questions.where((q) {
      if (_filterType == 'incorrect') return q.isWrong;
      if (_filterType == 'correct') return q.isCorrect;
      if (_filterType == 'unattempted') return !q.isAttempted;
      return true;
    }).toList();

    return Column(
      children: [
        // Filter bar
        SingleChildScrollView(
          scrollDirection: Axis.horizontal,
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
          child: Row(
            children: [
              _buildFilterChip('All (${r.questions.length})', 'all'),
              const SizedBox(width: 8),
              _buildFilterChip('Incorrect (${r.wrongCount})', 'incorrect', color: const Color(0xFFEF4444)),
              const SizedBox(width: 8),
              _buildFilterChip('Correct (${r.correctCount})', 'correct', color: const Color(0xFF10B981)),
              const SizedBox(width: 8),
              _buildFilterChip('Unattempted (${r.unattemptedCount})', 'unattempted'),
            ],
          ),
        ),

        const Divider(height: 1),

        // Questions list
        Expanded(
          child: filtered.isEmpty
              ? Center(
                  child: Text(
                    'No questions match this filter',
                    style: theme.textTheme.bodyLarge,
                  ),
                )
              : ListView.builder(
                  padding: const EdgeInsets.fromLTRB(16, 12, 16, 80),
                  itemCount: filtered.length,
                  itemBuilder: (context, index) {
                    final item = filtered[index];
                    final q = item.question;
                    final originalIndex = r.questions.indexOf(item);
                    final subject = Subject.findById(q.subjectId);

                    return Card(
                      margin: const EdgeInsets.only(bottom: 16),
                      child: Padding(
                        padding: const EdgeInsets.all(16),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            // Status badge & Subject
                            Row(
                              children: [
                                Container(
                                  padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                                  decoration: BoxDecoration(
                                    color: (subject?.primaryColor ?? theme.colorScheme.primary)
                                        .withValues(alpha: 0.15),
                                    borderRadius: BorderRadius.circular(6),
                                  ),
                                  child: Text(
                                    subject?.title ?? q.subjectName,
                                    style: TextStyle(
                                      color: subject?.primaryColor ?? theme.colorScheme.primary,
                                      fontWeight: FontWeight.bold,
                                      fontSize: 11,
                                    ),
                                  ),
                                ),
                                const Spacer(),
                                _buildStatusBadge(item),
                              ],
                            ),
                            const SizedBox(height: 10),

                            // Question
                            Text(
                              'Q${originalIndex + 1}. ${q.question}',
                              style: theme.textTheme.titleMedium?.copyWith(
                                fontWeight: FontWeight.w600,
                                height: 1.45,
                              ),
                            ),
                            const SizedBox(height: 12),

                            // Options
                            ...q.options.map((opt) {
                              final isUserChoice = item.selectedOptionKey == opt.key;
                              final isCorrect = opt.key == q.answer;

                              Color bgColor;
                              Color borderColor;
                              Color textColor;

                              if (isCorrect) {
                                bgColor = isDark ? const Color(0xFF064E3B) : const Color(0xFFD1FAE5);
                                borderColor = const Color(0xFF10B981);
                                textColor = isDark ? const Color(0xFF6EE7B7) : const Color(0xFF065F46);
                              } else if (isUserChoice && !isCorrect) {
                                bgColor = isDark ? const Color(0xFF450A0A) : const Color(0xFFFEE2E2);
                                borderColor = const Color(0xFFEF4444);
                                textColor = isDark ? const Color(0xFFFCA5A5) : const Color(0xFF991B1B);
                              } else {
                                bgColor = isDark ? const Color(0xFF334155) : const Color(0xFFF8FAFC);
                                borderColor = isDark ? const Color(0xFF475569) : const Color(0xFFE2E8F0);
                                textColor = isDark ? Colors.white70 : const Color(0xFF334155);
                              }

                              return Container(
                                margin: const EdgeInsets.only(bottom: 8),
                                padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
                                decoration: BoxDecoration(
                                  color: bgColor,
                                  borderRadius: BorderRadius.circular(8),
                                  border: Border.all(color: borderColor, width: (isCorrect || isUserChoice) ? 1.5 : 1),
                                ),
                                child: Row(
                                  children: [
                                    Container(
                                      width: 24,
                                      height: 24,
                                      decoration: BoxDecoration(
                                        color: isCorrect
                                            ? const Color(0xFF10B981)
                                            : (isUserChoice ? const Color(0xFFEF4444) : Colors.transparent),
                                        shape: BoxShape.circle,
                                        border: Border.all(
                                          color: isCorrect
                                              ? const Color(0xFF10B981)
                                              : (isUserChoice ? const Color(0xFFEF4444) : Colors.grey),
                                        ),
                                      ),
                                      alignment: Alignment.center,
                                      child: Text(
                                        '${opt.key}',
                                        style: TextStyle(
                                          fontWeight: FontWeight.bold,
                                          fontSize: 12,
                                          color: (isCorrect || isUserChoice) ? Colors.white : textColor,
                                        ),
                                      ),
                                    ),
                                    const SizedBox(width: 10),
                                    Expanded(
                                      child: Text(
                                        opt.text,
                                        style: TextStyle(
                                          fontSize: 13.5,
                                          fontWeight: (isCorrect || isUserChoice) ? FontWeight.w600 : FontWeight.w400,
                                          color: textColor,
                                        ),
                                      ),
                                    ),
                                    if (isCorrect)
                                      const Icon(Icons.check_circle_rounded, color: Color(0xFF10B981), size: 18),
                                    if (isUserChoice && !isCorrect)
                                      const Icon(Icons.cancel_rounded, color: Color(0xFFEF4444), size: 18),
                                  ],
                                ),
                              );
                            }),

                            // Hints & Memory Tips
                            HintTipWidget(
                              hint: q.hint,
                              memoryTip: q.memoryTip,
                              initialShowHint: false,
                              initialShowTip: false,
                            ),
                          ],
                        ),
                      ),
                    );
                  },
                ),
        ),
      ],
    );
  }

  Widget _buildFilterChip(String label, String value, {Color? color}) {
    final isSelected = _filterType == value;
    final theme = Theme.of(context);

    return ChoiceChip(
      label: Text(label),
      selected: isSelected,
      onSelected: (selected) {
        if (selected) {
          setState(() => _filterType = value);
        }
      },
      selectedColor: (color ?? theme.colorScheme.primary).withValues(alpha: 0.2),
      labelStyle: TextStyle(
        fontWeight: isSelected ? FontWeight.bold : FontWeight.w500,
        color: isSelected ? (color ?? theme.colorScheme.primary) : null,
      ),
    );
  }

  Widget _buildStatusBadge(QuizQuestionState item) {
    if (item.isCorrect) {
      return Container(
        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
        decoration: BoxDecoration(
          color: const Color(0xFFD1FAE5),
          borderRadius: BorderRadius.circular(6),
        ),
        child: const Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(Icons.check_circle_rounded, color: Color(0xFF10B981), size: 14),
            SizedBox(width: 4),
            Text(
              'Correct',
              style: TextStyle(
                color: Color(0xFF065F46),
                fontSize: 11,
                fontWeight: FontWeight.bold,
              ),
            ),
          ],
        ),
      );
    } else if (item.isWrong) {
      return Container(
        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
        decoration: BoxDecoration(
          color: const Color(0xFFFEE2E2),
          borderRadius: BorderRadius.circular(6),
        ),
        child: const Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(Icons.cancel_rounded, color: Color(0xFFEF4444), size: 14),
            SizedBox(width: 4),
            Text(
              'Incorrect',
              style: TextStyle(
                color: Color(0xFF991B1B),
                fontSize: 11,
                fontWeight: FontWeight.bold,
              ),
            ),
          ],
        ),
      );
    } else {
      return Container(
        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
        decoration: BoxDecoration(
          color: const Color(0xFFE2E8F0),
          borderRadius: BorderRadius.circular(6),
        ),
        child: const Text(
          'Skipped',
          style: TextStyle(
            color: Color(0xFF475569),
            fontSize: 11,
            fontWeight: FontWeight.bold,
          ),
        ),
      );
    }
  }
}
