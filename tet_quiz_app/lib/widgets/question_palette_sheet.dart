import 'package:flutter/material.dart';
import '../models/quiz_session.dart';

class QuestionPaletteSheet extends StatelessWidget {
  final List<QuizQuestionState> questions;
  final int currentIndex;
  final ValueChanged<int> onSelectQuestion;
  final VoidCallback onSubmitTest;

  const QuestionPaletteSheet({
    super.key,
    required this.questions,
    required this.currentIndex,
    required this.onSelectQuestion,
    required this.onSubmitTest,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final isDark = theme.brightness == Brightness.dark;

    final int answeredCount = questions.where((q) => q.isAttempted).length;
    final int reviewCount = questions.where((q) => q.isMarkedForReview).length;
    final int unattemptedCount = questions.length - answeredCount;

    return Container(
      height: MediaQuery.of(context).size.height * 0.75,
      padding: const EdgeInsets.fromLTRB(16, 12, 16, 16),
      decoration: BoxDecoration(
        color: isDark ? const Color(0xFF1E293B) : Colors.white,
        borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
      ),
      child: Column(
        children: [
          // Drag handle
          Center(
            child: Container(
              width: 40,
              height: 4,
              decoration: BoxDecoration(
                color: isDark ? const Color(0xFF475569) : const Color(0xFFCBD5E1),
                borderRadius: BorderRadius.circular(2),
              ),
            ),
          ),
          const SizedBox(height: 12),

          // Header
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                'Question Palette (${questions.length})',
                style: theme.textTheme.titleLarge?.copyWith(fontSize: 18),
              ),
              IconButton(
                icon: const Icon(Icons.close_rounded),
                onPressed: () => Navigator.pop(context),
              ),
            ],
          ),
          const SizedBox(height: 10),

          // Legend chips
          SingleChildScrollView(
            scrollDirection: Axis.horizontal,
            child: Row(
              children: [
                _buildLegendChip(
                  color: const Color(0xFF10B981),
                  label: 'Answered ($answeredCount)',
                  isDark: isDark,
                ),
                const SizedBox(width: 8),
                _buildLegendChip(
                  color: const Color(0xFF8B5CF6),
                  label: 'Review ($reviewCount)',
                  isDark: isDark,
                ),
                const SizedBox(width: 8),
                _buildLegendChip(
                  color: isDark ? const Color(0xFF475569) : const Color(0xFFE2E8F0),
                  label: 'Not Answered ($unattemptedCount)',
                  textColor: isDark ? Colors.white70 : const Color(0xFF64748B),
                  isDark: isDark,
                ),
              ],
            ),
          ),
          const SizedBox(height: 14),
          const Divider(height: 1),

          // Grid of numbers
          Expanded(
            child: GridView.builder(
              padding: const EdgeInsets.symmetric(vertical: 12),
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 6,
                crossAxisSpacing: 10,
                mainAxisSpacing: 10,
                childAspectRatio: 1.0,
              ),
              itemCount: questions.length,
              itemBuilder: (context, index) {
                final state = questions[index];
                final isCurrent = index == currentIndex;
                final isAnswered = state.isAttempted;
                final isReview = state.isMarkedForReview;

                Color bgColor;
                Color textColor;
                Border? border;

                if (isReview && isAnswered) {
                  bgColor = const Color(0xFF8B5CF6);
                  textColor = Colors.white;
                } else if (isReview) {
                  bgColor = const Color(0xFFD8B4FE);
                  textColor = const Color(0xFF581C87);
                } else if (isAnswered) {
                  bgColor = const Color(0xFF10B981);
                  textColor = Colors.white;
                } else {
                  bgColor = isDark ? const Color(0xFF334155) : const Color(0xFFF1F5F9);
                  textColor = isDark ? Colors.white70 : const Color(0xFF475569);
                }

                if (isCurrent) {
                  border = Border.all(
                    color: theme.colorScheme.primary,
                    width: 2.5,
                  );
                }

                return Material(
                  color: Colors.transparent,
                  child: InkWell(
                    borderRadius: BorderRadius.circular(10),
                    onTap: () {
                      Navigator.pop(context);
                      onSelectQuestion(index);
                    },
                    child: Container(
                      decoration: BoxDecoration(
                        color: bgColor,
                        borderRadius: BorderRadius.circular(10),
                        border: border,
                      ),
                      alignment: Alignment.center,
                      child: Text(
                        '${index + 1}',
                        style: TextStyle(
                          color: textColor,
                          fontWeight: FontWeight.bold,
                          fontSize: 15,
                        ),
                      ),
                    ),
                  ),
                );
              },
            ),
          ),

          const SizedBox(height: 8),

          // Bottom Submit Test button
          SizedBox(
            width: double.infinity,
            child: ElevatedButton.icon(
              style: ElevatedButton.styleFrom(
                backgroundColor: theme.colorScheme.primary,
                padding: const EdgeInsets.symmetric(vertical: 14),
              ),
              onPressed: () {
                Navigator.pop(context);
                onSubmitTest();
              },
              icon: const Icon(Icons.check_circle_outline_rounded),
              label: const Text('Submit Quiz / పూర్తి చేయండి'),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildLegendChip({
    required Color color,
    required String label,
    Color? textColor,
    required bool isDark,
  }) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
      decoration: BoxDecoration(
        color: color.withValues(alpha: 0.15),
        borderRadius: BorderRadius.circular(8),
        border: Border.all(color: color.withValues(alpha: 0.4)),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Container(
            width: 10,
            height: 10,
            decoration: BoxDecoration(
              color: color,
              shape: BoxShape.circle,
            ),
          ),
          const SizedBox(width: 6),
          Text(
            label,
            style: TextStyle(
              fontSize: 12,
              fontWeight: FontWeight.w600,
              color: textColor ?? color,
            ),
          ),
        ],
      ),
    );
  }
}
