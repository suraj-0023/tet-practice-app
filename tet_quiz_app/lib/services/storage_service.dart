import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/question.dart';

class StorageService {
  static final StorageService _instance = StorageService._internal();
  factory StorageService() => _instance;
  StorageService._internal();

  static const String _keyBookmarks = 'bookmarked_questions_v1';
  static const String _keyHistory = 'quiz_history_v1';
  static const String _keyDarkMode = 'is_dark_mode_v1';

  SharedPreferences? _prefs;

  Future<void> init() async {
    _prefs ??= await SharedPreferences.getInstance();
  }

  // --- Bookmarks ---
  List<String> getBookmarkedKeys() {
    return _prefs?.getStringList(_keyBookmarks) ?? [];
  }

  bool isBookmarked(Question question) {
    final keys = getBookmarkedKeys();
    return keys.contains(question.uniqueKey);
  }

  Future<bool> toggleBookmark(Question question) async {
    await init();
    final keys = getBookmarkedKeys().toList();
    final key = question.uniqueKey;
    bool newState;
    if (keys.contains(key)) {
      keys.remove(key);
      newState = false;
    } else {
      keys.add(key);
      newState = true;
    }
    await _prefs?.setStringList(_keyBookmarks, keys);
    return newState;
  }

  // --- Quiz History ---
  List<Map<String, dynamic>> getHistory() {
    final raw = _prefs?.getStringList(_keyHistory) ?? [];
    return raw.map((item) {
      try {
        return jsonDecode(item) as Map<String, dynamic>;
      } catch (_) {
        return <String, dynamic>{};
      }
    }).where((item) => item.isNotEmpty).toList();
  }

  Future<void> saveQuizResult({
    required String title,
    required int score,
    required int total,
    required double percentage,
    required int timeSeconds,
    required bool isGrandTest,
  }) async {
    await init();
    final history = _prefs?.getStringList(_keyHistory) ?? [];
    final entry = {
      'title': title,
      'score': score,
      'total': total,
      'percentage': percentage,
      'timeSeconds': timeSeconds,
      'isGrandTest': isGrandTest,
      'date': DateTime.now().toIso8601String(),
    };
    history.insert(0, jsonEncode(entry));
    if (history.length > 50) {
      history.removeLast(); // Keep latest 50 results
    }
    await _prefs?.setStringList(_keyHistory, history);
  }

  // --- Theme preference ---
  bool isDarkMode() {
    return _prefs?.getBool(_keyDarkMode) ?? false;
  }

  Future<void> setDarkMode(bool value) async {
    await init();
    await _prefs?.setBool(_keyDarkMode, value);
  }
}
