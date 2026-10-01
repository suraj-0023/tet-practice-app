import 'package:flutter_test/flutter_test.dart';
import 'package:tet_quiz_app/main.dart';

void main() {
  testWidgets('App launches smoke test', (WidgetTester tester) async {
    await tester.pumpWidget(const TetQuizApp());
    expect(find.byType(TetQuizApp), findsOneWidget);
  });
}
