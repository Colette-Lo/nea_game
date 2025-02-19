# using a graph to keep track of the game state
screen_graph = {
                "start_screen": ["initial_setup_screen", "home_page"],
                "initial_setup_screen": ["home_page"],
                "home_page": ["profile_screen", "scenario_decision_screen", "trade_screen", "technology_screen", "production_screen", "budget_screen", "resource_gathering_screen"],
                "scenario_decision_screen": ["scenario_news_screen"],
                "scenario_news_screen": ["home_page", "scenario_info_screen"],
                "scenario_info_screen": ["home_page"],
                "trade_screen": None,
                "technology_screen": None,
                "production_screen": None,
                "budget_screen": None,
                "resource_gathering_screen": None
}