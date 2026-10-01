import 'package:flutter/material.dart';
import '../models/question.dart';
import '../models/subject.dart';
import '../services/question_repository.dart';
import '../services/storage_service.dart';
import '../widgets/hint_tip_widget.dart';

class BookmarksScreen extends StatefulWidget {
  const BookmarksScreen({super.key});

  @override
  State<BookmarksScreen> createState() => _BookmarksScreenState();
}

class _BookmarksScreenState extends State<BookmarksScreen> {
  final QuestionRepository _repo = QuestionRepository();
  final StorageService _storage = StorageService();

  List<Question> _bookmarkedQuestions = [];
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadBookmarks();
  }

  Future<void> _loadBookmarks() async {
    setState(() => _isLoading = true);
    final bookmarkedKeys = _storage.getBookmarkedKeys().toSet();

    final List<Question> results = [];
    for (final subject in Subject.allSubjects) {
      final questions = await _repo.getQuestionsForSubject(subject.id);
      for (final q in questions) {
        if (bookmarkedKeys.contains(q.uniqueKey)) {
          results.add(q);
        }
      }
    }

    setState(() {
      _bookmarkedQuestions = results;
      _isLoading = false;
    });
  }

  Future<void> _removeBookmark(Question q) async {
    await _storage.toggleBookmark(q);
    setState(() {
      _bookmarkedQuestions.removeWhere((item) => item.uniqueKey == q.uniqueKey);
    });
    if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Removed from Saved Questions'),
          duration: Duration(seconds: 1),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final isDark = theme.brightness == Brightness.dark;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Saved Questions (బుక్‌మార్క్‌లు)'),
        actions: [
          if (_bookmarkedQuestions.isNotEmpty)
            Center(
              child: Padding(
                padding: const EdgeInsets.only(right: 16),
                child: Text(
                  '${_bookmarkedQuestions.length} Questions',
                  style: const TextStyle(fontWeight: FontWeight.bold),
                ),
              ),
            ),
        ],
      ),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : _bookmarkedQuestions.isEmpty
              ? Center(
                  child: Padding(
                    padding: const EdgeInsets.all(32),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(
                          Icons.bookmark_border_rounded,
                          size: 72,
                          color: isDark ? Colors.white38 : Colors.black26,
                        ),
                        const SizedBox(height: 16),
                        Text(
                          'No saved questions yet',
                          style: theme.textTheme.titleLarge,
                        ),
                        const SizedBox(height: 8),
                        Text(
                          'Tap the bookmark icon on any question during a quiz to save it for quick revision here.',
                          textAlign: TextAlign.center,
                          style: theme.textTheme.bodyMedium,
                        ),
                      ],
                    ),
                  ),
                )
              : ListView.builder(
                  padding: const EdgeInsets.all(16),
                  itemCount: _bookmarkedQuestions.length,
                  itemBuilder: (context, index) {
                    final q = _bookmarkedQuestions[index];
                    final subject = Subject.findById(q.subjectId);

                    return Card(
                      margin: const EdgeInsets.only(bottom: 16),
                      child: Padding(
                        padding: const EdgeInsets.all(16),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            // Subject tag & remove action
                            Row(
                              children: [
                                Container(
                                  padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                                  decoration: BoxDecoration(
                                    color: (subject?.primaryColor ?? theme.colorScheme.primary)
                                        .withValues(alpha: 0.15),
                                    borderRadius: BorderRadius.circular(8),
                                  ),
                                  child: Text(
                                    subject?.title ?? q.subjectName,
                                    style: TextStyle(
                                      color: subject?.primaryColor ?? theme.colorScheme.primary,
                                      fontWeight: FontWeight.w600,
                                      fontSize: 12,
                                    ),
                                  ),
                                ),
                                const Spacer(),
                                IconButton(
                                  icon: const Icon(Icons.bookmark_rounded, color: Colors.amber),
                                  onPressed: () => _removeBookmark(q),
                                  tooltip: 'Remove bookmark',
                                ),
                              ],
                            ),
                            const SizedBox(height: 8),

                            // Question text
                            Text(
                              'Q${index + 1}. ${q.question}',
                              style: theme.textTheme.titleMedium?.copyWith(
                                height: 1.45,
                                fontWeight: FontWeight.w600,
                              ),
                            ),
                            const SizedBox(height: 12),

                            // Options
                            ...q.options.map((opt) {
                              final isCorrect = opt.key == q.answer;
                              return Container(
                                margin: const EdgeInsets.only(bottom: 8),
                                padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
                                decoration: BoxDecoration(
                                  color: isCorrect
                                      ? (isDark ? const Color(0xFF064E3B) : const Color(0xFFD1FAE5))
                                      : (isDark ? const Color(0xFF334155) : const Color(0xFFF8FAFC)),
                                  borderRadius: BorderRadius.circular(8),
                                  border: Border.all(
                                    color: isCorrect
                                        ? const Color(0xFF10B981)
                                        : (isDark ? const Color(0xFF475569) : const Color(0xFFE2E8F0)),
                                    width: isCorrect ? 1.5 : 1,
                                  ),
                                ),
                                child: Row(
                                  children: [
                                    Container(
                                      width: 26,
                                      height: 26,
                                      decoration: BoxDecoration(
                                        color: isCorrect ? const Color(0xFF10B981) : Colors.transparent,
                                        shape: BoxShape.circle,
                                        border: Border.all(
                                          color: isCorrect
                                              ? const Color(0xFF10B981)
                                              : (isDark ? Colors.white38 : Colors.black26),
                                        ),
                                      ),
                                      alignment: Alignment.center,
                                      child: Text(
                                        '${opt.key}',
                                        style: TextStyle(
                                          fontWeight: FontWeight.bold,
                                          fontSize: 13,
                                          color: isCorrect
                                              ? Colors.white
                                              : (isDark ? Colors.white70 : Colors.black87),
                                        ),
                                      ),
                                    ),
                                    const SizedBox(width: 10),
                                    Expanded(
                                      child: Text(
                                        opt.text,
                                        style: TextStyle(
                                          fontSize: 14,
                                          fontWeight: isCorrect ? FontWeight.w600 : FontWeight.w400,
                                          color: isCorrect
                                              ? (isDark ? const Color(0xFF6EE7B7) : const Color(0xFF065F46))
                                              : null,
                                        ),
                                      ),
                                    ),
                                    if (isCorrect)
                                      const Icon(
                                        Icons.check_circle_rounded,
                                        color: Color(0xFF10B981),
                                        size: 20,
                                      ),
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
    );
  }
}
