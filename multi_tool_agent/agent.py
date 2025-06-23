from google.adk.agents import Agent
from . import prompt
import warnings

from google.adk.agents import SequentialAgent, LlmAgent

warnings.filterwarnings("ignore")

import logging
logging.basicConfig(level=logging.ERROR)

# if not hasattr(genai.models.Models.generate_content, '__wrapped__'):
#   genai.models.Models.generate_content = retry.Retry(
#       predicate=is_retriable)(genai.models.Models.generate_content)
  
MODEL = "gemini-2.5-flash"

user_interest_analysis_agent = Agent(
    model=MODEL,
    name="user_interest_analysis_agent",
    instruction=prompt.PERSONAL_INTEREST_PROMPT,
)

news_web_research_agent = Agent(
    model=MODEL,
    name="news_web_research_agent",
    instruction=prompt.NEWS_RESEARCH_PROMPT,
)

personal_news_script_agent = Agent(
    model=MODEL,
    name="personal_news_script_agent",
    instruction=prompt.PERSONAL_NEWS_SCRIPT_PROMPT,
)

# keywords are not extracted (only 2-3 words) - need to improve
# websearch should be inside and output should be all connected. 
# output all shows that they are crunching, not the output. fix the prompt overall
root_agent = SequentialAgent(name="news_generator_pipeline", sub_agents=[user_interest_analysis_agent, news_web_research_agent, personal_news_script_agent])







  