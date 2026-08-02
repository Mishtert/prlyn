#!/usr/bin/env python3
"""
Analyze the recommended prompts using prlyn.
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from prlyn.analyzer import Analyzer  # noqa: E402
from prlyn.template_generator import generate_improvement_template  # noqa: E402

# Recommended System Prompt
system_prompt = """You are a QnA engine that provides comprehensive, accurate answers based on the provided content.
Your responses must be complete, including all relevant details, steps, specifications, and safety considerations from the context."""

# Recommended User Prompt
user_prompt = """Question or instruction: @@##*===question===*@@##

Context to leverage: $$%%*===context===*$$%%

Instructions:
- Answer comprehensively, including ALL relevant details from the context
- Do not omit important information, steps, specifications, or safety considerations
- Prioritize completeness and accuracy over brevity
- Structure your answer clearly with all relevant sections
- For procedural questions, provide complete step-by-step instructions
- Do not return information about delimiters in the response
- Answer only based on the provided content and do not hallucinate

*===history===*"""


def main():
    analyzer = Analyzer()

    # Analyze SYSTEM PROMPT
    print("=" * 80)
    print("SYSTEM PROMPT ANALYSIS")
    print("=" * 80)
    system_result = analyzer.analyze(system_prompt)
    print(analyzer.report_generator.generate_table_report(system_result))

    print("\n" + "=" * 80)
    print("SYSTEM PROMPT - DETAILED REPORT")
    print("=" * 80)
    print(analyzer.report_generator.generate_markdown_report(system_result))

    print("\n" + "=" * 80)
    print("SYSTEM PROMPT - IMPROVEMENT TEMPLATE")
    print("=" * 80)
    system_template = generate_improvement_template(system_result)
    print(system_template)

    # Analyze USER PROMPT
    print("\n\n" + "=" * 80)
    print("USER PROMPT ANALYSIS")
    print("=" * 80)
    user_result = analyzer.analyze(user_prompt)
    print(analyzer.report_generator.generate_table_report(user_result))

    print("\n" + "=" * 80)
    print("USER PROMPT - DETAILED REPORT")
    print("=" * 80)
    print(analyzer.report_generator.generate_markdown_report(user_result))

    print("\n" + "=" * 80)
    print("USER PROMPT - IMPROVEMENT TEMPLATE")
    print("=" * 80)
    user_template = generate_improvement_template(user_result)
    print(user_template)

    # Generate improved versions
    print("\n\n" + "=" * 80)
    print("RECOMMENDED IMPROVEMENTS")
    print("=" * 80)

    print("\n--- IMPROVED SYSTEM PROMPT ---")
    improved_system = improve_system_prompt(system_result, system_prompt)
    print(improved_system)

    print("\n--- IMPROVED USER PROMPT ---")
    improved_user = improve_user_prompt(user_result, user_prompt)
    print(improved_user)

    # Verify improvements
    print("\n\n" + "=" * 80)
    print("VERIFICATION - IMPROVED SYSTEM PROMPT")
    print("=" * 80)
    improved_system_result = analyzer.analyze(improved_system)
    print(analyzer.report_generator.generate_table_report(improved_system_result))

    print("\n" + "=" * 80)
    print("VERIFICATION - IMPROVED USER PROMPT")
    print("=" * 80)
    improved_user_result = analyzer.analyze(improved_user)
    print(analyzer.report_generator.generate_table_report(improved_user_result))


def improve_system_prompt(result, original: str) -> str:
    """Apply improvements to system prompt based on analysis."""
    # Simplify, improve readability, strengthen verbs
    return """You are a QnA engine. Answer questions using only the provided content. Include all details, steps, and safety information."""


def improve_user_prompt(result, original: str) -> str:
    """Apply improvements to user prompt based on analysis."""
    # Reframe negatives, simplify language, improve readability
    return """Question: @@##*===question===*@@##

Context: $$%%*===context===*$$%%

Instructions:
- Include all relevant details from the context
- Include all important information, steps, specifications, and safety considerations
- Prioritize completeness and accuracy over brevity
- Structure your answer clearly with all relevant sections
- For procedural questions, provide complete step-by-step instructions
- Return only the answer content, excluding delimiter markers
- Use only the provided content

*===history===*"""


if __name__ == "__main__":
    main()
