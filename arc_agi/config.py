import os

from arc_agi.prompts import (
    FEEDBACK_PROMPT,
    SOLVER_PROMPT_1,
    SOLVER_PROMPT_2,
    SOLVER_PROMPT_3,
)
from arc_agi.types import ExpertConfig, Models

# SLMs APPROACH

API_KEY: str = os.getenv(key="OPENROUTER_API_KEY")

SLM_MAPPING: dict[Models, int] = {
    # "openrouter/openai/gpt-oss-120b": 1,
    "openrouter/openai/gpt-oss-20b": 1,
    # "openrouter/ibm-granite/granite-4.0-h-micro": 1,
    # "openrouter/deepseek/deepseek-r1-0528-qwen3-8b": 1,
    # "openrouter/liquid/lfm2-8b-a1b": 1,
    # "openrouter/baidu/ernie-4.5-21b-a3b-thinking": 1,
}

CONFIG_LIST: list[ExpertConfig] = []

for selected_slm, num_experts in SLM_MAPPING.items():
    CONFIG_LIST.extend(
		[
			{
				# Prompts
				'solver_prompt': SOLVER_PROMPT_1,
				'feedback_prompt': FEEDBACK_PROMPT,
				# LLM parameters
				'llm_id': selected_slm,  # Used model name
				'solver_temperature': 1.0,  # Control the randomness of the output (higher values = higher variability, lower values == higher consistency)
				'request_timeout': 60 * 60,  # in seconds
				'max_total_timeouts': 15,  # per problem per solver
				'max_total_time': None,  # per problem per solver
				'per_iteration_retries': 2,
				# Solver parameters
				'num_experts': num_experts,  # NOT USED 
				'max_iterations': 10,
				'max_solutions': 5,
				'selection_probability': 1.0,
				'seed': 0,  # Seed for Random
				'shuffle_examples': True,
				'improving_order': True,
				'return_best_result': True,
				# Voting parameters
				'use_new_voting': True,
				'count_failed_matches': True,
				'iters_tiebreak': False,
				'low_to_high_iters': False,
			}
		] * num_experts
	)

# POETIQ APPROACH - ORIGINAL

# # To run Poetiq(Gemini-3-a):
# NUM_EXPERTS = 1
# # To run Poetiq(Gemini-3-b):
# # NUM_EXPERTS = 2
# # To run Poetiq(Gemini-3-c):
# # NUM_EXPERTS = 8

# CONFIG_LIST: list[ExpertConfig] = [
#   {
#     # Prompts
#     'solver_prompt': SOLVER_PROMPT_1,
#     'feedback_prompt': FEEDBACK_PROMPT,
#     # LLM parameters
#     'llm_id': 'gemini/gemini-3-pro-preview',
#     'solver_temperature': 1.0,
#     'request_timeout': 60 * 60, # in seconds
#     'max_total_timeouts': 15, # per problem per solver
#     'max_total_time': None, # per problem per solver
#     'per_iteration_retries': 2,
#     # Solver parameters
#     'num_experts': 1,
#     'max_iterations': 10,
#     'max_solutions': 5,
#     'selection_probability': 1.0,
#     'seed': 0,
#     'shuffle_examples': True,
#     'improving_order': True,
#     'return_best_result': True,
#     # Voting parameters
#     'use_new_voting': True,
#     'count_failed_matches': True,
#     'iters_tiebreak': False,
#     'low_to_high_iters': False,
#   },
# ] * NUM_EXPERTS

