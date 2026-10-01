import 'package:flutter/material.dart';

class HintTipWidget extends StatefulWidget {
  final String? hint;
  final String? memoryTip;
  final bool initialShowHint;
  final bool initialShowTip;
  final ValueChanged<bool>? onHintToggled;
  final ValueChanged<bool>? onTipToggled;

  const HintTipWidget({
    super.key,
    this.hint,
    this.memoryTip,
    this.initialShowHint = false,
    this.initialShowTip = false,
    this.onHintToggled,
    this.onTipToggled,
  });

  @override
  State<HintTipWidget> createState() => _HintTipWidgetState();
}

class _HintTipWidgetState extends State<HintTipWidget> {
  late bool _showHint;
  late bool _showTip;

  @override
  void initState() {
    super.initState();
    _showHint = widget.initialShowHint;
    _showTip = widget.initialShowTip;
  }

  @override
  void didUpdateWidget(covariant HintTipWidget oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.hint != widget.hint || oldWidget.memoryTip != widget.memoryTip) {
      _showHint = widget.initialShowHint;
      _showTip = widget.initialShowTip;
    }
  }

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final isDark = theme.brightness == Brightness.dark;

    final hasHint = widget.hint != null && widget.hint!.trim().isNotEmpty;
    final hasTip = widget.memoryTip != null && widget.memoryTip!.trim().isNotEmpty;

    if (!hasHint && !hasTip) {
      return const SizedBox.shrink();
    }

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        const SizedBox(height: 16),
        const Divider(height: 1, color: Color(0xFFE2E8F0)),
        const SizedBox(height: 12),

        // Hint Button & Expandable Card
        if (hasHint) ...[
          _buildToggleButton(
            context: context,
            icon: Icons.lightbulb_outline_rounded,
            label: 'Hint (సూచన)',
            isExpanded: _showHint,
            activeColor: const Color(0xFFD97706),
            backgroundColor: isDark ? const Color(0xFF451A03) : const Color(0xFFFEF3C7),
            onTap: () {
              setState(() => _showHint = !_showHint);
              widget.onHintToggled?.call(_showHint);
            },
          ),
          AnimatedCrossFade(
            firstChild: const SizedBox(width: double.infinity),
            secondChild: Container(
              margin: const EdgeInsets.only(top: 8, bottom: 8),
              padding: const EdgeInsets.all(14),
              decoration: BoxDecoration(
                color: isDark ? const Color(0xFF272115) : const Color(0xFFFFFBEB),
                borderRadius: BorderRadius.circular(12),
                border: Border.all(
                  color: isDark ? const Color(0xFF78350F) : const Color(0xFFFDE68A),
                  width: 1.2,
                ),
              ),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Icon(
                    Icons.lightbulb_rounded,
                    size: 20,
                    color: Color(0xFFD97706),
                  ),
                  const SizedBox(width: 10),
                  Expanded(
                    child: Text(
                      widget.hint!,
                      style: TextStyle(
                        fontSize: 14.5,
                        height: 1.5,
                        color: isDark ? const Color(0xFFFDE68A) : const Color(0xFF92400E),
                        fontWeight: FontWeight.w500,
                      ),
                    ),
                  ),
                ],
              ),
            ),
            crossFadeState: _showHint ? CrossFadeState.showSecond : CrossFadeState.showFirst,
            duration: const Duration(milliseconds: 200),
          ),
        ],

        const SizedBox(height: 8),

        // Tip to Remember Button & Expandable Card
        if (hasTip) ...[
          _buildToggleButton(
            context: context,
            icon: Icons.psychology_alt_outlined,
            label: 'Tip to Remember / Formula (కీలక అంశం)',
            isExpanded: _showTip,
            activeColor: const Color(0xFF7C3AED),
            backgroundColor: isDark ? const Color(0xFF2E1065) : const Color(0xFFEDE9FE),
            onTap: () {
              setState(() => _showTip = !_showTip);
              widget.onTipToggled?.call(_showTip);
            },
          ),
          AnimatedCrossFade(
            firstChild: const SizedBox(width: double.infinity),
            secondChild: Container(
              margin: const EdgeInsets.only(top: 8, bottom: 8),
              padding: const EdgeInsets.all(14),
              decoration: BoxDecoration(
                color: isDark ? const Color(0xFF221738) : const Color(0xFFF5F3FF),
                borderRadius: BorderRadius.circular(12),
                border: Border.all(
                  color: isDark ? const Color(0xFF5B21B6) : const Color(0xFFDDD6FE),
                  width: 1.2,
                ),
              ),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Icon(
                    Icons.auto_awesome_rounded,
                    size: 20,
                    color: Color(0xFF7C3AED),
                  ),
                  const SizedBox(width: 10),
                  Expanded(
                    child: Text(
                      widget.memoryTip!,
                      style: TextStyle(
                        fontSize: 14.5,
                        height: 1.5,
                        color: isDark ? const Color(0xFFDDD6FE) : const Color(0xFF5B21B6),
                        fontWeight: FontWeight.w500,
                      ),
                    ),
                  ),
                ],
              ),
            ),
            crossFadeState: _showTip ? CrossFadeState.showSecond : CrossFadeState.showFirst,
            duration: const Duration(milliseconds: 200),
          ),
        ],
      ],
    );
  }

  Widget _buildToggleButton({
    required BuildContext context,
    required IconData icon,
    required String label,
    required bool isExpanded,
    required Color activeColor,
    required Color backgroundColor,
    required VoidCallback onTap,
  }) {
    final theme = Theme.of(context);
    final isDark = theme.brightness == Brightness.dark;

    return Material(
      color: Colors.transparent,
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(10),
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
          decoration: BoxDecoration(
            color: isExpanded ? backgroundColor : (isDark ? const Color(0xFF334155) : const Color(0xFFF1F5F9)),
            borderRadius: BorderRadius.circular(10),
            border: Border.all(
              color: isExpanded ? activeColor.withValues(alpha: 0.5) : (isDark ? const Color(0xFF475569) : const Color(0xFFCBD5E1)),
              width: 1,
            ),
          ),
          child: Row(
            children: [
              Icon(
                icon,
                size: 18,
                color: isExpanded ? activeColor : (isDark ? const Color(0xFF94A3B8) : const Color(0xFF64748B)),
              ),
              const SizedBox(width: 8),
              Expanded(
                child: Text(
                  label,
                  style: TextStyle(
                    fontSize: 13.5,
                    fontWeight: FontWeight.w600,
                    color: isExpanded ? activeColor : (isDark ? const Color(0xFFE2E8F0) : const Color(0xFF334155)),
                  ),
                ),
              ),
              Text(
                isExpanded ? 'Hide' : 'Click to View',
                style: TextStyle(
                  fontSize: 12,
                  fontWeight: FontWeight.w600,
                  color: isExpanded ? activeColor : (isDark ? const Color(0xFF94A3B8) : const Color(0xFF64748B)),
                ),
              ),
              const SizedBox(width: 4),
              Icon(
                isExpanded ? Icons.keyboard_arrow_up_rounded : Icons.keyboard_arrow_down_rounded,
                size: 18,
                color: isExpanded ? activeColor : (isDark ? const Color(0xFF94A3B8) : const Color(0xFF64748B)),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
