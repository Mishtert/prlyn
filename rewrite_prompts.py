#!/usr/bin/env python3
"""
Rewrite prompts using prlyn's improvement template generator.
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from prlyn.analyzer import Analyzer  # noqa: E402
from prlyn.template_generator import generate_improvement_template  # noqa: E402

# System prompt
system_prompt = "You are QnA engine and must provide response to the question based on the content provided"

# User prompt
user_prompt = """Question or instruction is enclosed under @@## and @@## delimiters. Content to leverage to answer the question is enclosed under $$%% and $$%% delimiters. Do not return information about delimiters in the response. Answer only based on the provided content and do not hallucinate. If historical context is provided and some previous questions were unanswered, do not hallucinate or assume the current question is unanswerable. Instead, consider the full context available to generate an informed and coherent response. @@##*===question===*@@##. $$%%*===context===*$$%%."""


def main():
    analyzer = Analyzer()

    # Analyze and rewrite SYSTEM PROMPT
    print("=" * 80)
    print("SYSTEM PROMPT ANALYSIS")
    print("=" * 80)
    system_result = analyzer.analyze(system_prompt)
    system_template = generate_improvement_template(system_result)

    print("\n" + "=" * 80)
    print("SYSTEM PROMPT - IMPROVEMENT TEMPLATE")
    print("=" * 80)
    print(system_template)

    print("\n" + "=" * 80)
    print("SYSTEM PROMPT - REWRITTEN")
    print("=" * 80)
    rewritten_system = rewrite_system_prompt(system_result, system_prompt)
    print(rewritten_system)

    print("\n" + "=" * 80)
    print("SYSTEM PROMPT - VERIFICATION")
    print("=" * 80)
    rewritten_system_result = analyzer.analyze(rewritten_system)
    print(analyzer.report_generator.generate_table_report(rewritten_system_result))

    # Analyze and rewrite USER PROMPT
    print("\n\n" + "=" * 80)
    print("USER PROMPT ANALYSIS")
    print("=" * 80)
    user_result = analyzer.analyze(user_prompt)
    user_template = generate_improvement_template(user_result)

    print("\n" + "=" * 80)
    print("USER PROMPT - IMPROVEMENT TEMPLATE")
    print("=" * 80)
    print(user_template)

    print("\n" + "=" * 80)
    print("USER PROMPT - REWRITTEN")
    print("=" * 80)
    rewritten_user = rewrite_user_prompt(user_result, user_prompt)
    print(rewritten_user)

    print("\n" + "=" * 80)
    print("USER PROMPT - VERIFICATION")
    print("=" * 80)
    rewritten_user_result = analyzer.analyze(rewritten_user)
    print(analyzer.report_generator.generate_table_report(rewritten_user_result))


def rewrite_system_prompt(result, original: str) -> str:
    """
    Rewrite the system prompt applying improvements.
    """
    # System prompt is short - strengthen it based on analysis
    # Original: "You are QnA engine and must provide response to the question based on the content provided"
    # Issues: Low position score, low instruction strength

    # Strengthened version with clearer structure
    return "You are a QnA engine. Provide responses to questions using only the content provided."


def rewrite_user_prompt(result, original: str) -> str:
    """
    Rewrite the user prompt applying improvements from the analysis.
    Follows the template generator's recommendations.
    """
    # Reorganized user prompt following template recommendations:
    # 1. Move critical instructions to START
    # 2. Replace vague terms
    # 3. Remove hedging
    # 4. Strengthen verbs
    # 5. Improve flow

    rewritten = """Question or instruction is enclosed under @@## and @@## delimiters. Content to leverage to answer the question is enclosed under $$%% and $$%% delimiters.

Answer strictly using only the provided content. Ensure all information comes directly from the provided context. Return only the answer content, excluding any delimiter markers.

If historical context is provided and any previous questions were unanswered, use the full available context to provide a complete answer.

Format: @@##*===question===*@@##. $$%%*===context===*$$%%."""

    return rewritten


if __name__ == "__main__":
    main()
