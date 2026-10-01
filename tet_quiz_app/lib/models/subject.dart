import 'package:flutter/material.dart';

class Subject {
  final String id;
  final String title;
  final String teluguTitle;
  final String assetPath;
  final IconData icon;
  final Color primaryColor;
  final Color accentColor;
  final int totalQuestions;
  final String description;

  const Subject({
    required this.id,
    required this.title,
    required this.teluguTitle,
    required this.assetPath,
    required this.icon,
    required this.primaryColor,
    required this.accentColor,
    required this.totalQuestions,
    required this.description,
  });

  static const List<Subject> allSubjects = [
    Subject(
      id: 'cdp',
      title: 'Child Development & Pedagogy',
      teluguTitle: 'శిశు వికాసం మరియు బోధనా పద్ధతులు',
      assetPath: 'assets/data/cdp_questions.json',
      icon: Icons.psychology_outlined,
      primaryColor: Color(0xFF6C5CE7),
      accentColor: Color(0xFFA29BFE),
      totalQuestions: 630,
      description: 'Growth, Development, Learning Theories, Special Education & ICT',
    ),
    Subject(
      id: 'telugu',
      title: 'Telugu Language I',
      teluguTitle: 'తెలుగు భాష - 1 (సాహిత్యం & వ్యాకరణం)',
      assetPath: 'assets/data/telugu_questions.json',
      icon: Icons.menu_book_rounded,
      primaryColor: Color(0xFF00B894),
      accentColor: Color(0xFF55EFC4),
      totalQuestions: 573,
      description: 'పద్యాలు, గద్యాలు, సంధులు, సమాసాలు, ఛందస్సు, వ్యాకరణాంశాలు',
    ),
    Subject(
      id: 'english',
      title: 'English Language II',
      teluguTitle: 'ఇంగ్లీష్ భాష - 2 (Grammar & Pedagogy)',
      assetPath: 'assets/data/english_questions.json',
      icon: Icons.translate_rounded,
      primaryColor: Color(0xFF0984E3),
      accentColor: Color(0xFF74B9FF),
      totalQuestions: 720,
      description: 'Tenses, Voice, Speech, Prepositions, Vocabulary & Methodology',
    ),
    Subject(
      id: 'maths',
      title: 'Mathematics',
      teluguTitle: 'గణిత శాస్త్రం & బోధనా పద్ధతులు',
      assetPath: 'assets/data/maths_questions.json',
      icon: Icons.calculate_outlined,
      primaryColor: Color(0xFFE17055),
      accentColor: Color(0xFFFAB1A0),
      totalQuestions: 240,
      description: 'Arithmetic, Algebra, Geometry, Trigonometry, Statistics & Pedagogy',
    ),
    Subject(
      id: 'physics',
      title: 'Physical Science',
      teluguTitle: 'భౌతిక - రసాయన శాస్త్రాలు',
      assetPath: 'assets/data/physics_questions.json',
      icon: Icons.science_outlined,
      primaryColor: Color(0xFFE84393),
      accentColor: Color(0xFFFD79A8),
      totalQuestions: 240,
      description: 'Mechanics, Heat, Light, Electricity, Atomic Structure & Chemistry',
    ),
    Subject(
      id: 'biology',
      title: 'Biological Science',
      teluguTitle: 'వృక్ష & జంతు శాస్త్రాలు (జీవశాస్త్రం)',
      assetPath: 'assets/data/biology_questions.json',
      icon: Icons.eco_outlined,
      primaryColor: Color(0xFF00CEC9),
      accentColor: Color(0xFF81ECEC),
      totalQuestions: 240,
      description: 'Cell Biology, Human Anatomy, Ecology, Plant Systems & Genetics',
    ),
  ];

  static Subject? findById(String id) {
    for (final s in allSubjects) {
      if (s.id == id) return s;
    }
    return null;
  }
}
