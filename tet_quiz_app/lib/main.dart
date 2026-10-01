import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'screens/home_screen.dart';
import 'services/question_repository.dart';
import 'services/storage_service.dart';
import 'theme/app_theme.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Set preferred orientations to portrait for mobile quiz experience
  await SystemChrome.setPreferredOrientations([
    DeviceOrientation.portraitUp,
    DeviceOrientation.portraitDown,
  ]);

  // Initialize storage service
  final storage = StorageService();
  await storage.init();

  // Preload questions in background
  final repo = QuestionRepository();
  repo.initialize();

  runApp(const TetQuizApp());
}

class TetQuizApp extends StatefulWidget {
  const TetQuizApp({super.key});

  @override
  State<TetQuizApp> createState() => _TetQuizAppState();
}

class _TetQuizAppState extends State<TetQuizApp> {
  final StorageService _storage = StorageService();
  late bool _isDarkMode;

  @override
  void initState() {
    super.initState();
    _isDarkMode = _storage.isDarkMode();
  }

  void _toggleTheme(bool isDark) {
    setState(() => _isDarkMode = isDark);
    _storage.setDarkMode(isDark);
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'TET Test Practice',
      debugShowCheckedModeBanner: false,
      theme: AppTheme.lightTheme,
      darkTheme: AppTheme.darkTheme,
      themeMode: _isDarkMode ? ThemeMode.dark : ThemeMode.light,
      home: HomeScreen(
        isDarkMode: _isDarkMode,
        onThemeChanged: _toggleTheme,
      ),
    );
  }
}
