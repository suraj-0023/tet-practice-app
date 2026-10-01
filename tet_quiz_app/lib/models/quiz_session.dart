import 'question.dart';

class QuizQuestionState {
  final Question question;
  int? selectedOptionKey;
  bool isMarkedForReview;
  bool showHint;
  bool showMemoryTip;
  bool showAnswer;

  QuizQuestionState({
    required this.question,
    this.selectedOptionKey,
    this.isMarkedForReview = false,
    this.showHint = false,
    this.showMemoryTip = false,
    this.showAnswer = false,
  });

  bool get isAttempted => selectedOptionKey != null;
  bool get isCorrect => selectedOptionKey == question.answer;
  bool get isWrong => isAttempted && selectedOptionKey != question.answer;
}

class SubjectStat {
  final String subjectId;
  final String subjectTitle;
  int total;
  int attempted;
  int correct;
  int wrong;

  SubjectStat({
    required this.subjectId,
    required this.subjectTitle,
    this.total = 0,
    this.attempted = 0,
    this.correct = 0,
    this.wrong = 0,
  });

  int get unattempted => total - attempted;
  double get accuracy => attempted > 0 ? (correct / attempted) * 100 : 0.0;
  double get scorePercentage => total > 0 ? (correct / total) * 100 : 0.0;
}

class QuizResult {
  final String quizTitle;
  final bool isGrandTest;
  final int totalQuestions;
  final int attemptedCount;
  final int correctCount;
  final int wrongCount;
  final int unattemptedCount;
  final int elapsedSeconds;
  final double scorePercentage;
  final Map<String, SubjectStat> subjectStats;
  final List<QuizQuestionState> questions;
  final DateTime completedAt;

  QuizResult({
    required this.quizTitle,
    required this.isGrandTest,
    required this.totalQuestions,
    required this.attemptedCount,
    required this.correctCount,
    required this.wrongCount,
    required this.unattemptedCount,
    required this.elapsedSeconds,
    required this.scorePercentage,
    required this.subjectStats,
    required this.questions,
    required this.completedAt,
  });

  String get timeFormatted {
    final minutes = elapsedSeconds ~/ 60;
    final seconds = elapsedSeconds % 60;
    return '${minutes.toString().padLeft(2, '0')}:${seconds.toString().padLeft(2, '0')}';
  }
}
