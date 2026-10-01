import 'dart:convert';
import 'dart:math';
import 'package:flutter/services.dart';
import '../models/question.dart';
import '../models/subject.dart';

class QuestionRepository {
  // Singleton pattern
  static final QuestionRepository _instance = QuestionRepository._internal();
  factory QuestionRepository() => _instance;
  QuestionRepository._internal();

  final Map<String, List<Question>> _cachedQuestions = {};
  bool _isInitialized = false;

  bool get isInitialized => _isInitialized;

  /// Preload all subjects into memory (total ~2.3 MB, takes ~50ms)
  Future<void> initialize() async {
    if (_isInitialized) return;

    for (final subject in Subject.allSubjects) {
      await getQuestionsForSubject(subject.id);
    }
    _isInitialized = true;
  }

  /// Load and parse questions for a specific subject
  Future<List<Question>> getQuestionsForSubject(String subjectId) async {
    if (_cachedQuestions.containsKey(subjectId)) {
      return _cachedQuestions[subjectId]!;
    }

    final subject = Subject.findById(subjectId);
    if (subject == null) return [];

    try {
      final jsonString = await rootBundle.loadString(subject.assetPath);
      final List<dynamic> jsonList = jsonDecode(jsonString);

      final List<Question> questions = jsonList
          .map((item) => Question.fromJson(
                item as Map<String, dynamic>,
                subjectId: subject.id,
                subjectName: subject.title,
              ))
          .toList();

      _cachedQuestions[subjectId] = questions;
      return questions;
    } catch (e) {
      // In case of error loading asset
      return [];
    }
  }

  /// Generate a Grand Mock Test with exactly 150 questions drawn equally
  /// from all subjects (25 questions from each of the 6 subjects = 150 total).
  /// Every call shuffles and samples freshly.
  Future<List<Question>> generateGrandMockTest({bool shuffleAcrossSubjects = false}) async {
    final Random random = Random();
    final List<Question> grandTestQuestions = [];

    // 6 subjects: CDP, Telugu, English, Maths, Physics, Biology
    // 150 / 6 = 25 questions each
    const int countPerSubject = 25;

    for (final subject in Subject.allSubjects) {
      final subjectQuestions = await getQuestionsForSubject(subject.id);
      if (subjectQuestions.isEmpty) continue;

      // Copy and shuffle
      final List<Question> shuffled = List<Question>.from(subjectQuestions)..shuffle(random);
      final int takeCount = min(countPerSubject, shuffled.length);
      grandTestQuestions.addAll(shuffled.take(takeCount));
    }

    if (shuffleAcrossSubjects) {
      grandTestQuestions.shuffle(random);
    }

    return grandTestQuestions;
  }

  /// Generate a Subject-wise quiz with requested question count, freshly shuffled.
  Future<List<Question>> generateSubjectQuiz(String subjectId, {int? count}) async {
    final subjectQuestions = await getQuestionsForSubject(subjectId);
    if (subjectQuestions.isEmpty) return [];

    final Random random = Random();
    final List<Question> shuffled = List<Question>.from(subjectQuestions)..shuffle(random);

    if (count != null && count > 0 && count < shuffled.length) {
      return shuffled.take(count).toList();
    }
    return shuffled;
  }

  /// Get total question count loaded
  int get totalQuestionsCount {
    int total = 0;
    for (final list in _cachedQuestions.values) {
      total += list.length;
    }
    return total;
  }
}
