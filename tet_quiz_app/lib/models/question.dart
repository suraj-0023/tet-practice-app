class Option {
  final int key;
  final String text;

  const Option({
    required this.key,
    required this.text,
  });

  factory Option.fromJson(Map<String, dynamic> json) {
    int parsedKey = 1;
    if (json['key'] is int) {
      parsedKey = json['key'];
    } else if (json['key'] is num) {
      parsedKey = (json['key'] as num).toInt();
    } else if (json['key'] is String) {
      parsedKey = int.tryParse(json['key']) ?? 1;
    }

    return Option(
      key: parsedKey,
      text: (json['text'] ?? '').toString().trim(),
    );
  }

  Map<String, dynamic> toJson() => {
    'key': key,
    'text': text,
  };
}

class Question {
  final int id;
  final String question;
  final List<Option> options;
  final int answer;
  final String? hint;
  final String? memoryTip;
  final String subjectId;
  final String subjectName;

  const Question({
    required this.id,
    required this.question,
    required this.options,
    required this.answer,
    this.hint,
    this.memoryTip,
    required this.subjectId,
    required this.subjectName,
  });

  factory Question.fromJson(
    Map<String, dynamic> json, {
    required String subjectId,
    required String subjectName,
  }) {
    int parsedId = 0;
    if (json['id'] is int) {
      parsedId = json['id'];
    } else if (json['id'] is num) {
      parsedId = (json['id'] as num).toInt();
    } else if (json['id'] is String) {
      parsedId = int.tryParse(json['id']) ?? 0;
    }

    int parsedAnswer = 1;
    if (json['answer'] is int) {
      parsedAnswer = json['answer'];
    } else if (json['answer'] is num) {
      parsedAnswer = (json['answer'] as num).toInt();
    } else if (json['answer'] is String) {
      parsedAnswer = int.tryParse(json['answer']) ?? 1;
    }

    List<Option> opts = [];
    if (json['options'] is List) {
      opts = (json['options'] as List)
          .map((item) => Option.fromJson(item as Map<String, dynamic>))
          .toList();
    }

    String? hintText;
    if (json['hint'] != null && json['hint'].toString().trim().isNotEmpty) {
      hintText = json['hint'].toString().trim();
    }

    String? tipText;
    if (json['memory_tip'] != null && json['memory_tip'].toString().trim().isNotEmpty) {
      tipText = json['memory_tip'].toString().trim();
    } else if (json['memoryTip'] != null && json['memoryTip'].toString().trim().isNotEmpty) {
      tipText = json['memoryTip'].toString().trim();
    }

    return Question(
      id: parsedId,
      question: (json['question'] ?? '').toString().trim(),
      options: opts,
      answer: parsedAnswer,
      hint: hintText,
      memoryTip: tipText,
      subjectId: subjectId,
      subjectName: subjectName,
    );
  }

  String get uniqueKey => '${subjectId}_$id';

  Map<String, dynamic> toJson() => {
    'id': id,
    'question': question,
    'options': options.map((o) => o.toJson()).toList(),
    'answer': answer,
    'hint': hint,
    'memory_tip': memoryTip,
    'subject_id': subjectId,
    'subject_name': subjectName,
  };

  Question copyWith({
    int? id,
    String? question,
    List<Option>? options,
    int? answer,
    String? hint,
    String? memoryTip,
    String? subjectId,
    String? subjectName,
  }) {
    return Question(
      id: id ?? this.id,
      question: question ?? this.question,
      options: options ?? this.options,
      answer: answer ?? this.answer,
      hint: hint ?? this.hint,
      memoryTip: memoryTip ?? this.memoryTip,
      subjectId: subjectId ?? this.subjectId,
      subjectName: subjectName ?? this.subjectName,
    );
  }
}
